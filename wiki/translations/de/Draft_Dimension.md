---
- GuiCommand:
   Name:Draft Dimension
   Name/de:Draft Maß
   MenuLocation:Anmerkung → Abmessung
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   Shortcut:**D** **I**
   Version:0.8
   SeeAlso:[Draft MaßKippen](Draft_FlipDimension/de.md)
---

# Draft Dimension/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_Dimension.svg  style="width:24px;"> **Draft Maß** [erstellt](#Erstellen.md) ein [lineares Maß](#Anwendung_lineares_Maß.md), ein [radiales Maß](#Anwendung_radiales_Maß.md) oder ein [Winkelmaß](#Anwendung_Winkelmaß.md). Der Befehl kann auch verwendet werden, um mit [Std AbstandMessen](Std_MeasureDistance/de.md) erstellte Objekte [umzuwandeln](#Umwandeln.md).

Lineare Maße auf Basis von Kanten und radiale Maße sind parametrisch. Das heißt, dass sie aktualisiert werden, wenn die bemaßte Kante verändert wird. Die bemaßten Kanten können zu Draft-Objekten gehören oder zu Volumenkörpern. Winkelmaße sind nicht parametrisch.

Draft-Maße können auf einem [TechDraw](TechDraw_Workbench/de.md)-Zeichnungsblatt in einer [TechDraw DraftAnsicht](TechDraw_DraftView/de.md) oder [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) angezeigt werden. Alternativ bietet der Arbeitsbereich [TechDraw](TechDraw_Workbench.md) eigene Bemaßungsbefehle, aber die erstellen Maße, die nur auf dem Zeichnungsblatt dargestellt werden und nicht in der [3D-Ansicht](3D_view/de.md).

<img alt="" src=images/Screenshot_Draft_Dimension.jpg  style="width:400px;"> 
*Durch drei Punkte definiertes lineares Maß (Längenmaß)*



## Erstellen

Siehe auch: [Draft Fach](Draft_Tray/de.md), [Draft Fangen](Draft_Snap/de.md) und [Draft Beschränken](Draft_Constrain/de.md).



### Anwendung lineares Maß 

1.  Wahlweise eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Dimension.svg" width=16px> [Abmessung](Draft_Dimension/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Dimension.svg" width=16px> Abmessung** auswählen.
    -   Das Tastaturkürzel **D** dann **I**.
3.  Der Aufgabenbereich **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
4.  Wenn bisher noch keine Kante ausgewählt wurde, wählt man eine der folgenden Möglichkeiten:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen.

    -   Die **Alt**-Taste drücken und halten, eine gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen und die **Alt**-Taste loslassen.

    -   Den zu messenden Abstand festlegen durch Auswahl von Punkten:
        -   Den ersten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
        -   Den zweiten Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
5.  Zum Positionieren der Maßlinie hat man folgende Möglichkeiten:
    -   Für ein ausgerichtetes Maß:
        -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen oder Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
    -   Für ein horizontales Maß:
        -   Den Mauszeiger über oder unter die Kante oder die Punkte bewegen.
        -   Die **Shift**-Taste dücken und halten, den Mauszeiger bewegen und einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
    -   Für ein vertikales Maß:
        -   Den Mauszeiger links oder rechts neben die Kante oder die Punkte bewegen.
        -   Die **Shift**-Taste dücken und halten, den Mauszeiger bewegen und einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.



### Anwendung radiales Maß 

1.  Wahlweise eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension/de.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Dimension.svg" width=16px> Abmessung** auswählen.
    -   Das Tastaturkürzel **D** dann **I**.
3.  Der Aufgabenbereich **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
4.  Wenn bisher noch keine Kante ausgewählt wurde, wählt man eine der folgenden Möglichkeiten:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen.

    -   Die **Alt**-Taste drücken und halten, eine kreisförmige Kante in der [3D-Ansicht](3D_view/de.md) auswählen unddie **Alt**-Taste loslassen.
5.  Zum Positionieren der Maßlinie hat man folgende Möglichkeiten:
    -   Für ein Durchmessermaß:
        -   Einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen, oder die Koordinaten eingeben und die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben** drücken.
    -   Für ein radiales Maß:
        -   Die **Shift**-Tast drücken und halten und einen Punkt in der [3D-Ansicht](3D_view/de.md).



### Anwendung Winkelmaß 

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** drücken.
    -   Den Menüeintrag **Anmerkung → <img src="images/Draft_Dimension.svg" width=16px> Abmessung** auswählen.
    -   Das Tastaturkürzel **D** dann **I**.
