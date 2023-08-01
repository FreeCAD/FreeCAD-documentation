# DAG view/ru
## Введение




[DAG](DAG_view/ru.md) (Directed Acyclic Graph) - это [направленный ациклический граф](https://ru.wikipedia.org/wiki/%D0%9E%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B0%D1%86%D0%B8%D0%BA%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D1%80%D0%B0%D1%84), который отображает взаимосвязи между различными объектами в документе. Этот иструмент предназначен в первую очередь для того, чтобы показать, зависимости между объектами в сложных моделях со множеством функций и ссылок, например созданных с помощью <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [верстака PartDesign](PartDesign_Workbench/ru.md).

The DAG view resembles the graph that can be produced from a Git repository and its branches. Together with the standard [tree view](tree_view.md) and the [dependency graph](Std_DependencyGraph.md), the DAG view is a tool to inspect the parametric history of objects in a document.

## Пример

Простая модель связи объектов которой будут представлены разными способами.

![](images/FreeCAD_DAG_view_3D.png ) 
*Композитная модель с 2-ух мерными и 3-ех мерными формами.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">



*Слева: объекты отображены в стандартном [древовидном представлении](tree_view/ru.md). Справа: объекты представлены в виде DAG.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )



*Отношения между объектами отображены в [графе зависимостей](Std_DependencyGraph/ru.md).*

## Включение возможности просмотра DAG 

The DAG view was introduced in 0.17 as an experimental feature for power users and developers, so they could troubleshoot complex models; therefore, the DAG view is not available by default.

Для того, чтобы сделать возможным просмотр DAG, откройте [ редактор параметров](Std_DlgParameter/ru.md) (через главное меню **Инструменты → Редактор параметров...**). И создайте следующую группу, если она еще не создана:

-    `BaseApp/Preferences/DockWindows/DAGView`
    

В группе создайте параметр `Enabled`, `Boolean` типа и установите его как {{true}}. Нажмите **Сохранить на диск** и закройте редактор параметров.

Перезапустите FreeCAD и откройте окно просмотра DAG через: **{{StdMenu|[Вид](Std_View_Menu/ru.md)** → Панели → Просмотор DAG}}.

In the [parameter editor](Std_DlgParameter.md) you can also change some properties in the following subgroup

-    `BaseApp/Preferences/DAGView`
    

-   FontPointSize - Set size of text font and can help with readability with high DPI displays. Set to 0 for default font size.

-   SelectionMode
    -   0 - single click selects an item. Ctrl-click to add items to selection.
    -   1 - every click adds/removes item to selection.

-   Direction - the order in which items are displayed.
    -   1 - child on top, parent under it
    -   -1 - parent on top, children under it

## Ссылки

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), forum thread presenting the new tool.
-   [easter egg of PartDesign Next: DAG View](https://forum.freecadweb.org/viewtopic.php?t=15375), including the view together with the update to PartDesign.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > DAG view/ru
