---
- GuiCommand:/de
   Name:Draft Dimension
   Name/de:Entwurf Bemaßung
   MenuLocation:Entwurf → Bemaßung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**D** **I**
   SeeAlso:[BemaßungKippen](Draft_FlipDimension/de.md)[TechDraw Arbeitsbereich](TechDraw_Workbench/de.md)
   Version:0.8
---


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das **<img src="images/Draft_Dimension.svg" width=16px> [Entwurf Bemaßung](Draft_Dimension/de.md)**s Werkzeug erstellt ein Objekt, das den Abstand zwischen zwei Punkten misst und anzeigt; ein dritter Punkt gibt die Position der Bemaßungslinie an.


</div>


<div class="mw-translate-fuzzy">

Das Werkzeug kann Kanten oder Linien messen, die direkt an festen Körpern befestigt sind; wenn sich der Körper ändert, aktualisiert sich die Dimension von selbst. Das Werkzeug kann auch einen Durchmesser oder Krümmungsradius messen, wie er beispielsweise durch einen [Draft Arc](Draft_Arc.md) oder durch die Operationen [Part Fillet](Part_Fillet.md), [Sketcher CreateFillet](Sketcher_CreateFillet.md), und [PartDesign Fillet](PartDesign_Fillet.md) erzeugt wird.


</div>


<div class="mw-translate-fuzzy">

Die resultierende Größe wird in der 3D-Ansicht angezeigt und als Zeichenobjekt behandelt. Das Zeichenobjekt kann auf einer [TechDraw Workbench](TechDraw_Workbench/de.md)-Seite angezeigt werden, in dem man die [Neue Draft-Ansicht](TechDraw_NewDraft/de.md)- oder [TechDraw Neuer Bogen](TechDraw_NewArch/de.md)-Werkzeuge verwendet. Alternativ hat TechDraw seine eigenen Werkzeuge, um Größen anzuzeigen, wie z.B. [TechDraw Längenbemaßung](TechDraw_Dimension_Length/de.md) und [TechDraw Radiusbemaßung](TechDraw_Dimension_Radius/de.md). Diese Tools sind jedoch für die Bereitung technischer Zeichnungen gedacht, wodurch sie die Größen nur auf der Zeichenfläche und nicht in der 3D-Ansicht generieren.


</div>

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Durch drei Punkte definierte geradlinige Bemaßung*

## Create

Siehe auch: [Entwurf Ablage](Draft_Tray/de.md), [Entwurf Fang](Draft_Snap/de.md) und [Entwurf beschränken](Draft_Constrain/de.md).

### Anwendung geradlinige Bemaßung 


<div class="mw-translate-fuzzy">

## Verwendung

1.  Die Schaltfläche **<img src="images/Draft_Dimension.png" width=16px> [Draft-Dimension](Draft_Dimension/de.md)** klicken oder die Tasten **D** und dann **I** betätigen.
2.  Einen Punkt in der 3D-Ansicht anklicken oder eine [Koordinate](Draft_Coordinates/de.md) eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** drücken.
3.  Einen zweiten Punkt in der 3D-Ansicht anklicken oder eine [Koordinate](Draft_Coordinates.md) eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** drücken. Die ersten beiden Punkte den zu messenden Abstand.
4.  Einen dritten Punkt in der 3D-Ansicht anklicken oder eine [Koordinate](Draft_Coordinates.md) eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> [Punkt hinzufügen](Draft_AddPoint/de.md)** drücken. Der letzte Punkt definiert die Position der Bemaßungslinie.


</div>

### Usage radial dimension 

1.  Optionally select a circular edge in the [3D view](3D_view.md).
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
4.  If you have not yet selected an edge do one of the following:
    -   Press **E** or the **<img src="images/view-select.svg" width=16px> Select edge** button and select a circular edge in the [3D view](3D_view.md).
    -   Hold down the **Alt** key, select a circular edge in the [3D view](3D_view.md) and release the **Alt** key.
5.  To position the dimension line do one of the following:
    -   For a diameter dimension:
        -   Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
    -   For a radial dimension:
        -   Hold down the **Shift** key and pick a point in the [3D view](3D_view.md).

