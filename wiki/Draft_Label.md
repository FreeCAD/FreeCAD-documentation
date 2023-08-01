---
- GuiCommand:
   Name:Draft Label
   MenuLocation:Annotation → Label
   Workbenches:[Draft](Draft_Workbench.md), [Arch](Arch_Workbench.md)
   Shortcut:**D** **L**
   Version:0.17
   SeeAlso:[Draft Text](Draft_Text.md), [Draft ShapeString](Draft_ShapeString.md)
---

# Draft Label

## Description

The <img alt="" src=images/Draft_Label.svg  style="width:24px;"> **Draft Label** command creates a multi-line text with a 2-segment leader line and an arrow.

If an object or a sub-element (face, edge or vertex) is selected when starting the command, the text can be made to display one or two attributes of the selected element, including position, length, area, volume and material. The text will then be linked to the attributes and will update if their values change.

To insert a text element without an arrow use the [Draft Text](Draft_Text.md) command instead.

 <img alt="" src=images/Draft_Label_example.jpg  style="width:400px;">  
*Various labels with different orientations, arrows and information*

## Usage

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).

1.  Optionally select an object or a sub-element (vertex, edge or face) that you want to display attributes of.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_Label.svg" width=16px> [Draft Label](Draft_Label.md)** button.
    -   Select the **Annotation → <img src="images/Draft_Label.svg" width=16px> Label** option from the menu.
    -   Use the keyboard shortcut: **D** then **L**.
