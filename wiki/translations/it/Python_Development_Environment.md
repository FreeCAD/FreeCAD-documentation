# Python Development Environment/it
## Un semplicistico Ambiente di sviluppo per Python all\'interno di FreeCAD 


<div class="mw-translate-fuzzy">

[Python](wikipedia:Python_(programming_language).md) è l\'ambiente di programmazione che è stato incorporato nel sistema di [FreeCAD](http://www.freecadweb.org/). Usando Python molte delle operazioni offerte da FreeCAD sono accessibili tramite programmazione. Di solito i programmi in Python per FreeCAD sono sviluppati per essere eseguiti nella console Python o attraverso la facilitazione delle Macro di FreeCAD (vedere [Come installare le macro](How_to_install_macros/it.md)).


</div>

Gli strumenti disponibili per lo sviluppo di programmi in Python sono numerosi. I fattori di complicazione per lo sviluppo di Python da usare con FreeCAD sono due: in primo luogo gli strumenti non hanno alcun supporto per le numerose strutture di dati e punti di accesso di FreeCAD; in secondo luogo non funzionano \"internamente a FreeCAD\". Ciò significa che è possibile utilizzare Python per sviluppare del codice all\'esterno di FreeCAD senza poterlo testare nell\'ambiente di destinazione; oppure si può svilupparlo nell\'ambiente di destinazione (ad esempio l\'ambiente FreeCAD), ma senza poter usufruire del supporto degli strumenti di sviluppo. Nessuna di queste è una soluzione accettabile.

## Background


<div class="mw-translate-fuzzy">

## Introduzione

