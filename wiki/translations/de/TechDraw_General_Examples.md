# TechDraw General Examples/de
## Einleitung

Der Arbeitsbereich <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [TechDraw](TechDraw_Workbench/de.md) enthält viele Werkzeuge, aber was sind die erforderlichen Elemente, um ein Blatt Papier in eine richtige Zeichnung zu verwandeln? Diese Seite beabsichtigt, einige Erkärungen und einige Beispiele zu geben, was mit TechDraw schon alles möglich ist.



## Zeichnungen

Eine Zeichnung enthält eine oder mehrere Ansichten, die ein Bauteil geometrisch darstellen\... Aber, das ist ja schon bekannt,oder?

Sehen wir uns die grundlegenden Elemente an.



### Manuell erstellte Zeichnungen 



#### Ein Blatt Papier 

Papierformate sind genormt und damit sie ohne Skalieren gedruckt werden können, sollte das Format unseres Zeichnungsblattes dem gewünschten Druckformat entsprechen.



#### Rahmen

Als noch von Hand gezeichnet wurde, mussten die Zeichnungsblätter mit Nadeln oder Klebefilm auf der Zeichenmaschine bzw. dem Zeichentisch befestigt werden. Die fertige Zeichnung wurde gelocht, damit sie nach Norm gefaltet in eine Mappe oder einem Ordner abgeheftet werden kann. Der dafür genutzte äußere Bereich wird mit einem rechteckigen Rahmen abgegrenzt. Ein weiterer rechteckiger Rahmen innerhalb des ersten legt die Zeichenfläche fest. Zwischen beiden Rahmen befinden sich meistens noch fortlaufende Indizes und Trennlinien, die verwendet werden, um die Position bestimmter Zeichnungselemente anzugeben.



#### Schriftfeld

Das Schriftfeld enthält schriftliche Informationen über das Bauteil und die Zeichnung wie z.B. Sachnummer, Benennung, Ersteller, Eigentümer usw.



#### Stückliste

Wahlweise können Zusammenbauzeichnungen auch Stücklisten enthalten. Die Stückliste kann auch als separates Zeichnungsblatt oder als Kalkulationstabelle erstellt werden.



#### Änderungstabelle

Änderungen am Bauteil oder an der Zeichnung werden in einer Änderungstabelle auf der Zeichnung protokolliert oder in einem separaten Dokument, das über die entsprechenden Indizes verknüpft ist.



#### Ansichten

Ansichten enthalten die grafische Beschreibung eines Bauteils aus einer bestimmten Richtung. Die Meisten Bauteile benötigen mindestens zwei Ansichten, um vollständig beschrieben zu sein.



#### Beschriftung

Zusätzliche Texte die nicht zu den oben aufgeführten Elementen gehören.



### Mit TechDraw erstellte Zeichnungen 

TechDraw verwendet ein Page-Objekt als Behälter für alle zur Zeichnung gehörenden Elemente; dieses kann nicht alleine existieren, sondern muss eine Vorlage (Template) enthalten. Daher gibt es keinen Befehl \"Neues Zeichnungsblatt\", und wann immer eine Vorlage eingefügt wird, wird automatisch auch ein Page-Objekt erstellt.



#### Vorlagen

Eine [Vorlage](TechDraw_Templates/de.md) (Template)-Objekt ist eine [SVG](SVG/de.md)-Abbildung, deren Code sämtliche Informationen enthält, um ein virtuelles Blatt Papier mit passenden Rahmen und Schriftfeld zu erstellen sowie wahlweise mit einer Stückliste.

SVG-Abbildungen sind nicht parametrisch. Das heißt, dass für jedes Format eine eigene Vorlage erstellt werden muss; solch ein Satz Vorlagen wird für jede Variation von Rahmen- und Schriftfeldobjekten benötigt. Das ist eine ziemlich große Menge Code, zu schreiben und zu verwalten, aber dafür können Vorlagen innerhalb von FreeCAD nicht aus Versehen ändert werden.

