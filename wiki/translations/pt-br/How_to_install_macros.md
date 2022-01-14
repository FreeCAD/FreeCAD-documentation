# How to install macros/pt-br
{{TutorialInfo
|Topic=Programming
|Level=Medium programmer
|Time=15 minutes
|FCVersion=All
|Author=[Mario52](User_Mario52.md)
}}

## Description

Since v0.17 it is easy to add macros by using the [Addon Manager](Std_AddonMgr.md). A regular user doesn\'t need to do more than use this tool. Keep reading for more information regarding installation of [macros](macros.md).

Macros are sequences of commands which are used to perform a complex drawing operation. Macros are [Python](Python.md) scripts, which means they are text files that can be written and edited with a text editor.

While Python scripts normally have the `.py` extension, FreeCAD macros should have the `.FCMacro` extension. A collection of macros written by experienced users is found in the [macros recipes](macros_recipes.md) page.

See [Introduction to Python](Introduction_to_Python.md) to learn about the Python programming language, and then [Python scripting tutorial](Python_scripting_tutorial.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) to learn about writing macros.

Here is a video on [installing FreeCAD macros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).

## The Macro menu and toolbar 

### Toolbar

-   <img alt="" src=images/Std_DlgMacroRecord.svg  style="width:32px;"> [Macro recording\...](Std_DlgMacroRecord.md)
-   <img alt="" src=images/Std_MacroStopRecord.svg  style="width:32px;"> [Stop macro recording](Std_MacroStopRecord.md)
-   <img alt="" src=images/Std_DlgMacroExecute.svg  style="width:32px;"> [Macros\...](Std_DlgMacroExecute.md)
-   <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:32px;"> [Execute macro](Std_DlgMacroExecuteDirect.md)

### Menu

Besides the tools in the toolbar, the following functions are also available in the **Macro** menu.

-   [Attach to remote debugger](Std_MacroAttachDebugger.md)
-   <img alt="" src=images/Std_MacroStartDebug.svg  style="width:32px;"> [Debug macro](Std_MacroStartDebug.md)
-   <img alt="" src=images/Std_MacroStopDebug.svg  style="width:32px;"> [Stop debugging](Std_MacroStopDebug.md)
-   [Step over](Std_MacroStepOver.md)
-   [Step into](Std_MacroStepInto.md)
-   [Toggle breakpoint](Std_ToggleBreakpoint.md)

## Macros directory 


<div class="toccolours mw-collapsible mw-collapsed">

Macros are created in a specific folder under the user\'s FreeCAD directory. This directory can be configured in the [Execute macro dialog](Std_DlgMacroExecute.md), or in the [Preferences Editor](Preferences_Editor.md), through the menu **Edit → Preferences → General → Macro → Macro recording settings**.

Downloaded macros should also be placed in this directory.


<div class="mw-collapsible-content">

### Default directory 

Macros can be simply copied into


```python
$ROOT_DIR/
```

where `$ROOT_DIR` is a top level directory searched by FreeCAD on startup.

The `$ROOT_DIR` could be a system wide directory, in which case the macro is installed for all users.

-   On Linux it is usually `/usr/share/freecad/`
-   On Windows it is usually `C:\Program Files\FreeCAD\`
-   On Mac OSX it is usually `/Applications/FreeCAD/`

The `$ROOT_DIR` could be a particular user\'s directory.

-   On Linux it is usually `/home/username/.FreeCAD/`
-   On Windows it is usually `C:\Users\username\Application Data\FreeCAD\`
-   On Mac OSX it is usually `/Users/username/Library/Preferences/FreeCAD/`

### Configuring the user directory 

1\. Open the menu **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Macros...](Std_DlgMacroExecute.md)** to open the [Execute macro dialog](Std_DlgMacroExecute.md).

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Opening the Execute macro dialog*

2\. Set the appropriate `User macros location`.

-   Linux: usually `/home/username/.FreeCAD/`
-   Windows: usually `C:\Users\username\AppData\Roaming\FreeCAD\`
-   MacOS: usually `/Users/username/Library/Preferences/FreeCAD/`

![](images/Dxf_Importer_Install_02.png ) 
*align=center|Setting of the macros directory*

3\. Navigate to that directory in your computer.

-   Linux: paste the address into your file manager, \"Nautilus\" or other. You may have to press **Ctrl**+**H** to make the hidden directory `.FreeCAD/` visible.
-   Windows: paste the address into your \"File explorer\" and confirm.
-   MacOS: locate the folder in the \"Finder\" or paste the address into a \"File explorer\"; remember the `file:///` prefix in the \"File explorer\" for a file on disk.

