import sys
import logging
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from hotkey_listener import HotkeyListener
from gui import ScreenshotWindow


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

class HotkeyThread(QThread):
    """Runs the hotkey listener in a separate thread to avoid blocking the GUI."""
    def __init__(self, hotkey_listener):
        super().__init__()
        self.hotkey_listener = hotkey_listener

    def run(self):
        # The start() method is non-blocking. join() will block this thread
        # until the listener is stopped, keeping the thread alive.
        self.hotkey_listener.start()
        self.hotkey_listener.listener.join()

class MainController(QObject):
    """Uses signals to communicate from the hotkey thread to the main GUI thread."""
    trigger_screenshot_signal = pyqtSignal()

def main():
    """Initializes and runs the application."""
    app = QApplication(sys.argv)
    
    # This prevents the app from quitting when the overlay/screenshot windows are closed
    app.setQuitOnLastWindowClosed(False)

    controller = MainController()
    
    # We create a single instance of the screenshot window and reuse it for performance.
    screenshot_window = ScreenshotWindow()
    
    def on_screenshot_triggered():
        """This function runs in the main thread and shows the screenshot window."""
        logging.info("Signal received, triggering screenshot window.")
        screenshot_window.start_selection()

    # Connect the signal from the controller to the function that shows the window.
    controller.trigger_screenshot_signal.connect(on_screenshot_triggered)
    
    def hotkey_callback():
        """This callback is executed by the hotkey listener in its thread."""
        logging.info("Hotkey pressed, emitting signal to main thread.")
        # Emit the signal. This is a thread-safe operation.
        controller.trigger_screenshot_signal.emit()

    # Setup and start the hotkey listener in its own thread.
    hotkey_listener = HotkeyListener(hotkey_callback)
    hotkey_thread = HotkeyThread(hotkey_listener)
    hotkey_thread.start()

    logging.info("Application started. Press Ctrl+Shift+X to capture.")
    print("Application is running. Press Ctrl+Shift+X to capture a screen area.")
    print("Close this console window to exit the application.")

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())