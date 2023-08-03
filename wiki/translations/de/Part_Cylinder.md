---
 GuiCommand:
   Name: Part Cylinder
   Name/de: Part Zylinder
   MenuLocation: Formteil , Grundkörper , Zylinder
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Primitives/de
---

# Part Cylinder/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Cylinder.svg  style="width:24px;"> **Part Zylinder** erstellt einen parametrischen Volumenkörper, einen Zylinder. Er ist das Ergebnis der Extrusion eines Kreises entlang eines geraden Pfades. Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt die Unterseite des Zylinders auf der XY-Ebene und ihre Mitte im Ursprung.

Ein Part-Zylinder kann in ein Zylindersegment gewandelt werden durch ändern seiner {{PropertyData/de|Winkel}}.

<img alt="" src=images/Part_Cylinder_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Cylinder.svg" width=16px> [Part Zylinder](Part_Cylinder/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Cylinder.svg" width=16px> Zylinder** auswählen.
2.  Der Zylinder wird erstellt.
3.  Wahlweise die Abmessungen und die {{PropertyData/de|Placement}} des Zylinders ändern, indem eine der folgenden Möglichkeiten ausgeführt wird:
    -   Ein Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Der Aufgabenbereich **Geometrische Grundkörper** wird geöffnet.
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

-    **Radius|Length**: The radius of the circular arc that defines the cylinder. The default is {{Value|2mm}}.

-    **Height|Length**: The height of the cylinder. The default is {{Value|10mm}}.

-    **Angle|Angle**: The angle of the circular arc that defines the cylinder. Valid range: {{Value|0° &lt; value &lt;&#61; 360°}}. The default is {{Value|360°}}. If it is smaller than {{Value|360°}} the resulting solid will be a segment of a cylinder.


{{TitleProperty|Prism}}

-    **First Angle|Angle**: The angle between the extrusion direction of the cylinder and its positive Z axis, measured around its Y axis. The angle is positive towards its positive X axis. Valid range: {{Value|0° &lt;&#61; value &lt; 90°}}. The default is {{Value|0°}}. <small>(v0.20)</small> 

-    **Second Angle|Angle**: The angle between the extrusion direction of the cylinder and its positive Z axis, measured around its X axis. The angle is positive towards its positive Y axis. Valid range: {{Value|0° &lt;&#61; value &lt; 90°}}. The default is {{Value|0°}}. <small>(v0.20)</small> 



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Ein Part Zylinder wird mit der Methode `addObject()` des Dokuments erstellt.


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
