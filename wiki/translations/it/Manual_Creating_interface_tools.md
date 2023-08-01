# Manual:Creating interface tools/it
{{Manual:TOC/it}}

Negli ultimi due capitoli, abbiamo visto come [creare della geometria Parte](Manual:Creating_and_manipulating_geometry/it.md) e [creare oggetti parametrici](Manual:Creating_parametric_objects/it.md). Manca un ultimo pezzo per avere il pieno controllo su FreeCAD: creare strumenti che interagiscono con l\'utente.

In molte situazioni, non è molto amichevole costruire un oggetto con valori zero, come abbiamo fatto con il rettangolo nel capitolo precedente, e poi chiedere all\'utente di compilare i valori di altezza e larghezza nel pannello delle Proprietà. Questo va bene per un numero molto limitato di oggetti, ma diventa veramente noioso se si devono fare parecchi rettangoli. Sarebbe meglio poter assegnare l\'altezza e la larghezza già durante la creazione del rettangolo.

Python offre uno strumento base che consente all\'utente di inserire il testo dallo schermo:

text = raw_input("Height of the rectangle?")
print("The entered height is ",text)

Però, questo richiede una console Python in esecuzione, e quando si esegue il codice da una macro, non siamo sempre sicuri che la console Python sia attiva sulla macchina dell\'utente.

