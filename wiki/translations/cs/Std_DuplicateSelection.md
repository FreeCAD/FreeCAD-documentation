---
- GuiCommand:/cs   Name:Std_DuplicateSelection   Name/cs:Std Duplikovat výběr   MenuLocation:Úpravy → Kopírovat   Shortcut:    Workbenches:All   SeeAlso:[Kopírovat](Std_Copy/cs.md), [Vložit](Std_Paste/cs.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Popis

Příkaz Duplikovat výběr je zkratka pro příkazy Kopírovat+Vložit. Vytváří repliky aktuálně vybraných objektů do aktuálního dokumentu.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Použití

1.  Vyberte objekty pro duplikaci.
2.  Použijte menu Úpravy → Duplikovat výběr.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Další

-   Podívejte se na stránku [Kopírování objektů](Copying_Objects/cs.md) na další podrobnosti o replikaci objektů.


</div>

## Preferences

-   Duplicate labels are allowed if **Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels** is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting

The **Std DuplicateSelection** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Std_DuplicateSelection')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





{{Std Base navi

}}  