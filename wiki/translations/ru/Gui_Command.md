# Gui Command/ru
<div class="mw-translate-fuzzy">

GuiCommand - одна из наиболее важных функций FreeCAD при взаимодействии с пользователем. Каждый раз, когда пользователь выбирает опцию в меню или нажимает на кнопку панели инструментов, активируется GuiCommand. Некоторые из атрибутов GuiCommand:

-   Задано имя
-   Содержит иконку
-   Определена возможности для отмены/повтора
-   Есть страница справки
-   Открывает и управляет диалогами
-   Записывается в макрос
-   и.т.д\...


</div>

## Naming


<div class="mw-translate-fuzzy">

### Назначение имен 

GuiCommand именуются определенным образом: *ИмяМодуля_ИмяКоманды* т.е. \"Base_Open\" это команда Открыть(Open) графического интерфейса в Base (базовой системе). GuiCommand в определенном модуле получает имя имя модуля впереди, например \"Part_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

Если документ не закончен (в смысле wiki статья) используйте шаблон [Template:UnfinishedDocu](Template_UnfinishedDocu.md)


</div>

## Help page 


<div class="mw-translate-fuzzy">

### Страница справки 

Каждая GuiCommand должна обладать страницей справки. Страница справки должна располагаться в FreeCAD wiki. Статья имеет то же имя, что и GuiCommand, например, [Draft ShapeString](Draft_ShapeString.md).


</div>


<div class="mw-translate-fuzzy">

Чтобы создать ваши собственные справочные страницы используйте шаблон: [GuiCommand model](GuiCommand_model.md)


</div>


<div class="mw-translate-fuzzy">

Примеры:

-   [Draft ShapeString](Draft_ShapeString.md)
-   [Draft Line](Draft_Line.md)


</div>


<div class="mw-translate-fuzzy">

### Иконки

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


</div>

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


<div class="mw-translate-fuzzy">

Каждая GuiCommand-а должна иметь иконку. Мы используем \[<http://tango.freedesktop.org/Tango_Desktop_Project>\| Tango набор иконок\] и его принципы. Справа вы можете видеть палитру цветов tango.


</div>


<div class="mw-translate-fuzzy">

Предпочтительней всех, иконки нарисованные в SVG , например с помощью [Inkscape](http://inkscape.org). Это упрощает добавление изменений и получение дополнительных Иконок в том же пространстве приложения.


</div>

### Диаграмма цветового кодирования иконок 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Мы стараемся насколько возможно следовать этой диаграмме, так что цвета иконок имеют прямое значение.



---
⏵ [documentation index](../README.md) > Gui Command/ru