Es gibt mehrere Möglichkeiten, eine Vorlage zu erstellen:

1.  Zeichnen mit with [Inkscape](https://de.wikipedia.org/wiki/Inkscape), siehe Anleitung [TechDraw-Vorlagen](TechDraw_TemplateHowTo/de.md).
2.  Manuelles Tippen, siehe [Template explained](Sandbox_TechDraw_TemplateExplained.md) (engl.).
3.  Ein Makro verwenden, siehe [TechDraw Vorlagengenerator](TechDraw_TemplateGenerator/de.md) und [Makro TemplateHelper](Macro_TemplateHelper/de.md).

<img alt="" src=images/TechDraw_ExampleDrawing-01.png  style="width:400px;">



*Ergebnis von Template explained*

<img alt="" src=images/Macro_TemplateHelper_A3+BOM.png  style="width:400px;">



*Ergebnis des Makros TemplateHelper, ISO A3 + Stückliste*



#### Die Zeichnung bis hier 

Bis hierher kann man wohl sicher sagen, dass TechDraw in Verbindung mit eingebetteten SVG-Vorlagen ein richtiges Zeichnungsblatt mit einem Rahmen und einem Schriftfeld erstellen kann. Einige Einträge können angepasst werden, dank editierbarer Texte und einige Inhalte können automatisch eingefügt werden, wenn Makros verwendet werden. 

## Ansichten 


<div lang="en" dir="ltr" class="mw-content-ltr">

Views contain the geometrical 2D description of an object. The content of a TechDraw view can be derived from 3D geometry or obtained from another workbench like <img alt="" src=images/TechDraw_ArchView.svg  style="width:16px;"> [Arch Views](TechDraw_ArchView.md) and <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Draft views](TechDraw_DraftView.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Since FreeCAD is a 3D modelling application TechDraw\'s key function is deriving 2D views from 3D geometry. Let\'s have a look at an easy example, the part from the [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md) that is also used with the [Basic TechDraw Tutorial](Basic_TechDraw_Tutorial.md):


</div>

<img alt="" src=images/Tut17_final_refined.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Part from the Basic Part Design Tutorial*


</div>



### Aktive Ansicht 


<div lang="en" dir="ltr" class="mw-content-ltr">

An <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Active View](TechDraw_ActiveView.md) is more or less a screen shot of the [3D view](3D_View.md) in its own kind of TechDraw view.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-02.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The item displayed in an Active View with No background option enabled*


</div>



### Ansicht


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [View](TechDraw_View.md) is TechDraw\'s basic view object to derive proper drawings. In contrast to an Active View it is not restricted to visible objects on the screen, but also displays selected objects outside the screen. The preferred scale depends on the available space and the level of detail that has to be displayed.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-03.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The item displayed in an arbitrary View like the Active View above*


</div>



### Ansichtengruppe


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Projection Group](TechDraw_ProjectionGroup.md) is a set of views. Each view direction is perpendicular to its neighbor and all depend on the 3D window\'s direction by default. TechDraw provides six views matching with the [Navigation Cube](Navigation_Cube.md) sides, and four isometric views.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-04.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The item displayed in a Projection Group consisting of three views (in first angle projection mode)*


</div>



### Schnittansicht


<div lang="en" dir="ltr" class="mw-content-ltr">

TechDraw provides tools to create a <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Simple Section View](TechDraw_SectionView.md) or a <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Complex Section View](TechDraw_ComplexSection.md). Both depend on a base view and on tools to define a section line and to derive the view direction. Have a look at [TechDraw Section Examples](TechDraw_Section_Examples.md) for an overview.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-05.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The cut item displayed in a Section A-A based on the Front view*


</div>



### Hilfsansicht


<div lang="en" dir="ltr" class="mw-content-ltr">

