---
 GuiCommand:
   Name: Std ViewDimetric
   MenuLocation: Ansicht , Standardansichten , Axonometrisch , Dimetrisch
   Workbenches: Alle
   SeeAlso: Std_ViewIsometric/de, Std_ViewTrimetric/de
---

# Std ViewDimetric/de

## Beschreibung

Der **Std AnsichtDimetrisch**-Befehl richtet die Kamera in der aktiven [3D-Ansicht](3D_view/de.md) neu aus, um eine [dimetrisch](https://de.wikipedia.org/wiki/Axonometrie#Bildachsen_und_Verzerrungen)e Ansicht ([dimetric](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types) view) zu erreichen. Für eine wahrlich (truly) trimetrische Ansicht muss die 3D-Ansicht im [orthographischen Modus](Std_OrthographicCamera/de.md) sein, aber der Befehl funktioniert auch, wenn die Ansicht im [perspektivischen Modus](Std_PerspectiveCamera/de.md) ist.

![](images/Std_ViewDimetric_example.svg ) 
*Das [Achsenkreuz](Std_AxisCross/de.md) und ein Würfel in dimetrischer Ansicht*

## Anwendung

1.  Wähle die **Ansicht → Standardansichten → Axonometric → <img src="images/Std_ViewDimetric.svg" width=16px> Dimetrisch**-Option aus dem Menü.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Um die Ansicht auf dimetrisch zu ändern, verwende die Methode `viewDimetric` des AktiveAnsicht-Objekts. Diese Methode ist nicht verfügbar, wenn sich FreeCAD im Konsolenmodus befindet.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewDimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewDimetric/de
