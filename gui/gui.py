from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

import subprocess
import argparse
import colorama
import libconfig
import datetime
import loglib
import time
import sys

class UserInterface(FloatLayout):
    def __init__(self, **kwargs):
        super(UserInterface, self).__init__(**kwargs)

class StegbruteApp(App):
    def build(self):
        self.load_kv("style.kv")
        return UserInterface()

StegbruteApp().run()