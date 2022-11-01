"""constants for Tibber integration."""

from homeassistant.components.sensor import (
    SensorEntityDescription,
    SensorStateClass,
)

DOMAIN = "glitre"

SENSORS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="forbruksledd",
        name="Pris forbruksledd",
        icon="mdi:currency-usd",
        native_unit_of_measurement="NOK/kWh",
        state_class=SensorStateClass.MEASUREMENT,
    ),
)