![](images/Dxf_Importer_Install_03.png ) 
*align=center|Accessing the macros directory in the operating system*

4\. Add macro files to this directory.

-   Linux: leave the file manager open, and bookmark the location for faster access.
-   Windows: leave open the file explorer.
-   MacOS: either leave a \"Finder\" window open, or bookmark the location in your \"File explorer\", or set up an \"Alias\" to point to it, or drag the folder into the \"SideBar\" of the \"Finder\" so it is there to use from other programs such as text editors.

![](images/Dxf_Importer_Install_04.png ) 
*align=center|Macros directory*





</div>


</div>

## Installing macros 


<div class="toccolours mw-collapsible mw-collapsed">

### Automatic method 

Starting with FreeCAD 0.17, use the [Addon Manager](Std_AddonMgr.md) in **Tools → Addon manager** to install a macro that has been included in the [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros) repository.


<div class="mw-collapsible-content">

In past versions of FreeCAD you could use two automated ways to install macros and other addons:

-   [addons\_installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons): itself a macro, this was the precursor to the Addon Manager, and is hosted in the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. You don\'t need to use this tool in new installations of FreeCAD.
-   [freecad-pluginloader](https://github.com/microelly2/freecad-pluginloader): also a macro, it could be used to install new components to FreeCAD. It is no longer developed.

The recommended way to install addons, that is, [external workbenches](external_workbenches.md) and macros, is the [Addon Manager](Std_AddonMgr.md). However, you can still add macros to your system with the manual methods described in the following sections; this is useful if you are developing and testing your own code.


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Manual method 1. Copy the code to the macro editor 

For macros that are relatively small, 300 lines or less, the code can be copied and pasted directly into the FreeCAD macro editor.


<div class="mw-collapsible-content">

We will use <img alt="" src=images/Part_Prism_Apothem.svg  style="width:24px;"> [Macro Apothem Based Prism GUI](Macro_Apothem_Based_Prism_GUI.md) as an example.

1\. Go to the macro wiki page, which should be listed in [Macros recipes](Macros_recipes.md).

If there is a custom icon download it; click on it with the right mouse button and select `Save image as...`; place the icon in the macros directory. This icon can be used as a shortcut for the macro in a [custom toolbar](Customize_Toolbars.md). The default icon is <img alt="" src=images/Text-x-python.png  style="width:24px;">.

![](images/Macro_Install_HowTo_28.png ) 
*align=center|Downloading the icon from the macro page*

2\. In the macro page, select the code inside the **Script** or **Macro** sections, and copy it.

3\. In FreeCAD, open the menu **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Macros...](Std_DlgMacroExecute.md)** to open the [Execute macro dialog](Std_DlgMacroExecute.md).

![](images/Dxf_Importer_Install_01.png ) 
*align=center|Opening the Execute macro dialog*

4\. Click **Create**.

![](images/Macro_Install_HowTo_17.png ) 
*align=center|Creating a new macro*

5\. Enter the macro name, here `Macro_Apothem_Based_Prism_GUI`, and press **OK**.

![](images/Macro_Install_HowTo_18.png ) 
*align=center|Entering the macro name*

6\. The macro editor opens, showing the full path of the new macro.

![](images/Macro_Install_HowTo_19.png ) 
*align=center|The macro editor*

7\. Paste the code in the editor window, and then click the cross on the tab to close the window.

![](images/Macro_Install_HowTo_20.png ) 
*align=center|Closing the macro editor*

8\. A window appears asking for confirmation to save the code; click on **Yes**. You can also use **Ctrl**+**S** to save the file.

Restart FreeCAD to correctly register the new macro.

![](images/Macro_Install_HowTo_27.png ) 
*align=center|Asking for confirmation to save the code*

9\. Open the menu again, **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Macros...](Std_DlgMacroExecute.md)**, select the new macro and press **Execute**.

![](images/Macro_Install_HowTo_21.png ) 
*align=center|Selecting the macro to run it*

10\. The macro now runs. Fill in the fields with your values and click the **OK** button.

![](images/Macro_Install_HowTo_22.png ) 
*align=center|The macro in action; fill in the information and press OK when ready*

11\. This macro should return an error if no document is active; other macros open a new document if none exists.

Create a new document with **File → <img src="images/Std_New.svg" width=16px> [New](Std_New.md)**, and then repeat the previous steps to execute the macro.

![](images/Macro_Install_HowTo_23.png ) 
*align=center|The macro returning an error if no document is active*

12\. Once an active document is available, the macro runs and creates an object.

![](images/Macro_Install_HowTo_24.png ) 
*align=center|Object created by the macro*

