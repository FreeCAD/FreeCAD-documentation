---
- GuiCommand:
   Name: Part Cone
   Name/de: Part Kegel
   MenuLocation: Formteil - Grundkörper - Kegel
   Workbenches: [Part](Part_Workbench/de.md)
   SeeAlso: [Part Grundelemente](Part_Primitives/de.md)
---

# Part Cone/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Cone.svg  style="width:24px;"> **Part Kegel** erstellt einen parametrischen Volumenkörper, einen Kegel. Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt die Unterseite des Kegels auf der XY-Ebene mit ihrem Mittelpunkt im Ursprung.

Standardmäßig ist der Part-Kegel ein Kegelstumpf. Er kann in einen Kegel mit Spitze gewandelt werden, indem die {{PropertyData/de|Radius1}} oder die {{PropertyData/de|Radius2}} auf Null gesetzt wird. Er kann in ein Kegelsegment gewandelt werden, durch Änderung der {{PropertyData/de|Winkel}}.

<img alt="" src=images/Part_Cone_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Cone.svg" width=16px> [Part Kegel](Part_Cone/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Cone.svg" width=16px> Kegel** auswählen.
2.  Der Kegel wird erstellt.
3.  Wahlweise die Abmaße und die {{PropertyData/de|Placement}} des Kegels anpassen durch eine der folgenden Möglichkeiten:
    -   Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Der Aufgabenbereich **Geometrische Grundelemente** wird geöffnet.
        2.  Eine oder mehrere Eigenschaften ändern.
        3.  Das Objekt wird in der [3D-Ansicht](3D_view/de.md) dynamisch aktualisiert.
        4.  Die Schaltfläche **OK** drücken.
    -   Die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) anpassen.
    -   Die {{PropertyData/de|Placement}} mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) ändern.



## Beispiel

![Part-Kegel aus dem Skriptbeispiel](images/Part_Cone_Scripting_Example.png )

Ein Part-Kegel-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde, wird hier dargestellt.



## Hinweise

-   Ein Part Kegel kann auch mit dem Befehl <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Grundkörper](Part_Primitives/de.md) erstellt werden. Mit dem Befehl können die Abmaße und die Positionierung zum Zeitpunkt der Erstellung festgelegt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Kegel-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

Das Objekt hat dieselben Befestigungseigenschaften wie ein [Part Part2DObject](Part_Part2DObject/de#Daten.md).


{{TitleProperty|Cone}}

-    {{PropertyData/de|Radius1|Length}}: Der Radius der Grundfläche des Kegels. Kann {{Value|0mm}} sein, wenn {{PropertyData/de|Radius2}} größer als {{Value|0mm}} ist. Der Standardwert ist {{Value|2mm}}.

-    {{PropertyData/de|Radius2|Length}}: Der Radius der Deckfläche des Kegels. Kann {{Value|0mm}} sein, wenn {{PropertyData/de|Radius1}} größer als {{Value|0mm}} ist. Der Standardwert ist {{Value|4mm}}.

-    {{PropertyData/de|Height|Length}}: Die Höhe des Kegels. Der Standardwert ist {{Value|10mm}}.

-    {{PropertyData/de|Angle|Angle}}: Der Winkel der Kreisbögen, die die Grund- und Deckflächen des Kegels festlegen. Wertebereich: {{Value|0° &lt; value &lt;&#61; 360°}}. Der Standardwert ist {{Value|360°}}. Ist er kleiner als {{Value|360°}}, ist der resultierende Festkörper ein Kegelsegment.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Ein Part Kegel wird mit der Methode `addObject()` des Dokuments erstellt.


```python
cone = FreeCAD.ActiveDocument.addObject("Part::Cone", "myCone")
```

-   Wobei {{Incode|"myCone"}} der Name des Objekts ist.
-   Die Funktion gibt das neu erstellte Objekt zurück.

Beispiel:


```python
import FreeCAD as App

doc = App.activeDocument()

cone = doc.addObject("Part::Cone", "myCone")
cone.Radius1 = 5
cone.Radius2 = 10
cone.Height = 50
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(30, 60, 15))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Cone/de
