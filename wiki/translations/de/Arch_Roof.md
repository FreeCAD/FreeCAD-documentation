---
- GuiCommand:/de
   Name:Arch Roof
   Name/de:Arch Dach
   MenuLocation:Arch → Dach
   Workbenches:[Arch](Arch_Workbench/de.md)
   Shortcut:**R** **F**
   SeeAlso:[Arch Struktur](Arch_Structure/de.md), [Arch Wand](Arch_Wall/de.md)
---

# Arch Roof/de



## Beschreibung

Das **<img src="images/Arch_Roof.svg" width=16px> [Arch Dach](Arch_Roof.md)** Werkzeug erlaubt die Erstellung eines geneigten Daches aus einem ausgewählten Linienzug. Das erstellte Dach Objekt ist parametrisch und behält seine Verbindung zum Basisobjekt. Das Prinzip ist, dass jeder Kante ein Dachprofil (Neigung, Breite, Überhang, Dicke) zugewiesen wird.

**Hinweis:** Dieses Werkzeug befindet sich noch in der Entwicklung und kann bei sehr komplexen Formen fehlschlagen.

<img alt="" src=images/RoofExample.png  style="width:600px;"> 
*Ansicht von oben auf das Dach eines Gebäudemodell mit einer gewissen Transparenz*



## Anwendung


<div class="mw-translate-fuzzy">

1.  Erstelle einen Linienzug entgegen dem Uhrzeigersinn und wähle ihn aus
    -   <img alt="" src=images/CounterclockwiseWire.png  style="width:600px;">

2.  Drücke die **<img src="images/Arch_Roof.svg" width=16px> [Arch Dach](Arch_Roof/de.md)** Taste oder drücke **R**, dann **F** Tasten

3.  Das Standard Dach Objekt könnte eine seltsame Form haben, weil das Werkzeug nicht alle notwendigen Informationen hat

4.  Nachdem erstellen des Standard Dachs, doppelklicke auf das Objekt in der [Baumansicht](tree_view/de.md), um auf alle Eigenschaften zuzugreifen und sie zu bearbeiten. Der Winkel muss zwischen 0 und 90 liegen.
    -   ![](images/RoofTable.png )

5.  Jede Linie entspricht einer Dachscheibe. Du kannst also für jede Dachscheibe die gewünschten Eigenschaften festlegen.

6.  Um Dir zu helfen, kannst Du `Winkel` oder `Run` auf `0` setzen und eine `relative Id` definieren, so dass eine automatische Berechnung die Daten relativ zu dieser `relative Id` ermittelt.

7.  Es funktioniert folgendermaßen:
    1.  Falls `Angle &#61; 0` und `Run &#61; 0`, dann ist das Profil identisch zum relativen Profil
    2.  Falls `Angle &#61; 0`, dann wird der `Angle` berechnet, so dass die Höhe die gleiche wie beim relativen Profil ist
    3.  Falls `Run &#61; 0`, dann wird der `Run` berechnet, so dass die Höhe die gleiche wie beim relativen Profil ist

8.  Am Ende setze den Winkel auf 90°, um einen Giebel zu erstellen
    -   <img alt="" src=images/RoofProfil.png  style="width:600px;">

9.  
    **Hinweis**: für ein besseres Verständnis siehe bitte diesen [youtube clip](https://www.youtube.com/watch?v=4Urwru71dVk).


</div>



## Optionen


<div class="mw-translate-fuzzy">

-   Dächer teilen die gemeinsamen Eigenschaften und Verhaltensweisen aller [Arch Komponenten](Arch_Component/de.md)


</div>



## Eigenschaften

-    {{PropertyData/de|Winkel}}: Liste der Neigungswinkel der Sparren (ein Winkel für jede Kante des Linienzuges).

-    {{PropertyData/de|Runs}}: Liste der Breite der Dachscheiben (ein Run für jede Kante des Linienzuges).

-    {{PropertyData/de|IdRel}}: Liste von Relation zwischen Winkel und Dachneigung

-    {{PropertyData/de|Dicke}}: Liste der Stärken der Dachsparren (eine Stärke pro Kante im Linienzug).

-    {{PropertyData/de|Überhang}}: Liste der Überhänge der Dachsparren (ein Überhang für jede Kante des Linienzuges).

-    {{PropertyData/de|Fläche}}: Der Flächenindex des zu verwendenden Basisobjekts (nicht wirklich genutzt)

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das Dach Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole durch Verwenden der folgenden Funktion verwendet werden:


</div>


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```

-   Erstellt ein `Roof` Objekt basierend auf dem vorgegebenen `baseobj`, das ein geschlossener Linienzug oder ein Festkörper sein kann.
    -   Falls `baseobj` ein Linienzug ist, kannst Du eine Liste von `angles` (Winkeln), `run` (Auflage?), `idrel`, `thickness` (Stärke) und `overhang` (Überhang) für jede Kante des Linienzuges vorgeben, um die Dachform zu definieren. Der Standardwert für Winkel ist 45 und die Liste wird automatisch komplettiert, so dass sie mit der Anzahl von Kanten übereinstimmt.
    -   Die Listen werden automatisch komplettiert, damit die Anzahl mit der Anzahl der Kanten des Linienzuges übereinstimmt.

Beispiel:


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Roof/de
