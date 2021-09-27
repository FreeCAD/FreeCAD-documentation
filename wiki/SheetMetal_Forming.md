---
- GuiCommand:
   Name:SheetMetal Forming
   MenuLocation:SheetMetal → Make Forming in Wall
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**M** **F**
---

# SheetMetal Forming

## Description

The <img alt="" src=images/SheetMetal_Forming.svg  style="width:24px;"> **SheetMetal Forming** command creates an embossed shape in a SheetMetal wall using a separate solid object.

The back side plane of the shape defining solid and the face to be embossed are used to position and orient the embossed shape, i.e. their local coordinate systems will have the same origin and the same orientation by default.  The angle around the z-axis and offsets in x, y, and z direction may be altered by changing the parameter values in the properties window.

A sketch can be added to multiply and distribute the embossed shape in regular or irregular patterns (using the center points of circles or arcs)

A small selection of features that can be created:

 <img alt="" src=images/SheetMetal_Forming-08.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-09.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-10.png  style="width:200px;"> <img alt="" src=images/SheetMetal_Forming-11.png  style="width:200px;">  
*dimples, louvres, drawn cutouts, bridges*

## Usage

Make sure that the body containing the object to be embossed is the active body.

:   If required Double click on its representation in the tree view to activate it.

### Dimple

1.  Select the face of the SheetMetal object to be embossed
2.  Select the **bottom face** (back side) of the shape defining solid
    -   **Note:** Both the object to be embossed **and** the shape defining solid must be selected. Activate the multi-select method appropriate for your operating system: **Control**/**Command**.
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

### Louvre

1.  Select the face of the SheetMetal object to be embossed
2.  Select the **bottom face** (back side) of the shape defining solid
3.  Select a **side face** adjoined to the bottom face to mark the area to be cut open
    -   **Note:** The object to be embossed **and** the shape defining solid **and** the marking cut face must be selected. Activate the multi-select method appropriate for your operating system: **Control**/**Command**.
4.  Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command (see above)

### Bridge

1.  Select the face of the SheetMetal object to be embossed
2.  Select the **bottom face** (back side) of the shape defining solid
3.  Select a **side face** adjoined to the bottom face to mark one area to be cut open
4.  Select the **opposite face** adjoined to the bottom face to mark the other area to be cut open
    -   **Note:** The object to be embossed **and** the shape defining solid, **and** both marking cut faces must be selected. Activate the multi-select method appropriate for your operating system: **Control**/**Command**.
5.  Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command (see above)

### Drawn Cutout 

1.  Select the face of the SheetMetal object to be embossed
2.  Select the **bottom face** (back side) of the shape defining solid
3.  Select the **top face** opposite the bottom face to mark the area to be cut open
    -   **Note:** The object to be embossed **and** the shape defining solid **and** marking face must be selected. Activate the multi-select method appropriate for your operating system: **Control**/**Command**.
4.  Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> [Make Forming in Wall](SheetMetal_Forming.md) command (see above)

### Multiply and Pattern 

To muliply and pattern the embossed feature a **sketch** containing circles and arcs can be added to the **WallForming** object\'s property **Sketch**.

The centerpoints of the circles or arcs are used to provide positions to put instances of the embossed feature; they don\'t influence the instances\' orientation.

The orientation still depends on the orientation of the first selected face.

### Adding Fillets 

1.  Switch to the <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench.md) workbench
2.  Select an edge on the upper side of the SheetMetal object to receive a fillet
3.  Activate the <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Fillet](PartDesign_Fillet.md) command using:
    -   
        **<img src="images/PartDesign_Fillet.svg" width=16px> [Fillet](PartDesign_Fillet.md)
**
        
        button

    -   
        **PartDesign → Apply a dress-up feature → <img src="images/PartDesign_Fillet.svg" width=16px> Fillet
**
        
        drop down menu
4.  Set the Fillet object\'s property  (It is quite **important** for the next fillet)
5.  Select an edge on the bottom side of the SheetMetal object to receive a fillet
6.  Activate the <img alt="" src=images/PartDesign_Fillet.svg  style="width:16px;"> [Fillet](PartDesign_Fillet.md) command (see above)

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

-    **Sketch|Link**: \"Point Sketch on Sheetmetal\". Link to the sketch containing information how to multiply and distribute instances of the Forming Tool. (Center points of circles and arcs are used to create and position these instances)

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
2.  Select the **back side** of the shape defining solid  (Remember both the object to be embossed **and** the shape defining solid must be selected. Activate the multi-select method appropriate for your operating system: <img alt="" src=images/SheetMetal_Forming-04.png  style="width:240px;">
3.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_Forming-05.png  style="width:240px;">
4.  Fillet the sharp edges:
    -   Flip the bowl and select one or more edges for the smaller inner radii
    -   Press the <img alt="" src=images/SheetMetal_Forming-12.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-02.png  style="width:240px;">
    -   Flip the bowl again and select one or more edges for the bigger outer radii
    -   Press the <img alt="" src=images/SheetMetal_Forming-13.png  style="width:240px;"> **\--\>** <img alt="" src=images/SheetMetal_Forming-01.png  style="width:240px;">   Done!  
5.  Alter orientation and position (should be done before filleting)
    -   Activate the <img alt="" src=images/SheetMetal_Forming.svg  style="width:16px;"> WallForming object in the [Tree view](Tree_view.md)
    -   Set the value of the property  <img alt="" src=images/SheetMetal_Forming-14.png  style="width:240px;">
    -   Set the value of the property  <img alt="" src=images/SheetMetal_Forming-06.png  style="width:240px;">  Here it is plain to see that it doesn\'t make sense to move the embossed geometry outside the selected wall.  
    -   Setting the value of the property  <img alt="" src=images/SheetMetal_Forming-07.png  style="width:240px;">  At least the FreeCAD doesn\'t crash when a part has two bodies\...  
6.  Some hints
    1.  The height of the defining solid determines the depth of the embossed shape.  That means changing the parameter **offset, z** to alter the depth won\'t deliver expected results.
    2.  The embossed geometry is made of a shell object i.e. it has a constant thickness.  And so the defining solid has to be offsetable, otherwise the tool will fail to create the emboss.
    3.  If the outer edges are filleted first it may rip the object into several pieces when the radii are set too large.


</div>


</div>






_ _ _

---
[documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > SheetMetal Forming
