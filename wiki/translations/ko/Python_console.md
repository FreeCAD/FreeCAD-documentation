# Python console/ko

 {{VeryImportantMessage|(January 2020) FreeCAD was originally designed to work with Python 2. Since Python 2 reached end of life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.}}

## Introduction

The [Python console](Python_console.md) is a panel that runs an instance of the [Python](Python.md) interpreter which can be used to control FreeCAD processes, and create and modify objects and their properties.

The Python console in FreeCAD has basic syntax highlighting, able to differentiate with various styles and colors, comments, strings, numeric values, built in functions, printed text output, and delimiters like parentheses and commas. These properties of the console can be configured in the [Preferences editor](Preferences_Editor.md).

<img alt="" src=images/FreeCAD_Python_console.png  style="width:800px;">


*The Python console showing messages when FreeCAD has just started.*

## Scripting


**For absolute beginners, see:**

[Introduction to Python](Introduction_to_Python.md), and [Python scripting tutorial](Python_scripting_tutorial.md).


**See also:**

[FreeCAD scripting basics](FreeCAD_Scripting_Basics.md), and [Scripted objects](Scripted_objects.md).

The Python console can perform basic code completion when a dot is written after an object; it will show public methods and attributes (variables) of the current object (class), for example, `obj.`

The console is also able to show the documentation string of a particular function when the opening parenthesis is written, for example, `function(`

<img alt="" src=images/FreeCAD_Python_console_example.png  style="width:800px;">


*Example Python code that produces objects in the 3D view.*

The FreeCAD initialization scripts automatically load some modules, and define some aliases. Therefore, in the Python console these are available 
```python
App = FreeCAD
Gui = FreeCADGui
```

Therefore these are equal


```python
App.newDocument()
FreeCAD.newDocument()
```


**Note:**

these pre-loaded modules and aliases are only available from the Python console embedded inside the FreeCAD program. If you use FreeCAD as a library in an external program, you must remember to load the `FreeCAD` and `FreeCADGui` modules and define the necessary aliases if you wish.

## Actions

Right click on the Python console shows some commands:

-    **Copy**: stores the selected text in the clipboard for later pasting; it is disabled if nothing is selected.

-    **Copy command**: stores the selected command in the clipboard for later pasting; it is disabled if nothing is selected.

-    **Copy history**: copy the entire history of Python commands entered in this session.

-    **Save history as**: save the entire history of Python commands entered in this session to a text file.

-    **Paste**: paste previously copied text in the clipboard to the Python console.

-    **Select all**: selects all text in the Python console.

-    **Clear console**: erases all commands entered into the Python console. This is useful if the Python console is full of messages and previously entered commands that may be distracting when testing a new function. This is merely aesthetic, as this command doesn\'t delete existing variables nor clears the imported modules in the session.

-    **Insert file name**: opens a dialog to search for a file in the system, then it inserts the full path of the file. This is useful to test functions that process an input file, without having to write the entire name in the console, which is error prone. This command does not run the file, and does not import it as a Python module, it just returns the full path of that file.

-    **Word wrap**: wrap very long lines that exceed the horizontal dimension of the Python console.

## Notes

-   One has the ability to scroll the API in the Python console. Example:
    1.  In the console type: `FreeCAD.`
    2.  A dialog box will display with optional classes/functions to choose from
    3.  Scroll through the list to read the description of each class/function
    4.  By choosing a function and following it with a `.` one can repeat steps 2 and 3 to traverse deeper in to the API
-   Tab/Word completion is supported using the **Ctrl**+**Space** shortcut


{{Interface navi

}} {{Std Base navi}} 
