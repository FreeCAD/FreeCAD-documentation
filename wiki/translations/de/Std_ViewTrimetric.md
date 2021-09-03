---
- GuiCommand:/de
   Name:Std ViewTrimetric
   MenuLocation:Ansicht → Standardansichten → Axonometrisch → Trimetrisch
   Workbenches:Alle
   SeeAlso:[Std AnsichtIsometrisch](Std_Isometric/de.md), [Std AnsichtDimetrisch](Std_ViewDimetric/de.md)
---

## Beschreibung

Der **Std AnsichtTrimetrisch**-Befehl richtet die Kamera in der aktiven [3D-Ansicht](3D_view/de.md) neu aus, um eine [trimetrisch](https://de.wikipedia.org/wiki/Axonometrie#Bildachsen_und_Verzerrungen)e Ansicht ([trimetric](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types) view) zu erreichen. Für eine wahrlich (truly) trimetrische Ansicht muss die 3D-Ansicht im [orthographischen Modus](Std_OrthographicCamera/de.md) sein, aber der Befehl funktioniert auch, wenn die Ansicht im [perspektivischen Modus](Std_PerspectiveCamera/de.md) ist.

![](images/Std_ViewTrimetric_example.svg ) *Das [Achsenkreuz](Std_AxisCross/de.md) und ein Würfel in trimetrischer Ansicht*

## Anwendung

1.  Wähle die **Ansicht → Standardansichten → Axonometric → <img src="images/Std_ViewTrimetric.svg" width=16px> Trimetrisch**-Option aus dem Menü.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit der `viewTrimetric`-Methode des Objektes der aktiven Ansicht wechselt man in die trimetrische Ansicht. Diese Methode gibt es im FreeCAD-Konsolenmodus nicht.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTrimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}  
