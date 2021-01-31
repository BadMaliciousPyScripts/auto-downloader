# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
from extrafunc import Main as xtra

class anonfiles:
    def download(url):
        link = anonfiles.extractDownloadLink(url)
        code = url.split("/")[-1]
        request = requests.get("https://api.anonfiles.com/v2/file/{}/info".format(code)).json()
        file_size = request["data"]["file"]["metadata"]["size"]["bytes"]
        file_name = request["data"]["file"]["metadata"]["name"]
        file_name_extension = file_name[-4:].replace("_", ".")
        file_name_raw = file_name[:-4:]
        file = file_name_raw + file_name_extension
        print("Downloading file: {} with anonfiles.py!".format(file))
        if os.path.isdir('Downloads'):
            pass
        else:
            os.mkdir("Downloads")
        with requests.get(
            link, stream=True, allow_redirects=True
            ) as req:
            with open(".\\Downloads\\" + file, "wb") as f:
                for chunk in req.iter_content(chunk_size=512*1024):
                    f.write(chunk)
                    file_info = os.stat(f.name)
                    strms = xtra.calcthisshit(file_info.st_size, file_size)
                    print('{:.2f}/{:.2f}mb downloaded - {}'.format(
                        file_info.st_size/1000000,
                        file_size/1000000,
                        strms,
                    ), end="\r")
        print("")

    def extractDownloadLink(url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        link = soup.find(
            "div", class_="row", id="download-wrapper"
        ).find("a", id="download-url")['href']
        return link
