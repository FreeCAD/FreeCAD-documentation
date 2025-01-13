# Manual:Using spreadsheets/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

В FreeCAD есть ещё один интересный для изучения верстак:[Spreadsheet](Spreadsheet_Workbench/ru.md). Этот верстак позволяет создать [Электронную таблицу](https://ru.wikipedia.org/wiki/Электронная_таблица) вроде тех что делаются в [Excel](https://ru.wikipedia.org/wiki/Microsoft_Excel) или [LibreOffice](https://ru.wikipedia.org/wiki/OpenOffice_Calc) прямо в FreeCAD. Эти электронные таблицы затем могут быть наполнены данными, взятыми из вашей модели, и производить некоторые вычисления между значениями. Электронные таблицы могут быть экспортированы в файлы CSV, которые могут импортироваться в любые приложения электронных таблиц.


</div>


<div class="mw-translate-fuzzy">

В FreeCAD электронные таблицы имеют дополнительную пользу: их ячейки могут получать имя, и после этого на них может ссылаться любое поле, поддерживаемое [механизмом выражений](Expressions.md). Это превращает электронные таблицы в мощные контрольные структуры, где значения в определённых ячейках могут управлять размерами модели. Только одно надо учесть, что FreeCAD запрещает круговые зависимости между объектами, таблица не может устанавливать параметр и в то же время получать значение от того же объекта. Это значит, что таблица и объект взаимно зависимы.


</div>

In addition to managing values, the workbench is excellent for data management, storing critical information such as material properties, dimensions, and project-wide parameters. This becomes particularly useful in complex projects where multiple values need to be referenced or adjusted.

Spreadsheets also allow users to input formulas for calculations and data management. These formulas can reference other spreadsheet cells or parameters within the 3D model, making the entire design process adaptable and responsive to changes.


<div class="mw-translate-fuzzy">

В следующем примере мы создадим пару объектов, получим некоторые их параметры в таблицу, затем используем таблицу для прямого управления параметрами других объектов.


</div>

In practice, the Spreadsheet Workbench is versatile for different use cases, including defining project-wide parameters, managing bills of materials (BOM), and performing custom calculations that influence design decisions. It simplifies complex projects by centralizing the control of parameters in one location.


<div class="mw-translate-fuzzy">

### Чтение свойств 


</div>




<div class="mw-translate-fuzzy">

-   Начнём с переключения в [верстак Part](Part_Workbench/ru.md), и создадим несколько объектов: <img alt="" src=images/Part_Box.svg  style="width:16px;"> [куб](Part_Box/ru.md), <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [цилиндр](Part_Cylinder/ru.md) и <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [сферу](Part_Sphere/ru.md).
-   Редактируем их параметр **Placement** (или используем инструмент <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Move](Draft_Move/ru.md)) чтобы поместить его немного в сторону, чтобы лучше видеть эффекты того, что мы будем делать:


</div>

-   Start by switching to the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part Workbench](Part_Workbench.md), and create a couple of objects: a <img alt="" src=images/Part_Box.svg  style="width:16px;"> [box](Part_Box.md), a <img alt="" src=images/Part_Cylinder.svg  style="width:16px;"> [cylinder](Part_Cylinder.md) and a <img alt="" src=images/Part_Sphere.svg  style="width:16px;"> [sphere](Part_Sphere.md).
-   Edit their **Placement** property (or use the <img alt="" src=images/Draft_Move.svg  style="width:16px;"> [Draft Move](Draft_Move.md) tool) to place them a little apart, so we can better see the effects of what we\'ll do:


<div class="mw-translate-fuzzy">

-   Теперь извлечём информацию из этих объектов. Переключимся в [верстак Spreadsheet](Spreadsheet_Workbench/ru.md)
-   Нажмём кнопку <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> 
**New Spreadsheet**
-   Дважды кликнем новый объект Spreadsheet в древе проектов, откроется редактор таблиц:


</div>

-   Now, let\'s extract some information about these objects. Switch to the <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:16px;"> [Spreadsheet Workbench](Spreadsheet_Workbench.md)
-   Press the <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> **New Spreadsheet** button
-   Double-click the new Spreadsheet object in the tree view. The spreadsheet editor opens:


<div class="mw-translate-fuzzy">

