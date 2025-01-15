# Dialog creation/it
## Introduzione

In questa pagina mostreremo come creare una semplice interfaccia grafica con [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), lo strumento ufficiale di Qt per la progettazione di interfacce; la finestra di dialogo verrà convertita in codice [Python](Python/it.md), quindi verrà utilizzata all\'interno di FreeCAD. Si assume che l\'utente sappia come scrivere ed eseguire [Python](Python/it.md) in generale.

In questo esempio, l\'intera interfaccia è definita in [Python](Python/it.md). Anche se questo è possibile per interfacce piccole, per interfacce più grandi la raccomandazione è di caricare i file **.ui** creati direttamente nel programma.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Due metodi generali per creare delle interfacce, includendo l'interfaccia nel file Python o usando i file `.ui*.`



### Progettare la finestra 

Nelle applicazioni CAD, il disegno di una buona UI (interfaccia utente) è molto importante. L\'utente esegue quasi tutte le operazioni tramite qualche componente dell\'interfaccia: legge le finestre di dialogo, preme i pulsanti, sceglie tra le icone, ecc. Quindi è molto importante pensare attentamente a ciò che si intende fare, a come si desidera che l\'utente si comporti, e a quale sarà il flusso di lavoro delle proprie azioni.

Quando si progetta l\'interfaccia, è bene tenere presenti alcune cose:

