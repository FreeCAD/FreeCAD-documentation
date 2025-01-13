# 3D view/ru
## Введение




3D вид в FreeCAD это экземпляр Coin3D [ граф сцены](Scenegraph/ru.md), который формирует самое важное окно [интерфейса](interface/ru.md). Coin3D-это библиотека, реализующая стандарт описания сцен OpenInventor 2.1


<div class="mw-translate-fuzzy">

Некоторые свойства вида, такие как цвет фона, [стиль навигации мыши](Mouse_Model/ru.md) и шаги масштабирования, можно настроить в [редакторе настроек](Preferences_Editor/ru.md).


</div>

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*<b>3D вид</b> является компонентом [интерфейса](Interface/ru.md) FreeCAD. По умолчанию он показывает небольшой виджет с координатными осями и навигационный куб также с координатными осями; сетку можно отобразить и настроить, загрузив [верстак Draft](Draft_Workbench/ru.md).*

## Context menu 

The options in the context menu of the 3D view depend on the selected object(s) and the currently active workbench. To display this menu optionally select one or more objects and then right-click in the 3D view.



## Подробности

FreeCAD использует библиотеку Quarter для использования Coin3D в среде Qt.


<div class="mw-translate-fuzzy">

Можно напрямую взаимодействовать с графом сцены 3D-вида из [консоли Python](Python_console/ru.md) с помощью библиотеки Python Pivy.


</div>

Дополнительные сведения см. в документации для опытных пользователей:

-   [Scenegraph](Scenegraph/ru.md), описание библиотеки Coin3D.
-   [Pivy](Pivy/ru.md), использование Coin3D из консоли Python.
-   [Сторонние библиотеки](Third_Party_Libraries/ru.md) используемые FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ документация.


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/ru
