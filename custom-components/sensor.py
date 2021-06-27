"""
Home Assistant component to feed the Upcoming Media Lovelace card with
Sonos Play Queue.
https://github.com/custom-cards/upcoming-media-card
"""
import logging
import json
import requests
import datetime
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
from .soco import SoCo

__version__ = '0.1'

_LOGGER = logging.getLogger(__name__)

CONF_IP = 'ip'
CONF_MAX = 'max'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_IP): cv.string,
    vol.Optional(CONF_MAX, default='3'): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([SonosUpcomingMediaSensor(hass, config)], True)

class SonosUpcomingMediaSensor(Entity):

    def __init__(self, hass, conf):
        self.ip = conf.get(CONF_IP)
        self._state = None
        self.data = []
        self.max_items = int(conf.get(CONF_MAX))

    @property
    def name(self):
        return 'Sonos_Upcoming_Media'

    @property
    def state(self):
        return self._state

    @property
    def device_state_attributes(self):
        import re
        """Return JSON for the sensor."""
        attributes = {}
        default = {}
        card_json = []
        default['title_default'] = '$title'
        default['line1_default'] = '$genres'
        default['line2_default'] = '$episode'
        default['line3_default'] = '$empty'
        default['line4_default'] = '$empty'
        default['icon'] = 'mdi:speaker'
        card_json.append(default)
        basetime = datetime.datetime.now()
        for index, item in enumerate(self.data):
            airtime = basetime + datetime.timedelta(seconds=index)
            card_item = {}
            card_item['airdate'] = airtime.isoformat()
            card_item['title'] = item.title
            card_item['episode'] = item.album
            card_item['genres'] = item.creator
            
            
            try:
                card_item['poster'] = re.sub('.jpg', '_t.jpg', item.album_art_uri)
                card_item['fanart'] = re.sub('.jpg', '_t.jpg', item.album_art_uri)
            except:
                continue

            card_json.append(card_item)
        attributes['data'] = card_json
        return attributes

    def update(self):
        try:
            speaker = SoCo(self.ip)
            queue = speaker.get_queue(0,self.max_items,True)
        except OSError:
            _LOGGER.warning("Host %s is not available", self.ip)
            self._state = '%s cannot be reached' % self.ip
            return

        if len("test") > 0:
            self._state = 'Online'
            self.data = queue
        else:
            self._state = '%s cannot be reached' % self.ip