Lo sviluppo dei software moderni nello standard commerciale di solito è fatto con un set di strumenti genericamente denominato [\'IDE\'](wikipedia_Integrated_development_environment.md) (Integrated Development Environment - Ambiente di sviluppo integrato). Tipicamente questi strumenti sono i seguenti 3:


</div>

-   un editor di codice sorgente
-   uno strumento di building automatico
-   un debugger

che sono standard, mentre i seguenti sono presenti in alcuni IDE, ma non in altri:

-   un tool di building automatico
-   un compilatore e/o un interprete integrato
-   un sistema di controllo di versione
-   gli strumenti per costruire la GUI (Graphical User Interface - Interfaccia Grafica per l\'Utente)
-   un navigatore di classi
-   un analizzatore di oggetti
-   un diagramma della gerarchia delle classi


<div class="mw-translate-fuzzy">

Una sintesi dello stato di questi strumenti all\'interno FreeCAD è (\'N/A\' significa \'Non disponibile\', (\'Not Available\')):


<table style="width: 100%" border="1">


<tr>


<td>

editor di codice sorgente


</td>


<td>

per le piattaforme supportate da FreeCAD sono disponibili vari editor, discussi in seguito


</td>


</tr>


<tr>


<td>

tool di building automatico


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

debugger


</td>


<td>

pianificato, ma non ancora disponibile, ci sono alcune soluzioni che sono discusse in seguito


</td>


</tr>


<tr>


<td>

intelligent code completion


</td>


<td>

qualcosa è disponibile tramite la console Python, ma solo questo


</td>


</tr>


<tr>


<td>

compilatore e/o interprete integrato


</td>


<td>

Il compilatore Python è integrato con la console Python, ma non con gli editor


</td>


</tr>


<tr>


<td>

sistema di controllo di versione


</td>


<td>

N/A - c\'è solo una versione del file


</td>


</tr>


<tr>


<td>

costruzione della Graphical User Interface (GUI)


</td>


<td>

ciò che è disponibile è di base e basato su copia / incolla di codice (vedere [PySide](PySide/it.md))


</td>


</tr>


<tr>


<td>

navigatore di classi


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

analizzatore di oggetti


</td>


<td>

N/A


</td>


</tr>


<tr>


<td>

diagramma della gerarchia delle classi


</td>


<td>

N/A


</td>


</tr>


</table>


</div>

Per la programmazione Python esistono molti strumenti per supportare le funzioni di cui sopra, ma purtroppo non si integrano con l\'ambiente di sviluppo di FreeCAD.


<div class="mw-translate-fuzzy">

Un elenco di IDE per Python si trova a [Integrated Development Environments for Python](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments)


</div>

## Editors


<div class="mw-translate-fuzzy">

## Editor

FreeCAD contiene incorporato un editor per Python, esso si avvia cliccando sul pulsante Modifica del menu Macro-\>Macros\... Se invece si desidera utilizzare un editor esterno più performante si può sceglire tra i numerosi editor Python disponibili per molte piattaforme e con diversi livelli di funzionalità. Utilizzando un editor esterno si ha il vantaggio di poter usare l\'area di visualizzazione di FreeCAD per l\'output (sia grafico che testuale nella console) mentre il codice sorgente viene visualizzato in un\'altra applicazione. Un elenco di editor per Python secondo la piattaforma è disponibile all\'indirizzo [Python Editors](https://wiki.python.org/moin/PythonEditors)


</div>

Nota: Per i Macintosh l\'editor di testo [TextWrangler](http://www.barebones.com/products/textwrangler/) funziona bene. Ha l\'evidenziazione del codice ed eccellenti funzioni di ricerca. Ci sono opzioni per eseguire i lavori in Python, ma ovviamente non funzionano con l\'ambiente FreeCAD.

### Macro Source Code Directories 


<div class="mw-translate-fuzzy">

### Directory del codice sorgente delle macro 

FreeCAD utilizza due directory, di default sono la stessa directory ma sono puntate da differenti punti richiamabili in FreeCAD:

-   FreeCAD.ConfigGet(\"UserAppData\")
-   FreeCAD.ParamGet(\'User parameter:BaseApp/Preferences/Macro\').GetString(\'MacroPath\')


</div>

\"UserAppData\" punta a una directory in cui le cose come i file di configurazione o altri file previsti per l\'utente possono essere conservati, ma non devono essere modificati dall\'utente.

\"MacroPath\" punta ad una directory in cui sono memorizzati i file Python che sono i file in cui sono archiviate le macro per FreeCAD. Per contrassegnare un file Python come un file di macro per FreeCAD, l\'estensione del file viene modificata da \".py\" a \".FCMacro\".

Di default queste due directory sono nella stessa posizione, ma questo non è indispensabile. Potrebbe essere conveniente spostare i file delle macro (\*.FCMacro) in una posizione diversa.

Modificare i file che si trovano in \"MacroPath\" è semplice, l\'editor di testo supporta questa funzione. Per facilitare l\'uso dei file macro di FreeCAD, si consiglia di mantenerli tutti nella directory puntata da \"MacroPath\".

Per modificare la directory di \"MacroPath\", utilizzare Strumenti -\> Modifica parametri, quindi selezionare Preferenze/Macro/MacroPath poi cliccare sul testo e modificarlo. In alternativa \"MacroPath\" può essere modificato con il codice:


```python
FreeCAD.ParamGet('User parameter:BaseApp/Preferences/Macro').SetString('MacroPath','/me/myself/and/I')
```

## Debugger


<div class="mw-translate-fuzzy">

## Debugger 


**'''Per FreeCAD è previsto un debugger e questi passi sono un'alternativa fino a quando esso non sarà disponibile. Vedere github.com/mumme74/FreeCAD/tree/editor_fixes'''**

Tipicamente i [Debugger](wikipedia_Debugger.md) forniscono due funzionalità principali (tra le altre):

-   i breakpoint (punti di sospensione) nel codice sorgente
-   l\'ispezione delle variabili


</div>

[Debuggers](https://en.wikipedia.org/wiki/Debugger) typically provide two main features (among others):

-   breakpoints in the source code
-   variable inspection

I punti di sospensione **Breakpoints** sono \"trappole\" che vengono inserite nel codice, se il percorso di esecuzione attraverso il codice incontra uno di questi punti di sospensione, l\'esecuzione viene fermata o sospesa. Notare che l\'esecuzione non viene interrotta, dato che quando un programma viene interrotto tutte le informazioni residenti in memoria, come le variabili, vanno perse. Mentre il programma è sospeso il contenuto delle variabili può essere ispezionato e talvolta alterato (dipende dalla capacità del debugger). Generalmente il codice sorgente non può essere cambiato, ma alcuni ambienti supportano anche questo. Quando si è pronti, si può riprendere l\'esecuzione del codice sorgente. Nel codice si possono inserire numerosi breakpoint e tramite questi punti si possono realizzare numerose sospensioni. Lo scopo del debugger è di fare in modo che l\'esecuzione con i breakpoint e le sospensioni sia funzionalmente identico all\'esecuzione senza breakpoint.

**L\'ispezione delle variabili** è disponibile durante la sospensione dell\'esecuzione causata da un breakpoint. In generale il contenuto delle variabili può essere visualizzato, e molti debugger supportano anche la modifica dei contenuti prima di riprende l\'esecuzione.

Per FreeCAD è previsto, ma non è ancora disponibile un debugger con tutte le funzionalità. Questa sezione descrive alcune soluzioni alternative per l\'interim, fino a quando il debugger non sarà rilasciato.

### Breakpoints


<div class="mw-translate-fuzzy">

### Breakpoint

Implementando i punti di interruzione si coinvolge un livello di supervisione del codice che gestisce l\'esecuzione del codice in fase di sviluppo. Al momento tale livello di codice per sviluppare Python all\'interno di FreeCAD non è disponibile. Come sostituto debole, il seguente codice è un\'opzione. Invece di sospendere l\'esecuzione del codice, ferma completamente l\'esecuzione dividendo un numero per zero. Questa è davvero una scelta molto debole rispetto ad un corretto debugger con i punti di interruzione, inoltre questa opzione è utile solo se è usata insieme alla routine mostrata nella prossima sezione \'Variable Inspection\'.


</div>

**Breakpoint Code** 
```python
def breakpoint(*args):
    # this routine will print an optional parameter on the console and then stop execution by diving by zero
    # e.g. breakpoint()
    # e.g. breakpoint("summation module")
    #
    if len(args)>0:
        FreeCAD.Console.PrintMessage('Breakpoint: '+str(args[0])+"\n")
    hereWeStop = 12/0
    
```

**Traceback nella Console**

Quando un programma fallisce durante l\'esecuzione, Python genera un testo noto come un traceback che elenca l\'ordine di esecuzione del programma (cioè quale programma ha chiamato quale programma, e in quale ordine).

Per il codice di esempio


```python
breakpoint('amalgamation routine')
```

otteniamo il seguente traceback


```python
Breakpoint: amalgamation routine
Traceback (most recent call last):
  File "/Users/wylbur/Library/Preferences/FreeCAD/testStub.FCMacro", line 40, in <module>
    breakpoint()
  File "/Users/wylbur/Library/Preferences/FreeCAD/myNewMacro.FCMacro", line 28, in breakpoint
    hereWeStop = 12/0
ZeroDivisionError: integer division or modulo by zero
```

Leggendo il traceback possiamo stabilire che:

-   un messaggio di \'Breakpoint: amalgamation routine\' è stato inviato dal breakpoint che ha la stringa \'amalgamation routine\'
-   l\'errore di esecuzione si è verificato alla riga 28 del modulo \'myNewMacro\'
-   la routine \'myNewMacro\' è stata chiamata dalla riga 40 del modulo \'testStub\'

Assumendo che la stringa passata alla chiamata del breakpoint sia significativa allora la posizione del breakpoint può essere determinata facilmente. Notare che in un sistema complesso all\'interno del traceback possono esserci decine o addirittura centinaia di voci.

Per diventare produttivi con questi punti di interruzione, continuare con la sezione successiva.

### Variable Inspection 


<div class="mw-translate-fuzzy">

### Variable Inspection 

La seconda caratteristica principale di un debugger è quella di esaminare ed eventualmente modificare il contenuto delle variabili. Ancora una volta, fino a quando il debugger FreeCAD per Python non sarà pronto dobbiamo dipendere da soluzioni alternative.


</div>


<div class="mw-translate-fuzzy">

Una caratteristica del sistema FreeCAD è la fornitura di variabili globali. Queste variabili sono create dal codice Python e risiedono nella memoria di FreeCAD fino a quando l\'utente esce da FreeCAD. La forma di queste variabili è:


</div>


```python
FreeCAD.myVariable = 123
```


<div class="mw-translate-fuzzy">

L\'istruzione crea una variabile Python nella memoria di FreeCAD che è completamente accessibile dal codice Python, di fatto si comporta esattamente come una normale variabile Python. Però, dopo che l\'esecuzione del codice Python termina, non importa se è eseguito come una macro o attraverso la console, la variabile \'FreeCAD.myVariable\' rimane nella memoria con il valore di 123. Inserire:


</div>


```python
>>> FreeCAD.myVariable
123
```

produce il contenuto della variabile sulla console. Questo valore rimane in FreeCAD fino a quando non viene modificato o l\'utente esce da FreeCAD. Ciò significa che il valore è presente e disponibile per essere letto da un successivo programma Python. Esso può essere controllato dalla console, in qualsiasi momento, digitando il suo nome. Quindi un programma chiamato \'Program A\':


```python
# program A
myListVariable = list()
myListVariable.append(123)
myListVariable.append('abc')
FreeCAD.myVariable = myListVariable
```

può essere eseguito e può caricare i valori nella variabile globale. Più tardi può essere eseguito un secondo programma chiamato \'Programma B\' che può recuperare i valori:


```python
myOtherVariable = FreeCAD.myVariable
# further calculations involving myOtherVariable
```

Presumibilmente il \'Programma B\' passa poi a fare calcoli che coinvolgono i valori lasciati in FreeCAD.myVariable. In qualsiasi momento l\'utente può digitare nella console per ispezionare il contenuto delle variabili:


```python
>>> FreeCAD.myVariable
[123, 'abc']
>>> 
```

Una cosa importante da tenere presente con le variabili globali di FreeCAD è che esistono nella memoria e vengono perse quando il programma viene chiuso. Esse non sono salvate con i documenti, ma esistono solo nella memoria.

### Usage


<div class="mw-translate-fuzzy">

### Uso

A questo punto possiamo mettere insieme le due fasi e usarle per rintracciare gli errori nel codice. Non è molto pratico da usare, ma è solo una alternativa finché il debugger di FreeCAD non sarà pronto.


</div>

Probabilmente è più facile presentando un esempio, vale a dire il seguente programma è in fase di debug:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

L\'esecuzione del programma produce nella console:


```python
>>> monthCounter()
10
```

che non è quello che ci aspettavamo! Supponendo non siamo in grado di vedere gli errori, possiamo usare il nostro pseudo breakpoint e l\'esaminatore variabile come segue. Possiamo inserire una riga per copiare il valore della variabile in una variabile globale, poi possiamo mettere un breakpoint per fermare l\'esecuzione in quel punto:


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 3
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable = temporaryVariable1 # <<<<<<<<<<< first inserted line
    breakpoint('is this assignment faulty?') # <<<<<<<<<<<<<< second inserted line
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Ora, quando si esegue il programma si ottiene:


```python
>>> monthCounter()
Breakpoint: is this assignment faulty?
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<input>", line 9, in monthCounter
  File "<input>", line 5, in breakpoint
ZeroDivisionError: integer division or modulo by zero
>>> 
```

Probabilmente le cose non appaiono molto bene, ma ora possiamo controllare il valore della variabile Python \'temporaryVariable1\' dato che abbiamo assegnato il suo valore alla variabile globale \'FreeCAD.saveMyVariable\':


```python
>>> FreeCAD.saveMyVariable
15
>>>
```

Ora, ricordando che la variabile \'FreeCAD.saveMyVariable\' contiene il valore della variabile Python \'temporaryVariable1\' possiamo determinare l\'errore nel valore e avviare tracingback per stabilire da dove arriva l\'errore. Quando controlliamo la variabile \'FreeCAD.saveMyVariable\' è importante rendersi conto che la variabile \'temporaryVariable1\' non è più disponibile - è stata rimossa dal sistema Python.

Quando l\'errore è stato localizzato nella istruzione


```python
numberOfSeasons = 3
```

e corretto con:


```python
numberOfSeasons = 4
```

Allora possiamo di nuovo eseguire il programma, e ottenere il valore \'11\', che non è ancora quello giusto. Possiamo fare più assegnazioni alle variabili globali di FreeCAD, avere più punti di interruzione (anche se l\'esecuzione si fermerà al primo breakpoint incontrato)


```python
def monthCounter():
    # program to calculate the number of months in the year
    signsInTheZodiac = 12
    numberOfSeasons = 4
    numberOfCompassPoints = 5
    #
    temporaryVariable1 = signsInTheZodiac + numberOfSeasons
    FreeCAD.saveMyVariable1 = temporaryVariable1
    #breakpoint('first assignment')
    numberOfMonths = temporaryVariable1 - numberOfCompassPoints
    FreeCAD.saveMyVariable2 = numberOfMonths
    breakpoint('second assignment')
    #
    FreeCAD.Console.PrintMessage(numberOfMonths)
```

Ora sono usati due punti di interruzione (anche se uno è commentato) e due variabili globali FreeCAD. Non vi è alcun limite pratico alle variabili globali disponibili da FreeCAD quindi non è necessario fare inutili economie. Ora nella console possiamo produrre quanto segue:


```python
>>> FreeCAD.saveMyVariable1
10
>>> FreeCAD.saveMyVariable2
11
>>> 
```

Alcuni punti circa l\'uso delle variabili globali FreeCAD:

-   Python considera queste variabili in modo identico a qualsiasi altra variabile Python
-   queste variabili possono contenere qualsiasi tipo di dato Python - qualsiasi cosa che possa essere contenuta da una normale variabile Python
-   queste variabili possono essere utilizzate per \'rendere pubblico\' il contenuto di una variabile Python in modo che si possa vederlo
-   queste variabili possono anche essere utilizzati per \'fornire\' i valori a una variabile Python impostando il loro valore dalla console prima di eseguire una routine, o impodolo in un programma Python precedente
-   queste variabili possono essere utilizzate per passare dei dati tra due programmi che vengono eseguiti in tempi diversi
-   (ripeto) queste variabili esistono solo per la durata della sessione di FreeCAD, quando si esce da FreeCAD le variabili sono perse

### Variable Watcher 


<div class="mw-translate-fuzzy">

### Variable Watcher 

La macro [Global Variable Watcher](Macro_Global_Variable_Watcher/it.md) aiuta a monitorare le variabili globali di FreeCAD. Si può visualizzare il contenuto di una variabile globale su richiesta o su base temporizzata.


</div>

### Name Space Clash 


<div class="mw-translate-fuzzy">

### Name Space Clash 

Una cosa da tenere presente è che non vi è la gestione di nomi delle variabili globali da parte di FreeCAD per cui è possibile cambiare una variabile o un altro pezzo di codice dal sistema. Di conseguenza, è una buona idea anteporre le variabili a qualcosa di unico come nome della routine. Ad esempio, per utilizzare una variabile da una routine chiamata \'alfa1\' il nome globale potrebbe essere \'FreeCAD.alpha1MyVariable\'.


</div>

## Coding Framework 


<div class="mw-translate-fuzzy">

## Coding Framework 

Se si sviluppano piccole parti di codice Python in FreeCAD può essere sufficiente utilizzare la console, ma quando il numero di righe del codice cresce è meglio memorizzarle in un file. Python può essere contenuto in qualsiasi file con l\'estensione \".py\", ma FreeCAD fornisce anche un meccanismo chiamato Macro per memorizzare tali programmi e interagire con loro (ad esempio modificarli, eseguirli). Python in file regolari \".py\" può essere eseguito solo dalla console mentre Python nel file \'.FCMacro\' può essere eseguito anche dall\'interfaccia per le macro di FreeCAD. Siccome l\'interfaccia del menu di FreeCAD è composta da un menu basato su una finestra di controllo ha lo svantaggio di provocare potenzialmente qualche disordine sullo schermo GUI.


</div>

Un approccio più semplice è quello di prendere il codice Python e invece di avviarlo dal menu Macro di FreeCAD, avviarlo da una barra degli strumenti. Una routine Python collegata ad un pulsante sulla barra degli strumenti può essere eseguita con un clic. Inoltre le barre degli strumenti sono finestre galleggianti che non ingombrano la visualizzazione sullo schermo. Infatti se la finestra di FreeCAD è inferiore alla dimensione fisica dello schermo la barra può essere lasciata fluttuare al di fuori della finestra di FreeCAD. Questo è utile quando sono richieste istantanee dello schermo di FreeCAD. Inoltre la barra degli strumenti può essere molto più piccola della finestra di controllo della macro visualizzata dal menu Macro di FreeCAD.


<div class="mw-translate-fuzzy">

Come collegare una macro a un pulsante sulla barra degli strumenti è descritto in [Come installare le Macro](How_to_install_macros/it.md) e [Come personalizzare la barra degli strumenti](Customize_Toolbars/it.md). Si può dedicare alcuni minuti per collegare una macro a un pulsante sulla barra degli strumenti, selezionare un\'icona ecc. Questo non è sempre necessario, dato che a volte si vuole semplicemente ampliare rapidamente un pezzo di codice che verrà poi integrato in qualche altro codice. Per questa situazione può essere utile uno stub test. Non esiste una vera e propria definizione di ciò che uno stub test implica, dipende dalla persona e dall\'ambito di applicazione. Un esempio è mostrato di seguito:


</div>


```python
#
#           TEST
#           TEST stub to clip any code onto...
#           TEST
#
################################
# routine to <description goes here>
"""
script does <long winded description goes here>
"""

# import statements
import FreeCAD
from FreeCAD import Base
import math, collections
from PySide import QtGui, QtCore

# UI Class definitions

# Class definitions

# Functions definitions

# Constant definitions

# code ***********************************************************************************

QtGui.QMessageBox.information(None,"","Test Stub")

##########################################################################################
##########################################################################################
##########################################################################################
```

Questo stub test serve anche come modello per il codice con le posizioni definite per i diversi aspetti di un grande programma Python. Quando viene eseguito il programma stub test genera semplicemente un messaggio che indica il suo nome e finisce. Utilizzando uno stub test, ogni riga principale del codice scritto viene collocata alla fine del file con il codice per la definizione della classe, le funzioni ecc situate nelle sezioni precedenti. Il modello può essere facilmente modificato per adattarlo alla situazione. Ovviamente per un programma di 5 righe vi è alcuna necessità di una tale mole di documentazione.


<div class="mw-translate-fuzzy">

Utilizzando un pulsante permanente su una barra e collegando tale pulsante al test stub, si dispone sempre di una zona in cui scrivere del codice ed eseguirlo immediatamente. L\'esecuzione sarà indipendente dalla console Python e può anche essere indipendente dallo schermo GUI. L\'output del programma in fase di sviluppo appare come dovrebbe sullo schermo senza interferenze da parte dell\'ambiente di programmazione. La console Python può essere nascosta per aumentare l\'area di visualizzazione oppure può essere usata per altri scopi, se necessario. Quando l\'esecuzione è affidata al pulsante sulla barra degli strumenti la console non è necessaria.


</div>


<div class="mw-translate-fuzzy">

Quando il codice è finito può essere semplicemente copiato/incollato in un altro file e il testo stub lasciato vuoto fino a quando non è nuovamente necessario.


</div>

Per sviluppare più pezzi di codice utilizzando lo stesso stub test, basta aggiungere il codice che fornisce più pulsanti e che è situato in [PySide Beginner Examples - Più di 2 pulsanti](PySide_Beginner_Examples/it#Più_di_2_pulsanti.md).

**Supporti aggiuntivi per PySide**

Per maggiori informazioni su PySide GUI c\'è la pagina [PySide](PySide/it.md)

**Supporti aggiuntivi per la programmazione Python**


<div class="mw-translate-fuzzy">

Per ulteriore assistenza con la codifica Python, esiste una macro scritta per facilitare lo sviluppo di codice Python, essa si trova in [Python Assistant Window](Macro_Python_Assistant_Window/it.md)


</div>

## Putting It All Together 


<div class="mw-translate-fuzzy">

## Mettere tutto insieme 

La gestione dello schermo può essere una sfida quando si sviluppa del codice che ha un output grafico complesso e dettagliato come fa FreeCAD. Il seguente sistema funziona bene:

-   FreeCAD per visualizzare console, report e GUI
-   barra degli strumenti per richiamare il codice in fase di sviluppo
-   editor esterno per modificare il codice
-   PAW (Python Assistant Window) per agevolare la generazione del codice Python


</div>

**Gestione dello schermo**

Con il test stub azionato da una barra degli strumenti, e utilizzando un editor esterno, l\'impaginazione della finestra nello schermo sarà qualcosa del tipo:

![](images/PythonDevelopmentEnvironment.jpg )

\"tree\" nel diagramma si riferisce alla vista combinata o struttura a albero, la console Python e la vista Report sono riuniti nella finestra inferiore e selezionabili tramite i pulsanti. Quanto sopra è solo un idea, e può essere ottimizzato per un uso selettivo degli strumenti del flusso di sviluppo. Questo modello è stato confezionato a titolo personale.

## Miscellaneous Links 


<div class="mw-translate-fuzzy">

## Link vari 

Alcuni altri link che riguardano le IDE per Python e che possono essere interessanti sono:

-   [Comparison of Python IDEs for Development](http://www.pythoncentral.io/comparison-of-python-ides-development/)
-   [Choosing the Best Python IDE](http://pedrokroger.net/choosing-best-python-ide/)
-   [Your Development Environment](http://docs.python-guide.org/en/latest/dev/env/)
-   [PyCharm Community Edition IDE](http://www.jetbrains.com/pycharm/)


</div>



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Python Code](Category_Python Code.md) > Python Development Environment/it
