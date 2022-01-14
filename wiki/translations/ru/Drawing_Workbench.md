# Drawing Workbench/ru
**Разработка [верстак TechDraw](Drawing_Workbench/ru]],_начиная_с_FreeCAD_0.16, остановлена, и в версии 0.17 был предложен новый [[TechDraw Workbench/ru.md), предназначенный для его замены. Оба верстака пока есть в v0.17, но в будущих выпусках верстак Drawing может быть удалён.**

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

Документ содержит трёхмерный объект-форму (Schenkel), по которому мы хотим сделать чертёж. Поэтому создается \"Лист\". Лист автоматически получает шаблон, в данном случае шаблон \"A3\_Landscape\". Этот шаблон представляет собой документ [SVG](SVG/ru.md) и может содержать обычную чертежную рамку, ваш логотип или другие элементы.

На этот лист вы можете поместить один и более видов. Каждый вид обладает своей позицией на странице, и коэффициентом масштабирования и другие дополнительные свойства. Каждый раз когда лист или вид или объект на который они ссылаются, изменяются, лист перерисовывается, и отображение листа обновляется.

## Написание сценариев 

На данный момент рабочий процес через графический интерфейс пользователя (GUI) очень ограничен, поэтому интересней писать сценарии для API.

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.

Скрипт [Macro\_CartoucheFC](Macro_CartoucheFC/ru.md) позволяет создать пользовательское информационное поле на горизонтальном листе A3.

## Шаблоны

FreeCAD поставляется вместе с набором стандартных шаблонов, но вы также можете найти больше на странице [Чертежных шаблонов](Drawing_templates.md) .

## Расширение модуля Drawing 

Некоторые примечания по программной стороне модуля были добавлены на страницу [Drawing Documentation](Drawing_Documentation.md). Это для быстрого понимания, как работает модуль Drawing, позволяя программистам быстро начать программирование для него.

## Учебники

-   [Учебник по модулю Drawing](Drawing_tutorial/ru.md)

## Внешние ссылки 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}} 

[<img src="images/Property.png" style="width:16px"> Obsolete Workbenches](Category_Obsolete_Workbenches.md)

---
[documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > Drawing Workbench/ru
