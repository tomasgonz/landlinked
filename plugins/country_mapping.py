"""Country code mapping utilities for M49 ↔ ISO conversions.

Used by UN SDG and FAOSTAT plugins which use M49 numeric codes
instead of ISO alpha codes.
"""

import json
import os

_COUNTRY_CODES_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "cache", "Countrycodesfull.json"
)

_m49_to_iso = None
_iso3_to_m49 = None


def _load():
    global _m49_to_iso, _iso3_to_m49
    if _m49_to_iso is not None:
        return

    with open(_COUNTRY_CODES_PATH, "r", encoding="utf-8") as f:
        codes = json.load(f)

    _m49_to_iso = {}
    _iso3_to_m49 = {}

    for entry in codes:
        m49 = entry.get("M49")
        iso2 = entry.get("ISO_3166_2", "")
        iso3 = entry.get("ISO_3166_3", "")
        name = entry.get("NAME.EN", "")

        if m49 and iso2 and iso3:
            m49_int = int(m49)
            _m49_to_iso[m49_int] = {"iso2": iso2, "iso3": iso3, "name": name}
            _iso3_to_m49[iso3] = m49_int


def build_m49_to_iso_map():
    """Return {m49_int: {'iso2': str, 'iso3': str, 'name': str}}."""
    _load()
    return _m49_to_iso


def build_iso3_to_m49_map():
    """Return {iso3_str: m49_int}."""
    _load()
    return _iso3_to_m49
