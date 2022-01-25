# Backend Adminstration
This page documents the FreeCAD backend project administration.

### Updating AppImage Link on the wiki 

Currently there is a script that queries the github API and gets the latest version name and URL of the Conda Appimage. It then automagically logs in to the wiki and changes the [Template:Development-Version](Template:Development-Version.md). It is invoked via cron every 6 hours. Instructions to trigger scrip manually:

 ssh foobar@de1.freecad.io
 cd core/
 python3 pwb.py freecad/freecad-update-dev-appimage-version.py

List crontab

 crontab -l

Update pywikibot:

 cd core/
 git pull --recurse-submodules



---
![](images/Right_arrow.png) [documentation index](../README.md) > Backend Adminstration
