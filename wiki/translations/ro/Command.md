# Command/ro
## Introduction


{{TOCright}}


<div class="mw-translate-fuzzy">

O comandă în FreeCAD este o aplicație care se execută atunci când apăsați un buton din bara de instrumente sau apăsați o scurtătură din tastatură. Poate fi o acțiune foarte simplă, cum ar fi schimbarea nivelului de zoom al vizualizării 3D sau rotirea punctului de vedere sau un sistem complex care va deschide casetele de dialog și va aștepta ca utilizatorul să îndeplinească anumite sarcini.


</div>


<div class="mw-translate-fuzzy">

Fiecare comandă FreeCAD are un nume unic care apare în lista tuturor comenzilor [   *Category   *Command_Reference](   *Category_Command_Reference.md). Comenzile pot fi invocate prin intermediul unui buton al barei de instrumente, al unei intrări în meniu, al unui script Python sau al consolei Python rulând   *


</div>


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Background


<div class="mw-translate-fuzzy">

Comenzile FreeCAD sunt definite prin Atelier/workbench. Atelierele de lucru vor adăuga, de regulă, definițiile comenzilor lor la momentul de pornire al programului FreeCAD, astfel încât comanda să existe și să fie disponibilă imediat ce începe FreeCAD, indiferent dacă Atelierul de lucru este activat sau nu. Cu toate acestea, în unele cazuri, autorul Atelierului de lucru s-ar fi putut decide să nu supraîncărcați procesul de boot FreeCAD și, prin urmare, să încărcați definițiile comenzii numai la inițializarea spațiului de lucru. În acele cazuri, comanda nu va fi disponibilă până când nu ați activat Atelierul de lucru (ați fost comutat cel puțin o dată acolo cu selectorul de Ateliere).


</div>


<div class="mw-translate-fuzzy">

Deoarece majoritatea dintre ele necesită interacțiune cu utilizatorul, comenzile FreeCAD sunt disponibile numai în modul GUI și nu în modul consola. Pentru simplificare, majoritatea comenzilor FreeCAD au o funcție Python corespunzătoare (cum ar fi Part.makeBox sau Draft.makeLine) sau execută un cod care poate fi ușor replicat într-un script Python.


</div>

Comenzile pot fi definite sau în C++ ori în Python.

## Commands defined in C++ 


<div class="mw-translate-fuzzy">

Exemplu de definiție a comenzii în C++ (usually defined in /Mod/ModuleName/Gui/Command.cpp)   *


</div>


{{Code|lang=cpp|code=
DEF_STD_CMD_A(StdCmdMyCommand);

StdCmdMyCommand   *   *StdCmdMyCommand()
     * Command("Std_My_Command")
{
    sGroup        = QT_TR_NOOP("File");
    sMenuText     = QT_TR_NOOP("My Command");
    sToolTipText  = QT_TR_NOOP("Runs my command in the active document");
    sWhatsThis    = "Std_MyCommand";
    sStatusTip    = QT_TR_NOOP("Runs my command in the active document");
    sPixmap       = "MyCommand.svg";
    sAccel        = "Ctrl+A";
}

void StdCmdExport   *   *activated(int iMsg)
{
    // place here the code to be executed when the command is ran
}

bool StdCmdMyCommand   *   *isActive(void)
{
    // here you have a chance to return true or false depending if your command must be shown as active or inactive (greyed).
}

// the command must be "registered" in FreeCAD's command system
CommandManager &rcCmdMgr = Application   *   *Instance->commandManager();
rcCmdMgr.addCommand(new StdCmdMyCommand());
}}

## Commands defined in Python 


<div class="mw-translate-fuzzy">

și comanda similară în python (no rule for where it must be done, each python workbench does as it sees fit\...)


</div>


```python
from PySide.QtCore import QT_TRANSLATE_NOOP


class MyCommand   *
    """Explanation of the command."""

    def __init__(self)   *
        """Initialize variables for the command that must exist at all times."""
        pass

    def GetResources(self)   *
        """Return a dictionary with data that will be used by the button or menu item."""
        return {'Pixmap'   * 'MyCommand.svg',
                'Accel'   * "Ctrl+A",
                'MenuText'   * QT_TRANSLATE_NOOP("My_Command", "My Command"),
                'ToolTip'   * QT_TRANSLATE_NOOP("My_Command", "Runs my command in the active document")}

    def Activated(self)   *
        """Run the following code when the command is activated (button press)."""
        print("Activated")

    def IsActive(self)   *
        """Return True when the command should be active or False when it should be disabled (greyed)."""
        return True

# The command must be "registered" with a unique name by calling its class.
FreeCADGui.addCommand('My_Command', MyCommand())
```

## Examples

See [Line drawing function](Line_drawing_function.md).




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md) [Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Command/ro
