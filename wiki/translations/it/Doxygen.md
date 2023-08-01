# Doxygen/it
## Introduzione


{{TOCright}}

Doxygen è uno strumento popolare per la generazione di documentazione da sorgenti C++ annotate; supporta anche altri linguaggi di programmazione popolari come C#, PHP, Java e Python. Visitare il [sito web Doxygen](http://www.doxygen.nl/) per saperne di più sul sistema e consultare il [Manuale Doxygen](http://www.doxygen.nl/manual/index.html) per informazioni complete.



## Doxygen e FreeCAD 

Questo documento fornisce una breve introduzione a Doxygen, in particolare a come viene utilizzato in FreeCAD per documentarne i sorgenti. Visitare la pagina [documentazione del codice sorgente](source_documentation/it.md) per istruzioni sulla creazione della documentazione di FreeCAD, anch\'essa ospitata online sul [sito web dell\'API di FreeCAD](https://www.freecadweb.org/api/).

<img alt="" src=images/FreeCAD_doxygen_workflow.svg  style="width:800px;">



*Flusso di lavoro generale per produrre documentazione del codice sorgente con Doxygen.*



## Doxygen col codice C++ 

La sezione [Getting started (Step 3)](http://www.doxygen.nl/manual/starting.html) del manuale Doxygen menziona i modi di base per documentare le fonti.

Per i membri, le classi e gli spazi dei nomi ci sono fondamentalmente due opzioni:

1.  Posizionare uno speciale \"blocco di documentazione\" (un paragrafo commentato) prima della dichiarazione o della definizione della funzione, membro, classe o spazio dei nomi. Per i membri di file, delle classi e dello spazio dei nomi (variabili) è anche consentito posizionare la documentazione direttamente dopo il membro. Vedere la sezione [Blocchi di commenti speciali](http://www.doxygen.nl/manual/docblocks.html#specialblock) nel manuale per saperne di più su questi blocchi.
2.  Posizionare un blocco di documentazione speciale da qualche altra parte (un altro file o un\'altra posizione nello stesso file) e inserire un \"comando strutturale\" nel blocco di documentazione. Un comando strutturale collega un blocco di documentazione a una determinata entità che può essere documentata (una funzione, un membro, una variabile, una classe, uno spazio dei nomi o un file). Vedere la sezione [Documentation at other places](http://www.doxygen.nl/manual/docblocks.html#structuralcommands) ​​nel manuale per saperne di più sui comandi strutturali.

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

Questo è un esempio da [1](https://vtk.org/VTK), una libreria di visualizzazione 3D utilizzata per presentare dati scientifici, come risultati di elementi finiti e informazioni sulla nuvola di punti.

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

-   Assicurarsi di avere i programmi `doxygen` e `doxywizard` nel proprio sistema. Si consiglia inoltre di avere il programma `dot` da [2](https://www.graphviz.org/Graphviz), per generare diagrammi con le relazioni tra classi e spazi dei nomi. Sui sistemi Linux questi programmi possono essere installati dal tuo gestore di pacchetti.


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

Tutti i comandi di documentazione di Doxygen [3](http://www.doxygen.nl/manual/commands.html) iniziano con una barra rovesciata `\` o un simbolo at `@`, a scelta. Normalmente si usa la barra rovesciata `\`, ma occasionalmente si usa `@` per migliorare la leggibilità.

I comandi possono avere uno o più argomenti. Nel manuale Doxygen gli argomenti sono descritti come segue.

-   Se vengono utilizzate parentesi con segno minore e maggiore `<sharp>` l\'argomento è una singola parola.
-   Se vengono utilizzate parentesi tonde `(round)` l\'argomento si estende fino alla fine della riga in cui è stato trovato il comando.
-   Se vengono utilizzate le parentesi graffe {curly} l\'argomento si estende fino al paragrafo successivo. I paragrafi sono delimitati da una riga vuota o da un indicatore di sezione.
-   Se si usano le parentesi quadre `[square]` l\'argomento è facoltativo.


<div class="mw-collapsible mw-collapsed toccolours">

Some of the most common keywords used in the FreeCAD documentation are presented here.


<div class="mw-collapsible-content">

-    (group title), see [\\defgroup](http://www.doxygen.nl/manual/commands.html#cmddefgroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   ]), see [\\ingroup](http://www.doxygen.nl/manual/commands.html#cmdingroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-    [(title)], see [\\addtogroup](http://www.doxygen.nl/manual/commands.html#cmdaddtogroup), and [Grouping](http://www.doxygen.nl/manual/grouping.html).
-   \author { list of authors }, see [\\author](http://www.doxygen.nl/manual/commands.html#cmdauthor); indicates the author of this piece of code.
-   \brief { brief description }, see [\\brief](http://www.doxygen.nl/manual/commands.html#cmdbrief); briefly describes the function.
-   ], see [\\file](http://www.doxygen.nl/manual/commands.html#cmdfile); documents a source or header file.
-    (title), see [\\page](http://www.doxygen.nl/manual/commands.html#cmdpage); puts the information in a separate page, not directly related to one specific class, file or member.
-   , see [\\package](http://www.doxygen.nl/manual/commands.html#cmdpackage); indicates documentation for a Java package (but also used with Python).
-   \fn (function declaration), see [\\fn](http://www.doxygen.nl/manual/commands.html#cmdfn); documents a function.
-   \var (variable declaration), see [\\var](http://www.doxygen.nl/manual/commands.html#cmdvar); documents a variable; it is equivalent to `\fn`, `\property`, and `\typedef`.
-    (section title), see [\\section](http://www.doxygen.nl/manual/commands.html#cmdsection); starts a section.
-    (subsection title), see [\\subsection](http://www.doxygen.nl/manual/commands.html#cmdsubsection); starts a subsection.
-   , see [\\namespace](http://www.doxygen.nl/manual/commands.html#cmdnamespace); indicates information for a namespace.
-   \cond [(section-label)], and \endcond, see [\\cond](http://www.doxygen.nl/manual/commands.html#cmdcond); defines a block to conditionally document or omit.
-   , see [\\a](http://www.doxygen.nl/manual/commands.html#cmda); displays the argument in italics for emphasis.
-    { parameter description }, see [\\param](http://www.doxygen.nl/manual/commands.html#cmdparam); indicates the parameter of a function.
-   \return { description of the return value }, see [\\return](http://www.doxygen.nl/manual/commands.html#cmdreturn); specifies the return value.
-   \sa { references }, see [\\sa](http://www.doxygen.nl/manual/commands.html#cmdsa); prints \"See also\".
-   \note { text }, see [\\note](http://www.doxygen.nl/manual/commands.html#cmdnote); adds a paragraph to be used as a note.


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

In the previous example, the Python file that is commented in a [Doxygen style](#Second_style__documentation_block_before_the_code.md) shows more detailed information and formatting for its classes, functions, and variables. The reason is that this style allows Doxygen to extract the special commands that start with `\` or `@`, while the [Pythonic style](#First_style__Pythonic_documentation.md) does not. Therefore, it would be desirable to convert the Pythonic style to Doxygen style before compiling the documentation. This is possible with an auxiliary Python program called [doxypypy](https://github.com/Feneric/doxypypy). This program is inspired by an older program called [doxypy](https://github.com/Feneric/doxypy), which would take the Pythonic '''docstrings''' and convert them to the Doxygen comment blocks that start with a double hash `##`. Doxypypy goes further than this, as it analyzes the docstrings and extracts items of interest like variables and arguments, and even doctests (example code in the docstrings).

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

The original file has a comment at the top '''@package pyexample_pythonic that indicates the module or namespace that is being described by the file. This `@package` keyword is not interpreted when using triple quotes in the comment block.

In the new file the commenting style is changed so the line becomes `##@package pyexample_pythonic`, which now will be interpreted by Doxygen. However, to be interpreted correctly, the argument has to be edited manually to match the new module (file) name; after doing this the line should be `##@package pyexample_doxygen`.


<div class="mw-collapsible mw-collapsed toccolours">


`pyexample_doxygen.py`

(the top is manually edited, the rest stays the same)


<div class="mw-collapsible-content">


```python
##@package pyexample_doxygen
#Documentation for this module.
#More details go here.
#
```


</div>


</div>

To compile, create the configuration, and run `doxygen` in the toplevel directory that contains the files. 
```python
cd toplevel-source/
doxygen -g
doxygen Doxyfile
xdg-open ./html/index.html
```

The documentation should show similar information to the following, and create appropriate links to the individual modules. 
```python
Namespace List
Here is a list of all documented namespaces with brief descriptions:

 N  pyexample_doxygen   Documentation for this module
 N  pyexample_pythonic  
```

### Converting the comment style on the fly 

In the previous example, the conversion of the documentation blocks was done manually with only one source file. Ideally we want this conversion to occur automatically, on the fly, with any number of Python files. To do this, the Doxygen configuration must be edited accordingly.

To start, don\'t use the `doxypypy` program directly; instead, create the configuration file with `doxygen -g`, then edit the created `Doxyfile`, and modify the following tag. 
```python
FILTER_PATTERNS        = *.py=doxypypy_filter
```

What this does is that files that match the pattern, all files with a extension ending in `.py`, will go through the `doxypypy_filter` program. Every time Doxygen encounters such file in the source tree, the file name will be passed as the first argument to this program. 
```python
doxypypy_filter example.py
```

The `doxypypy_filter` program does not exist by default; it should be created as a shell script to run `doxypypy` with the appropriate options, and to take a file as its first argument. 
```python
#!/bin/sh
doxypypy -a -c "$1"
```

After saving this shell script, make sure it has execute permissions, and that it is located in a directory contained in your system\'s `PATH`. 
```python
chmod a+x doxypypy_filter
mv doxypypy_filter $HOME/bin
```

On Windows systems, a batch file can be used in a similar way. 
```python
doxypypy -a -c %1
```

With this configuration done, the `doxygen Doxyfile` command can be run to generate the documentation as usual. Every Python file using Pythonic '''triple quotes''' will be reformatted on the fly to use `##Doxygen` style comments, and then will be processed by Doxygen, which now will be able to interpret the [special commands](#Doxygen_markup.md) and [Mardown syntax](#Markdown_support.md). The original source code won\'t be modified, and no temporary file with a different name needs to be created as in [the previous section](#Converting_the_Pythonic_style_to_Doxygen_style.md); therefore, if a `@package example` instruction is found, it doesn\'t need to be changed manually.

Note that existing Python files which already use the `##double hash` style for their comment blocks won\'t be affected by the `doxypypy` filter, and will be processed by Doxygen normally.

<img alt="" src=images/FreeCAD_doxygen_doxypypy_workflow.svg  style="width:800px;">



*General workflow to produce source code documentation with Doxygen, when the Python files are filtered to transform the comment blocks.*

### Python code quality check 

To use the automatic conversion of documentation blocks it is important that the original Python sources are correctly written, following the Pythonic guidelines in [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings) and [PEP257](https://www.python.org/dev/peps/pep-0257/). Sloppily written code will cause `doxypypy` to fail when processing the file, and thus Doxygen will be unable to format the documentation correctly.


<div class="mw-collapsible mw-collapsed toccolours">

The following commenting styles will not allow parsing of the docstrings by `doxypypy`, so they should be avoided.


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

Always use triple quotes for the docstrings, and make sure they immediately follow the class or function declaration.

It is also a good idea to verify the quality of your Python code with a tool such as [flake8](http://flake8.pycqa.org/en/latest/) ([Gitlab](https://gitlab.com/pycqa/flake8)). Flake8 primarily combines three tools, [Pyflakes](https://github.com/PyCQA/pyflakes), [Pycodestyle](https://github.com/PyCQA/pycodestyle) (formerly pep8), and the [McCabe complexity checker](https://github.com/PyCQA/mccabe), in order to enforce proper Pythonic style.


```python
pip install --user flake8
flake8 example.py
```

To check all files inside a source tree use `find`. 
```python
find toplevel-source/ -name '*.py' -exec flake8 {} '+'
```

If the project demands it, some code checks deemed too strict can be ignored. The error codes can be consulted in the [Pycodestyle documentation](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes). 
```python
find toplevel-source/ -name '*.py' -exec flake8 --ignore=E266,E402,E722,W503 --max-line-length=100 {} '+'
```

In similar way, a program that primarily checks that comments comply with [PEP257](https://www.python.org/dev/peps/pep-0257/) is [Pydocstyle](https://github.com/PyCQA/pydocstyle). The error codes can be consulted in the [Pydocstyle documentation](http://www.pydocstyle.org/en/4.0.0/error_codes.html). 
```python
pip install --user pydocstyle
pydocstyle example.py
```

Also use it with `find` to perform docstring checks on all source files. 
```python
find toplevel-source/ -name '*.py' -exec pydocstyle {} '+'
```

## Source documentation with Sphinx 

[Sphinx](https://www.sphinx-doc.org/en/master/) is the most popular system to document Python source code. However, since FreeCAD\'s core functions and workbenches are written in C++ it was deemed that Doxygen is a better documentation tool for this project.

While Sphinx can natively parse Python docstrings, it requires a bit more work to parse C++ sources. The [Breathe](https://breathe.readthedocs.io/en/latest/) ([Github](https://github.com/michaeljones/breathe)) project is an attempt at bridging the gap between Sphinx and Doxygen, in order to integrate both Python and C++ source code documentation in the same system. First, Doxygen needs to be configured to output an XML file; the XML output is then read by Breathe, and converted to suitable input for Sphinx.

See the [Quick start guide](https://breathe.readthedocs.io/en/latest/quickstart.html) in the Breathe documentation to know more about this process.

See this answer in [Stackoverflow](https://stackoverflow.com/a/35377654) for other alternatives to documenting C++ and Python code together in the same project.

## Related

-   [Source documentation](Source_documentation.md)
-   [FreeCAD API website](https://www.freecadweb.org/api/)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > [3rd Party](Category_3rd Party.md) > Doxygen/it
