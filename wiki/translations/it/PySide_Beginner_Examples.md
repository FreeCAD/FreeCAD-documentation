# PySide Beginner Examples/it
## Introduzione

Lo scopo di questa pagina è di coprire esempi di livello principiante del [PySide](PySide/it.md). Manager GUI (ci sono pagine di accompagnamento [Esempi di PySide di livello medio](PySide_Intermediate_Examples/it.md) e [Esempi di PySide di livello avanzato](PySide_Advanced_Examples/it.md)).

Chi non ha esperienza di programmazione GUI può inciampare nella parola \"widget\". Al di fuori dell\'ambiente informatico il termine di solito viene inteso come

> \"un piccolo gadget o un dispositivo meccanico, in particolare qualcosa il cui nome è sconosciuto o non specificato\"

Nei lavori di GUI come PySide il termine \"widget\" è utilizzato frequentemente per riferirsi agli elementi visibili della GUI, cioè le finestre, i dialoghi e le caselle di input o output. Tutti gli elementi visibili di PySide sono chiamati widget, e, per coloro che sono interessati, discendono tutti da una classe genitore comune: QWidget. Oltre agli elementi visibili PySide offre anche dei widget per il networking, XML, multimedia, e l\'integrazione di database. Ndt: un widget è sostanzialmente un componente visibile.

Se un widget non è incorporato in un widget genitore viene chiamato finestra, e di solito le finestre hanno una struttura e una barra del titolo. I tipi più comuni di finestre sono la \"finestra principale\" (dalla Classe QMainWindow) e le varie sottoclassi di finestre di dialogo (dalla classe QDialog). La finestra QDialog è modale (cioè l\'utente non può fare nulla al di fuori della finestra di dialogo mentre essa è aperta), invece la finestra QMainWindow è non-modale e permette all\'utente di interagire in parallelo con altre finestre.

Questa guida è una lista di scorciatoie per fare lavorare rapidamente un programma PySide sotto FreeCAD, non è finalizzata a insegnare Python o PySide. Alcuni siti che lo fanno sono:

-   [PySide tutorial](http://zetcode.com/gui/pysidetutorial/) in zetcode.com
-   [PySide/PyQt Tutorial](http://www.pythoncentral.io/series/python-pyside-pyqt-tutorial/) in PythonCentral.io
-   [PySide 1.0.7 Reference](http://srinikom.github.io/) in Srinikom.github.io (notare che questo è un manuale di riferimento, non un tutorial)



## La dichiarazione Import 

PySide non viene caricato automaticamente con Python, prima di usarlo deve essere richiamato. Il seguente comando:


```python
from PySide import QtCore
from PySide import QtGui
```

carica le 2 parti di PySide - QtGui possiede le classi per la gestione dell\'interfaccia grafica mentre QtCore contiene classi che non riguardano direttamente la gestione della GUI (ad esempio timer e geometria). Anche se è possibile importare solo quello che è necessario, generalmente sono necessarie entrambe e entrambe devono essere importate.

Le istruzioni di importazione non sono ripetute nei frammenti seguenti; si presume che venga fatto all\'inizio in ogni caso.

## Simplest Example 


<div class="mw-translate-fuzzy">

## L\'esempio più semplice 

L\'interazione più semplice con PySide è quella di presentare all\'utente un messaggio che può solo essere accettato:


</div>


```python
reply = QtGui.QMessageBox.information(None,"","Houston, we have a problem")
```

![](images/PySideScreenSnapshot5.jpg )

## Yes or No Query 


<div class="mw-translate-fuzzy">

## Richiedere una risposta Si o No 

La successiva interazione semplice consiste nel chiedere di rispondere si o no:


</div>


```python
reply = QtGui.QMessageBox.question(None, "", "This is your chance to answer, what do you think?",
         QtGui.QMessageBox.Yes {{!```

QtGui.QMessageBox.No, QtGui.QMessageBox.No) if reply == QtGui.QMessageBox.Yes:

        # this is where the code relevant to a 'Yes' answer goes
        pass

if reply == QtGui.QMessageBox.No:

        # this is where the code relevant to a 'No' answer goes
        pass

}}

