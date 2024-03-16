import datetime
import os
from os.path import isfile
"""
Generates log files.
Constructor params:
 - log_name, default is 'default.log'
 - log_location, default is ''
 - log_dir, default is '', if not empty will create a folder for log files
and will update log_location
"""


class Logs:
    log_name = ""
    log_name_full = ""
    log_location = ""
    log_dir = ""

    def __init__(self, log_name="default.log", log_location="", log_dir=""):
        self.log_dir = log_dir
        if log_location == "":
            self.get_location()
        else:
            self.log_location = log_location
        if log_dir != "":
            self.create_dir()
        self.log_name = log_name
        self.log_name_full = os.path.join(self.log_location, self.log_name)
        self.create_file()

    def get_location(self):
        self.log_location = os.path.dirname(__file__)

    def show_location(self):
        print(self.log_location)

    def create_dir(self):
        path = os.path.join(self.log_location, self.log_dir)
        if not os.path.isdir(path):
            os.mkdir(path)
        self.log_location = path

    def create_file(self):
        if not isfile(self.log_name_full):
            with open(self.log_name_full, 'w') as file:
                file.write('')

    @staticmethod
    def get_date():
        d = datetime.datetime.now()
        return f"{d.day}-{d.month}-{d.year} {d.hour}:{d.minute}:{d.second}"

    def write(self, msg):
        with open(self.log_name_full, 'a') as file:
            file.write(f"{self.get_date()} - {msg} \n")