If we need a view of a tilted plane to see its true lengths we would define the view direction in a base view and place the Auxiliary view accordingly, but TechDraw provides no tool for Auxiliary views yet.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Good news: It is quite easy to emulate using the <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Simple Section View](TechDraw_SectionView.md) tool:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Select a base view.
2.  Create a <img alt="" src=images/TechDraw_SectionView.svg  style="width:16px;"> [Simple Section View](TechDraw_SectionView.md) with default settings.
3.  Use <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Insert Angle Dimension](TechDraw_AngleDimension.md) to measure the angle of the plane.
4.  Edit the section view angle in the Set View Direction area of its task panel.
5.  Edit the section view coordinates in the Section Plane Location area of its task panel. Use **small steps** to move the section line outside the object or FreeCAD may crash.
6.  Hide unwanted annotation elements such as section line, section arrows, and section name.
7.  Add needed items like view arrow, and view name.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-06.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*A default section view based on the Left view displaying the section line angle*


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-07.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Section view with section line angle set to {{value|218,93°* (38,93° plus 180° to flip direction)}}


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-09.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Section view with relocated section line → Finished Auxiliary view *


</div>



### Detailansicht


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Detail View](TechDraw_DetailView.md) is a copy of an area of a base view usually to magnify hardly visible geometry.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-10.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Detail (view) Y based on Section A-A*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Imperfections


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Detail views according to ISO standard do not have a frame/border (the upper part of the enclosing circle). Editor\'s note: what is meant here?? Frames are not printed\...
-   The break line that cuts the detail off from the rest should be a thin freehand line or the cad equivalent, a thin zigzag line. FreeCAD/TechDraw do not provide freehand/zigzag lines (yet).
-   Hatched areas in the base view should be hatched in the detail view, too.


</div>



### Arch-Ansicht 


<div lang="en" dir="ltr" class="mw-content-ltr">

An <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Arch View](TechDraw_ArchView.md) displays a view of an <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [Arch SectionPlane](Arch_SectionPlane.md). Its content is rendered by the <img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Arch workbench](Arch_Workbench.md).


</div>



### Draft-Ansicht 


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Draft View](TechDraw_DraftView.md) displays a view of a selected [Part](Part_Workbench.md)-based object or Group object. It is intended for 2D objects. Its content is rendered by the <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Draft workbench](Draft_Workbench.md).


</div>

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Some Draft elements in the 3D view → The same elements displayed in a Draft View on a drawing*


</div>



### Tabellenansicht


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Spreadsheet View](TechDraw_SpreadsheetView.md) displays a view of a [Spreadsheet Workbench](Spreadsheet_Workbench.md) sheet.


</div>

<img alt="" src=images/TechDraw_Spreadsheetview.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Spreadsheet element displayed in a Spreadsheet View*


</div>



### Die Ansichten bis hier 


<div lang="en" dir="ltr" class="mw-content-ltr">

TechDraw needs some additions like break lines, and a proper auxiliary view tool and also some improvement of the Detail View tool. But even in this state we can describe our objects visually quite well:


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-11.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*This is how a drawing with a set of views of the example item could look*


</div>


{{Top}}



## Bemaßung


<div lang="en" dir="ltr" class="mw-content-ltr">

