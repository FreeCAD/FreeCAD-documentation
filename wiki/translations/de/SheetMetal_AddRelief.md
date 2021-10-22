---
- GuiCommand:/de
   Name:SheetMetal AddRelief
   Name/de:SheetMetal EntlastungsausschnittHinzufügen
   MenuLocation:SheetMetal → Make Relief
   Workbenches:[Blech (SheetMetal)](SheetMetal_Workbench/de.md)
   Shortcut:**S** **R**
---

# SheetMetal AddRelief/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Der Befehl <img alt="" src=images/SheetMetal_Relief.svg  style="width:24px;"> **Entlastungsausschnitt hinzufügen**\...


</div>

This command is the first of three steps to convert a shell object made with the [Part Workbench](Part_Workbench.md) or [PartDesign Workbench](PartDesign_Workbench.md) into an unfoldable sheet metal object:

1.  [SheetMetal AddRelief](SheetMetal_AddRelief.md)
2.  [SheetMetal AddJunction](SheetMetal_AddJunction.md)
3.  [SheetMetal AddBend](SheetMetal_AddBend.md)

<img alt="" src=images/SheetMetal_ConvertShellObject-01.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-02.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-03.png  style="width:100px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-04.png  style="width:100px;">


<div class="mw-translate-fuzzy">



*Entlastungsausschnitt für eine Blechabkantung erzeugen*


</div>

## Anwendung

1.  Select one or more corner vertex(es).
2.  Activate the <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **SheetMetal AddRelief** command using one of the following:
    -   The **<img src="images/SheetMetal_AddRelief.svg" width=16px> [SheetMetal AddRelief](SheetMetal_AddRelief.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddRelief.svg" width=16px> Make Relief** menu option.
    -   The keyboard shortcut: **S** then **R**

<img alt="" src=images/SheetMetal_ConvertShellObject-05.png  style="width:200px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/SheetMetal_ConvertShellObject-06.png  style="width:200px;">

## Notes

The commands <img alt="" src=images/SheetMetal_AddRelief.svg  style="width:16px;"> **_**, and <img alt="" src=images/SheetMetal_AddBend.svg  style="width:16px;"> **[SheetMetal AddBend](SheetMetal_AddBend.md)** work best with hollow cuboids i.e. shell objects with a constant thickness and only 90° angles between faces.

Shell objects can be created with commands from the <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> _.

To create a hollow cuboid with the [Part Workbench](Part_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/Part_Box.svg  style="width:16px;"> [Part Box](Part_Box.md).
    -   <img alt="" src=images/Part_Extrude.svg  style="width:16px;"> [Part Extrude](Part_Extrude.md) from:
        -   A <img alt="" src=images/Draft_Rectangle.svg  style="width:16px;"> [Draft Rectangle](Draft_Rectangle.md).
        -   A <img alt="" src=images/Draft_Wire.svg  style="width:16px;"> [Draft Wire](Draft_Wire.md).
        -   A <img alt="" src=images/Sketcher_NewSketch.svg  style="width:16px;"> [Sketch](Sketcher_NewSketch.md).
2.  Use <img alt="" src=images/Part_Thickness.svg  style="width:16px;"> [Part Thickness](Part_Thickness.md) to create a shell object from the solid (Typically with the thickness value of the sheet metal).

To create a hollow cuboid with the [PartDesign Workbench](PartDesign_Workbench.md):

1.  Create a solid using either:
    -   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:16px;"> [Additive Box](PartDesign_AdditiveBox.md).
    -   <img alt="" src=images/PartDesign_Pad.svg  style="width:16px;"> _.
2.  Use <img alt="" src=images/PartDesign_Thickness.svg  style="width:16px;"> [PartDesign Thickness](PartDesign_Thickness.md) to create a shell object from the solid (Typically with the thickness value of the sheet metal).

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