La [Graphical User Interface](https://en.wikipedia.org/wiki/Graphical_user_interface), o GUI, cioè, tutta la parte di FreeCAD che viene visualizzata sullo schermo (menu, barre degli strumenti, vista 3D, ecc), è tutta lì per questo scopo: interagire con l\'utente. L\'interfaccia di FreeCAD è costruita con [Qt](https://en.wikipedia.org/wiki/Qt_(software)), un kit di strumenti GUI open-source molto comune che offre una vasta gamma di strumenti quali finestre di dialogo, pulsanti, etichette, caselle di testo o menu a discesa. Tutti questi strumenti sono genericamente chiamati \"widget\".

Gli strumenti Qt sono molto facili da usare da Python, grazie ad un modulo Python chiamato [Pyside](https://en.wikipedia.org/wiki/PySide) (ci sono anche molti altri moduli Python per comunicare con Qt da Python). Questo modulo permette di creare e interagire con i widget, leggere ciò che l\'utente ha fatto con essi (leggere quello che è stato inserito nelle caselle di testo) o fare qualcosa quando, ad esempio, viene premuto un pulsante.

Qt fornisce anche un altro strumento interessante chiamato [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), che attualmente è incorporato all\'interno di un\'applicazione più grande chiamata [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator). Esso consente di progettare finestre di dialogo e pannelli dell\'interfaccia grafica, invece di doverli codificare manualmente. In questo capitolo, useremo Qt Creator per la progettazione di un pannello widget che useremo nel pannello **Azioni** di FreeCAD. Quindi è necessario scaricare e installare Qt Creator dalla sua [official page](https://www.qt.io/ide/) se siete su Windows o Mac (su Linux di solito è disponibile tramite il gestore del software).

Nel prossimo esercizio, inizieremo usando Qt Creator per creare un pannello che richieda i valori di lunghezza, larghezza e altezza, poi creeremo su di esso una classe Python che legga nel pannello i valori inseriti dall\'utente, e crei un box con le dimensioni indicate. Questa classe Python sarà poi utilizzata da FreeCAD per visualizzare e controllare il pannello delle azioni:

![](images/Exercise_python_07.jpg )

Cominciamo creando il widget. Avviare Qt Creator, quindi nel menu **File → New File or Project → Files and Classes → Qt → Qt Designer Form** scegliere **Dialog without buttons**. Cliccare **Next**, dare un nome per salvare il file, fare clic su **Next**, lasciare tutti i campi del progetto al loro valore di default (\"\"), e poi clic su **Create**. Il sistema Azioni di FreeCAD aggiungerà automaticamente i pulsanti OK e Annulla, è per questo che abbiamo scelto un dialogo senza pulsanti.

![](images/Exercise_python_06.jpg )

-   Trovare **Label** nell\'elenco degli oggetti del pannello di sinistra, e trascinarla sulla tela del widget. Fare doppio clic sulla Label appena inserita, e cambiare il suo testo in **Length**.
-   Fare clic destro sulla tela del widget, e selezionare **Lay out → Lay out in a Grid**. Questo trasforma il widget in una griglia con attualmente una sola cella, occupata dalla prima etichetta. Ora possiamo aggiungere le voci successive a sinistra, a destra, in alto o in basso rispetto alla prima etichetta, e la griglia si espande automaticamente.
-   Aggiungere altre due etichette sotto la prima, e cambiare il loro testo in Width e Height:

![](images/Exercise_python_08.jpg )

-   Ora inserire 3 widget **Double Spin Box** vicino alle etichette Length, Width e Height. Per ciascuno di essi, nel pannello inferiore di destra, che mostra tutte le impostazioni disponibili per il widget selezionato, individuare **Suffix** e impostare come loro suffisso **mm**. FreeCAD ha un widget più avanzato, in grado di gestire diverse unità, ma che non è disponibile di default in Qt Creator (ma che può essere [compilato](Compile_on_Linux#Qt_designer_plugin.md)), quindi per ora usiamo un Doppio Spin Box standard, e aggiungiamo il suffisso \"mm\" per essere sicuri che l\'utente sappia con quale unità sta lavorando:

![](images/Exercise_python_09.jpg )

-   Ora il nostro widget è creato, manca solo un\'ultima cosa. Dato che FreeCAD avrà bisogno di accedere a tale widget e leggere la lunghezza, la larghezza e l\'altezza, bisogna dare dei nomi appropriati a questi widget, in modo che all\'interno di FreeCAD possano essere ritrovati facilmente. Fare clic su ciascuna delle caselle Double Spin, e nella finestra in alto a destra, fare doppio clic sul nome dell\'oggetto, e cambiarlo a qualcosa di facile da ricordare, ad esempio,: BoxLength, BoxWidth e BoxHeight:

![](images/Exercise_python_10.jpg )

-   Salvare il file, e chiudere Qt Creator, il resto sarà fatto in Python.
-   Aprire FreeCAD e creare una nuova macro dal menù **Macro → Macro → Crea**
-   Incollare il codice seguente. Assicurarsi di modificare il percorso del file in modo che corrisponda a quello con cui è stato salvato il file .ui creato in Qt Creator:


```python
import FreeCAD,FreeCADGui,Part
 
# CHANGE THE LINE BELOW
path_to_ui = "C:\Users\yorik\Documents\dialog.ui"
 
class BoxTaskPanel:
   def __init__(self):
       # this will create a Qt widget from our ui file
       self.form = FreeCADGui.PySideUic.loadUi(path_to_ui)
 
   def accept(self):
       length = self.form.BoxLength.value()
       width = self.form.BoxWidth.value()
       height = self.form.BoxHeight.value()
       if (length == 0) or (width == 0) or (height == 0):
           print("Error! None of the values can be 0!")
           # we bail out without doing anything
           return
       box = Part.makeBox(length,width,height)
       Part.show(box)
       FreeCADGui.Control.closeDialog()
        
panel = BoxTaskPanel()
FreeCADGui.Control.showDialog(panel)
```

Nel codice precedente, abbiamo utilizzato una funzione di convenienza (PySideUic.loadUi) del modulo FreeCADGui. Questa funzione carica un .ui file, crea da esso un Qt Widget, e mappa i nomi, e in questo modo consente di accedere facilmente al SubWidget tramite i loro nomi (ex: self.form.BoxLength).

Anche la funzione \"accept\" è una convenienza offerta da Qt. Quando in un dialogo vi è un pulsante \"OK\" (che è il caso di default quando si utilizza il pannello Azioni di FreeCAD), qualsiasi funzione di nome \"accept\" viene automaticamente eseguita quando si preme il pulsante \"OK\". Analogamente, è possibile anche aggiungere una funzione \"reject\" che viene eseguita quando si preme il pulsante \"Annulla\". Nel nostro caso, abbiamo omesso tale funzione, quindi premendo \"Annulla\" si esegue il comportamento di default (non fare nulla e chiudere la finestra di dialogo).

Se implementiamo una delle funzioni accept o reject, il loro comportamento di default (non fare nulla e chiudere) non si verifica più. Quindi dobbiamo chiudere noi il pannello Azioni. Ciò viene fatto con:


```python
FreeCADGui.Control.closeDialog() 
```

Una volta che abbiamo il nostro BoxTaskPanel che ha 1- un widget chiamato \"self.form\" e 2- se necessario, accetta e rifiuta le funzioni, con esso possiamo aprire il pannello delle attività, tramite queste due ultime righe:


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```

Notare che il widget creato da PySideUic.loadUi non è specifico per FreeCAD, ma è un widget standard di Qt che può essere utilizzato con gli altri strumenti di Qt. Ad esempio, con esso possiamo mostrare una finestra di dialogo separata. Proviamo questo nella console Python di FreeCAD (ovviamente utilizzando il percorso corretto per il file .ui):


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```

Naturalmente al nostro dialogo non abbiamo aggiunto un pulsante \"OK\" o \"Cancel\", dato che è stato fatto per essere usato dal pannello Azioni di FreeCAD che fornisce già tali pulsanti. Quindi non c\'è nessun modo per chiudere la finestra di dialogo (oltre che premere il suo pulsante Chiudi finestra). Ma la funzione show() crea una finestra di dialogo non modale, il che significa che non blocca il resto dell\'interfaccia. Così si possono leggere i valori dei campi mentre il dialogo è ancora aperto,:


```python
w.BoxHeight.value() 
```

Ciò è molto utile per i test.

Infine, non dimenticate che c\'è molta altra documentazione sull\'utilizzo dei wiget di Qt, nella sezione [Script Python](Power_users_hub/it.md), che contiene un [tutorial per creare dialoghi](Dialog_creation/it.md), e uno speciale [tutorial per PySide](PySide/it.md) in tre parti che copre ampiamente l\'argomento.

## Link importanti 

-   [Documentazione di Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
-   [Installare Qt Creator](https://www.qt.io/ide/)
-   [Documentazione sugli script Python in FreeCAD](Power_users_hub/it.md)
-   [Tutorial per creare dialoghi in FreeCAD](Dialog_creation/it.md)
-   [Tutorial su PySide in FreeCAD](PySide/it.md)
-   [Documentazione di PySide](http://srinikom.github.io/pyside-docs/index.html)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Manual:Creating interface tools/it
