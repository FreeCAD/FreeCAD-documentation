# Macro at Startup/it
<div class="mw-translate-fuzzy">

## Introduzione


</div>


{{TOCright}}

Questa documentazione spiega come impostare una macro in modo che venga eseguita automaticamente all\'avvio di FreeCAD.


<div class="mw-translate-fuzzy">

Prima di iniziare, bisogna considerare le seguenti cose    *

-   L\'esecuzione automatica di macro all\'avvio può essere considerata un rischio per la sicurezza. Si devono eseguire solo delle macro fidate e testate in precedenza.
-   Per seguire questa procedura bisogna avere alcune nozioni di Python e di codifica.
-   Quando si fa riferimento a delle cartelle utente (\'Mod\', \'Macro\', \...), esse si trovano nella cartella FreeCAD dell\'utente. È possibile trovarle in Avvio e configurazione → [Informazioni relative all\'utente](Start_up_and_Configuration/it#Informazioni_relative_all'utente.md)
-   Questo comportamento non dovrebbe essere utilizzato per le macro che si occupano della modellazione delle parti. Questo è più appropriato per le macro che aggiungono funzionalità, migliorano l\'interfaccia utente, \...


</div>


<div class="mw-translate-fuzzy">

# Come fare 


</div>


<div class="mw-translate-fuzzy">

## Preparare la macro 


</div>

In genere, una macro non è pensata e fatta per essere eseguita all\'avvio, quindi deve essere ottimizzata.


<div class="mw-translate-fuzzy">

Prendere in considerazione la macro sottostante, memorizzata nella propria cartella \'Macro\' con il nome \'MySuperMacro.FCMacro\'   *


</div>

    ## Import section ##
    from PySide import QtGui

    ## Definition section (classes, functions, ...)
    class MyMsgBox(QtGui.QMessageBox)   *

        def __init__(self)   *
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Main instruction section
    MyMsgBox()


<div class="mw-translate-fuzzy">

Tutte le macro presentano generalmente una struttura simile con prima sezione di importazione, quindi una sezione di definizione e infine una sezione di istruzione principale. Ci concentreremo su quest\'ultima sezione perché le istruzioni principali sono in realtà quelle che \'eseguono\' la macro (sono abbastanza facili da individuare perché cominciano all\'inizio della riga). Nel passaggio successivo, bisogna importare la macro a livello di codice, quindi eseguirla. Questo non può essere fatto con la struttura effettiva della macro. Per poterlo fare, bisogna racchiudere le istruzioni principali in una funzione \--eg. run()\-- quindi assicurarsi che questa funzione sia ancora chiamata quando la macro viene eseguita manualmente dall\'utente. Se non si è completamente sicuri di ciò che si sta facendo, è meglio lavorare su una copia della macro (anche per conservare l\'originale della macro). Il file originale deve essere modificato come segue   *


</div>

    from PySide import QtGui
    ## The 2 below lines shall be added if not already present to ensure FreeCAD modules are imported
    import FreeCAD as App
    import FreeCADGui as Gui

    class MyMsgBox(QtGui.QMessageBox)   *

        def __init__(self)   *
            super(MyMsgBox, self).information(None, "MyTitle", "MyText")

    ## Enclose the main instructions in a function
    def run()   *
        MyMsgBox()

    ## Ensure main instructions are still called in case of manual run
    if __name__ == '__main__'   *
        run()

Ovviamente se la funzione \'run()\' esiste già nella macro, si può usare qualsiasi altro nome. Ora la macro è pronta per essere integrata nell\'avvio di FreeCAD.


<div class="mw-translate-fuzzy">

## Integrare la macro nell\'avvio di FreeCAD 


</div>


<div class="mw-translate-fuzzy">

Innanzitutto creare una nuova cartella nella cartella \"Mod\" dell\'utente, ad esempio \"MacroStartup\". Copiare la macro modificata in questa cartella appena creata e rinominala con un\'estensione \'.py\' se questo non è ancora il caso (nota che se sviluppi la macro da solo, può essere nominata con l\'estensione \".py\" anche in la cartella \"Macro\" in modo che non sia necessario rinominare durante la copia). Infine, creare nella stessa cartella un file chiamato \"InitGui.py\" in cui inserire il seguente codice   *


</div>

    def runStartupMacros(name)   *
        # Do not run when NoneWorkbench is activated because UI isn't yet completely there
        if name != "NoneWorkbench"   *
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

Notare che viene eseguita solo una volta. Se si vuole eseguire più di una macro, bisogna semplicemente aggiungere le altre nello stesso file (guardare i commenti sul codice precedente).


<div class="mw-translate-fuzzy">

Il lavoro è finito. La macro dovrebbe essere eseguita automaticamente al prossimo avvio di FreeCAD.


</div>

Notare che se la macro originale è stata scaricata tramite Addon Manager, nel caso di aggiornamento essa viene sovrascritta e quindi è necessario eseguire di nuovo questi passaggi.

## General Notes 

-   In the example \'InitGui.py\' script above, the function named \'runStartupMacros()\' may be changed, so long as you also change the other four references to it, so they all match.
-   This script will be run prior to the auto loading of your desired startup workbench in the FreeCAD Preferences, [General settings](Preferences_Editor#General_settings.md).

### Linux

### MacOS

### Windows

-   In the above example, you may place the \'MacroStartup\' folder within the \'Mod\' folder of your FreeCAD root directory (whether installed version or portable version), or you may create a \'Mod\' folder along side the \'Macro\' folder in \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\\', and place the \'MacroStartup\' folder there.
-   From observation, the workbenches found within either \'Mod\' folder are loaded alphabetically. Those in the FreeCAD root \'Mod\' folder are loaded first, then FreeCAD scans the \'%USERPROFILE%\\AppData\\Roaming\\FreeCAD\\Mod\' folder for additional workbenches.

## Related

-   [LazyLoader](Extra_python_modules#LazyLoader.md) is a Python module that allows deferred loading.




[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md) [Category   *Macros](Category_Macros.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Macros](Category_Macros.md) > Macro at Startup/it
