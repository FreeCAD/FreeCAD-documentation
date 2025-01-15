# Python Development Environment/ru
## Упрощённая среда разработки для Python в FreeCAD 

[Python](wikipedia:Python_(programming_language).md) is a programming environment which has been incorporated into the [FreeCAD](https://www.freecadweb.org/) system. Using Python many operations offered by FreeCAD are available for programmatic access. Python programs for FreeCAD are usually developed to be either run on the Python console or through the Macro facility of FreeCAD (see [How to install macros](How_to_install_macros.md)).

There are numerous tools available for program development in Python. The complicating factors for developing Python to use with FreeCAD are twofold: first the tools do not have any support for the numerous data structures and access points of FreeCAD; secondly they do not work \"within FreeCAD\". This means that you can use them to develop code outside of FreeCAD and not be able to test in the target environment; or you can develop Python in the target environment (i.e. the FreeCAD environment) but not have any support from the development tools. Neither of these is an acceptable solution.

## Background

Modern software development at the commercial standard is usually done using a set of tools generically referred to as [\'IDE\'](wikipedia_Integrated_development_environment.md). Typically these tools include the following 3:

-   source code editor
-   build automation tools
-   debugger

which are standard while the following are present in some IDEs but not in others:

-   intelligent code completion
-   integrated compiler, interpreter, or both
-   version control system
-   Graphical User Interface (GUI) construction
-   class browser
-   object browser
-   class hierarchy diagram

A summary of the status of these tools within FreeCAD is (\'N/A\' meaning \'Not Available\'):


<table style="width: 100%" border="1">


<tr>


<td>

source code editor


</td>


<td>

a variety of editors are available for the platforms supported by FreeCAD, discussed below


</td>


</tr>


<tr>


<td>

build automation tools


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

debugger


</td>


<td>

planned but not available yet, there are some work-arounds discussed below


</td>


</tr>


<tr>


<td>

intelligent code completion


</td>


<td>

there is some available through the Python console but that is all


</td>


</tr>


<tr>


<td>

integrated compiler, interpreter, or both


</td>


<td>

the Python compiler is integrated with the Python console but not with the editors


</td>


</tr>


<tr>


<td>

version control system


</td>


<td>

N/A - there is only one version of the file


</td>


</tr>


<tr>


<td>

Graphical User Interface (GUI) construction


</td>


<td>

what is available is basic and based on copy/paste of code (see [PySide](PySide.md))


</td>


</tr>


<tr>


<td>

class browser


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

object browser


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

class hierarchy diagram


</td>


<td>

N/A


</td>


</tr>


</table>

Many tools exist to support the above function for Python programming but unfortunately they do not integrate with the FreeCAD development environment.

A list of IDEs for Python is located at [Integrated Development Environments for Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments).

## Editors

There is an editor for Python as part of FreeCAD, it is started by clicking the Edit button on the Macro -\> [Macros\...](Std_DlgMacroExecute.md). If you want to use a 3rd party editor which takes advantage of your platform then there are various Python editors available, for numerous platforms and with a variety of level of functionality. One advantage of using an external editor is that the display area of FreeCAD can be used for output (both graphic and textual to the console) while the source code is displayed in a different application. A list of editors for Python for a variety of platforms is available at [Python Editors](https://wiki.python.org/moin/PythonEditors)

Note: For the Macintosh the text editor [TextWrangler](http://www.barebones.com/products/textwrangler/) works well. It has code highlighting and excellent search facilities. There are options to execute jobs in Python but of course they do not work with the FreeCAD environment.

### Macro Source Code Directories 

There are two directories used by FreeCAD, by default they are the same directory but they are pointed to by different callable point in FreeCAD:

-   FreeCAD.ConfigGet(\"UserAppData\")
-   FreeCAD.ParamGet(\'User parameter:BaseApp/Preferences/Macro\').GetString(\'MacroPath\')

The first one \"UserAppData\" points to a directory where things like configuration files or other files intended for the user but not to be edited by the user may be stored.

The second one \"MacroPath\" points to a directory where the Python files which are macro files for FreeCAD are stored. To mark a Python file as a macro file for FreeCAD, the file extension is changed from \".py\" to \".FCMacro\".

By default these two directories are the same location but this is not necessary. It might be convenient to alter the location for the macro files (\*.FCMacro) to a different location.

Editing files located in the \"MacroPath\" is straight forward, the text editor will accommodate this. For ease of use of FreeCAD Macro files, it is advisable to keep all the macro files in the directory pointed to by \"MacroPath\".

To alter the \"MacroPath\" directory, use Tools-\>Edit Parameters and then select Preferences/Macro/MacroPath where the text may be double-clicked and edited. Alternatively \"MacroPath\" can be altered by the code:


```python
FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')
```

## Debugger


**'''A debugger is planned for FreeCAD and these steps are a work-around until it is available. See github.com/mumme74/FreeCAD/tree/editor_fixes'''**

[Debuggers](https://en.wikipedia.org/wiki/Debugger) typically provide two main features (among others):

-   breakpoints in the source code
-   variable inspection

**Breakpoints** are \'traps\' that are placed in the code, if the execution path through the code encounters one of these breakpoints, then execution is halted or suspended. Note that execution is not stopped as when a program is stopped all memory resident information such as variables is lost. While the program is suspended the contents of variables can be inspected and sometimes altered (which depends on the ability of the debugger). Generally the source code can not be changed although some environments do support this. When ready, the execution of the source code can be resumed. Numerous breakpoints can be placed in the code and numerous suspensions through the breakpoints may occur. The purpose of the debugger is to make sure that the execution with the breakpoints and suspensions is functionally identical to execution without breakpoints.

**Variable Inspections** are available during the suspension of execution caused by a breakpoint. Generally the contents of variables can be viewed, many debuggers also support the editing of the contents before execution resumes.

Although a fully functioned debugger is planned for FreeCAD it is not available as of yet. This section will detail some work-arounds for the interim until the debugger is released.

### Breakpoints

Implementing breakpoints involves a supervisory level of code which administers the execution of the code under development. Such a level of code for Python development within FreeCAD is not presently available. As a weak substitute, the following code is an option. Instead of suspending the execution the code will halt execution completely by dividing a number by zero. This really is a very weak option compared to a proper debugger breakpoint, also this option is only of use when used alongside the routine shown in the next section \'Variable Inspection\'.

**Breakpoint Code** 
```python
def breakpoint(*args):
    # this routine will print an optional parameter on the console and then stop execution by diving by zero
    # e.g. breakpoint()
    # e.g. breakpoint("summation module")
    #
    if len(args)>0:
        FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
    hereWeStop = 12/0
    
```

**Console Traceback**

When a program fails during execution, Python generates what is known as a traceback which lists the order of program execution (i.e. which program called which program in which order).

For the code sample


```python
breakpoint('amalgamation routine')
```

we get the following traceback:


```python
Breakpoint: amalgamation routine
Traceback (most recent call last):
  File "/Users/wylbur/Library/Preferences/FreeCAD/testStub.FCMacro", line 40, in <module>
    breakpoint()
  File "/Users/wylbur/Library/Preferences/FreeCAD/myNewMacro.FCMacro", line 28, in breakpoint
    hereWeStop = 12/0
ZeroDivisionError: integer division or modulo by zero
```

Reading the traceback we can determine that:

-   a message of \'Breakpoint: amalgamation routine\' was sent by the breakpoint which has the string \'amalgamation routine\'
-   the execution error occurred at line 28 of module \'myNewMacro\'
-   routine \'myNewMacro\' was called from line 40 in the module \'testStub\'

Assuming the string passed to the breakpoint call is meaningful then the location of the breakpoint can easily be determined. Note that is a complex system the traceback may have tens or even hundreds of entries in it.

To become productive with these breakpoints, continue on to the next section.

### Variable Inspection 

The second main feature of a debugger is to examine and possibly alter the contents of variables. Once again, until the FreeCAD debugger for Python is ready we have to depend on work-arounds.

A feature of the FreeCAD system is the provision of global variables. These variables that are created by the Python code and exist in FreeCAD\'s memory until the user quits from FreeCAD. The form of these variables is:


```python
FreeCAD.myVariable = 123
```

The statement creates a Python variable in the FreeCAD memory which is fully accessible to Python code, in fact it behaves identically to a normal Python variable. Yet after the Python code finishes running, no matter if it is running as a macro or through the console, there will be a variable \'FreeCAD.myVariable\' remaining in memory with the value of 123. Entering:


```python
>>> FreeCAD.myVariable
123
```

will produce the contents of the variable on the console. This value will remain in FreeCAD until either it is changed or the user Quits from FreeCAD. This means the value is present and available for a subsequent Python program to read from. At any time it can be checked from the console by typing it\'s name. So a program called \'Program A\':


```python
# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable
```

can run and load values into the global variable. Later a second program called \'Program B\' can run and retrieve the value:


```python
myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable
```

Presumably \'Program B\' then goes on to make calculations involving the values left in FreeCAD.myVariable. At any time the user can type on the console to inspect the variable contents:


```python
>>> FreeCAD.myVariable
[123, 'abc']
>>> 
```

An important fact to be aware of with FreeCAD global variables is that they exist in memory and are lost when the program is Quit from. They are not saved with documents but only exist in memory.

### Usage

This brings us to a point where we can put the two steps together and use them to trace down errors in code. This is a bit cumbersome to use but is only the option until the FreeCAD debugger is ready.

It\'s probably easiest to present through an example, say the following program is being debugged:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Execution of the program on the console yields:


```python
>>> monthCounter()
10
```

which is not what we expected! Assuming we are unable to see the errors we can use our unsophisticated breakpoint and variable examiner as follows. We can insert a line to copy the value of the variable we are wondering about to a global variable, then we can place a breakpoint to halt execution there:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
    breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Now when we run the program we get:


```python
>>> monthCounter()
Breakpoint: is this assignment faulty?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 9, in monthCounter
  File "<input>", line 5, in breakpoint
ZeroDivisionError: integer division or modulo by zero
>>> 
```

Probably things don\'t look so good, but what we can now do is inspect the value of the Python variable \'temporaryVariable1\' as we assigned it\'s value to the global variable \'FreeCAD.saveMyVariable\':


```python
>>> FreeCAD.saveMyVariable
15
>>>
```

Remembering that the variable \'FreeCAD.saveMyVariable\' holds the value of the Python variable \'temporaryVariable1\' we can now determine the error in the value and start tracing back to determine where the error came from. When we are looking at \'FreeCAD.saveMyVariable\' it is important to realise that the variable \'temporaryVariable1\' is no longer available - it has been garbage collected away by the Python system.

Once the error has been located in the statement


```python
numberOfSeasons = 3
```

and corrected to:


```python
numberOfSeasons = 4
```

Then we can run the program again, and get the value of \'11\' which is still not right. We can make more assignments to FreeCAD global variables, have multiple breakpoints (although the first one encountered will stop execution)


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 4
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable1 = temporaryVariable1
    #breakpoint('first assignment')
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    FreeCAD.saveMyVariable2 = numberOfMonths
    breakpoint('second assignment')
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

We now have two breakpoints (although one is commented out) and two FreeCAD global variables in use. There is no practical limit to the global variables available from FreeCAD so there is no need to economise unnecessarily. We can now produce the following on the console:


```python
>>> FreeCAD.saveMyVariable1
10
>>> FreeCAD.saveMyVariable2
11
>>> 
```

Some points about the use of the FreeCAD global variables:

-   Python treats these variables identically to any other Python variable
-   these variables may hold any Python data type - anything a regular Python variable would hold
-   these variables may be used to \'bring out\' the contents of a Python variable so we can see them
-   also these variables may be used to \'supply\' values to a Python variable by setting their value from the console prior to running a routine, or setting it in a previous Python program
-   these variables may be used to pass data between two programs that run at different points in time
-   (to repeat) these variables are only for the duration of the FreeCAD session, once the user Quits from FreeCAD then the variables are lost

### Variable Watcher 

There is a utility [Global Variable Watcher](Macro_Global_Variable_Watcher.md) to help monitor the global variables of FreeCAD. It can display the contents of a global variable either on request or on a timed basis.

### Name Space Clash 

One thing to be aware of is as there is no management of global variable names by FreeCAD so there is the possibility of changing a variable from the system or another piece of code. Consequently it is a good idea to prefix your variables with something unique such as the routine name. For example to use a variablefrom a routine called \'alpha1\' the global name could be \'FreeCAD.alpha1MyVariable\'.

## Coding Framework 

When developing small pieces of Python code in FreeCAD it may be sufficient to use the Python console. However as the number of lines of code grows it makes more sense to store them in a file. Python can be in any file ending with the extension \".py\", however FreeCAD also provides a mechanism called Macro for storing such programs and interacting with them (e.g. editing, running). Python in regular \'.py\' files may only run from the Python console while python in macro file \'.FCMacro\' can be run from the FreeCAD interface for executing macros. One downside with the FreeCAD menu interface is it is menu based with a control window and potentially causes some clutter on the on-screen GUI.

An easier approach is to take the Python code and instead of starting it from the FreeCAD Macro menu, start it from a toolbar. A Python routine linked to a button on a toolbar may be executed by one click. Also as the toolbars are floating windows they do not clutter the on-screen display. In fact if the FreeCAD window is less then the physical size of the screen the toolbar may be left to float outside of the FreeCAD window. This is beneficial when screen snapshots are required of the FreeCAD display. Also the toolbar can be much smaller than the macro control window displayed by the Macro menu of FreeCAD.

Connecting a macro to a button on a toolbar is covered in [How to Install Macros](How_to_install_macros.md) and [How to Customise a Toolbar](Customize_Toolbars.md). It can take a number of minutes to connect a macro to button on toolbar, select an icon etc. This is not always required as sometimes you simply want to quickly flesh out a piece of code which will then be integrated in some other code. For this situation a Test Stub can be beneficial. There is no real definition for what a test stub would entail, it really depends on the person and the application area. An example is shown below:


```python
#
#           TEST
#           TEST stub to clip any code onto...
#           TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
```

This test stub also serves as a template for code with locations defined for the different aspects of a large Python program. When executed the test stub program simply generates a message showing it\'s name and finishes. In using a test stub, any main line code written is placed at the very end of the file with code for class definition, functions etc. placed in the previous sections. The template can easily be altered to match the situation. Obviously for a program of 5 lines there is no need for such an amount of documentation.

By keeping a button permanently on a toolbar and linking that button to the test stub, there is always an area to write code and execute it immediately. The execution will be independent of the Python console. Also the execution can be independent of the screen GUI. Output from the program under development will appear as it should on the screen without any other artifacts from the programming environment. The Python console can be hidden to increase display area or used for any other purpose if needed. When execution is handled by the button on the toolbar the console is not required.

When the code is finished then is can simply be copied/pasted over to another file and the test stub left empty until the next time it is needed.

Multiple pieces of code can be developed using the same test stub with some extra code for providing multiple buttons which is located at [PySide Beginner Examples - More Than 2 Buttons](PySide_Beginner_Examples#More_Than_2_Buttons.md).

**More PySide Support**

For more support using the PySide GUI there is the page [PySide](PySide.md)

**More Python Programming Support**

For more assistance with Python coding, there is a macro written to aid in developing Python code, it is located at [Python Assistant Window](Macro_Python_Assistant_Window.md).

## Putting It All Together 

Screen management can be a challenge when developing code that has complex and detailed graphical output like FreeCAD does. The following system works well:

-   FreeCAD for console, report, GUI display
-   toolbar to invoke code being developed
-   external editor to modify code
-   PAW (Python Assistant Window) to aid Python code generation

**Screen Management**

With the test stub operated from a toolbar, and an external editor used, the window layout on the screen will be something like:

![](images/PythonDevelopmentEnvironment.jpg )

\"tree\" in the diagram refers to the Combi or Tree browsers, the Python console and Report view are combined into the lower window and selectable by buttons. By selective use of the tools the development stream can be optimised, the above is only one idea. Tailoring is done on a personal basis.

## Miscellaneous Links 

Some other links about IDEs for Python which might be of interest are:

-   [Comparison of Python IDEs for Development](http://www.pythoncentral.io/comparison-of-python-ides-development/)
-   [Choosing the Best Python IDE](http://pedrokroger.net/choosing-best-python-ide/)
-   [Your Development Environment](http://docs.python-guide.org/en/latest/dev/env/)
-   [PyCharm Community Edition IDE](http://www.jetbrains.com/pycharm/)
-   [Using Pyzo Python IDE with FreeCAD](Pyzo.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Python Development Environment/ru
