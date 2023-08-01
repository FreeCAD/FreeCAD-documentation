# Drawing Workbench/ru
<div class="mw-translate-fuzzy">





</div>


**The '''Drawing Workbench''' is no longer included after version 0.20.<br>
The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">



## Введение

Модуль Черчения позволяет поместить ваши 3D наработки на бумагу. То есть, поместить проекции ваших моделей в 2D окно и вставить это окно в рисунок, например на лист с рамкой, вашим заголовком и логотипом и наконец распечатать всё это.


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Инструменты

Это инструменты для создания, настройки и экспортирования 2D чертежных листов

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Открыть SVG](Drawing_Open_SVG/ru.md): Открывает чертеж, ранее сохранённый в формате SVG

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Новый чертеж A3](Drawing_Landscape_A3/ru.md): Создает чертёж формата A3 c шаблоном FreeCAD по умолчанию

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Вставить вид в чертёж](Drawing_View/ru.md): Помещает вид выделенного объекта на активный лист чертежа.

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Аннотация](Drawing_Annotation/ru.md): Добавляет аннотацию на текущий чертёжный лист

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Клип](Drawing_Clip/ru.md): Добавляет группу клипов на текущий чертёжный лист

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Открыть в браузере](Drawing_Openbrowser/ru.md): Открывает предварительный просмотр текущего чертёжного листа в браузере

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Вставить ортографические виды](Drawing_Orthoviews/ru.md): Автоматически создаёт ортографические виды объекта на текущем чертёжном листе

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Символ](Drawing_Symbol/ru.md): Добавляет содержимое файла SVG как символ на текущий чертёжный лист

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing/ru.md): Вставляет специальный вид выбранного объекта на текущий чертёжный лист

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView/ru.md): Вставляет вид выбранного листа электронной таблицы на текущий чертёжный лист

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Экспортировать страницу](Drawing_Save/ru.md): Сохраняет указанный лист в SVG формате

-   [Проекция фигуры](Drawing_ProjectShape/ru.md): Создаёт проекцию выбранного объекта (источинка) в трёхмерном виде.

-    **Примечание:**Инструмент [Draft Drawing](Draft_Drawing/ru.md) главным образом используется с [объектами Draft](Draft_Workbench/ru.md). Он имеет некоторые дополнительных возможностей кроме стандартных инструментов верстака Drawing, и поддерживает специфические объекты вроде [размеров Draft](Draft_Dimension/ru.md).

## Workflow

Документ содержит трёхмерный объект-форму (Schenkel), по которому мы хотим сделать чертёж. Поэтому создается \"Лист\". Лист автоматически получает шаблон, в данном случае шаблон \"A3_Landscape\". Этот шаблон представляет собой документ [SVG](SVG/ru.md) и может содержать обычную чертежную рамку, ваш логотип или другие элементы.

На этот лист вы можете поместить один и более видов. Каждый вид обладает своей позицией на странице, и коэффициентом масштабирования и другие дополнительные свойства. Каждый раз когда лист или вид или объект на который они ссылаются, изменяются, лист перерисовывается, и отображение листа обновляется.



## Написание сценариев 

На данный момент рабочий процес через графический интерфейс пользователя (GUI) очень ограничен, поэтому интересней писать сценарии для API.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.



## Шаблоны

FreeCAD поставляется вместе с набором стандартных шаблонов, но вы также можете найти больше на странице [Чертежных шаблонов](Drawing_templates.md) .



## Расширение модуля Drawing 

Некоторые примечания по программной стороне модуля были добавлены на страницу [Drawing Documentation](Drawing_Documentation.md). Это для быстрого понимания, как работает модуль Drawing, позволяя программистам быстро начать программирование для него.


<div class="mw-translate-fuzzy">

## Учебники

-   [Учебник по модулю Drawing](Drawing_tutorial/ru.md)


</div>

## Macros

-    <img style="width:16px;" src="images/Macro_Automatic_drawing.png"> [Macro Automatic drawing](Macro_Automatic_drawing.md): Allows the user to get the view of his object in a drawing with 4 different position (front,top,iso,right). Needs some modification to be perfectly effective.

-    <img style="width:16px;" src="images/Macro_CartoucheFC.png"> [Macro CartoucheFC](Macro_CartoucheFC.md): This GUI macro to fill simply all fields of the cartridge of the plan implementation worksheet FreeCAD, the format of the date and the symbol of the projection mode adapt to the EU region or US selected.

-    <img style="width:16px;" src="images/Macro_CartoucheFC_2.png"> [Macro CartoucheFC 2](Macro_CartoucheFC_2.md): This GUI macro to fill simply all fields of the cartridge **model 2** of the plan implementation worksheet FreeCAD.

-    <img style="width:16px;" src="images/Macro_CartoucheFC_Full.png"> [Macro CartoucheFC Full](Macro_CartoucheFC_Full.md): This GUI macro to fill simply all fields of the cartridge [Misc templates Full](Misc_templates_Full.md) of the plan implementation worksheet FreeCAD, the format of the date and the symbol of the projection mode adapt to the EU region or US selected.

-    <img style="width:16px;" src="images/Macro_Corner_shapes_wizard.png"> [Macro Corner shapes wizard/update](Macro_Corner_shapes_wizard/update.md): Pops up a dialog asking for the dimensions of your corner piece, then creates the object in the document and creates a page view with top, front and lateral views of the piece.

## External links 


<div class="mw-translate-fuzzy">

## Внешние ссылки 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)


</div>


<div class="mw-translate-fuzzy">





</div>


{{Drawing Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/ru