13\. You can open the macro in the editor again to run it or modify it. Go to **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Macros...](Std_DlgMacroExecute.md)**, select the macro and press **Edit**.

![](images/Macro_Install_HowTo_25.png ) 
*align=center|Opening the macro in the editor*

14\. The macro can now be run with **Macro → <img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Execute macro](Std_DlgMacroExecuteDirect.md)**, or by clicking on the **<img src="images/Std_DlgMacroExecuteDirect.svg" width=16px> [Std DlgMacroExecuteDirect](Std_DlgMacroExecuteDirect.md)** button in the toolbar.

![](images/Macro_Install_HowTo_26.png ) 
*align=center|Running the macro that is loaded in the editor*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### Manual method 2. Add a macro file from a compressed .zip file 

Some macros are too big that it\'s inconvenient to copy and paste them into the macro editor, or they cannot be hosted in the wiki. In this case, the code may be hosted somewhere else, in a Github repository, or in the [FreeCAD forum](https://forum.freecadweb.org/). The code may also be compressed into a `.zip` file, tarball `.tar.xz`, or other type of archive if it contains several files. If the code is distributed in this way, the archive should be extracted and the files placed in the macros directory.


<div class="mw-collapsible-content">

We will use <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro screw maker](Macro_screw_maker1_2.md) as an example.

