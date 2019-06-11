import time
import requests
import json
import win32api, win32gui, win32con
import sys
import os

date = list(time.localtime(int(time.time())))
code = str(date[0]) + str(date[1]) + str(date[2])
origin_data = json.loads(open('cache.old','r').read())
waitTime = int(origin_data['waitTime'])

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}

def isConnectWifi():
    try:
        requests.get('https://baidu.com',headers=header)
    except Exception:
        return 0
    return 1

def setWallPaper(pic):
  regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
  win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
  win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
  win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)

if not origin_data['date'] == code:
    tryConnect = 0
    while not isConnectWifi():
        time.sleep(5)
        tryConnect += 5
        if tryConnect >= waitTime:
            warning_c = 'mshta vbscript:msgbox("NoWifiWarning: no wifi detected!",64,"Bing Wall Setter")(window.close)'
            os.system(warning_c)
            os._exit(0)

    try:
        web_c = json.loads(requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1',headers=header,timeout=10).content)['images'][0]['url']

        url = 'https://www.bing.com' + web_c.split('&')[0]
        file_type = url.split('.')[-1]

        with open('pic.'+file_type,'wb') as f:
            f.write(requests.get(url).content)
        setWallPaper(sys.path[0] + '/pic.jpg')

    except Exception as e:
        warning_c = 'mshta vbscript:msgbox("Error: cannot set the wallpaper because an error occure",64,"Bing Wall Setter")(window.close)'
        os.system(warning_c)
        os._exit(0)

    with open('cache.old', 'w') as f:
        origin_data['date'] = code
        f.write(json.dumps(origin_data))

