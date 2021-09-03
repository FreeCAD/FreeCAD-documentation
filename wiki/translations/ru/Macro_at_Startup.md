

## Введение


{{TOCright}}

This documentation will explain how to set up a macro to automatically run at FreeCAD startup.

Before starting, following things shall be considered:

-   Automatically running macro at startup can be considered a security risk. You should only run macro that you trust and that you previously tested
-   You probably need some Python and coding notions to follow this procedure
-   When user folders (\'Mod\', \'Macro\', \...) are referred to, they are located in your user FreeCAD folder. You can locate them at Start up and Configuration → [User related information](Start_up_and_Configuration#User_related_information.md)
-   This shouldn\'t be done for macros dealing with part modeling. This is rather appropriate for macros that add features, improve the UI, \...

## С чего начать 

### Prepare the macro 

Generally, it will happen that a macro isn\'t directly compatible with a startup launch and shall be fine-tuned

Consider the below macro that you downloaded from somewhere and is stored in your \'Macro\' folder with name \'MySuperMacro.FCMacro\':

    ## Import section ##
    from PySide import QtGui

    ## Definition section (classes, functions, ...)
    class MyMsgBox(QtGui.QMessageBox):

        def __init__(self):
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Main instruction section
    MyMsgBox()

All macros will generally present a similar structure with first import section, then definition section and finally main instruction section. We will focus on this latter because main instructions (they are quite easy to spot because they start at the full beginning of the line) are actually the ones that \'execute\' the macro. For later step, we\'ll need to programmatically import the macro then execute it. This can\'t be done with the actual structure of the macro. To be able to do so, we need to enclose the main instructions in a function \--eg. run()\-- then ensure this function is still called when the macro is manually run by the user. If you\'re not totally sure of what you\'re doing, it is advised to work on a copy of the macro (or you may just want to keep the original macro as is). The original file shall be modified as follows:

    from PySide import QtGui
    ## The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
    import FreeCAD as App
    import FreeCADGui as Gui

    class MyMsgBox(QtGui.QMessageBox):

        def __init__(self):
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Enclose the main instructions in a function
    def run():
        MyMsgBox()

    ## Ensure main instructions are still called in case of manual run
    if __name__ == '__main__':
        run()

Of course if the function \'run()\' already exists in the macro, you can choose any other convenient name Now the macro is ready to be integrated in FreeCAD startup.

### Integrate into FreeCAD startup 

First create a new folder in your user \'Mod\' folder, let\'s say called \'MacroStartup\'. Copy the modified macro into this newly created folder and rename it with a \'.py\' extension if this isn\'t yet the case (notice that if you develop the macro by yourself, it can be named with \'.py\' extension also in the \'Macro\' folder so that you don\'t need to rename when copying). Finally create in the same folder a file called \'InitGui.py\' which contains the following code:

    def runStartupMacros(name):
        # Do not run when NoneWorkbench is activated because UI isn't yet completely there
        if name != "NoneWorkbench":
            # Run macro only once by disconnecting the signal at first call
            FreeCADGui.getMainWindow().workbenchActivated.disconnect(runStartupMacros)

            # Following 2 lines shall be duplicated for each macro to run
            import MySuperMacro
            MySuperMacro.run()

            # Eg. if a second macro shall be launched at startup
            # import MyWonderfulMacro
            # MyWonderfulMacro.run()

    # The following 2 lines are important because InitGui.py files are passed to the exec() function...
    # ...and the runMacro wouldn't be visible outside. So explicitly add it to __main__
    import __main__
    __main__.runStartupMacros = runStartupMacros

    # Connect the function that runs the macro to the appropriate signal
    FreeCADGui.getMainWindow().workbenchActivated.connect(runStartupMacros)

Notice that it shall be done only once. If you want to run more than one macro, you can just add the others in the same file (look at the comments on the above code).

We are done. Your macro should automatically run at next FreeCAD launch.

Notice that if the original macro was downloaded through the Addon Manager, it will be overwritten on update and thus you have to follow again the steps here.

## General Notes 

-   In the example \'InitGui.py\' script above, the function named \'runStartupMacros()\' may be changed, so long as you also change the other four references to it, so they all match.
-   This script will be run prior to the auto loading of your desired startup workbench in the FreeCAD Preferences, [Preferences\_Editor\#General\_settings](Preferences_Editor#General_settings.md).

### Linux

### MacOS

### Windows

-   In the above example, you may place the \'MacroStartup\' folder within the \'Mod\' folder of your FreeCAD root directory (whether installed version or portable version), or you may create a \'Mod\' folder along side the \'Macro\' folder in \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\\', and place the \'MacroStartup\' folder there.
-   From observation, the workbenches found within either \'Mod\' folder are loaded alphabetically. Those in the FreeCAD root \'Mod\' folder are loaded first, then FreeCAD scans the \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\Mod\' folder for additional workbenches.

## Related

-   [Extra\_python\_modules\#LazyLoader](Extra_python_modules#LazyLoader.md) LazyLoader is a python module that allows deferred loading.


{{Powerdocnavi

}}

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md) [Category:Macros{{\#translation:}}](Category:Macros.md)
