---
 GuiCommand:
   Name: Draft Array
   Name/de: Draft Anordnung
   MenuLocation: Zeichnen , Anordnung
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Draft_OrthoArray, Draft_PolarArray, Draft_CircularArray
---

# Draft Array/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Array.svg  style="width:24px;"> Draft Anordnung erstellt eine orthogonale (3-Achsen)Anordnung aus einem ausgewählten Objekt. Die erstellte Anordnung kann in eine [polare Anordnung](Draft_PolarArray/de.md) oder eine [Kreis-Anordnung](Draft_CircularArray/de.md) umgewandelt werden, indem ihre {{PropertyData/de|Array Type}} geändert wird.

Dieser Befehl kann für 2D-Objekte verwendet werden, die mit den Arbeitsbereichen [Draft](Draft_Workbench/de.md) oder [Sketcher](Sketcher_Workbench/de.md) erstellt wurden, aber auch für viele 3D-Objekte, die mit anderen Arbeitsbereichen wie [Part](Part_Workbench/de.md), [PartDesign](PartDesign_Workbench/de.md) oder [Arch](Arch_Workbench/de.md) erstellt wurden.

Dieser Befehl ist jetzt veraltet. Stattdessen können [Draft RechtwinkligeAnordnung](Draft_OrthoArray.md), [Draft PolareAnordnung](Draft_PolarArray.md) oder [Draft KreisAnordnung](Draft_CircularArray.md) verwendet werden.



## Anwendung

1.  Um diesen Befehl in FreeCAD Version 0.19 und neuer zu verwenden, muss eine Schaltfläche zu einer benutzerdefinierten Symbolleiste hinzugefügt werden. Siehe [Oberfläche anpassen](Interface_Customization/de.md).
2.  Wahlweise ein Objekt auswählen.
3.  Die Schaltfläche **<img src="images/Draft_Array.svg" width=16px> [Draft Anordnung](Draft_Array/de.md)** drücken.
4.  Ist noch kein Objekt ausgewählt: If you have not yet selected an object: Ein Objekt auswählen.
5.  Die Anordnung wird erstellt.
6.  Wahlweise seine [Eigenschaften](Draft_OrthoArray/de#Eigenschaften.md) anpassen.



## Eigenschaften

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Eigenschaften.md).



## Skripten

Siehe [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de#Scripten.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Array/de
