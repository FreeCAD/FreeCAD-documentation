# Line drawing function/ru




{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

На этой странице показано лего можно создать продвинутую фукнкциональность в Python. В данном примере , мы создадим новый инструмент, для рисования линии. Этот инструмент может быть свзае с командой FreeCAD, и эта команда может быть вызвана из любого элемента интерфейса, таком как как опция меню или кнопка на панели инструментов.


</div>

## Основной скрипт 

В начале мы напишем сценарий содержащий всю нашу функциональность. Затем, мы сохраним его в файле и импортируем в FreeCAD, чтобы все классы и функции были доступны. Запустите текстовый редактор, в котором вам наиболее удобно работать и введите следующие строки:


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


{{Top}}

## Подробное описание 


```python
import Part, FreeCADGui
from pivy.coin import *
```


<div class="mw-translate-fuzzy">

В Python, когда вам требуется использовать функции из другого модуля, вам нужно импортировать его. В нашем случае, нам нужны функции из [Модуля Деталей](Part_Workbench/ru.md), для создания линии, и из Gui модуля (FreeCADGui), для доступа к 3D виду. Нам также нужно полное содержание библиотеки coin, так мы сможем напрямую использовать все coin объекта такие как SoMouseButtonEvent, и.т.д\...


</div>


```python
class line:
```

Здесь мы задаем наш основной класс. Почему мы используем класс а не функцию? Причина в том чтобы нащ инструмент оставался \"живым\" когда мы ждем что пользователь нажмет на экран. Функция завершится когда её задача будет выполнена, но объект (класс заданый как объект) остается живым пока не будет уничтожен.


```python
"""This class will create a line after the user clicked 2 points on the screen"""
```


<div class="mw-translate-fuzzy">

В Python, каждый класс или функция могут обладать строкой описания. Это особенно полезно в FreeCAD, потому что когда вы будете вызывать этот класс через интепритатор, строка описания будет отображатся в виде всплывающей подсказки.


</div>


```python
def __init__(self):
```


<div class="mw-translate-fuzzy">

Python класс всегда может содержать \_\_init\_\_ функцию, которая выполняется когда класс вызывается для создания объекта. Таким образом, мы положим сюда всё что мы хотим чтобы случилось, когда запустится наш инструмент \"линия\".


</div>


```python
self.view = FreeCADGui.ActiveDocument.ActiveView
```


<div class="mw-translate-fuzzy">

В классе, вам обычно нужно добавить *self.* перед именем переменной, для того чтобы получить легкий доступ к функциям в и вне класса. Здесь мы используем self.view для доступа к управлению активным 3D видом.


</div>


```python
self.stack = []
```


<div class="mw-translate-fuzzy">

Здесь мы создаем простой список содержащий 3D точки, переданные функцией getpoint.


</div>


```python
self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)
```


<div class="mw-translate-fuzzy">

Это важная часть: Посколько это фактически [coin3D](http://www.coin3d.org/) сцена(в смысле окно отображения), FreeCAD использует механизм обратного вызова coin, что позваляет вызывать функцию каждый раз когда на сцене что-то происходит. В нашем случае, мы создаем обратный вызов для события [SoMouseButtonEvent](http://doc.coin3d.org/Coin/group__events.html) , и мы привязываем его getpoint функции. Теперь, каждый раз когда клавиша мыши будет нажата или отпущена, будет выполнятся функция getpoint.


</div>


<div class="mw-translate-fuzzy">

Замети также что существует альтернативна addEventCallbackPivy(), зовется addEventCallback() которая обходится без использование pivy. Но так как pivy это очень эффективный и естественный способ получить доступ к любой части coin сцены, он гораздо лучше для использования так как вы можете!


</div>


{{Top}}


```python
def getpoint(self, event_cb):
```


<div class="mw-translate-fuzzy">

Теперь вы задали getpoint функцию, которая выполняется когда клавиша мыши щелкает по окну 3D вида. Эта функция будет получать аргумент, который мы назовем event\_cb. В время обратного вызова мы можем получить доступ к объекту события, который содержит некоторую информацию (информационный режим [описан здесь](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md)).


</div>


```python
if event.getState() == SoMouseButtonEvent.DOWN:
```


<div class="mw-translate-fuzzy">

Getpoint функция будет вызыватся когда клавиши мыши будет нажата или отжата. Но мы хотим фиксировать 3D точку только когда нажимаем (в противном случае мы мы можем получить две 3D точки очень близко друг от друга). Так что мы проверяем это.


</div>


```python
pos = event.getPosition()
```


<div class="mw-translate-fuzzy">

Здесь мы получаем координаты курсора мыши


</div>


```python
point = self.view.getPoint(pos[0], pos[1])
```


<div class="mw-translate-fuzzy">

Эта функция дает нам FreeCAD вектор (x,y,z) содержащий точку лежащую в фокальной плоскости, т.е. под вашим курсором. Если вы находитесь в режиме камеры, изображается луч идущий из камеры проходящий через курсор мыши, и достигающий фокальной плоскости. Это наша 3D точка. Если мы находимся в режиме ортогонального отображения, луч паралелен направлению вида.


</div>


```python
self.stack.append(point)
```


<div class="mw-translate-fuzzy">

Мы добавляем новую точку в stack


</div>


```python
if len(self.stack) == 2:
```

Если у вас, уже достаточное количество точек? если да, тогда давайте рисовать линию!


```python
l = Part.LineSegment(self.stack[0], self.stack[1])
```


<div class="mw-translate-fuzzy">

Здесь мы используем Line() функцию из [Модуля Деталей](Part_Workbench/ru.md) которая создает линию по двум FreeCAD векторам. Все что мы создаем и модифицируем внутри модуля Деталей, остается в модуле(Part module). Так что, до сих пор, когда мы создавали Line Part. Она не была привязана к какому либо объекту в нашем документе, поэтому ничего и не отображалось на экране.


</div>


```python
shape = l.toShape()
```


<div class="mw-translate-fuzzy">

FreeCAD документ может принимать только формы(shapes) из модуля Деталей. Формы являются наиболее универсальным типом из модуля Деталей. Таким образом, мы должны преобразовать нашу линию в форму и добавить её в документ.


</div>


```python
Part.show(shape)
```


<div class="mw-translate-fuzzy">

Модуль деталей обладает очень удобной функцией show() ,которая создает новый объект в документе и привязывает форму к нему. Мы таже могли создать новый объект и привязать к нему форму вручную.


</div>


```python
self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
```


<div class="mw-translate-fuzzy">

Теперь, когда мы закончили нашу линию, давайте уберем механизм обратного вызова, который потребляет драгоценные циклы ЦПУ.


</div>


{{Top}}

## Тестирвание сценария 


<div class="mw-translate-fuzzy">

Теперь, давайте сохраним наш сценарий где нибудь где FreeCAD python интепритатор сможет его найти. Когда импортируются модули, интепритатор просматривает следующие места: директорию куда установлен python,FreeCAD bin директорию, и все папки FreeCAD модулей. Так что, лучшим решением будет создать новую папку в одной из FreeCAD [Mod папках](Installing_more_workbenches.md), и сохранит наш сценарий в ней. Например, давайте создадим папку \"MyScripts\" , и сохраним наш сценарий как \"exercise.py\".


</div>


<div class="mw-translate-fuzzy">

Теперь, когда все готово, давайте запустим FreeCAD, создадим новый документ, и введем в python интерпритатор:


</div>


```python
import exercise
```


<div class="mw-translate-fuzzy">

Если сообщений об ошибке не появится, это означает, что наш учебный сценарий был загружен. Теперь мы можем проверить его содержимое:


</div>


```python
dir(exercise)
```


<div class="mw-translate-fuzzy">

Команда dir() встроенная python которая выдает список содержащегося в модуле. Мы можем видеть здесь нас ждет, наш класс line(). Теперь давайте протестируем его:


</div>


```python
'line' in dir(exercise)
```

Приступим к тестированию:


```python
exercise.line()
```


<div class="mw-translate-fuzzy">

Затем, щелкнем два раза на 3D виде, и бинго, вот наша линия! Чтобы сделать это снова , просто опять введите exercise.line(), и ещё раз, и ещё раз\... Чувствуете себе прекрасно, не так ли?


</div>


{{Top}}

## Регистрация сценария 


<div class="mw-translate-fuzzy">

Теперь, для нашего нового инструмента \"линия\" будет здорово, если он будет обладать кнопкой в интерфейсе, так чтобы нам не нужно было его каждый раз вводить. Простейший путь это преобразовать наш новый каталог MyScripts в полноценнный FreeCAD инструментарий(workbench). Это просто, все что нужно это поместить в файл зовущийся **InitGui.py** внутрь вашей MyScripts папки. InitGui.py будет содержать инструкции создания нового инструментария, м добавлять наш новый инструмент в него. Кроме того мы должны трансформировать код нашего примера, так чтобы инструмент line() был признан как официальная FreeCAD команда. Начнем с создания InitGui.py файла, и запишем в него следующий код:


</div>


```python
class MyWorkbench (Workbench):

    MenuText = "MyScripts"

    def Initialize(self):
        import exercise
        commandslist = ["line"]
        self.appendToolbar("My Scripts", commandslist)

Gui.addWorkbench(MyWorkbench())
```


<div class="mw-translate-fuzzy">

К этому моменту , я думаю, вы должны понимать сценарий выше: Мы создали новый класс назвали его MyWorkbench, мы задаем заглавие(MenuText), и задаем Initialize() функцию, которая будет выполняться когда инструментарий будт загружен в FreeCAD. В этой функции, мы загружаем вск что содержится в нашем exercise файле, и добавляем в FreeCAD команды найденные внутри списка команд(commandlist). Затем, мы создаем панель инструментов названую \"My Scripts\" и сопоставляем наш список команд с ней. Конечно, сейчас у нас есть только один инструмент, так как наш список команд содержит один элемент. Затем, когда наш инструментарий готов, мы добавляем его в основной(главный) интерфейс.


</div>


<div class="mw-translate-fuzzy">

Но это пока не будет работать, потому что FreeCAD команда для работы должна быть отформатирована определенным образом. Так что нам нужно преобразовать(доработать) наш line() инструмент. Наш новый exercise.py сценарий будет выглядеть следующим образом:


</div>


```python
import FreeCADGui, Part
from pivy.coin import *

class line:

    """This class will create a line after the user clicked 2 points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[0], self.stack[1])
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('line', line())
```


<div class="mw-translate-fuzzy">

То, что мы сделали здесь является преобразованием нашей \_\_init\_\_() функции в Activated() функцию, потому что, когда FreeCAD команды выполняются, они автоматически выполняют Activated() функцию. Мы также добавили функцию GetResources(), которая сообщает FreeCAD, где он может найти значок инструмента, и каким будет название и подсказка нашего инструмента. Любой JPG, PNG или SVG изображения будут работать, как иконка, они могут быть любого размера, но лучше использовать размер, близкий к последним аспектам, как 16x16, 24x24 или 32x32. Затем, мы добавили line() класс в качестве официального команды FreeCAD с AddCommand() методом.


</div>


<div class="mw-translate-fuzzy">

Это всё, теперь вам нужно перезапустить FreeCAD и вы получите новый хороший инструментарий с нашим новым инструментом линии!


</div>


{{Top}}

## Вы хотите большего? 


<div class="mw-translate-fuzzy">

Если вам понравился этот пример, почему не попытаться улучшить этот маленький инструмент? Существует множесво вещей которые нужно сделать, как например:

-   Добавить обратную связь с пользователем: до сих пор мы делали очень голый инструмент, пользователь может потерятся при его использовании. Таким образом мы могли бы добавить обратную связь, сообщающую ему что делать дальше. Например, мы можем выводит сообщения в FreeCAD консоль. Загляните в FreeCAD.Console модуль
-   Добавить возможность вводить координаты 3D точек вручную. Посмотрите, на пример, python input() функцию
-   Добавить способность добавлять более двух точек
-   Добавить события для других вещей: сейчас мы только проверяем события кнопок мыши, что если мы хотели бы также сделать что-то когда мышь перемещается, например отображать текущие координаты?
-   Давать имя созданному объекту

Не стесняйтесь писать ваши вопросы или идеи на [forum](http://forum.freecadweb.org/)!


</div>

Don\'t hesitate to ask questions or share ideas on the [forum](https://forum.freecadweb.org/)! {{Top}} {{Powerdocnavi}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