![](images/PySideScreenSnapshot6.jpg )

## Enter Text Query 


<div class="mw-translate-fuzzy">

## Richiedere l\'inserimento di un testo 

La prossima parte di codice chiede all\'utente di inserire un testo. Notare che il testo può essere prodotto usando qualsiasi tasto della tastiera:


</div>


```python
reply = QtGui.QInputDialog.getText(None, "Ouija Central","Enter your thoughts for the day:")
if reply[1]:
    # user clicked OK
    replyText = reply[0]
else:
    # user clicked Cancel
    replyText = reply[0] # which will be "" if they clicked Cancel
```

![](images/PySideScreenSnapshot7.jpg )

Ricordare che, anche se vengono inserite solo delle cifre, per esempio \"1234\", il testo è trattato da stringa e deve essere convertito in numero, intero o in virgola mobile, con uno dei seguenti modi:


```python
anInteger = int(userInput) # to convert to an integer from a string representation

aFloat = float(userInput) # to convert to a float from a string representation
```

## More Than 2 Buttons 


<div class="mw-translate-fuzzy">

## Più di 2 pulsanti 

L\'esempio finale del livello base spiega come costruire un dialogo con un numero arbitrario di pulsanti. Questo esempio è programmaticamente troppo complesso per essere invocato da una singola istruzione Python quindi dovrebbe essere contenuto nella pagina successiva, che è quella degli esempi PySide di livello medio. Ma d\'altra parte questo è sovente tutto ciò che è necessario senza entrare in definizioni GUI complesse, quindi questo codice viene posto alla fine della pagina del livello base di PySide invece che all\'inizio della pagina del livello medio.


</div>


```python
from PySide import QtGui, QtCore

class MyButtons(QtGui.QDialog):
    """"""
    def __init__(self):
        super(MyButtons, self).__init__()
        self.initUI()
    def initUI(self):      
        option1Button = QtGui.QPushButton("Option 1")
        option1Button.clicked.connect(self.onOption1)
        option2Button = QtGui.QPushButton("Option 2")
        option2Button.clicked.connect(self.onOption2)
        option3Button = QtGui.QPushButton("Option 3")
        option3Button.clicked.connect(self.onOption3)
        option4Button = QtGui.QPushButton("Option 4")
        option4Button.clicked.connect(self.onOption4)
        option5Button = QtGui.QPushButton("Option 5")
        option5Button.clicked.connect(self.onOption5)
        #
        buttonBox = QtGui.QDialogButtonBox()
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option5Button, QtGui.QDialogButtonBox.ActionRole)
        #
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 0, 50)
        self.setWindowTitle("Pick a Button")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    def onOption1(self):
        self.retStatus = 1
        self.close()
    def onOption2(self):
        self.retStatus = 2
        self.close()
    def onOption3(self):
        self.retStatus = 3
        self.close()
    def onOption4(self):
        self.retStatus = 4
        self.close()
    def onOption5(self):
        self.retStatus = 5
        self.close()

def routine1():
    print ('routine 1')

form = MyButtons()
form.exec_()
if form.retStatus==1:
    routine1()
elif form.retStatus==2:
    routine2()
elif form.retStatus==3:
    routine3()
elif form.retStatus==4:
    routine4()
elif form.retStatus==5:
    routine5()
```

Ogni parte del codice in prova è inserito in una funzione di nome \'routine1()\', \'routine2()\', etc. Si possono utilizzare molti pulsanti, tutti quelli che si possono posizionare nello schermo. Se necessario, seguire gli schemi del codice di esempio per aggiungere pulsanti extra - la finestra di dialogo imposterà la sua larghezza di conseguenza, fino alla larghezza dello schermo.

![](images/PySideScreenSnapshot8.jpg )

Vi è una linea di codice:


```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
```

che allinea orizzontalmente i pulsanti. Per allinearli in verticale, modificare la riga di codice in questo modo:


```python
buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > PySide Beginner Examples/it
