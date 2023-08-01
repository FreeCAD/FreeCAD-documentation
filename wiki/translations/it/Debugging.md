# Debugging/it
## Prova preliminare 

Prima di provare il debug usare la [Struttura di Test](Testing/it.md) (test framework - macro) per verificare se i test standard funzionano correttamente. Se non funzionano, è possibile che l\'installazione sia danneggiata.



## Riga di comando 

Il debug di FreeCAD è supportato da alcuni meccanismi interni. La versione a riga di comando di FreeCAD fornisce delle opzioni di supporto del debug:

Queste sono le opzioni attualmente riconosciute in FreeCAD 0.19:

Opzioni generiche:

 -v [ --version ]        Stampa la stringa della versione
 -h [ --help ]           Stampa un messaggio di aiuto
 -c [ --console ]        Si avvia in modalità console
 --response-file arg     Può essere specificato anche con '@name'
 --dump-config           Scarica la configurazione
 --get-config arg        Stampa il valore della chiave di configurazione richiesta

Configurazione:
-l \[ \--write-log \] Scrive un file di registro in:

                           $HOME/.local/share/FreeCAD/FreeCAD.log (Linux)
                           $HOME/Libreria/Applicazione\Supporto/FreeCAD/FreeCAD.log (macOS)
                           %APPDATA%\FreeCAD\FreeCAD.log (Windows)
 --log-file arg            Diversamente da --write-log, questo consente di accedere a un file
                           archivio arbitrario
 -u [ --user-cfg ] arg     File di configurazione utente per caricare/salvare le impostazioni utente
 -s [ --system-cfg ] arg   File di configurazione del sistema per caricare/salvare le impostazioni di sistema
 -t [ --run-test ] arg     Test case - o 0 per tutti
 -M [ --module-path ] arg  Percorsi di moduli aggiuntivi
 -P [ --python-path ] arg  Percorsi Python aggiuntivi
 --single-instance         Consente di eseguire una singola istanza dell'applicazione



## Generare un Backtrace 

Se si esegue una versione sperimentale di FreeCAD ancora in fase sviluppo, essa potrebbe \"bloccarsi\". Si può aiutare gli sviluppatori a risolvere questi problemi fornendo loro un \"backtrace\". Per fare questo, è necessario eseguire un \"debug build\" del software. \"Debug build\" è un parametro che viene impostato al momento della compilazione, perciò bisogna auto-compilare FreeCAD, oppure ottenere una versione \"debug\" precompilata.



### Per Linux 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

Linux Debugging →


<div class="mw-collapsible-content">

Prerequisiti:

