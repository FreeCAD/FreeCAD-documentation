# Dialog creation/sv
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

På denna sida kommer vi att visa hur man bygger en simpel Qt Dialog med [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), Qt\'s officiella verktyg för att designa gränssnitt, och sedan konvertera den till pythonkod, och sedan använda den inuti FreeCAD. Jag antar i exemplet att du redan vet hur du ska redigera och köra python skript, och att du kan göra enkla saker i ett terminalfönster som att navigera, etc. Du måste förstås också ha pyqt installerat.


</div>

In this example, the entire interface is defined in [Python](Python.md). Although this is possible for small interfaces, for larger interfaces the recommendation is to load the created {{FileName|.ui}} files directly into the program.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Two general methods to create interfaces, by including the interface in the Python file, or by using `.ui* files.`


<div class="mw-translate-fuzzy">

## Designa dialogen 

Att i CAD applikationer designa ett bra användargränssnitt är mycket viktigt. Nästan allt som användaren kommer att göra kommer att vara genom någon typ av gränssnitt: läsa dialogrutor, klicka på knappar, välja mellan ikoner, etc. Så det är mycket viktigt att noga tänka igenom vad du vill göra, hur du vill att användaren ska bete sig, och hur arbetsflödet i din aktion kommer att se ut.


</div>

In CAD applications, designing a good UI (User Interface) is very important. About everything the user will do will be through some piece of interface: reading dialog boxes, pressing buttons, choosing between icons, etc. So it is very important to think carefully to what you want to do, how you want the user to behave, and how will be the workflow of your action.

Det finns några koncept man bör känna till när man designar ett gränssnitt:

