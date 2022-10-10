# Command/it
## Introduzione


{{TOCright}}

Un **Comando** è ciò che viene eseguito quando si preme un pulsante della barra degli strumenti o si digita una scorciatoia da tastiera. Può essere un\'azione molto semplice, come cambiare il livello di zoom della vista 3D o ruotare il punto di vista oppure un sistema complesso che apre le finestre di dialogo e attende che l\'utente esegua delle specifiche attività.

Ogni comando di FreeCAD ha un nome univoco, che appare nella pagina [   *Category   *Command Reference](   *Category_Command_Reference.md) se originale inglese, e nella pagina [   *Category   *Command_Reference/it](   *Category   *Command_Reference/it.md) per le traduzioni . I comandi possono essere lanciati da un pulsante della barra degli strumenti, da una voce di menu o da uno script [Python](Python/it.md) o dalla [console Python](Python_console/it.md), eseguendo   *


```python
FreeCADGui.runCommand("my_Command_Name")
```

## Introduzione 

I comandi di FreeCAD sono definiti per ambienti (workbench). Normalmente gli ambienti aggiungono le loro definizioni di comando all\'avvio di FreeCAD, quindi il comando esiste ed è disponibile non appena viene avviato FreeCAD, non importa se l\'ambiente corrispondente è stato attivato o meno. In alcuni casi, però, l\'autore dell\'ambiente può aver deciso, per non sovraccaricare troppo il processo di avvio di FreeCAD, di caricare le definizioni dei comandi solo all\'avvio dell\'ambiente. In questi casi, il comando è disponibile solo dopo che l\'ambiente è stato attivato (si è passati ad esso almeno una volta usando il selettore dei workbench).

Dato che la maggior parte richiede l\'interazione dell\'utente, i comandi di FreeCAD sono disponibili solo in modalità GUI e non in modalità console. Tuttavia, per praticità, la maggior parte dei comandi di FreeCAD ha una corrispondente funzione Python (come `Part.makeBox` o `Draft.makeLine`), o si può eseguire il codice che è molto facile da replicare in uno script Python o in una [macro](macros/it.md).

I comandi possono essere definiti sia in C++ che in Python.

## Comandi definiti in C++ 

Esempio di definizione di un comando C++, di solito definito seguendo la struttura **Mod/ModuleName/Gui/Command.cpp**.


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

## Comandi definiti in Python 

Esempio di definizione di un comando Python, esso può essere posizionato in una directory come **Mod/ModuleName/tools/commands.py**. 
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

## Esempi

Vedere [Funzione per disegnare delle linee](Line_drawing_function/it.md).




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md) [Category   *Glossary](Category_Glossary.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Command_Reference|:Category:Command Reference]] se originale inglese, e nella pagina ](Category_Command_Reference|:Category:Command Reference]] se originale inglese, e nella pagina .md) > [Command_Reference/it]]  per le traduzioni . I comandi possono essere lanciati da un pulsante della barra degli strumenti, da una voce di menu o da uno script ](Category_Command_Reference/it]]  per le traduzioni . I comandi possono essere lanciati da un pulsante della barra degli strumenti, da una voce di menu o da uno script .md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Command/it
