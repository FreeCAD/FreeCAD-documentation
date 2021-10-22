---
- GuiCommand:/de
   Name:SheetMetal Extrude
   Name/de:SheetMetal KanteVerlängern
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**E**
---

# SheetMetal Extrude/de

## Beschreibung


<div class="mw-translate-fuzzy">

Der Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Kante verlängern** erweitert eine Blechfläche.


</div>

It creates a **simple extension** along the face normal of the selected edge face:

<img alt="" src=images/SheetMetal_Extrude-01.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-02.png  style="width:200px;">

If an outline sketch is added it creates **interlocking geometry** to close a profile:

<img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles with outline sketches to add -> three results*

## Anwendung

### Simple Extension 

1.  Select one or more edge face(s) to be extended.
2.  Activate the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Extrude** command using one of the following:
    -   The **<img src="images/SheetMetal_Extrude.svg" width=16px> [Extend Face](SheetMetal_Extrude.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_Extrude.svg" width=16px> Extend Face** menu option.
    -   The keyboard shortcut: **E**.
3.  Change the value of the property **length** to adjust the length of the extension.

### Interlocking Extension 

1.  Select one edge face to be extended.
2.  Activate the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:16px;"> **SheetMetal Extrude** command (see above).
3.  Add a coplanar outline sketch to the property **Sketch**.
4.  Set the property **Use Subtraction** to `True` to create cut-outs to make room for the extensions.
5.  Set the property **Offset** to adjust the clearance around the extension.

<img alt="" src=images/SheetMetal_Extrude-03.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-06.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-04.png  style="width:200px;">



*Three profiles -> position of the sketches -> results without cut-outs -> final results*

### Notes

-   A sketch can contain more than one outline.

:   After inserting a sketch, at least one of its outlines must at least touch one opposite face or the tool will fail to create any extension or cut-out.





:   Just one outline touching an opposite face is enough to create extension geometry from all outlines of the sketch.

-   Each cut-out will have a cuboid shape, no matter what shape the corresponding outline sketch is.

-   Shapes other than rectangles may behave little bit strange and even though the object can be unfolded, the result will not turn out as expected.

<img alt="" src=images/SheetMetal_Extrude-07.png  style="width:250px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_Extrude-08.png  style="width:250px;">



*Three outline sketches and their resulting extensions: separate triangle plate with a rectangular cut-out, circle without clearance -> unfold solid is split at an unexpected position *

-   In an extension operation it is recommended to leave the property **Refine** set to `True` (default).

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Extend-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base object\". Verweis zu der ebenen Fläche, die erweitert werden soll.

-    {{PropertyData/de|gap1|Distance}}: \"Gap from the left side\". Abstand von der linken Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|gap2|Distance}}: \"Gap from the right side\". Abstand von der rechten Seite, Standardwert: {{value|0,00 mm}}.

-    {{PropertyData/de|length|Length}}: \"Length of Wall\". Kantenlänge, Standardwert: {{value|10,00 mm}}.


{{Properties_Title/de|Parameters Ext.}}


<div class="mw-translate-fuzzy">

-    {{PropertyData/de|Offset|Distance}}: \"Offset for subtraction\". Abstand zur Aussparung, Standardwert: {{value|20,00 µm}}.

-    {{PropertyData/de|Refine|Bool}}: \"Use Refine\". Standardwert: `True`.

-    {{PropertyData/de|Sketch|Link}}: \"Wall Sketch\". Skizze für den zu erweiternden Bereich

-    {{PropertyData/de|Use Substraction|Bool}}: \"Use Substraction\". Aussparung anwenden, Standardwert: `False`


</div>




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Extrude/de
