# AppImage/pl
**As of 7 July 2019, the FreeCAD community has been observing that downloading AppImages from Github seems to timeout before completion. We aren't sure why this is occurring. If this happens to you please try downloading again. It make take a few tries. A recommended practice is to use the AppImage [https://www.freecadweb.org/wiki/Appimage#Automatic_updating auto-updating feature], which will restore the download from the place it failed.**


{{TOCright}}

## What is an AppImage? 

![](images/AppImage-logo.png ) **Package once and run everywhere. Reach users on all major Linux desktop distributions.**

AppImage is a \"universal binary package\" intended to distribute an application to any Linux distribution. Read more about it on the [Appimage homepage](https://appimage.org) and [Wikipedia](https://en.wikipedia.org/wiki/AppImage).

To run it, fist make it executable, and then type the relative or full path. 
```python
chmod +x FreeCAD_x86_64.AppImage
./FreeCAD_x86_64.AppImage
```

For other types of installation see [Download](Download.md).

## FreeCAD AppImages 


**'''Note:''' Development builds are now hosted on the [https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds '''FreeCAD-Bundle'''] github repo.<br/>If the download links below do not work, please manually download the files from the expanded "Assets" section of the above link**

  Stable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Development
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![](images/AppImage-logo.png ) \[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/>{{:Template:Stable-Major-and-Minor-Version}}/FreeCAD\_{{:Template:Stable-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{:Template:Stable-Version}}\] (\[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/>{{:Template:Stable-Major-and-Minor-Version}}/FreeCAD\_{{:Template:Stable-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])   ![](images/AppImage-logo.png ) \[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage {{:Template:Development-Version}}\] (\[<https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds->{{:Template:Development-Version}}-Linux-Conda\_glibc2.12-x86\_64.AppImage-SHA256.txt SHA256\])

  : style=\"text-align: center; font-size: 150%; \| Available FreeCAD AppImages \|+

**Important Notes:**

-   Development happens daily and rapidly, the link for the most up-to-date AppImage is a moving target.
-   The development link above should be up-to-date because it is updated via a script.
-   Many users on the forum utilize the development version.
-   It can be run on the same system in parallel with another version of FreeCAD.
-   Users use the dev version to take advantage of the latest features and bug fixes (since FreeCAD has a long release cycle). They also use it to help test and find bugs to spur development and improvement of FreeCAD.

#### Obligatory Word of Caution 

For the most part the development version is stable but of course it\'s important to add the obligatory statement to use it at your own risk. Though most people that utilize backups and \'save often\' do quite well.

## Automatic updating 

AppImage has a smart and economical way of updating. It calculates the difference between the new AppImage and the old one, and will only download the changes between their versions. In theory the user ends up downloading around 15% each time instead of an entirely new AppImage.

Automatic updating is done via several optional methods. Currently there are 4 methods, 2 through the graphical interface (GUI), and 2 through the command-line/terminal interface (CLI).

### Experimental in-app updating 

Thanks to the efforts of several key devs, there is an [ongoing effort](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324) to integrate a feature that allows **self-updating the AppImage within FreeCAD** itself. Starting from FC 0.19.21514 there now exists an AppImage section found via **Edit → Preferences → AppImage**. Please test this capability and report your experience to the [forum discussion](https://forum.freecadweb.org/viewtopic.php?f=8&t=44324).

### GUI method 1 (official) 

This is the official AppImageUpdate GUI application.

1.  Download [AppImageUpdate-x86\_64.AppImage](https://github.com/AppImage/AppImageUpdate/releases/download/continuous/AppImageUpdate-x86_64.AppImage).
2.  Make it executable by right clicking on the file, going in to properties and \"Run as an executable\".
3.  Double click on the AppImage icon, a dialog box will appear and you\'ll be prompted to specify what AppImage you want to update.
4.  Specify the path to your existing AppImage.
5.  Once the AppImage is updated, press the button **Run updated AppImage**.

### GUI method 2 (unofficial) 

This is a sleeker 3rd-party unofficial version of AppImageUpdate named: **AppImageUpdater**. It is still in development (at the time of this wiki edit) but nevertheless, quite nice to use.

1.  Download [AppImageUpdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous)
2.  Make it executable: 
```pythonchmod +x AppImageUpdater*-x86_64.AppImage```
3.  Run it: 
```pythonsource AppImageUpdater*-x86_64.AppImage```
4.  Find your current FreeCAD AppImage and drag-drop it on to the AppImageUpdater

Result: Follow the AppImageUpdater prompts

### CLI method 1 (official) 

Run the following instructions in your terminal


```python
wget https://github.com/AppImage/AppImageUpdate/releases/download/continuous/appimageupdatetool-x86_64.AppImage
chmod +x ./appimageupdatetool-x86_64.AppImage
./appimageupdatetool.AppImage path/to/old/FreeCAD.AppImage
chmod +x path/to/updated/FreeCAD.AppImage
./path/to/updated/FreeCAD.AppImage
```

Notes:

-   The file names will be unique because of the version info is embedded in them. The above instructions are simplified for convenience.
-   Run `./appimageupdatetool-x86_64.AppImage --help` to learn about functionality like `--remove-old`, `--overwrite` and `--self-update`.
-   There is also an i386 version; see the [AppImageUpdate release](https://github.com/AppImage/AppImageUpdate/releases) page.

Todo: share a script that can be added as an alias or cron job.

### CLI method 2 (unofficial) 

Similarly to the Graphical methods having an official and unofficial approaches to downloading AppImages, the same applies to the command line. This is a sleeker 3rd-party command line option to download AppImages

1.  Download [appimageupdater-\*-x86\_64.AppImage](https://github.com/antony-jr/AppImageUpdater/releases/tag/continuous-cli)
2.  Make it executable: 
```pythonchmod +x appimageupdater*-x86_64.AppImage```
3.  Run it: 
```pythonsource appimageupdater*-x86_64.AppImage /path/to/old/FreeCAD-AppImage.AppImage```

**Result**: Updates specified AppImage file if update exists

# Experimental

## Fixing AppImage zsync 

It may happen that an AppImage won\'t update because it\'s target file changed in some way. Instead of downloading a whole new appimage, it\'s possible to rewrite the zsync file that is used by the AppImage to download the delta. More info can be found at <https://github.com/antony-jr/appimage-update-info-writer>.

This section needs more details.

## Downloading via Bittorrent 

An experimental feature that the FreeCAD packaging team is exploring (thanks to the work of Antony-jr) is being able to download an appimage delta of FreeCAD via bittorrent. The repository issue is at <https://github.com/FreeCAD/FreeCAD-Bundle/issues/49>

# Developer Section 


**Note:**

the following sections are intended for developers

## Unpacking AppImages 

A very convenient aspect of FreeCAD is that a majority of it is built in [Python](Python.md), which doesn\'t need to be manually compiled like C++. Essentially, a Python file can be modified, and upon restarting FreeCAD those changes will be integrated into the application. A developer can quickly work on the latest FreeCAD release using this technique and an AppImage. Moreover, using an AppImage doesn\'t modify your system\'s environment in any way, that is, nothing is installed and no environmental variables are modified.

### Modifying AppImages 

An AppImage embeds a file system in it with everything that is required to run the application. In order to modify it, the file system needs to be extracted.


```python
./FreeCAD_xxx.AppImage --appimage-extract
cd squashfs-root/
```

Now open the required Python source files in your preferred code editor, modify them, and save them. Then run the application.


```python
./AppRun
```

### Repackaging AppImages 

If you\'ve modified the code, and now want to re-package the AppImage with your latest changes, use the [appimagetool-x86\_64](https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage) tool on the extracted file system.


```python
cd ..
wget "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
chmod +x appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage squashfs-root
```

## Personalized AppImages 

Thanks to the work of **realthunder**, author of [App Link](App_Link.md) and [Assembly3 Workbench](Assembly3_Workbench.md), it is possible to build custom AppImages using a set of scripts.

This makes it very convenient to release images for a specific branch of the source code for others to test. Although AppImages only work on Linux, realthunder\'s scripts make it possible to generate AppImages also on Windows and MacOS.

The repository for these scripts is at _ for more details.



_ _ _

---
[documentation index](../README.md) > [Packaging](Category_Packaging.md) > AppImage/pl
