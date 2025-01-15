---
 TutorialInfo:e
   Topic: FEM
   Level: Fortgeschritten
   Time: 60 min
   Author: User:JohnWang
   FCVersion: 0.19
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

Die neue SVG-Symboldatei muss für den GUI-Button registriert werden, indem sie in `src/Mod/Fem/Gui/Resources/Fem.qrc` eingefügt wird:


{{code|code=
     <file>icons/FEM_testButton.svg</file>
}}



## Eine neue Befehlsklasse erstellen 

Eine neue Befehlsklasse muss zum Modul `src/Mod/Fem/femcommands/commands.py` hinzugefügt werden.

Kopieren Sie einfach einen bestehenden Befehl und passen Sie das Symbol, den Menütext und den Tooltip in `__init__(self)` an:


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

Vergiss nicht, den Befehl am Ende der Moduldatei mit der Methode `addCommand(...)` zu registrieren:


{{code|code=
FreeCADGui.addCommand(
    "FEM_testButton",
    _testButton()
)
}}

**Hinweis**: Bitte schaue diese [Diskussion](https://forum.freecadweb.org/viewtopic.php?f=18&t=46693&start=10#p402004) im Forum an, wenn es um Icons geht.



## Einem Arbeitsbereich einen neuen Befehl hinzufügen 

Wir fügen den neuen Befehl sowohl der Symbolleiste **Lösen** als auch dem Menü **Lösen** hinzu.

Suche den folgenden Codeschnipsel in `/Gui/Workbench.cpp` und füge den neuen Befehl hinzu:


{{code|code= 
     Gui::ToolBarItem* solve = new Gui::ToolBarItem(root);
     solve->setCommand("Solve");
     *solve << "FEM_SolverCalculixCxxtools"
            << "FEM_SolverCalculiX"
            << "FEM_SolverElmer"
+           << "FEM_testButton"
            << "Separator"
}}

Um den Befehl zum **Löser** Menü der FEM-Workbench hinzuzufügen, suche nach dem folgenden Codeschnipsel in `Workbench.cpp`:


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

**Ergebnis**: Sie sollten soeben erfolgreich eine Test-Schaltfläche zur Symbolleiste und zum Menü einer FEM-Arbeitsbereich hinzugefügt haben. Jetzt kann FreeCAD kompiliert und Ihre neue Schaltfläche getesten werden.



## Verwandtes

-   [FEM Modul Erweitern](Extend_FEM_Module/de.md)
-   [Einführung für FEM-Entwickler](Onboarding_FEM_Devs/de.md)



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Add Button to FEM Toolbar Tutorial/de
