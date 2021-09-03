---
- GuiCommand:
   Name:Curves Pipeshell
   MenuLocation:Surfaces → Pipeshell 
   Workbenches:[Curves](Curves_Workbench.md)
---

## Descrizione

The <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Curves Pipeshell](Curves_Pipeshell.md) creates a Pipeshell sweep object. This tool is part of the [external workbench](External_workbenches.md) called [Curves](Curves_Workbench.md).

## Utilizzo

1.  Switch to the <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed)
2.  Select the edge that builds the sweep path in the [3D view](3D_view.md)
3.  Select one or more required profiles in the [Tree view](Tree_view.md)
4.  To invoke the command, do one of the following:
    -   Press the <img alt="" src=images/Curves_Pipeshell.svg  style="width:24px;"> [Creates a Pipeshell sweep object](Curves_Pipeshell.md) button in the tool bar
    -   Use the {{MenuCommand|Surfaces → Pipeshell}}
5.  Change the `Pipeshell` parameter to the required conditions

## Proprietà

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|Main}}

-    **Mode**: Default is **Frenet**. Mode is used to select the sweeping algorithm. Choices: Frenet, DiscreteTrihedron, FixedTrihetron, Binormal, ShapeSupport, AuxiliarySpine.

-    **Output**: Default is **Surface**. Output determines the shape of the object. Choices: Surface, Sections, Lofted Sections.

-    **Profile**: List of the used profiles.

-    **Spine**:


{{Properties_Title|Mode}}

-    **Auxiliary**:

-    **Contact**:

-    **Corrected**:

-    **Direction**:

-    **Equi Curvi**:

-    **Location**:

-    **Support**:


{{Properties_Title|Settings}}

-    **Max Degree**:

-    **Max Segments**:

-    **Samples**:

-    **Solid**: Default is **False**

-    **Tol3d**: Default is **0.00**.

-    **Tol Ang**: Default is **0.00**.

-    **Tol Bound**: Default is **0.00**.

## Notes

-    **Pipeshell**needs a wire object (as the sweep path), and at least one **Pipeshell Profile**.

-   The two tools **Pipeshell** and **Pipeshell Profile** work together as an \"Advanced\" Sweep tool.

## Limitations

## Scripting





{{Curves Tools navi

}} 
