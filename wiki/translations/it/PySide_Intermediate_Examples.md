# PySide Intermediate Examples/it
## Introduzione


{{TOCright}}


<div class="mw-translate-fuzzy">

Questa pagina contiene degli esempi di livello medio di gestione della GUI con [PySide](PySide/it.md). Gli [Esempi di base di PySide](PySide_Beginner_Examples/it.md) e gli [Esempi di livello avanzato di PySide](PySide_Advanced_Examples/it.md) sono contenuti nelle rispettive pagine. In questa pagina gli argomenti di PySide sono descritti utilizzando un programma come esempio. L\'intenzione è quella di presentare dei codici PySide funzionanti, e consentire a chi ha bisogno di usare PySide di copiare la sezione utile, di modificarla e adattarla ai propri scopi.


</div>

### Note

-   Questa pagina non è destinata a trattare il linguaggio Python o a fornire istruzioni su Python.
-   I nomi delle variabili non sono descrittivi, ma sono stati tenuti in sequenza per organizzare al meglio le spiegazioni.
-   Ci sono numerose convenzioni per i nomi dei componenti GUI, nessuno dei quali è mai \"right\" o \"wrong\"
-   C\'è una serie di diverse sequenze di dichiarazioni per i widget, i segnali, i metodi, e ancora una volta nessuna è mai \"right\" o \"wrong\"
-   Vale la pena di ricordare che PySide opera con le stringhe quando tratta gli input dell\'utente, e quello che appare sullo schermo come un numero è in realtà una rappresentazione testuale di un numero

## Discussione del codice - Parte dichiarativa 

Questo \"programma di esempio\" è in realtà una grande definizione di classe, la definizione di una classe PySide GUI, e ha più di 150 righe di codice (inclusi i commenti). La classe e il suo comportamento non sono finalizzati a nulla, l\'unico scopo è quello di dimostrare le azioni GUI possibili e di presentare un codice che si spera possa essere utilizzato da altri utenti di FreeCAD.

La definizione di classe e le poche righe di codice richiamate sono descritti nell\'ordine in cui si presentano nel file. Questo ordine si basa sulla disposizione degli elementi nella schermata ed è piuttosto arbitrario e destinato unicamente a dimostrare le caratteristiche. Questa è la schermata GUI modale generata dalla Classe PySide:

![](images/PySideScreenSnapshot3.jpg )

La maggior parte del resto di questa sezione descrive il contenuto della Class definition che compare alla fine di questa sezione. Prima si descrivono gli elementi dichiarativi che definiscono il funzionamento delle cose e come viene assemblata la GUI, poi si descrivono le sezioni operative (cioè il codice che viene eseguito quando si verificano le interazioni degli utenti). Questa finestra è basata sulla classe QDialog e quindi è modale, questo significa che non si può fare nessuna attività al di fuori della finestra mentre essa è aperta.

### La dichiarazione Import 

La dichiarazione di importazione obbligatoria 
```python
from PySide import QtGui, QtCore
``` Questa riga è meglio posizionarla all\'inizio del file Python.

### La definizione della classe 


```python
class ExampleModalGuiClass(QtGui.QDialog):
    """"""
    def __init__(self):
        super(ExampleModalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
```

È bene copiare esattamente questo codice e poi modificarlo. In sostanza, con questo codice stiamo sotto-classificando la classe QMainWindow di PySide. Adattando questo codice forse si vuole anche cambiare il nome della classe \"ExampleNonmodalGuiClass\" con uno più significativo, accertarsi di cambiarlo in entrambe le posizioni (ad esempio, le righe 1 e 4).

### Ripristinare lo stato della finestra 


```python
self.result = userCancelled
```

Questo non è obbligatorio, ma è piuttosto una buona pratica di programmazione, questo imposta lo stato di default di ripristino per la finestra che sarà disponibile indipendentemente dalle azioni dell\'utente. Più avanti nel codice questo può essere modificato dal codice Python per indicare le diverse opzioni che l\'utente può aver selezionato.

### Creare la finestra 


```python
# create our window
# define window     xLoc,yLoc,xDim,yDim
self.setGeometry(   250, 250, 400, 350)
self.setWindowTitle("Our Example Program Window")
self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
```

Ricordando che le dimensioni dello schermo sono misurate partendo dall\'angolo in alto a sinistra, i valori della terza riga si riferiscono a:

