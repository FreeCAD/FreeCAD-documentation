# Addon/ru
{{TOCright}}

## Введение

В FreeCAD и в этой документации [Дополнения](Addon/ru.md) - это любой компонент, который не является частью базовой установки, но который может быть добавлен в систему определенными методами.

## Различные типы 


<div class="mw-translate-fuzzy">

Грубо говоря существует три типа дополнения   *

-   [Макросы](Macros/ru.md)   * короткий фрагмент кода [Python](Python.md), который предоставляет новый инструмент или функциональность в одном файле, заканчивающемся расширением файла `.FCMacro`.
-   Модули   * один исходный файл Python или набор файлов Python, который каким-то образом расширяет программное обеспечение. Модули не обязательно определяют графический \"верстак\", но могут предоставлять вспомогательную функцию, например библиотеку, выполняющую преобразование форматов, или код, изменяющий графический [интерфейс](interface/ru.md).
-   [Верстаки](External_workbenches/ru.md)   * коллекции файлов Python, которые предоставляют связанные [команды Gui](Gui_Command/ru.md) (инструменты), сосредоточенные вокруг определенной темы, например, инструменты для проектирования шкафов, инструменты для работы с архитектурой, инструменты для проектирования лодок и т. Д. Эти верстаки обычно определяют новые панели инструментов, где [команды](Gui_Command/ru.md) размещаются в виде кнопок.


</div>

## Установка


<div class="mw-translate-fuzzy">

Начиная с FreeCAD версии 0.17, рекомендуется установка дополнений с помощью <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Менеджера дополнений](Std_AddonMgr/ru.md).


</div>


<div class="mw-translate-fuzzy">

Однако ручная установка остаётся возможной.

-   [Как установить макрос](How_to_install_macros/ru.md)
-   [Установка дополнительных верстаков](Installing_more_workbenches/ru.md)


</div>

## Information for developers 

If you have developed a macro or workbench, and want to see it included in the Addon manager, read how to do so on the repository pages   * ([FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) and [FreeCAD-macros](https   *//github.com/FreeCAD/FreeCAD-macros/)). If you add your macro to the [Macros recipes](Macros_recipes.md) page, there is nothing else to do, it will automatically be picked up by the Addon manager.

### Python workbenches 

For Python workbenches, you don\'t need any specific approval to have your workbench added to the Addon Manager. In addition, because your Addon is outside the FreeCAD source code, you can choose the license you want. If you request for your workbench to be added to the Addon Manager\'s default list (we will not add any new workbench without a request from its authors), either by asking so on the forum or by opening an issue on the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository, your code will stay on your own git repository, we will just add it as a submodule to the [FreeCAD-addons](https   *//github.com/FreeCAD/FreeCAD-addons/) repository. Of course, before adding your workbench, we will take a look at it and make sure there is nothing potentially problematic with it. For more details about structuring your Addon, including information about metadata used by the Addon Manager, see [Workbench creation](Workbench_creation.md).

### C++ workbenches 

If you develop a workbench in C++, it cannot be run directly by users and must be compiled first. You then have two options, either you provide precompiled versions of your workbench yourself, for the different operating systems, or you should request to have your code merged into the FreeCAD source code. For that, you should use the LGPL license (or a fully compatible license like MIT or BSD), and you must present your new tools to the community in the [FreeCAD forum](https   *//forum.freecadweb.org) for review. Once your code has been tested and approved, you should fork the FreeCAD repository, if not done yet, create a new branch, push your code to it, and open a pull request so that your branch is merged into the main repository.




[Category   *Addons](Category_Addons.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > Addon/ru
