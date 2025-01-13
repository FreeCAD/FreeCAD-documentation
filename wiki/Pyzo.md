# Pyzo
## General Information 

### Motivation

Pyzo is a free and open-source Python IDE focused on interactivity and introspection, which makes it well-suited for engineering and scientific applications. This page describes how to use it in conjunction with FreeCAD.

![Screenshot of Pyzo running the FreeCAD Python Interpreter](images/Screenshot_pyzo.png )

### Pyzo

-   website: <https://pyzo.org>
-   GitHub repository: <https://github.com/pyzo/pyzo>
-   free and open-source (BSD)
-   fully coded in Python
-   available for Linux, MS Windows and macOS

### Versions

Unless otherwise noted, this page assumes the following software versions:

-   Pyzo 4.16.0
-   FreeCAD 0.21.2

## Set-Up and Configuration 

### Preparing a FreeCAD AppImage in Linux 

-   download the AppImage \--\> e.g.: FreeCAD_0.21.2-Linux-x86_64.AppImage

-    {{Incode|1=$ chmod +x ./FreeCAD_0.21.2-Linux-x86_64.AppImage}}
    

-    {{Incode|1=$ ./FreeCAD_0.21.2-Linux-x86_64.AppImage --appimage-extract}}
    

-    {{Incode|1=$ mv ./squashfs-root FreeCAD}}
    

-   \[some older Linux systems require: {{Incode|1=export FREECAD_USER_HOME=$HOME}}\]

-   create a bash script **python_freecad.sh** in **./FreeCAD** (in the same directory as bash script **AppRun**)

:   
    {{Code|lang=bash|code=
    #!/bin/bash
    HERE="$(dirname "$(readlink -f "${0}")")"
    ${HERE}/AppRun python "$@"
    }}
    

-   Start FreeCAD via via {{Incode|1=$ ./FreeCAD/AppRun}} and close it again so that the user config files are created properly.

Note that, on some Linux systems, the FreeCAD 0.21.2 AppImage reports an error \"MESA-LOADER: failed to open \...\" when being started. In that case execute {{Incode|1=$ rm ./FreeCAD/usr/lib/libdrm*}} after extracting and renaming the AppImage, as suggested [here](https://github.com/realthunder/FreeCAD/issues/960#issuecomment-1974233355).

### Installing Pyzo 

