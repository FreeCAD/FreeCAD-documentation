---
 GuiCommand:
   Name: SheetMetal AddCutout
   Name/de: SheetMetal Ausschneiden
   MenuLocation: Sheet Metal , Extrudierter Ausschnitt
   Workbenches: SheetMetal_Workbench/de
   Shortcut: **E** **C**
   Version: 0.5.04
---

# SheetMetal AddCutout/de



## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_AddCutout.svg  style="width:32px;"> [Extrudierter Ausschnitt](SheetMetal_AddCutout/de.md) erstellt aus einer Skizze einen extrudierten Ausschnitt.

Der Unterschied zwischen einem \'normalen\' Ausschnitt und einem extrudierten Ausschnitt ist, dass bei letzterem die Kanten senkrecht zur ausgewählten Fläche des Blechobjekts ausgeführt werden. Die Auswirkung des Befehls ist nur sichtbar, wenn die Skizze nicht parallel zur Fläche verläuft.

![](images/SheetMetal_AddCutout_Example.png )



*Extrudierter Ausschnitt auf Basis einer kreisförmigen Skizze*



## Anwendung

1.  Eine ebene Fläche und eine Skizze mit einer geschlossenen Kontur auswählen (in beliebiger Reihenfolge).
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/SheetMetal_AddCutout.svg" width=16px> [Extrudierter Ausschnitt](SheetMetal_AddCutout/de.md)** drücken.
    -   Den Menüeintrag **Sheet Metal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Extrudierter Ausschnitt** auswählen.
    -   Ein Rechtsklick in die [Baumansicht](Tree_view/de.md) oder die [3D-Ansicht](3D_view/de.md) und die Menüoption **Sheet Metal → <img src="images/SheetMetal_AddCutout.svg" width=16px> Extrudierter Ausschnitt** im Kontextmenü auswählen.
    -   Das Tastaturkürzel **E** dann **C**.
3.  Das [Aufgaben-Fenster](Task_panel/de.md) **Extruded Cutout Parameters** wird geöffnet.
4.  Wahlweise die Schaltfläche **Face** drücken, um die ebene Fläche neu auszuwählen.
5.  Wahlweise die Schaltfläche **Sketch** drücken, um erneut eine Skizze auszuwählen.
6.  Wahlweise die Parameter im Aufgaben-Fenster anpassen.
7.  Die Schaltfläche **OK** rücken, um den Befehl abzuschließen und das Aufgaben-Fenster zu schließen.
8.  Ein **ExtrudedCutout**-Objekt wird erstellt und enthält ein oder mehrere Löcher in einer Reihe durch das Objekt.
9.  Wahlweise die Parameter im [Eigenschafteneditor](Property_editor/de.md) anpassen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-ExtrudedCutout-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet oder, wenn es sich in einem [PartDesign-Körper](PartDesign_Body/de.md) befindet, von einem [PartDesign Formelement](PartDesign_Feature/de.md) und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{Properties_Title|Extruded Cutout}}

-    {{PropertyData/de|Cut Side|Enumeration}}: Standardwert {{value|Inside}} (innerhalb). Seite des Ausschnitts.

-    {{PropertyData/de|Cut Type|Enumeration}}: Standardwert {{value|Through everything both sides}} (beidseitig durch alles). Art des Ausschnitts.

-    {{PropertyData/de|Extrusion Length1|Length|hidden}}: Standardwert {{value|500,0 mm}}. Länge in Extrusionsrichtung 1.

-    {{PropertyData/de|Extrusion Length2|Length|hidden}}: Standardwert {{value|500,0 mm}}. Länge in Extrusionsrichtung 2.

-    {{PropertyData/de|Selected Face|LinkSub}}: Das Objekt und die ausgewählte Fläche.

-    {{PropertyData/de|Sketch|Link}}: Die Skizze für den Ausschnitt.


{{Properties_Title|Extruded Cutout Improvements}}

-    {{PropertyData/de|Improve Cut|Bool}}: Standardwert {{value|False}}. Verbessert die Schnittgeometrie, wenn sie den Schnittbereich erreicht. {{value|True}} sollte nur ausgewählt werden, wenn der Ausschnitt korrigiert werden muss, da es sehr langsam sein kann.

-    {{PropertyData/de|Improve Level|IntegerConstraint|hidden}}: Standardwert {{value|4}}. Niveau der Qualität der Schnittverbesserung. Bei einem Wert größer als 10 kann es eine sehr lange Zeit dauern.

-    {{PropertyData/de|Refine|Bool}}: Standardwert {{value|False}}. Verfeinert die Geometrie.



---
⏵ [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > SheetMetal AddCutout/de
