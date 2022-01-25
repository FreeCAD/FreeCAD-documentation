---
- GuiCommand:
   Name:Draft Text
   MenuLocation:Annotation → Text
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**T** **E**
   Version:0.7
   SeeAlso:[Draft Label](Draft_Label.md), [Draft ShapeString](Draft_ShapeString.md)
---

# Draft Text

## Description

The <img alt="" src=images/Draft_Text.svg  style="width:24px;"> **Draft Text** command creates a multi-line text at a given point.

To create a text element with an arrow use the [Draft Label](Draft_Label.md) command instead.

<img alt="" src=images/Draft_Text_example.png  style="width:400px;"> 
*Single point required to position the text*

## Usage

See also: [Draft Tray](Draft_Tray.md) and [Draft Snap](Draft_Snap.md).

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Text.svg" width=16px> [Draft Text](Draft_Text.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Text.svg" width=16px> Text** option from the menu.
    -   Use the keyboard shortcut: **T** then **E**.
2.  The **Text** task panel opens. See [Options](#Options.md) for more information.
3.  Pick a point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button.
4.  Enter the desired text, press **Enter** to start a new line.
5.  Press **Enter** twice or press the **<img src="images/Button_valid.svg" width=16px> Create text** button to finish the command.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   The **Relative** checkbox, displayed in FreeCAD version 0.19 and earlier, has no purpose for this command.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **T** or click the **Continue** checkbox to toggle continue mode. If continue mode is on, the command will restart after finishing, allowing you to continue creating texts. The shortcut does not work in the second task panel. This option is not available in the first task panel in FreeCAD version 0.19 and earlier.
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Notes

-   A Draft Text can be edited by double-clicking it in the [Tree view](Tree_view.md). <small>(v0.20)</small> 
-   Draft Texts created with [FreeCAD version 0.18](Release_notes_0.18.md) are not backward compatible.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Text object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated.

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: specifies the position of the text in the [3D view](3D_view.md). See [Placement](Placement.md).

-    **Text|StringList**: specifies the contents of the text. Each item in the list represents a new text line.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the text. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the text.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|3D text}} the text will be displayed in a plane defined by its **Placement**. If it is {{value|2D text}} the text will always face the camera. This is an inherited property.


{{TitleProperty|Graphics}}

-    **Line Color|Color**: not used.

-    **Line Width|Float**: not used.


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead.

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small.

-    **Justification|Enumeration**: specifies if the alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Text Color|Color**: specifies the color of the text.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Text use the `make_text` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeText` method.

 
```python
text = make_text(string, placement=None, screen=False)
```

-   Creates a `text` object, at `placement`, which can be a `FreeCAD.Placement`, but also a `FreeCAD.Rotation` or a `FreeCAD.Vector`.

-    `string`is a string or a list of strings. If it is a list, each element is displayed on its own line.

-   If `screen` is `True`, the text always faces the camera, otherwise it is displayed in a plane defined by its **Placement**.

The view properties of `text` can be changed by overwriting its attributes; for example, overwrite `ViewObject.FontSize` with the new size in millimeters.

Example:

 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

t1 = "This is a sample text"
p1 = App.Vector(0, 0, 0)

t2 = ["First line", "second line"]
p2 = App.Vector(1000, 1000, 0)

text1 = Draft.make_text(t1, p1)
text2 = Draft.make_text(t2, p2)
text1.ViewObject.FontSize = 200
text2.ViewObject.FontSize = 200

zaxis = App.Vector(0, 0, 1)

t3 = ["Upside", "down"]
p3 = App.Vector(-1000, -500, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 180))
text3 = Draft.make_text(t3, place3)
text3.ViewObject.FontSize = 200

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Text
