# Extra python modules/it
## Introduzione

Questa pagina elenca alcuni moduli Python aggiuntivi o altre parti di software che possono essere scaricati gratuitamente da internet, e che aggiungono funzionalità alla vostra installazione FreeCAD.



## PySide (precedentemente era PyQt) 

-   homepage (PySide): [<http://qt-project.org/wiki/PySide>](http://qt-project.org/wiki/PySide)
-   licenza: LGPL
-   optional, ma è necessario per diversi moduli: Draft, Arch, Ship, Plot, OpenSCAD, Spreadsheet

PySide (precedentemente PyQt) è richiesto da diversi moduli di FreeCAD per accedere all\'interfaccia Qt di FreeCAD. È già incluso nella versione per windows di FreeCAD, e di solito su Linux è installato automaticamente da FreeCAD quando l\'installazione viene fatta dai repository ufficiali. Se i moduli Draft, Arch, ecc. sono abilitati, dopo che FreeCAD è installato, significa che PySide (precedentemente PyQt) è presente e non è più necessario fare nulla.

**Note:**

In FreeCAD, PyQt4 diventerà progressivamente obsoleto dopo la versione 0.13, a favore di [PySide](http://qt-project.org/wiki/PySide), che fa esattamente lo stesso lavoro, ma ha una licenza (LGPL) più compatibile con FreeCAD.



### Installazione

#### Linux

Il modo più semplice per installare PySide è attraverso il gestore dei pacchetti della propria distribuzione. Su sistemi Debian/Ubuntu, il nome del pacchetto è generalmente *python-PySide*, mentre per i sistemi basati su RPM viene chiamato *pyside*. Le dipendenze necessarie (Qt e SIP) si installano automaticamente.

#### Windows

Il programma può essere scaricato da <http://qt-project.org/wiki/Category:LanguageBindings>::PySide::Downloads. Prima di installare PyQt4 è necessario installare le librerie Qt e SIP (operazioni da documentare).

#### MacOS

PySide può essere installato su Mac tramite homebrew oppure port. Per maggiori informazioni, vedere [Installare le dipendenze](Compile_on_MacOS/it#Installare_le_dipendenze.md).



### Utilizzo

Dopo l\'installazione, è possibile verificare che tutto funzioni digitando nella console Python di FreeCAD:


```python
import PySide
```

Per accedere all\'interfaccia di FreeCAD, digitare:


```python
from PySide import QtCore,QtGui
FreeCADWindow = FreeCADGui.getMainWindow()
```

Quindi si può iniziare ad esplorare l\'interfaccia con il comando dir(). È possibile aggiungere nuovi elementi, ad esempio un widget personalizzato, con comandi come:


```python
FreeCADWindow.addDockWidget(QtCore.Qt.RghtDockWidgetArea,my_custom_widget)
```

Lavorare con Unicode:


```python
text = text.encode('utf-8')
```

Lavorare con QFileDialog e OpenFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Read a txt file", path, "*.txt")
```

Lavorare con QFileDialog e SaveFileName:


```python
path = FreeCAD.ConfigGet("AppHomePath")
#path = FreeCAD.ConfigGet("UserAppData")
SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Save a file txt", path, "*.txt")
```



### Esempio di passaggio da PyQt4 a PySide 

Nota: questi sono esempi di errori riscontrati nella transizione da PyQt4 verso PySide con le correzioni che sono state fatte. Con gli esempi precedenti sono certamente possibili altre soluzioni


```python
try:
    import PyQt4                                        # PyQt4
    from PyQt4 import QtGui ,QtCore                     # PyQt4
    from PyQt4.QtGui import QComboBox                   # PyQt4
    from PyQt4.QtGui import QMessageBox                 # PyQt4
    from PyQt4.QtGui import QTableWidget, QApplication  # PyQt4
    from PyQt4.QtGui import *                           # PyQt4
    from PyQt4.QtCore import *                          # PyQt4
except Exception:
    import PySide                                       # PySide
    from PySide import QtGui ,QtCore                    # PySide
    from PySide.QtGui import QComboBox                  # PySide
    from PySide.QtGui import QMessageBox                # PySide
    from PySide.QtGui import QTableWidget, QApplication # PySide
    from PySide.QtGui import *                          # PySide
    from PySide.QtCore import *                         # PySide
```

Per accedere all\'interfaccia di FreeCAD, digitare:

è possibile aggiungere nuovi elementi, come un widget personalizzato, con comandi come:


```python
myNewFreeCADWidget = QtGui.QDockWidget()          # create a new dockwidget
myNewFreeCADWidget.ui = Ui_MainWindow()           # myWidget_Ui()             # load the Ui script
myNewFreeCADWidget.ui.setupUi(myNewFreeCADWidget) # setup the ui
try:
    app = QtGui.qApp                              # PyQt4 # the active qt window, = the freecad window since we are inside it
    FCmw = app.activeWindow()                     # PyQt4 # the active qt window, = the freecad window since we are inside it
    FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
except Exception:
    FCmw = FreeCADGui.getMainWindow()             # PySide # the active qt window, = the freecad window since we are inside it
    FCmw.addDockWidget(QtCore.Qt.RightDockWidgetArea,myNewFreeCADWidget) # add the widget to the main window
```

Lavorare con Unicode


```python
try:
    text = unicode(text, 'ISO-8859-1').encode('UTF-8')  # PyQt4
except Exception:
    text = text.encode('utf-8')                         # PySide
```

Lavorare con QFileDialog e OpenFileName :


```python
OpenName = ""
try:
    OpenName = QFileDialog.getOpenFileName(None,QString.fromLocal8Bit("Lire un fichier FCInfo ou txt"),path,"*.FCInfo *.txt") # PyQt4
except Exception:
    OpenName, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Lire un fichier FCInfo ou txt", path, "*.FCInfo *.txt")#PySide
```

Lavorare con QFileDialog e SaveFileName :


```python
SaveName = ""
try:
    SaveName = QFileDialog.getSaveFileName(None,QString.fromLocal8Bit("Sauver un fichier FCInfo"),path,"*.FCInfo") # PyQt4
except Exception:
    SaveName, Filter = PySide.QtGui.QFileDialog.getSaveFileName(None, "Sauver un fichier FCInfo", path, "*.FCInfo")# PySide
```

Il MessageBox:


```python
def errorDialog(msg):
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Critical,u"Error Message",msg )
    try:
        diag.setWindowFlags(PyQt4.QtCore.Qt.WindowStaysOnTopHint) # PyQt4 # this function sets the window before
    except Exception:
        diag.setWindowFlags(PySide.QtCore.Qt.WindowStaysOnTopHint)# PySide # this function sets the window before
#    diag.setWindowModality(QtCore.Qt.ApplicationModal)       # function has been disabled to promote "WindowStaysOnTopHint"
    diag.exec_()
```

Lavorare con setProperty (PyQt4) e setValue (PySide)


```python
self.doubleSpinBox.setProperty("value", 10.0) # PyQt4
```

sostituire con:


```python
self.doubleSpinBox.setValue(10.0) # PySide
```

Lavorare con setToolTip


```python
self.doubleSpinBox.setToolTip(_translate("MainWindow", "Coordinate placement Axis Y", None)) # PyQt4
```

sostituire con:


```python
self.doubleSpinBox.setToolTip(_fromUtf8("Coordinate placement Axis Y")) # PySide
```

oppure:


```python
self.doubleSpinBox.setToolTip(u"Coordinate placement Axis Y.")# PySide
```



### Documentazione aggiuntiva 

-   [Qt official documentation site](https://doc.qt.io/qt.html#qtforpython)

## Pivy

-   homepage: [<https://bitbucket.org/Coin3D/coin/wiki/Home>](https://bitbucket.org/Coin3D/coin/wiki/Home)
-   licenza: BSD
-   optional, ma è necessario per alcuni moduli di FreeCAD: Draft, Arch

Pivy serve a alcuni moduli per accedere alla visualizzazione 3D di FreeCAD. Su Windows, Pivy è già in impacchettato nel programma di installazione FreeCAD, e su Linux solitamente è installato automaticamente quando si installa FreeCAD da un repository ufficiale. Su macOS, purtroppo, è necessario compilare pivy da soli.



### Installazione 



#### Prerequisiti

Si presume che prima di compilare Pivy si desideri avere Coin e SoQt installati.

Per compilarlo su Mac è sufficiente installare il [pacchetto binario Coin3](http://www.coin3d.org/lib/plonesoftwarecenter_view). Il tentativo di installare Coin da MacPorts è stato problematico: ha cercato di aggiungere un sacco di pacchetti di X Windows e alla fine il tentativo è fallito con un errore di script.

Per Fedora ho trovato un RPM con Coin3

SoQt compilato da [codice sorgente](http://www.coin3d.org/lib/soqt/releases/1.5.0) funziona bene su Mac e Linux.

#### Debian & Ubuntu 

A partire da Debian Squeeze e Ubuntu Lucid, Pivy sarà disponibile direttamente dai repository ufficiali e questo eviterà un sacco di problemi. Nel frattempo, è possibile scaricare uno dei pacchetti che abbiamo creato (per Debian e Ubuntu Karmic) e disponibili nelle pagine [Download](Download.md), o compilarlo da soli.

Il modo migliore per compilare facilmente Pivy è quello di prendere il pacchetto sorgente di Debian per Pivy e creare un pacchetto con debuild.

È lo stesso codice sorgente dal sito ufficiale di Pivy, ma la comunità di Debian vi ha fatto diverse aggiunte bug-fixing.

Si compila bene anche su Ubuntu Karmic: <http://packages.debian.org/squeeze/python-pivy> . Scaricare i file .orig.gz e .diff.gz, poi decomprimerli entrambi, quindi applicare .diff al codice sorgente: andare nella cartella del codice sorgente decompresso di Pivy, e applicare la patch .diff:


```python
patch -p1 < ../pivy_0.5.0~svn765-2.diff
```

poi


```python
debuild
```

per avere Pivy correttamente costruito in un pacchetto ufficiale installabile. Dopo è sufficiente installare il pacchetto con gdebi.



#### Altre distribuzioni Linux 

Prima di tutto scaricare gli ultimi sorgenti dai [repository del progetto](http://pivy.coin3d.org/mercurial/):


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

A partire dal marzo 2012, l\'ultima versione è Pivy-0.5.

In seguito serve uno strumento chiamato SWIG per generare il codice C++ per i binding di Python. Pivy-0.5 segnala che è stato testato solo con SWIG 1.3.31, 1.3.33, 1.3.35 e 1.3.40. Perciò si può scaricare un tarball del codice sorgente di una di queste vecchie versioni da [<http://www.swig.org>](http://www.swig.org). Poi scompattarlo e da una riga di comando fare (come root):


```python
./configure
make
make install (or checkinstall if you use it)
```

Impiega appena pochi secondi per costruirsi.

In alternativa, si può provare la costruzione con un SWIG più recente. A partire dal marzo 2012 la versione tipica del repository è la 2.0.4. Pivy presenta un piccolo problema di compilazione con SWIG 2.0.4 su macOS (vedere sotto), mentre pare si costruisca bene su Fedora Core 15.

Dopo le operazioni precedenti andare nel sorgente di Pivy e eseguire:


```python
python setup.py build
```

per creare i file sorgente. Notare che la generazione può produrre migliaia di avvisi, ma fortunatamente non ci sono errori.

Questo è probabilmente obsoleto, ma si può incorrere in un errore di compilazione in cui una \'const char\*\' non può essere convertita in una \'char\*\'. Per risolvere il problema basta scrivere una \'const\' prima nelle righe appropriate. Si devono correggere sei righe.

Dopo di che, installare digitando (come root):


```python
python setup.py install (or checkinstall python setup.py install)
```

Questo è tutto. Pivy è installato.

#### MacOS 

Queste istruzioni potrebbero non essere complete. Qualcosa di simile a questo ha funzionato per OS 10,7 dopo marzo 2012. Io uso MacPorts come repository, ma dovrebbero funzionare anche le altre opzioni.

Per quanto riguarda Linux, scaricare l\'ultimo codice sorgente:


```python
hg clone http://hg.sim.no/Pivy/default Pivy
```

Se non si dispone di hg, è possibile ottenerlo da MacPorts:


```python
port install mercurial
```

Poi, come prima, è necessario SWIG. Si tratta di fare:


```python
port install swig
```

C\'è bisogno anche di:


```python
port install swig-python
```

Da marzo 2012, la versione di SWIG in MacPorts è la 2.0.4. Come detto in precedenza per Linux, potrebbe essere meglio scaricare una versione precedente. SWIG 2.0.4 sembra avere un bug che blocca la costruzione di Pivy. Vedere il primo messaggio in questa [raccolta](https://sourceforge.net/mailarchive/message.php?msg_id=28114815)

Questo problema può essere corretto modificando i 2 percorsi del codice sorgente per aggiungere dereferenziazioni: arg4 \*, \* arg5 al posto di arg4, arg5. Ora si può costruire Pivy:


```python
python setup.py build
sudo python setup.py install
```

#### Windows 

Supponendo di utilizzare Visual Studio 2005 o versioni successive è necessario aprire un prompt dei comandi con \'Visual Studio 2005 Command prompt\' dal menu Strumenti. Se l\'interprete Python non è ancora nel percorso di sistema fare:


```python
set PATH=path_to_python_2.5;%PATH%
```

Per avere pivy funzionante si devono scaricare gli ultimi sorgenti dal repository del progetto:


```python
svn co https://svn.coin3d.org/repos/Pivy/trunk Pivy
```

Dopo serve lo strumento chiamato SWIG per generare il codice C++ per i binding con Python. Si raccomanda di utilizzare la versione 1.3.25 di SWIG, non l\'ultima versione, perché al momento pivy funziona correttamente solo con la 1.3.25. Scaricare i file binari per 1.3.25 da [<http://www.swig.org>](http://www.swig.org). Poi scompattarli e dalla riga di comando aggiungerli al percorso di sistema


```python
set PATH=path_to_swig_1.3.25;%PATH%
```

e impostare il percorso appropriato per COINDIR


```python
set COINDIR=path_to_coin
```

Su Windows il file di configurazione di pivy si aspetta SoWin invece di SoQt come predefinito. Non ho trovato un modo valido per costruirlo con SoQt, così ho modificato direttamente il file setup.py. Nella riga 200 è sufficiente rimuovere la parte \'sowin\': (\'gui.\_sowin\', \'sowin-config\', \'Pivy.gui.\') (non rimuovere le parentesi di chiusura).

Successivamente andare nel sorgente di pivy e eseguire:


```python
python setup.py build
```

per creare i file sorgente. Si può incorrere nell\'errore di compilazione \'header files couldn\'t be found\' (file di intestazione non trovati). In questo caso, impostare la variabile INCLUDE


```python
set INCLUDE=%INCLUDE%;path_to_coin_include_dir
```

e, se le intestazioni di SoQt non sono nella stessa posizione delle intestazioni di Coin, impostare anche


```python
set INCLUDE=%INCLUDE%;path_to_soqt_include_dir
```

e infine impostare le intestazioni di Qt


```python
set INCLUDE=%INCLUDE%;path_to_qt4\include\Qt
```

Se si utilizza la Express Edition di Visual Studio si potrebbe ricevere un\'eccezione keyerror di Python. In questo caso è necessario modificare alcune parti in msvccompiler.py, che si trova nella propria installazione di Python.

Andare alla riga 122 e sostituire la riga


```python
vsbase = r"Software\Microsoft\VisualStudio\%0.1f" % version
```

con


```python
vsbase = r"Software\Microsoft\VCExpress\%0.1f" % version
```

Quindi riprovare di nuovo. Se si riceve un secondo errore del tipo


```python
error: Python was built with Visual Studio 2003;...
```

è necessario sostituire anche la riga 128


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv1.1")
```

con


```python
self.set_macro("FrameworkSDKDir", net, "sdkinstallrootv2.0")
```

Riprovare ancora una volta. Se si ottiene di nuovo un errore quale


```python
error: Python was built with Visual Studio version 8.0, and extensions need to be built with the same version of the compiler, but it isn't installed.
```

allora si deve controllare le variabili d\'ambiente DISTUTILS_USE_SDK e MSSDK con


```python
echo %DISTUTILS_USE_SDK%
echo %MSSDK%
```

Se non sono ancora impostate basta impostarle, ad esempio, a 1


```python
set DISTUTILS_USE_SDK=1
set MSSDK=1
```

Ora, si può incorrere in un errore di compilazione in cui una \'const char \*\' non può essere convertita in una \'char \*\'. Per risolvere il problema basta scrivere una \'const\' prima nelle righe appropriate. Ci sono sei righe da correggere. Infine, copiare la directory di pivy generata in un posto dove l\'interprete di Python di FreeCAD possa trovarla.



### Utilizzo 

Per verificare se Pivy è installato correttamente:


```python
import pivy
```

Per consentire a Pivy di accedere al grafo di scena (Scenegraph) di FreeCAD effettuare le seguenti operazioni:


```python
from pivy import coin
App.newDocument() # Open a document and a view
view = Gui.ActiveDocument.ActiveView
FCSceneGraph = view.getSceneGraph() # returns a pivy Python object that holds a SoSeparator, the main "container" of the Coin scenegraph
FCSceneGraph.addChild(coin.SoCube()) # add a box to scene
```

Ora è possibile esplorare FCSceneGraph con il comando dir().



### Documentazione aggiuntiva 

Purtroppo in rete la documentazione su Pivy è ancora quasi inesistente. Ma può essere utile la documentazione di Coin, in quanto Pivy semplicemente traduce le funzioni di Coin, i nodi e i metodi in Python, tutto mantiene lo stesso nome e le stesse proprietà, tenendo presente la differenza di sintassi tra C e Python:

-   <http://doc.coin3d.org/Coin/classes.html> - Coin3D API Reference
-   <http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html> - The Inventor Mentor - La \"Bibbia\" del linguaggio di descrizione della scena di Inventor.

Potete anche esplorare il file Draft.py nella cartella Mod/Draft di FreeCAD, dato che che in esso si fa un grande uso di pivy.

## pyCollada

-   homepage: <http://pycollada.github.com>
-   license: BSD
-   optional, necessario per consentire di importare ed esportare i file di Collada (.DAE)

pyCollada è una libreria di Python che permette ai programmi di leggere e di scrivere [i file di Collada (\*.DAE)](http://en.wikipedia.org/wiki/COLLADA). Quando pyCollada è installato sul sistema, FreeCAD lo rileva e aggiunge le opzioni di importazione e di esportazione per gestire l\'apertura e il salvataggio di file nel formato Collada.



### Installazione 

#### Linux 


```python
sudo apt-get install python3-collada
```

Si può controllare se pycollada è stato installato correttamente digitando in una console Python:


```python
import collada
```

Se non viene restituito nulla (nessun messaggio di errore), allora tutto è OK

#### Windows 

Su Windows, dalla versione 0.15, pycollada è incluso in FreeCAD sia nella versione di rilascio che in quella di sviluppo quindi non sono più necessari ulteriori passaggi.

#### MacOS 

Se si utilizza la build Homebrew di FreeCAD è possibile installare pycollada nel proprio sistema Python utilizzando pip.

Se è necessario installare pip:


```python
$ sudo easy_install pip
```

Installare pycollada:


```python
$ sudo pip install pycollada
```

Se si utilizza una versione binaria di FreeCAD, si può dire a pip di installare pycollada all\'interno di FreeCAD.app:


```python
$ pip install --target="/Applications/FreeCAD.app/Contents/lib/python2.7/site-packages" pycollada
```

o dopo aver scaricato il codice pycollada


```python
$ export PYTHONPATH=/Applications/FreeCAD\ 0.16.6706.app/Contents/lib/python2.7/site-packages:$PYTHONPATH
$ python setup.py install --prefix=/Applications/FreeCAD\ 0.16.6706.app/Contents
```

## IfcOpenShell

-   homepage: <http://www.ifcopenshell.org>
-   licenza: LGPL
-   optional, necessario per consentire di importare i file IFC

IFCOpenShell è una libreria attualmente in fase di sviluppo, che permette di importare (e presto di esportare) file [Industry foundation Classes (\*.IFC)](http://en.wikipedia.org/wiki/Industry_Foundation_Classes). IFC è una estensione per il formato STEP, e sta diventando lo standard nei processi di lavoro [BIM](http://en.wikipedia.org/wiki/Building_information_modeling). Quando ifcopenshell è installato correttamente nel vostro sistema, il [ambiente Arch](Arch_Workbench/it.md) di FreeCAD è grado di rilevarlo e usarlo per importare i file IFC. Poiché ifcopenshell si basa su OpenCascade, come FreeCAD, la qualità della importazione è molto buona, producendo geometria solida di alta qualità.



### Installazione 

Dato che ifcopenshell è abbastanza recente, dovrete probabilmente compilarla da soli.

#### Linux 

Per compilare ifcopenshell serve che sul sistema siano installati un paio di pacchetti di sviluppo:


```python
liboce-*-dev
python-dev
swig
```

ma dato che anche FreeCAD richiede tutti questi pacchetti, se è possibile compilare FreeCAD, non serve alcun dipendenza in più per compilare IfcOpenShell.

Prelevare l\'ultimo codice sorgente da:


```python
git clone https://github.com/IfcOpenShell/IfcOpenShell.git
```

Il processo di costruzione è molto semplice:


```python
mkdir ifcopenshell-build
cd ifcopenshell-build
cmake ../IfcOpenShell/cmake
```

o, se si utilizza Oce invece di OpenCascade:


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce ../ifcopenshell/cmake
```

Siccome ifcopenshell è fatto principalmente per Blender, utilizza Python3 di impostazione predefinita. Per usarlo dentro FreeCAD, è necessario compilarlo contro la stessa versione di Python che viene utilizzata da FreeCAD. Quindi potrebbe essere necessario forzare la versione di Python con parametri aggiuntivi cmake (adattare per la vostra versione di Python):


```python
cmake -DOCC_INCLUDE_DIR=/usr/include/oce -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 -DPYTHON_LIBRARY=/usr/lib/python2.7.so ../ifcopenshell/cmake
```

Poi:


```python
make
sudo make install
```

Si può controllare se ifcopenshell è stato installato correttamente digitando in una console Python:


```python
import ifcopenshell
```

Se non viene restituito nulla (nessun messaggio di errore), allora tutto è OK

#### Windows 

**Nota**: I programmi di installazione di FreeCAD ufficiali ottenuti dal website/github di FreeCAD contengono già ifcopenshell.

*Copiato dal file README di IfcOpenShell*

Si consiglia agli utenti di utilizzare il file Visual Studio .sln nella cartella win/. Per gli utenti Windows è disponibile una versione predefinita di Open CASCADE sul [sito web di opencascade](http://opencascade.org). Scaricare e installare questa versione e fornire i percorsi dell\'intestazione Open CASCADE e dei file di libreria a MS Visual Studio C++.

Per creare il wrapper IfcPython, è necessario installare SWIG. Si prega di scaricare l\'ultima versione di swigwin dal [sito web di swig](https://www.swig.org/download.html). Dopo aver estratto il file .zip, aggiungi la cartella estratta alla variabile di ambiente PATH. Python deve essere installato, fornire i percorsi di inclusione e libreria a Visual Studio.



### Link

Tutorial [Importare e Esportare IFC - compilare IfcOpenShell](Import/Export_IFC_-_compiling_IfcOpenShell/it.md)



### Installazione 

Su tutte le piattaforme, solo installando il pacchetto appropriato dal [Convertitore ODA DWG-DXF](https://www.opendesign.com/guestfiles/oda_file_converter). Dopo l\'installazione, se l\'utilità non viene trovata automaticamente da FreeCAD, potrebbe essere necessario impostare manualmente il percorso dell\'eseguibile del convertitore, aprire Modifica → Preferenze → Importa-Esporta → DWG e compilare in modo appropriato \"Percorso al convertitore di file Teigha\".

## LazyLoader

LazyLoader è un modulo Python che consente il caricamento differito, pur continuando a importare all\'inizio dello script. Ciò è utile se stai importando un altro modulo che è lento e viene utilizzato più volte durante lo script. L\'utilizzo di LazyLoader può migliorare i tempi di avvio del workbench, ma il modulo dovrà comunque essere caricato al primo utilizzo.



### Installazione 

LazyLoader è incluso in FreeCAD v0.19



### Utilizzo 

Dovrai importare LazyLoader, quindi modificare l\'importazione di qualsiasi modulo desideri rinviare.


```python
from lazy_loader.lazy_loader import LazyLoader
Part = LazyLoader('Part', globals(), 'Part')
```

La variabile Part è il nome del modulo nel tuo script. È possibile replicare \"importa parte come P\" modificando la variabile.


```python
P = LazyLoader('Part', globals(), 'Part')
```

Si può anche importare un modulo da un pacchetto. 
```python
utils = LazyLoader('PathScripts', globals(), 'PathScripts.PathUtils')
``` Non si può importare singole funzioni, solo interi moduli.



### Link 

-   Sorgente originale: <https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/util/lazy_loader.py>
-   Ulteriori indicazioni: <https://wil.yegelwel.com/lazily-importing-python-modules/>
-   Codice all\'interno del codice sorgente di FreeCAD: <https://github.com/FreeCAD/FreeCAD/tree/master/src/3rdParty/lazy_loader>
-   Discussione nel forum: <https://forum.freecadweb.org/viewtopic.php?f=10&t=45298>



---
⏵ [documentation index](../README.md) > [Python Code](Category_Python Code.md) > [Developer Documentation](Category_Developer Documentation.md) > Extra python modules/it
