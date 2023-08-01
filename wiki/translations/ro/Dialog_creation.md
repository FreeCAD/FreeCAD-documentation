# Dialog creation/ro
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

In această pagină vă vom expune cum se construiește o casetă de dialog Qt Dialog cu [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), Qt\'s instrumentul oficial pentru proiectarea interfețelor, apoi se convertesc în codul Pytohn, ca mai apoi să fie utilizat în interiorul FreeCAD. Voi presupune în exemplul acesta că știți cum se editează și se rulează deja scripturile Python și că puteți face lucruri simple într-o fereastră terminală, cum ar fi navigarea, etc. Trebuie să fi instalat, firește, pyqt.


</div>

In this example, the entire interface is defined in [Python](Python.md). Although this is possible for small interfaces, for larger interfaces the recommendation is to load the created **.ui** files directly into the program.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Two general methods to create interfaces, by including the interface in the Python file, or by using `.ui* files.`


<div class="mw-translate-fuzzy">

## Proiectarea dialogului 

In aplicațiile CAD , proiectarea unei bune interfețe user UI (User Interface) este foarte importantă. Despre tot ce va face utilizatorul va fi prin intermediul unei interfețe: citirea casetelor de dialog, apăsarea butoanelor, alegerea între pictograme etc. De aceea este foarte important să vă gândiți cu atenție la ceea ce doriți să faceți, cum doriți să se comporte utilizatorul, și cum va fi fluxul de activități al acțiunii dvs.


</div>

In CAD applications, designing a good UI (User Interface) is very important. About everything the user will do will be through some piece of interface: reading dialog boxes, pressing buttons, choosing between icons, etc. So it is very important to think carefully to what you want to do, how you want the user to behave, and how will be the workflow of your action.

Există câteva concepte pe care trebuie să le cunoașteți atunci când proiectați interfața:

