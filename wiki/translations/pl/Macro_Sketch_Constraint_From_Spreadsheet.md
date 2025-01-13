# Macro Sketch Constraint From Spreadsheet/pl
<div lang="en" dir="ltr" class="mw-content-ltr">


{{Macro
|Name=Macro Sketch Constraint From Spreadsheet
|Description=Macro which, with a simple click on a spreadsheet cell, adds a length constraint to a line, a circle, or between 2 points using a spreadsheet cell alias or address (ex. C2). Future changes to the spreadsheet will update the constraint. The macro can create alias for you.<br>Just select 1 line, 2 points or a constraint, click on a spreadsheet cell and run the macro. You can select lines, points at the ends of a line, points, circles or arcs of circles.<br>
|Author=2cv001
|Download=[https://wiki.freecad.org/images/d/dc/Macro_Sketch_Constraint_From_Spreadsheet.svg ToolBar icon]
|Version=01.04
|Date=2024-11-25
|FCVersion=All
}}


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Description


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

**Contact me in case of any problems.**


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Macro which, with a simple click on a spreadsheet cell, adds a length constraint to a line or between 2 points using a spreadsheet cell alias or address (ex. C2). Future changes to the spreadsheet will update the constraint. The macro can create alias for you.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Just select 1 line, 2 points or a constraint, click on a spreadsheet cell and run the macro. You can select lines, points at the ends of a line, points, circles or arcs of circles.


</div>

![](images/SketchConstraintFromSpreadsheet1.gif )


{{Codeextralink|https://raw.githubusercontent.com/2cv001/FreeCAD-macros/master/Spreadsheet/Sketch_Constraint_From_Spreadsheet.FCMacro}}


<div lang="en" dir="ltr" class="mw-content-ltr">

## Usage


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Automatic Object creation 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If you run the macro and have not yet created a spreadsheet, a body or a sketch, the macro suggests to create one and then opens the sketch in edition mode and the spreadsheet so that you can start filling it.


</div>

![](images/SketchConstraintFromSpreadsheet7.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

### Automatic Alias creation 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

It is not mandatory, but it is better to use aliases in your spreadsheet. The macro can create aliases from texts in cells.
Two modes:

-   a manual mode where you select yourself the cells with text for alias and an automatic mode.
-   and an automatic mode:


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Automatic mode 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

An automatic mode where alias are automatically created using a text zone defined by a cell. The zone includes the cell and those below. These texts correspond to the alias name. The alias is created to the right of its text. The designated cell (here A3) is editable in these dialog boxes:


</div>

![Alias automatic creation](images/SketchConstraintFromSpreadsheet2302.png )

![Alias automatic creation](images/SketchConstraintFromSpreadsheet2303.png ) ![Alias automatic creation](images/SketchConstraintFromSpreadsheet2304.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Manual mode 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

To use manual mode don\'t check the \"Automatic alias\" option.


</div>

![Alias creation](images/SketchConstraintFromSpreadsheet2301.png )

![Alias creation](images/SketchConstraintFromSpreadsheet8.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

### Constraints creation 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

1\) Select:

-   a line,
-   two points (end of a line, center of a circle, etc.)
-   or a length constraint.


</div>

![](images/SelectPoints.png )


<div lang="en" dir="ltr" class="mw-content-ltr">

2\) Click on a spreadsheet cell, with or without an alias, that has a numerical value:


</div>

![](images/Capture1.png )


<div lang="en" dir="ltr" class="mw-content-ltr">

3\) Run the macro.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

4\) Select the desired type of constraint:


</div>

![](images/Choose_type_of_constraint.png )


<div lang="en" dir="ltr" class="mw-content-ltr">

If the cell has an alias, the length property of the constraint will be something like \'Spreadsheet.alias\'. Otherwise, something like \'Spreadsheet.D4\'.


</div>

![](images/If_the_spreadsheet_has_an_alias.png )


<div lang="en" dir="ltr" class="mw-content-ltr">

5\) If the constraint causes a conflict in the sketch and the \"conflict detection\" box is checked, the macro will offer to delete the new constraint:


</div>

![](images/SketchConstraintFromSpreadsheet3.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

If you select an existing constraint, you can change its value for a value from a spreadsheet:


</div>

![](images/SketchConstraintFromSpreadsheet2.gif ) ![](images/SketchConstraintFromSpreadsheet4.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

The macro can also handle external geometry from another sketch:


</div>

![](images/SketchConstraintFromSpreadsheet9.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

To make things even more refined, if, for example, a line is horizontal rather than vertical, when the dialogue box opens, the focus will be on the button for apply a horizontal constraint. If the line is vertical rather than horizontal, the focus will be on the button to apply a vertical constraint. In both cases, simply press the enter key if you are happy with this choice.


</div>

![](images/SketchConstraintFromSpreadsheet5.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

The macro also works for Pads (property Length), Pockets (property Length), Fillets (property Radius), Chamfers (property Size) and Thicknesses (property Value). If you click on a Pad, for example, and then on a cell with the desired value, the Length property of the pad is automatically modified.


</div>

![](images/SketchConstraintFromSpreadsheet20240801.gif )


<div lang="en" dir="ltr" class="mw-content-ltr">

## Links


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

-   [Forum discussion (French)](https://forum.freecad.org/viewtopic.php?t=75972)
-   [Forum discussion (English)](https://forum.freecad.org/viewtopic.php?style=5&t=76990)
-   [Macros recipes](Macros_recipes.md)
-   [How to install macros](How_to_install_macros.md)
-   [How to customize toolbars](Customize_Toolbars.md)


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Credits


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Thanks to openBrain, mario52 and onekk for their help on the code!
Thanks to Syres for tests and for the help on the format in the code.
Thanks to Roy043 and David69 for the various reviews and improvements to the wiki.
Thanks to L\'ami René for tests and ideas.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Script


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

ToolBar Icon ![](images/Macro_Sketch_Constraint_From_Spreadsheet.svg )


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

### Code


</div>

ver 01.04 2024/11/25 by 2cv001 **Macro_Sketch_Constraint_From_Spreadsheet.FCMacro**


<div lang="en" dir="ltr" class="mw-content-ltr">

#### Download


</div>

{{CodeDownload|https://raw.githubusercontent.com/2cv001/FreeCAD-macros/master/Spreadsheet/Sketch_Constraint_From_Spreadsheet.FCMacro| Download latest version of the macro}}



---
⏵ [documentation index](../README.md) > Macro Sketch Constraint From Spreadsheet/pl