-   \[for MS Windows and macOS\] use the installer or extract the compressed archive from <https://github.com/pyzo/pyzo/releases>
-   or run it from source: Download the [Pyzo main branch as an archive](https://github.com/pyzo/pyzo/archive/refs/heads/main.zip), unpack the archive and then run {{Incode|python3 /path/to/pyzo-main/pyzolauncher.py}}. To use a specific Qt API instead of the automatically detected one, set environment variable \"QT_API\" before. Possible values are: pyside2, pyside6, pyqt5, pyqt6.
-   or install it as a Python module: {{Incode|python3 -m pip install pyzo}}

Linux users please run Pyzo from source because there could be library incompatibilities with the provided binary version of Pyzo, resulting in a crash when opening the file dialog.

See also the chapter \"Installation\" in the Pyzo ReadMe: <https://github.com/pyzo/pyzo#installation>

### Shell Configuration 

Start Pyzo and enter the shell configuration dialog via the Menu:
Shell -\> Edit shell configurations\...
A dialog window will appear. If there was no old shell configuration found, then Pyzo will create a single tab named \"Python\" with an empty \"exe\" textbox. Fill out this tab with the values provided below. Otherwise, if there is no tab with an empty \"exe\" textbox, press the button \"Add config\" on the top right corner, and then fill out the tab:

name
:   freecad (or something else)

exe \[for Windows\]

:   
    **C:\Program Files\FreeCAD 0.21\bin\python.exe**
    

exe \[for Linux\]

:   
    **/home/.../FreeCAD/python_freecad.sh**
    

exe \[for macOS\]

:   
    **/Applications/FreeCAD.app/Contents/Resources/bin/python**
    

:   Or, in case of this error: *Fatal Python error: take_gil: PyMUTEX(gil-\>mutex) failed*, try:

:   
    **/Applications/FreeCAD.app/Contents/Resources/bin/freecadcmd**
    

gui
:   PySide2

pythonPath \[for Windows and Linux\]
:   \[leave empty\]

pythonPath \[for macOS\]

:   
    **/Applications/FreeCAD.app/Contents/Resources/lib**
    

startupScript
:   select radio button \"Code to run at startup\"
:   enter the following code in the text field, replacing everything that was there before:
:   
    
```python
    from PySide2 import QtCore, QtWidgets
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts, True)
    # optional switches:
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    # AFTER_GUI - code below runs after integrating the GUI
    import os, sys
    if sys.platform == 'linux': # ... and using the (extracted) AppImage
        sys.path.append(os.environ['PATH_TO_FREECAD_LIBDIR'])
    # some older Linux systems require the following line:
    # os.environ['FREECAD_USER_HOME'] = os.environ['HOME']

    import FreeCAD as App
    import FreeCADGui as Gui
    App.ParamGet('User parameter:BaseApp/Preferences/OutputWindow').SetBool('RedirectPythonOutput', False)
    App.ParamGet('User parameter:BaseApp/Preferences/OutputWindow').SetBool('RedirectPythonErrors', False)
    Gui.showMainWindow()
    
```
    

environ:
:   enter the following environment variables:
:   
    {{Code|lang=text|code=
    PYZO_PROCESS_EVENTS_WHILE_DEBUGGING=1
    LC_NUMERIC=C
    }}
    

Finally, press button \"Done\" in the shell configuration dialog. Run a new \"freecad\" shell via Pyzo\'s \"Shell\" menu. This will start the FreeCAD Gui and a will open a FreeCAD Python shell in Pyzo.

On Linux, when not using an (extracted) AppImage, change {{Incode|sys.path.append(os.environ['PATH_TO_FREECAD_LIBDIR'])}} in the text field \"startupScript\" to e.g. {{Incode|sys.path.append('/builds/freecad-source/build/lib')}}, specifying the directory to the library files \"FreeCAD.so\" and \"FreeCADGui.so\". This library directory path could also be added to the field \"pythonPath\" in the Pyzo shell configuration dialog instead.

The environment variable entry {{Incode|PYZO_PROCESS_EVENTS_WHILE_DEBUGGING&#61;1}} will tell Pyzo to periodically update FreeCAD\'s Qt-GUI while FreeCAD is stopped during a breakpoint.

Do not remove the {{Incode|# AFTER_GUI}} comment in the newly entered startup code \-- this is a separator used by Pyzo to split the code into two blocks.

If you have an older Mac and pyzo fails to launch (e.g. pyzo 4.13.2 on OS-X 10.15), a possible work-around is to launch a patched pyzo 4.12.7 from the Terminal. See [FreeCAD forum message](https://forum.freecad.org/viewtopic.php?p=707159#p707159)

## General Pyzo Usage 

See <https://pyzo.org/guide.html> and run the Pyzo Wizard (Menu: Help -\> Pyzo Wizard) to get a short introduction.

Noteworthy information:

-   You can enter some \"magic\" commands in the Pyzo\'s Python shell, for example \"pip install sympy\". This also works with FreeCAD.
-   Ctrl+I in the shell (or clicking on the flash symbol) will send a KeyboardInterrupt. Ctrl+C is used for the normal copy function.
-   Press F5 or Ctrl+E to execute the whole file. But do not use \"Run file as script\" as this will restart the shell together with FreeCAD.
-   Press F9 to execute just the selected code.
-   Press F10 to execute the current line in the editor and print the result to the shell
-   Press Ctrl+Return to execute the current cell.
-   Right click on an editor tab will open a context menu.
-   Many keyboard shortcuts are similar to MATLAB.
-   The \"Logger\" tool (widget) has a shell to the Pyzo GUI\'s Python interpreter. You can fully access all objects there, for example copying a shell configuration via {{Incode|pyzo.config.shellConfigs2.insert(0, pyzo.config.shellConfigs2[1].copy())}}.
-   When there is a printed stack trace in the Python shell, double click the filename to open the file at the specific line number.
-   When dealing with performance critical code, avoid printing too much to the shell as stream outputs directed to the Pyzo IDE will slow down the execution.
-   There is no{{Incode|__file__}} variable defined in the interactive mode, but as a workaround you can run {{Incode|import inspect; __file__ &#61; inspect.getfile(inspect.currentframe())}} to get it.
-   In Pyzo\'s \"About\" dialog (Help -\> About Pyzo) you can see the folder where Pyzo stores the settings.
-   Pyzo can be configured to be portable, e.g to run it from a usb pen-drive with encapsulated settings. To enable this, rename the folder \"\_settings\" in Pyzo\'s application folder to \"settings\".
-   You can directly modify Pyzo\'s source code even in the binary distribution because the binary is just a Python-Interpreter that runs the Python source code in the installation directory.

## Example Work Flows 

A normal workflow to automate FreeCAD operations is similar to using just FreeCAD. The shell in Pyzo has access to the same Python interpreter as the \"Python console\" panel in the FreeCAD GUI. Both can be used in a mixed fashion, whatever is more convenient in the situation.

Pyzo brings very nice features to this workflow, just to list some of them:

-   Write a new function in the editor, set a breakpoint and run the code. You can now work inside the function\'s scope and continue your workflow even manipulating objects manually in FreeCAD.
-   If you started an (almost) endless loop, you can interrupt the execution by pressing Ctrl+I in Pyzo (\"Shell -\> Interrupt\" in the menu). You also can pause execution, inspect/modify data and resume execution \-- press the pause button in the shell\'s toolbar (\"Shell -\> Pause\" in the menu).
-   You can have some code fragments prepared in the Pyzo editor tabs and execute individual cells. Try new commands and add them to the code editor to grow your new script.
-   The command history in the Pyzo shell is not cluttered with auto-generated commands but you can still access the automatically inserted comments in the FreeCAD Python panel.
-   If there was an exception which made your code abort execution, just do a post-mortem debug and watch all the variables in different stack layers to find out the cause of the error.

Have a look [here](https://forum.freecad.org/viewtopic.php?p=679419#p679419) and [here](https://forum.freecad.org/viewtopic.php?p=679580#p679580) to see this in action (with an older version where the FreeCAD start was not yet included in the Pyzo shell configuration).

### Example for manipulating an object in a shape generation macro 

1.  Start Pyzo with FreeCAD, switch to the Part workbench and create a new file.
2.  Open file \"Mod/Part/BasicShapes/Shapes.py\" (inside the FreeCAD folder) in Pyzo.
3.  Set a breakpoint at line 37 ({{Incode|inner_cylinder &#61; Part.makeCylinder(innerRadius, height)}}).
4.  Apply the breakpoints, for example by pressing Return in the shell in Pyzo.
5.  In FreeCAD, run \"Part -\> Primitives -\> Create tube\".
6.  Function \"makeTube\" is now interrupted via the breakpoint.
7.  Execute the command {{Incode|outer_cylinder.rotate((0, 0, 0), (0, 1, 0), 45)}} in Pyzo\'s shell.
8.  Continue execution, e.g. via \"Shell -\> Debug continue\"
9.  Now you have a cylinder with a misaligned hole.

### Example for skipping code in a shape generation macro 

1.  Start Pyzo with FreeCAD, switch to the Part workbench and create a new file.
2.  Open file \"Mod/Part/BasicShapes/Shapes.py\" (inside the FreeCAD folder) in Pyzo.
3.  Set a breakpoint at line 37 ({{Incode|inner_cylinder &#61; Part.makeCylinder(innerRadius, height)}}).
4.  Apply the breakpoints, for example by pressing Return in the shell in Pyzo.
5.  In FreeCAD, run \"Part -\> Primitives -\> Create tube\".
6.  Function \"makeTube\" is now interrupted via the breakpoint.
7.  In Pyzo, set the text cursor to line 39 ({{Incode|return shape}}).
8.  Run \"Shell -\> Debug jump\" or click the new icon in the shell\'s toolbar.
9.  Continue execution, e.g. via \"Shell -\> Debug continue\"
10. Now you have a cylinder instead of a pipe because you skipped creating the inner cylinder and cutting it.

### Example for using breakpoints in callbacks 

This is a step-by-step demonstration of how breakpoints can be used to debug callbacks in FeaturePython objects.

1.  Copy the full example code from <https://wiki.freecad.org/Create_a_FeaturePython_object_part_II#Complete_code> and save it to a file (to have a module), e.g. /tmp/mymodules/mytest.py
2.  Start Pyzo with a FreeCAD shell and wait till the FreeCAD GUI is fully loaded.
3.  Run the following commands in the Pyzo shell (or in the Python console panel in FreeCAD\'s GUI): 
```pythonimport sys
    sys.path.append('/tmp/mymodules')

    import mytest

    doc = App.newDocument()
    mytest.create('abcde')
    
```
4.  Open file \"/tmp/mymodules/mytest.py\" in Pyzo (if not already open).
5.  Set a breakpoint at the line {{Incode|1=obj.Shape = ...}} in method {{Incode|execute(self, obj)}} of class {{Incode|Box}}.
6.  Breakpoints are updated in Pyzo when giving a command to execute code (or continuing execution when the debugger is active). Therefore run the dummy code {{Incode|pass}} in Pyzo\'s shell or just press Return there so that the breakpoint will be applied.
7.  Switch to the FreeCAD GUI, select object \"abcde\" and change the value of property \"Height\", for example from 10 to 20 mm.
8.  Now, the breakpoint is triggered. Switch to Pyzo and inspect the value of obj.Height by executing {{Incode|obj.Height}} in the shell. Change the value by executing {{Incode|1=obj.Height = 400}} and continue execution via \"Shell -\> Debug continue\". Switch back to the FreeCAD GUI \-- the box shape now has a height of 400 mm.

### Example for monkey patching FeaturePython objects 

Normally, the code for FeaturePython objects is part of a module. Once FreeCAD objects are created, changes to the code in the module will only take effect after closing the FCStd-file, reloading the module, and re-opening the FCStd file.

To make quick iteration cycles during development of FeaturePython code, a monkey patching strategies can be used, as demonstrated with the following example.

First we create the module with the FeaturePython object\'s code. Create a new python script with the following code and save it into your user macros directory as \"mymod.py\".


<div style="height:20em; width:100%; overflow:auto; border: 1px solid #000">


```python
import FreeCAD as App


def create(obj_name):
    obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)
    MyBox(obj)
    App.ActiveDocument.recompute()
    return obj


class MyBox():
    def __init__(self, obj):
        self.Type = self.__class__.__name__
        obj.Proxy = self

    def execute(self, obj):
        # called on document recompute
        self.my_computations(obj)

    ## start of code for monkeypatching

    def my_computations(self, obj):
        print(obj.Label, 'aaa')

    if '__module__' not in dir():
        def _monkeypatch_method(classname, method):
            import inspect, os, sys
            __this_file__ = os.path.abspath(inspect.getfile(inspect.currentframe()))
            for mod in sys.modules.values():
                if __this_file__.startswith(getattr(mod, '__file__', None) or '_'):
                    setattr(getattr(mod, classname), method.__name__, method)
        _monkeypatch_method('MyBox', my_computations)

    ## end of code
    
```


</div>

We assume that, at this point, your already have started FreeCAD via Pyzo. Execute the following code (either in Pyzo\'s FreeCAD-shell or in FreeCAD\'s Python console panel): 
```python
import mymod

doc = App.newDocument()
mymod.create('obj1')
mymod.create('obj2')

doc.recompute()
``` Now, everytime you recompute one of the two created FeaturePython objects, the object\'s label and \"aaa\" will be printed in Pyzo\'s shell.

We want to quickly change the behavior of the FeaturePython object so that it prints \"bbb\" instead of \"aaa\". Open the module in Pyzo\'s editor (if not already opened) and change the string literal \"aaa\" to \"bbb\". To apply these changes, just execute that cell (which is defined by the two \"##\" comment lines) in Pyzo by pressing Ctrl+Return. Recompute the objects, and we have the desired result. Editing the method and executing the cell can now be repeated as often as desired. Debugging also works normally, e.g. using breakpoints. If you want set breakpoints below the code cell, there might be a line offset because the rest of the class definition is not updated. A nice aspect of this strategy is that the code is directly modified in the real module, so when just saving the module, restarting FreeCAD and re-opening the FCStd file, you already have the newest version without any monkey patching.

## Advanced Topics 

### Creating a Custom Tool 

![Custom tool example \"MyRunner\" in Pyzo](images/PyzoMyRunner.png )

Pyzo includes a Plug-In concept to extend its features without patching its source code.

See the example code in the Pyzo repository:

<https://github.com/pyzo/pyzo/blob/main/pyzo/resources/tool_examples/myRunner.py>

### Debugging Start-Up of FreeCAD Modules 

To debug the init script of a FreeCAD Mod, e.g. files such as **Mod/Draft/Init.py** or **Mod/Draft/InitGui.py** using breakpoints, we need to set a breakpoint in the code file. These init script files are not directly executed.

During startup, FreeCAD runs the Python scripts **src/App/FreeCADInit.py** and **src/Gui/FreeCADGuiInit.py**, and each of these reads the corresponding init scripts (App and Gui) of the Mod and executes them as a string with the code contents:


```python
with open(file=InstallFile, encoding="utf-8") as f:
    exec(f.read())
```

The interpreter has no more information about the filepath of the executed code. To include the filepath, we need to patch the lines above. FreeCAD version 0.22 or newer [already contain this patch](https://github.com/FreeCAD/FreeCAD/pull/10618).

This is not all. The scripts **src/App/FreeCADInit.py** and **src/Gui/FreeCADGuiInit.py** are not individual files anymore but resource files in libraries in the distributed binary versions of FreeCAD. Therefore we will extract them into files and replace the data in the libraries with a short Python script that will call our new out-sourced scripts. So we could also open these new files and set breakpoints there.

The following code will extract the scripts from the libraries, patch them and place the caller code back in the libraries:


<div style="height:20em; overflow:auto; border: 1px solid #000">


```python
import os
import sys
import shutil


lib_dirpath = '/home/.../FreeCAD/usr/lib' # example for linux os
# lib_dirpath = r'C:\ProgramData\FreeCAD\bin' # example for windows os

restore_original_libs = False
# restore_original_libs = True


lib_dirpath = os.path.abspath(lib_dirpath)
for appgui in ['App', 'Gui']:
    if sys.platform == 'linux':
        fp = os.path.join(lib_dirpath, 'libFreeCAD{}.so'.format(appgui))
    elif sys.platform == 'win32':
        fp = os.path.join(lib_dirpath, 'FreeCAD{}.dll'.format(appgui))
    else: raise NotImplementedError()

    fp_backup = fp + '.orig'

    if restore_original_libs:
        shutil.copy(fp_backup, fp)
        continue

    if not os.path.isfile(fp_backup):
        shutil.copy(fp, fp_backup)

    with open(fp_backup, 'rb') as fd:
        dd = fd.read()

    if appgui == 'App':
        needle = b'\n# FreeCAD init module\n'
        fp_py = fp + '.FreeCADInit.py'
    else:
        needle = b'\n# FreeCAD gui init module\n'
        fp_py = fp + '.FreeCADGuiInit.py'

    i_needle = dd.index(needle)
    assert dd.find(needle, i_needle + 1) == -1

    i_start = i_needle - dd[:i_needle][::-1].index(b'\x00')
    i_end = dd.index(b'\x00', i_needle)

    dd_code = dd[i_start:i_end]

    fp_py_orig = fp_py + '.orig'
    with open(fp_py_orig, 'wb') as fd:
        fd.write(dd_code)

    loader_code = '\n'.join([
        'fp = ' + repr(fp_py),
        'with open(fp, "rt", encoding="utf-8") as fd: source = fd.read()',
        'exec(compile(source, fp, "exec"))',
        ]).format(repr(fp_py))

    dd_code_new = loader_code.encode('utf-8')
    assert len(dd_code_new) <= len(dd_code)
    dd_code_new += b'\x00' * (len(dd_code) - len(dd_code_new))

    dd_new = dd[:i_start] + dd_code_new + dd[i_end:]
    assert len(dd_new) == len(dd)

    with open(fp, 'wb') as fd:
        fd.write(dd_new)


    tt_code = dd_code.decode('utf-8')

    needle = """
                with open(file=InstallFile, encoding="utf-8") as f:
                    exec(f.read())
    """

    needle_patched = """
                with open(InstallFile, 'rt', encoding='utf-8') as f:
                    exec(compile(f.read(), InstallFile, 'exec'))
    """

    if needle in tt_code:
        # older FreeCAD versions < 0.22 need to be patched
        tt_code = tt_code.replace(needle, needle_patched)
    else:
        assert needle_patched in tt_code

    with open(fp_py, 'wt', encoding='utf-8') as fd:
        fd.write(tt_code)

```


</div>

We can now, for example, open **Mod/Draft/Init.py** in Pyzo, set a breakpoint there in line 26 and start the FreeCAD shell in Pyzo. Execution will be interrupted at the breakpoint. We can switch the stack frames, view and manipulate variables and step/continue the code execution.

## Pyzo customizations developed by FreeCAD users 

### Workspace2 by TheMarkster et al. 

<https://forum.freecad.org/viewtopic.php?p=720709#p720709>

A modified \"workspace\" tool that adds filters and a watchlist.

### WorkspaceWatch by heda 

<https://forum.freecad.org/viewtopic.php?p=774260#p774260>

A modified \"workspace\" tool that adds an extra treeview widget for displaying \"watched\" variables.

### GitBashTool by TheMarkster 

<https://forum.freecad.org/viewtopic.php?p=774810#p774810>

Displays a push button to open a git bash shell in the path of the file in the current editor.

## Known Limitations and Issues 

### General issues caused by importing FreeCAD as a module in Python 

-   auto backups are not enabled \--\> save often
-   for FreeCAD \< v0.22: custom FreeCAD Qt-GUI color themes are not available

### Wrong scaling for the FreeCAD GUI on multiple screens with different resolutions 

problem description
:   <https://forum.freecad.org/viewtopic.php?p=774781#p774781>

solution
:   <https://forum.freecad.org/viewtopic.php?p=774803#p774803>
:   <https://forum.freecad.org/viewtopic.php?p=774972#p774972>

### Fontconfig related crash when switching to the Draft workbench because of third-party software \"Graphviz\" 

problem description
:   <https://forum.freecad.org/viewtopic.php?p=776449#p776449>

solution
:   <https://forum.freecad.org/viewtopic.php?p=776751#p776751>

## Feedback

To ask questions about this topic, share ideas, give input, point out mistakes, etc, please write a message to [the initial topic in the FreeCAD forum](https://forum.freecad.org/viewtopic.php?t=78047) or create a new one.

## Miscellaneous Links 

-   [Official Pyzo Website](https://pyzo.org)
-   [Pyzo GitHub Repository](https://github.com/pyzo/pyzo)
-   [initial topic in the FreeCAD forum](https://forum.freecad.org/viewtopic.php?t=78047)
-   [Python_Development_Environment](Python_Development_Environment.md)
-   [Debugging#Python_Debugging](Debugging#Python_Debugging.md)
-   [Embedding_FreeCAD](Embedding_FreeCAD.md)



---
⏵ [documentation index](../README.md) > Pyzo
