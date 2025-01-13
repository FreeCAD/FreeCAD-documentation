---
 GuiCommand:
   Name: Arch Truss
   Name/de: Arch Fachwerkträger
   MenuLocation: 3D/BIM , Träger
   Workbenches: BIM_Workbench/de
   Version: 0.19
---

# Arch Truss/de



## Beschreibung

Das Werkzeug **Arch Fachwerkträger** baut einen [Fachwerkträger](https://de.wikipedia.org/wiki/Fachwerk) (Truss-Objekt) auf, entweder aus einem ausgewählten linearen Objekt (d.h.einer [Draft-Linie](Draft_Line/de.md) oder einer [Skizze](Sketcher_NewSketch/de.md)) oder von Grund auf neu, wenn beim Aufruf des Befehls kein Objekt ausgewählt ist.

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">



## Anwendung



### Aus einem ausgewählten Objekt erstellen 

1.  Eine einzelne Linie in einem Arbeitsbereich nach Wahl erstellen.
2.  Diese Linie auswählen.
3.  Die Schaltfläche **<img src="images/Arch_Truss.svg" width=16px> [Arch Träger](Arch_Truss/de.md)
**
4.  Die Einstellungendes Trägers wie gewünscht anpassen.



### Von Grund auf neu erstellen 

1.  Sicherstellen, dass nichts ausgewählt ist.
2.  Die Schaltfläche **<img src="images/Arch_Truss.svg" width=16px> [Arch Träger](Arch_Truss/de.md)** drücken.
3.  In die 3D-Ansicht klicken, um einen ersten Punkt festzulegen oder die X-, Y- und Z-Koordinaten eingeben.
4.  In die 3D-Ansicht klicken, um einen zweiten Punkt festzulegen oder die X-, Y- und Z-Koordinaten eingeben.
5.  Die Eigenschaften des Trägers wie gewünscht anpassen.



## Eigenschaften



### Daten

-    **TrussAngle**: Der Winkel des Trägers

-    **SlantType**: Der Neigungstyp dieses Trägers

-    **Normal**: Die normale Ausrichtung dieses Trägers

-    **HeightStart**: Die Höhe des Trägers an der Startposition

-    **HeightEnd**: Die Höhe des Trägers an der Endposition

-    **StrutStartOffset**: Ein optionaler Startversatz für die obersten Strebe

-    **StrutEndOffset**: Ein optionaler Endversatz für die obere Strebe

-    **StrutHeight**: Die Höhe der oberen und unteren Hauptelemente des Trägers

-    **StrutWidth**: Die Breite der oberen und unteren Hauptelemente des Trägers

-    **RodType**: Der Typ der mittleren Elemente des Trägers

-    **RodDirection**: Die Richtung der Stäbe

-    **RodSize**: Der Durchmesser oder die Breite der Stäbe

-    **RodSections**: Die Anzahl der Stababschnitte

-    **RodEnd**: Ob der Träger am Ende einen Stab hat

-    **RodMode**: Wie die Stäbe zu zeichnen sind



## Skripten

Das Werkzeug Fachwerkträger kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus durch Verwendung der folgenden Funktion verwendet werden:


```python
Truss = makeFence([baseobj])
```

Beispiel:


```python
import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0,0,0)
p2 = FreeCAD.Vector(2000,0,0)
baseline = Draft.makeLine(p1,p2)
truss = Arch.makeTruss(baseline)
truss.HeightStart = 200
truss.HeightEnd = 400
# adjust other needed properties
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Truss/de
