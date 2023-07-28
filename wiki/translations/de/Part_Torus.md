---
- GuiCommand:/de
   Name:Part Torus
   Name/de:Part Torus
   MenuLocation:Formteil → Grundkörper → Torus
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundelemente](Part_Primitives/de.md)
---

# Part Torus/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Torus.svg  style="width:24px;"> **Part Torus** erstellt einen parametrischen Volumenkörper, einen Torus. Er ist das Ergebnis der Austragung eines Kreises entlang eines kreisförmigen Pfades. Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt der kreisförmige Pfad auf der XY-Ebene und seine Mitte im Ursprung.

Ein Part-Torus kann in ein Torussegment gewandelt werden, durch Änderung der Daten-EigenschaftAngle3 (Umfangswinkel). Durch Änderung der {{PropertyData/de|Angle1}} und/oder der {{PropertyData/de|Angle2}} kann das Austragungsprofil in ein Kreissegment geändert werden.

<img alt="" src=images/Part_Torus_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Torus.svg" width=16px> [Torus](Part_Torus/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Torus.svg" width=16px> Torus** auswählen.
2.  Der Torus wird erstellt.
3.  Wahlweise die Abmaße und {{PropertyData/de|Placement}} des Torus anpassen durch eine der folgenden Möglichkeiten:
    -   Ein Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Der Aufgabenbereich **Geometrische Grundkörper** wird geöffnet.
        2.  Eine oder mehrere Eigenschaften ändern.
        3.  Das Objekt wird in der [3D-Ansicht](3D_view/de.md) dynamisch aktualisiert.
        4.  Die Schaltfläche **OK** drücken.
    -   Die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) ändern.
    -   Die {{PropertyData/de|Placement}} mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) ändern.



## Beispiel

![Part-Torus aus dem Skriptbeispiel](images/Part_Torus_Scripting_Example.png )

Ein Part-Torus-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde, wird hier dargestellt.



## Hinweise

-   Ein Part kann auch mit dem Befehl <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Grundkörper](Part_Primitives/de.md) erstellt werden. Mit dem Befehl können die Abmaße und die Positionierung zum Zeitpunkt der Erstellung festgelegt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Torus-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

Das Objekt hat dieselben Befestigungseigenschaften wie ein [Part Part2DObject](Part_Part2DObject/de#Daten.md).


{{TitleProperty|Torus}}

-    {{PropertyData/de|Radius1|Length}}: Der Radius des kreisförmigen Pfades des Torus. Der Standardwert ist {{Value|10mm}}.

-    {{PropertyData/de|Radius2|Length}}: Der Radius des kreisförmigen Profils desTorus. Der Standardwert ist {{Value|2mm}}.

-    {{PropertyData/de|Angle1|Angle}}: Der Startwinkel des kreisförmigen Profils. Wertebereich: {{Value|-180° &lt;&#61; Wert &lt;&#61; 180°}}. Der Standardwert ist {{Value|-180°}}.

-    {{PropertyData/de|Angle2|Angle}}: Der Endtwinkel des kreisförmigen Profils. Wertebereich: {{Value|-180° &lt;&#61; Wert &lt;&#61; 180°}}. Der Standardwert ist {{Value|180°}}. Ist der Gesamtwinkel des kreisförmigen Profils kleiner als {{Value|360°}}, hat das Profil die Form eines Tortenstücks.

-    {{PropertyData/de|Angle3|Angle}}: Der Winkel des kreisförmigen Pfades des Torus. Wertebereich: {{Value|0° &lt; Wert &lt;&#61; 360°}}. Der Standardwert ist {{Value|360°}}. Ist er kleiner als {{Value|360°}}, ist der resultierende Festkörper ein Torussegment.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Ein Part Torus wird mit der Methode `addObject()` des Dokuments erstellt.


```python
torus = FreeCAD.ActiveDocument.addObject("Part::Torus", "myTorus")
```

-   Wobei {{Incode|"myTorus"}} der Name des Objekts ist.
-   Die Funktion gibt das neu erstellte Objekt zurück.

Beispiel:


```python
import FreeCAD as App

doc = App.activeDocument()

torus = doc.addObject("Part::Torus", "myTorus")
torus.Radius1 = 20
torus.Radius2 = 10
torus.Angle1 = -90
torus.Angle2 = 45
torus.Angle3 = 270
torus.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 45, 10))

doc.recompute()
```





{{Part_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Torus/de
