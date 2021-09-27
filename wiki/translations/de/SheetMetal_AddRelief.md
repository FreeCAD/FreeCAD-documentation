---
- GuiCommand:/de
   Name:SheetMetal AddRelief
   Name/de:SheetMetal EntlastungsausschnittHinzufügen
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**S** **R**
---

# SheetMetal AddRelief/de

## Beschreibung

Der Befehl <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **Entlastungsausschnitt hinzufügen**\...

<img alt="" src=images/PostRelief.png  style="width:320px;"> 
*Entlastungsausschnitt für eine Blechabkantung erzeugen*

## Anwendung

To add relief to corner of bend:

1.  Start with a base plate or sheet, select a corner vertex to apply relief
2.  Click on the <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **Relief** tool to add relief cut to corner.


**Note**

: The workbench does not have a tool to create a base plate, so you need to start your model with one of the following methods:

:\* Method 1: <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box.md)

:\* Method 2: An extruded solid made with <img alt="" src=images/Part_Extrude.svg  style="width:24px;"> [Part Extrude](Part_Extrude.md) from either a:

::\* <img alt="" src=images/Draft_Rectangle.svg  style="width:24px;"> [Draft Rectangle](Draft_Rectangle.md) or a

::\* <img alt="" src=images/Draft_Wire.svg  style="width:24px;"> [Draft Wire](Draft_Wire.md) or a

::\* <img alt="" src=images/Sketcher_NewSketch.svg  style="width:24px;"> [Sketch](Sketcher_NewSketch.md)

::\* Use <img alt="" src=images/Part_Thickness.svg  style="width:24px;"> [Part Thickness](Part_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:\* Method 3: <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [PartDesign Body](PartDesign_Body.md) containing either an

::\* <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:24px;"> [additive box](PartDesign_AdditiveBox.md) or a

::\* <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> _.

::\* Use <img alt="" src=images/PartDesign_Thickness.svg  style="width:24px;"> [PartDesign Thickness](PartDesign_Thickness.md) to create shell (**Typically with the thickness value of the sheet metal.**)

:   

    :   If you start with a <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> PartDesign Body, you can mix Sheet Metal features with PartDesign features such as <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> _.

## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein SheetMetal-Relief-Objekt wird von einem [Part-Formelement](Part_Feature/de.md) abgeleitet und erbt alle seine Eigenschaften. Außerdem hat es die folgenden zusätzlichen Eigenschaften und sein Label hat eine Standardwert:

### Daten


{{Properties_Title/de|Basis}}

-    {{PropertyData/de|Label|String}}: Standardwert: Der vom Benutzer änderbare Name dieses Objekts, der aus einer beliebigen UTF8-Zeichenkette bestehen kann.

-    {{PropertyData/de|Base Feature|Link|hidden}}: Base Feature. Verweis zum Eltern-Objekt.

-    {{PropertyData/de|_Body|LinkHidden|hidden}}: Unsichtbarer Verweis zum Eltern-Body.


{{Properties_Title/de|Parameters}}

-    {{PropertyData/de|base Object|LinkSub}}: \"Base Object\". Verweise zu den Eckpunkten, die die Lage der Entlastungsausschnitte bestimmen.

-    {{PropertyData/de|relief|Length}}: \"Relief Size\". Größe der Entlastungsausschnitte, Standardwert: {{value|2,00 mm}}.




_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal AddRelief/de
