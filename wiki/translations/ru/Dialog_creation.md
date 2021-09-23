# Dialog creation/ru



{{TOCright}}

## Введение

На этой странице мы покажем как создать простой графический интерфейс с помощью [Qt Designer](http://qt-project.org/doc/qt-4.8/designer-manual.html), официальный инструмент Qt для создания интерфейсов, диалог будет сковертирован в код [Python](Python/ru.md), затем использован внутри FreeCAD. Мы будем полагать что пользователь знает в общих чертах как редактировать и запускать [Python](Python/ru.md).

In this example, the entire interface is defined in [Python](Python.md). Although this is possible for small interfaces, for larger interfaces the recommendation is to load the created {{FileName|.ui}} files directly into the program. See [Interface creation with UI files](Interface_creation_with_UI_files.md) for more information.

<img alt="" src=images/FreeCAD_creating_interfaces.svg  style="width:600px;"> *Two general methods to create interfaces, by including the interface in the Python file, or by using `.ui* files.`

## Проектирование диалога 

В приложениях САПР очень важно проектирование хорошего Пользовательского Интерфейса. Практически всё, что пользователь будет делать, делается через части интерфейса: чтение диалоговых окон, нажатие кнопок, выбор между иконками, и.т.д. Так что очень важно тщательно подумать, что вы хотите сделать, как вы хотите чтобы пользователь повел себя и каков будет рабочий процесс с вашими действиями.

Известно несколько понятий, от том как проектировать интерфейс:

-   [Modal/non-modal dialogs](http://en.wikipedia.org/wiki/Modal_window): Модальное окно появляется поверх всех окон, останавливая действия происходящие в главном окне приложения, заставляя пользователя отвечать в диалоговом окне, тогда как не модальный диалог не останавливает вас от работы в главном окне. В некоторых случаях лучше первое, в других нет.
-   Определение того, что требуется и что считается дополнительны: Убедитесь что пользователь знает что он должен делать. Ставте на все метки с описанием, используйте подсказки, и.т.д.
-   Отделяйте команды от параметров: Это обычно делается с помощью кнопок и полей текстовых ввода. Пользователь знает что нажатие кнопки будет производить действие тогда как изменение значения внутри текстового поля где-то будет изменять параметр. В настоящие время, однако, пользователи обычно отлично знают что есть кнопка, а что есть поле ввода, и.т.д. В качестве графического инструментария используется, Qt, это современный инструментарий, и мы не должны больш беспокоится о создании ясности, так как он уже сам по себе очень ясный/понятный интерфейс.

Таким образом, теперь когда мы четко определили что должны делать, откройте qt designer. Давайте спроектируем очень простой диалог, как здесь:

![](images/Qttestdialog.jpg )

Мы будем использовать этот диалог в FreeCAD для создания хороших прямоугольных плоскосте. Вам может показаться что это не очень удобно для создания прямоугольных плоскосте, но его легко можно изменить позже, чтобы делать более сложные вещи. Когда вы откроете Qt Designer, он выглядит следующим образом:

![](images/Qtdesigner-screenshot.jpg )

## Создание диалога 

Qt Designer очень прост в использовании. На левой панели есть элименты которые можно перетащить на ваш виджет. На правой стороне находится панель свойств отображающая все виды редактируемых свойств, выбранного элемента. Так что начните с создания нового виджета.

1.  Выберете \"Диалог без кнопок\", так как мы не хотим кнопки по умолчанию **OK**/**Cancel**.
2.  Нам нужны *\'Labels*. Labels (этикетки) - это просто тексты которые появляются на вашем виджете, чтобы проинформировать пользователя. Если вы выбираете этикетку, на правой стороне появляются свойства которые вы можете поменять, если вы хотите, такие как стиль шрифта, высота и.т.д. Так что перетащите на ваш виджет 3 этикетки:
    -   Одна для заголовка,
    -   Одно для надписи \"Height\"
    -   Одна для записи \"Width\".
3.  Теперь нам нужны LineEdits. Перетащите два из них на виджет. **LineEdits** это текстовые поля, которые конечный пользователь может заполнить. Нам нужен один LineEdit для *Height* и один для *Width*. Здесь мы тоже можем редактировать свойства. Например, почему бы не установить значения по умолчанию, например: 1.00 для каждого. Таким образом, пользователь увидит диалог, где оба значения уже заполнены. Если он удовлетворён, он может прямо нажать кнопку, сохраняя время.
4.  Далее добавим **PushButton**. Это кнопка, которую конечному пользователю следует нажать после заполнения обоих полей.

**Заметьте:** мы выбрали очень просто управление. В Qt гораздо больше функций, например, например вы можете использовать Spinboxes вместо LineEdits, и.т.д\... Обратите внимание на то что доступно, у вас несомнено появятся другие идеи.

Вот и все, что мы должны сделать в Qt Designer. Последнее, давайте переименуем все наши элементы дав им более простые имена, так что будет легче определять их в нашем сценарии:

![](images/Qtpropeditor.jpg )

## Конвертация нашего диалога в python 

Теперь сохраните ваш виджет где-нибудь. Он будет сохранен как .ui файл, который мы легко преобразуем в python сценарий с помощью pyuic. В windows, программа pyuic связанна с pyqt (должно быть проверено), на linux вам вероятно нужно будет установить его отдельно в вашем пакетном менеджере (для debian-based систем, это часть пакета pyqt4-dev-tools). Для преобразования, вам необходимо открыть окно терминала (или окно командной строки в windows), переместитесь туда где вы сохранили ваш .ui файл и введите: 
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

На некоторых системах программа называется pyuic4 вместо pyuic. Это просто сконвертирует файл .ui файл в сценарий python. Если мы откроем файл mywidget.py, его содержание очень легко понять: 
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
``` Как вы видете, он обладает очень простым устройством: созданный класс называемый Ui\_Dialog, он содержит все элементы интерфейса нашего виджета. Этот класс обладает двумя методами, один для создания виджета, и одни для перевода его содержания, которая является частью механизма Qt для перевода элементов интерфейса. Метод установки(setup method) просто создает один за другим, виджетв так как мы задали их в Qt Designer, и задает их настройки так как мы определили ранее. Затем, весь инструмент будет переведен, и наконец, подключаются слоты (мы поговорим об этом позже).

Теперь мы можем создать новый виджет и использовать этот класс для созданияего интерфейса. Мы уже можем увидеть наш виджет в действии, поместив наш файл mywidget.py в место где FreeCAD сможет найти его (в FreeCAD в паку bin, или в любую Mod поддиректорию), и ввести в интерпретаторе FreeCAD python: 
```python
from PySide import QtGui
import mywidget
d = QtGui.QWidget()
d.ui = mywidget.Ui_Dialog()
d.ui.setupUi(d)
d.show()
``` И наш диалог появится! Заметим, что наш интерпретатор по прежнему работает, т.е у нас не модальный диалог. Так что, закроем его, мы можем (конечно, помимо того как щелкнуть на иконке закрытия) ввести: 
```python
d.hide()
```

## Делаем так чтобы наш диалог делал что-нибудь 

Теперь когда мы можем показать или скрыть наш диалог, на осталось добавить последнюю часть:Чтобы оно что-то делало! Если вы немного поиграетесь с Qt designer, вы быстро обнаружите целый раздел под название \"сигналы и слоты\". В основном, это работает следующим образом: элемент на вашем виджете (в Qt терминалогии, эти элементы сами по себе являются виджетами) может отправить сигнал. Этот сигнал отличаются в зависимости от типа виджета. Например, кнопка может подать сигнал при нажатии, и когда она будет отпущена. Этот сигнал может быть соединен со слотами, которые могут быть специальными функциями других виджетов(например диалог обладающий слотом \"закрыть\" который можно подключить к сигналу от кнопки закрытия), или это могут быть пользовательские функции. [PyQt Reference Documentation](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) список всех qt виджетов, что они делают, какие сигналы могут отправлять и.т.д\...

Что мы будем делать здесь, создадим новую функцию , которая создает плоскость основываясь на её длине и ширине, и подключим эту функцию к сигналу нажатия испускаемому нашей кнопкой \"Create!\" . Так что , давайте начнем с импорта наших модулейr FreeCAD, палагая следующую строку введенной в начале нашего сценария, где мы уже импортировали QtCore и QtGui: 
```python
import FreeCAD, Part
``` Затем , давайте добавим новую функцию в наш класс Ui\_Dialog: 
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
``` Потом, нам нужно сообщить Qt о подключении функции к кнопке, разместив следующую строчку перед QtCore.QMetaObject.connectSlotsByName(Dialog): 
```python
QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.createPlane)
``` как вы видете, подключение сигнала pressed() от нашего созданного объекта (кнопка \"Create!\"), к слоту названому createPlane, который мы только что определили. И это всё!!Теперь,финальный штрих, мы можем добавить маленькую функцию в создание диалога, его легче будет вызвать. Вне класса Ui\_Dialog, давайте добавим этот код: 
```python
class plane():
   def __init__(self):
       self.d = QtGui.QWidget()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self.d)
       self.d.show()
``` (Python reminder: the \_\_init\_\_ method of a class is automatically executed whenever a new object is created!)

Затем , в FreeCAD, нам необходимо сделать только: 
```python
import mywidget
myDialog = mywidget.plane()
``` \"Это все ребята\"\... Теперь вы можете попробовать разные вещи, например как вставить ваш виджет в FreeCAD интерфейс (смотри страницу [Отрывки кода](Code_snippets/ru.md) ), или создать более продвинутый пользовательский инструмент, используя другие элементы в вашем виджете.

## Готовый сценарий 

Это полный сценарий, для справки: 
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

-   [Manual:Creating interface tools](Manual:Creating_interface_tools.md)
-   [Interface creation with UI files](Interface_creation_with_UI_files.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
