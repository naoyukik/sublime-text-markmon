import sublime
import time
import sublime_plugin
import webbrowser
import subprocess
import atexit
import re
from .MarkmonListener import MarkmonListener
import http.client
from . import util, markmon
import os

class MarkmonToggleCommand(sublime_plugin.WindowCommand):
    def __init__(self, window):
        """Initialize a new instance."""
        super().__init__(window)
        self.server = None

    def run(self, **args):
        if args['enable']:
            markmon.markmon.set_running(True)
        else:
            markmon.markmon.set_running(False)

    def is_enabled(self):
        return True