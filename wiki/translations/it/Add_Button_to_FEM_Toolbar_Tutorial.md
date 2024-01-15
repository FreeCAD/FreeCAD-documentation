---
 TutorialInfo:t
   Topic: FEM
   Level: Advanced
   Time: 60 min
   Author: User:JohnWang
   FCVersion: 0.19
   Files: 
---

# Add Button to FEM Toolbar Tutorial/it







## Introduzione

L\'ambiente FEM dispone di barre degli strumenti e di menu. Questo tutorial mostra come aggiungere un pulsante di prova a una barra degli strumenti. Mostra anche come aggiungere una voce di menu a un menu.

Il compito può essere suddiviso in quattro parti:

-   **Creare un nuovo file di icone**.
-   **Registrare il nuovo file di icone**. È necessaria la modifica di `src/Mod/Fem/Gui/Resources/Fem.qrc`
-   **Creare una nuova classe di comandi**. È necessaria la modifica di `src/Mod/Fem/femcommands/commands.py`
-   **Aggiungere un nuovo comando all\'ambiente**. È necessaria la modifica di `src/Mod/Fem/Gui/Workbench.cpp`



## Creare un nuovo file per l\'icona 

Per il pulsante abbiamo bisogno di un file icona. Si può utilizzare uno qualsiasi dei propri strumenti preferiti per crearlo, ma deve essere nel formato SVG. Qui utilizzeremo il file **FEM_testButton.svg** come esempio.

Deve essere inserito in: `src/Mod/Fem/Gui/Resources/icons/`.



## Registrare il nuovo file dell\'icona 

Il nuovo file icona SVG deve essere registrato per il pulsante della GUI inserendolo in `src/Mod/Fem/Gui/Resources/Fem.qrc`:


{{code|code=
     <file>icons/FEM_testButton.svg</file>
}}



## Creare una nuova classe del comando 

Deve essere aggiunta una nuova classe per il comando nel modulo `src/Mod/Fem/femcommands/commands.py`.

Basta copiare/incollare un comando esistente, quindi modificare l\'icona, il testo del menu e il suggerimento in `__init__(self)`:


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

Non si dimentichi di registrare il comando in fondo al file del modulo con il metodo `addCommand(...)`:


{{code|code=
FreeCADGui.addCommand(
    "FEM_testButton",
    _testButton()
)
}}

**Nota**: vedere questo [thread di discussione](https://forum.freecadweb.org/viewtopic.php?f=18&t=46693&start=10#p402004) nel forum se sono coinvolte le icone.



## Aggiungere il nuovo comando all\'ambiente 

Aggiungeremo il nuovo comando sia alla barra degli strumenti **Risolvi** che al menu **Risolvi**.

Cercare il seguente snippet di codice in `/Gui/Workbench.cpp` e aggiungere il nuovo comando:


{{code|code= 
     Gui::ToolBarItem* solve = new Gui::ToolBarItem(root);
     solve->setCommand("Solve");
     *solve << "FEM_SolverCalculixCxxtools"
            << "FEM_SolverCalculiX"
            << "FEM_SolverElmer"
+           << "FEM_testButton"
            << "Separator"
}}

Per aggiungere il comando al menu **Risolvi** di FEM, cercare il seguente snippet di codice in `Workbench.cpp`:


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

**Risultato**: si dovrebbe aver appena aggiunto con successo un pulsante di test alla barra degli strumenti e al menu di FEM. Ora si può [compilare FreeCAD](Compiling.md) e testare il tuo nuovo pulsante.



## Correlati

-   [Estendere il modulo FEM](Extend_FEM_Module/it.md)
-   [Onboarding degli sviluppatori FEM](Onboarding_FEM_Devs/it.md)



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add Button to FEM Toolbar Tutorial/it
