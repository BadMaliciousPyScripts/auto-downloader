# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
import os
from extrafunc import Main as xtra


class MyList(list):
    def last_index(self):
        return len(self)-1

class nopy:
    def download(link):
        file = link.split("//")[1].split("/")[-1]
        c_list = link.split("//")[1].split("/")
        index_l = MyList(c_list).last_index()
        code = c_list[(index_l-1)]
        data = {
            "file": file,
            "code": code
        }
        print("Downloading file: {} with nopy.py".format(file))

        sessionreq = requests.post("https://data.nopy.to/file", data=data).json()

        download_data = {
            "code": code,
            "fid": sessionreq["msg"]["fid"],
            "request": sessionreq["msg"]["request"],
            "session": sessionreq["msg"]["session"]
        }

        file_size = int(eval(sessionreq["msg"]["raw_size"]))

        downloadreq = requests.post(
                        "https://data.nopy.to/download",
                        data=download_data
                       ).json()

        with requests.get(
            downloadreq["msg"]["download"], stream=True, allow_redirects=True
            ) as req:
            with open(".\\Downloads\\" + file, "wb") as f:
                for chunk in req.iter_content(chunk_size=4096*3072):
                    f.write(chunk)
                    file_info = os.stat(f.name)
                    strms = xtra.calcthisshit(file_info.st_size, file_size)
                    print('{:.2f}/{:.2f}mb downloaded - {}'.format(
                        file_info.st_size/1000000,
                        file_size/1000000,
                        strms,
                    ), end="\r")
        print("")
