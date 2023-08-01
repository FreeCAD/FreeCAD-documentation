# <img alt="Manipulator workbench icon" src=images/Manipulator_workbench_icon.svg  style="width:64px;"> Manipulator Workbench/hr

## Predstavljanje


{{TOCright}}

The [Manipulator Workbench](Manipulator_Workbench.md) is an [external workbench](External_workbenches.md) aimed to help FreeCAD users with Aligning, Moving, Rotating and Measuring 3D objects through a friendly GUI. These series of tools help to Transform the placement and Measure objects and STEP models in FreeCAD.


<div class="mw-translate-fuzzy">

**Obilježja:**


</div>

![](images/Aligner-ico.png ) **Aligner:** a set of tools to move and align 3D parts; it can also align an object (face, edge, point) to the origin in FreeCAD.

![](images/Manipulator_Mover.svg ) **Mover:** a set of tools to move and rotate 3D parts on different Axis

![](images/Manipulator_Caliper.svg ) **Caliper:** a set of tools to measure 3D parts, with some Snap facility and Radius, Length, Angle measurements.

These helpers work with **Part, App::Part and Body objects**.

The Tools can be **Floating** or **Docked Left or Right**.

Each Tool has a **Help Button** ![](images/Help-btn.png ) to get some useful tips

## References

-   Author on github: [\@easyw](https://github.com/easyw)
-   FreeCAD Forums: [easyw-fc](https://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=6387)
-   Source code on github: <https://github.com/easyw/Manipulator>
-   Forum announcements/discussion: <https://forum.freecadweb.org/viewtopic.php?t=24742>

## Tutorial

<img alt="Title Manipulator-WB-@Work" src=images/Manipulator-WB-@Work.png  style="width:1024px;">



*YouTube Tutorial [https://youtu.be/owGzsd1fyZc Manipulator WorkBench @Work]*

## Alati

![](images/Manipulator-WB-Tools.png ) 
*Above: Manipulator workbench dialog. For a more detailed description see [https://github.com/easyw/Manipulator/blob/master/README.md README.md] on Github.*

### Aligner

![](images/Manipulator-WB-Aligner.gif ) 
*Aligner: set of tools to move and align 3D parts; it can also align an object (face, edge, point) to the origin in FreeCAD*

### Mover

![](images/Manipulator-WB-Mover.gif ) 
*Mover: set of tools to move and rotate 3D parts on different Axis*

![](images/Manipulator-WB-Mover-with-App_Part&Body.gif ) 
*Mover: Using App:Part and Body*

![](images/Manipulator-WB-Mover-with-External-Reference.gif ) 
*Mover: with External Reference*

### Caliper

![](images/Manipulator-WB-Measure-Radius.gif ) 
*Caliper: measuring Radius*

![](images/Manipulator-WB-Measure-Angles.gif ) 
*Caliper: measuring Angles*

![](images/Manipulator-WB-Dimension.gif ) 
*Caliper: measuring Dimensions*

![](images/Manipulator-WB-Dimension-2.gif ) 
*Caliper: measuring Dimensions (cont.)*

![](images/Manipulator-WB-Parallel-Planes-Distance.gif ) 
*Caliper: parallel planes distance*

### Manipulator

![](images/Manipulator-WB-Assembly-Parts.gif )

## Instalacija

### Automatic Installation 

The recommended way to install the Manipulator Workbench is via the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) under the **Tools → Addon Manager** menu.


<div class="mw-collapsible mw-collapsed toccolours" style="width:600px">

### Manual Installation 

If a manual install is necessary please follow the following instructions:


<div class="mw-collapsible-content">

-   Copying the Manipulator source in to the **Mod** sub-directory of the FreeCAD application.


```python
cd ~/.FreeCAD/Mod 
git clone https://github.com/easyw/Manipulator Manipulator
```

-   Restart FreeCAD


</div>


</div>

### Supports

-   FreeCAD v0.15 4671
-   FreeCAD v0.16 \>= 6712
-   FreeCAD v0.17 \>= 11707
-   FreeCAD v0.18+
-   FreeCAD v0.19+

## History

The workbench evolved out of the [Center Align Objects with Faces or Edges](Macro_Center_Align_Objects_with_Faces_or_Edges.md) macro

## External workbenches 

FreeCAD workbenches are easy to program in [Python](Python.md), there are therefore many people developing additional workbenches outside of the FreeCAD main developers.

The [external workbenches](External_workbenches.md) page has some information and tutorials on some of them, and the [FreeCAD Addons](https://github.com/FreeCAD/FreeCAD-addons) project aims at gathering them and making them easily installable from within FreeCAD.

New workbenches are in development, stay tuned!



---
![](images/Button_right.svg) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Manipulator Workbench/hr
