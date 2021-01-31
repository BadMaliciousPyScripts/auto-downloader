import filechecker
import time
from mega import Mega
import platform
import os
import nopy
import anonfiles
import mediafire

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

class main:
    def download_mega(urllist):
        print("Logging in to mega...")
        mega = Mega()
        mlogin = mega.login()
        url = urllist[0]
        urlinfo = mega.get_public_url_info(url)
        fname = urlinfo["name"]
        print(
            F"\nDownload from mega with mega.py!\nFile name: {fname}"
        )
        urllist = urllist.remove(urllist[0])
        try:
            mlogin.download_url(url, ".\\Downloads\\")
        except Exception:
            pass
        main.update_dllist(urllist[0])

    def download_nopy(urllist):
        nopy.nopy.download(urllist[0])
        main.update_dllist(urllist[0])

    def download_anonfiles(urllist):
        anonfiles.anonfiles.download(urllist[0])
        main.update_dllist(urllist[0])

    def download_mediafire(urllist):
        mediafire.mediafire.download(urllist[0])
        main.update_dllist(urllist[0])

    def update_dllist(url):
        dwnloadedflist = open("downloadlistc.txt", "r").read()
        nlist = dwnloadedflist.split("\n")
        nlist.append(url)
        for x in nlist:
            if x == "" or x == " ":
                nlist.remove(x)
        open("downloadlistc.txt", "w").write(func.listtostring(nlist))
        print("")
