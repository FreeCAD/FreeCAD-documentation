# <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> {{TOCright}} 3Dconnexion input devices/pl

## Driver installation 

### Linux

FreeCAD supports drivers from project [Spacenav](http://spacenav.sourceforge.net/). This is a project aiming to create an open-sourced driver which is compatible with the proprietary drivers from 3Dconnexion.

#### Install from repo 

##### Ubuntu


```python
sudo apt-get install spacenavd
```

Note, however, that version 0.6 available on Ubuntu 20.04 (and probably older ones) does not seem to work. You then have to compile spacenavd from source as explained below.

##### Fedora


```python
sudo yum install spacenavd
```

##### Debian


```python
apt-get install spacenavd libspnav-dev
```


:   spacenav needs these permissions:





:   
    
```python
    cp ~/.Xauthority /root/
    
```
    





:   Restart spnavd and FreeCAD





:   
    
```python
    /usr/bin/spnavd_ctl x11 stop
    /usr/bin/spnavd_ctl x11 start
    
```
    

##### openSUSE


```python
sudo zypper install spacenavd
```

#### Compile Spacenav from source 

This is recommended if your distribution might provide an outdated version.

-   Download the following files:
    -   [spacenavd](https://sourceforge.net/projects/spacenav/files/latest/download) (latest version)
    -   [libspnav](https://sourceforge.net/projects/spacenav/files/spacenav%20library%20%28SDK%29/) (get latest libspnav version)
    -   [spnavcfg](https://sourceforge.net/projects/spacenav/files/spacenavd%20config%20gui/) (get latest libspnav version)
-   Unpack the archives into a folder in your home directory.
-   Enter the spacenavd-x.x directory and run the following commands:

:   
    
```python
    ./configure
    make
    
```
    

-   If this was successful, run the following commands **as root** (or prefix with sudo.)

:   
    
```python
    make install
    ./setup_init
    /etc/init.d/spacenavd start
    
```
    

-   This installs the spacenav daemon, configures it to automatically load on system boot, and starts the daemon without having to reboot.
-   Now it is time to check that your device is properly detected. With your device unplugged, run the following command and then plug it in.

:   
    
```python
    tail -n100 -f /var/log/spnavd.log 
    
```
    

-   If the output looks something like this, you can continue.

:   
    
```python
    Device detection, parsing /proc/bus/input/devices
    trying alternative detection, querying /dev/input/eventX device names...
      trying "/dev/input/event1" ... Power Button
      trying "/dev/input/event2" ... 3Dconnexion SpaceNavigator
    using device: /dev/input/event2
    device name: 3Dconnexion SpaceNavigator
    
```
    

-   Now enter the directory named libspnav-x.x.x and run the following commands:

:   
    
```python
    ./configure
    make
    
```
    

-   If make fails with the following error: \...

:   
    
```python
    fatal error: gtk/gtk.h: No such file or directory
    
```
    

-   \... then you need to install libgtkmm-2.4-dev. Under Ubuntu, this is done like this:

:   
    
```python
    sudo apt-get install libgtkmm-2.4-dev
    
```
    

-   When make has completed successfully, run the following command **as root** (or prefix with sudo.)

:   
    
```python
    make install
    
```
    

-   Look in the directory libspnav-x.x.x/examples/. If you want to test your device, compile and run either one of the two examples.

-   Follow the same pattern to compile and install spnavcfg. Make sure to run spnavcfg as root, or no settings will be saved!

#### Starting spacenavd as a systemd service at boot 

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.

#### Restarting spacenavd 

If sometimes navigator stops working, it is good to restart driver. To restart it, go to Terminal and execute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

After that restart FreeCAD. On some distros this is necessary at each boot.

### Known Issues 

A user reported on the [forum](https://forum.freecadweb.org/viewtopic.php?p=341327#p341327) they saw the following:

 Spacenav daemon 0.6
 failed to open config file /etc/spnavrc: No such file or directory. using defaults.
 adding device.
 device name: 3Dconnexion SpacePilot
 using device: /dev/input/event5
 No protocol specified
 failed to open X11 display ":0.0" 

The workaround that worked for them:


```python 
sudo cp ~/.Xauthority /root/
sudo spnavd_ctl x11 start
sudo systemctl restart spacenavd 
```

### OSX

3Dconnexion input devices are supported on OS X, provided that FreeCAD is built and used on a system with the 3Dconnexion drivers installed.

### Windows

As of version 0.13, 3D mouse is supported under Windows. You need to have 3Dconnexion drivers installed.

#### Known Issue 

There is an issue where 3Dconnexion sends duplicate scroll events to FreeCAD, which causes the view to jump. To fix it:

1.  Open 3Dconnexion Properties. You can double-click its icon in the Taskbar, next to the Windows clock.
2.  Click on the Advanced Settings button.
3.  Open FreeCAD or switch to an already-open FreeCAD window.
4.  Switch back to 3Dconnexion Advanced Settings. Confirm that it says \"FreeCAD\" in the heading.
5.  Uncheck all boxes on the page.

ref: <https://freecadweb.org/tracker/view.php?id=1893>

## Setting up FreeCAD 

3D mouse support was made with spnav project on Linux, and on a very low level on Windows. This means there was no support for any settings for a device, since on Linux there is no good support for this, and on Windows it is overridden. This is why two additional pages were added to \"Customize\" dialog.

<img alt="" src=images/Spaceball_Motion.png  style="width:450px;"> <img alt="" src=images/Spaceball_Buttons.png  style="width:450px;">

### Spaceball Motion 

In this tab you have ability to set up some of general space mouse settings. They include:

-   Global Sensitivity - Slider with ability to set global sensitivity
-   Dominant - if you enable dominant mode, only axes with highest move will be considered
-   Flip YZ - This option enables you to flip Y and Z axes on 3D mouse
-   Enable Translations - easy way to enable/disable translations
-   Enable Rotations - easy way to enable/disable rotations
-   Calibrate - enables you to calibrate space navigator. It is pressed while space navigator is not moved.
-   Set To Default - removes all settings and sets them to default.

Other than this, for each axes you have ability to set:

-   Enabled - Enable/Disable axes
-   Reverse - Reverse movement on axes
-   Sensitivity - slider with ability to set sensitivity

### Spaceball Buttons 

When you open this tab for the first time, it will be empty and unavailable. To activate it, you must press one of your space mouse buttons. After you do, list of buttons will appear on the left side, and list of commands will be available on the right side.

To connect certain command with a button, select button on the left side, and it\'s command on the right side. To clear commands from button, press \"Clear\".

## Related

-   Forum thread [spacenav on windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > 3Dconnexion input devices/pl
