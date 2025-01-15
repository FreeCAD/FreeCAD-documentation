---
 GuiCommand:
   Name: Std ShowSelection
   Name/ru: Std ShowSelection
   Empty: 1
   MenuLocation: Вид , Видимость , Показать выделенные
   Workbenches: All
   SeeAlso: Std_ToggleVisibility/ru, Std_HideSelection/ru, Std_ToggleObjects/ru, Std_ShowObjects/ru, Std_HideObjects/ru
---

# Std ShowSelection/ru


</div>



## Описание

The **Std ShowSelection** command shows selected objects in [3D views](3D_view.md).



## Применение

1.  Select one or more objects.
    -   Invisible objects can be selected in the [Tree view](Tree_view.md).
    -   Be careful when you use **Ctrl**+**A** to select all objects in the Tree view. This will also selects sub-elements of [PartDesign bodies](PartDesign_Body.md) and objects used for [Part Booleans](Part_Boolean.md). In most cases these should stay invisible.
    -   Objects used for [Part Booleans](Part_Boolean.md) are also selected when you use **Ctrl**+**A** in a 3D view.
2.  There are several ways to invoke the command:
    -   Select the **View → Visibility → <img src="images/Std_ShowSelection.svg" width=16px> Show selection** option from the menu.
    -   Select the **<img src="images/Std_ShowSelection.svg" width=16px> Show selection** option from the Tree view context menu.



## Примечания

See [Std ToggleVisibility](Std_ToggleVisibility#Notes.md).

## Scripting

See [Std ToggleVisibility](Std_ToggleVisibility#Scripting.md).


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std ShowSelection/ru
