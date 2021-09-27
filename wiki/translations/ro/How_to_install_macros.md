# How to install macros/ro
<div class="mw-translate-fuzzy">


{{TutorialInfo/ro|Topic=Programming|Level=Medium programmer|Time=15 minutes|FCVersion=All|Author=_}}


</div>


<div class="mw-translate-fuzzy">

## Descriere

Acest tutorial scurt vă va arăta cum să instalați și să utilizați macrocomenzile FreeCAD.


</div>

Since v0.17 it is easy to add macros by using the [Addon Manager](Std_AddonMgr.md). A regular user doesn\'t need to do more than use this tool. Keep reading for more information regarding installation of [macros](macros.md).

Macros are sequences of commands which are used to perform a complex drawing operation. Macros are [Python](Python.md) scripts, which means they are text files that can be written and edited with a text editor.

While Python scripts normally have the `.py` extension, FreeCAD macros should have the `.FCMacro` extension. A collection of macros written by experienced users is found in the [macros recipes](macros_recipes.md) page.

See [Introduction to Python](Introduction_to_Python.md) to learn about the Python programming language, and then [Python scripting tutorial](Python_scripting_tutorial.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md) to learn about writing macros.

Here is a video on [installing FreeCAD macros in Ubuntu](https://wiki.opensourceecology.org/wiki/Installing_Macros_in_FreeCAD).


<div class="mw-translate-fuzzy">

## Meniul Macro Menu și Iconițele Instrumentelor 


</div>

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


<div class="mw-translate-fuzzy">

## Locația și destinația mcrocomanzilor 


</div>


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


<div class="mw-translate-fuzzy">

**1 :** click **Menu \> Macro \> Macros** (which has the icon <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:24px;"> and the tool tip \"Open a dialog to let you execute a recorded macro\")


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Dxf_Importer_Install_01.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**3 :** The address of \"Macro destination\" (**C:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\** in the screen snapshot below)

-   Windows: the form is usually **drive:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\**
-   Ubuntu: the form is usually **/home/your\_user\_name/.FreeCAD**
-   Macintosh: the form is usually \"/Users/your\_user\_name/Library/Preferences/FreeCAD\"


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Dxf_Importer_Install_02.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**5 :** View the macro folder by:

-   Windows: paste the address into your File explorer and confirm
-   Macintosh: locate the folder in the Finder or paste the address into a File explorer (remember the \"<file:///>\" prefix in the File explorer for a file on disk)


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Dxf_Importer_Install_03.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**6 :** Access the files by:

-   Windows: leave open the file explorer
-   Macintosh: either leave a Finder window open, or bookmark the location in your File explorer, or set up an Alias to point to it, or drag the folder into the SideBar of the Finder so it is there to use from other programs such as text editors etc. (Note: version 0.14 of FreeCAD does not support Aliases but does support the SideBar)


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Dxf_Importer_Install_04.png  style="width:640px;"> 


</div>





</div>


</div>

## Installing macros 


<div class="toccolours mw-collapsible mw-collapsed">

### Automatic method 

Starting with FreeCAD 0.17, use the [Addon Manager](Addon_Manager.md) in **Tools → Addon manager** to install a macro that has been included in the [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros) repository.


<div class="mw-collapsible-content">

In past versions of FreeCAD you could use two automated ways to install macros and other addons:

-   [addons\_installer.FCMacro](https://github.com/FreeCAD/FreeCAD-addons): itself a macro, this was the precursor to the Addon Manager, and is hosted in the [FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons) repository. You don\'t need to use this tool in new installations of FreeCAD.
-   [freecad-pluginloader](https://github.com/microelly2/freecad-pluginloader): also a macro, it could be used to install new components to FreeCAD. It is no longer developed.

The recommended way to install addons, that is, [external workbenches](external_workbenches.md) and macros, is the [Addon Manager](Addon_Manager.md). However, you can still add macros to your system with the manual methods described in the following sections; this is useful if you are developing and testing your own code.


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">


<div class="mw-translate-fuzzy">


<div class="toccolours mw-collapsible mw-collapsed">

## Method copy the code in one window and paste in the FreeCAD editor 


<div class="mw-collapsible-content">


</div>

For macros that are relatively small, 300 lines or less, the code can be copied and pasted directly into the FreeCAD macro editor.


<div class="mw-collapsible-content">

We will use <img alt="" src=images/Part_Prism_Apothem.svg  style="width:24px;"> [Macro Apothem Based Prism GUI](Macro_Apothem_Based_Prism_GUI.md) as an example.


<div class="mw-translate-fuzzy">

If there are one or more icon (s) download also position your mouse over the icon, click the right mouse button and click \"Save image as \...\" the icon or icons are placed in the macro directory and one of these icons serve as a shortcut icon to place on the [toolbar.](Customize_Toolbars.md)


</div>

If there is a custom icon download it; click on it with the right mouse button and select `Save image as...`; place the icon in the macros directory. This icon can be used as a shortcut for the macro in a [custom toolbar](Customize_Toolbars.md). The default icon is <img alt="" src=images/Text-x-python.png  style="width:24px;">.


<div class="mw-translate-fuzzy">

<img alt="Download icon" src=images/Macro_Install_HowTo_28.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

After copying your code we will paste the code in FreeCAD editor.


</div>


<div class="mw-translate-fuzzy">

**1 :** Open FreeCAD and open the editor in FreeCAD


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Dxf_Importer_Install_01.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**2 :** The window macros file opens, click **Create** button


</div>


<div class="mw-translate-fuzzy">

<img alt="The window macros file opens" src=images/Macro_Install_HowTo_17.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

**3 :** A new window opens, enter the macro name (here \"**Macro\_Apothem\_Based\_Prism\_GUI**\")and click the create **Ok** button


</div>


<div class="mw-translate-fuzzy">

<img alt="enter the macro name" src=images/Macro_Install_HowTo_18.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

**4 :** The editing window FreeCAD macros is now available and has the name of our future macro.


</div>


<div class="mw-translate-fuzzy">

<img alt="The editing window FreeCAD macros" src=images/Macro_Install_HowTo_19.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**5 :** Paste your code in the macro editor window and click the little **cross** to close the window.


</div>


<div class="mw-translate-fuzzy">

<img alt="close the window" src=images/Macro_Install_HowTo_20.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**6 :** A warning window appears asking for confirmation of save code, click on **Yes**


</div>

Restart FreeCAD to correctly register the new macro.


<div class="mw-translate-fuzzy">

<img alt="A warning window appears asking for confirmation of save code" src=images/Macro_Install_HowTo_27.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

**7 :** Repeat the number **1 :** , Click on your new macro and button **Execute**


</div>


<div class="mw-translate-fuzzy">

<img alt="Click on your new macro and button Execute" src=images/Macro_Install_HowTo_21.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

**8 :** The macro runs, complete the fields with your values and click the **OK** button


</div>


<div class="mw-translate-fuzzy">

<img alt="The macro runs, complete the fields" src=images/Macro_Install_HowTo_22.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

9 : The macro returns an error ! we do not have to open document, open a document <img alt="" src=images/Document-new.svg  style="width:24px;"> and repeat the operation **7** and **8**. Some macros open a new document if it does not find one.


</div>

Create a new document with **File → <img src="images/Std_New.svg" width=16px> [New](Std_New.md)**, and then repeat the previous steps to execute the macro.


<div class="mw-translate-fuzzy">

<img alt="The macro returns an error!" src=images/Macro_Install_HowTo_23.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

10 : Here is your prism


</div>


<div class="mw-translate-fuzzy">

<img alt="your prism" src=images/Macro_Install_HowTo_24.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

11 : You can also open your macro in the editor to run or modify, click the **Edit** button


</div>


<div class="mw-translate-fuzzy">

<img alt="You can also open your macro in the editor" src=images/Macro_Install_HowTo_25.png  style="width:300px;">


</div>

12: The macro is now in the FreeCAD editor you can run through the menu \"Macro Run Macro\" or by clicking on the triangle <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:16px;"> green in the macros toolsbar


<div class="mw-translate-fuzzy">

<img alt="The macro is now in the FreeCAD editor" src=images/Macro_Install_HowTo_26.png  style="width:640px;">


</div>


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">


<div class="mw-translate-fuzzy">


<div class="toccolours mw-collapsible mw-collapsed">

## Method macro in a compressed .ZIP file 


<div class="mw-collapsible-content">


</div>


<div class="mw-translate-fuzzy">

Download the file compressed here (example) _)


</div>


<div class="mw-collapsible-content">

We will use <img alt="" src=images/Text-x-python.png  style="width:24px;"> [Macro screw maker](Macro_screw_maker1_2.md) as an example.

1\. Download the compressed code from the forum, [Screw Maker](http://forum.freecadweb.org/viewtopic.php?f=22&t=6558#p52887).


<div class="mw-translate-fuzzy">

Free for Windows [7-zip](http://www.7-zip.org/) ou [L-Zarc](http://www.kanmandet.dk/?p=37) ou [quickzip](http://www.quickzip.org/quickzip51.html)


</div>


```python
unzip your_file.zip -d your_directory
```


<div class="mw-translate-fuzzy">

**1 :** Download your file in your local folder here the folder **Temp**


</div>


<div class="mw-translate-fuzzy">

<img alt="Download your file in your local folder here the folder Temp" src=images/Macro_Install_HowTo_01.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**2 :** Unzip your file in the folder.


</div>


<div class="mw-translate-fuzzy">

<img alt="Unzip your file in the folder. " src=images/Macro_Install_HowTo_02.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**3 :** The decompressor finished his work and created a new folder with the unpacked file


</div>


<div class="mw-translate-fuzzy">

<img alt="The decompressor finished his work and created a new folder with the unpacked file" src=images/Macro_Install_HowTo_03.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**4 :** Enter in the newly created directory, move about the file, click the right mouse button and click on **Cut**.


</div>


<div class="mw-translate-fuzzy">

<img alt="Enter in the newly created directory" src=images/Macro_Install_HowTo_04.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**5 :** Return to your File explorer remained open in the macro location (here **C:\\Users\\your\_user\_name\\AppData\\Roaming\\FreeCAD\\**) and close the File explorer.


</div>


<div class="mw-translate-fuzzy">

<img alt="Return to your File explorer remained open" src=images/Macro_Install_HowTo_05.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**6 :** Open FreeCAD click **Menu \> Macro \> Macros** or the click the **bottom** <img alt="" src=images/Std_DlgMacroExecuteDirect.svg  style="width:18px;"> \"Open a dialog to let you execute a macro Recorded\"


</div>


<div class="mw-translate-fuzzy">

<img alt="Open FreeCAD" src=images/Macro_Install_HowTo_06.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**7 :** The macros window open , select your macro and click the button **Execute**


</div>


<div class="mw-translate-fuzzy">

<img alt="The macros window open" src=images/Macro_Install_HowTo_07.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**8 :** Your macro is executed enter the data and click the **Create** button


</div>


<div class="mw-translate-fuzzy">

<img alt="Your macro is executed" src=images/Macro_Install_HowTo_08.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

<img alt="Whaouu" src=images/Macro_Install_HowTo_30.png  style="width:640px;">


</div>


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


<div class="mw-translate-fuzzy">

## The indentation errors examples wrong code 


<div class="mw-collapsible-content">


</div>


<div class="mw-translate-fuzzy">

Indentarea în programarea python este foarte importantă și este parte integrantă a codului, un spațiu sau o schimbare necorespunzătoare provoacă o eroare de indentare de ex,:


</div>

This section describes some errors that may be encountered when copying and pasting, and writing macro code.


<div class="mw-collapsible-content">


<div class="mw-translate-fuzzy">

 **\<type \'exceptions.IndentationError\'\>: (\'expected an indented block\', (\'C:/Users/d/AppData/Roaming/FreeCAD/Macro\_Apothem\_Based\_Prism\_GUI.FCMacro\', 21, 3, \'def priSm(self):\\n\'))** 


</div>


```python
<unknown exception traceback><type 'exceptions.IndentationError'>: ('expected an indented block', ('C:/Users/d/AppData/Roaming/FreeCAD/Macro_Apothem_Based_Prism_GUI.FCMacro', 21, 3, 'def priSm(self):\n'))
```


<div class="mw-translate-fuzzy">

**1 :** In this example, the code was stuck without any indentation and of course does not work! here definitely a programmer error when pasting the code on the page as it would have never known it to work.


</div>

If the code lacks any indentation, the code won\'t work. Class (`class`) and function definitions (`def()`), as well as control structures (`if`, `while`, `for`) should be followed by a block of indented code.

This error is possible if the user doesn\'t copy the code correctly, and all spaces are accidentally removed.


<div class="mw-translate-fuzzy">

![the code was stuck without any indentation](images/Macro_Install_HowTo_09.png )


</div>


<div class="mw-translate-fuzzy">

**2 :** the code was correct indentations in the right place.


</div>


<div class="mw-translate-fuzzy">

![the code was correct indentations in the right place](images/Macro_Install_HowTo_10.png )


</div>


<div class="mw-translate-fuzzy">

**3 :** we select the code, and we see that the selection is at the edge of the code, the macro must works so good


</div>


<div class="mw-translate-fuzzy">

![the macro must works so good](images/Macro_Install_HowTo_11.png )


</div>


<div class="mw-translate-fuzzy">

**4 :** Here additional space is selected (it can happen) then you need to copy the code into a word processor to remove **one space all lines**


</div>

If an additional space is introduced at the beginning of all lines, the Python interpreter will fail and complain about unnecessary indentation. In this case, all lines need the initial space removed.


<div class="mw-translate-fuzzy">

![remove one space all lines](images/Macro_Install_HowTo_12.png )


</div>


<div class="mw-translate-fuzzy">

**5 :** Here the code has been copied in a forum window with the **Select all** button apparently the selection is good


</div>

Here the code has been copied from a forum thread by using the **Select all** button. Apparently the selection is good.


<div class="mw-translate-fuzzy">

<img alt="Here the code has been copied in a forum" src=images/Macro_Install_HowTo_14.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**6 :** But the selection pasted into the FreeCAD editor gives a surprise, an indent of four spaces has been added by the system ? the code is not good


</div>


<div class="mw-translate-fuzzy">

<img alt="But the selection pasted into the FreeCAD editor gives a surprise" src=images/Macro_Install_HowTo_15.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**7 :** You must delete all the extra space that is four spaces on each line, for Windows word processing [notepad-plus-plus](http://notepad-plus-plus.org/) enables vertical selection with a combination of buttons **Alt** + Mouse dragging or Menu\> Edit\> Indent\> Decrease the indentation


</div>

In Windows, [Notepad++](http://notepad-plus-plus.org/) can perform selection with **Alt** + Mouse dragging, and then use **Edit → Indent → Decrease the indentation**.


<div class="mw-translate-fuzzy">

<img alt="You must delete all the extra space" src=images/Macro_Install_HowTo_16.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**8 :** Here the selection also take the column numbers which will also give an error


</div>

Here the selection also selects the line numbers in the code example. If this selection is pasted into the macro editor, it won\'t work. All line numbers need to be removed, and the spaces adjusted so that the Python code has the proper indentation.


<div class="mw-translate-fuzzy">

<img alt="Here the selection also take the column numbers" src=images/Macro_Install_HowTo_29.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**9 :** Perfect code.


</div>


<div class="mw-translate-fuzzy">

![Perfect code](images/Macro_Install_HowTo_13.png )


</div>


</div>


</div>


<div class="toccolours mw-collapsible mw-collapsed">


<div class="mw-translate-fuzzy">


<div class="toccolours mw-collapsible mw-collapsed">

## For those who see no information is displayed. 


<div class="mw-collapsible-content">

Some macros display information on the screen in general they are displayed in the report view.


</div>

Macros may output information to the report view to detail what the code is doing when it is running.

If no information is displayed, make sure the report view and [Python](Python.md) console are visible, and that the output is directed tot he report view.


<div class="mw-collapsible-content">

#### Printing information 

FreeCAD macros have two methods to print information to the report view.


<div class="mw-translate-fuzzy">

**1 : Commands**


</div>


```python
FreeCAD.Console.PrintMessage("Hello World! \n")
FreeCAD.Console.PrintError("Hello World! \n")
FreeCAD.Console.PrintWarning("Hello World! \n")
```


<div class="mw-translate-fuzzy">

or


</div>


```python
print("Hello World!")
```


<div class="mw-translate-fuzzy">

To see the information displayed in the console you should:


</div>


<div class="mw-translate-fuzzy">

**1 :** Open FreeCAD


</div>


<div class="mw-translate-fuzzy">

<img alt="Open FreeCAD" src=images/Macro_Install_HowTo_31.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

<img alt="Click the View menu and Views" src=images/Macro_Install_HowTo_32.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**3 :** Check **Report View** and **Python Console**


</div>


<div class="mw-translate-fuzzy">

<img alt="Check Report View and Python Console" src=images/Macro_Install_HowTo_33.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**4 :** the windows are enabled and available commands like \"**App.Console.PrintMessage**\" is configured to the \"Report View\"


</div>


<div class="mw-translate-fuzzy">

<img alt="Hello World!" src=images/Macro_Install_HowTo_34.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**2 : command \"print\" which is a Python command.**


</div>


<div class="mw-translate-fuzzy">

**1 :** Click the **Edit menu** and then **Preferences**


</div>


<div class="mw-translate-fuzzy">

<img alt="Edit menu" src=images/Macro_Install_HowTo_35.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**2 :** In the new window, click **General**, and select the **Output window** tab


</div>


<div class="mw-translate-fuzzy">

<img alt="General" src=images/Macro_Install_HowTo_36.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

**3 :** check both boxes:


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Redirect internal Python output to Report view


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Case_a_cocher_O.png  style="width:16px;"> Redirect internal Python errors to Report view


</div>


<div class="mw-translate-fuzzy">

and click the **OK** button


</div>


<div class="mw-translate-fuzzy">

<img alt="Redirect internal" src=images/Macro_Install_HowTo_37.png  style="width:640px;">


</div>


<div class="mw-translate-fuzzy">

<img alt="the setup is complete" src=images/Macro_Install_HowTo_38.png  style="width:640px;">


</div>


</div>


</div>


{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > How to install macros/ro
