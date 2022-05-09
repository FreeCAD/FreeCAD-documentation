# Debugging/sv
{{TOCright}}


<div class="mw-translate-fuzzy">

## Testa först 

Innan du går igenom avbuggningssmärtan, använd testramverket för att kontrollera om standardtesterna fungerar korrekt. Om inte så kanske det kan bero på en trasig installation.


</div>

Before you go through the pain of debugging use the [Test framework](Testing.md) to check if the standard tests work properly. If they do not run complete there is possibly a broken installation.


<div class="mw-translate-fuzzy">

## kommandorad

*Avbuggningen* av FreeCAD stöds av en del interna mekanismer. Kommandoradsversionen av FreeCAD erbjuder alternativ för avbuggningsstöd   *

-v   * Med \"v\" alternativet så ger FreeCAD en mer pratig utmatning.
-l   * Med \"l\" alternativet så skriver FreeCAD extra information till en loggfil.


</div>

The *debugging* of FreeCAD is supported by a few internal mechanisms. The command line version of FreeCAD provides some options for debugging support.

These are the currently recognized options in FreeCAD 0.19   *

Generic options   *

 -v [ --version ]          Prints version string
 -h [ --help ]             Prints help message
 -c [ --console ]          Starts in console mode
 --response-file arg       Can be specified with '@name', too
 --dump-config             Dumps configuration
 --get-config arg          Prints the value of the requested configuration key

Configuration   *

 -l [ --write-log ]        Writes a log file to   *
                           $HOME/.FreeCAD/FreeCAD.log (Linux)
                           $HOME/Library/Preferences/FreeCAD/FreeCAD.log (macOS)
                           %APPDATA%\FreeCAD\FreeCAD.log (Windows)
 --log-file arg            Unlike to --write-log this allows to log to an 
                           arbitrary file
 -u [ --user-cfg ] arg     User config file to load/save user settings
 -s [ --system-cfg ] arg   System config file to load/save system settings
 -t [ --run-test ] arg     Test case - or 0 for all
 -M [ --module-path ] arg  Additional module paths
 -P [ --python-path ] arg  Additional Python paths
 --single-instance         Allow to run a single instance of the application

## Generating a Backtrace 

If you are running a version of FreeCAD from the bleeding edge of the development curve, it may \"crash\". You can help solve such problems by providing the developers with a \"backtrace\". To do this, you need to be running a \"debug build\" of the software. \"Debug build\" is a parameter that is set at compile time, so you\'ll either need to compile FreeCAD yourself, or obtain a pre-compiled \"debug\" version.

### For Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prerequisites   *

