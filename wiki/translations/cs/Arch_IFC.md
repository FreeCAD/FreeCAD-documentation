# Arch IFC/cs
<div class="mw-translate-fuzzy">


{{docnav/cs
|
|[DAE](Arch_DAE.md)
|[Arch Module](Arch_Workbench.md)
}}


</div>


{{TOCright}}

## Description

The <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench.md) and <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM Workbenches](BIM_Workbench.md) feature an [Industry Foundation Classes (IFC)](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) importer and exporter. The IFC format is a continuously growing format to interchange data among [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) applications, used in architecture and engineering.

Both the importer and exporter depend on the [IfcOpenShell](IfcOpenShell.md) library, which is bundled in some distributions of FreeCAD. An easy way to check if IfcOpenShell is available is to enter the following in the [Python console](Python_console.md):


```python
import ifcopenshell
```

If no error message appears, IfcOpenShell is installed, and you may proceed with [importing](Std_Import.md) IFC files. Otherwise, you will need to install IfcOpenShell yourself; read the [IfcOpenShell](IfcOpenShell.md) page to learn more about this process.


**Note:**

the **[<img src=images/BIM_Setup.svg style="width:16px"> [BIM Setup](BIM_Setup.md)** tool will look for IfcOpenShell too, and issue a notification if it is not installed.


**Note 2:**

in the past (2013) the Arch Workbench used to feature a simpler IFC importer that didn\'t depend on IfcOpenShell. This legacy module is still included in the source code but as of v0.19 it is not recommended at all; it will only be able to import a very small subset of IFC objects, and should be considered completely obsolete.

## Importing

All [IfcProduct](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifckernel/lexical/ifcproduct.htm)-based entities from IFC2x3 or IFC4 files will be imported into the FreeCAD document. The IFC preferences settings allow you to set how the IFC objects are imported:

-   **full parametric Arch objects**, the geometry will, as much as possible, be editable in FreeCAD
-   **non-parametric Arch objects**, objects will carry IFC information and properties but will not be editable
-   **non-parametric Part shapes**, the geometry will be faithfully rendered but IFC information will be discarded
-   **one Part shape per floor**, one all-in-one object, just for reference

Each of these types loses some information over the previous one, but is lighter on resources, which allows to open bigger files. A last type allows to discard entirely the importing of Arch objects, which is useful for structural analytic models.

Typically, if you try to open a large file and FreeCAD takes too long to import it, try with a lower import mode.

IfcOpenShell supports all IFC2x3 and IFC4 entities (IFC4-add1 and IFC4-add2 are being implemented in v0.6 and might be available by the time you read this) but not all of them can be converted to [Arch](Arch_Workbench.md) objects, those that can\'t will be imported as simple [Part](Part_Workbench.md) shapes. The IFC importer starts by importing all IFC entities derived from [IfcProduct](http://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifckernel/lexical/ifcproduct.htm), that is, basically, all the objects that compose a building, such as walls or windows or pipes. All other entities needed by one of these objects, such as profiles of extrusion, or components of boolean operations, will be imported as required.

If using an import mode that uses Arch objects, being parametric or not, all objects will carry the full set of [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) attached to each object, grouped by Property Set.

Building structures such as Sites, Buildings and Storeys are also faithfully imported and the structure is correctly recreated in FreeCAD. Group structures (using IfcGroups) are also imported and rendered in FreeCAD, and can be combined with building structures, for ex. having groups inside storeys or storeys inside groups.

[IfcAnnotation](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcproductextension/lexical/ifcannotation.htm) objects are also imported, as well as linear and curve-based [IfcStructuralItem](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralitem.htm)-based entities.

Quantities specified in the IFC file are **NOT** imported. However, since the geometry is fully recreated in FreeCAD, most of the quantities such as length, area, etc. are easily obtainable for each object.

Enabling the **show debug messages** in the IFC preferences settings will print a report indicating if any object from the IFC file failed to import.

**Note**: The BIM Workbench features an [IFC explorer](BIM_IfcExplorer.md) tool that allows you to open an IFC file in fast, text-only mode, and import only the parts you wish.

## Exporting

Exporting to IFC files will export all the selected objects and their descendants. All Arch/BIM objects are supported, as well as other objects created in other workbenches. The only not fully supported objects, at the moment, are **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Bodies](PartDesign_Body.md)**, **[<img src=images/Std_Part.svg style="width:16px"> [Std Parts](Std_Part.md)**, and new structures such as **[<img src=images/Link.svg style="width:16px"> [App Links](Std_LinkMake.md)** and **[<img src=images/LinkGroup.svg style="width:16px"> LinkGroups**, so you will need a bit of testing if using them. [Arch References](Arch_Reference.md) will currently export as `IfcBuildingElementProxies`.

To export a whole site or building or a whole floor or a group containing other objects, it is only needed to select that building or floor or group. Arch objects will be exported with the type set in their \"IFC Type\" property. Their [IfcProperties](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcpropertyresource/lexical/ifcproperty.htm) are exported as well, and if these objects have an IFC UID from a previous import, the same UID will be kept at export. Objects that are not Arch objects are exported as [IfcBuildingElementProxy](http://www.buildingsmart-tech.org/ifc/IFC4/Add1/html/schema/ifcsharedbldgelements/lexical/ifcbuildingelementproxy.htm).

IFC files are exported as IFC2x3 or IFC4 depending on your version of IfcOpenShell, which can be compiled with any of the IFC schemas. If using IfcOpenShell v0.6 or higher, the IFC version specified in the Arch preferences will be used.

If the shape of exported objects is based on an extrusion or a boolean operation, the operation and components will be correctly exported to IFC. If not, the object\'s shape is exported as [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4x1/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm). If the shape contains curves, these will be triangulated. However, IfcOpenShell v0.5 or above feature a serializer, which must be enabled in the Import/Export → IFC preferences. If enabled, this serializer is able to export very complex curved objects such as those based on NURBS, and thus avoid triangulated faces. At the time of writing, though, few other BIM applications support IFC NURBS objects, so a bit of testing is advised.

## Further information 

-   [IfcOpenShell](IfcOpenShell.md), more information on installing this library.


<div class="mw-translate-fuzzy">


{{docnav/cs
|
|[DAE](Arch_DAE.md)
|[Arch Module](Arch_Workbench.md)
}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [File Formats](Category_File Formats.md) > [Arch](Arch_Workbench.md) > Arch IFC/cs
