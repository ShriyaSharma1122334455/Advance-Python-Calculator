# calculator/plugins/plugin_manager.py
import importlib

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name):
        try:
            plugin_module = importlib.import_module(plugin_name)
            self.plugins[plugin_name] = plugin_module.plugin
        except ImportError:
            print(f"Error loading plugin {plugin_name}")

    def register_plugin(self, plugin_name, plugin_func):
        self.plugins[plugin_name] = plugin_func