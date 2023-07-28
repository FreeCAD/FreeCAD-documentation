# Addon/ru
{{TOCright}}



## Введение

В FreeCAD и в этой документации [Дополнения](Addon/ru.md) - это любой компонент, который не является частью базовой установки, но который может быть добавлен в систему определенными методами.



## Различные типы 


<div class="mw-translate-fuzzy">

Грубо говоря существует три типа дополнения:

-   [Макросы](Macros/ru.md): короткий фрагмент кода [Python](Python.md), который предоставляет новый инструмент или функциональность в одном файле, заканчивающемся расширением файла `.FCMacro`.
-   Модули: один исходный файл Python или набор файлов Python, который каким-то образом расширяет программное обеспечение. Модули не обязательно определяют графический \"верстак\", но могут предоставлять вспомогательную функцию, например библиотеку, выполняющую преобразование форматов, или код, изменяющий графический [интерфейс](interface/ru.md).
-   [Верстаки](External_workbenches/ru.md): коллекции файлов Python, которые предоставляют связанные [команды Gui](Gui_Command/ru.md) (инструменты), сосредоточенные вокруг определенной темы, например, инструменты для проектирования шкафов, инструменты для работы с архитектурой, инструменты для проектирования лодок и т. Д. Эти верстаки обычно определяют новые панели инструментов, где [команды](Gui_Command/ru.md) размещаются в виде кнопок.


</div>



## Установка


<div class="mw-translate-fuzzy">

Начиная с FreeCAD версии 0.17, рекомендуется установка дополнений с помощью <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Менеджера дополнений](Std_AddonMgr/ru.md).


</div>

Однако для макросов и верстаков доступна ручная установка.

-   [Как установить макросы](How_to_install_macros/ru.md)
-   [Установка дополнительных верстаков](Installing_more_workbenches/ru.md)



## Информация для разработчиков 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages: ([FreeCAD-addons](https://github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https://github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

See also:

-   [Distribution of a Python workbench](Workbench_creation#Distribution.md)
-   [Distribution of a C++ workbench](Workbench_creation#Distribution_2.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/ru
