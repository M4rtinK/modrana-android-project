#!/usr/bin/env python

# A simple PySide example

import sys
import os
import traceback

import android_util
from android_util import log

APP_DIR = os.path.dirname(os.path.abspath(__file__))


def run_app():
    """Start and show the app."""

    log("Starting modRana !!!")
    log(sys.argv)
    pth = "/data/data/org.modrana.modrana/files/app/modrana"
    log(pth)
    os.chdir(pth)
    sys.path.append(pth)
    #sys.argv.append('-d')
    #sys.argv.append('pc')
    sys.argv.append('-u')
    sys.argv.append('QML')
    sys.argv = ["pth" + "modrana.py", "-d", "android", "-u", "QML"]
    #sys.argv = ["pth" + "modrana.py", "-u", "QML"]
    from modrana import ModRana
    ModRana()

def main():
    """
    Start the app.
    If we are on an android device, setup the logging first.
    """
    os.chdir(APP_DIR)
    if android_util.is_on_android:
        log_file = os.path.join(os.environ['LOG_DIR'], 'python_log.txt')

        # Redirect stdout and stderr to a file on /sdcard/
        with open(log_file, 'w', 1) as fSock:
            sys.stdout = fSock
            sys.stderr = fSock
            try:
                run_app()
            except Exception:
                traceback.print_exc(file=fSock)
        exit(0)

    else:
        run_app()


if __name__ == '__main__':
    main()
