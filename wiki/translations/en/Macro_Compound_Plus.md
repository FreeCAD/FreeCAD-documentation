# Macro Compound Plus/en
{{Macro
|Name=Macro Compound Plus
|Description=Draft command set in a small macro for the 2D wire example: work with the DXF files. The macro detected : Line, Arc, Circle, Ellipse, BSplineCurve and reproduce the DXF wire in a Draft object. The text is converted in ShapeString.
|Author=Mario52
|Version=00.05
|Date=2024-11-11
|FCVersion= 0.21.2 and more
|Download=[https://www.freecadweb.org/wiki/images/f/fd/Macro_Compound_Plus.png ToolBar Icon]
}}

## Description

Draft command set in a small macro for the 2D wire example: work with the DXF files. The macro detected : Line, Arc, Circle, Ellipse, BSplineCurve and reproduce the DXF wire in a Draft object. The text is converted in ShapeString.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/7be361a8c489deec918f664fdcfc4394/raw/2d12268123cbd38a3fba10fff1c7f35837cd3325/Macro_Compound_Plus.FCMacro}}

## Usage

![Macro_Compound_Plus_00](images/Macro_Compound_Plus_00.png )

### Choice

-    **<img src="images/Part_Compound.svg" width=16px> Compound I**Type I \[1 + 1 = 1\] : Create one compound unique of all objects selected without history.

-    **<img src="images/Part_Compound.svg" width=16px> Compound II**Type II \[1 + 1 = A (1 + 1)\] : Create one compound of all objects selected with history of all objects. Same \"**Menu → Part → Make compound**\".

### {{CheckBox}} Option color 

If it {{CheckBox}} checked the colour to object to work are coloured (edge, vertex)

-    **{{ColoredText|#ff0000|<img src="images/Workbench_Image.svg" width=16px> Color** }}: Gives a colour to object. (Default Red 255, 0, 0)

### Tools

-   LineEdit : display (Iindex of Font / Number of font) the path and name of the font.

-    **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)**: convert the text <img alt="" src=images/Draft_Text.svg  style="width:16px;"> in a shape string <img alt="" src=images/Draft_ShapeString.svg  style="width:16px;"> (The height of the text converted is respected but the visual result may not be respected, see the Combo view property for confirm). (A) is Automatic value height of text.

    -   
        {{SpinBox|0,00 Auto}}
        
        : If the spinbox is egual 0.0 the heigth of the VALUE of the text is respected, if other of 0.0 the **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** change to **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (M)** manual.

-    **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**: This command convert the wire in one line with coordinates. (ex: one compound downgraded does not have coordinates, this function create a line with the coordinate as Draft line and reproduce the DXF wire in a Draft object are detected: Line, Arc, Circle, Ellipse, BSplineCurve.

    -   
        {{SpinBox|0,00 Auto}}
        
        : Gives a thickness of the wire. If the spinbox is egual 0.0 the heigth of the VALUE of the text is respected, if other of 0.0 the **<img src="images/Draft_Line.svg" width=16px> Convert Wire (A)** change to **Convert Wire (M)** manual.

-    {{CheckBox|<img src="images/Draft_BezCurve.svg" width=16px> BezierCurve}}: By default the BezierCurve detected is <img alt="" src=images/Draft_BezCurve.svg  style="width:24px;">, if it is checked the BezierCurve is Cubic <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> and the button change {{CheckBox|TRUE|<img src="images/Draft_CubicBezCurve.svg" width=16px> Cubic BezierCurve}}

-    {{RadioButton|TRUE|<img src="images/Std_DrawStyleFlatLines.svg" width=16px> FlatLines}}: The objects created is FlatLines.

-    {{RadioButton|<img src="images/Std_DrawStyleWireFrame.svg" width=16px> Wireframe}}: The objects created is Wireframe.

-    {{RadioButton|<img src="images/Std_DrawStylePoints.svg" width=16px> Points}}: The objects created is Points.

-    **[<img src=images/Draft_Upgrade.svg style="width:16px"> UpGrade**: UpGrade

-    **[<img src=images/Draft_Downgrade.svg style="width:16px"> DownGrade**: DownGrade

### For Compound I and Convert Edge 

This section work only with the tools **<img src="images/Part_Compound.svg" width=16px> Compound I
**, **[<img src=images/Draft_Text.svg style="width:16px"> Convert Text (A)** and **[<img src=images/Draft_Line.svg style="width:16px"> Convert Wire (A)**

-    {{RadioButton|TRUE|None}}: Everything originals objects remains as it is.

-    {{RadioButton|Hidden original objest(s)}}: Hidden the originals objest(s).

-    {{RadioButton|Delete original objest(s)}}: Delete the originals objest(s).

### Force on a form : Line 

If the object line, arc or circle is not reconized (as form in a volume 3D object), this section force the creation of Line, Arc or Circle.

no verification is done, this section tray to create a requested shape 2D (Draft) based on the data provided

-    {{RadioButton|TRUE|<img src="images/Draft_Line.svg" width=16px> Lines}}: Tray to create a Line.

-    {{RadioButton|<img src="images/Draft_Arc.svg" width=16px> Arc}}: Tray to create a Arc.

-    {{RadioButton|<img src="images/Draft_Circle.svg" width=16px> Circle}}: Tray to create a Circle.

-    **<img src="images/Draft_Line.svg" width=16px> Force on : Line**: Button Force

### Command

-   ProgressBar

-    **Reset**: Reset the macro

-    **Quit**: Quit the macro, bye

-    **Help**: Display the wiki page in the FreeCAD browser

## Script

The icon for you toolBar ![](images/Macro_Compound_Plus.png ) copy in same directory to the macro

[How to Customize Toolbars](Customize_Toolbars.md), [How to install macros](How_to_install_macros.md)

The script to github [Macro_Compound_Plus.FCMacro](https://gist.github.com/mario52a/7be361a8c489deec918f664fdcfc4394)

## Links

My macros to [Github](https://gist.github.com/mario52a)

## Version

-   11/11/2024 ver 00.05 : return to **PySide** and replace **WebGui** by **webbrowser**
-   15/08/2020 ver 00.04 : adding section \"Force the forme\" if not detected, create Line, Arc and Circle on forced
-   14/05/2020 ver 00.03 : upgrade pySide2 and Qt5 layout and (matPlotLib Font) and convert Circle, Arc, Ellipse, BezierCurve
-   24/01/2018 ver 00.02 : sup \"import PyQt4\"
-   21/11/2016 ver 00.01 :



---
⏵ [documentation index](../README.md) > Macro Compound Plus/en
