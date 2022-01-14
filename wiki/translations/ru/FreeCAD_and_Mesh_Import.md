# FreeCAD and Mesh Import/ru
{{TOCright}}

## Post-Import 


<div class="mw-translate-fuzzy">

## Операции после импорта 

После импорта сетки для FreeCAD модель будет представлять собой набор граней. Вам захочется преобразовать модель в форму, обрабатываемую FreeCAD, и это можно сделать внутри FreeCAD.


</div>


<div class="mw-translate-fuzzy">

Для этого:

-   Переключитесь на верстак Part
-   Выберите сетку, и выберите в меню Деталь \--\> Создание формы из сетки
-   Нажмите OK в диалоговом окне
-   Выберите вновь созданную форму
-   Выберите в меню Деталь -\> Преобразовать в твердое
-   Выбрать вновь созданное твёрдое тело
-   Выбрать в меню Деталь -\> [Уточнить форму](Refine_shape/ru.md)


</div>


<div class="mw-translate-fuzzy">

Последний шаг не обязателен, но это очистит тело от его от ненужных кромок на плоских и цилиндрических поверхностях.


</div>

## Errors

### \"cannot convert because shape is not a shell\" 


<div class="mw-translate-fuzzy">

## Что делать, если получено сообщение об ошибке: \"cannot convert because shape is not a shell\"? 

Вероятно, ваша форма содержит ошибки, возможно, она не замкнута (имеет дыры). Поскольку возможности верстака Mesh в FreeCAD пока еще ограничены, вам следует попробовать проверить и восстановить вашу модель с помощью сторонних программ. После этого попробуйте импортировать и конвертировать вашу модель заново.


</div>


<div class="mw-translate-fuzzy">

## Какие программы можно использовать для проверки/исправления сеточной модели? 

-   [Meshlab](http://meshlab.sourceforge.net/)
    -   Лицензия: Open Source (GPL V2)
    -   Работает на Windows 32/64 bit, Linux и Mac OS X


</div>


<div class="mw-translate-fuzzy">

-   [netFabb basic](http://www.netfabb.com/downloadcenter.php?basic=1)
    -   Лицензия: Freeware
    -   Работает на Windows XP/7/8, Linux и Mac OS X


</div>

## Tutorials


<div class="mw-translate-fuzzy">

## Учебники

-   [Импорт из файлов формата STL или OBJ](Import_from_STL_or_OBJ/ru.md)
-   [Экспорт в файлы формата STL или OBJ](Export_to_STL_or_OBJ/ru.md)


</div>

## Related

-   [FreeCAD Howto Import Export](FreeCAD_Howto_Import_Export.md)

[<img src="images/Property.png" style="width:16px"> User\_Documentation](Category_User_Documentation.md) [<img src="images/Property.png" style="width:16px"> File\_Formats](Category_File_Formats.md)

---
[documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > FreeCAD and Mesh Import/ru
