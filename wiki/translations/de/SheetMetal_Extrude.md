---
- GuiCommand:/de
   Name:SheetMetal Extrude
   Name/de:SheetMetal KanteVerlängern
   MenuLocation:SheetMetal → Extend Face
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**E**
---

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Kante verlängern** erweitert eine Blechfläche.

## Anwendung

To Extend the face:

1.  Start with a base plate or sheet, select a thin face representing the thickness of the metal sheet
2.  Click on the <img alt="" src=images/SheetMetal_Extrude.svg  style="width:24px;"> **Extrude** tool to extend the face.


**Note**

: To create a base plate use a closed 2D outline - preferably a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md) - with the <img alt="" src=images/SheetMetal_AddBase.svg  style="width:24px;"> [Make Base Wall](SheetMetal_AddBase.md) command.
Alternatively you can generate a base plate with one of the following methods as well:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box.md)

:\* Method 2: An extruded solid made with <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrude](Part_Extrude.md) from either a:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) or a

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) or a

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) containing either an

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [additive box](PartDesign_AdditiveBox.md) or a

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md) made from a <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md).

:   

    :   If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Body, you can mix Sheet Metal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [pockets](PartDesign_Pocket.md) or <img alt="" src=images/PartDesign_Hole.svg  style="width:24px;"> [holes](PartDesign_Hole.md).


**Note**

: In an extension operation, set `Refine {{:=` true}}.

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

-    {{PropertyData/de|Offset|Distance}}: \"Offset for subtraction\". Abstand zur Aussparung, Standardwert: {{value|20,00 µm}}.

-    {{PropertyData/de|Refine|Bool}}: \"Use Refine\". Standardwert: `True`.

-    {{PropertyData/de|Sketch|Link}}: \"Wall Sketch\". Skizze für den zu erweiternden Bereich

-    {{PropertyData/de|Use Substraction|Bool}}: \"Use Substraction\". Aussparung anwenden, Standardwert: `False`




[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
