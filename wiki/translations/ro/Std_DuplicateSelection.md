---
- GuiCommand:/ro   Name:Std DuplicateSelection   Name/ro:Std DuplicateSelection   MenuLocation:Edit → Copy   Shortcut:    Workbenches:All   SeeAlso:[Copy](Std_Copy/ro.md), [Paste](Std_Paste/ro.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

The Duplicate Selection command is a short-cut for the Copy+Paste commands. It creates replicas of the currently selected objects into the current document.


</div>

## Usage


<div class="mw-translate-fuzzy">

## Cum se utilizează {#cum_se_utilizează}

1.  [ Select](Draft_Select.md) unul sau mai multe obiecte pentru a fi duplicate.
2.  Deschideți meniul pe calea Edit → Duplicate Selection.

În arborescența proiectului, intrările noi apar numeric celor selectați: acestea sunt duplicate.

Pentru [ select](Draft_Select.md) mai multe obiecte:

-   utilizați tasta ** CTRL** făcând clic pe funcțiile pe care doriți să le copiați în arborescența proiectului sau direct în vizualizare,
-   sau în meniul \'\'\' Editați **utilizați elementul** Caseta de selectare \'\'\'pentru a selecta obiectele incluse într-o anumită zonă,
-   Sau din meniul **Edit** pentru a utiliza **<img src=images/_Std_SelectAll.png  style="width: 16px">** Selectați toate pentru a selecta întregul document.

### Exemplu

Funcții selectate: ![](images/DuplicateSelection1.png ) {{Clear}}

Funcții duplicate: ![](images/DuplicateSelection2.png ) {{Clear}}

După această operație, duplicatele nu se deosebesc de originale deoarece sunt plasate în aceeași poziție. [ Mișcați](Placement_/_en.md) un obiect sau ascundeți-l pentru a îl afișa în mod individual.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Suplimentar

-   Vedeți pagina [Copying objects](Copying_Objects.md) pentru mai multe detalii privind replicarea obiectelor.


</div>

## Preferences

-   Duplicate labels are allowed if {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → Document → DuplicateLabels}} is set to `True`. This setting can also be changed in the [Preferences Editor](Preferences_Editor#Document.md).

## Scripting

The **Std DuplicateSelection** command can be applied after selecting one or more objects in the [Tree view](Tree_view.md):


```python
FreeCADGui.runCommand('Std_DuplicateSelection')
```

The selection can be manual (by using the mouse), or via the [Python console](Python_console.md).
To know more about selecting objects programmatically, refer to [Selection methods](Selection_methods.md).





{{Std Base navi

}}  
