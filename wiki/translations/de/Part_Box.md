---
 GuiCommand:
   Name: Part Box
   Name/de: Part Quader
   MenuLocation: Formteil , Grundkörper , Quader 
   Workbenches: Part_Workbench/de
   SeeAlso: Part_Primitives/de
---

# Part Box/de



## Beschreibung

Der Befehl <img alt="" src=images/Part_Box.svg  style="width:24px;"> **Part Quader** erstellt einen parametrischen quaderförmigen Festkörper (Siehe [Quader](https://de.wikipedia.org/wiki/Quader)). Im Koordinatensystem durch seine {{PropertyData/de|Placement}} festgelegt, liegt die Unterseite des Quaders auf der XY-Ebene mit seiner vorderen linken Ecke im Ursprung und seiner Vorderkante parallel zur X-Achse.

<img alt="" src=images/Part_Box_Example.png  style="width:400px;">



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Part_Box.svg" width=16px> [Part Quader](Part_Box/de.md)** drücken.
    -   Den Menüeintrag **Part → Grundkörper → <img src="images/Part_Box.svg" width=16px> Quader** auswählen.
2.  Der Quader wird erstellt.
3.  Wahlweise die Abmessungen und die {{PropertyData/de|Placement}} des Quaders ändern, indem eine der folgenden Möglichkeiten ausgeführt wird:
    -   Ein Doppelklick auf das Objekt in der [Baumansicht](Tree_view/de.md):
        1.  Das Aufgaben-Fenster **Geometrische Grundkörper** wird geöffnet.
        2.  Eine oder mehrere Eigenschaften Ändern.
        3.  Das Objekt wird dynamisch in der [3D-Ansicht](3D_view/de.md) aktualisiert.
        4.  Die Schaltfläche **OK** drücken.
    -   Die Eigenschaften im [Eigenschafteneditor](Property_editor/de.md) anpassen.
    -   Die {{PropertyData/de|Placement}} mit dem Befehl <img alt="" src=images/Std_TransformManip.svg  style="width:16px;"> [Std Bewegen](Std_TransformManip/de.md) ändern.



## Beispiel

![Part-Quader aus dem Skriptbeispiel](images/Part_Box_Scripting_Example.png )

Ein Part-Quader-Objekt, das mit dem [Skriptbeispiel](#Skripten.md) weiter unten erzeugt wurde, wird hier dargestellt.



## Hinweise

-   Ein Part-Quader kann auch mit dem Befehl <img alt="" src=images/Part_Primitives.svg  style="width:16px;"> [Part Grundkörper](Part_Primitives/de.md) erstellt werden. Mit dem Befehl können die Abmaße und die Positionierung zum Zeitpunkt der Erstellung festgelegt werden.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Part-Quader-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Attachment}}

Das Objekt hat dieselben Befestigungseigenschaften wie ein [Part Part2DObject](Part_Part2DObject/de#Daten.md).


{{TitleProperty|Box}}

-    {{PropertyData/de|Length|Length}}: Die Länge des Quader-Objekts. Dies ist die Länge in seiner X-Richtung. Der Standardwert ist {{Value|10mm}}.

-    {{PropertyData/de|Width|Length}}: Die Breite des Quader-Objekts. Dies ist die Länge in seiner Y-Richtung. Der Standardwert ist {{Value|10mm}}.

-    {{PropertyData/de|Height|Length}}: Die Höhe des Quader-Objekts. Dies ist die Länge in seiner Z-Richtung. Der Standardwert ist {{Value|10mm}}.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/), [Part Skripten](Part_scripting/de.md) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Ein Part-Quader wird mit der Methode `addObject()` des Dokuments erstellt.


```python
box = FreeCAD.ActiveDocument.addObject("Part::Box", "myBox")
```

-   Wobei {{Incode|"myBox"}} der Name des Objekts ist.
-   Die Funktion gibt das neu erstellte Objekt zurück.

Beispiel:


```python
import FreeCAD as App

doc = App.activeDocument()

box = doc.addObject("Part::Box", "myBox")
box.Length = 4
box.Width = 8
box.Height = 12
box.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Box/de