1\. Download the compressed code from the forum, [Screw Maker](http://forum.freecadweb.org/viewtopic.php?f=22&t=6558#p52887).

You need to use a decompressor to get the internal files.

-   For Windows you can use an application like [7-zip](http://www.7-zip.org/) or [L-Zarc](http://www.kanmandet.dk/?p=37) or [quickzip](http://www.quickzip.org/quickzip51.html).
-   For Linux you can use a command from the terminal


```python
unzip your_file.zip -d your_directory
```

2\. Download the compressed archive with the macro code to a local folder.

![](images/Macro_Install_HowTo_01.png ) 
*align=center|Downloading the compressed archive to a local directory*

3\. Decompress the file in the folder.

![](images/Macro_Install_HowTo_02.png ) 
*align=center|Decompressing the file in the folder*

4\. The decompressor creates a new directory with the unpacked files.

![](images/Macro_Install_HowTo_03.png ) 
*align=center|New directory created after unpacking the archive*

5\. Go inside the new directory, and copy or cut the macro file.

![](images/Macro_Install_HowTo_04.png ) 
*align=center|Entering the newly created directory with the decompressed macro file*

6\. Go to the macro directory and paste the file there.

![](images/Macro_Install_HowTo_05.png ) 
*align=center|Placing the macro file in the macro directory*

7\. In FreeCAD, open the menu **Macro → <img src="images/Std_DlgMacroExecute.svg" width=16px> [Macros...](Std_DlgMacroExecute.md)** to open the [Execute macro dialog](Std_DlgMacroExecute.md).

![](images/Macro_Install_HowTo_06.png ) 
*align=center|Opening the Execute macro dialog*

8\. Select the new macro and press **Execute**.

![](images/Macro_Install_HowTo_07.png ) 
*align=center|Selecting the macro to run it*

9\. The macro now runs. Select the desired options, and click the **Create** button.

<img alt="" src=images/Macro_Install_HowTo_08.png  style="width:640px;"> 
*align=center|The macro in action; select the desired options, and press Create when ready*

![](images/Macro_Install_HowTo_30.png ) 
*align=center|Object created by the macro*


</div>


</div>

## Execute a macro in command line 


<div class="toccolours mw-collapsible mw-collapsed">

Command line execute a macro (.FCMacro or .py)


<div class="mw-collapsible-content">

on Windows


```python
"C:\Program Files\FreeCAD\bin\FreeCAD.exe" "C:\Users\userName\AppData\Roaming\FreeCAD\Mod\WorkFeature\start_WF.FCMacro"
```

on Linux


```python
todo
```


</div>


</div>

## Errors in macros 


<div class="toccolours mw-collapsible mw-collapsed">

### Indentation errors 

The white space at the beginning of the lines (indentation) in the [Python](Python.md) programming language is very important, and an integral part of the code. An inappropriate space may cause the code to not run or present errors.

This section describes some errors that may be encountered when copying and pasting, and writing macro code.


<div class="mw-collapsible-content">

A typical indentation error looks like this:


```python
<unknown exception traceback><type 'exceptions.IndentationError'>: ('expected an indented block', ('C:/Users/d/AppData/Roaming/FreeCAD/Macro_Apothem_Based_Prism_GUI.FCMacro', 21, 3, 'def priSm(self):\n'))
```

#### Example 1 

If the code lacks any indentation, the code won\'t work. Class (`class`) and function definitions (`def()`), as well as control structures (`if`, `while`, `for`) should be followed by a block of indented code.

This error is possible if the user doesn\'t copy the code correctly, and all spaces are accidentally removed.

![](images/Macro_Install_HowTo_09.png ) 
*align=center|Python code that lacks any indentation; it will cause an error when it's run*

Indentation problem fixed.

![](images/Macro_Install_HowTo_10.png ) 
*align=center|Python code with the correct indentation*

If the code is selected, all lines should be highlighted all the way to the left edge, indicating that the lines are aligned.

![](images/Macro_Install_HowTo_11.png ) 
*align=center|Python code highlighted, showing that all lines start at the left edge*

#### Example 2 

If an additional space is introduced at the beginning of all lines, the Python interpreter will fail and complain about unnecessary indentation. In this case, all lines need the initial space removed.

![](images/Macro_Install_HowTo_12.png ) 
*align=center|Python code with additional space on each line*

#### Example 3 

Here the code has been copied from a forum thread by using the **Select all** button. Apparently the selection is good.

![](images/Macro_Install_HowTo_14.png ) 
*align=center|Python code copied from a forum*

However, when the selection is pasted into the macro editor, undesirable indentation seems to appear.

![](images/Macro_Install_HowTo_15.png ) 
*align=center|Python code copied from a forum into the macro editor; unnecessary indentation is added*

In this case, the initial spaces need to be removed. This can be done with a specialized text editor to quickly decrease the indentation of the lines.

In Windows, [Notepad++](http://notepad-plus-plus.org/) can perform selection with **Alt** + Mouse dragging, and then use **Edit → Indent → Decrease the indentation**.

![](images/Macro_Install_HowTo_16.png ) 
*align=center|Python code with the correct indentation*

#### Example 4 

Here the selection also selects the line numbers in the code example. If this selection is pasted into the macro editor, it won\'t work. All line numbers need to be removed, and the spaces adjusted so that the Python code has the proper indentation.

![](images/Macro_Install_HowTo_29.png ) 
*align=center|Selection that also selects the line numbers; if this code is pasted into the macro editor, it won't work*

#### Good code 

![](images/Macro_Install_HowTo_13.png ) 
*align=center|Python code with the correct indentation*


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">

### No text output from macros 

Macros may output information to the report view to detail what the code is doing when it is running.

If no information is displayed, make sure the report view and [Python](Python.md) console are visible, and that the output is directed tot he report view.


<div class="mw-collapsible-content">

#### Printing information 

FreeCAD macros have two methods to print information to the report view.

The FreeCAD functions


```python
FreeCAD.Console.PrintMessage("Hello World! \n")
FreeCAD.Console.PrintError("Hello World! \n")
FreeCAD.Console.PrintWarning("Hello World! \n")
```

The simple Python function


```python
print("Hello World!")
```

#### Enabling the report view 

To see the information displayed in the console you should:

1\. Go to the menu **View → Panels**.

![](images/Macro_Install_HowTo_31.png )

![](images/Macro_Install_HowTo_32.png ) 
*align=center|Making the panels visible in the menu View → Panels*

2\. Enable the `Report view` and the `Python console`.

![](images/Macro_Install_HowTo_33.png ) 
*align=center|Enabling the report view and the Python console*

3\. The panels are now visible, and commands like `FreeCAD.Console.PrintMessage()` now print information that appears in the `Report view`.

![](images/Macro_Install_HowTo_34.png ) 
*align=center|FreeCAD main window with the Report view and the Python console*

#### Enabling the print() command 

FreeCAD may need to be configured so the `print()` function of [Python](Python.md) redirects its output correctly to the report view.

1\. Go into the [Preferences Editor](Preferences_Editor.md) with the menu **Edit → Preferences**.

![](images/Macro_Install_HowTo_35.png ) 
*align=center|Going into the preferences editor*

2\. Go to **General** section, and then **Output window → Python interpreter**.

![](images/Macro_Install_HowTo_36.png ) 
*align=center|Output window preferences*

3\. Check both boxes:

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Redirect internal Python output to report view

-   <img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Redirect internal Python errors to report view

and then press the **OK** button.

![](images/Macro_Install_HowTo_37.png ) 
*align=center|Redirecting the Python output to the report view*

![](images/Macro_Install_HowTo_38.png ) 
*align=center|Python commands printing information to the report view*


</div>


</div>


{{Powerdocnavi

}} 

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md) [<img src="images/Property.png" style="width:16px"> Python Code](Category_Python_Code.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > How to install macros/pt-br