-   numero di pixel dell\'angolo in alto a sinistra, a destra del bordo sinistro dello schermo (250)
-   numero di pixel dell\'angolo in alto a sinistra, sotto al bordo superiore dello schermo (250)
-   larghezza in pixel della finestra (400)
-   altezza in pixel della finestra (350)

Dopo viene impostato il titolo della finestra e la riga finale significa semplicemente che questa finestra non sarà mai oscurata da un\'altra finestra, se non si desidera questo, basta semplicemente inserire il carattere di commento Python (\'\#\') come primo carattere della riga.

### Creare le etichette 


```python
# create some Labels
self.label1 = QtGui.QLabel("                       ", self)
self.label1.setFont('Courier') # set to a non-proportional font
self.label1.move(20, 20)
self.label2 = QtGui.QLabel("sample string number two", self)
self.label2.move(20, 70)
self.label3 = QtGui.QLabel("                        ", self)
self.label3.setFont('Courier') # set to a non-proportional font
self.label3.move(20, 120)
self.label4 = QtGui.QLabel("can you see this?", self)
self.label4.move(20, 170)
```

In PySide le etichette (label) servono a due scopi, per le etichette statiche (come suggerisce il nome), e per quelle di sola lettura (cioè di sola visualizzazione) dei campi di testo. Così possono essere comunicati all\'utente sia le istruzioni immutabili come \"Non premere il pulsante rosso\", sia i risultati dei calcoli dinamici come \"42\". La riga 2 dichiara un\'etichetta e imposta il suo valore iniziale (che in questo caso è vuoto). La riga 3 specifica il tipo di carattere. Si può specificare qualsiasi tipo di carattere disponibile nel sistema, se il font non è specificato viene utilizzato quello di default. In questo caso il carattere viene specificato come non proporzionale. Infine l\'etichetta viene spostata nella sua posizione della finestra - le sue coordinate specificano la sua posizione rispetto alla finestra, non allo schermo.

### Creare una casella di controllo 


```python
# checkboxes
self.checkbox1 = QtGui.QCheckBox("Left side", self)
self.checkbox1.clicked.connect(self.onCheckbox1)
#self.checkbox1.toggle() # will set an initial value if executed
self.checkbox1.move(210,10)
#
self.checkbox2 = QtGui.QCheckBox("Right side", self)
self.checkbox2.clicked.connect(self.onCheckbox2)
self.checkbox2.move(210,30)
```

