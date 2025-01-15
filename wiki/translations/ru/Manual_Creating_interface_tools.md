# Manual:Creating interface tools/ru
{{Manual:TOC}}

В последних двух главах мы видели как [создать геометрию Part](Manual:Creating_and_manipulating_geometry/ru.md) и [создавать параметрический объекты](Manual:Creating_parametric_objects/ru.md). Чтобы получить полный контроль за FreeCAD, осталось одно: создание инструментов, взаимодействующими с пользователем.


<div class="mw-translate-fuzzy">

В большинстве случаев не стоит подвергать пользователя испытанию, когда объект конструируется с нулевыми значениями, как мы делали с прямоугольником в предыдущей главе, и затем спрашивать пользователя заполнить значения Height и Width в панели Properties. Это работает для очень малого числа объектов, но становится утомительным когда надо создать их во множестве. Лучше иметь возможность задавать Height и Width при создании прямоугольника.


</div>


<div class="mw-translate-fuzzy">

Python предоставляет базовые инструменты для ввода пользовательского текста на экране:


</div>

text = raw_input("Height of the rectangle?")
print("The entered height is ",text)

Тем не менее, для этого нужна запущенная консоль Python, и при запуске нашего кода как макроса мы не всегда уверены, что консоль Python работает на пользовательской машине.


<div class="mw-translate-fuzzy">

