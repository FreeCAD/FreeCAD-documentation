---
- GuiCommand:
   Name:Std Refresh
   MenuLocation:[Bearbeiten](Std_Edit_Menu/de.md) → Aktualisieren
   Workbenches:All
   Shortcut:**F5** or **Ctrl+R**
---


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Wenn verwendet, berechnet dieser Befehl alle geänderten Komponenten auf dem Bildschirm neu und aktualisiert die Anzeige .


</div>

The **Std Refresh** command recomputes the active document. The command is disabled if the document does not require a recompute.


<div class="mw-translate-fuzzy">

## Anwendung


</div>


<div class="mw-translate-fuzzy">

Drücke **F5** oder **Ctrl**+**R** oder klicke auf das Symbol **<img src=images/Std_Refresh.svg style="width:16px"> [Refresh](Std_Refresh.md)**.


</div>

## Options

-   To force a recompute select the document or one or more objects in the [Tree view](Tree_view.md), choose the **<img src="images/Std_MarkToRecompute.svg" width=16px> Mark to recompute** option from the context menu, and invoke the command.
-   For objects, but not for documents, you can also choose **Recompute object** from the same context menu (<small>(v0.19)</small> ).

## Notes

-   For a macro that will recompute the active document see: [Macro ForceRecompute](Macro_ForceRecompute.md).


<div class="mw-translate-fuzzy">

## Skripten


</div>


<div class="mw-translate-fuzzy">


**Siehe auch:**

[FreeCAD Grundlagen Skripten ](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Die Neuberechnung des Modells kann in der [Makros](macros.md) und von der [Python](Python.md) Konsole aus mit Hilfe der `recompute` Methode des aktuell aktiven Dokuments durchgeführt werden.


</div>


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}  