-   pacchetto software gdb installato
-   un debug build di FreeCAD (in questo momento disponibili solo per la [compilazione di Debug](Compile_on_Linux/it#Per_una_compilazione_di_Debug.md))
-   un modello di FreeCAD che causa un crash

Passaggi:

Immettere quanto segue nella finestra del terminale:

Trovare il codice binario di FreeCAD sul proprio sistema:


```python
$ whereis freecad
freecad: /usr/local/freecad <--- for example

$ cd /usr/local/freecad/bin
$ gdb FreeCAD
```

LLDB produrrà alcune informazioni di inizializzazione. Il (lldb) mostra che il debugger è in esecuzione nel terminale, ora inserisci::


```python
(gdb) handle SIG33 noprint nostop
(gdb) run
```

FreeCAD verrà avviato. Effettuare le operazioni che causano il crash o il blocco di FreeCAD, quindi immettere \'bt\' nella finestra del terminale.


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



### Per macOSX 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

macOSX Debugging →


<div class="mw-collapsible-content">

Prerequisiti:

-   pacchetto software lldb installato
-   un debug build di FreeCAD
-   un modello di FreeCAD che causa un crash

Passaggi:

Immettere quanto segue nella finestra del terminale:


```python
$ cd FreeCAD/bin
$ lldb FreeCAD
```

LLDB produrrà alcune informazioni di inizializzazione. Il (lldb) mostra che il debugger è in esecuzione nel terminale, ora inserisci:


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



## Elencare le librerie caricate da FreeCAD 

(Applicabile a Linux e macOS)

A volte è utile capire quali librerie sta caricando FreeCAD, in particolare se ci sono più librerie caricate con lo stesso nome ma versioni diverse (collisione di versioni). Per vedere quali librerie vengono caricate da FreeCAD quando si arresta in modo anomalo, è necessario aprire un terminale ed eseguirlo nel debugger. In una seconda finestra del terminale, scopri l\'id del processo di FreeCAD:


`ps -A &#124; grep FreeCAD`

Usa l\'id restituito e passalo a `lsof`:


` lsof -p process_id`

Questo stampa un lungo elenco di risorse caricate. Quindi, ad esempio, se si tenta di verificare se è caricata più di una versione della libreria Coin3d, scorrere l\'elenco o cercare direttamente Coin nell\'output:


`lsof -p process_id &#124; grep Coin`



## Eliminare errori Python 

Per un approccio più moderno al debug di Python, almeno su Windows, vedere questo

-   \[<https://forum.freecadweb.org/viewtopic.php?f=22&t=28901&hilit=2017>\| post nel Forum\].
-   [Python workbenches debugging](https://forum.freecadweb.org/viewtopic.php?f=10&t=35383)
-   [python3.dll, Qt5Windgets.dll, Qt5Gui.dll and Qt5Core.dll not found](https://forum.freecadweb.org/viewtopic.php?f=4&t=40251)

### winpdb


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

winpdb Debugging →


<div class="mw-collapsible-content">

Ecco un esempio dell\'uso di \"Winpdb\" all\'interno di FreeCAD:

E\' necessario il debugger di Python: \"Winpdb\". Se non lo è installato, su Ubuntu/Debian installarlo con:


```python
sudo apt-get install winpdb
```

Questo consente di impostare il debugger.

1.  Start *Winpdb*.
2.  Impostare la password del debugger su \"test\": andare al menu \"File\" → \"Password\" e impostare la password.

Ora si esegua uno script Python di prova in FreeCAD passo dopo passo.

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


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

VS Code Debugging →


<div class="mw-collapsible-content">

Prerequisiti:

-   Il pacchetto ptvsd deve essere installato in un Python 3 al di fuori di FreeCAD, quindi il modulo deve essere copiato nella cartella della libreria Python di FreeCAD.


```python
# In a cmd window that has a path to you local Python 3:
pip install ptvsd
# Then if your Python is installed in C:\Users\<userid>\AppData\Local\Programs\Python\Python37
# and your FreeCAD is installed in C:\freecad\bin
xcopy "C:\Users\<userid>\AppData\Local\Programs\Python\Python37\Lib\site-packages\ptvsd" "C:\freecad\bin\Lib\site-packages\ptvsd"
```

[pypi page](https://pypi.org/project/ptvsd/)

[Documentazione di Visual Studio Code per il debug remoto](https://code.visualstudio.com/docs/python/debugging#_remote-debugging)

Passi:

-   Aggiungere il seguente codice all\'inizio dello script


```python
import ptvsd
print("Waiting for debugger attach")
# 5678 is the default attach port in the VS Code debug configurations
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

-   Aggiungere una configurazione di debug nel codice di Visual Studio **Debug → Aggiungi configurazioni ...**.
-   La configurazione dovrebbe assomigliare a questa:




        "configurations": [
            {
                "name": "Python: Attacher",
                "type": "python",
                "request": "attach",
                "port": 5678,
                "host": "localhost",
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            },

-   In VS Code aggiungere un breakpoint dove si desidera.
-   Avviare lo script in FreeCAD. FreeCAD si blocca in attesa dell\'allegato.
-   In VS Code avviare il debug, utilizzando la configurazione creata. Si dovrebbero vedere le variabili nell\'area del debugger.
-   Quando si impostano i punti di interruzione, VS Code segnalerà di non trovare il file .py aperto nell\'editor di VS Code.
    -   Cambiare \"remoteRoot\": \".\" to \"remoteRoot\": \"\"
        -   Ad esempio, se il file Python risiede in */home/FC_myscripts/myscript.py*
        -   Cambiare in: \"remoteRoot\": \"/home/FC_myscripts\"
    -   Se si sta solo eseguendo il debug delle macro di FreeCAD dalla cartella delle macro di FreeCAD e quella cartella è \"C:/Users//AppData/Roaming/FreeCAD/Macro\", usare:
        -   \"localRoot\": \"C:/Users//AppData/Roaming/FreeCAD/Macro\",
        -   \"remoteRoot\": \"C:/Users//AppData/Roaming/FreeCAD/Macro\"
-   Se la macro non riesce a trovare ptvsd nonostante l\'abbia installata da qualche parte, far precedere \'import ptvsd\' con


```python
from sys import path
sys.path.append('/path/to/site-packages')
```

Dove si trova il percorso della directory in cui è stato installato ptvsd.

-   Sul bordo in basso a sinistra di VSCode si può scegliere l\'eseguibile Python: è meglio impostarlo alla versione installata con FreeCAD.

Nel package Mac è /Applications/FreeCAD.App/Contents/Resources/bin/python.

E\' possibile individuarlo sul proprio sistema digitando


```python
import sys
print(sys.executable)
```

nella console Python di FreeCAD.


</div>


</div>



### Con LiClipse e AppImage 


<div class="toccolours mw-collapsible mw-collapsed" style="width:800px;">

LiClipse Debugging →


<div class="mw-collapsible-content">

-   Estrarre AppImage.


```python
> ./your location/FreeCAD_xxx.AppImage --appimage-extract
> cd squashfs-root/
```

-   La posizione sqashfs-root è il punto in cui il debugger viene successivamente collegato.

-   Assicurarsi di poter avviare una sessione di FreeCAD dalla posizione squashfs-root.


```python
squashfs-root> ./usr/bin/freecadcmd
```

-   Si dovrebbe avviare una sessione della riga di comando di FreeCAD.

-   Installare [1](https://www.liclipse.com/LiClipse).
    -   Viene fornito pronto con pydev e dispone di programmi di installazione per tutte le piattaforme.
    -   Per Linux è sufficiente estrarlo (in qualsiasi posizione) ed eseguire.

-   Configurare liclipse per il debug.
    -   Fare clic con il pulsante destro del mouse sull\'icona pydev (angolo in alto a destra) e scegli Personalizza.
        -   Attivare \"PyDev Debug\" (tramite la casella di controllo, oppure potrebbe essere necessario andare alla scheda \"Disponibilità set di azioni\" e attivarla prima).
        -   Nel menu pydev scegliere \"start debug server\".
    -   Usare finestra menu/apri prospettiva/altro \> debug.
        -   Fai clic con il pulsante destro del mouse sull\'icona di debug (angolo in alto a destra) e scegliere Personalizza.
        -   Selezionando \"Debug\" vengono visualizzati gli strumenti di navigazione di debug nella barra degli strumenti.
    -   Aprire le preferenze tramite la finestra del menu/preferenze.
        -   In PyDev/Interpreters aggiungere \"nuovo interprete navigando\".
        -   L\'interprete aggiunto dovrebbe essere: `your loc/squashfs-root/usr/bin/python`.
        -   Se si sta usando solo per fc, si possono aggiungere anche le cartelle del workbench AddOn o farlo in un progetto pydev in seguito.

-   Trovare il percorso per `pydevd.py` nella tua installazione di liclipse.
    -   Qualcosa sulla falsariga di: `your location/liclipse/plugins/org.python.pydev.xx/pysrc`.
-   Creare un normale progetto pydev in liclipse.
    -   Importare fonti esterne, ad esempio una macro di cui si desidera eseguire il debug o un workbench esterno.
    -   In quella macro (o file .py del workbench) aggiungere le righe di codice:

:   
    
```python
    import sys; sys.path.append("path ending with /pysrc")
    import pydevd; pydevd.settrace()
    
```
    

  - Questo è il punto in cui l\'esecuzione si fermerà quando viene eseguita la macro.

-   Avviare il server di debug liclipse (menu pydev).

-   Avviare FreeCAD.


```python
squashfs-root> ./usr/bin/freecad
```

-   Eseguire la macro (o qualsiasi altro file con un trigger `pydevd.settrace()`) da freecad, come si farebbe normalmente.

-   Buon debug.

-   L\'uso di LiClipse per il debug remoto e i passaggi qui descritti relativi a liclipse dovrebbero funzionare su qualsiasi piattaforma. Le parti relative ad AppImage sono solo per Linux.


</div>


</div>

## Debugging OpenCasCade 

Per gli sviluppatori che hanno bisogno di approfondire il kernel OpenCasCade, l\'utente \@abdullah ha creato un [thread](https://forum.freecadweb.org/viewtopic.php?f=10&t=47017) di orientamento che spiega come farlo.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Debugging/it
