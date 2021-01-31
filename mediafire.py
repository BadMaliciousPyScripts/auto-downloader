# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os
from extrafunc import Main as xtra

class mediafire:
    def download(url):
        download_link = mediafire.extractDownloadLink(url)
        file_name = mediafire.extractFileName(url)
        print("Downloading file: {} with mediafire.py!".format(file_name))
        file_size = int(requests.head(download_link).headers.get("Content-Length"))
        with requests.get(
                download_link, stream=True, allow_redirects=True
            ) as req:
            with open(".\\Downloads\\" + file_name, "wb") as f:
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


    def extractFileName(url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        name = soup.find(
                "div", class_="promoDownloadName notranslate"
               ).find("div", class_="dl-btn-label")['title']
        return name

    def extractDownloadLink(url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        link = soup.find(
            "div", class_="download_link", id="download_link"
        ).find("a", id="downloadButton")['href']
        return link
