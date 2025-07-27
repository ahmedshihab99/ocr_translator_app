from pynput import keyboard
from utils.config import HOTKEY

class HotkeyListener:
    def __init__(self, on_activate):
        self.on_activate = on_activate
        self.hotkey = keyboard.HotKey(
            keyboard.HotKey.parse(HOTKEY),
            self.on_activate
        )
        self.listener = keyboard.Listener(
            on_press=self.for_canonical(self.hotkey.press),
            on_release=self.for_canonical(self.hotkey.release)
        )

    def for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    def start(self):
        self.listener.start()
        
