---
- TutorialInfo   *   Topic   *FEM
   Level   *Advanced
   Time   *60 min
   Author   *[JohnWang](User_JohnWang.md)
   FCVersion   *0.19
   Files   *
---

# Add Button to FEM Toolbar Tutorial/en





## Introduction

The FEM workbench has toolbars and menus. This tutorial shows how to add a test button to a toolbar. It also shows how to add a menuitem to a menu.

The task can be split into four parts   *

-   **Create a new icon file**.
-   **Register the new icon file**. Modification needed to `src/Mod/Fem/Gui/Resources/Fem.qrc`
-   **Create a new command class**. Modification needed to `src/Mod/Fem/femcommands/commands.py`
-   **Add new command to workbench**. Modification needed to `src/Mod/Fem/Gui/Workbench.cpp`

## Create a new icon file 

For the button we need an icon file. You can use any of your favorite tools to create it, but it must be in the SVG format. Here we will use the **FEM_testButton.svg** file as an example.

It must be placed in   * `src/Mod/Fem/Gui/Resources/icons/`.

## Register the new icon file 

The new SVG icon file has to be registered for the GUI-button by inserting it in `src/Mod/Fem/Gui/Resources/Fem.qrc`   *


{{code|code=
     <file>icons/FEM_testButton.svg</file>
}}

## Create a new command class 

A new command class has to be added to the `src/Mod/Fem/femcommands/commands.py` module.

Just copy/paste an existing command, then adjust the icon, menu text and tool-tip in `__init__(self)`   *


{{code|code=
class _testButton(CommandManager)   *
    "The FEM_testButton command definition"

    def __init__(self)   *
        super(_testButton, self).__init__()
        self.menuetext = "test Button"
        self.tooltip = "This is a test button"
        self.is_active = "always"
        #self.do_activated = "add_obj_on_gui_selobj_noset_edit"
}}

Don\'t forget to register the command at the bottom of the module file with the `addCommand(...)` method   *


{{code|code=
FreeCADGui.addCommand(
    "FEM_testButton",
    _testButton()
)
}}

**Note**   * Please see this [discussion thread](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=46693&start=10#p402004) in the forum if icons are involved.

## Add new command to workbench 

We will add the new command to both the **solve** toolbar and the **solve** menu.

Search for the following code snippet in `/Gui/Workbench.cpp` and add the new command   *


{{code|code= 
     Gui   *   *ToolBarItem* solve = new Gui   *   *ToolBarItem(root);
     solve->setCommand("Solve");
     *solve << "FEM_SolverCalculixCxxtools"
            << "FEM_SolverCalculiX"
            << "FEM_SolverElmer"
+           << "FEM_testButton"
            << "Separator"
}}

To add the command to the **solve** menu of the FEM workbench, search for the following code snippet in `Workbench.cpp`   *


{{code|code= 
    Gui   *   *MenuItem* solve = new Gui   *   *MenuItem;
    root->insertItem(item, solve);
    solve->setCommand("&Solve");
    *solve << "FEM_SolverCalculixCxxtools"
           << "FEM_SolverCalculiX"
           << "FEM_SolverElmer"
           << "FEM_SolverZ88"
+          << "FEM_testButton"
           << "Separator"
}}

**Result**   * You should have just successfully added a test button to a FEM workbench toolbar and menu. Now, you can [compile FreeCAD](Compiling.md) and test your new button.

## Related

-   [Extend FEM Module](Extend_FEM_Module.md)
-   [Onboarding FEM Devs](Onboarding_FEM_Devs.md)

[Category   *FEM](Category_FEM.md) [Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Button to FEM Toolbar Tutorial/en
