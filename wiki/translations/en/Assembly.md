# Assembly/en
## Introduction


{{TOCright}}

In FreeCAD the word \"[Assembly](Assembly.md)\" is normally used to refer to a [3D model](model.md) that is composed of several distinguishable parts, that are put together in some way to create a functional object, just like real life products are made.

For example, a bolt, a washer and a nut are three separate bodies that when put together comprise an assembly.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*Left: three individual contiguous solids, each of them modelled by a _ to create an assembly.*

## Usage

### Manual assembly 

In general terms, you don\'t need special tools to create assemblies, you just need to have many different [bodies](Body.md) arranged in some way.

To position the bodies where you want them, you can

-   use the [Std TransformManip](Std_TransformManip.md) tool,
-   use the <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Std Placement](Std_Placement.md) dialog, or
-   modify the [placement](Placement.md) property directly in the [property editor](Property_editor.md).

You may use one of the pseudo-assembly [external workbenches](external_workbenches.md), like Lattice2, Manipulator, Part-o-magic, or WorkFeature, to help you find intersections, measure distances, and distribute your objects in the desired way.

In general, the **<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part.md)** object was designed to serve as the basic building block to create assemblies. This object is used to group several [bodies](body.md) and move them together as a unit, that is, as a sub-assembly. Then this sub-assembly can be placed next to, or used inside of other sub-assemblies in order to create the final assembly.

### Constrained assembly 

You can also use a dedicated assembly workbench, like <img alt="" src=images/A2p_workbench.svg  style="width:24px;"> _, or <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4](Assembly4_Workbench.md). Please note that [Assembly2](Assembly2_Workbench.md) is unmaintained, so it is not recommended for new models.

The assembly workbenches use constraints and expressions to create relationships between the objects in your model, in order to mathematically tie the objects in place, for example, \"this face should stick to this other face\", \"this cylinder should be concentric to that circle\", \"this point should follow this edge\", etc.

This is an advanced usage of the software that is normally used in complex mechanical systems. If your [model](model.md) is not very complex, then using an assembly workbench may not be necessary.

## Notes

As of FreeCAD 0.19, there is no official assembly workbench included by default with the system. Assembly workbenches are difficult to program because many problems need to be solved regarding the efficient use of [bodies](Body.md) and [parts](Part.md) in your model. Nevertheless, the introduction of the [App Link](App_Link.md) object has improved the situation.

Please note that assembly workbenches are generally incompatible with each other. If you create an assembly with one of these workbenches, you should stick to it, and not use another assembly workbench to work with the same document.

The assembly workbenches continue development, and it is expected that at some point one assembly workbench will emerge as the \"official\" one. This could happen by promoting one of the current assembly workbenches, or by combining them to produce a more complete solution.


{{Std Base navi

}} {{Document objects navi}} 

_

---
[documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/en
