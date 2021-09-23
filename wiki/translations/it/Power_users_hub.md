# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/it

------------------------------------------------------------------------



Questo è il posto per esplorare più a fondo FreeCAD. Qui si può imparare a personalizzazione e estendere FreeCAD secondo le proprie esigenze.

FreeCAD è estendibile con il codice [Python](Python/it.md) che viene eseguito direttamente nella [Console Python](Python_console/it.md) o che viene caricato dai moduli all\'avvio. Questo significa che è possibile modificare FreeCAD senza dover ricompilare il programma. Ad esempio, è possibile:

-   **Creare e modificare elementi di geometria**: serve un particolare oggetto (forma o linea speciale) che non è presente nell\'installazione di default FreeCAD? Si può facilmente creare un nuovo tipo di oggetto, sia partendo da zero che adattando un tipo di oggetto esistente.
-   **Creare strumenti e comandi personalizzati**: aggiungere un set di strumenti che eseguono il proprio codice.
-   **Modificare l\'interfaccia**: creare delle barre degli strumenti per mettere i propri strumenti, creare finestre, pannelli o interfacce speciali per interagire con i propri strumenti.
-   **Modificare il grafo della scena**: per costruire e calcolare la geometria, FreeCAD usa processi diversi da quelli che usa per visualizzare la geometria sullo schermo. Si ha accesso totale al modo in cui i contenuti della scena vengono visualizzati sullo schermo, quindi è possibile modificare tale rappresentazione, interagire con essa, o aggiungere tutti i tipi di comportamenti personalizzati e agli accessori dello schermo, quali, ad esempio, informazioni, opzioni di trascinamento, ancoraggio o entità temporanee.

Se si desidera contribuire con contenuti a queste pagine, richiedere un account wiki con autorizzazioni dell\'editor [nel forum](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830) e leggere le [WikiPages](WikiPages.md) per le linee guida generali da seguire. Per gli altri modi di contribuire al progetto, vedere la pagina [Contribuire a FreeCAD](Help_FreeCAD/it.md).

## Personalizzare FreeCAD 

