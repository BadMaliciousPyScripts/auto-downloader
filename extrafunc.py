import time


class Main:
    def calcthisshit(fileinfo1, fileinfo2):
        list1 = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
        l2 = "[~~~~~~~~~~~~~~~~~~~~]"
        percent = fileinfo1/fileinfo2*100
        percent = float("{:.2f}".format(percent))
        i = 0
        for x in list1:
            if x > percent:
                i = list1.index(x) + 1
                while i != 0:
                    l2 = list(l2)
                    l2[i] = "█"
                    l2 = Main.listtostring(l2)
                    i -= 1
                break
        if percent > 99:
            l2 = "[████████████████████]"
        l2 = l2, str(percent) + "%"
        return Main.listtostring(l2)

    def listtostring(list):
        str = ""
        for x in list:
            str += x
        return str

    def downsec(fileinfo, timeinfo, altfileinfo):
        fileinfoc = fileinfo - altfileinfo
        mbpersec = fileinfoc/timeinfo
        return mbpersec, fileinfo

    def getremtime(sizemb, downspeed):
        timeinsec = float(sizemb) / float(downspeed)
        timeinsec = int(timeinsec)
        total = Main.timetot(timeinsec)
        return total

    def timetot(timeinsec):
        hr = timeinsec / 3600
        hr = int(hr)
        mins = (timeinsec - (hr * 3600)) / 60
        mins = int(mins)
        secs = timeinsec - (hr*3600) - (mins * 60)
        secs = int(secs)
        if secs < 10:
            secs = str(secs)
            secs = "0" + secs
        else:
            secs = str(secs)
        if mins < 10:
            mins = str(mins)
            mins = "0" + mins
        else:
            mins = str(mins)
        if hr < 10:
            hr = str(hr)
            hr = "0" + hr
        else:
            hr = str(hr)
        total = hr + ":" + mins + ":" + secs
        return total
