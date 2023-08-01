---
- GuiCommand:
   Name:Draft Circle
   Name/de:Draft Kreis
   MenuLocation:Entwurf - Kreis
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**C** **I**
   Version:0.7
   SeeAlso:[Draft Bogen](Draft_Arc/de.md), [Draft Bogen 3Punkte](Draft_Arc_3Points/de.md)
---

# Draft Circle/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Draft_Circle.svg  style="width:24px;"> **Draft Kreis** erstellt einen Kreis auf der aktuellen [Arbeitsebene](Draft_SelectPlane/de.md) aus Mittelpunkt und Radius. Der Radius kann durch Indizieren eines Punktes festgelegt werden.

Ein Draft-Kreis kann in einen Bogen gewandelt werden, indem seine {{PropertyData/de|First Angle}} und {{PropertyData/de|Last Angle}} auf unterschiedliche Werte gesetzt werden

<img alt="" src=images/Draft_Circle_example.jpg  style="width:400px;"> 
*Ein durch zwei Punkte festgelegter Kreis aus Mittelpunkt und Radius*



## Anwendung

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Drücke die **<img src="images/Draft_Circle.png" width=16px> [Kreis](Draft_Circle/de.md)** Schaltfläche oder drücke **C**, dann **I** Tasten.
2.  Klicke einen ersten Punkt in der 3D Ansicht oder tippe eine Koordinate und drücke die **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**-Schaltfläche.
3.  Klicke einen zweiten Punkt in der 3D Ansicht oder gib einen Wert für den Radius ein.


</div>



## Optionen

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

## Optionen 

-   Die primäre Anwendung des Kreis-Werkzeugs erfolgt durch Auswahl von zwei Punkten: dem Mittelpunkt und einem Punkt auf dem Umkreis zur Definition des Radius.
-   Durch Drücken von **Alt** kannst Du eine Tangente anstatt eines Punkts zur Definition des Basiskreises des Bogens auswählen. Du kannst deshalb verschiedene Kreisarten durch Auswahl von ein, zwei oder drei Tangenten erstellen.
-   Um Koordinaten manuell einzugeben, gibt einfach die Ziffern ein, drücke dann **Enter** zwischen den X-, Y- und Z-Komponenten. Du kannst den **<img src="images/Draft_AddPoint.svg" width=16px> Punkt hinzufügen**-Button drücken, nachdem die gewünschten Werte eingegeben wurden.
-   Drücke **Alt**+**N** oder klicke das Ankreuzkästchen zum de/aktivieren des Fortsetzungsmodus. Wenn der Fortsetzungsmodus aktiviert ist, wird das Kreis-Tool nach Eingabe des zweiten Punkts neugestartet, um das Zeichnen eines weiteren Kreises ohne erneutes Drücken des Kreis-Buttons zu ermöglichen.

Klicke das Ankreuzkästchen zum de/aktivieren des **'''Gefüllt'''**-Modus. Wenn der \'Geüllt\'-Modus aktiviert ist, wird der Kreis mit einer Fläche gefüllt.

-   Drücke **Strg** während des Zeichnens, um das [Einrasten](Draft_Snap/de.md) Deines Punkts an der nächsten Einrastposition zu erzwingen, unabhängig vom Abstand.
-   Drücke **Shift** während des Zeichnens, um Deinen Punkt horizontal oder vertikal in Relation zum ersten einzuschränken.
-   Drücke **Esc** oder den **'''Schließen'''**-Button, um den aktuellen Befehl abzubrechen.
-   Der Kreis kann nach der Erstellung durch Setzen von unterschiedlichen Wertes für die Eigenschaften des ersten und letzten Winkels in einen Kreisbogen umgewandelt werden.


</div>



## Hinweise


<div class="mw-translate-fuzzy">

Der Kreis kann durch doppelklicken des Elements in der Baumansicht geändert werden oder durch drücken der **<img src="images/Draft_Edit.svg" width=16px> [Draft Bearbeiten](Draft_Edit/de.md)** Schaltfläche. Dann können der Mittel- und die Radiuspunkte an eine neue Position verschoben werden.


</div>



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md) und [Draft Einstellungen](Draft_Preferences/de.md).

-   To change the number of decimals used for the input of coordinates and radii: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Circle](Part_Circle.md) instead of a Draft Circle.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft-Kreis-Objekt wird von einem [Part Part2DObject](Part_Part2DObject/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:



### Daten


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Daten 

-    {{PropertyData/de|First Angle}}: Gibt den Startwinkel des Kreises an; normalerweise 0°.

-    {{PropertyData/de|Last Angle}}: Gibt den Endwinkel des Kreises an; normalerweise 0°.

-    {{PropertyData/de|Radius}}: Gibt den Radius des Kreises an.

-    {{PropertyData/de|Make Face}}: Gibt an, ob der Kreis ausgefüllt wird. Falls auf `True` gesetzt, wird eine Fläche erstellt, ansonsten wird nur der Umfang als Teil des Objekts betrachtet. Diese Eigenschaft funktioniert nur, wenn die Form einen vollen Umfang hat.

:   Damit es ein Vollkreis ist, sollten **Anfangswinkel** und **Endwinkel** den gleichen Wert haben, ansonsten wird ein [Draft Arc](Draft_Arc/de.md) angezeigt. Die Werte 0° und 360° werden nicht als gleich angesehen, so dass der Kreis bei Verwendung dieser beiden Werte keine Fläche bildet.


</div>



### Ansicht


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Ansicht 

-    {{PropertyView/de|Pattern}}: definiert ein [Entwurfsmuster](Draft_Pattern/de.md), mit dem die Kreisoberfläche gefüllt wird. Diese Eigenschaft funktioniert nur, wenn {{PropertyData/de|Make Face}} auf `True` und {{PropertyView/de|Display Mode}} auf \"Flat Lines\" gesetzt ist.

-    {{PropertyView/de|Pattern Size}}: gibt die Größe des [Musters](Draft_Pattern/de.md) an.


</div>



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Zum Erstellen eines Draft-Kreises wird die Methode `make_circle` des Draft-Moduls verwendet ({{Version/de|0.19}}). Diese Methode ersetzt die veraltete Methode `makeCircle`.


```python
circle = make_circle(radius, placement=None, face=None, startangle=None, endangle=None, support=None)
circle = make_circle(Part.Edge, placement=None, face=None, startangle=None, endangle=None, support=None)
```


<div class="mw-translate-fuzzy">

-   Erstellt ein `Circle` Objekt mit gegebenem `radius` in mm.
    -   
        `radius`
        
        kann auch eine `Part.Edge` sein, dessen `Curve` Attribut ein `Part.Circle` sein muss.
-   Falls ein `placement` angegeben ist, wird es benutzt. Anderenfalls wird die Form am Ursprung erstellt.
-   Falls `face` auf `True` gesetzt ist, wird der Kreis ausgefüllt, sonst als ein Drahtmodell gezeigt.
-   Falls `startangle` und `endangle` angegeben sind (in Grad) und unterschiedliche Werte haben, werden sie benutzt und das Objekt erscheint als [Draft Bogen](Draft_Arc/de.md).


</div>

Beispiel: 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

circle1 = Draft.make_circle(200)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(1000, 1000, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 0))
circle2 = Draft.make_circle(500, placement=place2)

p3 = App.Vector(-1000, -1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 0))
circle3 = Draft.make_circle(750, placement=place3)

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Circle/de