### Usage angular dimension 

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
2.  The **Dimension** task panel opens. See [Options](#Options.md) for more information.
3.  Hold down the **Alt** key, select two straight edges in the [3D view](3D_view.md) and release the **Alt** key.
4.  To position the dimension arc pick a point in the [3D view](3D_view.md).
5.  Depending on the edges and the picked point the displayed angle will be the acute (sharp) or obtuse (blunt) angle between the edges, or the angle of one of the edges with the horizontal. In some cases you may have to first add auxiliary geometry ([Draft Lines](Draft_Line.md) for example) to get a particular angle.

### Optionen

Die im Aufgabenpaneel verfügbaren Einzelzeichen Tastaturkürzel können geändert werden. Siehe [Entwurf Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die Standardtastenkürzel.

## Optionen 

-   Drücke die Taste **X**, **Y** oder **Z** nach einem Punkt, um den nächsten Punkt auf die entsprechende Achse festzulegen.
-   Um Koordinaten von Hand einzugeben, tippe einfach die Zahlen gefolgt von **ENTER** zwischen der X-, Y- und Z-Komponente.
-   Drücken von **CTRL** während des Zeichnens lässt [snapping](Draft_Snap.md) Deinen Punkt bei der nächsten Rastposition einschnappen, unabhängig vom Abstand.
-   Halten von **SHIFT** legt [constrain](Draft_Constrain.md) die Maßlinie in horizontaler oder vertikaler Richtung fest oder wechselt zwischen Radius und Durchmesser, falls an einem Kreisbogen gearbeitet wird.
-   Tippe auf **R** oder klicke in das Kontrollkästchen, um den **'''Relativ'''** Modus ein- oder abzuschalten. Wenn der Relativmodus ausgewählt ist, sind die Koordinaten des nächsten Punktes relativ zum vorherigen Punkt. Ansonsten sind die Koordinaten absolute zum Ursprung (0,0,0) des Koordinatensystems.
-   Drücke **T** oder klicke das Kontrollkästchen neben **Nächstes**, um es zu de/aktivieren. Bei aktiviertem Nächstes-Modus kannst Du fortlaufende Bemaßungen zeichnen, eine nach der anderen, die die gleichen Basislinie haben.
-   Drücke **ESC** oder den **'''Abbrechen'''**-Button, um den aktuelle Linien-Befehl abzubrechen.
-   Anstatt Messpunkte einzugeben, wird durch Auswahl einer existierenden Kante mit **Alt** die Bemaßung **parametrisch** und merkt sich, mit welcher Kante sie verbunden ist. Wenn sich die Endpunkte der Kante später verschieben, folgt ihnen die Bemaßung.
-   Wenn eine Kante vor dem Beginn des Bemaßungsbefehl gewählt wird, ist die erstellte Bemaßung ebenfalls **parametrisch**.
-   Die Richtung der Bemaßung kann später durch Anpassung der \"Direction\"-Eigenschaft verändert werden.

## Convert

### Anwendung

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.

## Hinweise


<div class="mw-translate-fuzzy">

Die Bemaßung kann durch doppelklicken des Elements in der Baumansicht geändert werden oder durch drücken des **<img src="images/Draft_Edit.svg" width=16px> [Bearbeiten](Draft_Edit/de.md)**-Buttons. Dann kannst Du die Punkte an eine andere Position ziehen.


</div>


<div class="mw-translate-fuzzy">

## Eigenschaften

-    **Start**: Der Startpunkt des zu messenden Abstands

-    **End**: Der Endpunkt des zu messenden Abstands

-    **Dimline**: Ein Punkt, durch den die Maßlinie verlaufen muss

-    **Display Mode**: Gibt an, ob der Text an den Maßlinien ausgerichtet ist, oder immer dem Blickpunkt folgt

-    **Font Size**: Die Größe der Zeichen

-    **Ext Lines**: Die Größe der Erweiterungslinie (zwischen den Messpunkten und der Maßlinie)

-    **Text Position**: Kann benutzt werden, um die Textanzeige an einer bestimmten Position zu erzwingen

-    **Text Spacing**: Gibt den Platz zwischen Text und Maßlinie an

-    **Override**: Zeigt einen Text anstatt des Maßes an. Füge \"\$dim\" in den Text ein, um das Maß anzuzeigen

-    **Font Name**: Die Schriftart für den anzuzeigenden Text. Es kann ein Schriftartennamen sein, wie \"Arial\", ein Schriftstil wie \"sans\", \"serif\" oder \"mono\" oder eine Familie wie \"Arial,Helvetica,sans\" oder ein Name mit einem Schriftstil wie \"Arial:Bold\". Wenn die angegebene Schriftart nicht auf dem System gefunden wird, wird eine generische benutzt.

-    **Arrow Type**: Der Typ des zu benutzenden Pfeils

-    **Arrow Size**: Die Größe der Pfeile

-    **Decimals**: Die Anzahl der anzuzeigenden Dezimalstellen der Bemaßung

-    **Flip Arrows**: Vertauschen der Richtung der Pfeile

-    **Unit Override**: Drückt den Abstand in der angegebenen Einheit aus (falls leer, wird die Einheit des Systems (system unit) verwendet) <small>(v0.17)</small> 


</div>

See also: [Property editor](Property_editor.md).

A Draft Dimension object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data linear and radial dimension 


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension line passes.

-    **Linked Geometry|LinkSubList**: specifies the object and its subelement(s) the dimension is linked to.

-    **Normal|Vector**: specifies the normal of the plane of the text.

-    **Support|Link|hidden**: specifies the measured object.


{{TitleProperty|Linear/radial dimension}}

-    **Direction|Vector**: specifies the direction of the measurement.

-    **Distance|Length**: (read-only) specifies the value of the measurement.

-    **End|VectorDistance**: specifies the end point of the measurement.

-    **Start|VectorDistance**: specifies the start point of the measurement.


{{TitleProperty|Radial dimension}}

-    **Diameter|Bool**: specifies if a radial dimension is displayed as a diameter dimension. If it changed the symbol used in **Override** must be updated manually (from {{Value|Ø}} to {{Value|R}} or vice versa). Not used for linear dimensions.

### Data angular dimension 


{{TitleProperty|Angular dimension}}

-    **Angle|Angle**: (read-only) specifies the value of the measurement.

-    **Center|VectorDistance**: specifies the center of the measurement.

-    **First Angle|Angle**: specifies the start angle of the measurement.

-    **Last Angle|Angle**: specifies the end angle of the measurement.


{{TitleProperty|Dimension}}

-    **Dimline|VectorDistance**: specifies the point through which the dimension arc passes.

-    **Linked Geometry|LinkSubList|hidden**: not used.

-    **Normal|Vector|hidden**: specifies the normal of the plane of the dimension.

-    **Support|Link|hidden**: not used.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|2D text}} the text will be displayed in a plane defined by the **Normal** of the measurement. If it is {{value|3D text}} the text will always face the camera. Note that these values are switched compared to [Draft Texts](Draft_Text.md). This is an inherited property.


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbols displayed at the ends of the dimension line or arc.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the ends of the dimension line or arc, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifies the additional length added to the dimension line. Not used for angular dimensions.

