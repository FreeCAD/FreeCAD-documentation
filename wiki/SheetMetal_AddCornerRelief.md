---
- GuiCommand   *
   Name   *SheetMetal AddCornerRelief
   MenuLocation   *SheetMetal → Add Corner Relief
   Workbenches   *[SheetMetal](SheetMetal_Workbench.md)
   Shortcut   ***C** **R**
---

# SheetMetal AddCornerRelief

## Description

The <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width   *24px;"> **SheetMetal AddCornerRelief** command adds a corner relief to a corner of two bends.

 <img alt="" src=images/SheetMetal_AddCornerRelief-01.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-02.png  style="width   *300px;"> 



*Default corner of two bends -> Corner with added corner relief*

The command can as well be used to add a relief to an open corner at one end of a bend.

 <img alt="" src=images/SheetMetal_AddCornerRelief-03.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-04.png  style="width   *300px;"> 



*Default open corner -> Open corner with added corner relief*

This command is restricted to one corner at a time!

## Usage

1.  Select two edges of a corner.
2.  Activate the <img alt="" src=images/SheetMetal_AddCornerRelief.svg  style="width   *16px;"> **SheetMetal AddCornerRelief** command using one of the following   *
    -   The **<img src="images/SheetMetal_AddCornerRelief.svg" width=16px> [Add Corner Relief](SheetMetal_AddCornerRelief.md)** button.
    -   The **SheetMetal → <img src="images/SheetMetal_AddCornerRelief.svg" width=16px> Add Corner Relief** menu option.
    -   The keyboard shortcut   * **C** then **R**

### Different shapes 

The resulting corner relief can be altered by changing property values (see below)   *

The value of the property **ReliefSketch** can be chosen from a list   * {{value|Circle}} (default), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

   *   
    {{value|Circle}}and {{value|Square}} use the value of the property **Size** to scale the relief.

   *   
    {{value|Circle-Scaled}}and {{value|Square-Scaled}} use the value of the property **Size Ratio** to scale the relief.

   *   
    {{value|Sketch}}activates the use of a sketch listed in the property **Sketch** to define the relief shape.

 <img alt="" src=images/SheetMetal_AddCornerRelief-05.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-06.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-07.png  style="width   *200px;"> 



*Circular relief (default settings) -> Square relief (default settings) -> Sketch based relief*

## Notes

-   The k factor defines where within the thickness of a sheet the neutral axis is located.

   *   (It would be nice to know if this factor is according to ISO or ANSI standard\...)


<div class="mw-collapsible mw-collapsed">

### A closer look at the relief sizes 


<div class="mw-collapsible-content">

To get an idea how and where the relief is placed we unfold a default corner without a relief.

 <img alt="" src=images/SheetMetal_AddCornerRelief-08.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-09.png  style="width   *200px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-10.png  style="width   *200px;"> 



*Default corner of two bends -> Corner with unfold solid -> Corner in top view*

The next step is to open the unfold sketch, add a circle through 3 points and add a radius dimension.
Now we add a corner relief, create the corresponding unfold solid and open the first unfold sketch again.
Adding another concentric circle of 3 mm radius reveals that we have found out how the internal circle is positioned as the new circle fits perfectly into the cut-out of the relief\'s unfold solid.

 <img alt="" src=images/SheetMetal_AddCornerRelief-11.png  style="width   *300px;"> <img alt="" src=images/Button_right.svg  style="width   *16px;"> <img alt="" src=images/SheetMetal_AddCornerRelief-12.png  style="width   *300px;"> 



*Default corner with unfold sketch -> Corner with default relief and the same unfold sketch*

Trying to set the property **Size** to a value below the determined 1,67 mm will result in an error; any value above should work fine.

Switching to Circle-Scaled and creating another unfold solid shows that 1,67 mm is the base for the property **Size Ratio**, too.


</div>


</div>

## Properties

See also   * [Property editor](Property_editor.md).

A SheetMetal CornerRelief object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties and its label has a default value   *

### Data


{{Properties_Title|Base}}

-    **Label|String**   * Default value   * The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**   * Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**   * Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **ReliefSketch|Enumeration**   * \"Corner Relief Type\". {{value|Circle}} (default), {{value|Circle-Scaled}}, {{value|Square}}, {{value|Square-Scaled}}, {{value|Sketch}}.

-    **Size|Length**   * \"Size of Shape\". Default   * {{value|3,00 mm}}.

-    **Size Ratio|Float**   * \"Size Ratio of Shape\". Default   * {{value|1,50}}.

-    **base Object|LinkSub**   * \"Base Object\". Links to the pair of edges defining the Corner Relief position.

-    **kfactor|FloatConstraint**   * \"Neutral Axis Position\". Default   * {{value|0,50}}.


{{Properties_Title|Parameters1}}

-    **Sketch|Link**   * \"Corner Relief Sketch\".

-    **XOffset|Distance**   * \"Gap from side one\". Default   * {{value|0,00 mm}}.

-    **YOffset|Distance**   * \"Gap from side two\". Default   * {{value|0,00 mm}}.






[Category   *SheetMetal](Category_SheetMetal.md) [Category   *Addons](Category_Addons.md) [Category   *External Command Reference](Category_External_Command_Reference.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal AddCornerRelief
