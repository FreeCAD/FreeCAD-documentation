---
- GuiCommand:
   Name: Arch Project
   MenuLocation: Arch -> Project
   Workbenches: Arch_Workbench
   Shortcut: **P** **O**
   SeeAlso: Arch_Site, Arch_Building
---

# Arch Project/en

## Description

The Arch Project is a special object suitable to add better compatibility with [IFC](Arch_IFC.md) files. Every IFC file is required to contain an [IfcProject](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifckernel/lexical/ifcproject.htm) entity. The IfcProject is mostly used to define general project settings such as projection systems, for GIS compatibility, or units systems.

When exporting a FreeCAD model to the IFC file format, if your model does not contain any Project object, a default one will be created automatically, which in most cases will be sufficient. However, you might want to be able to fine-tune the project settings, in which case adding a Project object can be useful. When importing an IFC file, a Project object will always be created. However, if not specifically using it, you can simply delete it after import.

Note that, although any other BIM object can be added to a Project, which the IFC standard does not prohibit, the common way of doing is always to only have [sites](Arch_Site.md) or [buildings](Arch_Building.md) as direct children of a project. All other BIM objects should be inside these sites or buildings. The Project itself should always be at the top of your model structure, that is, it shouldn\'t be included in any other object.

## Usage

1.  Press the **<img src="images/Arch_Project.svg" width=16px> [Arch Project](Arch_Project.md)** button, or press the **P** then **O** keys.
2.  Add any object to your project by drag-and-dropping them onto the Project in the [Tree view](Tree_view.md).



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Project/en
