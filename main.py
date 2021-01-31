# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# base modules
import time
import os

# pypi modules
import platform
from stopwatch import Stopwatch

# self made modules
import filechecker
import downloader
from extrafunc import Main as xtra
sw = Stopwatch()
sw.stop()


class func:
    def listtostring(list):
        str = ""
        for x in list:
            if x == list[0]:
                str += x
            else:
                str += "\n" + x
            if list.index(x) == (len(list) - 1):
                str += "\n"
        return str

    def cleanscreen():
        opsys = platform.system()
        if opsys == "Windows":
            os.system("cls")
        if opsys == "Darwin" or opsys == "Linux":
            os.system("clear")

    def return_f(function):
        return function

    def freturn():
        return


class main:
    def loop():
        while True:
            main.main()

    def main():
        urllist = filechecker.main()
        if sw.running != 1:
            sw.start()
        if urllist is False:
            dur = str(sw)
            print(f"Cond False ignoring Task for: {dur}          ", end="\r")
        else:
            sw.reset()
            main.switch_downloader(urllist[0], urllist)

    def switch_downloader(arg, urllist):
        url = urllist[0]
        arg = xtra.listtostring(url).split("//")[1].split(".")[0]
        if arg == "www":
            arg = xtra.listtostring(url).replace(
                "www.", ""
            ).split("//")[1].split(".")[0]
        downloader = {
            "mega": main.downloadmega,
            "nopy": main.downloadnopy,
            "mediafire": main.downloadmediafire,
            "anonfiles": main.downloadanonfiles
        }
        function = downloader.get(
            arg, lambda: print("Invalid Argument", lambda: func.freturn())
        )
        function(urllist)

    def downloadmega(urllist):
        downloader.main.download_mega(urllist)

    def downloadnopy(urllist):
        downloader.main.download_nopy(urllist)

    def downloadmediafire(urllist):
        downloader.main.download_mediafire(urllist)

    def downloadanonfiles(urllist):
        downloader.main.download_anonfiles(urllist)

main.loop()
