# Command/de


## Einführung


{{TOCright}}

Ein [Befehl](Command/de.md) ist das, was ausgeführt wird, wenn Du eine Werkzeugleisten Schaltfläche oder einen Tastenkürzel eingibst. Es kann eine sehr einfache Handlung sein, wie den Zoomfaktor in der [3D Ansicht](3D_view/de.md) ändern oder das Drehen des Blickwinkels, oder ein komplexes System, das Dialogfenster öffnet und darauf wartet, dass der Benutzer bestimmte Aufgaben ausführt.

Jeder FreeCAD-Befehl hat einen eindeutigen Namen, der in der [Liste aller Befehle](:Category:Command_Reference/de.md)-Seite erscheint. Befehle können über eine Werkzeugleisten-Schaltfläche, einen Menüpunkt, oder aus einem [Python](Python/de.md)-Skript oder der [Python Konsole](Python_console/de.md), ausgeführt werden:


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Hintergrund

FreeCAD Befehle sind pro Arbeitsbereich definiert. Arbeitsbereiche werden ihre Befehlsdefinitionen normalerweise zum FreeCAD Programmstartzeitpunkt hinzufügen, so dass der Befehl existiert und verfügbar ist, sobald FreeCAD startet, unabhängig davon, ob der jeweilige Arbeitsbereich aktiviert ist oder nicht. Allerdings könnte der Arbeitsbereichsautor in einigen Fällen entschieden haben, den FreeCAD Startprozess nicht zu überlasten/belasten und deshalb die Befehlsdefinitionen erst bei der Initialisierung des Arbeitsbereichs zu laden. In diesen Fällen ist der Befehl erst nach der Aktivierung des Arbeitsbereichs verfügbar (Du hast wenigstens einmal dorthin mit dem Arbeitsbereichswähler gewechselt).

Da die meisten von ihnen Benutzeraktionen erfordern, sind FreeCAD Befehle nur im GUI-Modus und nicht im Konsolen Modus verfügbar. Der Einfachheit halber haben die meisten FreeCAD Befehle eine entsprechende Python Funktion (wie `Part.makeBox` oder `Draft.makeLine`) oder führen Code aus, der sehr einfach in einem Python Skript und/oder [Makronachgebildet](macros/de.md) werden kann.

Befehle können entweder in C++ oder Python festgelegt werden.

## In C++ definierte Befehle 

Beispiel einer C++ Befehlsdefinition, in der Regel definiert nach der Struktur {{FileName|Mod/ModuleName/Gui/Command.cpp}}.


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

## In Python definierte Befehle 

Beispiel für eine Python Befehlsdefinition, sie kann in einem Verzeichnis wie {{FileName|Mod/ModuleName/tools/commands.py}} abgelegt werden. 
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

## Beispiele

Siehe [Linienzeichungsfunktion](Line_drawing_function/de.md).


{{Powerdocnavi

}}

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md) [Category:Glossary](Category:Glossary.md)