[Графический интерфейс пользователя](https://ru.wikipedia.org/wiki/Графический_интерфейс_пользователя), или ГИП, GUI, то есть все части FreeCAD, отображаемые на экране (меню, панели инструментов, окно трёхмерного вида и так далее) как раз для этого: взаимодействия с пользователем. Интерфейс FreeCAD построен на [Qt](https://ru.wikipedia.org/wiki/Qt), широко распространённая библиотека ГИП, предоставляющая широкий набор инструментов вроде диалоговых боксов, кнопок, панелей, меток, полей ввода, или ниспадающих меню. В целом они все называются \"виджетами\".


</div>


<div class="mw-translate-fuzzy">

Инструменты Qt очень легко использовать из Python, благодаря модулю Python, называемому [Pyside](https://ru.wikipedia.org/wiki/PySide) (есть и другие модули Python для взаимодействия с Qt из Python). Этот модуль обеспечивает создание и взаимодействовать с виджетами, считывать что пользователи делают с ними (что вписывают в текстовые боксы) или делать что-то когда, например, нажимается кнопка.


</div>

One of the key advantages of Qt is its cross-platform compatibility, enabling FreeCAD to run seamlessly on different operating systems like Windows, macOS, and Linux. Additionally, Qt's flexibility makes it easy for developers to extend or customize FreeCAD's interface, either by creating new toolbars and menus or by building entirely new modules that integrate into the software. This adaptability ensures that FreeCAD remains both user-friendly and highly extensible.

For users interested in scripting or developing new tools, FreeCAD\'s Python API also provides access to many Qt features. This means you can not only automate tasks but also create custom widgets or dialogs that integrate directly into the FreeCAD environment.

The Qt tools are very easy to use from Python, thanks to a Python module called [PySide](https://en.wikipedia.org/wiki/PySide). PySide is the official Python binding for the Qt library, providing a seamless way to create and interact with widgets programmatically. It allows developers to design interfaces, manage user inputs (such as reading text from input boxes), and define actions based on user interactions, such as responding to a button press. Using PySide, you can build custom dialog boxes, menus, and toolbars directly within FreeCAD, extending its functionality in a way that integrates smoothly with its existing interface.

PySide makes it easy to connect user actions to specific functions in your code. For example, you can set up a button so that when it's pressed, it triggers a script to execute a command or modify an object in the 3D view. This interactive capability opens up endless possibilities for customizing workflows and automating repetitive tasks.


<div class="mw-translate-fuzzy">

В Qt так же есть другой интересный инструмент, называемый [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html), полностью встроенный в большое приложение [Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator). Он позволяет проектировать диалоговые боксы и интерфейсные панели графически, вместо того чтобы делать это вручную. В этой главе мы будем использовать Qt Creator для проектирование панельного виджета, который использует панель **Task** FreeCAD. Так что Вам надо скачать и установить Qt Creator с их [официальной страницы](https://www.qt.io/ide/), если Вы на Windows или Mac (в Linux он обычно доступен из менеджера приложений).


</div>

В следующем примере мы сначала с помощью Qt Creator создадим панель, которая будет запрашивать длину, ширину и высоту, затем создадим вокруг неё класс Python, который читает введённые значения, и создадим куб с данными размерами. Класс Python затем будет использоваться FreeCAD для показа и управления панели задач:

![](images/Exercise_python_07.jpg )


<div class="mw-translate-fuzzy">

Начнём с создания виджета. Запустите Qt Creator, затем меню **File → New File or Project → Files and Classes → Qt → Qt Designer Form → Dialog without buttons**. Кликните **Next**, задайте имя файла для сохранения, кликните **Next**, оставьте все поля проекта со значениями по умолчанию (\"\"), затем **Create**. Система задач FreeCAD автоматически добавит кнопки OK/Cancel, поэтому мы выбрали здесь диалог без кнопок.


</div>

![](images/Exercise_python_06.jpg )


<div class="mw-translate-fuzzy">

-   Найдём в списке на левой панели **Label**, и перетащим её на полотно нашего виджета. Дважды кликнем размещённую метку, и изменим её текст на **Length**.
-   Правым кликом на холсте виджета выберем **Lay out→ Lay out in a Grid**. Это превратит наш виджет в сетку с пока ещё только одной ячейкой, занятой нашей первой меткой. Мы теперь можем добавить следующий элемент слева, справа, сверху или снизу от нашей первой метки, и сетка автоматически расширится.
-   Добавим ещё две метки под первой, и изменим их текст на Width и Height:


</div>

![](images/Exercise_python_08.jpg )


<div class="mw-translate-fuzzy">

-   Теперь поместим 3 виджета **Double Spin Box** вблизи наших меток Length, Width и Height. Для каждой из них в нижней правой панели, которые показывают доступные установки для выбранных виджетов, найдите **Suffix** и установите суффикс в **mm**. У FreeCADа есть более совершенный виджет, который может поддерживать различные единицы, но он не доступен в Qt Creator по умолчанию (но может быть [вкомпилирован](Compile_on_Linux/Unix/ru#Qt_designer_plugin.md)), так что теперь мы будем использовать станданртный Double Spin Box, и мы добавим суффикс \"mm\", чтобы пользователи знали, в каких единицах они работают:


</div>

![](images/Exercise_python_09.jpg )


<div class="mw-translate-fuzzy">

-   Теперь наш виджет готов, осталось убедиться в последней вещи. Поскольку FreeCAD должен иметь доступ к нему и читать значения Length, Width и Height, нам надо дать этим виджетам подходящие имена, чтобы мы могли легко получить их из FreeCAD. Кликните каждый из этих полей ввода, и в верхнем правом окне дважды кликните их Object Name, и измените его во что-то лёгкое для запоминания, например: BoxLength, BoxWidth и BoxHeight:


</div>

![](images/Exercise_python_10.jpg )

-   Сохраните файл, и можете закрыть Qt Creator, остальное будет сделано в Python.
-   Откройте FreeCAD и создайте новый макрос из меню **Макросы → Макрос**
-   Вставьте следующий код. Убедитесь, что Вы изменили путь к файлу на тот, где вы сохранили файл .ui, созданный в QtCreator:


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


<div class="mw-translate-fuzzy">

В вышеуказанном коде мы использовали общую функцию (PySideUic.loadUi) из модуля FreeCADGui. Эта функция загружает файл .ui, создаёт из него виджет Qt, и сопоставляет имена, так что мы можем легко добираться до подвиджетов по их именам (пример: self.form.BoxLength).


</div>

Функция \"accept\" это так же удобство, предлагаемое Qt. Когда в диалоге есть кнопка \"OK\" (которая есть по умолчанию при использовании панели задач FreeCAD), любая функция, называемая \"accept\" автоматически выполняется когда нажата кнопка \"OK\". Соответственно, Вы можете так же добавить функцию \"reject\", которая будет исполняться когда будет нажата кнопка \"Cancel\". В нашем случае мы опустили эту функцию, так что нажатие \"Cancel\" обрабатывается по умолчанию (ничего не делает и закрывает диалог).

Если мы создадим функции accept или reject, их действие по умолчанию (ничего не делать и закрыть) больше не сработает. Так что нам надо закрывать панель Task самостоятельно. Это делается с помощью:


```python
FreeCADGui.Control.closeDialog() 
```

Когда у нас есть BoxTaskPanel, в которой: 1- виджет \"self.form\", и 2- при необходимости функции accept и reject, мы можем открыть с её помощью панель задач, что делается этими двумя последними строчками:


```python
panel = BoxTaskPanel()
 FreeCADGui.Control.showDialog(panel)
```


<div class="mw-translate-fuzzy">

Заметьте, что создаваемый PySideUic.loadUi виджет не специффичен для FreeCAD, это стандартный виджет Qt, который может использоваться в других инструментах Qt. Например, мы можем показывать отдельное диалоговое окно с его помощью. Попробуем это в консоли Python FreeCADа (разумеется, используя правильный путь к вашему файлу .ui):


</div>


```python
from PySide import QtGui
 w = FreeCADGui.PySideUic.loadUi("C:\Users\yorik\Documents\dialog.ui")
 w.show()
```


<div class="mw-translate-fuzzy">

Разумеется, мы не добавляем в наш диалог никакую кнопку \"OK\" или \"Cancel\", поскольку сделан для использования из панели Task FreeCADа, которая содержит эти кнопки. Так что этот диалог нельзя закрыть (кроме как нажав кнопку закрытия окна). Но функция show() создаёт немодальный диалог, то есть он не блокирует остальной интерфейс. Поэтому, когда диалог всё ещё открыт, мы можем читать значения полей:


</div>


```python
w.BoxHeight.value() 
```

Это очень полезно для тестирования.

В итоге, не забудьте, что в FreeCAD Wiki гораздо больше документации об использовании виджетов Qt, в секции [Python Scripting](Power_users_hub/ru.md), которая содержит [руководство по созданию диалогов](Dialog_creation/ru.md), специальное [руководство по PySide](PySide/ru.md), которое шире описывает тему.

## Связанные ссылки 

-   [Документация Qt Creator](https://en.wikipedia.org/wiki/Qt_Creator)
-   [Установка Qt Creator](https://www.qt.io/ide/)
-   [Документация по скриптам на Python в FreeCAD](Power_users_hub/ru.md)
-   [Учебник создания диалогов FreeCAD](Dialog_creation/ru.md)
-   [Учебник PySide для FreeCAD](PySide/ru.md)
-   [Документация PySide](http://srinikom.github.io/pyside-docs/index.html)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Python Code](Category_Python%20Code.md) > Manual:Creating interface tools/ru
