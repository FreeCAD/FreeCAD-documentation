---
- GuiCommand:/ru
   Name:Std TreeSyncPlacement
   Name/ru:Std TreeSyncPlacement
   MenuLocation:Вид → Дерево документа → Sync placement
   Workbenches:All
   Shortcut:**T** **3**
   Version:0.19
---

# Std TreeSyncPlacement/ru

## Описание

Команда **Std TreeSyncPlacement** переключает режим SyncPlacement [древа проекта](Tree_view/ru.md). Если этот режим включен, параметр **Placement** объектов автоматически корректируется, когда они перетаскиваются из одного контейнера в другой с другой системой координат, сохраняя их расположение относительно глобальной системы координат.

## Применение

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **Sync placement** option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeSyncPlacement.svg" width=16px> Sync placement** option from the menu.
    -   Use the keyboard shortcut: **T** then **3**.

## Настройки

The Tree view SyncPlacement mode is stored: **Tools → Edit parameters... → BaseApp → Preferences → TreeView → SyncPlacement**. It is a boolean value, the default is `False`.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std TreeSyncPlacement/ru
