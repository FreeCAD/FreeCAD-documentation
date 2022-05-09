# Debugging/it
<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Prova preliminare 

Prima di provare il debug usare la [La struttura di Test](Testing/it.md) (test framework - macro) per verificare se i test standard funzionano correttamente. Se non funzionano, è possibile che l\'installazione sia danneggiata.

## Riga di comando 

Il debug di FreeCAD è supportato da alcuni meccanismi interni. La versione a riga di comando di FreeCAD fornisce delle opzioni di supporto del debug   *


<div class="mw-translate-fuzzy">

Queste sono le opzioni attualmente riconosciute in FreeCAD 0.15   *


</div>


<div class="mw-translate-fuzzy">

Opzioni generiche   *

 -v [ --version ]      Stampa una stringa della versione
 -h [ --help ]         Stampa un messaggio di aiuto
 -c [ --console ]      Avvia in modalità console
 --response-file arg   Può anche essere specificato con '@name'


</div>


<div class="mw-translate-fuzzy">

Configurazione   *

 -l [ --write-log ]       Scrive un file di log file in   * $HOME/.FreeCAD/FreeCAD.log
 --log-file arg           A differenza di --write-log permette di scrivere il file di log in un file arbitrario
 -u [ --user-cfg ] arg    File per caricare/salvare le impostazioni dell'utente
 -s [ --system-cfg ] arg  File per caricare/salvare le impostazioni di sistema
 -t [ --run-test ] arg    Livello di Test
 -M [ --module-path ] arg Percorsi di moduli aggiuntivi
 -P [ --python-path ] arg Percorsi aggiuntivi di python


</div>

## Generare un Backtrace 

Se si esegue una versione sperimentale di FreeCAD ancora in fase sviluppo, essa potrebbe \"bloccarsi\". Si può aiutare gli sviluppatori a risolvere questi problemi fornendo loro un \"backtrace\". Per fare questo, è necessario eseguire un \"debug build\" del software. \"Debug build\" è un parametro che viene impostato al momento della compilazione, perciò bisogna auto-compilare FreeCAD, oppure ottenere una versione \"debug\" precompilata.

### Per Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prerequisiti   *


<div class="mw-translate-fuzzy">

