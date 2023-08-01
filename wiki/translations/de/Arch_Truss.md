---
- GuiCommand:
   Name: Arch Truss
   Name/de: Arch Traverse
   MenuLocation: Arch - Traverse
   Workbenches: [Arch](Arch_Workbench/de.md)
   Version: 0.19
---

# Arch Truss/de

## Beschreibung

Das [Architektur Fachwerkswerkzeug](Arch_Truss/de.md) baut ein [Fachwerk](https://de.wikipedia.org/wiki/Fachwerk)sobjekt auf, entweder aus einem ausgewählten linearen Objekt (z.B. [Entwurf Linie](Draft_Line/de.md) oder [Skizze](Sketcher_NewSketch/de.md)), oder von Grund auf neu, wenn beim Aufruf des Befehls kein Objekt ausgewählt ist.

<img alt="" src=images/Arch_Truss_example.png  style="width:600px;">

## Anwendung

### Erzeugen aus einem ausgewählten Objekt 

1.  Benutze einen Arbeitsbereich deiner Wahl zum Erstellen einer einzelnen Linie
2.  Wähle diese Linie
3.  Drücke die **<img src="images/Arch_Truss.svg" width=16px> [Arch Traverse](Arch_Truss/de.md)**-Schaltfläche
4.  Passe die Traverseneinstellungen an deine Bedürfnisse an

### Erzeugen von Grund auf 

1.  Stelle sicher, dass nichts ausgewählt ist
2.  Drücke die **<img src="images/Arch_Truss.svg" width=16px> [Arch Traverse](Arch_Truss/de.md)**-Schaltfläche
3.  Klicke in die 3D-Ansicht, um einen ersten Punkt zu definieren oder gib die X-, Y- und Z-Koordinaten ein
4.  Klicke in die 3D-Ansicht, um einen zweiten Punkt zu definieren oder gib die X-, Y- und Z-Koordinaten ein
5.  Passe die Traverseneigenschaften an deine Bedürfnisse an

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

Das Traversen-Werkzeug kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole heraus durch Verwendung der folgenden Funktion verwendet werden:


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



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Truss/de
