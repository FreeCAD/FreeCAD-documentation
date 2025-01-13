# Drawing Documentation/it
Questa pagina documenta la comprensione del modulo Drawing di jcc242. Il modulo include i file e le funzioni su cui sta lavorando attualmente e non può ancora essere inserita nel ramo master. La fonte di questi file è il suo [Github](https://github.com/jcc242/FreeCAD), ma fate attenzione in quanto è molto instabile!

## Base (Mod/Drawing) 

### gdtsvg.py

Script Python che genera snippet SVG per elementi come simboli gd&t, simboli di quotatura ed elementi SVG di base come linee, cerchi e percorsi.

Ha diversi file di supporto che non fanno molto. Eseguire DrawingTest.py per creare un gruppo di icone SVG nella directory delle icone che visualizza in anteprima varie icone nel file gdtsvg.py. settingslist.py, dimesettings e convert.py sono tutti deprecati dai metodi di impostazione precedenti e dovrebbero probabilmente essere rimossi man mano che il ramo Drawing si avvicina alla fusione in master.

### DrawingAlgos.py

Crea linee SVG da un elenco di vertici, supporta sia i bordi nascosti che quelli visibili. Probabilmente dovrebbe essere unito a gdtsvg.py man mano che il file matura.

#### createSVG

Accetta part come argomento, proietta la parte in linee dall\'oggetto Drawing.project e poi disegna crea l\'svg per ogni linea.

## App

Contiene il lato backend del modulo di disegno.

### AppDrawing.cpp

Inizializza i vari namespaces, moduli e materiale utilizzato nel modulo di disegno. Genera un errore se non riesce a caricare il modulo Part.

### DrawingExport.cpp

Due classi: SVGOutput e DXFOutput. Entrambi contengono metodi per pubblicare il codice nella rispettiva lingua. In genere richiedono un oggetto con il typedef appropriato e talvolta alcune informazioni identificative aggiuntive.

### FeatureClip.cpp

Metodi di callback (?) per il clipping delle feature della la GUI, così sembrerebbe. Chiamato da solo creerà il percorso della clip, se ShowFrame.getValue è impostato su TRUE mostrerà anche il bordo della cornice.

### FeaturePage.cpp

Gestisce le visualizzazioni.

onChanged() per fare delle cose quando le proprietà vengono modificate.

execute() per ricalcolare una feature view, o almeno così afferma. Sembra che contenga elementi per verificare la presenza di testi modificabili e salvare disegni. È necessario indagare ulteriormente.

getEditableTextsFromTemplate() per recuperare testo che può essere modificato da FreeCAD da un file SVG.

### FeatureProjection.cpp

Appiattisce l\'oggetto su un\'immagine 2D?

### FeatureView.cpp

Definisce le proprietà per le visualizzazioni.

### FeatureViewAnnotation.cpp

Definisce le proprietà per le annotazioni (per ora solo testo), ha un metodo di esecuzione per aggiornare il testo se modificato/spostato.

### FeatureViewPart.cpp

Costruttore per aggiungere proprietà. Ottiene elementi di aspetto per le parti proiettate.

### PageGroup.cpp

Aggiunge solo una proprietà per un elenco di pagine, non fa molto altro.

### Precompiled.cppp

Solamente #include \"PreCompiled.h\"

### ProjectionAlgos.cpp

Il costruttore esegue semplicemente il metodoexecute() per aggiornare le sue cose

invertY: poiché SVG utilizza il suo asse y al contrario rispetto a ogni altro sistema di coordinate nel mondo, è necessario invertirlo quando si converte da una parte di FreeCAD a una proiezione SVG per la vista del disegno.

getSVG: recupera il codice SVG da DrawingExport. Formati a seconda del tipo di linea (nascosta o meno e alcune altre cose che devo capire).

getDXF: uguale a getSVG tranne che per il formato DXF.

## Gui

### AppDrawingGui.cpp

Inizializza la GUI di disegno.

### AppDrawingGuiPy.cpp

Fornisce interfacce di apertura, importazione ed esportazione? Sembra che sia accessibile da Python.

### Command.cpp

Gestisce i comandi (dalla barra degli strumenti?) come la creazione di nuovi disegni e altro. Sembra che questo gestisca le chiamate QT dal clic sul pulsante a qualsiasi comando a cui deve andare, ad es. facendo clic sul pulsante CmdDrawingOrthoViews verrà visualizzata la GUI delle viste ortografiche nella finestra di dialogo delle attività.

### DrawingView.cpp

Fa un sacco di cose sulla GUI QT, ho bisogno di leggere di più al riguardo.

### TaskDialog.cpp

Crea la finestra di dialogo delle attività sul lato e probabilmente passa ad essa dalla visualizzazione ad albero, a seconda dei casi.

### TaskOrthoViews.cpp

Crea la finestra di dialogo delle attività per posizionare le viste ortografiche!!

Fa molti calcoli su dove posizionare le cose (anche calcoli automatici, a quanto pare).

Prende l\'input dalla GUI TaskOrthoViews e fa alcune cose con esso. Utilizza il metodo di ereditarietà singola di cui si parla [sul sito Web qt](http://doc.qt.digia.com/qt/designer-using-a-ui-file.html).

### ViewProviderPage.cpp

Il costruttore aggiunge alcune proprietà per gli elementi di visualizzazione. Il distruttore non fa nulla. Associa qualcosa (associa cosa? associa la vista alla pagina?) imposta e ottiene le modalità di visualizzazione (cosa sono le modalità di visualizzazione? cosa fanno e quali sono le opzioni possibili?) Fa qualcosa sull\'aggiornamento di alcuni tipi di dati ha un menu contestuale che dice \"Mostra disegno\", scoprire cosa significa Ha una funzione per fare doppio clic per selezionare la vista (credo?)

showDrawingView sembra fare un po\' di lavoro sulle impostazioni: ottiene il documento corrente, imposta l\'icona e il titolo della finestra, lo aggiunge alla finestra principale (di FreeCAD?)

### ViewProviderView.cpp

Non sembra fare molto, anche se sono sicuro che sia importante.

### Workbench.cpp

Aggiunge le icone alle barre degli strumenti e cose del genere.



## Flusso di lavoro 

## Flusso del programma 

CanvasView è l\'oggetto QGraphicsScene effettivo e DrawingView elabora un elenco di FeatureView collegati per riferimento in /App/FeatureViewPage. DrawingView sceglie quindi la classe QGraphicsItem appropriata (QGraphicsItemViewPart o QGraphicsItemViewDimension) e quindi chiama una funzione in CanvasView per crearla e aggiungerla alla scena.

## Aggiunta di comandi all\'ambiente Disegno 

4 semplici passaggi:

1.  Aggiungere una classe a Command.cpp. Seguire gli altri per un esempio della formattazione.
2.  Aggiungere un titolo, un\'icona, un tooltip, ecc., ancora una volta, seguire le classi esistenti in command.cpp
3.  Aggiungere la propria classe alla fine di Command.cpp
4.  Aggiungere le proprie informazioni a Workbench.cpp, questo dirà al modulo FreeCAD/Drawing dove posizionare le icone definite in command.cpp nell\'effettiva interfaccia di Freecad (le barre degli strumenti, i menu a discesa, ecc.)

{{Drawing Tools navi}}



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Drawing](Category_Drawing.md) > Drawing Documentation/it