Редактор таблиц FreeCAD, хотя и не так закончен и мощен как вышеперечисленные более полные приложения электронных таблиц, всё же имеет большинство общеупотребительных базовых инструментов и функций, вроде возможности изменения оформления ячеек (размер, цвет, выключка), объединение и разбивка ячеек, использование формул вроде **=2+2** или ссылки на другие ячейки с **=B1**.


</div>


<div class="mw-translate-fuzzy">

В FreeCAD поверх этих общих возможностей, есть новая интересная: возможность ссылаться не только на другие ячейки, но и другие объекты в документе, и взять значения из их параметров. Например, примем несколько параметров из трёх ранее созданных объектов. Параметры будут те, что мы видим в окне редактора параметров во вкладке **Data**, при выделении объекта.


</div>


<div class="mw-translate-fuzzy">

-   Начнём с вводом текста в ячейки A1, A2 и A3, чтобы мы запомнили что есть что на будущее, например, **Cube Length**, **Cylinder Radius** и **Sphere Radius**. Для ввода текста просто напишите в поле \"Содержание\" над таблицей, или сделайте двойной клик по ячейке.
-   Теперь получим фактическое значение длины куба. В ячейке B1 напишем **=Куб.Length**. Вы увидите, что таблица имеет механизм автозаполнения, тот же самый, что и в редакторе выражений, использованный в предыдущей главе.
-   Повторим то же для ячеек B2 (**=Цилиндр.Radius**) and B3 (**=Сфера.Radius**).


</div>

-   Let\'s start by entering a couple of texts in the cells A1, A2 and A3, so we remember what is what later on, for example **Cube Length**, **Cylinder Radius** and **Sphere Radius**. To enter text, just write in the \"Contents\" field above the spreadsheet, or double-click a cell.
-   Now let\'s retrieve the actual length of our cube. In cell B1, type **=Cube.Length**. You will notice that the spreadsheet has an auto-completion mechanism, which is actually the same as the expression editor we used in the previous chapter.
-   Do the same for cell B2 (**=Cylinder.Radius**) and B3 (**=Sphere.Radius**).


<div class="mw-translate-fuzzy">

-   Хотя это ожидаемо, значения могут обрабатываться как любые числа, попробуйте, например, ввести в ячейку C1: **=B1\*2**.
-   Теперь мы можем изменить одно из этих значений в редакторе параметров, и изменения немедленно отразятся в таблице. Например, изменим длину куба на **20mm**:


</div>

-   Although these results are expressed with their units, the values can be manipulated as any number, try for example entering in cell C1: **=B1\*2**.
-   We can now change one of these values in the properties editor, and the change will be immediately reflected in the spreadsheet. For example, let\'s change the length of our cube to **20mm**:


<div class="mw-translate-fuzzy">

Страница [верстака Spreadsheet](Spreadsheet_Workbench/ru.md) покажет подробности о всех возможных операциях и функциях, которые доступны в таблице.


</div>


<div class="mw-translate-fuzzy">

### Запись свойств 


</div>




<div class="mw-translate-fuzzy">

Другое интересное использование верстака Spreadsheet в FreeCAD противоположно тому, что мы делали: вместо чтения значений параметров трёхмерных объектов мы можем назначать им значения. Помните, тем не менее, одно из базовых правил FreeCAD: запрет круговых зависимостей. Поэтому мы не можем использовать ту же таблицу для чтения **и** записи значений в трёхмерный объект. Это может сделать объект зависимым от таблицы, которая будет зависеть от объекта. Вместо этого нам надо сделать другую таблицу.


</div>


<div class="mw-translate-fuzzy">

