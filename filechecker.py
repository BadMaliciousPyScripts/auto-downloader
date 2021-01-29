import os


def main():
    if os.path.isfile("downloadlistc.txt"):
        filelist = open("downloadlistc.txt", "r").read()
    else:
        filelist = open("downloadlistc.txt", "w").write("")
        filelist = open("downloadlistc.txt", "r").read()

    listnl = filelist.split("\n")
    if os.path.isfile("downloadlist.txt"):
        dwnlist = open("downloadlist.txt", "r").read()
    else:
        dwnlist = open("downloadlist.txt", "w")
        dwnlist = open("downloadlist.txt", "r").read()
    dwnlist = dwnlist.split("\n")
    dwnlist_bak = dwnlist
    for n in range(3000):
        for x in listnl:
            if x in dwnlist:
                dwnlist_bak.remove(x)
    if dwnlist_bak is None or dwnlist_bak == [""] or dwnlist_bak == []:
        dwnlist_bak = False
    return dwnlist_bak