-   [Finestre di dialogo modali e non-modali](https://it.wikipedia.org/wiki/Finestra_modale): una finestra di dialogo modale appare sullo schermo in primo piano, blocca l\'azione della finestra principale e costringe l\'utente a rispondere alla finestra di dialogo, mentre un dialogo non-modale permette di continuare a lavorare sulla finestra principale. In alcuni casi è meglio usare la prima soluzione, in altri casi no.
-   Identificare ciò che è necessario e ciò che è facoltativo. Accertarsi che l\'utente sappia esattamente quello che deve fare. Etichettare tutto con una descrizione adeguata, realizzare dei suggerimenti per l\'uso degli strumenti, ecc.
-   Separare i comandi dei parametri. Questo solitamente si ottiene con pulsanti e campi per inserire i testi. L\'utente sa che cliccando su un pulsante si produce una azione, e che, invece, sostituendo un valore all\'interno di un campo di testo si modifica un parametro da qualche parte. In genere, oggi gli utenti sanno bene che cosa è un pulsante, che cosa è un campo di input, ecc. Il toolkit Qt, che stiamo per usare, è il più avanzato strumento di costruzione di interfacce. Non dovrete preoccuparvi molto di fare le cose chiare, dal momento che sarà già esso stesso molto chiaro.

Ora che abbiamo definito con precisione quello che faremo, è il momento di aprire Qt Designer.

Disegneremo una finestra di dialogo molto semplice, simile a questa:

![](images/Qttestdialog.jpg )

Dopo utilizzeremo questa finestra di dialogo all\'interno di FreeCAD per produrre un bel piano rettangolare. Forse pensate che produrre dei bei piani rettangolari non è particolarmente utile, però, in un secondo tempo, sarà facile apportarvi delle modifiche e creare delle cose più complesse.

Quando viene aperto, Qt Designer ha questo aspetto:

![](images/Qtdesigner-screenshot.jpg )

## Creazione della finestra di dialogo 

Qt Designer è molto semplice da usare. Sulla barra di sinistra ci sono gli elementi, che possono essere trascinati sul tuo widget. Sul lato destro ci sono i pannelli delle proprietà, che mostrano tutti i tipi di proprietà modificabili degli elementi selezionati. Quindi, si inizia con la creazione di un nuovo widget.

1.  Selezionare \"Dialogo senza pulsanti\", poiché non vogliamo i pulsanti **OK**/**Annulla** predefiniti.
2.  Avremo bisogno di **Etichette**. Le etichette sono semplici stringhe di testo che appaiono sul tuo widget per informare l\'utente finale. Quando si seleziona un\'etichetta, si nota che sul lato destro appariranno diverse proprietà, che puoi modificare, come: stile del carattere, altezza, ecc\... Quindi trasciniamo 3 etichette separate sul nostro widget:
    -   Un\'etichetta per il titolo
    -   Un\'altra etichetta per scrivere \"**Altezza**\"
    -   E un\'altra etichetta per scrivere \"**Larghezza**\"
3.  Ora abbiamo bisogno di LineEdit (2 di loro in realtà). Trascinane due sul widget. **LineEdits** sono campi di testo, che l\'utente finale può compilare. Quindi abbiamo bisogno di un LineEdit per *Height* e uno per *Width*. Anche qui possiamo modificare le proprietà. Ad esempio, perché non impostare un valore predefinito? Diciamo ad esempio: 1,00 per ciascuno. In questo modo, quando l\'utente vedrà la finestra di dialogo, entrambi i valori saranno già compilati. Se l\'utente finale è soddisfatto, può premere direttamente il pulsante, risparmiando tempo prezioso.
4.  Poi aggiungiamo un **PushButton**. Questo è il pulsante che l\'utente finale dovrà premere dopo aver compilato entrambi i campi.

Notare che qui si sono scelti dei comandi molto semplici, ma Qt dispone di molte altre opzioni, ad esempio, è possibile utilizzare **Spinboxes** invece di **LineEdits**, ecc .. Date un\'occhiata a ciò che è disponibile, esplorate, vi verranno sicuramente altre idee.

Questo è tutto quello che si deve fare in Qt Designer. Un\'ultima cosa, però, rinominare tutti i propri elementi con nomi più adeguati, così negli script sarà più facile identificarli:

![](images/Qtpropeditor.jpg )



### Convertire il dialogo in Python 

Ora, salviamo il nostro widget da qualche parte. Esso verrà salvato come un file .ui, che potremo facilmente convertire in script di Python tramite pyuic. Su Windows, il programma pyuic è incluso con PyQt (da verificare), su Linux probabilmente è necessario installarlo separatamente tramite il proprio gestore di pacchetti (su sistemi debian-based è parte del pacchetto di strumenti PyQt4-dev-tools). Per fare la conversione, è necessario aprire una finestra di terminale (o una finestra del prompt dei comandi in Windows), portarsi nella cartella in cui si è salvato il file .ui, e digitare: 
```python
pyuic mywidget.ui > mywidget.py
``` In Windows pyuic.py si trova in \"C:\\Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\" Per creare il file batch \"compQt4.bat: 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` Nella console Dos digitare senza estensione 
```python
compQt4 myUiFile
```

In macOS, puoi recuperare la versione appropriata (la stessa utilizzata internamente in FreeCAD 0.19) di QT e Pyside con questi comandi (pip richiesto) 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` Questo installerà uic nella cartella \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\" e Designer in \"/Library/Frameworks/Python.framework/Versions /3.7/lib/python3.7/site-packages/PySide2/Designer.app\". Per comodità puoi creare un link di uic in /usr/local/bin per poterlo richiamare semplicemente con uic -g python\... invece di digitare tutto il percorso del programma, e un link a Designer per recuperarlo in la cartella Applicazioni del mac con 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

In Linux : da fare

Dato che, dopo la versione 0.13, FreeCAD si è progressivamente allontanato da PyQt a favore di [PySide](http://qt-project.org/wiki/PySide) (Choice your PySide install [building PySide](http://pyside.readthedocs.org/en/latest/building/)), per costruire il file basato su PySide ora è necessario utilizzare:


```python
pyside-uic mywidget.ui -o mywidget.py
```

In Windows uic.py si trova in \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\" Per creare il file batch \"compSide.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` Nella console Dos digitare senza estensione 
```python
compSide myUiFile
``` In Linux : da fare

Su alcuni sistemi il programma si chiama pyuic4 invece di pyuic. Questa operazione converte semplicemente il file .ui in uno script Python. Se apriamo il file mywidget.py, è molto facile capire il suo contenuto: 
```python
from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(187, 178)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.title.setObjectName("title")
        self.label_width = QtGui.QLabel(Dialog)
        ...

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("Dialog", "Plane-O-Matic", None, QtGui.QApplication.UnicodeUTF8))
        ...
``` Come potete vedere ha una struttura molto semplice: viene creata una classe denominata Ui_Dialog, che memorizza gli elementi dell\'interfaccia del nostro widget. Questa classe ha due metodi, uno per la creazione del widget, e uno per la traduzione del suo contenuto, questo fa parte del meccanismo generale di Qt per tradurre gli elementi dell\'interfaccia. Il metodo di installazione crea semplicemente, uno per uno, i widget come li abbiamo definiti in Qt Designer, e imposta le loro opzioni come abbiamo deciso in precedenza. Poi, viene tradotta l\'intera interfaccia e, infine, vengono collegati gli slot (di cui parleremo più avanti).

Ora possiamo creare un nuovo widget, e utilizzare questa classe per creare la sua interfaccia. A questo punto, possiamo già vedere in azione il nostro widget e, per provarlo, mettiamo il nostro file mywidget.py in un luogo dove FreeCAD possa trovarlo (nella directory bin di FreeCAD, o in una qualsiasi delle sottodirectory Mod), e, nell\'interprete Python di FreeCAD, digitiamo: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` Ecco apparire la nostra finestra di dialogo! Notare che il nostro interprete Python sta ancora funzionando in quanto stiamo usando un dialogo non-modale. Per chiudere la finestra, (ovviamente, oltre a cliccare sulla sua icona di chiusura) possiamo digitare: 
```python
d.hide()
```

### Utilizzare la finestra di dialogo 

Ora che siamo in grado di mostrare e nascondere la nostra finestra di dialogo, basta solo aggiungere una ultima parte: per fargli fare qualcosa!

Provando per un po\' Qt Designer, scoprirete presto un\'intera sezione chiamata \"signals and slots\" (segnali e porte di ingresso dei segnali).

In pratica, funziona così: i componenti dei widget (nella terminologia Qt, questi elementi sono a loro volta dei widget) sono in grado di inviare dei segnali. Tali segnali differiscono a seconda del tipo widget. Ad esempio, un pulsante può inviare un segnale quando viene premuto e quando viene rilasciato. Questi segnali possono essere collegati agli slot. Gli slot possono essere una funzionalità speciale di altri widget (ad esempio una finestra di dialogo ha uno slot \"close\" al quale è possibile collegare il segnale di un pulsante di chiusura), o possono essere funzioni personalizzate.

La [Documentazione di riferimento di PyQt](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) elenca tutti i widget Qt, che cosa possono fare, quali segnali possono inviare, ecc..

Qui, come esempio, creiamo una nuova funzione che genera un piano basato su altezza e larghezza, e colleghiamo tale funzione al segnale \"pressed\" (premuto) emesso dal pulsante \"Create!\".

Allora, cominciamo con l\'importazione dei nostri moduli FreeCAD, inserendo la seguente riga all\'inizio dello script, dove importiamo già QtCore e QtGui: 
```python
import FreeCAD, Part
``` Dopo, aggiungiamo una nuova funzione alla nostra classe Ui_Dialog: 
```python
def createPlane(self):
    try:
        # first we check if valid numbers have been entered
        w = float(self.width.text())
        h = float(self.height.text())
    except ValueError:
        print("Error! Width and Height values must be valid numbers!")
    else:
        # create a face from 4 points
        p1 = FreeCAD.Vector(0,0,0)
        p2 = FreeCAD.Vector(w,0,0)
        p3 = FreeCAD.Vector(w,h,0)
        p4 = FreeCAD.Vector(0,h,0)
        pointslist = [p1,p2,p3,p4,p1]
        mywire = Part.makePolygon(pointslist)
        myface = Part.Face(mywire)
        Part.show(myface)
        self.hide()
``` Poi, bisogna dire a Qt di collegare il pulsante alla funzione, inserendo la seguente riga appena prima di QtCore.QMetaObject.connectSlotsByName (Dialog): 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Questo, come vedete, collega il segnale \"pressed()\" del nostro oggetto create (il pulsante \"Create!\"), allo slot chiamato createPlane, che abbiamo appena definito. Questo è tutto!

Ora, come tocco finale, possiamo aggiungere una piccola funzione per creare il dialogo, così sarà più facile chiamarlo.

Fuori dalla classe Ui_Dialog, aggiungiamo questo codice: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Promemoria di Python: ogni volta che viene creato un nuovo oggetto il metodo \_\_init\_\_ di una classe viene eseguito automaticamente!)

Poi, da FreeCAD, basta solo fare: 
```python
import mywidget
myDialog = mywidget.plane()
``` Questo è tutto amici \... Ora è possibile provare diverse cose, come ad esempio inserire il widget nell\'interfaccia di FreeCAD (vedere la pagina [Modelli di codici](Code_snippets/it.md)), oppure creare strumenti personalizzati molto più avanzati, utilizzando altri elementi nel proprio widget.

### Lo script completo 

Questo è lo script completo di riferimento: 
```python
# Form implementation generated from reading ui file 'mywidget.ui'
#
# Created: Mon Jun  1 19:09:10 2009
#      by: PyQt4 UI code generator 4.4.4
# Modified for PySide 16:02:2015 
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import FreeCAD, Part 

class Ui_Dialog(object):
   def setupUi(self, Dialog):
       Dialog.setObjectName("Dialog")
       Dialog.resize(187, 178)
       self.title = QtGui.QLabel(Dialog)
       self.title.setGeometry(QtCore.QRect(10, 10, 271, 16))
       self.title.setObjectName("title")
       self.label_width = QtGui.QLabel(Dialog)
       self.label_width.setGeometry(QtCore.QRect(10, 50, 57, 16))
       self.label_width.setObjectName("label_width")
       self.label_height = QtGui.QLabel(Dialog)
       self.label_height.setGeometry(QtCore.QRect(10, 90, 57, 16))
       self.label_height.setObjectName("label_height")
       self.width = QtGui.QLineEdit(Dialog)
       self.width.setGeometry(QtCore.QRect(60, 40, 111, 26))
       self.width.setObjectName("width")
       self.height = QtGui.QLineEdit(Dialog)
       self.height.setGeometry(QtCore.QRect(60, 80, 111, 26))
       self.height.setObjectName("height")
       self.create = QtGui.QPushButton(Dialog)
       self.create.setGeometry(QtCore.QRect(50, 140, 83, 26))
       self.create.setObjectName("create")

       self.retranslateUi(Dialog)
       QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
       QtCore.QMetaObject.connectSlotsByName(Dialog)

   def retranslateUi(self, Dialog):
       Dialog.setWindowTitle("Dialog")
       self.title.setText("Plane-O-Matic")
       self.label_width.setText("Width")
       self.label_height.setText("Height")
       self.create.setText("Create!")
       print("tyty")
   def createPlane(self):
       try:
           # first we check if valid numbers have been entered
           w = float(self.width.text())
           h = float(self.height.text())
       except ValueError:
           print("Error! Width and Height values must be valid numbers!")
       else:
           # create a face from 4 points
           p1 = FreeCAD.Vector(0,0,0)
           p2 = FreeCAD.Vector(w,0,0)
           p3 = FreeCAD.Vector(w,h,0)
           p4 = FreeCAD.Vector(0,h,0)
           pointslist = [p1,p2,p3,p4,p1]
           mywire = Part.makePolygon(pointslist)
           myface = Part.Face(mywire)
           Part.show(myface)

class plane():
  def __init__(self):
      self.d = QtGui.QWidget()
      self.ui = Ui_Dialog()
      self.ui.setupUi(self.d)
      self.d.show()

```



## Altri esempi 

-   [Creare una finestra di dialogo con diversi widget](Dialog_creation_with_various_widgets/it.md) con `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton` e altri.
-   [Creare una finestra di dialogo per leggere e scrivere file](Dialog_creation_reading_and_writing_files/it.md) con `QFileDialog`.
-   [Creare una finestra di dialogo per la regolazione del colore](Dialog_creation_setting_colors/it.md) con `QColorDialog`.
-   [Creare una finestra di dialogo per immagini e GIF animate](Dialog_creation_image_and_animated_GIF/it.md) con `QLabel` e `QMovie`.
-   [Frammenti di codice per l\'utilizzo di PySide](PySide_usage_snippets/it.md).
-   [Esempio di Qt](Qt_Example/it.md)



## Link utili 

-   [Manuale:Creare interfacce di strumenti](Manual:Creating_interface_tools/it.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Dialog creation/it