-   [Personalizzare l\'interfaccia](Interface_Customization/it.md): Cominciando dall\'inizio: le barre degli strumenti e i tasti di scelta rapida
-   [Operare con le Macro](Macros/it.md): Registrare semplicemente le operazioni che vengono ripetute spesso o creare il codice Python
-   [Esempi di macro](Macros_recipes/it.md)
-   [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)
-   [Installare ambienti aggiuntivi](Installing_more_workbenches/it.md)

## Script in FreeCAD 

### General


<div class="mw-translate-fuzzy">

### Generale

-   [Introduzione a Python](Introduction_to_Python/it.md) - Vedere anche altri tutorial Python in fondo a questa pagina
-   [Guida agli script in FreeCAD](Python_scripting_tutorial/it.md) - Uno sguardo generale agli script in Python FreeCAD
-   [Script base in FreeCAD](FreeCAD_Scripting_Basics/it.md): Gli script di base\...
-   [Comandi dell\'interfaccia grafica](Gui_Command/it.md) : Aggiungere comandi personalizzati alla GUI
-   [Unità](Units/it.md): utilizzare unità miste in FreeCAD
-   [Profilazione](Profiling/it.md) del codice Python


</div>

### Moduli

Le funzionalità di FreeCAD sono suddivise in moduli che trattano tipi specifici di dati e di applicazioni. FreeCAD è composto da moduli built-in e da moduli di estensione (plug-in). Quando i moduli plugin sono installati, sono disponibili come i moduli built-in. I moduli descritti di seguito sono i moduli di default, inclusi in ogni installazione FreeCAD.

-   I [Moduli builtin](Builtin_modules/it.md) sono i moduli principali di FreeCAD. Essi contengono gli strumenti per manipolare le configurazioni generali di FreeCAD, i documenti e il loro contenuto.
-   La pagina [Creare un Ambiente di lavoro](Workbench_creation/it.md) spiega come creare un proprio ambiente di lavoro.

#### Working with Meshes 


<div class="mw-translate-fuzzy">

### Lavorare con Mesh 

-   [Script per Mesh](Mesh_Scripting/it.md): Come interagire con il [Modulo Mesh](Mesh_Workbench/it.md)


</div>

#### Working with Parts 


<div class="mw-translate-fuzzy">

#### Lavorare con Parti 

-   [Il Modulo Parte](Part_Workbench/it.md): Come sono utilizzati gli strumenti e la struttura di [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE) in FreeCAD
-   [Script di dati topologici](Topological_data_scripting/it.md): Come interagire con il Modulo Parte
-   [PythonOCC](PythonOCC.md) - [PythonOCC](PythonOCC/it.md): Come utilizzare tutta la potenza di Open CASCADE
-   [Da Mesh a Parte](Mesh_to_Part/it.md): Conversione tra tipi di oggetti


</div>

#### Accessing the Coin scenegraph 


<div class="mw-translate-fuzzy">

#### Accedere alla scenografia di Coin 

-   [La grafica di scena di Coin/Inventor](Scenegraph/it.md): Come funziona la rappresentazione della scena in FreeCAD
-   [Pivy](Pivy/it.md): Come accedere alla grafica della scena e come modificarla


</div>

### Controlling the Qt interface 


<div class="mw-translate-fuzzy">

### Controllare l\'interfaccia di Qt 

-   [PySide](PySide/it.md): Come accedere alla gestione dell\'interfaccia e modificare il suo contenuto
-   [Using the FreeCAD GUI](Embedding_FreeCADGui.md) - [Utlizzare l\'interfaccia grafica utente di FreeCAD](Embedding_FreeCADGui/it.md) in una diversa applicazione Qt tramite PyQt


</div>

### Lavorare con oggetti parametrici 

-   [Script di oggetti](Scripted_objects/it.md): come realizzare oggetti con script Python al 100%.
    -   [Oggetti creati da script con parti associate](Scripted_objects_with_attachment/it.md): come rendere gli oggetti creati da script associabili ad altri oggetti.
    -   [Oggetti creati da script che salvano gli attributi](Scripted_objects_saving_attributes/it.md): come salvare e ripristinare gli attributi della classe proxy con `__getstate__` e `__setstate__`.
    -   [Migrazione di oggetti creati da script](Scripted_objects_migration/it.md): come migrare dei vecchi oggetti creati da script in una nuova classe.

### Examples


<div class="mw-translate-fuzzy">

### Esempi

-   [Parti di codici](Code_snippets/it.md) : Una raccolta di esempi di codice Python di FreeCAD, da utilizzare negli script \...
-   [Funzione per tracciare linee](Line_drawing_function/it.md): Come costruire un semplice strumento per tracciare linee
-   [Creare finestre di dialogo](Dialog_creation/it.md): Come creare finestre di dialogo con Qt designer, e come utilizzarle in FreeCAD
-   [Incorporare FreeCAD](Embedding_FreeCAD/it.md): Come importare FreeCAD sotto forma di un modulo Python in altre applicazioni
-   Il [Modulo Disegno](Draft_Workbench/it.md) aggiunge a FreeCAD funzioni base di disegno 2D. E \'scritto interamente in Python, e costituisce un valido esempio per scrivere moduli personali.
-   [FreeCAD vector math library](FreeCAD_vector_math_library.md) - [Libreria di matematica vettoriale di FreeCAD](FreeCAD_vector_math_library/it.md) : Un paio di funzioni utili per manipolare i vettori in FreeCAD. Questa libreria è inclusa anche nel modulo Draft.


</div>

## Funzioni API 

La documentazione completa di FreeCAD si trova in <http://www.freecadweb.org/api/> . Essa contiene le API C++ e Python, e non è ancora del tutto formattata, il che può essere fonte di confusione quando si cerca solo il codice Python. Una versione delle API più facile da esplorare si trova [in questa pagina in inglese](:Category:API.md) e [in questa in italiano](:Category:API/it.md). Ricordare che può essere incompleta in quanto viene aggiornata manualmente. Per informazioni più accurate, esplorare i moduli direttamente dalla console di FreeCAD.

Relazionato: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## Modifiche avanzate 

-   [Avvio e configurazione](Start_up_and_Configuration/it.md): Avvio e opzioni della riga di comando
-   [Installare in Windows](Install_on_Windows/it.md): Utlizzando l\'installatore di Windows
-   [Compilare FreeCAD in Windows](Compile_on_Windows/it.md) e [Compilare FreeCAD in Linux](Compile_on_Linux/it.md)
-   [Marchiare e Personalizzare](Branding/it.md): Semplici modifiche che si possono apportare al codice sorgente per modificare alcuni aspetti del FreeCAD
-   [Moduli extra in Python](Extra_python_modules/it.md) : Potenzia l\'interprete di Python in FreeCAD con questi moduli aggiuntivi!

## Guide di Python 

Questi sono buoni tutorial generici, non specifici per FreeCAD, che possono interessare chi è totalmente nuovo a Python.


<div class="mw-translate-fuzzy">

**Python**

-   [Official python tutorial](https://docs.python.org/2.7/tutorial/index.html) - Una guida molto completa per scoprire Python
-   [Non-programmer tutorial per Python](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python) - Un eccellente wiki
-   [Python per novizi](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - Un grande manuale che si occupa di tutti i concetti base


</div>

**PySide** - Come creare e gestire l\'interfaccia Qt di FreeCAD con Python

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) : Una piattaforma che funge da tutorial mostrando esempi sull\'uso di PySide
-   [PySide/PyQt tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) : Un tutorial di facile lettura con esempi che riguardano PySide e PyQt
-   [PySide documentation](http://qt-project.org/wiki/PySideDocumentation) : dal Progetto Qt
-   [Using QtCreator in PySide](http://qt-project.org/wiki/QtCreator_and_PySide) : anche dal Progetto Qt
-   [PySide reference](http://srinikom.github.io/pyside-docs/index.html) : infiniti dettagli sulle minuzie di PySide e Qt, una fonte di riferimento attendibile
-   [PySide code snippets](http://nullege.com/codes/search?cq=PySide) : un ricercato database di parti di codice di PySide

I seguenti sono due riferimenti specifici di PyQt (non di PySide) che possono offrire alcune informazioni sul suo utilizzo:

-   [Tutorial base di PyQt](http://www.cs.usfca.edu/~afedosov/qttut/) : Un semplice e breve tutorial basato su Linux che spiega come lavorare con PyQt e Qt Designer
-   [Programmare Applicazioni Qt in Python](http://vizzzion.org/?id=pyqt) : Un tutorial molto approfondito che copre tutti i processi di lavoro con Qt e Python.


<div class="mw-translate-fuzzy">

**Pivy** - Come interagire con le scene 3D di FreeCAD

-   [Tutorial base di Pivy](http://pivy.coin3d.org/documentation/pycon) : Un tutorial molto semplice del sito di Pivy
-   [Introduzione a Pivy](http://www.google.com.br/url?sa=U&start=3&q=http://studierstube.icg.tu-graz.ac.at/doc/pdf/PivyStudierstubeTutorial.pdf&ei=XyC1Sc2wOeCKmQem_eHnBQ&usg=AFQjCNEYhb-0DcUc6OxFVijAe1epBb-4aA) : Un documento che non è realmente un tutorial, ma che illustra bene come funziona Pivy


</div>

## Progetti della comunità 

Nel [Portale della comunità](FreeCAD_Community_Portal/it.md), è possibile trovare altri progetti basati su FreeCAD e gestiti dalla comunità degli utenti di FreeCAD. Quando si avvia un nuovo progetto con FreeCAD, ricordarsi di riferirlo nel Portale!

È anche disponibile una pagina dove è descritto come [Contribuire a FreeCAD](Help_FreeCAD/it.md).

-   [Letteratura scientifica](Scientific_literature/it.md): articoli che fanno riferimento o utilizzano il sistema FreeCAD in vari modi.


{{Powerdocnavi

}}

[Category:Hubs](Category:Hubs.md)

---
[documentation index](../README.md) > [API|in questa pagina in inglese]] e ](Category:API|in questa pagina in inglese]] e .md) > Power users hub/it
