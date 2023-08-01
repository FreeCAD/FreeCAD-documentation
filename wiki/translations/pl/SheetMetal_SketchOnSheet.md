---
- GuiCommand:
   Name:SheetMetal SketchOnSheet
   MenuLocation:SheetMetal → Sketch On Sheet metal
   Workbenches:[SheetMetal](SheetMetal_Workbench.md)
   Shortcut:**M** **S**
---

# SheetMetal SketchOnSheet/pl

## Description

The <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> [Sketch On Sheet metal](SheetMetal_SketchOnSheet.md) command cuts holes along the folded walls of a sheet metal object. For the hole layout a <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md) is used.

In contrast to the <img alt="" src=images/PartDesign_Pocket.svg  style="width:16px;"> [PartDesign Pocket](PartDesign_Pocket.md) command, where holes are just cut along the sketch normal (local z axis), this tool acts as if it would unfold the sheet metal object, cut the holes, and refold the object.

## Usage

1.  Select a **planar face**
2.  Select a coplanar <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [sketch](Sketcher_Workbench.md) (i.e. lying on the same plane) for the **hole layout** (preferably from the [tree view](Tree_view.md)).
    -   **Note:** Don\'t forget the **Control**/**Command** key!
3.  Activate the <img alt="" src=images/SheetMetal_SketchOnSheet.svg  style="width:16px;"> Sketch On Sheet metal command using the:
    -   
        **<img src="images/SheetMetal_SketchOnSheet.svg" width=16px> [Sketch On Sheet metal](SheetMetal_SketchOnSheet.md)
**
        
        button

    -   
        **SheetMetal → <img src="images/SheetMetal_SketchOnSheet.svg" width=16px> Sketch On Sheet metal
**
        
        drop down menu

    -   keyboard shortcut: **M** then **S**

## Notes

-   The sketch may contain more than just one outline.
-   Any outline has to touch the planar face, at least, otherwise it won\'t cut a hole at all.

## Properties

See also: [Property editor](Property_editor.md).

A SheetMetal SketchOnSheet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

-    **Label|String**: Default value: The user editable name of this object, it may be any arbitrary UTF8 string.

-    **Base Feature|Link|hidden**: Base Feature. Link to the parent feature.

-    **_Body|LinkHidden|hidden**: Hidden link to the parent body.


{{Properties_Title|Parameters}}

-    **Sketch|Link**: \"Sketch on Sheetmetal\". Link to the hole layout/cut-out sketch.

-    **base Object|LinkSub**: \"Base Object\". Link to the planar face where the cut-out starts.

-    **kfactor|FloatConstraint**: \"Gap from Left Side\". Default: {{value|0,50}}.

## Example

<img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:300px;"> 
*A simple thingamajig*


<div class="mw-collapsible mw-collapsed">


<div class="mw-collapsible-content">

### Preparation

This thingamajig is made of a folded sheet metal object with holes added.  And so one open contour sketch for the sheet metal and one sketch for the hole layout have to be prepared in advance.  One straight line of the first sketch must be coplanar to the other sketch plane, this will result in coplanar sketch and face used in the next steps.

<img alt="" src=images/SheetMetal_SketchOnSheet-01.png  style="width:200px;"> 
*Just a contour and a hole layout*

### Workflow

1.  Create a folded sheet metal object
    1.  Select the **contour** sketch  <img alt="" src=images/SheetMetal_SketchOnSheet-02.png  style="width:240px;">
    2.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_SketchOnSheet-03.png  style="width:240px;">  
2.  Cut some holes
    1.  Select the **planar face**
    2.  Select the **hole layout** sketch  <img alt="" src=images/SheetMetal_SketchOnSheet-04.png  style="width:240px;">
    3.  Press the  or use the keyboard shortcut:  <img alt="" src=images/SheetMetal_SketchOnSheet-05.png  style="width:240px;">   Done!  
3.  Some hints
    1.  Check if the folded object\'s thickness is built to the right side.  <img alt="" src=images/SheetMetal_SketchOnSheet-06.png  style="width:240px;">   The yellow contour should lie on the top face of the bottom fold (as shown).  To reverse direction set the value of **Bend Side** property (Outside \<-\> Inside).  
    2.  **Hole shapes** not touching the used planar face won\'t cut holes into the folded object.  <img alt="" src=images/SheetMetal_SketchOnSheet-07.png  style="width:240px;">  The lower rectangle which is hardly touching said face does cut a hole while the upper slot shape doesn\'t.


</div>


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [SheetMetal](Category_SheetMetal.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External Command Reference.md) > SheetMetal SketchOnSheet/pl
