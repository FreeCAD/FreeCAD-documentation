---
- GuiCommand:
   Name: Std TreeSingleDocument
   Name/ru: Std TreeSingleDocument
   MenuLocation: Вид - Дерево документа - Одиночный документ
   Workbenches: All
   SeeAlso: [Std TreeMultiDocument](Std_TreeMultiDocument/ru.md), [Std TreeCollapseDocument](Std_TreeCollapseDocument/ru.md)
---

# Std TreeSingleDocument/ru


</div>

## Описание

The **Std TreeSingleDocument** command switches the [Tree view](Tree_view.md) DocumentMode to SingleDocument. In this mode only a single document is visible in the Tree view. The other modes are [MultiDocument](Std_TreeMultiDocument.md) and [CollapseDocument](Std_TreeCollapseDocument.md).

In SingleDocument mode you can switch to a different document by activating a 3D view belonging to that document. You can do this in the [Main view area](Main_view_area.md) or via the **Windows** menu.

## Применение

1.  There are several ways to invoke the command:
    -   Click on the black down arrow to the right of the **<img src="images/Std_TreeSyncView.svg" width=16px>** button and select the **Single document** option from the flyout. Note: the button image will change depending on the selected option.
    -   Select the **View → TreeView actions → <img src="images/Std_TreeSingleDocument.svg" width=16px> Single document** option from the menu.

## Настройки

The Tree view DocumentMode mode is stored: **Tools → Edit parameters... → BaseApp → Preferences → TreeView → DocumentMode**. It is an integer value. Possible values are `0` (SingleDocument), `1` (MultiDocument) or `2` (CollapseDocument). The default is `2`.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std TreeSingleDocument/ru
