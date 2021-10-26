import importlib


class PluginInterface:
    """Used to initialize plugins"""

    @staticmethod
    def initialize() -> None:
        """Initialize the plugin"""


def import_module(name: str) -> PluginInterface:
    """Imports a module"""
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Load the plugins defined in the list"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
