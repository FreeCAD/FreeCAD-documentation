# BlenderSverchokAddonSetup
**These notes are a work in progress.**

## Introduction

The Sverchok addon for Blender allows direct read and write of FreeCAD FCStd files.

There are some requirements to configure the Sverchok addon to get it working.

Generally, both Blender and FreeCAD must be using the same major.minor version of Python. So, for example if Blender is using Python 3.9, then FreeCAD must be as well. When configuring the Sverchok addon in Blender, the Blender addon must display a checkmark and *FreeCAD package is available* in the FreeCAD setup area at the bottom of the addon setting in Blender preferences.

Both Blender and FreeCAD version continue to change and may different on any given PC. Versions mentioned in the following were what was used as the writing of these notes.

### Debian 11 

(Note: on this machine I build multiple flavors of FreeCAD. Here I discuss my install/build of FreeCAD source retrieved and built from github daily. I run FreeCAD from the build directory and do not install, i.e. I never run 'make install' .)

This PC has Python 3.9.2.

Blender is at 2.93.3. In the Addons section sverchok nodes (1.0.1) are installed in the usual way. But, there is no path specified for FreeCAD python. On the Addons Blender/sverchok setup line for FreeCAD it says 'FreeCAD package is available'.

At the Python console in Blender (Shift-F4) the following commands produce:


```python
import PartDesign; PartDesign.__file__
'~/fc-daily-build-occt77/Mod/PartDesign/__init__.py'

 import freecad; freecad.__file__
'~/fc-daily-build-occt77/Ext/freecad/__init__.py'

import Part; Part.__file__
'~/fc-daily-build-occt77/Mod/Part/Part.so'
```

(Note: the tide represents the users home directory)

(Note: so the modules that Python finds are in the build folder in my home directory.) (Note: Modules PartDesign and freecad don\'t have .so files, but, Part does.)

If python sys.path is used to see the path it searches:

(Note: in this particular case, it works with nothing specified in the Blender Preferences Sverchok addons FreeCAD path. This happens on this particular PC because the Python path includes the required FreeCAD modules.)


```python
import sys
>>> print(sys.path)
['/home/mac/.local/share/FreeCAD/Mod/lattice2/./', '/home/mac/.local/share/FreeCAD/Mod/lattice2', '/home/mac/.local/share/FreeCAD/Mod/Curves/./', '/home/mac/.local/share/FreeCAD/Mod/Curves', '/home/mac/.local/share/FreeCAD/Mod/CurvedShapes/./', '/home/mac/.local/share/FreeCAD/Mod/CurvedShapes', '/home/mac/.local/share/FreeCAD/Mod/A2plus/./', '/home/mac/.local/share/FreeCAD/Mod/A2plus', '/home/mac/.local/share/FreeCAD/Mod/sheetmetal/./', 
<a long list that includes>
~/<build dir>/Mod/PartDesign
~/<build dir>/Mod
~/<build dir>/Ext
…
...
```

So, in this case Blender/sverchok has found the FreeCAD modules, the Python versions matches, and the nodes work.

### Manjaro

On this PC Blender 3.1.2 and FreeeCAD AUR is installed. The later means FreeCAD is built from the latest github source and is installed.

Installed, should imply that things are pretty much the same, but, there is a wrinkle thanks to the way the AUR package is installed. (I don't know if it is a bug in the AUR script or it is a glitch thanks to the fact that Arch/Manjaro updated to Python 3.10.)

Most of the previous discussion is the same. Except that none of the places that Python searches has a directory called PartDesign, the Blender/sverchok can't find \[/i\]PartDesign/\_\_init\_\_py\[/i\].

The solution is to use a BASH shellscript to launch Blender that uses the python path and Linux export to add the needed path to the Python search path. Save the following (adjusted for paths and such on the target PC) in a file with the extension *.sh* 
```python
PYTHONPATH=/usr/lib/freecad/Mod           #define PYTHONPATH
export PYTHONPATH                         #export PYTHONPATH
blender                                   #launch blender
```

### Linux Appimage 

This process was determined under Ubuntu 22.04 with Blender 3.4.1 and the Appimage of FreeCAD 0.21. (Both using Python 3.10.x)

When the FreeCAD appimage is started it creates a temporary FreeCAD installation in the /tmp directory. The name is different each time FreeCAD is started. It is in the following form where the last 6 letters are a random string: 
```python
/tmp/.mount_FreeCAwoAlTz
```

This directory is only available while FreeCAD is running. This means that the setting under Blender Preferences Add-ons for Sverchok can\'t be set permanently and must be discoverable by Sverchok. Sverchok need to know where the FreeCAD Modules reside. The complete is as follows: 
```python
/tmp/.mount_FreeCAwoAlTz/usr/lib
```

The solution is to use a BASH shellscript to launch Blender that uses the python path and Linux export to add the needed path to the Python search path. Save the following (adjusted for paths and such on the target PC) in a file with the extension *.sh* 
```python
PYTHONPATH=$(find  /tmp -type d -iname '*mount_FreeCA*' 2>/dev/null)"/usr/lib"    #define PYTHONPATH
export PYTHONPATH                                                                 #export PYTHONPATH
blender                                                                           #launch blender
```

FreeCAD *must* be running *before* this script executes and remain running while Blender/Sverchok is in use. As script similar to the following would only launch Blender if FreeCAD is running. 
```python
#!/bin/bash
APP="FreeCAD.appimag"
if pgrep "$APP" >/dev/null      #Is FreeCAD running?
then
    echo "$APP is running! Starting Blender" #launch blender

    PYTHONPATH=$(find  /tmp -type d -iname '*mount_FreeCA*' 2>/dev/null)"/usr/lib"
    echo "PYTHONPATH: $PYTHONPATH"

    cd ~/blender
    ./blender
else
    echo "$APP is not running, exiting!"
fi                                                                          
```

### Miscellaneous

-   Notes on other operating systems need to be added.
-   The initial Arch/Majaro AUR install of FreeCAD has been addressed as this writing (6/16/2022). Specifics mentioned above may be different or not required.
-   In some cases, the Sverchok addon setup just finds FreeCAD and no additional path setting is required.



---
![](images/Right_arrow.png) [documentation index](../README.md) > BlenderSverchokAddonSetup
