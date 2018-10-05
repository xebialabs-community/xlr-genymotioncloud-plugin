from subprocess import check_output, check_call, STDOUT, CalledProcessError
import os
import sys


class Gmtool:
    instance = None

    def __init__(self):
        if sys.platform.startswith("win32"):
            self.gmtool = "gmtool.exe"
        else:
            self.gmtool = "gmtool"

    def connect(self, email, password):
        cmd = [self.gmtool, "config", "username", email, "password", password]
        try:
            output = check_output(cmd).decode("utf-8").strip()
            return output
        except CalledProcessError as e:
            raise Exception(str(e))

    def register_license(self, license_key):
        cmd = [self.gmtool, "license", "register", license_key]
        try:
            output = check_output(cmd).decode("utf-8").strip()
            return output
        except CalledProcessError as e:
            raise Exception(str(e))

    def start_device(self, template, device_name, adb_serial_port=None):
        """Use gmtool in order to add a cloud device with the arguments passed.
            """
        if adb_serial_port is None:
            cmd = [
                self.gmtool,
                "--cloud",
                "admin",
                "startdisposable",
                template,
                device_name,
            ]
        else:
            cmd = [
                self.gmtool,
                "--cloud",
                "admin",
                "startdisposable",
                template,
                device_name,
                "--adb-serial-port",
                adb_serial_port,
            ]

        try:
            output = check_output(cmd).decode("utf-8").strip()
            return output
        except CalledProcessError as e:
            raise Exception(str(e))

    def stop_device(self, device_name):
        """Use gmtool in order to stop a cloud device with the arguments passed.
            """
        cmd = [self.gmtool, "--cloud", "admin", "stopdisposable", device_name]

        try:
            output = check_output(cmd).decode("utf-8").strip()
            return output
        except CalledProcessError as e:
            raise Exception(str(e))