3.  The **Label** task panel opens. See [Options](#Options.md) for more information.
4.  If you have selected an element: select an option from the **Label type** dropdown list. See [Label types](#Label_types.md) below.
5.  Pick the first point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button. This point indicates the target (arrow head). This can be anywhere, it does not have to be on an element.
6.  Pick the second point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button. This point indicates the start of the horizontal or vertical segment of the leader.
7.  Pick the third point in the [3D view](3D_view.md), or type coordinates and press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button. This point indicates the base point of the text.

## Options

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.

-   To manually enter coordinates enter the X, Y and Z component, and press **Enter** after each. Or you can press the **<img src="images/Draft_AddPoint.svg" width=16px> Enter point** button when you have the desired values. It is advisable to move the pointer out of the [3D view](3D_view.md) before entering coordinates.
-   Press **R** or click the **Relative** checkbox to toggle relative mode. If relative mode is on, coordinates are relative to the last point, if available, else they are relative to the coordinate system origin.
-   Press **G** or click the **Global** checkbox to toggle global mode. If global mode is on, coordinates are relative to the global coordinate system, else they are relative to the [working plane](Draft_SelectPlane.md) coordinate system. <small>(v0.20)</small> 
-   Press **S** to switch [Draft snapping](Draft_Snap.md) on or off.
-   Press **Esc** or the **Close** button to abort the command.

## Label types 

The following label types are available:

-    {{Value|Custom}}: displays the contents of **Custom Text**.

-    {{Value|Name}}: displays the internal name of the target object. The internal name is assigned when an object is created and remains fixed throughout the existence of the object.

-    {{Value|Label}}: displays the label of the target object. The label of an object can be changed by the user.

-    {{Value|Position}}: displays the coordinates of the base point of the target object, of the target vertex, or of the center of mass of the target subelement, if applicable.

-    {{Value|Length}}: displays the length of the target object or subelement, if applicable.

-    {{Value|Area}}: displays the area of the target object or subelement, if applicable.

-    {{Value|Volume}}: displays the volume of the target object, if applicable.

-    {{Value|Tag}}: displays the `Tag` attribute of the target object, if applicable. Objects created with the [Arch Workbench](Arch_Workbench.md) can have this attribute.

-    {{Value|Material}}: displays the label of the material of the target object, if applicable.

-    {{Value|Label + Position}}
    

-    {{Value|Label + Length}}
    

-    {{Value|Label + Area}}
    

-    {{Value|Label + Volume}}
    

-    {{Value|Label + Material}}
    

## Notes

-   The direction of the second segment of the leader determines the alignment of the text. If the segment is horizontal and pointing to the right the text is aligned to the left and vice versa. If the second segment goes vertically up, the text is aligned to the left. If it goes vertically down, the text is aligned to the right.
-   Draft Labels created or saved with [FreeCAD version 0.21](Release_notes_0.21.md) are not backward compatible.

## Properties

See also: [Property editor](Property_editor.md).

A Draft Label object is derived from an [App FeaturePython](App_FeaturePython.md) object and inherits all its properties. The following properties are additional unless otherwise stated:

### Data


{{TitleProperty|Label}}

-    **Custom Text|StringList**: specifies the contents of the text if **Label Type** is {{Value|Custom}}. Each item in the list represents a new text line.

-    **Label Type|Enumeration**: specifies the type of information displayed by the label. See [Label types](#Label_types.md).

-    **Placement|Placement**: specifies the position of the text in the [3D view](3D_view.md) and, unless **Straight Direction** is {{Value|Custom}}, also of the first leader segment, which is the segment where the text is attached. See [Placement](Placement.md).

-    **Text|StringList**: (read-only) specifies the contents of the text that is actually displayed. Each item in the list represents a new text line.


{{TitleProperty|Leader}}

-    **Points|VectorList**: specifies the points of the leader.

-    **Straight Direction|Enumeration**: specifies the direction of the first leader segment: {{Value|Custom}}, {{Value|Horizontal}} or {{Value|Vertical}}.

-    **Straight Distance|Distance**: specifies the length of the first leader segment. Only used if **Straight Direction** is {{Value|Horizontal}} or {{Value|Vertical}}. If the distance is positive, the leader starts from the right side of the text and the text aligns to the right. Otherwise the leader starts from the left side of the text and the text aligns to the left.


{{TitleProperty|Target}}

-    **Target|LinkSub**: specifies the object and optional subelement the label is linked to.

-    **Target Point|Vector**: specifies the position of the tip of the leader, which is where the arrow is attached.

### View


{{TitleProperty|Annotation}}

-    **Annotation Style|Enumeration**: specifies the annotation style applied to the label. See [Draft AnnotationStyleEditor](Draft_AnnotationStyleEditor.md).

-    **Scale Multiplier|Float**: specifies the general scaling factor applied to the label.


{{TitleProperty|Display Options}}

-    **Display Mode|Enumeration**: specifies how the text is displayed. If it is {{value|World}} the text will be displayed on a plane defined by the **Placement** of the label. If it is {{value|Screen}} the text will always face the screen. This is an inherited property. The mentioned options are the renamed options (<small>(v0.21)</small> ).


{{TitleProperty|Graphics}}

-    **Arrow Size|Length**: specifies the size of the symbol displayed at the tip of the leader.

-    **Arrow Type|Enumeration**: specifies the type of symbol displayed at the tip of the leader, which can be {{value|Dot}}, {{value|Circle}}, {{value|Arrow}}, {{value|Tick}} or {{value|Tick-2}}.

-    **Frame|Enumeration**: specifies what type of frame is drawn around the text. The current options are {{Value|None}} or {{Value|Rectangle}}.

-    **Line|Bool**: specifies whether to display the leader line. If it is `False` only the arrow and the text are displayed.

-    **Line Color|Color**: specifies the color of the leader and the arrow. This is also used for the frame (<small>(v0.20)</small> ).

-    **Line Width|Float**: specifies the width of the leader. This is also used for the frame (<small>(v0.20)</small> ).


{{TitleProperty|Text}}

-    **Font Name|Font**: specifies the font used to draw the text. It can be a font name, such as {{value|Arial}}, a default style such as {{value|sans}}, {{value|serif}} or {{value|mono}}, a family such as {{value|Arial,Helvetica,sans}}, or a name with a style such as {{value|Arial:Bold}}. If the given font is not found on the system, a default font is used instead. <small>(v0.21)</small> 

-    **Font Size|Length**: specifies the size of the letters. The text can be invisible in the [3D view](3D_view.md) if this value is very small. <small>(v0.21)</small> 

-    **Justification|Enumeration**: specifies the horizontal alignment of the text: {{value|Left}}, {{value|Center}} or {{value|Right}}. Only used if **Straight Direction** is {{Value|Custom}}. Otherwise the horizontal alignment is based on the sign (positive or negative) of **Straight Distance**.

-    **Line Spacing|Float**: specifies the factor applied to the default line height of the text.

-    **Max Chars|Integer**: specifies the maximum number of characters on each line of the text.

-    **Text Alignment|Enumeration**: specifies the vertical alignment of the text: {{value|Top}}, {{value|Middle}} or {{value|Bottom}}.

-    **Text Color|Color**: specifies the color of the text.

## Scripting

See also: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To create a Draft Label use the `make_label` method (<small>(v0.19)</small> ) of the Draft module. This method replaces the deprecated `makeLabel` method.

 
```python
label = make_label(target_point=App.Vector(0, 0, 0),
                   placement=App.Vector(30, 30, 0),
                   target_object=None, subelements=None,
                   label_type="Custom", custom_text="Label",
                   direction="Horizontal", distance=-10,
                   points=None)
```

Example:

 
```python
import FreeCAD as App
import Draft

doc = App.newDocument()

rectangle = Draft.make_rectangle(4000, 1000)
doc.recompute()

p1 = App.Vector(-200, 1000, 0)
place1 = App.Placement(App.Vector(-1000, 1300, 0), App.Rotation())

label1 = Draft.make_label(p1, place1, target_object=rectangle, distance=500, label_type="Label")
label1.ViewObject.TextSize = 200

p2 = App.Vector(-200, 0, 0)
place2 = App.Placement(App.Vector(-1000, -300, 0), App.Rotation())

label2 = Draft.make_label(p2, place2, target_object=rectangle, distance=500, label_type="Custom",
                          custom_text="Beware of the sharp edges")
label2.ViewObject.TextSize = 200

p3 = App.Vector(1000, 1200, 0)
place3 = App.Placement(App.Vector(2000, 1800, 0), App.Rotation())

label3 = Draft.make_label(p3, place3, target_object=rectangle, distance=-500, label_type="Area")
label3.ViewObject.TextSize = 200

doc.recompute()
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Label
