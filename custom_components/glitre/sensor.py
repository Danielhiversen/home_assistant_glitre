"""Glitre data"""
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import DOMAIN, SENSORS
from .data_coordinator import GlitreDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass: HomeAssistant, _, async_add_entities, config):
    """Set up the Glitre sensor."""
    hass.data[DOMAIN] = {}
    metering_point_id = config["metering_point_id"]
    api_key = config["api_key"]
    coordinator = GlitreDataUpdateCoordinator(hass, metering_point_id, api_key)

    async_add_entities(
        GlitreDataSensor(coordinator, description) for description in SENSORS
    )


class GlitreDataSensor(SensorEntity, CoordinatorEntity["GlitreDataUpdateCoordinator"]):
    """Representation of a Glitre sensor."""

    def __init__(self, coordinator, entity_description):
        """Initialize the sensor."""
        super().__init__(coordinator=coordinator)
        self.entity_description = entity_description
        self._attr_unique_id = (
            f"{coordinator.metering_point_id}_{entity_description.key}"
        )

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        if self.entity_description.key == "forbruksledd":
            self._attr_native_value = self.coordinator.data["forbruksledd"][
                dt_util.utcnow().replace(minute=0, second=0, microsecond=0)
            ]
        else:
            self._attr_native_value = self.coordinator.data.get(
                self.entity_description.key
            )
        self.async_write_ha_state()
