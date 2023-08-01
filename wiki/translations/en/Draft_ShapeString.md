---
- GuiCommand:
   Name: Draft ShapeString
   MenuLocation: Drafting - Shape from text
   Workbenches: [Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut: 
   Version: 0.14
   SeeAlso: [Draft Text](Draft_Text.md), [Draft Label](Draft_Label.md), [Part Extrude](Part_Extrude.md)
---

# Draft ShapeString/en

## Description

The <img alt="" src=images/Draft_ShapeString.svg  style="width:24px;"> **Draft ShapeString** command creates a compound shape that represents a text string. This shape can be used to create 3D letters with the [Part Extrude](Part_Extrude.md) command.

The Draft ShapeString command is not intended for standard text annotations. The [Draft Text](Draft_Text.md) command or the [Draft Label](Draft_Label.md) command should be used for that purpose.

![](images/Draft_ShapeString_Example400.png ) 
*Single point required to position the ShapeString*

## Usage

For Windows users: please read the [Font file selection on Windows](#Font_file_selection_on_Windows.md) paragraph first.

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ShapeString.svg" width=16px> [Draft ShapeString](Draft_ShapeString.md)** button.
    -   Select the **Drafting → <img src="images/Draft_ShapeString.svg" width=16px> Shape from text** option from the menu.
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

-   Press **Esc** or the **Cancel** button to abort the command.

## Notes

-   A Draft ShapeStrings can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Supported fonts include TrueType (**.ttf**), OpenType (**.otf**) and Type 1 (**.pfb**).
-   The command is restricted to LTR (left-to-right) text. Therefore at the moment RTL (right-to-left + top-to-bottom) text isn\'t supported.
-   Very small text heights may result in deformed character shapes due to loss of detail in scaling.
-   Many fonts will generate problematic geometry. This is because font contours are allowed to overlap, have small gaps, and have varying directions within a glyph. These conditions are considered errors in wires used to define faces.
-   Draft ShapeStrings can also be created with the [Macro Fonts Win10 PYMP](Macro_Fonts_Win10_PYMP.md).
-   To create Draft ShapeStrings arranged in a circular fashion use the [Macro FCCircularText](Macro_FCCircularText.md).

## Font file selection on Windows 

On Windows access to the default font folder is restricted. This affects the font file selection for ShapeStrings. There are three cases in FreeCAD where a font file for ShapeStrings can be specified: in the ShapeString task panel, when changing the **Font File** property of a ShapeString, and when specifying the default font file in the [Draft Preferences](Draft_Preferences#Texts_and_dimensions.md).

Pressing the **...** button and then selecting a file from the default Windows font folder is not possible when using the native file dialog. There are a number of workarounds:

-   Make sure **DontUseNativeFontDialog** is set to {{True}}, which is the default value for this preference. This will only call a different, non-native, file dialog when pressing the **...** button in the ShapeString task panel. With this file dialog the default Windows font folder can be accessed.
-   Change **DontUseNativeDialog** to {{True}}. This instructs FreeCAD to always use the non-native file dialog.
-   Specify the font file in the input box. You can of course type the full path or copy-paste the path from the Windows File Explorer. But there is also another way to enter the path. If you enter {{Value|C:\}} a dropdown list will appear. Select {{Value|Windows}} from that list and add {{Value|\F}}. Select {{Value|Fonts}} from the new dropdown list. Finally add {{Value|\}} and the first letter(s) of the font file, and then select it from the dropdown list.
-   Create a custom folder for your font files.

See the [Preferences](#Preferences.md) paragraph below for the location of the mentioned preferences.

## Tutorials

-   [Draft ShapeString tutorial](Draft_ShapeString_tutorial.md): extrude a ShapeString, position it in 3D space, and create an engraving in another body.
-   [How to use ShapeStrings in PartDesign](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623)

## Preferences

See also: [Preferences Editor](Preferences_Editor.md), [Draft Preferences](Draft_Preferences.md) and [Std DlgParameter](Std_DlgParameter.md).

-   The default font file can be changed in the preferences: **Edit → Preferences... → Draft → Texts and dimensions → Default ShapeString font file**.
-   For Windows users:
    -   Set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeFontDialog** to {{True}} to use the non-native file dialog when selecting a font file from the ShapeString task panel.
    -   Alternatively, set **Tools → Edit parameters... → BaseApp → Preferences → Dialog → DontUseNativeDialog** to {{True}} to always use the non-native file dialog.

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

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

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



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ShapeString/en