Le caselle di controllo (Checkbox) possono essere selezionate o deselezionate in qualsiasi combinazione (a differenza dei pulsanti di opzione). La riga 2 ne dichiara una e imposta il suo valore iniziale. La riga 3 specifica quale metodo viene eseguito quando si clicca sulla casella di controllo (in questo caso il metodo \'onCheckBox1\'). Se la riga 4 non non è stata commentata mettendo il carattere di commento Python (\'\#\') come primo carattere, essa viene eseguita e segna la casella di controllo come selezionata. Infine la riga 5 sposta la casella di controllo nella sua posizione.

### Creare i pulsanti di opzione 


```python
# radio buttons
self.radioButton1 = QtGui.QRadioButton("random string one",self)
self.radioButton1.clicked.connect(self.onRadioButton1)
self.radioButton1.move(210,60)
#
self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
self.radioButton2.clicked.connect(self.onRadioButton2)
self.radioButton2.move(210,80)
```


<div class="mw-translate-fuzzy">

La creazione dei pulsanti di opzione (radioButton) è molto simile alla creazione delle caselle di controllo. L\'unica differenza è data dal comportamento dei pulsanti di opzione in quanto non possono essere selezionati contemporaneamente


</div>

### Creare i menu a scomparsa 


```python
# set up lists for pop-ups
self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
# set up pop-up menu
self.popup1 = QtGui.QComboBox(self)
self.popup1.addItems(self.popupItems1)
self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
self.popup1.activated[str].connect(self.onPopup1)
self.popup1.move(210, 115)
```

Nella riga 2 è costruita la lista di quelle che saranno le scelte consentite agli utenti. Un\'alternativa è quella di costruire un dizionario, ma di utilizzare solo i tasti per l\'elenco del menu delle scelte. La riga 4 crea il menu pop-up (noto come un ComboBox in PySide), le opzioni utente sono aggiunte nella riga 5.

Come nota a margine, se è stato utilizzato il dizionario le righe appaiono come queste: 
```python
self.popupItems1 = OrderedDict([("2","widget"),("pink","foobar"),("4","galopsis")])

self.popup1.addItems(self.popupItems1.keys())
``` Tornando al codice principale dell\'esempio per questa sezione, la riga 6 imposta la scelta predefinita, questa riga può essere omessa, il valore della scelta di default può anche essere caricato nell\'etichetta corrispondente. Infine la riga 8 stabilisce il posizionamento.

### Creare i pulsanti - Parte 1 


```python
# toggle visibility button
pushButton1 = QtGui.QPushButton('Toggle visibility', self)
pushButton1.clicked.connect(self.onPushButton1)
pushButton1.setAutoDefault(False)
pushButton1.move(210, 165)
```

Il pulsante (button) e il suo nome sono creati nella riga 2. Il gestore del segnale per sapere quando questo pulsante viene cliccato è specificato nella riga 3. La riga 4 impedisce che il pulsante diventi il \'pulsante di default\' - il pulsante che viene cliccato se l\'utente preme semplicemente il tasto **Return**. Lo spostamento nella sua posizione conclude questo segmento di codice.

### Creare un campo per inserire dei testi 


```python
# text input field
self.textInput = QtGui.QLineEdit(self)
self.textInput.setText("cats & dogs")
self.textInput.setFixedWidth(190)
self.textInput.move(20, 220)
```

Il QLineEdit è probabilmente il widget più comune per consentire all\'utente di inserire dei testi. Questa sezione di codice crea il campo (riga 2), imposta un valore iniziale (riga 3), imposta la lunghezza del campo (riga 4) e posiziona l\'oggetto (riga 5). In questo esempio, la sezione di codice successiva crea un menù contestuale per operare su di esso.

### Creare un menu contestuale 


```python
# set contextual menu options for text editing widget
# set text field to some dogerel
popMenuAction1 = QtGui.QAction(self)
popMenuAction1.setText("load some text")
popMenuAction1.triggered.connect(self.onPopMenuAction1)
# make text uppercase
popMenuAction2 = QtGui.QAction(self)
popMenuAction2.setText("uppercase")
popMenuAction2.triggered.connect(self.onPopMenuAction2)
# menu dividers
popMenuDivider = QtGui.QAction(self)
popMenuDivider.setText('---------')
popMenuDivider.triggered.connect(self.onPopMenuDivider)
# remove all text
popMenuAction3 = QtGui.QAction(self)
popMenuAction3.setText("clear")
popMenuAction3.triggered.connect(self.onPopMenuAction3)
# define menu and add options
self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
self.textInput.addAction(popMenuAction1)
self.textInput.addAction(popMenuAction2)
self.textInput.addAction(popMenuDivider)
self.textInput.addAction(popMenuAction3)
```

Siccome la stessa azione viene eseguita con diversi valori, questo codice ha numerose ripetizioni, ed è una parte di ciò che rende il codice GUI così lungo (non importa quale sistema). Prima viene creata una QAction - si tratta di un abbinamento (o collegamento) del testo che l\'utente vede come opzione selezionabile con il metodo che viene eseguito quando l\'opzione viene selezionata. Si tratta sostanzialmente di un abbinamento tra la scelta utente e una parte di codice. La riga 3 crea, la riga 4 definisce l\'opzione dell\'utente (come vedremo) e la riga 5 specifica quale pezzo di codice Python viene eseguito.

Saltando alla riga 19 (la riga con \"self.textInput.setContextMenuPolicy\") viene creato un ActionsContextMenu, che è il titolare di tutti i singoli collegamenti di QAction tra la scelta dell\'utente e il codice da eseguire. Ogni widget può avere un solo menu contestuale (ovvero il menu associato al tasto destro del mouse), perciò la riga 19 definisce tale menu. Le 4 righe successive aggiungono i collegamenti creati all\'inizio di questa sezione di codice. L\'ordine è significativo, l\'utente vede le opzioni del menu nell\'ordine in cui vengono aggiunte. Notare che l\'opzione del menu 3 non è niente, il suo codice è nullo, ma nel menu contestuale serve a separare due gruppi di opzioni.

### Creare un campo di input numerico 


```python
# numeric input field
self.numericInput = QtGui.QLineEdit(self)
self.numericInput.setInputMask("999")
self.numericInput.setText("000")
self.numericInput.setFixedWidth(50)
self.numericInput.move(250, 220)
```

La creazione del campo di input numerico è simile a quella per l\'inserimento di testi vista in precedenza. Infatti il codice è identico ad eccezione delle righe 3 e 4. La riga 3 imposta la Mask (maschera) come definita da PySide, che in questo caso specifica fino a 3 cifre (che possono includere 0). Un elenco completo dei codici InputMask si trova in [QLineEdit InputMask](http://doc.qt.io/qt-5/qlineedit.html#inputMask-prop)

### Creare i pulsanti - Parte 2 


```python
# cancel button
cancelButton = QtGui.QPushButton('Cancel', self)
cancelButton.clicked.connect(self.onCancel)
cancelButton.setAutoDefault(True)
cancelButton.move(150, 280)
# OK button
okButton = QtGui.QPushButton('OK', self)
okButton.clicked.connect(self.onOk)
okButton.move(260, 280)
```

Entrambi i pulsanti sono creati con un nome (che apparirà come loro etichetta), sono associati ad un metodo che viene eseguito quando sono cliccati, e sono posizionati. L\'unica eccezione è la riga 4, che definisce il tasto \'Cancella\' come il pulsante di default - che significa che sarà \"cliccato\" se l\'utente preme il tasto **Return**.

### Visualizzare la finestra 


```python
# now make the window visible
self.show()
```

C\'è una sola riga e provoca la visualizzazione della GUI dopo il setup.

## Discussione del codice - Parte operativa 

Ora passiamo alla parte operativa della definizione della GUI, che è il codice che viene eseguito in risposta alle interazioni dell\'utente con l\'interfaccia grafica. L\'ordine dei gruppi di dichiarazione non è molto rilevante - con l\'avvertenza che le cose devono essere dichiarate prima di poter essere riferite. Alcuni mettono tutti i gestori di un certo tipo (ad esempio, i gestori dei pulsanti) in un gruppo, altri elencano i gestori in ordine alfabetico. Per specifiche applicazioni ci può essere un motivo correlato a un problema per raggruppare i gestori in un modo specifico.

Vi è un elevato grado di somiglianza tra i gestori. La maggior parte non ricevono un parametro, il fatto che sono in esecuzione è davvero l\'unico parametro (o segnale) che ottengono. Altri come \"onPopup1\" e \"mousePressEvent\" accettano un parametro.

Ci deve essere una corrispondenza 1 a 1 tra i gestori indicati nella sezione dichiarativa e i gestori dichiarati in questa sezione, la sezione operativa. Ci possono essere dei gestori aggiuntivi dichiarati che non vengono mai invocati, ma non ce ne deve essere nessuno mancante.

### I gestori generici 

In questo esempio di codice, dei gestori generici gestiscono i seguenti eventi:

-   onCheckbox1
-   onCheckbox2
-   onRadioButton1
-   onRadioButton2
-   onPushButton1
-   onPopMenuAction1
-   onPopMenuAction2
-   onPopMenuDivider
-   onPopMenuAction3
-   onCancel
-   onOk

La forma generale per i gestori è: 
```python
def handlerName(self):
    lineOfCode1
    lineOfCode2
``` La prima riga ha la parola chiave \"def\" seguita dal nome del gestore. Il nome del gestore deve corrispondere esattamente al nome dato nella sezione dichiarativa precedente. Il parametro \"self\", le parentesi tonde e i due punti finali sono fanno parte della sintassi standard. Once the first line is finished then there are no requirements of the following code, it is purely application specific.

### La gestione dei menu a discesa 


```python
def onPopup1(self, selectedText):
```

Il gestore dei menù Pop-Up è uguale al gestore generico con l\'eccezione che viene passato un secondo parametro, il testo selezionato dall\'utente. Ricordare che tutto quello che è testo in arrivo dal menu pop-up, anche se l\'utente ha selezionato il numero 3, viene passato come stringa \"3\".

### La gestione degli eventi del mouse 


```python
def mousePressEvent(self, event):
    # print mouse position, X & Y
    print("X = ", event.pos().x())
    print("Y = ", event.pos().y())
    #
    if event.button() == QtCore.Qt.LeftButton:
        print("left mouse button")
    if self.label1.underMouse():
        print("over the text '"+self.label1.text()+"'")
```

Il gestore degli eventi del mouse è uguale al gestore generico con l\'eccezione che viene passato un secondo parametro, l\'evento del mouse da parte dell\'utente, es clic del tasto sinistro o destro. Il nome del gestore , \"mousePressEvent\", è riservato e se viene modificato il gestore non riceve più l\'evento dal mouse premuto.

Le coordinate X e Y di posizione del mouse quando viene premuto sono date dai riferimenti \"event.pos().x()\" e \"event.pos().y()\". Le costanti \"QtCore.Qt.LeftButton\" e \"QtCore.Qt.RightButton\" vengono utilizzate per stabilire quale pulsante del mouse è stato premuto.

Si può creare un riferimento a un widget con \"self.widgetName.underMouse()\", che restituisce `True` o `False` secondo se il cursore del mouse si trova sopra al widget \"widgetName\". Sebbene sia presentato nella stessa parte di codice il gestore \"underMouse()\" non è legato al gestore \"mousePressEvent\" e può essere utilizzato in qualsiasi momento.

## Discussione del codice - Parte principale 

La maggior parte del codice si trova nella definizione della classe GUI, nella routine principale non ce nè molto. 
```python
# Constant definitions
global userCancelled, userOK
userCancelled = "Cancelled"
userOK = "OK"
``` Le righe 2,3 e 4 sono quelle che coordinano lo stato della interazione dell\'utente con l\'interfaccia grafica - ad esempio Annulla, OK, o qualsiasi altra definizione di stato dell\'applicazione. Le routine del gestore On Cancel e OnOK precedenti imposta anche questi stati. 
```python
form = ExampleGuiClass()
form.exec_()

if form.result==userCancelled:
    pass # steps to handle user clicking Cancel
if form.result==userOK:
    # steps to handle user clicking OK
    localVariable1 = form.label1.text()
    localVariable2 = form.label2.text()
    localVariable3 = form.label3.text()
    localVariable4 = form.label4.text()
``` Le righe 1 e 2 mostrano il metodo per invocare la GUI. Per un programma possono esserci più definizioni GUI e inoltre non è necessario che l\'interfaccia grafica sia invocata come prima cosa nel file Python, essa può essere richiamata in qualsiasi momento. Il nome della classe GUI è specificato nella riga 1 (in questo caso è \"ExampleGuiClass\"), ma il resto delle 2 righe deve essere copiato alla lettera.

Le righe 4 e 6 utilizzano il campo del risultato per determinare l\'azione appropriata. Le ultime 4 righe mostrano semplicemente la copia dei dati nell\'oggetto GUI per le variabili locali alla procedura principale di esecuzione.

## Esempio completo di codice Modale 

Questo è il codice di esempio completo (sviluppato su FreeCAD v0.14): 
```python
# import statements
from PySide import QtGui, QtCore

# UI Class definitions

class ExampleModalGuiClass(QtGui.QDialog):
    """"""
    def __init__(self):
        super(ExampleModalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
        self.result = userCancelled
        # create our window
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 400, 350)
        self.setWindowTitle("Our Example Modal Program Window")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # create some Labels
        self.label1 = QtGui.QLabel("                       ", self)
        self.label1.setFont('Courier') # set to a non-proportional font
        self.label1.move(20, 20)
        self.label2 = QtGui.QLabel("sample string number two", self)
        self.label2.move(20, 70)
        self.label3 = QtGui.QLabel("                        ", self)
        self.label3.setFont('Courier') # set to a non-proportional font
        self.label3.move(20, 120)
        self.label4 = QtGui.QLabel("can you see this?", self)
        self.label4.move(20, 170)
        # checkboxes
        self.checkbox1 = QtGui.QCheckBox("Left side", self)
        self.checkbox1.clicked.connect(self.onCheckbox1)
        #self.checkbox1.toggle() # will set an initial value if executed
        self.checkbox1.move(210,10)
        #
        self.checkbox2 = QtGui.QCheckBox("Right side", self)
        self.checkbox2.clicked.connect(self.onCheckbox2)
        self.checkbox2.move(210,30)
        # radio buttons
        self.radioButton1 = QtGui.QRadioButton("random string one",self)
        self.radioButton1.clicked.connect(self.onRadioButton1)
        self.radioButton1.move(210,60)
        #
        self.radioButton2 = QtGui.QRadioButton("owt gnirts modnar",self)
        self.radioButton2.clicked.connect(self.onRadioButton2)
        self.radioButton2.move(210,80)
        # set up lists for pop-ups
        self.popupItems1 = ("pizza","apples","candy","cake","potatoes")
        # set up pop-up menu
        self.popup1 = QtGui.QComboBox(self)
        self.popup1.addItems(self.popupItems1)
        self.popup1.setCurrentIndex(self.popupItems1.index("candy"))
        self.popup1.activated[str].connect(self.onPopup1)
        self.popup1.move(210, 115)
        # toggle visibility button
        pushButton1 = QtGui.QPushButton('Toggle visibility', self)
        pushButton1.clicked.connect(self.onPushButton1)
        pushButton1.setAutoDefault(False)
        pushButton1.move(210, 165)
        # text input field
        self.textInput = QtGui.QLineEdit(self)
        self.textInput.setText("cats & dogs")
        self.textInput.setFixedWidth(190)
        self.textInput.move(20, 220)
        # set contextual menu options for text editing widget
        # set text field to some dogerel
        popMenuAction1 = QtGui.QAction(self)
        popMenuAction1.setText("load some text")
        popMenuAction1.triggered.connect(self.onPopMenuAction1)
        # make text uppercase
        popMenuAction2 = QtGui.QAction(self)
        popMenuAction2.setText("uppercase")
        popMenuAction2.triggered.connect(self.onPopMenuAction2)
        # menu dividers
        popMenuDivider = QtGui.QAction(self)
        popMenuDivider.setText('---------')
        popMenuDivider.triggered.connect(self.onPopMenuDivider)
        # remove all text
        popMenuAction3 = QtGui.QAction(self)
        popMenuAction3.setText("clear")
        popMenuAction3.triggered.connect(self.onPopMenuAction3)
        # define menu and add options
        self.textInput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textInput.addAction(popMenuAction1)
        self.textInput.addAction(popMenuAction2)
        self.textInput.addAction(popMenuDivider)
        self.textInput.addAction(popMenuAction3)
        # numeric input field
        self.numericInput = QtGui.QLineEdit(self)
        self.numericInput.setInputMask("999")
        self.numericInput.setText("000")
        self.numericInput.setFixedWidth(50)
        self.numericInput.move(250, 220)
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, 280)
        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, 280)
        # now make the window visible
        self.show()
        #
    def onCheckbox1(self):
        text = self.label1.text()
        if text[0]==' ':
            self.label1.setText('left'+text[4:])
        else:
            self.label1.setText('    '+text[4:])
    def onCheckbox2(self):
        text = self.label1.text()
        if text[-1]==' ':
            self.label1.setText(text[:-5]+'right')
        else:
            self.label1.setText(text[:-5]+'     ')
    def onRadioButton1(self):
        self.label2.setText(self.radioButton1.text())
    def onRadioButton2(self):
        self.label2.setText(self.radioButton2.text())
    def onPopup1(self, selectedText):
        if self.label3.text().isspace():
            self.label3.setText(selectedText)
        else:
            self.label3.setText(self.label3.text()+","+selectedText)
    def onPushButton1(self):
        if self.label4.isVisible():
            self.label4.hide()
        else:
            self.label4.show()
    def onPopMenuAction1(self):
        # load some text into field
        self.textInput.setText("Lorem ipsum dolor sit amet")
    def onPopMenuAction2(self):
        # set text in field to uppercase
        self.textInput.setText(self.textInput.text().upper())
    def onPopMenuDivider(self):
        # this option is the divider and is really there as a spacer on the menu list
        # consequently it has no functional code to execute if user selects it
        pass
    def onPopMenuAction3(self):
        # clear the text from the field
        self.textInput.setText('')
    def onCancel(self):
        self.result         = userCancelled
        self.close()
    def onOk(self):
        self.result         = userOK
        self.close()
    def mousePressEvent(self, event):
        # print mouse position, X & Y
        print("X = ", event.pos().x())
        print("Y = ", event.pos().y())
        #
        if event.button() == QtCore.Qt.LeftButton:
            print("left mouse button")
        if self.label1.underMouse():
            print("over the text '"+self.label1.text()+"'")
        if self.label2.underMouse():
            print("over the text '"+self.label2.text()+"'")
        if self.label3.underMouse():
            print("over the text '"+self.label3.text()+"'")
        if self.label4.underMouse():
            print("over the text '"+self.label4.text()+"'")
        if self.textInput.underMouse():
            print("over the text '"+self.textInput.text()+"'")
        if event.button() == QtCore.Qt.RightButton:
            print("right mouse button")
# Class definitions

# Function definitions

# Constant definitions
userCancelled = "Cancelled"
userOK = "OK"

# code ***********************************************************************************

form = ExampleModalGuiClass()
form.exec_()

if form.result==userCancelled:
    pass # steps to handle user clicking Cancel
if form.result==userOK:
    # steps to handle user clicking OK
    localVariable1 = form.label1.text()
    localVariable2 = form.label2.text()
    localVariable3 = form.label3.text()
    localVariable4 = form.label4.text()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#
``` Il modo migliore di utilizzare questo codice è quello di copiarlo in un editor o in un file macro di FreeCAD e poi provarlo.

## Discussione del codice - Esempio di codice non modale 

Tutti i singoli widget dell\'esempio di finestra modale precedente possono essere trasferiti e utilizzati in una finestra non modale. La differenza principale è che la finestra non modale non impedisce all\'utente di interagire con altre finestre. Fondamentalmente, una finestra non modale è una finestra che può essere aperta e lasciata aperta per tutto il tempo necessario senza che essa ponga delle restrizioni sulle altre finestre dell\'applicazione. Tra i due tipi di finestre ci sono poche differenze di codice, che saranno evidenziate, quindi questo esempio di codice è abbastanza breve. Tutto ciò che è uguale al precedente esempio modale sarà omesso per mantenere breve questa panoramica. Questa è la schermata GUI non modale generata dalla Classe PySide:

![](images/PySideScreenSnapshot4.jpg )

### La dichiarazione Import 

La dichiarazione di importazione obbligatoria 
```python
from PySide import QtGui, QtCore
``` Questa riga è meglio posizionarla all\'inizio del file Python.

### La definizione della classe 


```python
class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    """"""
    def __init__(self):
        super(ExampleNonmodalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
```

È bene copiare esattamente questo codice e poi modificarlo. In sostanza, con questo codice stiamo sotto-classificando la classe QMainWindow di PySide. Adattando questo codice forse si vuole anche cambiare il nome della classe \"ExampleNonmodalGuiClass\" con uno più significativo, accertarsi di cambiarlo in entrambe le posizioni (ad esempio, le righe 1 e 4).

### Creare la finestra 


```python
# create our window
# define window xLoc,yLoc,xDim,yDim
self.setGeometry(   250, 250, 400, 150)
self.setWindowTitle("Our Example Nonmodal Program Window")
self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
self.setMouseTracking(True)
```

Ovviamente le dimensioni della nostra finestra e il titolo sono diversi. La cosa principale da notare è l\'ultima riga che permette a PySide di sapere in tempo reale che cosa inviare come eventi di posizione del mouse. Notare che questi eventi non sono inviati quando il mouse si trova sopra un widget, ad esempio su un pulsante, dato che il widget cattura gli eventi.

### La gestione degli eventi del mouse 


```python
def mouseMoveEvent(self,event):
    self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
```

Questo gestore riceve gli eventi di spostamento del mouse (Mouse Move) e ne visualizza la forma formattata. Provare cosa succede quando si trova sopra ai widget o all\'esterno della finestra.

### Invocare la finestra 


```python
form = ExampleNonmodalGuiClass()
```

Richiamare la finestra è un\'altra area di differenza dall\'esempio precedente. Questa volta per invocare la GUI basta la riga 1.

## Esempio completo di codice Non modale 


```python
from PySide import QtGui, QtCore

# UI Class definitions

class ExampleNonmodalGuiClass(QtGui.QMainWindow):
    """"""
    def __init__(self):
        super(ExampleNonmodalGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
        self.result = userCancelled
        # create our window
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   250, 250, 400, 150)
        self.setWindowTitle("Our Example Nonmodal Program Window")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        # create Labels
        self.label4 = QtGui.QLabel("can you see this?", self)
        self.label4.move(20, 20)
        self.label5 = QtGui.QLabel("Mouse position:", self)
        self.label5.move(20, 70)
        self.label6 = QtGui.QLabel("               ", self)
        self.label6.move(135, 70)
        # toggle visibility button
        pushButton1 = QtGui.QPushButton('Toggle visibility', self)
        pushButton1.clicked.connect(self.onPushButton1)
        pushButton1.setMinimumWidth(150)
        #pushButton1.setAutoDefault(False)
        pushButton1.move(210, 20)
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, 110)
        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, 110)
        # now make the window visible
        self.show()
        #
    def onPushButton1(self):
        if self.label4.isVisible():
            self.label4.hide()
        else:
            self.label4.show()
    def onCancel(self):
        self.result         = userCancelled
        self.close()
    def onOk(self):
        self.result         = userOK
        self.close()
    def mouseMoveEvent(self,event):
        self.label6.setText("X: "+str(event.x()) + " Y: "+str(event.y()))
# Class definitions

# Function definitions

# Constant definitions
global userCancelled, userOK
userCancelled       = "Cancelled"
userOK          = "OK"

# code ***********************************************************************************

form = ExampleNonmodalGuiClass()
#
#OS: Mac OS X
#Word size: 64-bit
#Version: 0.14.3703 (Git)
#Branch: releases/FreeCAD-0-14
#Hash: c6edd47334a3e6f209e493773093db2b9b4f0e40
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
```

## Argomenti aggiuntivi vari 

In merito alla gestione dello spazio sullo schermo in un ambiente GUI ci sono 3 concetti :

-   lo spazio fisico dello schermo
-   il telaio (frame)
-   la geometria (geometry)

All\'interno del software tutto è misurato in pixel. PySide ha una funzione per misurare in unità del mondo reale, ma dato che i produttori non hanno degli standard per la dimensione dei pixel e per le proporzioni, queste misure sono inaffidabili.

Il telaio (Frame) è la dimensione di una finestra comprese le sue barre laterali, la barra superiore (eventualmente con un menu in essa) e la barra inferiore. La geometria (Geometry) è lo spazio contenuto all\'interno del telaio e quindi è sempre inferiore o uguale al telaio. A sua volta il telaio è sempre inferiore o uguale alla dimensione dello schermo disponibile.

### Dimensioni dello spazio disponibile 


```python
# get screen dimensions (Available Screen Size)
screenWidth     = QtGui.QDesktopWidget().screenGeometry().width()
screenHeight        = QtGui.QDesktopWidget().screenGeometry().height()
# get dimensions for available space on screen
availableWidth      = QtGui.QDesktopWidget().availableGeometry().width()
availableHeight     = QtGui.QDesktopWidget().availableGeometry().height()
```

Generalmente \"availableHeight\" deve essere inferiore a \"ScreenHeight\" di un valore pari all\'altezza della barra dei menu. Questi 4 valori sono basati sull\'ambiente hardware e cambiano da computer a computer. Essi non dipendono da nessuna delle dimensioni della finestra dell\'applicazione.

(Since Python 3.9 this warning appears when the above code is executed: **DeprecationWarning: QDesktopWidget.screenGeometry(int screen) const is deprecated**. A replacement seems to be needed from Python 3.10 onwards.)

### Le dimensioni del telaio e della geometria 


```python
# set up a variable to hold the Main Window to save some typing...
mainWin = FreeCAD.Gui.getMainWindow()

mainWin.showFullScreen() # no menu bars, every last pixel is given over to FreeCAD
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showMaximized() # show maximised within the screen, window edges and the menu bar will be displayed
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.showNormal() # show at the last non-maximised or non-minimised size (and location)
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()

mainWin.setGeometry(50, 50, 800, 800) # specifically set FreeCAD main window's size and location, this will become the new setting for 'showNormal()'

mainWin.showMinimized() # FreeCAD will disappear from view after this command...
mainWin.geometry()
mainWin.frameSize()
mainWin.frameGeometry()
```

Questi stessi comandi possono essere eseguiti anche su una finestra generata dall\'utente, la sintassi non cambia.


{{Powerdocnavi

}} 

_ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > PySide Intermediate Examples/it
