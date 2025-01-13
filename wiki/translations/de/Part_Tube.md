---
 GuiCommand:
   Name: Part Tube
   Name/de: Part Rohr
   MenuLocation: Part , Grundkörper , Rohr erstellen...
   Workbenches: Part_Workbench/de
   Version: 0.19
   SeeAlso: Part_Primitives/de
---

# Part Tube/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Tube.svg  style="width:24px;"> **Part Rohr** erstellt einen parametrischen Volumenkörper, ein Rohr (Hohlzylinder). Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt die Unterseite des Rohrs auf der XY-Ebene mit ihrem Mittelpunkt im Ursprung.

<img alt="" src=images/Part_Tube_Example.png  style="width:400px;">



## Anwendung



### Erstellung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Tube.svg" width=16px> [Hohlzylinder erstellen](Part_Tube/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Tube.svg" width=16px> Hohlzylinder erstellen** auswählen.
2.  Das Aufgaben-Fenster **Rohr** wird geöffnet und eine Vorschau auf das Rohr in der [3D-Ansicht](3D_view/de.md) dargestellt.
3.  Die Maße festlegen.
4.  Die Vorschau wird dynamisch aktualisiert.
5.  Die Schaltfläche **OK** drücken.
6.  Das Rohr wird erstellt.
7.  Wahlweise wird die {{PropertyData/de|Placement}} des Rohrs im [Eigenschafteneditor](Property_editor/de.md) geändert, oder mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md).



### Bearbeiten

1.  Double-click the tube in the [Tree view](Tree_view.md)
2.  The **Tube** task panel opens.
3.  Change one or more dimensions.
4.  The tube is dynamically updated in the [3D view](3D_view.md).
5.  Press the **OK** button.



## Beispiel

![Part-Tube aus dem Skriptbeispiel](images/Part_Tube_Scripting_Example.png )

Ein Part-Tube-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde, wird hier dargestellt.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Tube-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

The object has the same attachment properties as a [Part Part2DObject](Part_Part2DObject#Data.md).


{{TitleProperty|Tube}}

-    {{PropertyData/de|Height|Length}}: Die Höhe des Rohrs. Der Standardwert ist {{Value|10mm}}.

-    {{PropertyData/de|Inner Radius|Length}}: Der Innenradius des Rohrs. Er muss kleiner sein als die {{PropertyData/de|Outer Radius}} und darf {{Value|0}} sein. Der Standardwert ist {{Value|2mm}}.

-    {{PropertyData/de|Outer Radius|Length}}: Der Außenradius des Rohrs. Er muss größer sein als die {{PropertyData/de|Inner Radius}}. Der Standardwert ist {{Value|5mm}}.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

A Part Tube can be created with the {{Incode|addTube()}} method (<small>(v0.20)</small> ) of the Shapes module:


```python
tube = Shapes.addTube(FreeCAD.ActiveDocument, "myTube")
```

-   Where {{Incode|"myTube"}} is the name for the object.
-   The function returns the newly created object.

Beispiel:


```python
import FreeCAD as App
from BasicShapes import Shapes

doc = App.activeDocument()

tube = Shapes.addTube(FreeCAD.ActiveDocument, "myTube")
tube.Height = 20
tube.InnerRadius = 2
tube.OuterRadius = 3
tube.Placement = App.Placement(App.Vector(2, 4, 5), App.Rotation(60, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Tube/de
