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


<div class="mw-translate-fuzzy">

### Назначение имен 

GuiCommand именуются определенным образом: *ИмяМодуля\_ИмяКоманды* т.е. \"Base\_Open\" это команда Открыть(Open) графического интерфейса в Base (базовой системе). GuiCommand в определенном модуле получает имя имя модуля впереди, например \"Part\_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

Если документ не закончен (в смысле wiki статья) используйте шаблон [Template:UnfinishedDocu](Template:UnfinishedDocu.md)


</div>


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


<div class="mw-translate-fuzzy">

Каждая GuiCommand-а должна иметь иконку. Мы используем \[<http://tango.freedesktop.org/Tango_Desktop_Project>\| Tango набор иконок\] и его принципы. Справа вы можете видеть палитру цветов tango.


</div>


<div class="mw-translate-fuzzy">

Предпочтительней всех, иконки нарисованные в SVG , например с помощью [Inkscape](http://inkscape.org). Это упрощает добавление изменений и получение дополнительных Иконок в том же пространстве приложения.


</div>

### Диаграмма цветового кодирования иконок 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Мы стараемся насколько возможно следовать этой диаграмме, так что цвета иконок имеют прямое значение.


<div class="mw-translate-fuzzy">

### Требования к качеству 

Существует множество GuiCommands (Особенностей/Фишек) в FreeCAD которые являются экспериментальными или используются недолгое время для реализации целей. Эти GuiCommands в основном помещаются в инструментарии, такие как Part, Mesh или Cam. Для обеспечения хорошей работы пользователя, был создан*Полный(Complete)* инструментарий. Это инструментарий, который запускается по умолчанию при старте FreeCAD и он включает в себя все GuiCommand-ы, отвечающие **Требованиям к качеству** ,описанным здесь:


</div>

There are a lot of GuiCommands (tools) in FreeCAD which are experimental or used for a short time to test implementation of new features. These GuiCommands are mostly in the dedicated workbenches like Part, Mesh or Cam. To ensure a good user experience the workbench *Complete* was created. This workbench incorporates all GuiCommands which meet certain quality requirements which are described here:


<div class="mw-translate-fuzzy">

-   Команда/Функция должна быть **законченой**. Никаких незавершенных работ!
-   Должен иметь **справочную страницу** как [эта](Std_ViewScreenShot.md)
    -   Все поля [Template:GuiCommand](Template:GuiCommand.md) должны быть заполнены
    -   Картинки с изображением диологов команды и конечный вывод
    -   детальное описание команды и всех её параметров и настроек
    -   Описание связанных python интерфесов и классов с примерами кода
-   Настройка надлежащей иконки и позиции в меню


</div>


<div class="mw-translate-fuzzy">

Надеюсь, что так будет со всеми GuiCommands из [Списка команд](List_of_Commands/ru.md).


</div>


{{Powerdocnavi

}}

---
[documentation index](../README.md) > Gui Command/ru