-    **Ext Lines|Distance**: specifies the maximum length of the extension lines that go from the measured points to the dimension line. Not used for angular dimensions.

-    **Ext Overshoot|Distance**: specifies the additional length of the extension lines beyond the dimension line. Not used for angular dimensions.

-    **Flip Arrows|Bool**: specifies whether to flip the orientation of the symbols at the ends of the dimension line or arc. Only works if the symbols are arrows.

-    **Line Color|Color**: specifies the color of the dimension including the text.

-    **Line Width|Float**: specifies the width of the lines or arc belonging to the dimension.

-    **Show Line|Bool**: specifies whether to display the dimension line. Does not affect the display of extension lines and overshoots. Not used for angular dimensions.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement. Not used for angular dimensions.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.

## Scripting


<div class="mw-translate-fuzzy">

## Scripting 


**Siehe auch:**

[Draft API](Draft_API/de.md) und [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/de.md).


</div>

To create a Draft Dimension use the `make_dimension` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeDimension` method.


```python
dimension = make_dimension(p1, p2, p3=None, p4=None)```

There are various ways to invoke this method, depending on the arguments passed to it:


```python
dimension = make_dimension(p1, p2, p3=None)
dimension = make_dimension(object, i1, i2, p4=None)
dimension = make_dimension(object, i1, mode, p4=None)
```


<div class="mw-translate-fuzzy">

-   Erstellt ein Bemaßungs-Objekt mit der Bemaßungslinie durch p3.
-   Das Bemaßungs-Objekt übernimmt die in der Befehlszeile (command bar) gesetzte [Linienbreite und -farbe](Draft_Linestyle/de.md).
-   Es gibt viele Wege zur Erstellung einer Bemaßung, abhängig von den übergebenen Argumenten:

1.  (p1,p2,p3): erstellt eine Standardbemaßung von p1 bis p2.
2.  (Objekt,i1,i2,p3): erstellt eine verbundene Bemaßung zum angegebenen Objekt, mit dem Abstand zwischen den Kanten i1 und i2.
3.  (Objekt,i1,Modus,p3): erstellt eine verbundene Bemaßung zum angegebenen Objekt, i1 ist der Index der zu messenden (gebogenen) Kante und Modus ist entweder \"radius\" oder \"diameter\". Liefert das neu erstellte Objekt zurück.


</div>

To create an angular dimension use the following method:


```python
dimension = make_angular_dimension(center, angles, p3, normal=None)
dimension = make_angular_dimension(center, [angle1, angle2], p3, normal=None)
```


<div class="mw-translate-fuzzy">

-   erstellt eine Winkelbemaßung vom angegebenen Mittelpunkt mit den angegebenen Winkeln durch den Punkt p3.
-   liefert das neu erstellte Objekt zurück.


</div>

The view properties of `dimension` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Beispiel:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(-2500, 0, 0)
dimension1 = Draft.make_dimension(p1, p2, p3)
dimension1.ViewObject.FontSize = 200

polygon = Draft.make_polygon(3, radius=1000)
doc.recompute()

p4 = App.Vector(-2000, 1500, 0)
dimension2 = Draft.make_dimension(polygon, 1, 2, p4)
dimension2.ViewObject.FontSize = 200

center = App.Vector(2000, 0, 0)
p5 = App.Vector(3000, 1000, 0)
angle1 = 45
angle2 = 10
dimension3 = Draft.make_angular_dimension(center, [angle1, angle2], p5)
dimension3.ViewObject.FontSize = 200

dimension4 = Draft.make_angular_dimension(center, [angle2, angle1], p5*1.2)
dimension4.ViewObject.FontSize = 200

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