-   [Modal/non-modal dialogs](http://en.wikipedia.org/wiki/Modal_window): En modal dialog kommer fram längst fram på skärmen, stoppar aktionen i huvudfönstret, och tvingar användare att svara på dialogen, emedan en icke-modal dialog inte stoppar dig från att arbeta med huvudfönstret. I en del fall så är det första bättre, i andra fall inte.

-   Identifiera vad som krävs och vad som är valbart: Försäkra dig om att användaren vet vad den måste göra. Etikettera allting med en riktig beskrivning, använd verktygstips, etc.

-   Separera kommandon från parametrar: Detta görs vanligtvis med knappar och textinmatningsfält. Användaren vet att om en knapp klickas så produceras en aktion emedan ändring av ett värde inuti ett textfält kommer att ändra en parameter någonstans. Nuförtidan så vet de flesta användarna vad en kanpp är, vad ett inmatningsfält är, etc. Det gränssnitts verktygskit vi använder, Qt, är en av de bästa verktygskiten, och vi behöver inte bry oss om så mycket om hur man klargör saker, eftersom de redan är mycket tydliga.

Så, nu när vi har definierat vad vi ska göra, så är det dags att öppna qt designer. Låt oss designa en mycket enkel dialog, som den här:

![](images/Qttestdialog.jpg )

Vi kommer sedan använda denna dialog i FreeCAD till att producera ett fint rektangulärt plan. Du kanske tycker att det inte är så användbart att producera fina rektangulära plan, men det kommer vara lätt att senare ändra den till att göra mer komplexa saker. När du öppnar det, så ser Qt Designer ut så här:

![](images/Qtdesigner-screenshot.jpg )


<div class="mw-translate-fuzzy">

Det är mycket enkelt att använda. I den vänstra lådan har du element som kan dras till din widget. på den högra sidan har du egenskapspanelerna som visar alla möjliga redigerbara egenskaper på de valda elementen. Så, börja med att skapa en ny widget. Välj \"Dialog without buttons\", eftersom vi inte vill ha standard Ok/Cancel knappar. Dra sedan**3 labels**, på din widget, en för titeln, en för att skriva \"Höjd\" och en för att skriva \"Bredd\". Labels är enkla texter som syns på din widget, bara för att informera användaren. Om du väljer en label, så kommer det fram flera egenskaper på den högra sidan som du kan ändra om du vill, som teckensnitt, höjd, etc.


</div>


<div class="mw-translate-fuzzy">

Notera att jag här valde mycket enkla kontroller, men Qt har många fler alternativ, du kan till exempel använda Spinboxes istället för LineEdits, etc\... Ta en titt på vad som finns tillgängligt, du kommer säkert att få andra ideer.


</div>


<div class="mw-translate-fuzzy">

Det är ungefär allt vi behöver göra i Qt Designer. En sista sak bara, låt oss döpa om alla våra element till lättare namn, så blir det lättare att identifiera dem i våra skript:


</div>

![](images/Qtpropeditor.jpg )

## Konvertera vår dialog till python 

Låt oss nu spara vår widget någonstans. Den kommar att sparas som en .ui fil, som vi smidigt kan omvandla till python skript med pyuic. på windows, så är pyuic programmet hoppackat med pyqt (ska verifieras), på linux behöver du troligen installera den separat från din pakethanterare (på debian-baserade system, så är det en del av pyqt4-dev-tools paketet). För att göra konverteringen, så behöver du öppna ett terminalfönster (eller ett kommandoprompt fönster på windows), navigera till där du sparade din .ui file, och skriva: 
```python
pyuic mywidget.ui > mywidget.py
``` In Windows pyuic.py is located in \"C:\\Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\" For conversion create a batch file called \"compQt4.bat: 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` In the DOS console type without extension 
```python
compQt4 myUiFile
```

In macOS, you can retrieve the appropriate version (the same that is used internally in FreeCAD 0.19) of QT and Pyside with these commands (pip required) 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` This will install uic in the folder \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\", and Designer in \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app\". For convenience you can create a link of uic in /usr/local/bin to be able to call it simply with uic -g python \... instead of typing the whole path of the program, and a link to Designer to retrieve it in the mac\'s Applications folder with 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

Into Linux : to do

Since FreeCAD progressively moved away from PyQt after version 0.13, in favour of [PySide](http://qt-project.org/wiki/PySide) (Choose your PySide install [building PySide](http://pyside.readthedocs.org/en/latest/building/)), to make the file based on PySide now you have to use:


```python
pyside-uic mywidget.ui -o mywidget.py
```

In Windows uic.py are located in \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\" For create batch file \"compSide.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` In the DOS console type without extension 
```python
compSide myUiFile
``` Into Linux : to do


<div class="mw-translate-fuzzy">

På en del system så kallas programmet pyuic4 istället för pyuic. Detta kommer att konvertera .ui filen till ett python skript. Om vi öppnar mywidget.py filen, så är dess innehåll mycket lätt att förstå:


</div>


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
```


<div class="mw-translate-fuzzy">

Som du ser så har det en mycket enkel struktur: En klass benämnd Ui\_Dialog skapas, som sparar din widgets gränssnittselement. Den klassen har två metoder, en fär att ställa in widgeten, och en för att översätta dess innehåll, som är en del av de allmäna Qt mekanismerna för översättning av gränssnittselement. Inställningsmetoden skapar, en och en, widgetarna som vi har definierat dem i Qt Designer, och sätter deras alternativ som vi bestämt tidigare. Sedan blir hela gränssnittet översatt, och slutligen, blir sloten anslutna (vi pratar om det senare).


</div>


<div class="mw-translate-fuzzy">

Vi kan nu skapa en ny widget, och använda denna klass till att skapa dess gränssnitt. Vi kan redan se vår widget i aktion, genom att sätta vår mywidget.py fil på en plats där FreeCAD kommer att hitta den (i FreeCAD\'s bin katalog, eller i någon av underkatalogerna till Mod ), och i FreeCAD pythontolken skriva:


</div>


```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
```


<div class="mw-translate-fuzzy">

Och vår dialog kommer fram! Notera att din pythontolk fortfarande fungerar, vi har en icke-modal dialog. Så, för att stänga den, så kan vi (förutom att klicka på dess stängningsikon, förstås) skriva:


</div>


```python
d.hide()
```

## Ordna så att vår dialog gör något 

Nu när vi kan visa och gömma vår dialog, så behöver vi bara lägga till en sista bit: Att låta den göra något! Om du leker lite med Qt designer, så kommer du snabbt upptäcka ett helt avsnitt som kallas \"signals and slots\". I grunden så fungerar det så här: element på dina widgetar (i Qt terminologi, så är dessa element widgetar själva) kan sända signaler. Dessa signaler skiljer sig beroende på widget typ. Till exempel, en knapp kan sända en signal när den är nedtryckt och när den släpps. Dessa signaler kan anslutas till slots, vilka kan vara en speciell funktionalitet i andra widgetar (till exempel en dialog har en \"stäng\" slot till vilken du kan ansluta signalen från en stäng knapp), eller kan vara anpassade funktioner. [PyQt Referensdokumentation](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) listar alla qt widgetar, vad de kan göra, vilka signaler de kan sända , etc\...

Vad vi kommer att göra här, är att skapa en ny funktion som kommer att skapa ett plan, baserat på höjd och bredd, och ansluta denna funktion till nedtryckt signalen som sänds av vår \"Skapa!\" button. Så, låt os börja med att importera våra FreeCAD moduler, genom att sätta följande rader i toppen på skriptet, där vi redan har importerat QtCore och QtGui: 
```python
import FreeCAD, Part
``` Låt oss sedan lägga till en ny funktion till vår Ui\_Dialog klass: 
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
``` Sedan behöver vi informera Qt att ansluta knappen till funktionen, genom att placera följande rad precis innan QtCore.QMetaObject.connectSlotsByName(Dialog): 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Detta ansluter, som du ser, pressed() signalen från vårt skapade objekt (\"Skapa!\" knappen), till en slot benämnd createPlane, som vi just definierade. Klart! Nu, som en slutlig justering, så kan vi lägga till lite funktion för att skapa dialogen, så kommer den bli lättare att anropa. Utanför Ui\_Dialog klassan, så lägger vi till denna kod: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Python reminder: the \_\_init\_\_ method of a class is automatically executed whenever a new object is created!)

Det enda vi sedan behöver göra från FreeCAD är: 
```python
import mywidget
myDialog = mywidget.plane()
``` Det var allt. Nu kan du försöka andra saker, som till exempel sätta in din widget i FreeCAD\'s gränssnitt (se [kodbitar](Code_snippets/sv.md) sidan), eller göra mycket mer avancerade verktyg, genom att använda andra element på din widget.

## Det kompletta skriptet 

För referens, så är det kompletta skriptet här: 
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

## More examples 

-   [Dialog creation with various widgets](Dialog_creation_with_various_widgets.md) with `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton`, and others.
-   [Dialog creation reading and writing files](Dialog_creation_reading_and_writing_files.md) with `QFileDialog`.
-   [Dialog creation setting colors](Dialog_creation_setting_colors.md) with `QColorDialog`.
-   [Dialog creation image and animated GIF](Dialog_creation_image_and_animated_GIF.md) with `QLabel` and `QMovie`.
-   [PySide usage snippets](PySide_usage_snippets.md).
-   [Qt Example](Qt_Example.md)

## Relevant links 

-   [Manual:Creating interface tools](Manual_Creating_interface_tools.md)


<div class="mw-translate-fuzzy">


{{docnav/sv|Line drawing function/sv|Licence/sv}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation/sv
