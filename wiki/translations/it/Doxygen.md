# Doxygen/it
## Introduzione




Doxygen è uno strumento popolare per la generazione di documentazione da sorgenti C++ annotate; supporta anche altri linguaggi di programmazione popolari come C#, PHP, Java e Python. Visitare il [sito web Doxygen](http://www.doxygen.nl/) per saperne di più sul sistema e consultare il [Manuale Doxygen](http://www.doxygen.nl/manual/index.html) per informazioni complete.



## Doxygen e FreeCAD 

Questo documento fornisce una breve introduzione a Doxygen, in particolare a come viene utilizzato in FreeCAD per documentarne i sorgenti. Visitare la pagina [documentazione del codice sorgente](source_documentation/it.md) per istruzioni sulla creazione della documentazione di FreeCAD, anch\'essa ospitata online sul [sito web dell\'API di FreeCAD](https://www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per produrre documentazione del codice sorgente con Doxygen.*



## Doxygen col codice C++ 

La sezione [Getting started (Step 3)](http://www.doxygen.nl/manual/starting.html) del manuale Doxygen menziona i modi di base per documentare le fonti.

Per i membri, le classi e gli spazi dei nomi ci sono fondamentalmente due opzioni:

1.  Posizionare uno speciale \"blocco di documentazione\" (un paragrafo commentato) prima della dichiarazione o della definizione della funzione, membro, classe o spazio dei nomi. Per i membri di file, delle classi e dello spazio dei nomi (variabili) è anche consentito posizionare la documentazione direttamente dopo il membro. Vedere la sezione [Blocchi di commenti speciali](http://www.doxygen.nl/manual/docblocks.html#specialblock) nel manuale per saperne di più su questi blocchi.
2.  Posizionare un blocco di documentazione speciale da qualche altra parte (un altro file o un\'altra posizione nello stesso file) e inserire un \"comando strutturale\" nel blocco di documentazione. Un comando strutturale collega un blocco di documentazione a una determinata entità che può essere documentata (una funzione, un membro, una variabile, una classe, uno spazio dei nomi o un file). Vedere la sezione [Documentazione in altri luoghi](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) ​​nel manuale per saperne di più sui comandi strutturali.

Nota:

-   Il vantaggio della prima opzione è che non si deve ripetere il nome dell\'entità (funzione, membro, variabile, classe o spazio dei nomi), poiché Doxygen analizzerà il codice ed estrarrà le informazioni rilevanti.
-   I file possono essere documentati solo utilizzando la seconda opzione, poiché non è possibile inserire un blocco di documentazione prima di un file. Naturalmente, i membri del file (funzioni, variabili, typedef, define) non necessitano di un comando strutturale esplicito; semplicemente mettendo un blocco di documentazione prima o dopo di questi tutto funzionerà correttamente.



### Primo stile: blocco della documentazione prima del codice 

Di solito si desidera documentare il codice nel file di intestazione, appena prima della dichiarazione di classe o del prototipo di funzione. Ciò mantiene la dichiarazione e la documentazione vicine l\'una all\'altra, quindi è facile aggiornare quest\'ultima se la prima cambia.

Il blocco di documentazione speciale inizia come un commento in stile C `/*` ma ha un asterisco aggiuntivo, quindi `/**`; il blocco termina con un `*/` corrispondente. Un\'alternativa è utilizzare i commenti in stile C++ `//` con una barra aggiuntiva, quindi `///`. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



### Secondo stile: blocco della documentazione altrove 

In alternativa, la documentazione può essere collocata in un altro file (o nello stesso file in alto o in basso, o dovunque), lontano dalla dichiarazione di classe o dal prototipo di funzione. In questo caso, avrai informazioni duplicate, una volta nel file di origine effettivo e una volta nel file di documentazione.

Primo file, `source.h`: 
```python
std::string name() const;
void setName(const std::string&);
```

Secondo file, `source.h.dox`: 
```python
/** \file source.h
 *  \brief The documentation of source.h
 *   
 *   The details of this file go here.
 */

/** \fn std::string name() const;
 *  \brief Returns the name of the workbench object.
 */
/** \fn void setName(const std::string&);
 *  \brief Set the name to the workbench object.
 */
```

In questo caso viene usato il comando strutturale `\file` per indicare quale file sorgente si sta documentando; un comando strutturale `\fn` indica che il seguente codice è una funzione, e il comando `\brief` è usato per dare una breve descrizione di questa funzione.

Questo modalità di documentare un file sorgente è utile se vuoi solo aggiungere documentazione al tuo progetto senza aggiungere codice reale. Quando si inserisce un blocco di commento in un file con una delle seguenti estensioni `.dox`, `.txt` o `.doc`, Doxygen analizzerà i commenti e creerà la documentazione appropriata, ma nasconderà questo file ausiliario dall\'elenco dei file.

Il progetto FreeCAD contiene diversi file che terminano con `.dox` in molte cartelle per fornire una descrizione, o esempi, del codice presente. È importante che tali file siano correttamente categorizzati in un gruppo o in uno spazio dei nomi, per il quale Doxygen fornisce alcuni comandi ausiliari come `\defgroup`, `\ingroup` e `\namespace` .


<div class="mw-collapsible mw-collapsed toccolours">

Esempio `src/Base/core-base.dox`; questo file nell\'albero dei sorgenti di FreeCAD fornisce una breve spiegazione dello spazio dei nomi `Base`.


<div class="mw-collapsible-content">


```python
/** \defgroup BASE Base
 *  \ingroup CORE
    \brief Basic structures used by other FreeCAD componentsThe Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units

*/

/*! \namespace Base
    \ingroup BASE
    \brief Basic structures used by other FreeCAD components

    The Base module includes most of the basic functions of FreeCAD, such as:
    - Console services: printing different kinds of messages to the FreeCAD report view or the terminal
    - Python interpreter: handles the execution of Python code in FreeCAD
    - Parameter handling: Management, saving and restoring of user preferences settings
    - Units: Management and conversion of different units
*/
```


</div>


</div>

Un altro esempio è il file `src/Gui/Command.cpp`. Prima dei dettagli di implementazione dei metodi `Gui::Command`, c\'è un blocco di documentazione che spiega alcuni dettagli del framework di comando di FreeCAD. Ha vari comandi `\section` per strutturare la documentazione. Include anche codice di esempio racchiuso in una coppia di parole chiave `\code` e `\endcode`; quando il file viene elaborato da Doxygen, questo esempio di codice verrà appositamente formattato per distinguersi. La parola chiave `\ref` viene utilizzata in diversi punti per creare collegamenti a sezioni, sottosezioni, pagine o ancore denominate altrove nella documentazione. Allo stesso modo, i comandi `\see` o `\sa` stampano \"Vedi anche\" e forniscono un collegamento ad altre classi, funzioni, metodi, variabili, file o URL.


<div class="mw-collapsible mw-collapsed toccolours">

Esempio `src/Gui/Command.cpp`


<div class="mw-collapsible-content">


```python
/** \defgroup commands Command Framework
    \ingroup GUI
    \brief Structure for registering commands to the FreeCAD system
 * \section Overview
 * In GUI applications many commands can be invoked via a menu item, a toolbar button or an accelerator key. The answer of Qt to master this
 * challenge is the class \a QAction. A QAction object can be added to a popup menu or a toolbar and keep the state of the menu item and
 * the toolbar button synchronized.
 *
 * For example, if the user clicks the menu item of a toggle action then the toolbar button gets also pressed
 * and vice versa. For more details refer to your Qt documentation.
 *
 * \section Drawbacks
 * Since QAction inherits QObject and emits the \a triggered() signal or \a toggled() signal for toggle actions it is very convenient to connect
 * these signals e.g. with slots of your MainWindow class. But this means that for every action an appropriate slot of MainWindow is necessary
 * and leads to an inflated MainWindow class. Furthermore, it's simply impossible to provide plugins that may also need special slots -- without
 * changing the MainWindow class.
 *
 * \section wayout Way out
 * To solve these problems we have introduced the command framework to decouple QAction and MainWindow. The base classes of the framework are
 * \a Gui::CommandBase and \a Gui::Action that represent the link between Qt's QAction world and the FreeCAD's command world. 
 *
 * The Action class holds a pointer to QAction and CommandBase and acts as a mediator and -- to save memory -- that gets created 
 * (@ref Gui::CommandBase::createAction()) not before it is added (@ref Gui::Command::addTo()) to a menu or toolbar.
 *
 * Now, the implementation of the slots of MainWindow can be done in the method \a activated() of subclasses of Command instead.
 *
 * For example, the implementation of the "Open file" command can be done as follows.
 * \code
 * class OpenCommand : public Command
 * {
 * public:
 *   OpenCommand() : Command("Std_Open")
 *   {
 *     // set up menu text, status tip, ...
 *     sMenuText     = "&Open";
 *     sToolTipText  = "Open a file";
 *     sWhatsThis    = "Open a file";
 *     sStatusTip    = "Open a file";
 *     sPixmap       = "Open"; // name of a registered pixmap
 *     sAccel        = "Shift+P"; // or "P" or "P, L" or "Ctrl+X, Ctrl+C" for a sequence
 *   }
 * protected:
 *   void activated(int)
 *   {
 *     QString filter ... // make a filter of all supported file formats
 *     QStringList FileList = QFileDialog::getOpenFileNames( filter,QString::null, getMainWindow() );
 *     for ( QStringList::Iterator it = FileList.begin(); it != FileList.end(); ++it ) {
 *       getGuiApplication()->open((*it).latin1());
 *     }
 *   }
 * };
 * \endcode
 * An instance of \a OpenCommand must be created and added to the \ref Gui::CommandManager to make the class known to FreeCAD.
 * To see how menus and toolbars can be built go to the @ref workbench.
 *
 * @see Gui::Command, Gui::CommandManager
 */
```


</div>


</div>



### Esempio dal progetto VTK 

Questo è un esempio da [VTK](https://vtk.org/), una libreria di visualizzazione 3D utilizzata per presentare dati scientifici, come risultati di elementi finiti e informazioni come nuvola di punti.

Una classe per archiviare una raccolta di coordinate è definita in un file di intestazione C++. La parte superiore del file è commentata e vengono utilizzate alcune parole chiave, come `@class`, `@brief` e `@sa` per indicare parti importanti. All\'interno della classe, prima dei prototipi del metodo della classe, un blocco di testo commentato spiega cosa fa la funzione ei suoi argomenti.

-   Codice sorgente di [vtkArrayCoordinates.h](https://github.com/Kitware/VTK/blob/master/Common/Core/vtkArrayCoordinates.h).
-   Doxygen ha prodotto la documentazione per la [classe vtkArrayCoordinates](http://www.vtk.org/doc/nightly/html/classvtkArrayCoordinates.html).



## Compilazione della documentazione 

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per produrre la documentazione del codice sorgente con Doxygen.*

Per generare la documentazione del codice sorgente ci sono due passaggi fondamentali:

1.  Creare un file di configurazione per controllare come Doxygen elaborerà i file sorgente.
2.  Eseguire `doxygen` su quella configurazione.


<div class="mw-collapsible mw-collapsed toccolours">

Il processo è descritto di seguito.


<div class="mw-collapsible-content">

-   Assicurarsi di avere i programmi `doxygen` e `doxywizard` nel proprio sistema. Si consiglia inoltre di avere il programma `dot` da [Graphviz](https://www.graphviz.org/), per generare diagrammi con le relazioni tra classi e spazi dei nomi. Sui sistemi Linux questi programmi possono essere installati dal tuo gestore di pacchetti.


```python
sudo apt install doxygen doxygen-gui graphviz
```

-   Assicurarsi di essere nella stessa cartella dei tuoi file di origine, o nella directory di livello superiore del tuo albero di origine, se si hanno molti file di origine in diverse sotto cartelle.


```python
cd toplevel-source
```

-   Eseguire `doxygen -g DoxyDoc.cfg` per creare un file di configurazione chiamato `DoxyDoc.cfg`. Se si omette questo nome, il valore predefinito sarà `Doxyfile` senza estensione.
-   Questo è un grande file di testo semplice che include molte variabili con i loro valori. Nel manuale Doxygen queste variabili sono chiamate \"tag\". Il file di configurazione e tutti i tag sono ampiamente descritti nella sezione [Configurazione](http://www.doxygen.nl/manual/config.html) del manuale. È possibile aprire il file con qualsiasi editor di testo e modificare il valore di ogni tag secondo necessità. Nello stesso file puoi leggere i commenti che spiegano ciascuno dei tag e i loro valori predefiniti.


```python
DOXYFILE_ENCODING      = UTF-8
PROJECT_NAME           = "My Project"
PROJECT_NUMBER         =
PROJECT_BRIEF          =
PROJECT_LOGO           =
OUTPUT_DIRECTORY       =
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = NO
BRIEF_MEMBER_DESC      = YES
REPEAT_BRIEF           = YES
...
```

-   Invece di utilizzare un editor di testo, si può avviare `doxywizard` per modificare più tag contemporaneamente. Con questa interfaccia è possibile definire molte proprietà come informazioni sul progetto, tipo di output (HTML e LaTeX), utilizzo di Graphviz per creare diagrammi, messaggi di avviso da visualizzare, modelli di file (estensioni) da documentare o escludere, filtri di input, intestazioni opzionali e piè di pagina per le pagine generate in HTML, opzioni per output LaTeX, RTF, XML o Docbook e molte altre opzioni.


```python
doxywizard DoxyDoc.cfg
```

-   Un\'altra opzione è creare il file di configurazione da zero e aggiungere solo i tag desiderati con un editor di testo.
-   Dopo aver salvato la configurazione, si può eseguire Doxygen su questo file di configurazione.


```python
doxygen DoxyDoc.cfg
```

-   La documentazione generata verrà creata all\'interno di una cartella denominata `toplevel-source/html`. Consisterà in molte pagine HTML, immagini PNG per la grafica, fogli di stile a cascata (`.css`), file Javascript (`.js`) e potenzialmente molte sotto cartelle con più file a seconda sulla dimensione del codice. Il punto di accesso alla documentazione è `index.html`, che si può aprire con un browser web.


```python
xdg-open toplevel-source/html/index.html
```


</div>


</div>

Se si stanno scrivendo nuove classi, funzioni o un intero nuovo workbench, si consiglia di eseguire periodicamente `doxygen` per verificare che la documentazione blocchi [Markdown](#Markdown_support.md) e [special commands](#Doxygen_markup.md) vengano letti correttamente e che tutte le funzioni pubbliche siano completamente documentate. Si prega di leggere anche i [suggerimenti per la documentazione](https://github.com/FreeCAD/FreeCAD/blob/master/src/Doc/doctips.dox) che si trovano nel codice sorgente.

Quando si genera la documentazione completa di FreeCAD, non si esegue `doxygen` direttamente. Invece, il progetto utilizza `cmake` per configurare l\'ambiente di compilazione, quindi `make` avvia la compilazione dei sorgenti di FreeCAD e della documentazione di Doxygen; questo è spiegato nella pagina [documentazione sorgente](source_documentation/it.md).



## markup di Doxygen 

Tutti i [comandi di documentazione](http://www.doxygen.nl/manual/commands.html) di Doxygen iniziano con una barra rovesciata `\` o un simbolo at `@`, a scelta. Normalmente si usa la barra rovesciata `\`, ma occasionalmente si usa `@` per migliorare la leggibilità.

I comandi possono avere uno o più argomenti. Nel manuale Doxygen gli argomenti sono descritti come segue.

-   Se vengono utilizzate parentesi con segno minore e maggiore `<sharp>` l\'argomento è una singola parola.
-   Se vengono utilizzate parentesi tonde `(round)` l\'argomento si estende fino alla fine della riga in cui è stato trovato il comando.
-   Se vengono utilizzate le parentesi graffe {curly} l\'argomento si estende fino al paragrafo successivo. I paragrafi sono delimitati da una riga vuota o da un indicatore di sezione.
-   Se si usano le parentesi quadre `[square]` l\'argomento è facoltativo.


<div class="mw-collapsible mw-collapsed toccolours">

Alcune delle parole chiave più comuni utilizzate nella documentazione di FreeCAD sono presentate qui.


<div class="mw-collapsible-content">

-    (group title), vedere [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   ]), vedere [\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-    [(title)], vedere [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), e [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, vedere [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); indica l\'autore di questo pezzo di codice.
-   \brief { brief description }, vedere [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); descrive brevemente la funzione.
-   ], vedere [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); documenta un file di origine o di intestazione.
-    (title), see [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); inserisce le informazioni in una pagina separata, non direttamente correlata a una specifica classe, file o membro.
-   , vedere [\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); indica la documentazione per un pacchetto Java (ma è utilizzato anche con Python).
-   \fn (function declaration), vedere [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); documenta una funzione.
-   \var (variable declaration), vedere [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); documenta una variabile; è equivalente a `\fn`, `\property`, e `\typedef`.
-    (section title), vedere [\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); inizia una sessione.
-    (subsection title), vedere [\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); inizia una sottosessione.
-   , vedere [\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); indica le informazioni per uno spazio dei nomi.
-   \cond [(section-label)], e \endcond, vedere [\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); definisce un blocco da documentare o omettere in modo condizionale.
-   , vedere [\\a](http://www.doxygen.nl/manual/commands.html#cmda); visualizza l\'argomento in corsivo per dare enfasi.
-    { parameter description }, vedere [\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); indica il parametro di una funzione.
-   \return { description of the return value }, vedere [\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); specifica il valore restituito.
-   \sa { references }, vedere [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); stampa \"See also\".
-   \note { text }, vedere [\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); aggiunge un paragrafo da utilizzare come nota.


</div>


</div>



## Supporto al Markdown 

A partire da Doxygen 1.8, la sintassi Markdown è riconosciuta dai blocchi di documentazione. Markdown è un linguaggio di formattazione minimalista ispirato all\'e-mail di testo semplice che, simile alla sintassi wiki, intende essere semplice e leggibile senza richiedere codice complicato come quello che si trova in HTML, LaTeX o i comandi di Doxygen. Markdown ha guadagnato popolarità con il software libero, specialmente nelle piattaforme online come Github, in quanto consente di creare documentazione senza utilizzare codice complicato. Consultare la sezione [Markdown support](http://www.doxygen.nl/manual/markdown.html) nel manuale Doxygen per saperne di più. Visitare il [sito web di Markdown](https://daringfireball.net/projects/markdown/) per saperne di più sull\'origine e la filosofia di Markdown.

Doxygen supporta un set standard di istruzioni Markdown, nonché alcune estensioni come [Github Markdown](https://github.github.com/github-flavored-markdown/).


<div class="mw-collapsible mw-collapsed toccolours">

Di seguito vengono presentati alcuni esempi di formattazione Markdown.


<div class="mw-collapsible-content">

Quello che segue è Markdown standard. 
```python
Ecco il testo per un paragrafo.

Continuiamo con altro testo in un altro paragrafo.

Questa è un'intestazione di livello 1
========================

Questa è un'intestazione di livello 2


# Questa è un'intestazione di livello 1

### Questa è l'intestazione di livello 3 #######

> Questa è un blocco di citazione
> su più righe

- Articolo 1

  Altro testo per questo articolo.

- Punto 2
  * voce di elenco nidificata.
  * un altro elemento nidificato.
- Punto 3

1. Primo elemento.
2. Secondo elemento.

*asterisco singolo: enfasi*

 _sottolineature singole_

 **doppio asterisco: enfasi forte**

 __sottolineature doppie__

Questo è un paragrafo normale

    Questo è un blocco di codice

Continuiamo di nuovo con un paragrafo normale.

Usa la funzione printf(). codice inline.

[Il testo del link](http://example.net/)

![Testo della didascalia](images//path/to/img.jpg)

<http://www.example.com>
```

Le seguenti sono estensioni di Markdown.

    [TOC]

    Prima intestazione    | Seconda intestazione
    | 
    Contenuto della Cella | Contenuto della Cella
    Contenuto della Cella | Contenuto della Cella 

    <nowiki>~~~~~~~~~~~~~</nowiki>{.py}
    # A class
    class Dummy:
        pass
    <nowiki>~~~~~~~~~~~~~</nowiki>

    <nowiki>~~~~~~~~~~~~~</nowiki>{.c}
    int func(int a, int b) { return a*b; }
    <nowiki>~~~~~~~~~~~~~</nowiki>
int func(int a, int b) { return a*b; }
    


</div>


</div>



## Analisi dei blocchi della documentazione 

Il testo all\'interno di uno speciale blocco di documentazione viene analizzato prima di essere scritto nei file di output HTML e LaTeX. Durante l\'analisi si verificano i seguenti passaggi:

-   La formattazione Markdown è sostituita dall\'HTML corrispondente o da comandi speciali.
-   Vengono eseguiti i comandi speciali all\'interno della documentazione. Vedere la sezione [Comandi speciali](http://www.doxygen.nl/manual/commands.html) nel manuale per una spiegazione di ciascun comando.
-   Se una riga inizia con degli spazi bianchi seguiti da uno o più asterischi (`*`) e poi facoltativamente altri spazi bianchi, tutti gli spazi bianchi e gli asterischi vengono rimossi.
-   Tutte le righe vuote risultanti vengono trattate come separatori di paragrafo.
-   I collegamenti vengono creati automaticamente per le parole corrispondenti a classi o funzioni documentate. Se la parola è preceduta da un simbolo di percentuale `%`, questo simbolo viene rimosso e non viene creato alcun collegamento per la parola.
-   I collegamenti vengono creati quando nel testo vengono trovati determinati schemi. Vedere la sezione [Generazione automatica di link](http://www.doxygen.nl/manual/autolink.html) nel manuale per ulteriori informazioni.
-   I tag HTML presenti nella documentazione vengono interpretati e convertiti in equivalenti LaTeX per l\'output LaTeX. Vedere la sezione [Comandi HTML](http://www.doxygen.nl/manual/htmlcmds.html) nel manuale per una spiegazione di ciascun tag HTML supportato.



## Doxygen con codice Python 

Doxygen funziona meglio per linguaggi tipizzati staticamente come C++. Tuttavia, può anche creare [documentazione per i file Python](http://www.doxygen.nl/manual/docblocks.html#pythonblocks).

Esistono due modi per scrivere blocchi di documentazione per Python:

1.  Il modo Pythonico, usando \"docstrings\", cioè un blocco di testo racchiuso tra '''virgolette triple''' subito dopo la definizione della classe o della funzione.
2.  Il modo Doxygen, inserendo i commenti prima della definizione della classe o della funzione; in questo caso vengono utilizzati i doppi caratteri hash `##` per iniziare il blocco di documentazione, e quindi un singolo carattere hash può essere utilizzato nelle righe successive.

Nota:

-   La prima opzione è preferita per rispettare [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings), [pep-0257/ PEP257](https://www.python.org/dev/peps/) e la maggior parte delle linee guida di stile per la scrittura di Python (vedere [1](https://realpython.com/python-pep8/), [2](https://realpython.com/documenting-python-code/)). Si consiglia di utilizzare questo stile se si intende produrre fonti documentate utilizzando [Sphinx](https://www.sphinx-doc.org/en/master/), che è uno strumento molto comune per documentare il codice Python. Se usi questo stile, Doxygen sarà in grado di estrarre i commenti alla lettera, ma i comandi speciali di Doxygen che iniziano con `\` o `@` non funzioneranno.
-   La seconda opzione non è il tradizionale stile Python, ma ti permette di usare i comandi speciali di Doxygen come `\param` e `\var`.



### Primo stile: documentazione Pythonica 

Nell\'esempio seguente una docstring è all\'inizio per spiegare i contenuti generali di questo modulo (file). Quindi le docstring appaiono all\'interno delle definizioni di funzione, classe e metodo di classe. In questo modo Doxygen estrarrà i commenti e li presenterà così come sono, senza modifiche.


```python
'''@package pyexample_a
Documentazione per questo modulo.
Maggiori dettagli.
'''


def func():
    '''Documentazione per una funzione.
    Maggiori dettagli.
    '''
    pass


class PyClass:
    '''Documentazione per una classe.
    Maggiori dettagli.
    '''

    def __init__(self):
        '''Il costruttore.'''
        self._memVar = 0

    def PyMethod(self):
        '''Documentazione per un metodo.'''
        pass
```



### Secondo stile: blocco di documentazione prima del codice 

Nell\'esempio seguente i blocchi di documentazione iniziano con doppi cancelletti `##`. Uno appare all\'inizio per spiegare il contenuto generale di questo modulo (file). Quindi ci sono blocchi prima delle definizioni di funzione, classe e metodo di classe e c\'è un blocco dopo una variabile di classe. In questo modo, Doxygen estrarrà la documentazione, riconoscerà i comandi speciali `@package`, `@param` e `@var` e formatterà il testo di conseguenza. 
```python
## @package pyexample_b
#  Documentation for this module.
#
#  More details.


## Documentation for a function.
#
#  More details.
def func():
    pass


## Documentation for a class.
#
#  More details.
class PyClass:

    ## The constructor.
    def __init__(self):
        self._memVar = 0

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self):
        pass

    ## A class variable.
    classVar = 0
    ## @var _memVar
    #  a member variable
```



### Compilazione della documentazione 

La compilazione della documentazione procede come [per i sorgenti C++](#Compilazione_della_documentazione.md). Se entrambi i file Python, `pyexample_a.py` e `pyexample_b.py`, con uno stile di commento distinto si trovano nella stessa directory, verranno elaborati entrambi. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

La documentazione dovrebbe mostrare informazioni simili alle seguenti e creare collegamenti appropriati ai singoli moduli e classi. 
```python
Class List
Here are the classes, structs, unions and interfaces with brief descriptions:

N  pyexample_a
   C  PyClass

N  pyexample_b  Documentation for this module
   C  PyClass   Documentation for a class
```



### Conversione dello stile Pythonico in stile Doxygen 

Nell\'esempio precedente, il file Python commentato in un [stile Doxygen](#Secondo_stile__blocco_della_documentazione_altrove.md) mostra informazioni e formattazione più dettagliate per le sue classi, funzioni e variabili. Il motivo è che questo stile consente a Doxygen di estrarre i comandi speciali che iniziano con `\` o `@`, mentre lo [stle Pythonico](#Primo_stile__blocco_della_documentazione_prima_del_codice.md) no. Pertanto, sarebbe desiderabile convertire lo stile Pythonico in stile Doxygen prima di compilare la documentazione. Questo è possibile con un programma Python ausiliario chiamato [doxypypy](https://github.com/Feneric/doxypypy). Questo programma è ispirato a un vecchio programma chiamato [doxypy](https://github.com/Feneric/doxypy), che prende le '''docstrings''' di Python e le converte nei blocchi di commenti Doxygen che iniziano con un doppio hash `##`. Doxypypy va oltre, poiché analizza le docstring ed estrae elementi di interesse come variabili e argomenti e persino doctest (codice di esempio nelle docstring).

Doxypypy può essere installato usando `pip`, il programma di installazione dei pacchetti Python. 
```python
pip3 install --user doxypypy
```

Se il comando `pip` viene utilizzato senza l\'opzione `--user`, saranno necessari i privilegi di superutente (root) per installare il pacchetto, ma ciò non è necessario nella maggior parte dei casi; usare i permessi di root solo se sei certo che il pacchetto non entrerà in collisione con i pacchetti forniti dalla tua distribuzione.

Se il pacchetto è stato installato come utente, potrebbe risiedere nella tua home directory, ad esempio in `$HOME/.local/bin`. Se questa directory non è nel `PATH` del tuo sistema, il programma non verrà trovato. Pertanto, aggiungere la directory alla variabile `PATH`, nel file `$HOME/.bashrc` o nel file `$HOME/.profile`. 
```python
export PATH="$HOME/.local/bin:$PATH"
```

In alternativa, si può creare un collegamento simbolico al programma `doxypypy`, posizionando il collegamento in una directory che è già inclusa nel `PATH`. 
```python
mkdir -p $HOME/bin
ln -s $HOME/.local/bin/doxypypy $HOME/bin/doxypypy
```

Una volta che il programma `doxypypy` è installato e accessibile dal terminale, un file Python con docstring Pythonic può essere riformattato in stile Doxygen con le seguenti istruzioni. Il programma invia il codice riformattato allo standard output, quindi reindirizza questo output a un nuovo file. 
```python
doxypypy -a -c pyexample_pythonic.py > pyexample_doxygen.py
```


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_pythonic.py`


<div class="mw-collapsible-content">


```python
'''@package pyexample_pythonic
Documentation for this module.
More details go here.
'''


def myfunction(arg1, arg2, kwarg='whatever.'):
    '''
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError, AssertionError, & ValueError.

    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    '''
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`


<div class="mw-collapsible-content">


```python
##@package pyexample_pythonic
#Documentation for this module.
#More details go here.
#


## @brief     Does nothing more than demonstrate syntax.
#
#    This is an example of how a Pythonic human-readable docstring can
#    get parsed by doxypypy and marked up with Doxygen commands as a
#    regular input filter to Doxygen.
#
#
# @param        arg1    A positional argument.
# @param        arg2    Another positional argument.
#
#
# @param        kwarg   A keyword argument.
#
# @return
#        A string holding the result.
#
#
# @exception        ZeroDivisionError
# @exception        AssertionError
# @exception        ValueError.
#
# @b Examples
# @code
#        >>> myfunction(2, 3)
#        '5 - 0, whatever.'
#        >>> myfunction(5, 0, 'oops.')
#        Traceback (most recent call last):
#            ...
#        ZeroDivisionError: integer division or modulo by zero
#        >>> myfunction(4, 1, 'got it.')
#        '5 - 4, got it.'
#        >>> myfunction(23.5, 23, 'oh well.')
#        Traceback (most recent call last):
#            ...
#        AssertionError
#        >>> myfunction(5, 50, 'too big.')
#        Traceback (most recent call last):
#            ...
#        ValueError
# @endcode
#

def myfunction(arg1, arg2, kwarg='whatever.'):
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)
```


</div>


</div>

Il file originale ha un commento in alto '''@package pyexample_pythonic che indica il modulo o lo spazio dei nomi che viene descritto dal file. Questa parola chiave `@package` non viene interpretata quando si utilizzano le virgolette triple nel blocco dei commenti.

Nel nuovo file lo stile di commento è cambiato in modo che la riga diventi `##@package pyexample_pythonic`, che ora sarà interpretata da Doxygen. Tuttavia, per essere interpretato correttamente, l\'argomento deve essere modificato manualmente in modo che corrisponda al nome del nuovo modulo (file); dopo aver fatto questo la riga dovrebbe essere `##@package pyexample_doxygen`.

div class=\"mw-collapsible mw-collapsed toccolours\"\> `pyexample_doxygen.py` (la parte superiore viene modificata manualmente, il resto rimane invariato)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

Per compilare, creare la configurazione ed eseguire `doxygen` nella directory di livello superiore che contiene i file. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

La documentazione dovrebbe mostrare informazioni simili alle seguenti e creare collegamenti appropriati ai singoli moduli. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```



### Conversione immediata dello stile del commento 

Nell\'esempio precedente, la conversione dei blocchi di documentazione è stata eseguita manualmente con un solo file sorgente. Idealmente si desidera che questa conversione avvenga automaticamente, al volo, con qualsiasi numero di file Python. Per fare ciò, la configurazione Doxygen deve essere modificata di conseguenza.

Per iniziare, non utilizzare direttamente il programma `doxypypy`; invece, creare il file di configurazione con `doxygen -g`, quindi modificare il `Doxyfile` creato e modificare il seguente tag. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

Quello che fa è che i file che corrispondono al modello, tutti i file con un\'estensione che termina con `.py`, passeranno attraverso il programma `doxypypy_filter`. Ogni volta che Doxygen incontra tale file nell\'albero dei sorgenti, il nome del file verrà passato come primo argomento a questo programma. 
```python
doxypypy_filter example.py
```

Il programma `doxypypy_filter` non esiste di default; dovrebbe essere creato come uno script di shell per eseguire `doxypypy` con le opzioni appropriate e per prendere un file come primo argomento. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

Dopo aver salvato questo script di shell, assicurarsi che abbia i permessi di esecuzione e che si trovi in una directory contenuta nel `PATH` del tuo sistema. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

Sui sistemi Windows, un file batch può essere utilizzato in modo simile. 
```python
doxypypy -a -c %1
```

Con questa configurazione impostata, il comando `doxygen Doxyfile` può essere eseguito per generare la documentazione come di consueto. Per ogni file Python che usa '''virgolette triple''' Pythonic sarà riformattato al volo per usare i commenti in stile `##Doxygen`, e poi questi saranno elaborati da Doxygen, che quindi sarà in grado di interpretare i [comandi speciali](#markup_di_Doxygen.md) e la [sintassi markdown](#Supporto_al_Markdown.md). Il codice sorgente originale non verrà modificato e non è necessario creare alcun file temporaneo con un nome diverso come [nella sezione precedente](#Conversione_dello_stile_Pythonico_in_stile_Doxygen.md); pertanto, se viene trovata un\'istruzione `@package example`, non è necessario modificarla manualmente.

Nota che i file Python esistenti che usano già lo stile `##doppio cancelletto` per i loro blocchi di commenti non saranno influenzati dal filtro `doxypypy` e saranno processati normalmente da Doxygen.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per produrre la documentazione del codice sorgente con Doxygen, quando i file Python vengono filtrati per trasformare i blocchi dei commenti.*



### Controllo della qualità del codice Python 

Per utilizzare la conversione automatica dei blocchi di documentazione è importante che i sorgenti Python originali siano scritti correttamente, seguendo le linee guida Pythonic in [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings) e [PEP257](https://www.python.org/dev/peps/pep-0257/). Un codice scritto in modo approssimativo causerà il fallimento di `doxypypy` durante l\'elaborazione del file, e quindi Doxygen non sarà in grado di formattare correttamente la documentazione.


<div class="mw-collapsible mw-collapsed toccolours">

I seguenti stili di commento non consentiranno l\'analisi delle docstring da parte di `doxypypy`, quindi dovrebbero essere evitati.


<div class="mw-collapsible-content">


```python
'''@package Bad
'''

def first_f(one, two):

    "Bad comment 1"

    result = one + two
    result_m = one * two
    return result, result_m

def second_f(one, two):
    "Bad comment 2"
    result = one + two
    result_m = one * two
    return result, result_m

def third_f(one, two):
    'Bad comment 3'
    result = one + two
    result_m = one * two
    return result, result_m

def fourth_f(one, two):
    #Bad comment 4
    result = one + two
    result_m = one * two
    return result, result_m
```


</div>


</div>

Usa sempre le virgolette triple per le docstring e assicurati che seguano immediatamente la dichiarazione della classe o della funzione.

È anche una buona idea verificare la qualità del tuo codice Python con uno strumento come [flake8](http://flake8.pycqa.org/en/latest/) ([Gitlab](https://gitlab.com/pycqa/flake8)). Flake8 combina principalmente tre strumenti, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle) (precedentemente pep8) e [/PyCQA/mccabe Controllo della complessità di McCabe](https://github.com), al fine di applicare il corretto stile Pythonic.


```python
pip install --user flake8
flake8 example.py
```

Per controllare tutti i file all\'interno di un albero dei sorgenti usa `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

Se il progetto lo richiede, alcuni controlli del codice ritenuti troppo severi possono essere ignorati. I codici di errore possono essere consultati nella [Documentazione di Pycodestyle](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

In modo simile, un programma che controlla principalmente che i commenti siano conformi a [PEP257](https://www.python.org/dev/peps/pep-0257/) è [Pydocstyle](https://github.com/PyCQA/pydocstyle). I codici di errore possono essere consultati nella [documentazione di Pydocstyle](http://www.pydocstyle.org/en/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Usalo anche con `find` per eseguire controlli docstring su tutti i file sorgente. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```



## Documentazione del sorgente con Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/) è il sistema più popolare per documentare il codice sorgente Python. Tuttavia, poiché le funzioni principali e gli ambienti di lavoro di FreeCAD sono scritti in C++, si è ritenuto che Doxygen fosse uno strumento di documentazione migliore per questo progetto.

Mentre Sphinx può analizzare in modo nativo le docstring Python, analizzare i sorgenti C++ richiede un po\' più di lavoro. Il progetto [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) è un tentativo di colmare il divario tra Sphinx e Doxygen, al fine di integrare la documentazione del codice sorgente sia Python che C++ nello stesso sistema. Innanzitutto, Doxygen deve essere configurato per produrre un file XML; l\'output XML viene quindi letto da Breathe e convertito in input adatto per Sphinx.

Consultare la [Guida rapida](https://breathe.readthedocs.io/en/latest/quickstart.html) della documentazione di Breathe per saperne di più su questo processo.

Vedi questa risposta in [Stackoverflow](https://stackoverflow.com/a/35377654) per altre alternative alla documentazione del codice C++ e Python insieme nello stesso progetto.



## Relazioni

-   [Documentazione del sorgente](Source_documentation/it.md)
-   [Sito web della API di FreeCAD](https://www.freecadweb.org/api/)



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Doxygen/it
