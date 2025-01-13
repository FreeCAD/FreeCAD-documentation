# <img alt="3Dconnexion SpaceNavigator" src=images/SpaceNavigator.jpg  style="width:200px;"> 3Dconnexion input devices/en




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

Spacenav needs these permissions:

:   
    
```python
    cp ~/.Xauthority /root/
    
```
    

Restart spnavd and FreeCAD

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
    

-   \... then you need to install **libgtkmm-2.4-dev**. Under Ubuntu, this is done like this:

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

-   Follow the same pattern to compile and install **spnavcfg**. Make sure to run spnavcfg as root, or no settings will be saved!

#### Starting spacenavd as a systemd service at boot 

If you want to start spacenavd at boot using systemd, do the following:

-   Go to the directory where you clone the spacenavd repository (to the root of the repository)
-   \"sudo cp contrib/systemd/spacenavd.service /usr/lib/systemd/system/spacenavd-local.service\".
-   \"sudo systemctl enable spacenavd-local.service\".
-   \"sudo systemctl start spacenavd-local.service\", if you want to start it right away.

This is only necessary for the installation from source.

#### Restarting spacenavd 

If sometimes SpaceNavigator stops working, it is good to restart driver. To restart it, go to Terminal and execute:


```python
sudo xhost +
sudo /etc/init.d/spacenavd restart
```

After that restart FreeCAD. On some distros this is necessary at each boot.

#### Known Issues 

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

### MacOS

3Dconnexion input devices are supported on macOS, provided FreeCAD is built and used on a system with the 3Dconnexion drivers installed. You may need 3DxWare 10.7.2 or greater for macOS 12 Monterey.

### Windows

As of version 0.13, 3D mouse is supported under Windows. You need to have 3Dconnexion drivers installed. In FreeCAD version 1.0 a [new integration with 3Dconnexion devices](https://github.com/FreeCAD/FreeCAD/pull/12929) has been introduced. If compiled with that integration, only recent hardware is supported: to support older devices users will need to self-compile with the FREECAD_3DCONNEXION_SUPPORT cMake variable set to \"Raw Input\". Windows users should be aware that 3Dconnexion\'s driver (*not* the code in FreeCAD) contains a telemetry package that communicates information about your installed software back to 3Dconnexion.

#### Known Issues 

-   In FreeCAD version 1.0 and later changing settings in the 3DX config window may not have the expected results ([issue](https://github.com/FreeCAD/FreeCAD/issues/14044)). To fix this:
    1.  Stop the driver (by running Stop 3DxWare).
    2.  Go to **..<user>\AppData\Roaming\3Dconnexion\3DxWare\Cfg** and delete the **FreeCAD.xml** file.
    3.  Start the driver (by running Start 3DxWare).
    4.  Run FreeCAD and check if you can change the [Spaceball Motion](#Spaceball_Motion.md) settings.

## Setting up FreeCAD 


<small>(v1.0)</small> 

: The 3Dconnexion manipulator can be set up in its driver app (3DxWare software).


{{VersionMinus|0.21}}

: If a Spaceball is detected the following tabs in the [Customize dialog](Interface_Customization.md) can be used to change settings:

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

### Troubleshooting

Check if your FreeCAD installation links to the spacenav library. The best way to check this is by running FreeCAD from the command line terminal `FreeCAD --log-file /tmp/freecad.log` and close it immediately again. Then open the file **/tmp/freecad.log** and search for the messages:


`Connected to spacenav daemon`

or


`Couldn't connect to spacenav daemon. Please ignore if you don't have a spacemouse.`

If none of them appears then your FreeCAD build doesn\'t link to the spacenav library. If the former message appears then it basically works. The latter message means there is probably a problem with the spacenav daemon.

## Related

-   Forum thread [spacenav on Windows](https://forum.freecadweb.org/viewtopic.php?f=3&t=51023)
-   Forum thread [Space navigator axis confusion](https://forum.freecadweb.org/viewtopic.php?f=8&t=57188)



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [3rd Party](Category_3rd Party.md) > 3Dconnexion input devices/en
