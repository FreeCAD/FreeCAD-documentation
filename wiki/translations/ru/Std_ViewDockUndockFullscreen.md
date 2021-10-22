---
- GuiCommand:/ru

   Name:Std ViewDockUndockFullscreen
   Name/ru:Std ViewDockUndockFullscreen
   Empty:1
   MenuLocation:Вид → Окно документа → Закреплённое/Откреплённное
   Workbenches:All
   Shortcut:**V** **D** / **V** **U**
   SeeAlso:[Std ViewFullscreen](Std_ViewFullscreen/ru.md), [Std MainFullscreen](Std_MainFullscreen/ru.md)
---

# Std ViewDockUndockFullscreen/ru

## Введение

[Окно трёхмерного просмотра](3D_view/ru.md) можно отсоединить от основного [интерфейса FreeCAD](Interface/ru.md) и, например, переместить на другой дисплей.

![](images/FinestraNonAgganciata.png ) 
*Отстыкованный трёхмерный вид*

## Пристыкованное

### Описание

The **Docked** menu option docks the active [3D view](3D_view.md) inside the main FreeCAD interface.

### Применение

1.  Activate an undocked 3D view.
2.  There are several ways to invoke the option:
    -   If there are no docked 3D views: select the **View → Document window → Docked** option from the menu.
    -   Select the **Document window → Docked** option from the 3D view context menu.
    -   Use the keyboard shortcut: **V** then **D**.

## Отстыкованное

### Описание 

The **Undocked** menu option undocks the active [3D view](3D_view.md) from the main FreeCAD interface.

### Применение 

1.  Activate a docked 3D view.
2.  There are several ways to invoke the option:
    -   Select the **View → Document window → Undocked** option from the menu.
    -   Select the **Document window → Undocked** option from the 3D view context menu.
    -   Use the keyboard shortcut: **V** then **U**.

## Примечания

-   Для одного и того же документа можно создать несколько трёхмерных представлений с помощью команды [Std ViewCreate](Std_ViewCreate/ru.md).
-   Трёхмерные виды также можно закреплять и откреплять с помощью команды [Std ViewFullscreen](Std_ViewFullscreen/ru.md).





{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewDockUndockFullscreen/ru