-   [Modal/non-modal dialogs](http://en.wikipedia.org/wiki/Modal_window): Un dialog modal apare în fața ecranului, oprind acțiunea ferestrei principale, forțând utilizatorului să răspundă la dialog, în timp ce un dialog non-modal nu vă oprește să lucrați pe fereastra principală. În unele cazuri, prima este mai bună, în alte cazuri nu.
-   Identificarea cerințelor și a opțiunilor: Asigurați-vă că utilizatorul știe ce trebuie să facă. Etichetați totul cu o descriere adecvată, utilizați sfaturi pentru sfaturi, etc.
-   Separarea comenzilor de parametrii: Aceasta se face de obicei cu butoanele și câmpurile de introducere a textului. Utilizatorul știe că dacă faceți clic pe un buton veți produce o acțiune în timp ce modificați o valoare în interiorul unui câmp de text, veți schimba un parametru undeva. În prezent, totuși, utilizatorii cunosc de obicei bine ce este un buton, ce este un câmp de intrare etc. Setul de instrumente de interfață pe care îl folosim, Qt, este un set de instrumente de ultimă oră și nu ne vom teme prea mult despre clarificarea lucrurilor, deoarece vor fi deja foarte clare de la sine.

Deci, acum că am definit bine ce vom face, este timpul să deschidem designerul qt. Să proiectăm un dialog foarte simplu, după cum urmează:

![](images/Qttestdialog.jpg )

Apoi, vom folosi acest dialog în FreeCAD pentru a produce un plan dreptunghiular. S-ar putea să nu fie foarte util să produci planuri dreptunghiulare, dar va fi ușor să le schimbi mai târziu pentru a face lucruri mai complexe. Când îl deschideți, Designer Qt arată astfel:

![](images/Qtdesigner-screenshot.jpg )


<div class="mw-translate-fuzzy">

Este foarte simplu de utilizat. În bara din stânga aveți elemente care pot fi trase pe widget(toate instrumentele). În partea dreaptă aveți panouri care afișează tot felul de proprietăți editabile ale elementelor selectate. Deci, începeți cu crearea unui widget nou. Selectați \"Dialog fără butoane\", deoarece nu dorim butoanele implicite Ok / Cancel. Apoi trageți pe widget-ul 3 etichete , unul pentru titlu, unul pentru scrierea \"Înălțime\" și unul pentru scrierea \"Lățime\". Etichetele sunt simple texte care apar pe widget-ul dvs., doar pentru a informa utilizatorul. Dacă selectați o etichetă, în partea dreaptă vor apărea mai multe proprietăți pe care le puteți modifica dacă doriți, cum ar fi stilul fontului, dimensiune a, etc.


</div>


<div class="mw-translate-fuzzy">

Rețineți că selectăm aici niște controale foarte simple, dar Qt are mai multe opțiuni, de exemplu, ați putea folosi Spinboxes în loc de LineEdits, etc \... Aruncați o privire la ceea ce este disponibil, veți avea cu siguranță alte idei.


</div>


<div class="mw-translate-fuzzy">

Este vorba despre tot ce trebuie să facem în Qt Designer. Un ultim lucru, totuși, să redenumim toate elementele noastre cu nume mai ușor, deci va fi mai ușor să le identificăm în scenariile noastre:


</div>

![](images/Qtpropeditor.jpg )

## Traducerea dialogului nostru în python 

Acum, hai să salvăm widget-ul undeva. Acesta va fi salvat ca un fișier .ui, pe care îl vom converti cu ușurință în scriptul python cu pyuic. Sub Windows, programul pyuic este livrat cu pyqt (pentru a fi verificat), sub Linux probabil că va trebui să îl instalați separat plecând de la managerul de pachete (pe sistemele bazate pe debian, face parte din pachetul pyqt4-dev-tools). Pentru a face conversia, va trebui să deschideți o fereastră de terminal (sau sub Windows o fereastră cu prompt de comandă ), să navigați la locul unde ați salvat fișierul .ui și să emiteți/tastați: 
```python
pyuic mywidget.ui > mywidget.py
``` În Windows pyuic.py este localizat in \"C:\\Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\" Pentru conversie creați un batch file numit \"compQt4.bat: 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` In consola Dos tastează fără extensie 
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

In Linux : to do

Deoarece FreeCAD s-a depărtat treptat de PyQt după versiunea 0.13, în favoarea [PySide](http://qt-project.org/wiki/PySide) (Alegeți-vă PySide install [building/building PySide](http://pyside.readthedocs.org/en/latest)), pentru a face fișierul bazat pe PySide acum trebuie să utilizați:


```python
pyside-uic mywidget.ui -o mywidget.py
```


<div class="mw-translate-fuzzy">

In Windows uic.py este localizat in \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\" Pentru a crea un fișier batch \"compSide.bat\":

    @"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py

In consola Dos tastați fără extensie

    compSide myUiFile

Into Linux : to do


</div>


```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
```

In the DOS console type without extension 
```python
compSide myUiFile
``` Into Linux : to do

Pe unele sisteme programul este numit pyuic4 în loc de pyuic. Acest lucru va transforma pur și simplu fișierul .ui într-un script python. Dacă deschidem fișierul mywidget.py, conținutul său este foarte ușor de înțeles: 
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
``` După cum vedeți, are o structură foarte simplă: este creată o clasă numită Ui_Dialog, care stochează elementele de interfață ale widget-ului nostru. Această clasă are două metode, una pentru configurarea widget-ului și una pentru traducerea conținutului său, care este parte din mecanismul general Qt pentru traducerea elementelor de interfață. Metoda de configurare creează pur și simplu, unul câte unul, widget-urile așa cum le-am definit în Qt Designer și le stabilește opțiunile așa cum am decis mai devreme. Apoi, întreaga interfață este tradusă și, în sfârșit, sloturile se conectează (vom vorbi despre asta mai târziu).

Acum putem crea un nou widget și putem folosi această clasă pentru a crea interfața sa. Putem vedea deja widget-ul nostru în acțiune, punând fișierul mywidget.py într-un loc în care va fi găsit de către FreeCAD (în directorul bin FreeCAD sau în oricare dintre subdirectoarele Mod) și, în interpretul Python FreeCAD, facem: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` Și dialogul nostru va apărea! Rețineți că interpretorul nostru Python funcționează încă, avem o fereastră de dialog nemodal. Deci, pentru a o închide, putem (în afară de a face clic pe iconița/pictograma ei apropiată, desigur) să facem: 
```python
d.hide()
```

## Hai să facem ceva cu fereastra noastră de dialog 

Acum, că putem afișa și ascunde fereasta noastră de dialog, trebuie doar să adăugăm o ultimă parte: Să faci ceva! Dacă explorați un pic designerul Qt, veți descoperi rapid o întreagă secțiune numită \"semnale și sloturi\". Practic, funcționează astfel: elementele de pe widget-urile dvs. (în terminologia Qt, aceste elemente sunt ele însele widget-uri) pot trimite semnale. Aceste semnale diferă în funcție de tipul de widget. De exemplu, un buton poate trimite un semnal atunci când este apăsat și când este eliberat. Aceste semnale pot fi conectate la sloturi, care pot fi funcționalități speciale ale altor widgeturi (de exemplu, un dialog are un slot \"închis\" la care puteți conecta semnalul de la un buton de închidere) sau pot fi funcții personalizate. Documentația [PyQt Reference Documentation](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) afișează toate widgeturile qt, ce pot face ele și ce semnale pot trimite etc.

Ceea ce vom face aici este crearea unei noi funcții care va crea un plan definit pe înălțime și lățime și pentru conectarea acelei funcții la semnalul emis de butonul apăsat \"Creare!\". Deci, să începem cu importul modulelor noastre FreeCAD, punând următoarea linie în partea de sus a scriptului, unde deja importăm QtCore și QtGui: 
```python
import FreeCAD, Part
``` Apoi, hai să adăugăm o nouă funție la a noastră Ui_Dialog class: 
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
``` Apoi, trebuie să informăm Qt pentru a conecta butonul la funcție, plasând următoarea linie înainte QtCore.QMetaObject.connectSlotsByName(Dialog): 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` Aceasta, după cum vedeți, conectează semnalul pressed() pus de obiectul creat (butonul \"Creare!\"), Într-un slot numit createPlane, pe care tocmai l-am definit. Gata, asta e! Acum, ca tușă finală, putem adăuga o mică funcție pentru a crea dialogul, va fi mai ușor de apelat. În afara clasei Ui_Dialog, să adăugăm acest cod: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Python amintește: the \_\_init\_\_ method of a class este executată automat ori de câte ori este creat un obiect nou!) Apoi, de la FreeCAD, avem nevoie doar de: 
```python
import mywidget
myDialog = mywidget.plane()
``` Et voila \... Acum puteți încerca tot felul de lucruri, cum ar fi de exemplu inserarea widget-ului în interfața FreeCAD (consultați pagina [Code snippets](Code_snippets.md)) sau realizarea unor instrumente personalizate mult mai avansate, utilizând alte elemente pe widgetul tău.

## Scriptul complet 

Acesta este scriptul complet, pentru referințe: 
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


<div class="mw-translate-fuzzy">

## Crearea unui dialog cu butoane 


</div>

-   [Dialog creation with various widgets](Dialog_creation_with_various_widgets.md) with `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton`, and others.
-   [Dialog creation reading and writing files](Dialog_creation_reading_and_writing_files.md) with `QFileDialog`.
-   [Dialog creation setting colors](Dialog_creation_setting_colors.md) with `QColorDialog`.
-   [Dialog creation image and animated GIF](Dialog_creation_image_and_animated_GIF.md) with `QLabel` and `QMovie`.
-   [PySide usage snippets](PySide_usage_snippets.md).
-   [Qt Example](Qt_Example.md)

## Relevant links 

-   [Manual:Creating interface tools](Manual_Creating_interface_tools.md)


<div class="mw-translate-fuzzy">


{{docnav|Line drawing function|Licence}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Dialog creation/ro
