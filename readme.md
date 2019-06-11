![logo](ico.ico)

<center>Bing Wallpaper Setter</center>

---

Catch the Today’s wallpaper from bing.com, and set as wallpaper

**feature:**

1. Automatically try connect WIFI
2. Always 2k resolution
3. save the ChangeLog and judge the date
4. Beautiful and simplest code

**usage:**

1. set the `cache.old` by your preference
2. set the `bws.exe` as startup run program by execute following code in cmd:

```cmd
@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit 
:begin
@reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "bws" /d "[bws.exe absolutly address]" /f
pause
```

3. Have fun

**delete:**

1. execute following code to cancel startup running option:

```cmd
@reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "bws" 
pause
```

2. delete the whole program file
3. OK

