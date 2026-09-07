"""An automation project that reads a CSV file and registers products in a system."""

import os
import time

import pandas as pd
import pyautogui as gui

SLEEP_TIME = 3
BROWSER = "chrome"
BROWSER_MULTIUSER = True
CREDS = {"email": "mr.employee.man@gmail.com", "password": "strongpassword123"}
APP_PATH = "../../resources/dummy-app/login.html"
TABLE_PATH = "resources/spreadsheets/sample-products.csv"


def main():  # pylint: disable=missing-function-docstring
    _open_browser(BROWSER)

    _navigate_to_new_window(multiprofile=BROWSER_MULTIUSER)

    current_abs_path = os.path.dirname(os.path.abspath(__file__))
    app_abs_path = os.path.join(current_abs_path, APP_PATH)
    _open_website(app_abs_path)

    _log_in(CREDS["email"], CREDS["password"])

    table = pd.read_csv(TABLE_PATH)

    for line in table.index:
        _register_product(table, line)
        _rollback()


def _open_browser(browser: str) -> None:
    gui.press("win")
    time.sleep(SLEEP_TIME)

    gui.write(browser)
    gui.press("enter")
    time.sleep(SLEEP_TIME)


def _navigate_to_new_window(multiprofile: bool = False) -> None:
    if multiprofile:
        gui.press("tab")
        gui.press("enter")
        time.sleep(SLEEP_TIME)

    gui.hotkey("ctrl", "n")
    time.sleep(SLEEP_TIME)


def _open_website(url: str) -> None:
    gui.write(url)
    gui.press("enter")

    time.sleep(SLEEP_TIME)


def _log_in(email: str, password: str) -> None:
    gui.press("tab")
    gui.write(email)

    gui.press("tab")
    gui.write(password)

    gui.press("tab")
    gui.press("enter")

    time.sleep(SLEEP_TIME)


def _register_product(table: pd.DataFrame, prod_line: int) -> None:
    for column in table.columns:
        gui.press("tab")

        value = table.loc[prod_line, column]
        if not pd.isna(value):
            gui.write(str(value))

    gui.press("tab")
    gui.press("enter")


def _rollback() -> None:
    # it'd probably be faster using scroll and click
    for _ in range(8):
        gui.hotkey("shift", "tab")
