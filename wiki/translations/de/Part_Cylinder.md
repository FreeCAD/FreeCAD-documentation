---
 GuiCommand:
   Name: Part Cylinder
   Name/de: Part Zylinder
   MenuLocation: Part , Grundkörper , Zylinder
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Primitives/de
---

# Part Cylinder/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> **Part Zylinder** erstellt einen parametrischen Festkörper, einen Zylinder. Er ist das Ergebnis der Extrusion eines Kreises entlang eines geraden Pfades. Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt die Unterseite des Zylinders auf der XY-Ebene und ihre Mitte im Ursprung.

Ein Part-Zylinder kann in ein Zylindersegment gewandelt werden, indem seine {{PropertyData/de|Winkel}} geändert wird.

<img alt="" src=images/Part_Cylinder_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Cylinder.svg" width=16px> [Zylinder](Part_Cylinder/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Cylinder.svg" width=16px> Zylinder** auswählen.
2.  Der Zylinder wird erstellt.
3.  Wahlweise die Abmessungen und die {{PropertyData/de|Placement}} des Zylinders ändern, indem eine der folgenden Möglichkeiten ausgeführt wird:
    -   Ein Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Das Aufgaben-Fenster **Geometrische Grundkörper** wird geöffnet.
        2.  Eine oder mehrere Eigenschaften Ändern.
        3.  Das Objekt wird dynamisch in der [3D-Ansicht](3D_view/de.md) aktualisiert.
        4.  Die Schaltfläche **OK** drücken.
    -   Die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) anpassen.
    -   Die {{PropertyData/de|Placement}} mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) ändern.



## Beispiel

![Part-Zylinder aus dem Skriptbeispiel](images/Part_Cylinder_Scripting_Example.png )

Ein Part-Zylinder-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde wird hier dargestellt.



## Hinweise

-   Ein Part Zylinder kann auch mit dem Befehl <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Grundkörper](Part_Primitives/de.md) erstellt werden. Mit dem Befehl können die Abmaße und die Positionierung zum Zeitpunkt der Erstellung festgelegt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Zylinder-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

Das Objekt hat dieselben Befestigungseigenschaften wie ein [Part Part2DObject](Part_Part2DObject/de#Daten.md).


{{TitleProperty|Cylinder}}

-    {{PropertyData/de|Radius|Length}}: Der Radius des Kreisbogens, der den Zylinder definiert. Der Standardwert ist {{Value|2mm}}.

-    {{PropertyData/de|Height|Length}}: Die Höhe des Zylinders. Der Standardwert ist {{Value|10 mm}}.

-    {{PropertyData/de|Winkel|Angle}}: Der Winkel des Kreisbogens, der den Zylinder definiert. Gültiger Bereich: {{Value|0° &lt; Wert &lt;&#61; 360°}}. Der Standardwert ist {{Value|360°}}. Wenn er kleiner als {{Value|360°}} ist, ist der resultierende Festkörper ein Zylindersegment.


{{TitleProperty|Prism}}

-    {{PropertyData/de|First Angle|Angle}}: Der Winkel zwischen der Extrusionsrichtung des Zylinders und seiner positiven Z-Achse, gemessen um seine Y-Achse. Der Winkel ist positiv zur positiven X-Achse. Gültiger Bereich: {{Value|0° &lt;&#61; Wert &lt; 90°}}. Der Standardwert ist {{Value|0°}}. {{Version/de|0.20}}

-    {{PropertyData/de|Second Angle|Angle}}: Der Winkel zwischen der Extrusionsrichtung des Zylinders und seiner positiven Z-Achse, gemessen um seine X-Achse. Der Winkel ist positiv zur positiven Y-Achse. Gültiger Bereich: {{Value|0° &lt;&#61; Wert &lt; 90°}}. Der Standardwert ist {{Value|0°}}. {{Version/de|0.20}}



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Ein Part-Zylinder wird mit der Methode `addObject()` des Dokuments erstellt.


```python
cylinder = FreeCAD.ActiveDocument.addObject("Part::Cylinder", "myCylinder")
```

-   Wobei {{Incode|"myCylinder"}} der Name des Objekts ist.
-   Die Funktion gibt das neu erstellte Objekt zurück.

Beispiel:


```python
import FreeCAD as App

doc = App.activeDocument()

cylinder = doc.addObject("Part::Cylinder", "myCylinder")
cylinder.Radius = 10
cylinder.Height = 50
cylinder.Placement = App.Placement(App.Vector(5, 10, 15), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cylinder/de
