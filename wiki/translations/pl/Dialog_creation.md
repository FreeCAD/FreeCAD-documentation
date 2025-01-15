# Dialog creation/pl
## Wprowadzenie

Na tej stronie pokażemy, jak zbudować prosty interfejs graficzny za pomocą [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), oficjalnego narzędzia Qt do projektowania interfejsów. Przekonwertujemy okno dialogowe na kod [Python](Python/pl.md), a następnie będzie używane wewnątrz FreeCAD. Zakładamy, że użytkownik wie, jak edytować i uruchamiać [Python](Python/pl.md).

W tym przykładzie cały interfejs jest zdefiniowany w środowisku [Python](Python.md). Chociaż jest to możliwe w przypadku małych interfejsów, w przypadku większych interfejsów zaleca się ładowanie utworzonych plików **.ui** bezpośrednio do programu.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> 
*Dwie ogólne metody tworzenia interfejsów, poprzez włączenie interfejsu do pliku Python lub poprzez użycie plików `.ui*.`



## Projektujemy okno dialogowe 

W aplikacjach CAD zaprojektowanie dobrego interfejsu użytkownika *(UI)* jest bardzo ważne. Prawie wszystko, co użytkownik będzie robił, będzie odbywało się za pośrednictwem jakiegoś elementu interfejsu: czytanie okien dialogowych, naciskanie przycisków, wybieranie między ikonami itp. Dlatego bardzo ważne jest, aby dokładnie przemyśleć co chcesz zrobić, jak chcesz aby użytkownik postępował i jaki będzie przepływ pracy.

Istnieje kilka pojęć, które należy znać podczas projektowania interfejsu:

