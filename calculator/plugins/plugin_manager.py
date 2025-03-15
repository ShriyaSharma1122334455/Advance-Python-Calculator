"""
Plugin Manager module.

This module provides the PluginManager class, which is responsible for loading
and managing plugins in the application. Plugins can be dynamically loaded and
registered using this class.
"""

import importlib

class PluginManager:
    """
    PluginManager class to manage plugins.

    This class allows loading and registering plugins. It provides functionality
    to load plugins dynamically by name and register them with a plugin name 
    and associated function.
    """

    def __init__(self):
        """
        Initializes the PluginManager with an empty plugins dictionary.

        The dictionary will hold the loaded plugins, with plugin names as keys
        and the plugin functions as values.
        """
        self.plugins = {}

    def load_plugin(self, plugin_name):
        """
        Loads a plugin dynamically by name.

        This method attempts to load a plugin module by its name using 
        importlib and adds it to the `self.plugins` dictionary if successful.

        Args:
            plugin_name (str): The name of the plugin to load.

        Prints an error message if the plugin fails to load.
        """
        try:
            plugin_module = importlib.import_module(plugin_name)
            self.plugins[plugin_name] = plugin_module.plugin
        except ImportError:
            print(f"Error loading plugin {plugin_name}")

    def register_plugin(self, plugin_name, plugin_func):
        """
        Registers a plugin manually.

        This method allows registering a plugin with a given name and function.

        Args:
            plugin_name (str): The name of the plugin to register.
            plugin_func (function): The function to associate with the plugin.
        """
        self.plugins[plugin_name] = plugin_func