-   software package gdb installed
-   a debug build of FreeCAD (at this time only available by [building from source](Compile_on_Linux#For_a_Debug_build.md))
-   a FreeCAD model that causes a crash

Steps   * Enter the following in your terminal window   *

Find FreeCAD binary on your system   *


```python
$ whereis freecad
freecad   * /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

GNUdebugger will output some initializing information. The (gdb) shows GNUDebugger is running in the terminal, now input   *


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD will now start up. Perform the steps that cause FreeCAD to crash or freeze, then enter in the terminal window   *


```python
(gdb) bt
```

This will generate a lengthy listing of exactly what the program was doing when it crashed or froze. Include this with your problem report.


```python
(gdb) bt full
```

Print the values of the local variables also. This can be combined with a number to limit the number of frames shown.


</div>


</div>

### For macOS 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

macOS Debugging →


<div class="mw-collapsible-content">

Prerequisites   *

-   software package lldb installed
-   a debug build of FreeCAD
-   a FreeCAD model that causes a crash

Steps   * Enter the following in your terminal window   *


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB will output some initializing information. The (lldb) shows the debugger is running in the terminal, now input   *


```python
(lldb) run
```

FreeCAD will now start up. Perform the steps that cause FreeCAD to crash or freeze, then enter in the terminal window   *


```python
(lldb) bt
```

This will generate a lengthy listing of exactly what the program was doing when it crashed or froze. Include this with your problem report.


</div>


</div>

## List Libraries Loaded by FreeCAD 

(Applicable to Linux and macOS)

Sometimes it\'s helpful to understand what libraries FreeCAD is loading, specifically if there are multiple libraries being loaded of the same name but different versions (version collision). In order to see which libraries are loaded by FreeCAD when it crashes you should open a terminal and run it in the debugger. In a second terminal window, find out the process id of FreeCAD   *


`ps -A &#124; grep FreeCAD`

Use the returned id and pass it to `lsof`   *


` lsof -p process_id`

This prints a long list of loaded resources. So for example, if trying to ascertain if more than one Coin3d library versions is loaded, scroll through the list or search directly for Coin in the output   *


`lsof -p process_id &#124; grep Coin`

## Python Debugging 

For a more modern approach to debugging Python, see these posts   *

-   [Debugging macros with VS 2017](https   *//forum.freecadweb.org/viewtopic.php?f=22&t=28901)
-   [Python workbenches debugging](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

winpdb Debugging →


<div class="mw-collapsible-content">

Here is an example of using *Winpdb* inside FreeCAD   *

We need the Python debugger   * *Winpdb*. If you do not have it installed, on Ubuntu/Debian install it with   *


```python
sudo apt-get install winpdb
```

Now lets setup the debugger.

1.  Start *Winpdb*.
2.  Set the debugger password to \"test\"   * Go to menu *File* → \'\'Password\" and set the password.

Now we will run a test Python script in FreeCAD step by step.

1.  Run winpdb and set the password (e.g. test)
2.  Create a Python file with this content


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Start FreeCAD and load the above file into FreeCAD
2.  Press F6 to execute it
3.  Now FreeCAD will become unresponsive because the Python debugger is waiting
4.  Switch to the Windpdb GUI and click on \"Attach\". After a few seconds an item \"\" appears where you have to double-click
5.  Now the currently executed script appears in Winpdb.
6.  Set a break at the last line and press F5
7.  Now press F7 to step into the Python code of Draft.makeWire


</div>


</div>

### Visual Studio Code (VS Code) 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

VS Code Debugging →


<div class="mw-collapsible-content">

Prerequisites   *

-   The ptvsd package needs to be installed in a Python 3 outside of FreeCAD, then the module must be copied to FreeCAD\'s Python library folder.


```python
# In a cmd window that has a path to you local Python 3   *
pip install ptvsd
# Then if your Python is installed in C   *Users\<userid>\AppData\Local\Programs\Python\Python37
# and your FreeCAD is installed in C   *freecad\bin
xcopy "C   *Users\<userid>\AppData\Local\Programs\Python\Python37\Lib\site-packages\ptvsd" "C   *freecad\bin\Lib\site-packages\ptvsd"
```

[pypi page](https   *//pypi.org/project/ptvsd/)

[Visual Studio Code documentation for remote debugging](https   *//code.visualstudio.com/docs/python/debugging#_remote-debugging)

Steps   *

-   Add following code at the beginning of your script


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Add a debug configuration in Visual Studio Code **Debug → Add Configurations…**.
-   The config should look like this   *




        "configurations"   * [
            {
                "name"   * "Python   * Attacher",
                "type"   * "python",
                "request"   * "attach",
                "port"   * 5678,
                "host"   * "localhost",
                "pathMappings"   * [
                    {
                        "localRoot"   * "${workspaceFolder}",
                        "remoteRoot"   * "."
                    }
                ]
            },

-   In VS Code add a breakpoint anywhere you want.
-   Launch the script in FreeCAD. FreeCAD freeze waiting for attachment.
-   In VS Code start debugging using created configuration. You should see variables in debugger area.
-   When setting breakpoints, VS Code will complain about not finding the .py file opened in the VS Code editor.
    -   Change \"remoteRoot\"   * \".\" to \"remoteRoot\"   * \"\"
        -   For example, if the Python file resides in */home/FC\_myscripts/myscript.py*
        -   Change to   * \"remoteRoot\"   * \"/home/FC\_myscripts\"
    -   If you\'re just debugging FreeCAD macros from the FreeCAD macro folder, and that folder is \"C   */Users//AppData/Roaming/FreeCAD/Macro\", then use   *
        -   \"localRoot\"   * \"C   */Users//AppData/Roaming/FreeCAD/Macro\",
        -   \"remoteRoot\"   * \"C   */Users//AppData/Roaming/FreeCAD/Macro\"
-   If your macro can\'t find ptvsd despite having installed it somewhere precede \'import ptvsd\' with


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

Where the path is to the directory where ptvsd was installed.

-   On the left bottom edge of VSCode you can choose the Python executable - it\'s best to make this the version packaged with FreeCAD.

In the Mac package it is /Applications/FreeCAD.App/Contents/Resources/bin/python.

You can locate it on your system by typing


```python
import sys
print(sys.executable)
```

into FreeCAD\'s Python console.


</div>


</div>

### With LiClipse and AppImage 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

LiClipse Debugging →


<div class="mw-collapsible-content">

-   Extract AppImage.


```python
> ./your location/FreeCAD_xxx.AppImage --appimage-extract
> cd squashfs-root/
```

-   The sqashfs-root location is where the debugger later on is hooked up to.

-   Make sure you can start a FreeCAD session from within the squashfs-root location.


```python
squashfs-root> ./usr/bin/freecadcmd
```

-   Should start up a FreeCAD commandline session.

-   Install [LiClipse](https   *//www.liclipse.com/).
    -   Comes ready with pydev and has installers for all platforms.
    -   For linux it is just to extract (to any location) and run.

-   Configure liclipse for debugging.
    -   Right-click pydev icon (upper right corner) and choose customize.
        -   Activate \"PyDev Debug\" (through checkbox, or it might be needed to go to tab \"Action Set Availability\" and activate there first).
        -   In the pydev menu you can now choose \"start debug server\".
    -   Use menu window/open perspective/other \> debug.
        -   Right-click debug icon (upper right corner) and choose customize.
        -   Checking \"Debug\" brings the debugging navigation tools to the toolbar.
    -   Open preferences through menu window/preferences.
        -   In PyDev/Interpreters add \"new Interpreter by browsing\".
        -   The added interpreter should be   * `your loc/squashfs-root/usr/bin/python`.
        -   If you are only using this for fc, you can add AddOn workbench folders as well, or do that in a pydev-project later on.

-   Find path to `pydevd.py` in your liclipse installation.
    -   Something along the lines of   * `your location/liclipse/plugins/org.python.pydev.xx/pysrc`.
-   Create a regular pydev-project in liclipse.
    -   Import external sources, for example a macro that you want to debug, or an external workbench.
    -   In that macro (or workbench .py file) add the code lines   *

   *   
    
```python
    import sys; sys.path.append("path ending with /pysrc")
    import pydevd; pydevd.settrace()
    
```
    

   ** This is where the execution will halt when the macro is run.

-   Start the liclipse debug server (menu pydev).

-   Start FreeCAD.


```python
squashfs-root> ./usr/bin/freecad
```

-   Run the macro (or any other file with a `pydevd.settrace()` trigger) from within freecad, as you would normally do.

-   Happy debugging.

-   The use of LiClipse for remote debugging, and the steps described here related to liclipse, should work on any platform. The parts related to AppImage is for linux only.


</div>


</div>

## Debugging OpenCasCade 

For developers needing to dig deeper in to the OpenCasCade kernel, user \@abdullah has created a [thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=47017) orientation discussing how to do so.


<div class="mw-translate-fuzzy">





</div>


 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Debugging/sv
