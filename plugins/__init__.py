"""Data source plugin registry.

Maps source names to plugin classes and provides helpers
to instantiate all plugins for a given indicator catalogue.
"""

from plugins.worldbank import WorldBankPlugin
from plugins.unsdg import UNSDGPlugin
from plugins.faostat import FAOSTATPlugin
from plugins.imf import IMFPlugin

PLUGIN_CLASSES = {
    "World Bank": WorldBankPlugin,
    "UN SDG": UNSDGPlugin,
    "FAOSTAT": FAOSTATPlugin,
    "IMF": IMFPlugin,
}


def get_all_plugins(indicators_dict, **kwargs):
    """Return a list of instantiated plugin objects for all registered sources.

    Only plugins that have at least one matching indicator are returned.
    """
    plugins = []
    for name, cls in PLUGIN_CLASSES.items():
        plugin = cls(indicators_dict, **kwargs)
        if plugin.indicators:
            plugins.append(plugin)
    return plugins
