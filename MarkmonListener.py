import sublime
import sublime_plugin

class MarkmonListener(sublime_plugin.EventListener):
    @classmethod
    def shared_plugin(cls):
        """Return the plugin instance."""
        return cls.shared_instance

    def __init__(self, *args, **kwargs):
        """Initialize a new instance."""
        super().__init__(*args, **kwargs)

        self.settings = None
        self.on_setting_change_callbacks = []
        self.on_modified_callbacks = []

        self.__class__.shared_instance = self


    def add_on_settings_change(self, callback):
        self.on_setting_change_callbacks.append(callback)
        callback(self.settings)

    def add_on_modified(self, callback):
        self.on_modified_callbacks.append(callback)

    def load_settings(self):
        self.settings = sublime.load_settings('sublime-text-markmon.sublime-settings')
        self.settings.add_on_change("*", self.settings_updated)

    def settings_updated(self):
        for callback in self.on_setting_change_callbacks:
            callback(self.settings)

    def on_modified_async(self, view):
        for callback in self.on_modified_callbacks:
            callback(view)

    def on_activated_async(self, view):
        for callback in self.on_modified_callbacks:
            callback(view)
