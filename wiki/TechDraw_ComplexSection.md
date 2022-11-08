---
- GuiCommand   *
   Name   *TechDraw ComplexSection
   MenuLocation   *TechDraw → Insert Complex Section
   Workbenches   *[TechDraw](TechDraw_Workbench.md)
   Version   *1.0
   SeeAlso   *[TechDraw Section](TechDraw_SectionView.md), [TechDraw View](TechDraw_View.md), [TechDraw Projection Group](TechDraw_ProjectionGroup.md)
---

# TechDraw ComplexSection

## Description

The Complex Section tool creates a cross section view based on a profile and an existing part view.

 <img alt="" src=images/TechDraw_QuarterSection_example.png  style="width   *250px;">  
*A quarter section view created with the Complex Section tool*

 <img alt="" src=images/TechDraw_AlignedSection_example.png  style="width   *250px;">  
*An aligned section view created with the Complex Section tool*

 <img alt="" src=images/TechDraw_OffsetSection_example.png  style="width   *250px;">  
*An offset section view created with the Complex Section tool*

## Usage

1.  Select a part view and a profile object in the 3D window or tree. Profiles are typically Sketches, but any object whose shape can be made into a wire will work.
2.  Press the **<img src="images/TechDraw_ComplexSection.svg" width=16px> [Insert Complex Section](TechDraw_ComplexSection.md)** button
3.  A dialog will open which will help calculate the various Complex Section properties. The dialog calculates reasonable starting points for the view Direction, but these may be changed.
4.  If you make a mistake, or change your mind while setting up the Section parameters, press the **Reset** button, and you can start over.

 <img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width   *" height="380px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width   *" height="380px;"> 

## Properties ComplexSection 

See also [TechDraw SectionView](TechDraw_SectionView#Properties.md).

### Data


{{TitleProperty|Cutting Tool}}

-    **CuttingToolWireObject**   * The document object whose shape will be used to generate the cutting profile.

-    **ProjectionStrategy**   * Controls how the cut is performed and how the result is projected to the page.

    -   
        {{Value|Offset}}
        
           * Performs a simple cut of the Source shape and projects the result.

    -   
        {{Value|Aligned}}
        
           * Cuts the Source shape using a tool created from each segment (edge) of the cutting profile. The results of each cut are projected in a vertical or horizontal array, depending on the orientation of the cutting profile.

    -   
        {{Value|NoParallel}}
        
           * As Aligned, but profile segments which are parallel to the view direction are skipped.

## Notes

-   **TrimAfterCut**   * the section cut operation sometimes leaves behind a portion of the source shape. If TrimAfterCut is true, an additional cut operation is performed on the result of the first cut and should remove any unwanted pieces.

## Scripting


**See also   ***

[TechDraw API](TechDraw_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ComplexSection tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following functions   *

 
```python
view = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewPart','View')
rc = page.addView(view)
view.Source = box
view.Direction = (0.0,0.0,1.0)

profile = FreeCAD.ActiveDocument.Sketch

section = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawComplexSection','ComplexSection')
rc = page.addView(section)
section.BaseView = view
section.CuttingToolWireObject = profile
```




 {{TechDraw Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ComplexSection
