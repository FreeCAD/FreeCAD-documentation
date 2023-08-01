# Draft Pattern
## Description

[Draft](Draft_Workbench.md) objects with a **Make Face** property can display an SVG pattern instead of a solid face color.

 ![](images/DraftPatternSample.png )  
*An ellipse and a polygon with an SVG pattern*

## Usage

1.  Make sure the objects are closed and planar, and do not self-intersect.
2.  To close a [Draft Wire](Draft_Wire.md), a [Draft BSpline](Draft_BSpline.md), a [Draft CubicBezCurve](Draft_CubicBezCurve.md) or a [Draft BezCurve](Draft_BezCurve.md) set its **Closed** property to `True`.
3.  To close a [Draft Circle](Draft_Circle.md) or a [Draft Ellipse](Draft_Ellipse.md) set its **First Angle** and **Last Angle** properties to the same value.
4.  Select the objects.
5.  Switch to the **View** tab of the [Property editor](Property_editor.md).
6.  The **Display Mode** must be set to {{Value|Flat Lines}}.
7.  Select a **Pattern**.
8.  Optionally change the **Pattern Size**. Note that a higher value results in a denser pattern.
9.  The pattern is not displayed when the objects are selected. Deselect them to check the result.
10. Optionally reselect the objects to change the pattern properties.

## Available patterns 



Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Notes

-   SVG patterns are stored in **.SVG** files. It is possible to use your own custom patterns. See [Preferences](#Preferences.md).
-   The patterns themselves are not saved in the FreeCAD document. Objects whose **Pattern** cannot be found are displayed with a solid face color instead.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To specify a directory with addition SVG patterns: **Edit → Preferences... → Draft → Visual settings → Alternate SVG patterns location**. Select a file in the directory and then remove the filename in the preferences input box, leaving only the path. After changing this preference you must restart FreeCAD.
-   The **Edit → Preferences... → Draft → Visual settings → SVG pattern resolution** preference is not used.
-   To change the **Pattern Size** used for new objects: **Edit → Preferences... → Draft → Visual settings → SVG pattern default size**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Pattern
