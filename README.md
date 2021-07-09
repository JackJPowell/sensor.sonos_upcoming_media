# Sonos Upcoming Media Component

Home Assistant component to feed [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card) with your Sonos Queue.</br></br>
This component displays your Sonos Queue, not the queue of media that may be playing through your Sonos. As an example, if you are airplaying to your sonos or steaming to it over spotify connect, those queues will not be displayed in this component.</br>
This component does not require, nor conflict with, the default Sonos component.</br></br>
### Issues
Read through these two resources before posting issues to GitHub or the forums.
* [troubleshooting guide](https://github.com/custom-cards/upcoming-media-card/blob/master/troubleshooting.md)
* [@thomasloven's lovelace guide](https://github.com/thomasloven/hass-config/wiki/Lovelace-Plugins).

## Installation:

1. Install this component by copying [these files](https://github.com/JackJPowell/sensor.sonos_upcoming_media/tree/main/custom-components) to `/custom_components/sonos_upcoming_media/`.
2. Install the card: [Upcoming Media Card](https://github.com/custom-cards/upcoming-media-card)
3. Add the code to your `configuration.yaml` using the config options below.
4. Add the code for the card to your `ui-lovelace.yaml`. 
5. **You will need to restart after installation for the component to start working.**

| key | default | required | description
| --- | --- | --- | ---
| ip | | yes | Your Sonos IP
| max | 3 | no | Max number of items in sensor.
</br>

### Sample for configuration.yaml:

```
sensor:
  - platform: sonos_upcoming_media
    ip: 192.168.1.200
    max: 4
```

### Sample for ui-lovelace.yaml:

    - type: custom:upcoming-media-card
      entity: sensor.sonos_upcoming_media
      title: Sonos Queue
      
      
### Card Content Defaults:

| key | default | example |
| --- | --- | --- |
| title | $title | "You Can Call Me Al" |
| line1 | $genres | "Paul Simon" |
| line2 | $episode | "Graceland"|
| line3 | $empty  | |
| line4 | $empty | |
| icon | mdi:speaker | https://materialdesignicons.com/icon/speaker