-   pacchetto software gdb installato
-   un debug build di FreeCAD (in questo momento disponibili solo per la [compilazione da sorgenti](Compile_on_Linux#For_a_Debug_build.md))
-   un modello di FreeCAD che causa un crash


</div>

Passaggi   *

Immettere quanto segue nella finestra del terminale   *

Find FreeCAD binary on your system   *


```python
$ whereis freecad
freecad   * /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

LLDB produrrà alcune informazioni di inizializzazione. Il (lldb) mostra che il debugger è in esecuzione nel terminale, ora inserisci   *   *


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

Ora FreeCAD viene avviato. Effettuare le operazioni che causano il crash o il blocco di FreeCAD, quindi immettere \'bt\' nella finestra del terminale.


```python
(gdb) bt
```

Questo genera una lunga lista che descrive esattamente ciò che il programma stava facendo quando è andato in crash o in blocco. Includere questa lista nel vostro rapporto sul problema.


```python
(gdb) bt full
```

Stampa anche i valori delle variabili locali. Questo può essere combinato con un numero per limitare il numero di frame mostrati.


</div>


</div>


<div class="mw-translate-fuzzy">

### Per MacOSX 


</div>


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">


<div class="mw-translate-fuzzy">

MacOSX Debugging →


</div>


<div class="mw-collapsible-content">

Prerequisiti   *

-   pacchetto software lldb installato
-   un debug build di FreeCAD
-   un modello di FreeCAD che causa un crash

Passaggi   *

Immettere quanto segue nella finestra del terminale   *


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB produrrà alcune informazioni di inizializzazione. Il (lldb) mostra che il debugger è in esecuzione nel terminale, ora inserisci   *


```python
(lldb) run
```

Ora FreeCAD viene avviato. Effettuare le operazioni che causano il crash o il blocco di FreeCAD, quindi immettere \'bt\' nella finestra del terminale.


```python
(lldb) bt
```

Questo genera una lunga lista che descrive esattamente ciò che il programma stava facendo quando è andato in crash o in blocco. Includere questa lista nel vostro rapporto sul problema.


</div>


</div>

## List Libraries Loaded by FreeCAD 

(Applicable to Linux and macOS)

Sometimes it\'s helpful to understand what libraries FreeCAD is loading, specifically if there are multiple libraries being loaded of the same name but different versions (version collision). In order to see which libraries are loaded by FreeCAD when it crashes you should open a terminal and run it in the debugger. In a second terminal window, find out the process id of FreeCAD   *


`ps -A &#124; grep FreeCAD`

Use the returned id and pass it to `lsof`   *


` lsof -p process_id`

This prints a long list of loaded resources. So for example, if trying to ascertain if more than one Coin3d library versions is loaded, scroll through the list or search directly for Coin in the output   *


`lsof -p process_id &#124; grep Coin`

## Eliminare errori Python 

Per un approccio più moderno al debug di Python, almeno su Windows, vedere questo

-   \[<https   *//forum.freecadweb.org/viewtopic.php?f=22&t=28901&hilit=2017>\| post nel Forum\].
-   [Python workbenches debugging](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https   *//forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

winpdb Debugging →


<div class="mw-collapsible-content">

Ecco un esempio dell\'uso di \"Winpdb\" all\'interno di FreeCAD   *


<div class="mw-translate-fuzzy">

Abbiamo bisogno del debugger di Python   * \"Winpdb\". Se non lo hai installato, su Ubuntu/Debian installalo con   *


</div>


```python
sudo apt-get install winpdb
```

Ora consente di impostare il debugger.

1.  Start *Winpdb*.
2.  Imposta la password del debugger su \"test\"   * vai al menu \"File\" → \"Password\" e imposta la password.


<div class="mw-translate-fuzzy">

Ora eseguiremo uno script Python di prova in FreeCAD passo dopo passo.


</div>

1.  Eseguire winpdb e impostare la password (ad esempio test)
2.  Creare un file Python con questo contenuto


```python
import rpdb2
rpdb2.start_embedded_debugger("test")
import FreeCAD
import Part
import Draft
print "hello"
print "hello"
import Draft
points=[FreeCAD.Vector(-3.0,-1.0,0.0),FreeCAD.Vector(-2.0,0.0,0.0)]
Draft.makeWire(points,closed=False,face=False,support=None)
```

1.  Avviare FreeCAD e caricare il file precedente in FreeCAD.
2.  Premere F6 per eseguirlo.
3.  Ora FreeCAD non risponde perché il debugger Python è in attesa
4.  Passare alla GUI di Windpdb e cliccare su \"Attach\". Dopo pochi secondi appare una voce \"\" su cui si deve fare doppio clic.
5.  Ora in Winpdb viene visualizzato lo script attualmente in esecuzione.
6.  Impostare un break nell\'ultima riga e premere F5.
7.  Ora premere F7 per entrare nel codice Python di Draft.makeWire


</div>


</div>

### Visual Studio Code (VS Code) 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

VS Code Debugging →


<div class="mw-collapsible-content">

Prerequisiti   *


<div class="mw-translate-fuzzy">

-   ptvsd il pacchetto deve essere installato


</div>


```python
# In a cmd window that has a path to you local Python 3   *
pip install ptvsd
# Then if your Python is installed in C   *Users\<userid>\AppData\Local\Programs\Python\Python37
# and your FreeCAD is installed in C   *freecad\bin
xcopy "C   *Users\<userid>\AppData\Local\Programs\Python\Python37\Lib\site-packages\ptvsd" "C   *freecad\bin\Lib\site-packages\ptvsd"
```

[pypi page](https   *//pypi.org/project/ptvsd/)

[Documentazione di Visual Studio Code per il debug remoto](https   *//code.visualstudio.com/docs/python/debugging#_remote-debugging)

Passi   *

-   Aggiungi il seguente codice all\'inizio del tuo script


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```


<div class="mw-translate-fuzzy">

-   Aggiungi una configurazione di debug nel codice di Visual Studio **Debug → Aggiungi configurazioni ...**. Dovrebbe apparire così   *


</div>

        "configurations"   * [
            {
                "name"   * "Python   * Attacher",
                "type"   * "python",
                "request"   * "attach",
                "port"   * 5678,
                "host"   * "localhost",
                "pathMappings"   * [
                    {
                        "localRoot"   * "${workspaceFolder}",
                        "remoteRoot"   * "."
                    }
                ]
            },


<div class="mw-translate-fuzzy">

-   In VS Code aggiungi un breakpoint dove vuoi.
-   Avvia lo script in FreeCAD. Blocco di FreeCAD in attesa di allegato.
-   In VS Code avviare il debug della configurazione creata utilizzata. Dovresti vedere le variabili nell\'area debugger.


</div>


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

Where the path is to the directory where ptvsd was installed.

-   On the left bottom edge of VSCode you can choose the Python executable - it\'s best to make this the version packaged with FreeCAD.

In the Mac package it is /Applications/FreeCAD.App/Contents/Resources/bin/python.

You can locate it on your system by typing


```python
import sys
print(sys.executable)
```

into FreeCAD\'s Python console.


</div>


</div>

### With LiClipse and AppImage 


<div class="toccolours mw-collapsible mw-collapsed" style="width   *800px;">

LiClipse Debugging →


<div class="mw-collapsible-content">

-   Extract AppImage.


```python
> ./your location/FreeCAD_xxx.AppImage --appimage-extract
> cd squashfs-root/
```

-   The sqashfs-root location is where the debugger later on is hooked up to.

-   Make sure you can start a FreeCAD session from within the squashfs-root location.


```python
squashfs-root> ./usr/bin/freecadcmd
```

-   Should start up a FreeCAD commandline session.

-   Install [LiClipse](https   *//www.liclipse.com/).
    -   Comes ready with pydev and has installers for all platforms.
    -   For linux it is just to extract (to any location) and run.

-   Configure liclipse for debugging.
    -   Right-click pydev icon (upper right corner) and choose customize.
        -   Activate \"PyDev Debug\" (through checkbox, or it might be needed to go to tab \"Action Set Availability\" and activate there first).
        -   In the pydev menu you can now choose \"start debug server\".
    -   Use menu window/open perspective/other \> debug.
        -   Right-click debug icon (upper right corner) and choose customize.
        -   Checking \"Debug\" brings the debugging navigation tools to the toolbar.
    -   Open preferences through menu window/preferences.
        -   In PyDev/Interpreters add \"new Interpreter by browsing\".
        -   The added interpreter should be   * `your loc/squashfs-root/usr/bin/python`.
        -   If you are only using this for fc, you can add AddOn workbench folders as well, or do that in a pydev-project later on.

-   Find path to `pydevd.py` in your liclipse installation.
    -   Something along the lines of   * `your location/liclipse/plugins/org.python.pydev.xx/pysrc`.
-   Create a regular pydev-project in liclipse.
    -   Import external sources, for example a macro that you want to debug, or an external workbench.
    -   In that macro (or workbench .py file) add the code lines   *

   *   
    
```python
    import sys; sys.path.append("path ending with /pysrc")
    import pydevd; pydevd.settrace()
    
```
    

   ** This is where the execution will halt when the macro is run.

-   Start the liclipse debug server (menu pydev).

-   Start FreeCAD.


```python
squashfs-root> ./usr/bin/freecad
```

-   Run the macro (or any other file with a `pydevd.settrace()` trigger) from within freecad, as you would normally do.

-   Happy debugging.

-   The use of LiClipse for remote debugging, and the steps described here related to liclipse, should work on any platform. The parts related to AppImage is for linux only.


</div>


</div>

## Debugging OpenCasCade 

For developers needing to dig deeper in to the OpenCasCade kernel, user \@abdullah has created a [thread](https   *//forum.freecadweb.org/viewtopic.php?f=10&t=47017) orientation discussing how to do so.


<div class="mw-translate-fuzzy">





</div>


 

[Category   *Developer Documentation](Category_Developer_Documentation.md) [Category   *Python Code](Category_Python_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Debugging/it
