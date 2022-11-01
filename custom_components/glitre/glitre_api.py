"""Helpers for the Glitre integration."""
import json
import logging

from homeassistant.util import dt as dt_util

GLITRE_API_URL = "https://apigw.glitreenergi-nett.no/api/nettleie-for-styring/"

_LOGGER = logging.getLogger(__name__)


async def get_glitre_forbruksledd_data(session, metering_point_id: str, api_key: str):
    """Get glitre data."""
    post_args = {
        "headers": {
            "content-type": "application/json",
            "X-API-Key": api_key,
        },
        "data": json.dumps({"range": "today", "meteringPointIds": [metering_point_id]}),
    }
    resp = await session.post(
        GLITRE_API_URL + "api/1/tariffquery/meteringpointsgridtariffs", **post_args
    )
    json_resp = await resp.json()
    grid_tariff = json_resp["gridTariffCollections"][0]["gridTariff"]
    res = {}
    for val in grid_tariff["tariffPrice"]["hours"]:
        res[dt_util.parse_datetime(val["startTime"]).astimezone(dt_util.UTC)] = val[
            "energyPrice"
        ].get("total", 0)
    return res