Now that our item is described geometrically, dimensions will be added to further define the shape, and tolerances to define the allowed deviation. TechDraw supplies several tools to apply dimensions to the 2D representation of our item:

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md)
-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontal Dimension](TechDraw_HorizontalDimension.md)
-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertical Dimension](TechDraw_VerticalDimension.md)
-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:16px;"> [Radius Dimension](TechDraw_RadiusDimension.md)
-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Diameter Dimension](TechDraw_DiameterDimension.md)
-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Angle Dimension](TechDraw_AngleDimension.md)
-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [3-Point Angle Dimension](TechDraw_3PtAngleDimension.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

They have in common that they measure the projected shape of the item. If you have learned drafting the manual way, you know how to use auxiliary views to turn the item into a position where projected lengths equal true lengths. For visualization other than this old school way, dimensions can be linked to 3D geometry using <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [TechDraw DimensionRepair](TechDraw_DimensionRepair.md) to display \"true dimensions\".


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Two other tools measure the overall length horizontally or vertically respectively:

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:16px;"> [Insert Horizontal Extent Dimension](TechDraw_HorizontalExtentDimension.md)
-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:16px;"> [Insert Vertical Extent Dimension](TechDraw_VerticalExtentDimension.md)

These cannot be linked with 3D geometry (yet).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

See [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md) (and the following properties section) for all settings that are not mentioned in this overview.


</div>



### Einfache Maße 


<div lang="en" dir="ltr" class="mw-content-ltr">

The dimension text depends mainly on these properties:

-    **Format Spec**
    

-    **Format Spec Over Tolerance**
    

-    **Format Spec Under Tolerance**
    

:   By default their defaults are {{Value|%.2f}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To \"cheat\" we can use these two properties:

-    **Arbitrary**
    

:   

    :   Set to `False` to use the content of the **Format Spec** to format the actual dimensional value.
    :   Set to `True` to use the content of the **Format Spec** to be displayed as text instead if the dimension value.

-    **Arbitrary Tolerances**: Like **Arbitrary**, but for the tolerance.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If we only need the dimension value there\'s nothing to do but to change the number of decimals if desired.

:   For example: {{Value|%.2f}} → {{Value|%.3f}} to display 3 decimals, or {{Value|%.2f}} → {{Value|%.0f}} to display whole numbers.


</div>



#### Längenmaße


<div lang="en" dir="ltr" class="mw-content-ltr">

There are three tools to add length dimensions: <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontal Dimension](TechDraw_HorizontalDimension.md), and <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertical Dimension](TechDraw_VerticalDimension.md).


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-17.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-18.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Left: Two views of an object with length dimensions applied → Right: The same Front view rotated by 20°*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

This shows that it is important to rotate a front view in the Projection Group dialog or otherwise the connected views will not follow. On the other hand that would restrict us to 90° turns.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If a dimension has to run parallel to an edge it needs another selectable line perpendicular to the edge and the <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md) tool, that can find the shortest (= perpendicular) distance between a point and a line. An edge will not be automatically extended by an imaginary line and so we need to create an auxiliary (cosmetic) line manually. (A cosmetic point could be used as well, but that requires even more work).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   The black (point to line) <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md) depends on a cosmetic line that doesn\'t rotate with the view. (A cosmetic point wouldn\'t be helpful either.)
-   The <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontal Dimension](TechDraw_HorizontalDimension.md) and <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertical Dimension](TechDraw_VerticalDimension.md) (red and green) stay with the page orientation and change their values accordingly.
-   The blue is a point to line <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md), too but rotates with the view as there is no cosmetic geometry involved.


</div>



#### Winkelmaße


<div lang="en" dir="ltr" class="mw-content-ltr">

TechDraw provides two tools to add angle dimensions: <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Angle Dimension](TechDraw_AngleDimension.md) and <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [3-Point Angle Dimension](TechDraw_3PtAngleDimension.md).


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-19.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Two Ways to to add an angle dimension*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Blue: an <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Angle Dimension](TechDraw_AngleDimension.md) between two edges.
-   Red: a <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [3-Point Angle Dimension](TechDraw_3PtAngleDimension.md) using both end points and the center point of an arc.


</div>



#### Fasenmaß


<div lang="en" dir="ltr" class="mw-content-ltr">