2.  Der Aufgabenbereich **Dimension** wird geöffnet. Siehe [Optionen](#Optionen.md) für mehr Informationen.
3.  Eine der folgenden Möglichkeiten auswählen:
    -   
        **E**
        
        oder die Schaltfläche **<img src="images/view-select.svg" width=16px> Kante auswählen** drücken und eine erste gerade Kante in der [3D-Ansicht](3D_view/de.md) auswählen. Diesen Schritt zur Auswahl einer zweiten geraden Kante wiederholen.

    -   Die **Alt**-Taste drücken und halten, zwei gerade Kanten in der [3D-Ansicht](3D_view/de.md) auswählen und die **Alt**-Taste loslassen.
4.  Zum Positionieren der Maßlinie einen Punkt in der [3D-Ansicht](3D_view/de.md) auswählen.
5.  Der angezeigte Winkel hängt von den Kanten und dem ausgewählten Punkt ab.



### Optionen

Die im Aufgabenbereich vorhandenen Einzelzeichen-Tastaturkürzel können geändert werden. Siehe [Draft Einstellungen](Draft_Preferences/de.md). Die hier genannten Tastenkürzel sind die voreingestellten Tastenkürzel.

-   Um Koordinaten von Hand einzugeben, gibt man die werte der X-, Y- und Z-Komponenten jeweils gefolgt von einem **Enter** ein. Oder man drückt die Schaltfläche **<img src="images/Draft_AddPoint.svg" width=16px> Punkt eingeben**, wenn die gewünschten Werte erreicht sind. Es ist ratsam, den Mauszeiger aus der [3D-Ansicht](3D_view.md) herauszubewegen, bevor man Koordinaten eingibt.

-    **R**drücken oder die Checkbox **Relativ** aktivieren, um den relativen Modus ein- bzw. auszuschalten. Wenn der relative Modus aktiviert ist, beziehen sich Koordinaten auf den letzten Punkt, falls vorhanden, andernfalls beziehen sie sich auf den Ursprung des Koordinatensystems.

-    **G**drücken oder die Checkbox **Global** aktivieren, um den globalen Modus ein- bzw. auszuschalten. Wenn der globale Modus aktiviert ist, beziehen sich Koordinaten auf das globale Koordinatensystem, andernfalls beziehen sie sich auf das Koordinatensystem der [Arbeitsebene](Draft_SelectPlane/de.md). {{Version/de|0.20}}

-    **T**drücken oder die Checkbox **Continue** aktivieren, um den Fortsetzungsmodus ein- bzw. auszuschalten. Wenn der Fortsetzungsmodus aktiviert ist, wird der Befehl nach jeder Fertigstellung wieder neu starten und ermöglicht so, dass man kontinuierlich weitere Maße erstellen kann. Alle folgenden Maße starten am Endpunkt des vorhergehenden Maßes und verwenden dieselbe Grundlinie für das erste Maß. Man beachte, dass die Auswahl von Kanten bei aufeinader folgenden Maßen nicht möglicht ist.

-    **S**drücken, um [Draft Fangen](Draft_Snap/de.md) ein- bzw. auszuschalten.

-    **Esc**oder die Schaltfläche **Close** drücken, um den Befehl fertigzustellen.



## Umwandeln



### Anwendung

1.  Select one or more [Std MeasureDistance](Std_MeasureDistance.md) objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Dimension.svg" width=16px> [Draft Dimension](Draft_Dimension.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Dimension.svg" width=16px> Dimension** option from the menu.
    -   Use the keyboard shortcut: **D** then **I**.
3.  Each selected object is replaced by a non-parametric linear Draft Dimension.



## Hinweise


<div class="mw-translate-fuzzy">

-   Lineare und radiale Draft-Maße können mit dem Befehl [Draft Bearbeiten](Draft_Edit/de.md) editiert werden.


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

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Draft Dimension-Objekt ist von einem [App FeaturePython](App_FeaturePython/de.md)-Objekt abgeleitet und erbt alle seine Eigenschaften. Die folgenden sind, wenn nicht anders angegeben, zusätzliche Eigenschaften:

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



### Ansicht


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the dimension. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the dimension.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Normal** of the measurement. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbols displayed at the ends of the dimension line or arc.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the ends of the dimension line or arc, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Dim Overshoot|Distance**: specifies the additional length added to the dimension line. Not used for angular dimensions.

-    **Ext Lines|Distance**: specifies the length of the extension lines that go from the dimension line to the measured points. Use {{Value|0}} for full extension lines. A negative value defines the gap between the ends of the extension lines and the measured points. A positive value defines the maximum length of the extension lines. Only used for linear dimensions.

-    **Ext Overshoot|Distance**: specifies the additional length of the extension lines beyond the dimension line. Not used for angular dimensions.

-    **Flip Arrows|Bool**: specifies whether to flip the orientation of the symbols at the ends of the dimension line or arc. Only works if the symbols are arrows.

-    **Line Color|Color**: specifies the color of the dimension line or arc, and the arrows.

-    **Line Width|Float**: specifies the width of the lines or arc belonging to the dimension.

-    **Show Line|Bool**: specifies whether to display the dimension line. Does not affect the display of extension lines and overshoots. Not used for angular dimensions.


{{TitleProperty|Text}}

-    **Flip Text|Bool**: specifies whether to flip the orientation of the text.

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Override|String**: specifies a custom text to display instead of the actual measurement. Use the string {{value|$dim}} inside the text to include the measurement.

-    **Text Color|Color**: specifies the color of the text. <small>(v0.21)</small> 

-    **Text Position|VectorDistance**: specifies the position of the text in absolute coordinates. {{Value|[0, 0, 0]}} will display the text in its default position near the dimension line or arc.

-    **Text Spacing|Length**: specifies the space between the text and the dimension line or arc.


{{TitleProperty|Units}}

-    **Decimals|Integer**: specifies the number of decimal places to display for the measurement.

-    **Show Unit|Bool**: specifies whether to display the unit next to the numerical value of the measurement. Not used for angular dimensions.

-    **Unit Override|String**: specifies the unit in which to express the measurement, for example, {{value|km}}, {{value|m}}, {{value|cm}}, {{value|mm}}, {{value|mi}}, {{value|ft}}, {{value|in}} or {{value|arch}} for arch units. Leave this blank to use the default unit. Not used for angular dimensions.



## Skripten

Siehe auch: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Dimension/de
