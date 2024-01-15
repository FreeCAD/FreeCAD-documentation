---
 GuiCommand:
   Name: Part Mirror
   MenuLocation: Part , Mirroring...
   Workbenches: Part_Workbench
---

# Part Mirror/en

## Description

**Part Mirror** creates a new object (image) which is a reflection of the original object (source). The image object is created behind a mirror plane. The mirror plane may be standard plane (**XY**, **YZ**, or **XZ**), any plane parallel to a standard plane, or (<small>(v0.22)</small> ) any arbitrary plane by using a reference object.

An example:

![](images/PARTMirrorBeforev11.png )



*Before*

![](images/PARTMirrorAfterv11.png )



*After mirrored through YZ plane*

## Usage

![](images/PartMirroring_Scr1.png )

1.  Optionally select one or more source objects.
2.  There are several ways to invoke the command:
    -   Press the **<img src="images/Part_Mirror.svg" width=16px> [Mirroring...](Part_Mirror.md)** button.
    -   Select the **Part → <img src="images/Part_Mirror.svg" width=16px> Mirroring...** option from the menu.
3.  If you have not yet selected objects or want to change the selection: pick one or more objects from the **Shapes** list.
4.  Do one of the following:
    -   Select a standard **Mirror plane** from the dropdown list.
    -   Select a reference object in the [Tree view](Tree_view.md) or the [3D view](3D_view.md). The reference object can be any planar face or circular edge.
5.  Press the **OK** button.
6.  For each source object a separate Part Mirror object is created.

When the select button label says **Selecting** you are in reference selection mode and there is a selection gate in effect, which disallows the selection of unsupported reference objects. Click the button to toggle the selection gate off, the button label then changes to **Select reference**.

The mirror plane is defined by a **Normal** (direction) and a **Base** (position). When the **Mirror Plane** property contains a reference object these properties are made read-only as they are then computed based on that object. The plane is infinite even if the reference object is not.

A reference object can be a planar face, such as the face of a [Part Box](Part_Box.md), a circular edge, a [Datum Plane](PartDesign_Plane.md), an [origin plane](App_OriginGroupExtension.md) of a [Std Part](Std_Part.md) container, or any object with a single planar face or single circular edge. There is also support for [Links](App_Link.md). Note, however, that B-spline surfaces, such as [ruled surfaces](Part_RuledSurface.md) or [loft faces](Part_Loft.md) are not supported.

## Options

If a standard plane instead of a reference object is selected, the **Base point** boxes can be used to move it. Only one of the **X**, **Y**, or **Z** boxes is effective for a given standard plane.

  Standard plane   Base point box   Effect
    
  **XY**           **Z**            Move mirror plane along **Z** axis
  **XY**           **X**, **Y**     No effect
  **XZ**           **Y**            Move mirror plane along **Y** axis
  **XZ**           **X**, **Z**     No effect
  **YZ**           **X**            Move mirror plane along **X** axis
  **YZ**           **Y**, **Z**     No effect

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 
-   After selecting a standard mirror plane, the **Normal** and **Base** of the Part Mirror object can be changed to any value. So that even without a reference object you are not restricted to the standard planes.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/en
