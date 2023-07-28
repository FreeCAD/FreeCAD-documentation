---
- GuiCommand:/de
   Name:Part Sphere
   Name/de:Part Kugel
   MenuLocation:Part → Grundkörper → Kugel
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:[Part Grundelemente](Part_Primitives/de.md)
---

# Part Sphere/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Sphere.svg  style="width:24px;"> **Part Kugel** erstellt einen parametrischen Volumenkörper, eine Kugel. Sie ist das Ergebnis der Drehung eines Kreisbogens um eine Achse. Im Koordinatensystem durch ihre {{PropertyData/de|Placement}} festgelegt, liegt ihr Mittelpunkt im Ursprung und Ihre Drehachse ist die Z-Achse.

Eine Part-Kugel kann oben und/oder unten beschnitten werden, indem man die {{PropertyData/de|Angle1}} und die {{PropertyData/de|Angle2}} ändert (die Winkel vom Äquator in Richtung der Pole). Sie kann in ein Kugelsegment gewandelt werden, durch Änderung der {{PropertyData/de|Angle3}} (Umfangswinkel).

<img alt="" src=images/Part_Sphere_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Sphere.svg" width=16px> [Kugel](Part_Sphere.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Sphere.svg" width=16px> Kugel** auswählen.
2.  Die Kugel wird erstellt.
3.  Wahlweise die Abmaße und die {{PropertyData/de|Placement}} der Kugel ändern durch eine der folgenden Möglichkeiten:
    -   Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Der Aufgabenbereich **Geometrische Grundelemente** wird geöffnet.
        2.  Eine oder mehrere Eigenschaften ändern.
        3.  Das Objekt wird in der [3D-Ansicht](3D_view/de.md) dynamisch aktualisiert.
        4.  Die Schaltfläche **OK** drücken.
    -   Die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) anpassen.
    -   Die {{PropertyData/de|Placement}} mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) ändern.



## Beispiel

![Part-Kugel aus dem Skriptbeispiel](images/Part_Sphere_Scripting_Example.png )

Ein Part-Kugel-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde wird hier dargestellt.



## Hinweise

-   Eine Part Kugel kann auch mit dem Befehl <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Grundkörper](Part_Primitives/de.md) erstellt werden. Mit dem Befehl können die Abmaße und die Positionierung zum Zeitpunkt der Erstellung festgelegt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Kugel-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

Das Objekt hat dieselben Befestigungseigenschaften wie ein [Part Part2DObject](Part_Part2DObject/de#Daten.md).


{{TitleProperty|Kugel}}

-    {{PropertyData/de|Radius|Length}}: Der Radius der Kugel. Der Standardwert ist {{Value|5mm}}.

-    {{PropertyData/de|Angle1|Angle}}: Der Startwinkel des Kreisbogenprofils der Kugel. Wertebereich: {{Value|-90° &lt;&#61; Wert &lt;&#61; 90°}}. Darf nicht genau so groß sein wie {{PropertyData/de|Angle2}}. Der Standardwert ist {{Value|-90°}}.

-    {{PropertyData/de|Angle2|Angle}}: Der Endwinkel des Kreisbogenprofils der Kugel. Wertebereich: {{Value|-90° &lt;&#61; Wert &lt;&#61; 90°}}. Darf nicht genau so groß sein wie {{PropertyData/de|Angle1}}. Der Standardwert ist {{Value|90°}}. Ist der Gesamtwinkel des Kreisbogenprofils kleiner als {{Value|180°}}, wird die Kugel beschnitten und erhält eine ebene Fläche an ihrer Ober- und/oder Unterseite.

-    {{PropertyData/de|Angle3|Angle}}: Der vollständige Drehwinkel der Kugel. Wertebereich: {{Value|0° &lt; Wert &lt;&#61; 360°}}. Der Standardwert ist {{Value|360°}}. Ist er kleiner als {{Value|360°}}, ist der resultierende Festkörper ein Kugelsegment.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Eine Part Kugel wird mit der Methode `addObject()` des Dokuments erstellt.


```python
sphere = FreeCAD.ActiveDocument.addObject("Part::Sphere", "mySphere")
```

-   Wobei {{Incode|"mySphere"}} der Name des Objekts ist.
-   Die Funktion gibt das neu erstellte Objekt zurück.

Beispiel:


```python
import FreeCAD as App

doc = App.activeDocument()

sphere = doc.addObject("Part::Sphere", "mySphere")
sphere.Radius = 20
sphere.Angle1 = -30
sphere.Angle2 = 45
sphere.Angle3 = 90
sphere.Placement = App.Placement(App.Vector(3, 9, 11), App.Rotation(75, 60, 30))

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sphere/de
