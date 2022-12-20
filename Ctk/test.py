def import_files():

    import main
    import creation_window
    import credit
    import database
    import join_window
    import main_window
    import opening_window
    import room
    import user
    import window
    import error_window
    import audio_player


import customtkinter
import sys

from timeit import repeat
from random import randint


ARRAY_LENTH = 1_000_000

sys.setrecursionlimit(10000)


def run_sorting_algorithm(file, algorithm, array):
    setup_code = f"from {file} import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution: {min(times)}")


class TestWindow(customtkinter.CTk):

    customtkinter.set_default_color_theme("dark-blue")
    customtkinter.set_appearance_mode("dark")

    def __init__(self, *args, **kwargs):
        super(TestWindow, self).__init__(*args, **kwargs)

        self.geometry("720x480")
        self.title("TestWindow")

        self.current_window = None

    def set_current_window(self, elt: object):
        self.current_window = elt
        self.current_window.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    array = [randint(0, 1_000) for i in range(ARRAY_LENTH)]
    run_sorting_algorithm(file="audio_player", algorithm="quick_sort", array=array)
