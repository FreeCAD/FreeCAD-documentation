---
- GuiCommand:
   Name:SheetMetal Forming
   MenuLocation:SheetMetal → Make Forming in Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**M** **F**
---

## Description

The <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> **SheetMetal Forming** command creates an embossed shape in a SheetMetal wall using a separate solid object.

The back side plane of the shapedefining solid is used to position and orient the embossed shape, i.e. their local coordinate systems will have the same origin and the same orientation by default.  The angle around the z-axis and offsets in x, y, and z direction may be altered by changing the parameter values in the properties window.

## Usage

1.  Select the wall of the SheetMetal object to be embossed
2.  Select the **back side** of the shape defining solid
    -   **Note:** Don\'t forget the **Control**/**Command** key!
3.  Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command using:
    -   
        **<img src="images/SheetMetal_Forming.svg" width=16px> [Make Forming in Wall](SheetMetal_Forming.md)
**
        
        button

    -   
        **SheetMetal → <img src="images/SheetMetal_Forming.svg" width=16px> Make Forming in Wall
**
        
        drop down menu

    -   keyboard shortcut: **M** then **F**

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal WallForming object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**:


{{Properties_Title|Parameters}}

-    **Suppress Feature|Bool**: \"Suppress Forming Feature\". Default value is `False`.

-    **angle|Angle**: \"Tool Position Angle\". Default angle: {{value|0,00°}}.

-    **base Object|LinkSub**: \"Base Object\". Link to the planar face to be embossed.

-    **offset|VectorDistance**: \"Offset from Center of Face\". Default: {{value|[0,00 mm, 0,00 mm, 0,00 mm]}}.

-    **thickness|Distance**: \"Thickness of Sheetmetal\". Thickness of the **Base Feature||hidden**:.

-    **tool Object|LinkSub**: \"Forming Tool Object\". Link to the planar face used to position the Forming Tool


{{Properties_Title|Parameters1}}

-    **Sketch|Link**: \"Point Sketch on Sheetmetal\".

## Example

 <img alt="" src=images/SheetMetal_Forming-01.png  style="width:300px;"> <img alt="" src=images/SheetMetal_Forming-02.png  style="width:300px;"> 


*A hexagon bowl with embossed centre*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Preparation

This bowl is made of a folded sheet metal object with a shape embossed, both have to be prepared in advance.

No need to work with coplanar sketches here.

 <img alt="" src=images/SheetMetal_Forming-03.png  style="width:200px;"> 


*SheetMetal bowl and embossing object*

### Workflow

1.  Select the wall of the SheetMetal object to be embossed
2.  Select the **back side** of the shape defining solid  <img alt="" src=images/SheetMetal_Forming-04.png  style="width:240px;">
3.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_Forming-05.png  style="width:240px;">   Done!  
4.  Alter orientation and position
    1.  Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> WallForming object in the [Tree view](Tree_view.md)
    2.  Set the value of the parameter **angle** to e.g. 45°  <img alt="" src=images/SheetMetal_Forming-01.png  style="width:240px;">
    3.  Set the value of the parameter **offset, x** to e.g. greater than 0  <img alt="" src=images/SheetMetal_Forming-06.png  style="width:240px;">  Here it is plain to see that it doesn\'t make sense to move the embossed geometry outside the selected wall.  
    4.  Setting the value of the parameter **offset, z** to e.g. greater than 0 isn\'t any better:  <img alt="" src=images/SheetMetal_Forming-07.png  style="width:240px;">  At least the FreeCAD doesn\'t crash when a part has two bodies\...  
5.  Some hints
    1.  The height of the defining solid determines the depth of the embossed shape.  That means changing the parameter **offset, z** to alter the depth won\'t deliver expected results.
    2.  The embossed geometry is made of a shell object i.e. it has a constant thickness.  And so the defining solid has to be offsetable, otherwise the tool will fail to create the emboss.


</div>


</div>






[Category:SheetMetal](Category:SheetMetal.md) [Category:Addons](Category:Addons.md) [Category:External Command Reference](Category:External_Command_Reference.md)
