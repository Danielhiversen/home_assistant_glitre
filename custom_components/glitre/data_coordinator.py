"""Data coordinator for Tibber."""
import datetime
import logging

from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.event import async_track_point_in_utc_time
from homeassistant.util import dt as dt_util

from .glitre_api import get_glitre_forbruksledd_data

_LOGGER = logging.getLogger(__name__)


class GlitreDataUpdateCoordinator(DataUpdateCoordinator):
    """Handle Glitre data."""

    def __init__(self, hass, metering_point_id: str, api_key: str):
        """Initialize the data handler."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"Glitre Data {metering_point_id}",
            update_interval=None,
        )
        self.metering_point_id = metering_point_id
        self._api_key = api_key

        self._session = async_get_clientsession(hass)

    async def _async_update_data(self):
        """Update data via API."""
        data = {} if self.data is None else self.data
        print(dt_util.now(dt_util.DEFAULT_TIME_ZONE))
        try:
            data["forbruksledd"] = await get_glitre_forbruksledd_data(
                self._session, self.metering_point_id, self._api_key
            )
            print(data["forbruksledd"])
        except Exception:  # pylint: disable=broad-except
            _LOGGER.exception("Error fetching Glitre data")
        now = dt_util.utcnow()

        self._unsub_refresh = async_track_point_in_utc_time(
            self.hass,
            self._job,
            dt_util.utcnow().replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1) ,
        )
        return data
