---
- GuiCommand:/sv   Name:Draft ShapeString   Name/sv:Draft ShapeString   Workbenches:[Arch](Draft_Workbench/sv___Draft]],_[[Arch_Workbench/sv.md)|MenuLocation:Draft -> ShapeString   Shortcut:S S   SeeAlso:[Draft Text](Draft_Text/sv.md), [Part Extrude](Part_Extrude/sv.md)---


</div>

#### Beskrivning

The <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft ShapeString** command creates a compound shape that represents a text string. This shape can be used to create 3D letters with the [Part Extrude](Part_Extrude.md) command.

The Draft ShapeString command is not intended for standard text annotations. The [Draft Text](Draft_Text.md) command or the [Draft Label](Draft_Label.md) command should be used for that purpose.

![](images/Draft_ShapeString_Example400.png )


<div class="mw-translate-fuzzy">

![](images/Draft_ShapeString_Example400.png )


</div>


<div class="mw-translate-fuzzy">

## Bruk


</div>

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** button.
    -   Select the **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text** option from the menu.
    -   Use the keyboard shortcut: **S** then **S**.
2.  The **ShapeString** task panel opens.
3.  Click a point in the [3D view](3D_view.md), or type coordinates.
4.  Optionally press the **Reset Point** button to reset the point to the origin.
5.  Enter a **String**.
6.  Specify the **Height**.
7.  To select a font do one of the following:
    -   Enter a file path in the **Font file** input box.
    -   Press the **...** button and select a file.
8.  Press the **OK** button to finish the command.

## Options

-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   Supported fonts include TrueType ({{FileName|.ttf}}), OpenType ({{FileName|.otf}}) and Type 1 ({{FileName|.pfb}}).
-   The command is restricted to LTR (left-to-right) text. Therefore at the moment RTL (right-to-left + top-to-bottom) text isn\'t supported.
-   Very small text heights may result in deformed character shapes due to loss of detail in scaling.
-   Many fonts will generate problematic geometry. This is because font contours are allowed to overlap, have small gaps, and have varying directions within a glyph. These conditions are considered errors in wires used to define faces.
-   Draft ShapeStrings can also be created with the [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP.md).
-   To create Draft ShapeStrings arranged in a circular fashion use the [Macro FCCircularText](Macro_FCCircularText.md).

## Tutorials

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**. See [Draft Preferences](Draft_Preferences.md).

## Properties

See also: [Property editor](Property_editor.md).

A Draft ShapeString object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}

-    **Font File|File**: specifies the path of the font file used to draw the text.

-    **Size|Length**: specifies the general height of the text.

-    **String|String**: specifies the text string to display. Unlike a [Draft Text](Draft_Text.md), a Draft ShapeString can only display a single text line.

-    **Tracking|Length**: specifies the additional inter-character spacing of the text.

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: specifies the [Draft Pattern](Draft_Pattern.md) with which to fill the faces of the text. This property only works if **Display Mode** is {{value|Flat Lines}}.

-    **Pattern Size|Float**: specifies the size of the [Draft Pattern](Draft_Pattern.md).

## Scripting


<div class="mw-translate-fuzzy">

## Skript


</div>

To create a Draft ShapeString use the `make_shapestring` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeShapeString` method.


```python
shapestring = make_shapestring(String, FontFile, Size=100, Tracking=0)
```

-   Creates a `shapestring` compound shape using the specified `String` and the full path of a supported `FontFile`.

-    `Size`is the height of the resulting text in millimeters.

-    `Tracking`is the additional inter-character spacing in millimeters.

The placement of the ShapeString can be changed by overwriting its `Placement` attribute, or by individually overwriting its `Placement.Base` and `Placement.Rotation` attributes.

Example:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

font1 = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font2 = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
font3 = "/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf"

S1 = Draft.make_shapestring("This is a sample text", font1, 200)

S2 = Draft.make_shapestring("Inclined text", font2, 200, 10)

zaxis = App.Vector(0, 0, 1)
p2 = App.Vector(-1000, 500, 0)
place2 = App.Placement(p2, App.Rotation(zaxis, 45))
S2.Placement = place2

S3 = Draft.make_shapestring("Upside-down text", font3, 200, 10)
S3.Placement.Base = App.Vector(0, -1000, 0)
S3.Placement.Rotation = App.Rotation(zaxis, 180)

doc.recompute()
```





 