-   [Modalne/niemodalne okna dialogowe](http://en.wikipedia.org/wiki/Modal_window): Modalne okno dialogowe pojawia się przed ekranem, zatrzymując działanie głównego okna, zmuszając użytkownika do odpowiedzi na okno dialogowe, podczas gdy niemodalne okno dialogowe nie przerywa pracy w głównym oknie. W niektórych przypadkach pierwsze rozwiązanie jest lepsze, w innych nie.
-   Określenie, co jest wymagane, a co opcjonalne: Upewnij się, że użytkownik wie, co musi zrobić. Oznacz wszystko odpowiednim opisem, użyj podpowiedzi itp.
-   Oddzielanie poleceń od parametrów: Zazwyczaj robi się to za pomocą przycisków i pól wprowadzania tekstu. Użytkownik wie, że kliknięcie przycisku spowoduje akcję, podczas gdy zmiana wartości w polu tekstowym zmieni gdzieś parametr. Jednak w dzisiejszych czasach użytkownicy zwykle dobrze wiedzą, co jest przyciskiem, co jest polem wejściowym itp. Zestaw narzędzi interfejsu, którego używamy, Qt, jest najnowocześniejszym zestawem narzędzi i nie będziemy musieli się zbytnio martwić o wyjaśnianie rzeczy, ponieważ będą one już bardzo zrozumiałe same w sobie.

Tak więc, teraz, gdy dobrze zdefiniowaliśmy, co będziemy robić, nadszedł czas, aby otworzyć projektanta QT. Zaprojektujmy bardzo proste okno dialogowe, takie jak to:

![](images/Qttestdialog.jpg )

Następnie użyjemy tego okna dialogowego w programie FreeCAD, aby utworzyć ładną prostokątną płaszczyznę. Może się okazać, że nie jest to zbyt przydatne do tworzenia ładnych prostokątnych płaszczyzn, ale łatwo będzie je później zmienić, aby robić bardziej złożone rzeczy. Po otwarciu Qt Designer wygląda następująco:

![](images/Qtdesigner-screenshot.jpg )

## Tworzymy okno dialogowe 

Qt Designer jest bardzo prosty w użyciu. Na lewym pasku znajdują się elementy, które można przeciągnąć na widżet. Po prawej stronie znajdują się panele właściwości wyświetlające wszystkie rodzaje edytowalnych właściwości wybranych elementów. Zacznijmy więc od utworzenia nowego widżetu.

1.  Wybieramy \"Dialog bez przycisków\", ponieważ nie chcemy domyślnych przycisków **OK**/**Cancel**.
2.  Potrzebujemy **Etykiety**. Etykiety to proste ciągi tekstowe, które pojawiają się na widżecie, aby poinformować użytkownika końcowego. Jeśli wybierzesz etykietę, zauważysz, że po prawej stronie pojawi się kilka właściwości, które możesz modyfikować, takich jak: styl czcionki, wysokość itp. Przeciągnijmy więc 3 oddzielne etykiety na nasz widżet:
    -   Jedna etykieta dla tytułu
    -   Kolejna etykieta do napisania \"**Wysokość**\"
    -   Kolejna etykieta do napisania \"**Szerokość**\"
3.  Potrzebujemy teraz LineEdits *(a właściwie 2 z nich)*. Przeciągnij dwa z nich na widżet. **LineEdits** to pola tekstowe, które użytkownik końcowy może wypełnić. Potrzebujemy więc jednego LineEdit dla \"Wysokość\" i jednego dla \"Szerokość\". Tutaj również możemy edytować właściwości. Na przykład, dlaczego nie ustawić wartości domyślnej, powiedzmy na przykład: 1.00 dla każdego. W ten sposób, gdy użytkownik zobaczy okno dialogowe, obie wartości będą już wypełnione. Jeśli użytkownik będzie zadowolony, może bezpośrednio nacisnąć przycisk, oszczędzając cenny czas.
4.  Następnie dodajmy przycisk **PushButton**. Jest to przycisk, który użytkownik końcowy będzie musiał nacisnąć po wypełnieniu obu pól.

**Uwaga:** wybraliśmy tutaj bardzo proste kontrolki. Qt ma o wiele więcej opcji, na przykład można użyć **Spinboxes** zamiast **LineEdits** itp. Przyjrzyj się temu, co jest dostępne, zbadaj\... na pewno będziesz miał inne pomysły.

To wszystko, co musimy zrobić w Qt Designer. Na koniec zmieńmy nazwy wszystkich elementów na prostsze, aby łatwiej było je zidentyfikować w naszych skryptach:

![](images/Qtpropeditor.jpg )



## Konwersja naszego okna dialogowego do środowiska Python 

Teraz zapiszmy gdzieś nasz widget. Zostanie on zapisany jako plik .ui, który z łatwością przekonwertujemy na skrypt Pythona za pomocą pyuic. Na Windowsie program pyuic jest dołączony do pyqt *(do sprawdzenia)*, na linuksie prawdopodobnie będziesz musiał zainstalować go osobno z menedżera pakietów *(na systemach opartych na debianie jest on częścią pakietu pyqt4-dev-tools)*. Aby dokonać konwersji, należy otworzyć okno terminala (lub okno wiersza polecenia w systemie Windows), przejść do miejsca, w którym zapisano plik .ui i wydać polecenie: 
```python
pyuic mywidget.ui > mywidget.py
``` W systemie Windows pyuic.py znajduje się w \"C:\\Python27\\Lib\\site-packages\\PyQt4\\uic\\pyuic.py\". Do konwersji należy utworzyć plik wsadowy o nazwie \"compQt4.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" -x %1.ui > %1.py
``` W konsoli DOS wpisz bez rozszerzenia 
```python
compQt4 myUiFile
```

W systemie macOS można pobrać odpowiednią wersję *(tę samą, która jest używana wewnętrznie w FreeCAD 0.19)* QT i Pyside za pomocą następujących poleceń *(wymagany program)*: 
```python
python3 -m pip install pyqt5
python3 -m pip install pySide2
``` Spowoduje to zainstalowanie uic w folderze \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic\", a Designer w \"/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app\". Dla wygody można utworzyć link do uic w /usr/local/bin, aby móc go wywołać po prostu za pomocą uic -g python \... zamiast wpisywania całej ścieżki programu, oraz link do Designera, aby pobrać go w folderze Aplikacje na komputerze Mac za pomocą: 
```python
sudo ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/uic /usr/local/bin
ln -s /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/PySide2/Designer.app /Applications
```

W Linuksie: do zrobienia.

Ponieważ FreeCAD stopniowo odchodził od PyQt po wersji 0.13, na rzecz [PySide](http://qt-project.org/wiki/PySide) *(Wybierz instalację PySide [budowanie PySide](http://pyside.readthedocs.org/en/latest/building/))*, aby plik był oparty na PySide, musisz teraz użyć:


```python
pyside-uic mywidget.ui -o mywidget.py
```

W systemie Windows plik uic.py znajduje się w katalogu \"C:\\Python27\\Lib\\site-packages\\PySide\\scripts\\uic.py\". Aby utworzyć plik wsadowy \"compSide.bat\": 
```python
@"C:\Python27\python" "C:\Python27\Lib\site-packages\PySide\scripts\uic.py" %1.ui > %1.py
``` W konsoli DOS wpisz bez rozszerzenia: 
```python
compSide myUiFile
``` W Linuksie: do zrobienia.

W niektórych systemach program nazywa się pyuic4 zamiast pyuic. Spowoduje to po prostu konwersję pliku .ui na skrypt Pythona. Jeśli otworzymy plik mywidget.py, jego zawartość jest bardzo przejrzysta: 
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
``` Jak widać, ma on bardzo prostą strukturę: tworzona jest klasa o nazwie Ui_Dialog, która przechowuje elementy interfejsu naszego widżetu. Ta klasa ma dwie metody, jedną do konfiguracji widżetu, a drugą do tłumaczenia jego zawartości, co jest częścią ogólnego mechanizmu Qt do tłumaczenia elementów interfejsu. Metoda konfiguracji po prostu tworzy, jeden po drugim, widżety tak, jak zdefiniowaliśmy je w Qt Designer i ustawia ich opcje tak, jak zdecydowaliśmy wcześniej. Następnie cały interfejs zostaje przetłumaczony, a na koniec sloty zostają połączone *(o tym powiem później)*.

Możemy teraz utworzyć nowy widżet i użyć tej klasy do stworzenia jego interfejsu. Możemy już zobaczyć nasz widżet w akcji, umieszczając nasz plik mywidget.py w miejscu, w którym FreeCAD go znajdzie (w katalogu bin FreeCAD lub w dowolnym z podkatalogów Mod), a następnie w interpreterze python FreeCAD wydać polecenie: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` I pojawi się nasze okno dialogowe! Zauważ, że nasz interpreter Python nadal działa, mamy niemodalne okno dialogowe. Tak więc, aby je zamknąć, możemy *(oprócz kliknięcia ikony zamknięcia, oczywiście)* wydać polecenie: 
```python
d.hide()
```

## Sprawiamy, by nasze okno dialogowe robiło coś 

Teraz, gdy możemy pokazywać i ukrywać nasze okno dialogowe, musimy tylko dodać ostatnią część: Sprawić, by coś robiło! Jeśli pobawisz się trochę Qt Designerem, szybko odkryjesz całą sekcję o nazwie \"sygnały i sloty\". Zasadniczo działa to w następujący sposób: elementy na widżetach *(w terminologii Qt te elementy są same w sobie widżetami)* mogą wysyłać sygnały. Sygnały te różnią się w zależności od typu widżetu. Na przykład przycisk może wysyłać sygnał po naciśnięciu i zwolnieniu. Sygnały te mogą być podłączone do slotów, które mogą być specjalnymi funkcjami innych widżetów *(na przykład okno dialogowe ma slot \"zamknij\", do którego można podłączyć sygnał z przycisku zamykania)* lub mogą być funkcjami niestandardowymi. Dokumentacja [PyQt Reference](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) zawiera listę wszystkich widżetów qt, co mogą robić, jakie sygnały mogą wysyłać itd.

To, co tutaj zrobimy, to utworzenie nowej funkcji, która utworzy płaszczyznę na podstawie wysokości i szerokości oraz podłączenie tej funkcji do sygnału naciśnięcia emitowanego przez nasz przycisk \"Utwórz!\". Zacznijmy więc od zaimportowania naszych modułów FreeCAD, umieszczając następującą linię na górze skryptu, gdzie już zaimportowaliśmy QtCore i QtGui: 
```python
import FreeCAD, Part
``` Następnie dodajmy nową funkcję do naszej klasy Ui_Dialog: 
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
``` Następnie musimy poinformować Qt, aby podłączył przycisk do funkcji, umieszczając następującą linię tuż przed QtCore.QMetaObject.connectSlotsByName(Dialog): 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` To, jak widać, łączy sygnał pressed() naszego obiektu create *(przycisk \"Create!\")* ze slotem o nazwie createPlane, który właśnie zdefiniowaliśmy. To wszystko! Teraz, jako ostatni akcent, możemy dodać małą funkcję do tworzenia okna dialogowego, która będzie łatwiejsza do wywołania. Dodajmy ten kod poza klasą Ui_Dialog: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` *(Przypomnienie Pythona: metoda \_\_init\_\_ klasy jest automatycznie wykonywana za każdym razem, gdy tworzony jest nowy obiekt)*! Następnie, z FreeCAD, musimy tylko zrobić: 
```python
import mywidget
myDialog = mywidget.plane()
``` To wszystko\... Teraz możesz spróbować różnych rzeczy, takich jak na przykład wstawianie widżetu do interfejsu FreeCAD *(zobacz stronę [wycinki kodu](Code_snippets/pl.md))* lub tworzenie znacznie bardziej zaawansowanych narzędzi niestandardowych, używając innych elementów na widżecie.

## Kompletny skrypt 

To jest kompletny skrypt, dla porównania: 
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



## Więcej przykładów 

-   [Tworzenie dialogów z różnymi widżetami](Dialog_creation_with_various_widgets/pl.md) with `QPushButton`, `QLineEdit`, `QCheckBox`, `QRadioButton`, and others.
-   [Tworzenie dialogów odczyt i zapis plików](Dialog_creation_reading_and_writing_files/pl.md) with `QFileDialog`.
-   [Tworzenie okna dialogowego ustawienie kolorów](Dialog_creation_setting_colors/pl.md) with `QColorDialog`.
-   [Tworzenie dialogu grafika i animowany GIF](Dialog_creation_image_and_animated_GIF/pl.md) with `QLabel` and `QMovie`.
-   [PySide przydatne wycinki](PySide_usage_snippets/pl.md).
-   [Przykłady Qt](Qt_Example/pl.md)



## Istotne odnośniki internetowe 

-   [Podręcznik:Tworzenie narzędzi interfejsu](Manual:Creating_interface_tools/pl.md)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Dialog creation/pl
