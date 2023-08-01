# Selection methods/ru
## Обзор

[Методы выбора](Selection_methods/ru.md) в FreeCAD позволяют выбирать объекты в [интерфейсе FreeCAD](Interface/ru.md): таких как [3D view](3D_view/ru.md), [древе проекта](Tree_view/ru.md), [вид выбора](Selection_view/ru.md) и других диалогах. Некоторые методы выбора зависят от конкретной рабочей среды и задокументированы в соответствующей документации по рабочей среде.



## Трёхмерный вид 


<div class="mw-translate-fuzzy">

В [трёхмерном виде](3D_view/ru.md) есть различные способы выбора объектов с помощью указателя мыши.


</div>



### Простое выделение 


<div class="mw-translate-fuzzy">

Простой выбор с помощью мыши (по умолчанию щелчок левой кнопкой мыши) и предварительный выбор (наведение курсора) описаны на странице [навигация с помощью мыши](Mouse_Model/ru.md).


</div>



### Повторные клики 


<div class="mw-translate-fuzzy">

Первый щелчок выбирает подэлемент (вершину, кромку или грань) объекта под курсором мыши. Второй щелчок выделяет весь объект. <small>(v0.18)</small> 


</div>


<div class="mw-translate-fuzzy">

Третий щелчок расширяет выделение на объект-контейнер ([PartDesign Body](PartDesign_Body/ru.md), [Std Part](Std_Part/ru.md) и другие). Дальнейшие щелчки расширяют выбор вверх по цепочке контейнеров. <small>(v0.19)</small> 


</div>



### Команды выделения 


<div class="mw-translate-fuzzy">

Выбор перетаскиванием мышью для выбора нескольких объектов или подэлементов (вершин или граней) доступен с использованием [Std SelectAll](Std_SelectAll/ru.md), [Std BoxSelection](Std_BoxSelection/ru.md), [Part BoxSelection](Part_BoxSelection/ru.md) и [Std BoxElementSelection](Std_BoxElementSelection/ru.md).


</div>



## Панель выделения 

[Панель выделения](Selection_view/ru.md) показывает имена выбираемых объектов, включая их полное имя внутри объекта, например `Unnamed#Body.Box001.Face17`.

It also allows to perform some actions like [Std ViewFitSelection](Std_ViewFitSelection.md), and sending the object to the [Python console](Python_console.md).



### Экспорт объектов 

*This should be in the [selection view](selection_view.md) page.*

Выберите любой сложный объект, например, [PartDesign Body](PartDesign_Body/ru.md) или [Std Part](Std_Part/ru.md), затем в [панели выделения](selection_view/ru.md) снова выберите объект, а затем нажмите **Ctrl** + **C** на клавиатуре, чтобы открыть диалоговое окно **Выбор объекта**. Это позволяет копировать выбранный объект вместе со всеми или только некоторыми объектами зависимостей этого объекта. Например, для [Std Part](Std_Part/ru.md) возможные объекты для выбора включают сам [Std Part](Std_Part/ru.md), его начало координат, его три базовые оси (XYZ) и его три базовые плоскости (XY, YZ, XZ).

После нажатия **OK** выбранные объекты копируются в память, а затем могут быть вставлены в документ только для дублирования этих объектов.

![](images/ObjectSelection.png )



*Диалог выбора объекта, запускаемый из [панель выделения](Selection_view/ru.md).*



## Древо проекта 

В [древе проекта](tree_view/ru.md) элементы можно выбирать или отменять по одному, удерживая клавишу **Ctrl** и щелкая мышью.

Ряд элементов можно выбрать, щелкнув первый элемент, удерживая **Shift** и щелкнув последний элемент.

Выбор отдельного элемента также покажет его свойства в [редакторе свойств](property_editor/ru.md).

Двойной щелчок откроет любую связанную [панель задач](task_panel/ru.md), содержащую действия. Обязательно закройте эту панель задач перед выполнением другой команды или переключением на любую другую рабочую среду.

Дополнительные методы доступны при открытии контекстного меню (щелчок правой кнопкой мыши), в зависимости от выбранного объекта или активной рабочей среды; см. информацию в [древе проекта](tree_view/ru.md).



## Программирование

Выбор объектов по своей сути является графической задачей и поэтому доступен только тогда, когда графический интерфейс пользователя загружен.


<div class="mw-translate-fuzzy">

Эти команды можно использовать в [макросе](Macros/ru.md) или из [консоли Python](Python_console/ru.md).


</div>


```python
import FreeCADGui as Gui

Gui.Selection.addSelection
Gui.Selection.addSelectionGate
Gui.Selection.Filter
```


<div class="mw-translate-fuzzy">

Команда `addSelectionGate` запрещает пользователю выбирать объекты, не указанные в строке выбора. Символ появляется, когда указатель находится над элементом, не входящим в указанную группу.


</div>


```python
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Edge")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Face")

#### or
Gui.Selection.addSelectionGate("SELECT Part::Feature SUBELEMENT Vertex")
```

To remove `SelectionGate()`:


```python
Gui.Selection.removeSelectionGate()
```

Смотрите [Документацию по исходным кодам](Source_documentation/ru.md) и [Std PythonHelp](Std_PythonHelp/ru.md) для получения дополнительной помощи по использованию этих инструментов.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Selection methods/ru
