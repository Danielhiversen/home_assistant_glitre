# Glitre Data :zap: 
[![Validate with hassfest](https://github.com/Danielhiversen/home_assistant_glitre/workflows/Validate%20with%20hassfest/badge.svg)
[![GitHub Release][releases-shield]][releases]
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Display Glitre price sensor.

[Buy me a coffee :)](http://paypal.me/dahoiv)

You get the following sensors:
* Forbruksledd kr/kWh



## Install

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Danielhiversen&repository=home_assistant_glitre&category=integration)

## Configuration 

In configuration.yaml:

```
glitre:
  metering_point_id: XXXXX
  api_key: XXXX # https://www.glitreenergi-nett.no/kunde/ny-nettleie/api-for-nettleiepriser/

```

[releases]: https://github.com/Danielhiversen/home_assistant_glitre/releases
[releases-shield]: https://img.shields.io/github/release/Danielhiversen/home_assistant_glitre.svg?style=popout
[downloads-total-shield]: https://img.shields.io/github/downloads/Danielhiversen/home_assistant_glitre/total
[hacs-shield]: https://img.shields.io/badge/HACS-Default-orange.svg
[hacs]: https://hacs.xyz/docs/default_repositories
