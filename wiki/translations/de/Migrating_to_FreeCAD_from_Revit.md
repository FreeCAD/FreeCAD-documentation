# Migrating to FreeCAD from Revit/de
This page is intended to give you a quick start with FreeCAD if you are coming from Autodesk Revit.

### Setting things up 

FreeCAD is a multi-purpose 3D modeling application. Although it is not solely a BIM application, it features a dedicated [BIM Workbench](BIM_Workbench.md), which is bundled with every FreeCAD installation, and contains a set of BIM tools.

### Key concepts 

Although you will be able to perform the same tasks and obtain a similar result to what you are used to in Revit, both software are different and you should learn the differences.

-   The Revit file format (.RVT) is proprietary, non-documented, and is not supported by FreeCAD (supporting it would be a gigantic task which would swallow all of FreeCAD resources for a very incomplete result). Instead, you should rely on open formats such as [IFC](Arch_IFC.md), which is rather well supported by both applications. Families can also be exported to ACIS/SAT which is supported by the InventorLoader addon, installable via the [Addons manager](Std_AddonMgr.md).

-   BIM assets such as windows, equipment or furniture are usually easy to find on popular websites such as [bimobject.com](https://bimobject.com) in IFC format. But the format does not always guarantee the quality of the geometry. The [grabcad library](https://grabcad.com/library?softwares=step-slash-iges) has a good selection of downloadable assets in STEP format with good geometry quality.

-   There is no concept of family in FreeCAD. But there are many ways to obtain the same result, that is, several objects that share the same properties and are linked together (if you modify one, you modify them all). The most straightforward is [cloning](Draft_Clone.md). A clone is like a copy of an object, but if you modify the original object, its clones will get updated too. But there are other, more subtle ways to make objects share properties. For example, you can draw a 2D profile and build several objects from the same 2D profile.

-   Although they can be convenient, you don\'t need to use the BIM tools to produce BIM objects. Any FreeCAD object, or even objects made with another software, can become BIM objects. You only need to select one and use the [Component](Arch_Component.md) tool. This also allows you to use other tools, for example from the [PartDesign Workbench](PartDesign_Workbench.md), to create complex objects that are usually hard to achieve with standard BIM tools.

-   Objects created with one BIM tool can have all supported BIM types. You only need to change their **IFC Type** property. So, for example, you can create a beam using the wall tool, just by changing its IFC type to \"Beam\" afterwards.

-   BIM tools follow the [Draft Workbench](Draft_Workbench.md) philosophy: They can be created anywhere and anyhow in the 3D space. You just need to set your [working plane](Draft_Snap_WorkingPlane.md) correctly, then next BIM objects will be created on that plane.

-   There is no mandatory building structure (floors in Revit) in FreeCAD. You can group your objects using [groups](Std_Group.md), or [Building parts](Arch_BuildingPart.md) (which are commonly used to make levels, but can actually be used for any kind of grouping) to work the same way as in Revit, but you are the one who chooses the most appropriate way for your project.

### Suggested adoption workflow 

-   Don\'t try to migrate at once. Learning a new software is a complex task. FreeCAD is free, start with installing and exploring it, then when you can, use it to model a small part of a project, then as you gain knowledge and mastery, do more and more in FreeCAD and less in Revit.

-   Make sure you can always fall back to Revit if things go wrong: Export to IFC early and often, open the file in Revit, make sure everything is there.

-   Creating views and sheets works like in Revit, if you are using [Draft](Draft_Workbench.md) views (the recommended way). Create [shape views](Draft_Shape2DView.md) of your objects or levels, move them out of your model, annotate them, place everything in a group or [Building part](Arch_BuildingPart.md), then create [TechDraw](TechDraw_Workbench.md) pages and add your Draft views to it.

### Further reading 

-   the [BIM Workbench](BIM_Workbench.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)



---
⏵ [documentation index](../README.md) > Migrating to FreeCAD from Revit/de
