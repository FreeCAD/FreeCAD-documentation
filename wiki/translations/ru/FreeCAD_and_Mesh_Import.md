


{{TOCright}}

## Post-Import {#post_import}


<div class="mw-translate-fuzzy">

## Операции после импорта {#операции_после_импорта}

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

### \"cannot convert because shape is not a shell\" {#cannot_convert_because_shape_is_not_a_shell}


<div class="mw-translate-fuzzy">

## Что делать, если получено сообщение об ошибке: \"cannot convert because shape is not a shell\"? {#что_делать_если_получено_сообщение_об_ошибке_cannot_convert_because_shape_is_not_a_shell}

Вероятно, ваша форма содержит ошибки, возможно, она не замкнута (имеет дыры). Поскольку возможности верстака Mesh в FreeCAD пока еще ограничены, вам следует попробовать проверить и восстановить вашу модель с помощью сторонних программ. После этого попробуйте импортировать и конвертировать вашу модель заново.


</div>


<div class="mw-translate-fuzzy">

## Какие программы можно использовать для проверки/исправления сеточной модели? {#какие_программы_можно_использовать_для_проверкиисправления_сеточной_модели}

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

[Category:User\_Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:File\_Formats{{\#translation:}}](Category:File_Formats.md)