A chamfer dimension can be applied as a [length dimension](#Length_dimension.md) with a manually edited **Format Spec** property or by using <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:16px;"> [Create Horizontal Chamfer Dimension](TechDraw_ExtensionCreateHorizChamferDimension.md) and <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:16px;"> [Create Vertical Chamfer Dimension](TechDraw_ExtensionCreateVertChamferDimension.md) to create a size and angle dimension for a chamfer.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-16.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Left: Chamfer dimensions applied to an object with horizontal and vertical sides → Center: The same view rotated by 10° → Right: Object tilted by 10°, view is at 0°*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The chamfer tools work well for objects with horizontal and vertical sides as long as they are parallel to the view\'s = the page\'s X and Y axes, but many parts won\'t do us the favor of being perfectly aligned.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The angle values are not parametric! They do not change if the view is tilted. The last page shows the correct angles, but dimensions positioned like this are pointless.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To align the chamfer dimension along an edge we need an auxiliary (cosmetic) point where the unchamfered edges would meet and have to use <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md); but cosmetic point won\'t follow the edges if the view is tilted. (also see [Length dimension](#Length_dimension.md).)


</div>



#### Radienmaß


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:16px;"> [Radius Dimension](TechDraw_RadiusDimension.md) adds a radius dimension to a circle or circular arc, no more no less.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-20.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Two ways to add a radius dimension, the red one with flipped arrowheads*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To change the arrowhead direction just set the **Flip Arrowheads** property to {{true}}.


</div>



#### Durchmessermaß


<div lang="en" dir="ltr" class="mw-content-ltr">

Diameter dimensions can be added as a <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Diameter Dimension](TechDraw_DiameterDimension.md) or one of the length dimensions <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Length Dimension](TechDraw_LengthDimension.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Horizontal Dimension](TechDraw_HorizontalDimension.md), and <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Vertical Dimension](TechDraw_VerticalDimension.md). (Or in connection with a leader line pointing to a circle center or a center line - not displayed.)


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-12.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Several ways to place a diameter dimension (please ignore the missing center line)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   Blue: a <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> length dimension in the side view of the hole needs a \"⌀\" prefixed to distinguish this from a rectangular hole.

:   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:16px;"> [Insert \'⌀\' Prefix](TechDraw_ExtensionInsertDiameter.md) is an easy way to do this, but the **Format Spec** property can be edited manually as well.

-   Green: a simple <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> length dimension.

:   It needs some auxiliary geometry (cosmetic points) as it cannot be applied to circles directly.

-   Red: a <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> diameter dimension. In case you look along the hole axis and can see the circular shape of the hole the \"⌀\" may be omitted. To remove it edit the **Format Spec** property manually.


</div>



#### Gewindemaß


<div lang="en" dir="ltr" class="mw-content-ltr">

Thread dimensions can be applied just like diameter dimensions, but they require some auxiliary geometry created beforehand: <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:16px;"> [Add Cosmetic Thread Hole Side View](TechDraw_ExtensionThreadHoleSide.md), <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:16px;"> [Add Cosmetic Thread Hole Bottom View](TechDraw_ExtensionThreadHoleBottom.md), <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:16px;"> [Add Cosmetic Thread Bolt Side View](TechDraw_ExtensionThreadBoltSide.md), or <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:16px;"> [Add Cosmetic Thread Bolt Bottom View](TechDraw_ExtensionThreadBoltBottom.md).


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-13.png  style="width:350px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*A countersunk thread with several ways to place a thread dimension (and a counter sink diameter)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

All Thread dimensions are applied to auxiliary (cosmetic) lines or circles (in connection with cosmetic points) and all **Format Spec** properties need to be edited manually to prefix the \"M\" for metric threads.


</div>



#### Toleranzen


<div lang="en" dir="ltr" class="mw-content-ltr">

Tolerances express how much a measured dimension may deviate from the dimension value on the drawing. To suffix a tolerance values to the dimension value simply set the **Over Tolerance** property to a value other than {{Value|0}}, this results in a symmetric tolerance such as {{Value|±0,5}}.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

