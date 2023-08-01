---
- TutorialInfo:/de
   Topic:FEM
   Level:Fortgeschritten
   Time:60 min
   Author:[JohnWang](User_JohnWang.md)
   FCVersion:0.19
---

# Add Button to FEM Toolbar Tutorial/de







## Einleitung

Der Arbeitsbereich FEM enthält Symbolleisten und Menüs. Diese Anleitung zeigt, wie eine Test-Schaltfläche zu einer Symbolleiste hinzugefügt wird. Sie zeigt auch, wie einem Menü ein Menüeintrag hinzugefügt wird.

Die Aufgabe lässt sich in vier Teile aufteilen:

-   **Eine neue Symboldatei erstellen**.
-   **Die neue Symboldatei registrieren**. `src/Mod/Fem/Gui/Resources/Fem.qrc` muss geändert werden.
-   **Eine neue Befehlsklasse erstellen**. `src/Mod/Fem/femcommands/commands.py` muss geändert werden
-   **Einem Arbeitsbereich einen neuen Befehl hinzufügen**. `src/Mod/Fem/Gui/Workbench.cpp` muss geändert werden.



## Eine neue Symboldatei erstellen 

Für die Schaltfläche brauchen wir eine Symboldatei. Sie kann mit jedem deiner Lieblingswerkzeuge erstellt werden, muss aber im SVG-Format gespeichert werden. Wir verwenden als Beispiel **FEM_testButton.svg**

Sie muss hier abgelegt werden: `src/Mod/Fem/Gui/Resources/icons/`.



## Die neue Symboldatei registrieren 

The new SVG icon file has to be registered for the GUI-button by inserting it in `src/Mod/Fem/Gui/Resources/Fem.qrc`:


{{code|code=
     <file>icons/FEM_testButton.svg</file>
}}



## Eine neue Befehlsklasse erstellen 

A new command class has to be added to the `src/Mod/Fem/femcommands/commands.py` module.

Just copy/paste an existing command, then adjust the icon, menu text and tool-tip in `__init__(self)`:


{{code|code=
class _testButton(CommandManager):
    "The FEM_testButton command definition"

    def __init__(self):
        super(_testButton, self).__init__()
        self.menuetext = "test Button"
        self.tooltip = "This is a test button"
        self.is_active = "always"
        #self.do_activated = "add_obj_on_gui_selobj_noset_edit"
}}

Don\'t forget to register the command at the bottom of the module file with the `addCommand(...)` method:


{{code|code=
FreeCADGui.addCommand(
    "FEM_testButton",
    _testButton()
)
}}

**Note**: Please see this [discussion thread](https://forum.freecadweb.org/viewtopic.php?f=18&t=46693&start=10#p402004) in the forum if icons are involved.



## Einem Arbeitsbereich einen neuen Befehl hinzufügen 

We will add the new command to both the **solve** toolbar and the **solve** menu.

Search for the following code snippet in `/Gui/Workbench.cpp` and add the new command:


{{code|code= 
     Gui::ToolBarItem* solve = new Gui::ToolBarItem(root);
     solve->setCommand("Solve");
     *solve << "FEM_SolverCalculixCxxtools"
            << "FEM_SolverCalculiX"
            << "FEM_SolverElmer"
+           << "FEM_testButton"
            << "Separator"
}}

To add the command to the **solve** menu of the FEM workbench, search for the following code snippet in `Workbench.cpp`:


{{code|code= 
    Gui::MenuItem* solve = new Gui::MenuItem;
    root->insertItem(item, solve);
    solve->setCommand("&Solve");
    *solve << "FEM_SolverCalculixCxxtools"
           << "FEM_SolverCalculiX"
           << "FEM_SolverElmer"
           << "FEM_SolverZ88"
+          << "FEM_testButton"
           << "Separator"
}}

**Result**: You should have just successfully added a test button to a FEM workbench toolbar and menu. Now, you can [compile FreeCAD](Compiling.md) and test your new button.

## Related

-   [Extend FEM Module](Extend_FEM_Module.md)
-   [Onboarding FEM Devs](Onboarding_FEM_Devs.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Button to FEM Toolbar Tutorial/de
