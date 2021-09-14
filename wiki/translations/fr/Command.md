# Command/fr



## Introduction


{{TOCright}}

Une [commande](Command/fr.md) est ce qui est en cours d'exécution lorsque vous appuyez sur un bouton de la barre d'outils ou tapez un raccourci clavier. Cela peut être une action très simple, comme changer le niveau de zoom de la [vue 3D](3D_view/fr.md) ou faire pivoter le point de vue, ou un système complexe qui ouvrira des boîtes de dialogue et attendra que l\'utilisateur exécute des tâches spécifiques.

Chaque commande FreeCAD a un nom unique, qui apparaît dans la page [:Category:Command\_Reference](:Category:Command_Reference.md). Les commandes peuvent être lancées à l\'aide d\'un bouton de la barre d\'outils, d\'un élément de menu, d\'un script [Python](Python/fr.md) ou de la [console Python](Python_console/fr.md), en exécutant :


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Contexte

Les commandes FreeCAD sont définies par atelier. Les ateliers ajoutent normalement leurs définitions de commande au moment de l'initialisation de FreeCAD. La commande existe donc et est disponible dès le démarrage de FreeCAD, que l\'atelier correspondant ait été activé ou non. Dans certains cas, cependant, l\'auteur de l\'atelier pourrait avoir décidé de ne pas surcharger/alourdir le processus de démarrage de FreeCAD et de charger les définitions de commande uniquement à l\'initiation de l\'atelier. Dans ce cas, la commande ne sera disponible qu\'après l\'activation de l\'atelier (vous y avez basculé au moins une fois à l\'aide du sélecteur d\'atelier).

Comme la plupart d'entre elles nécessitent une interaction de l'utilisateur, les commandes FreeCAD ne sont disponibles qu'en mode graphique, et non en mode console. Cependant, pour des raisons pratiques, la plupart des commandes FreeCAD auront une fonction python correspondante (telle que `Part.makeBox` ou `Draft.makeLine`) ou exécuteront du code très facile à répliquer dans un script python et/ou dans des [macros](macros/fr.md).

Les commandes peuvent être définies en C ++ ou en Python.

## Commandes définies en C++ 

Exemple d\'une définition de commande C++, généralement définie suivant la structure {{FileName|Mod/ModuleName/Gui/Command.cpp}}.


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

## Commandes définies en Python 

Exemple d\'une définition de commande Python, elle peut être placée dans un répertoire comme {{FileName|Mod/ModuleName/tools/commands.py}}. 
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

## Exemples

Voir [Fonction - tracer une ligne](Line_drawing_function/fr.md).


{{Powerdocnavi

}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md) [Category:Glossary](Category:Glossary.md)