For an asymmetric tolerance set **Equal Tolerance** property to {{false}} and specify also a lower value for the **Under Tolerance** property.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The values can be set in the [Dimension dialog](TechDraw_LengthDimension#Dimension_dialog.md) or directly in the [Property editor](Property_editor.md).


</div>



#### Wellen- und Bohrungspassungen 


<div lang="en" dir="ltr" class="mw-content-ltr">

Fit tolerances can be added by suffixing tolerance classes to a dimension. A tolerance class consist of a tolerance field specifier (letter, upper case for holes, lower case for shafts) and a tolerance grade specifier (number) and can be suffixed in three ways:

1.  Set the **Arbitrary Tolerances** property to {{true}} and specify both tolerance classes in the **Over Tolerance** and **Under Tolerance** properties.
2.  Use the <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:16px;"> [Add hole or shaft fit](TechDraw_HoleShaftFit.md) tool. This suffixes only one tolerance class but adds the related values to the **Over Tolerance** and **Under Tolerance** properties.
3.  For a single tolerance simply suffix the tolerance class to the format specifier in the **Format Spec** property.


</div>



#### Gewindepassung


<div lang="en" dir="ltr" class="mw-content-ltr">

Thread fit tolerances can be suffixed like described above for hole/shaft fit tolerances, except method 2. The thread tolerance classes display the tolerance grade specifier (number) in front of the tolerance field specifier (letter, upper case for internal threads, lower case for external threads).


</div>



### Prüfmaße


<div lang="en" dir="ltr" class="mw-content-ltr">

Inspection dimensions (test dimensions) are not yet implemented.

:   (Maybe obsolete already. See [\...test dimension was withdrawn\...](https://forum.freecad.org/viewtopic.php?p=691914#p691914) on the forum)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To fake an inspection dimension we set the **Format Spec** property to \" \" (one space - no character at all and we would have no handle to grab the dimension line to move it) and then set the **Arbitrary** property to `True`; this results in a dimension without value. The value can now be substituted with a balloon without leader line. This only works with horizontal dimensions since we cannot rotate balloons.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-21.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*The example item with an inspection dimension. In this case 100% of the production items have to be checked if they are within the tolerance*


</div>



### Form- und Lagetolerierung 


<div lang="en" dir="ltr" class="mw-content-ltr">

The system of [geometric dimensioning and tolerancing](TechDraw_Geometric_dimensioning_and_tolerancing.md) (GD&T) aims at describing shapes more precisely than toleranced dimensions alone can do. It is built on datums, theoretically exact dimensions, and tolerance indicators.


</div>



#### Bezüge


<div lang="en" dir="ltr" class="mw-content-ltr">

Datums are virtual surfaces, planes, lines, and points used as references to describe geometrical features with theoretically exact dimensions and tolerance indicators. They can be used to built a theoretically exact virtual coordinate system.


</div>



#### Bezugselemente


<div lang="en" dir="ltr" class="mw-content-ltr">

A datum feature is a geometric feature of an object corresponding with a certain datum. Datum feature symbols are added using <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Balloon](TechDraw_Balloon.md) annotations.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-22.png  style="width:350px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Example item with datum features. Both views display exactly the same datum features*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

The **Kink Length** property has to be set to {{Value|0}} for vertical leader lines. On {{VersionMinus|0.21}} this results in a portion of the line shown within the frame.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-27.png  style="width:200px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Now the leader line starts on the frame which is perfect for horizontal ones, but now it is impossible to draw vertical leader lines correctly*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Datum target 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Datum targets are points or relatively small areas that denote where to derive a datum from. Most common use is to create a theoretically exact virtual coordinate system from a set of six datum targets.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-23.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*This kind of datum target is not implemented yet*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

There is no known workaround at the moment.

:   Special point symbols to indicate the reference point of the datum target are not yet included in the options of leader lines.
:   The circles have to be derived from 3D geometry and are hard to handle in projection groups.


</div>



#### Theoretisch exakte Maße 


<div lang="en" dir="ltr" class="mw-content-ltr">

Theoretically exact dimensions are added the same way as [simple dimensions](#Simple_dimensions.md) and the Theoretically exact checkbox makes the difference: It sets the **Theoretically Exact ** property to {{true}} which adds a rectangular frame to the dimension value and deactivates tolerances and all tolerance settings.


</div>



#### Toleranzrahmen


<div lang="en" dir="ltr" class="mw-content-ltr">

A tolerance indicator, also called \"feature control frame\", is a frame containing tolerance information about:

-   which geometric characteristic is tolerated
-   the shape and size of the tolerance field
-   the datums to be referenced
-   some more symbols to describe the features even more precisely.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-24.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*Theoretically exact dimensions (red) and tolerance indicators with reference to datum feature A (blue)*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Tolerance indicators are like datum feature symbols added using <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Balloon](TechDraw_Balloon.md) annotations but using the {{value|Rectangle}}option. Use <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:16px;"> [Customize format label](TechDraw_ExtensionCustomizeFormat.md) to insert special characters.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

In most cases tolerance indicators are aligned with a dimension line which is impossible in TechDraw except for horizontal dimensions since, as already mentioned, balloon annotations can not be rotated.


</div>


{{Top}}



## Beschriftung 



### Hinweislinien


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:16px;"> [Leader line](TechDraw_LeaderLine.md) points to a vertex, edge, or face where the attached information is valid.

:   Tools that provide information and attach to a preselected leader line are <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [RichTextAnnotation](TechDraw_RichTextAnnotation.md), and <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [WeldSymbol](TechDraw_WeldSymbol.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Balloons


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

A <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Balloon](TechDraw_Balloon.md) is a combination of a leader line and a short text. It requires a preselected view, or an item belonging to a view or the command will return an error message. The leader line starts horizontally without exception and turns towards the selected item after a short distance defined in the **Kink Length** property. Its value can also be set to {{Value|0}}.


</div>

### Text


<div lang="en" dir="ltr" class="mw-content-ltr">

Techdraw supplies two tools to add text to a drawing:

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:16px;"> [Insert Annotation](TechDraw_Annotation.md) adds a plain text block as annotation to a page. Annotations use the same default settings as dimensions, some parameters can be changed, and they can be edited and rotated, but they cannot be attached.
-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [Insert Rich Text Annotation](TechDraw_RichTextAnnotation.md) adds a rich text block as annotation to a page, a leader line, or a view. Annotations attached to a leader line or a view move synchronously with the view or leader line when their positions change.


</div>



### Schweißsymbole


<div lang="en" dir="ltr" class="mw-content-ltr">

The <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [WeldSymbol](TechDraw_WeldSymbol.md) tool attaches to a preselected leader line and adds information about how to create a certain seam between two objects to avoid modelling the seam faces on the raw parts. The fork text determines which welding or soldering process has to be used for the seam.

:   It seems like the weld symbols demand an integrated leader line to get a fork symbol that matches the size of the text, otherwise the symbols on the leader line have to be scalable.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-26.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*A weld symbol for a circumferential V-seam, 111 meaning manual arc welding - Don't beat me if I have cited the internet wrongly*


</div>



### Oberflächensymbole


<div lang="en" dir="ltr" class="mw-content-ltr">

<img alt="" src=images/TechDraw_SurfaceFinishSymbol.svg  style="width:16px;"> [Add Surface Finish Symbol](TechDraw_SurfaceFinishSymbol.md) adds a surface finish symbol to the page, which means these symbols do not move with their referenced geometry.


</div>

<img alt="" src=images/TechDraw_ExampleDrawing-25.png  style="width:300px;">


<div lang="en" dir="ltr" class="mw-content-ltr">



*A surface finish symbol in comparison with a dimension*


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

These symbols cannot be customized regarding line width and font type to match with the dimensions and they can hardly be edited after creation.


</div>


{{Top}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw General Examples/de
