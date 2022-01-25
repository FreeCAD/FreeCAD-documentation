# Command/pt-br
## Introdução


{{TOCright}}

A [command](Command.md) is what is being executed when you press a toolbar button or type a keyboard shortcut. It can be a very simple action, like changing the zoom level of the [3D view](3D_view.md) or rotating the point of view, or a complex system that will open dialog boxes and wait for the user to perform specific tasks.

Each FreeCAD command has a unique name, that appears in the [:Category:Command Reference](:Category_Command_Reference.md) page. Commands can be launched by a toolbar button, a menu item, or from a [python](Python.md) script or the [Python console](Python_console.md), by running:


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Background

FreeCAD commands are defined per workbench. Workbenches will normally add their command definitions at FreeCAD init time, so the command exists and is available as soon as FreeCAD is started, no matter if the corresponding workbench has been activated yet or not. In some cases however, the workbench author might have decided to not overload/burden the FreeCAD startup process and therefore loaded the command definitions only at workbench init. In those cases, the command will only be available after the workbench has been activated (you have switched to it at least once with the workbench selector).

As most of them require user interaction, FreeCAD commands are only available in GUI-mode, and not in console mode. However, for convenience, most FreeCAD commands will either have a corresponding python function (like `Part.makeBox` or `Draft.makeLine`), or will execute code that is very easy to replicate in a python script and/or [macro](macros.md).

Commands can be defined either in C++ or in Python.

## Commands defined in C++ 

Example of a C++ command definition, usually defined following the structure {{FileName|Mod/ModuleName/Gui/Command.cpp}}.


{{Code|lang=cpp|code=
DEF_STD_CMD_A(StdCmdMyCommand);

StdCmdMyCommand::StdCmdMyCommand()
  : Command("Std_My_Command")
{
    sGroup        = QT_TR_NOOP("File");
    sMenuText     = QT_TR_NOOP("My Command");
    sToolTipText  = QT_TR_NOOP("Runs my command in the active document");
    sWhatsThis    = "Std_MyCommand";
    sStatusTip    = QT_TR_NOOP("Runs my command in the active document");
    sPixmap       = "MyCommand.svg";
    sAccel        = "Ctrl+A";
}

void StdCmdExport::activated(int iMsg)
{
    // place here the code to be executed when the command is ran
}

bool StdCmdMyCommand::isActive(void)
{
    // here you have a chance to return true or false depending if your command must be shown as active or inactive (greyed).
}

// the command must be "registered" in FreeCAD's command system
CommandManager &rcCmdMgr = Application::Instance->commandManager();
rcCmdMgr.addCommand(new StdCmdMyCommand());
}}

## Commands defined in Python 

Example of a Python command definition, it can be placed in a directory like {{FileName|Mod/ModuleName/tools/commands.py}}. 
```python
from PySide.QtCore import QT_TRANSLATE_NOOP


class MyCommand:
    """Explanation of the command."""

    def __init__(self):
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self):
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap': 'MyCommand.svg',
                'Accel': "Ctrl+A",
                'MenuText': QT_TRANSLATE_NOOP("My_Command", "My Command"),
                'ToolTip': QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

    def Activated(self):
        """Run the following code when the command is activated (button press)."""
        print("Activated")

    def isActive(self):
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

# The command must be "registered" with a unique name by calling its class.
FreeCADGui.addCommand('My_Command', MyCommand())
```

## Examples

See [Line drawing function](Line_drawing_function.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Command_Reference|:Category:Command Reference]] page. Commands can be launched by a toolbar button, a menu item, or from a ](Category_Command_Reference|:Category:Command Reference]] page. Commands can be launched by a toolbar button, a menu item, or from a .md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Command/pt-br