-   Теперь закроем вкладку таблицы (в трёхмерном окне). Это не обязательно, можно и оставить несколько таблиц открытыми.
-   Нажмём снова кнопку <img alt="" src=images/Spreadsheet_Create.png  style="width:16px;"> 
**New Spreadsheet**
-   Изменим имя новой таблицы на что-то более содержательное, вроде **Ввод** (это делается правым кликом на новой таблице и выбором **Переименовать**).
-   Откроем редактор таблиц двойным кликом по таблице **Ввод**.
-   В ячейке A1 поместим описание, например: \"Размеры Куба\"
-   В ячейке B1 напишем **=5mm** (использование знака \"=\" гарантирует, что значение будет понято как величина, а не текст).
-   Теперь, чтобы использовать это значение за пределами таблицы, надо дать имя ячейке B1 псевдоним. Сделаем правый клик на ячейке, нажмём **Свойства** и выделим вкладку **Псевдоним**. Дадим имя, например, **cubedims**:


</div>

-   We can now close the spreadsheet tab (under the 3D view). This is not mandatory, there is no problem in keeping several spreadsheet windows open.
-   Press the <img alt="" src=images/Spreadsheet_Create.svg  style="width:16px;"> **New Spreadsheet** button again
-   Change the name of the new spreadsheet to something more meaningful, such as **Input** (do this by right-clicking the new spreadsheet object, and choosing **Rename**).
-   Double-click the Input spreadsheet to open the spreadsheet editor.
-   In cell A1, let\'s put a descriptive text, for example: \"Cube dimensions\"
-   In cell B1, write **=5mm** (using the = sign makes sure the value is interpreted as a unit value, not a text).
-   Now to be able to use this value outside the spreadsheet, we need to give a name, or alias, to the B1 cell. Right-click the cell, click **Properties** and select the **Alias** tab. Give it a name, such as **cubedims**:


<div class="mw-translate-fuzzy">

-   Нажмём **OK** и закроем вкладку таблицы
-   Выделим куб
-   В редакторе параметров кликнем маленькую иконку <img alt="" src=images/Bound-expression-unset.png  style="width:16px;"> **expression** справа от поля **Length**. Это откроет [редактор выражений](Expressions/ru.md), где мы сможем написать **Spreadsheet001.cubedims**. Повторим это для Height и Width:


</div>

-   Press **OK**, then close the spreadsheet tab
-   Select the cube object
-   In the properties editor, click the little <img alt="" src=images/Bound-expression-unset.svg  style="width:16px;"> **expression** icon at the right side of the **Length** field. This will open the [expressions editor](Expressions.md), where you can write **Spreadsheet001.cubedims**. Repeat this for **Height** and **Width**:


<div class="mw-translate-fuzzy">

Вы можете удивиться, почему нам понадобилось использовать в выражении \"Spreadsheet001\" вместо \"Ввод\". Это потому, что каждый объект в документе FreeCAD имеет **внутреннее имя**, уникальное для документа, и **метку**, видимую в древе проекта. Если Вы снимите соответствующую опцию в настройках, FreeCAD позволит давать одноименные метки для разных объектов. Поэтому все операции, которые должны однозначно идентифицировать объекты, используют внутренние имена вместо меток, которые могут обозначать разные объекты. Проще всего узнать внутренние имена объектов оставлять открытой панель **просмотр выделения** (меню Вид-\>Панели), она всегда показывает внутреннее имя выбранного объекта:


</div>

The reason we use \"Spreadsheet001\" instead of \"Input\" in the expression is that every object in a FreeCAD document has a unique internal name and a more user-friendly label. While the label is what appears in the tree view, the internal name is used to uniquely identify objects within the document. FreeCAD allows you to assign the same label to multiple objects if you adjust your preferences, but the internal name remains unique. For any operation that requires identifying an object without ambiguity, FreeCAD uses the internal name rather than the label, as the label could refer to more than one object. To find the internal name of an object, it\'s useful to keep the Selection Panel (accessible via View → Panels) open. This panel will always display the internal name of the selected object, ensuring you use the correct reference in your expressions.


<div class="mw-translate-fuzzy">

Используя в таблицах псевдонимы ячеек мы можем использовать таблицы для хранения \"основных значений\" в документах FreeCAD. Это может использоваться, например, для моделей различных размеров, сохраняя эти размеры в таблице. Становится лёгким создавать другие модели с различными размерами, просто открыв файл и изменив набор размеров в таблице.


</div>


<div class="mw-translate-fuzzy">

В итоге заметьте, что ограничения внутри эскизов так же могут получать значения из табличных ячеек:


</div>

Finally, note that the constraints inside a sketch can also receive the value of a spreadsheet cell:

Так же можно создать псевдонимы для размерных ограничений (горизонтальных, вертикальных или по расстояниям) в эскизах (которые так же можно использовать за пределами эскизов)

![](images/FreeCAD_SpreedSheet_Rectangle.png )

**Загрузки**

-   Файл, полученный в этом примере: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/spreadsheet.FCStd>

**Читать далее**

-   [Верстак Spreadsheet](Spreadsheet_Workbench/ru.md)
-   [Использование выражений в параметрах](Expressions/ru.md)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Using spreadsheets/ru
