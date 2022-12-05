---
- GuiCommand:
   Name:PartDesign Migrate
   MenuLocation:Part Design → Migrate
   Workbenches:[PartDesign](PartDesign_Workbench.md)
   Version:0.17
---

# PartDesign Migrate

## Description

The PartDesign workbench in FreeCAD v0.17 introduces new tools and elements that are not recognized by older FreeCAD versions (0.16 and older). FreeCAD documents created in older versions can still be opened and edited. To benefit from the new features, they must be migrated via the menu PartDesign → Migrate.


<small>(v0.17)</small> 

## Usage

1.  Open a FreeCAD document that was created with FreeCAD {{VersionMinus|0.16}}
2.  Switch to the **<img src="images/Workbench_PartDesign.svg" width=16px> [PartDesign](PartDesign_Workbench.md)** workbench.
3.  Go to the **Part Design** → **Migrate** menu.
4.  If the migration works, a <img alt="" src=images/Std_Part.svg  style="width:24px;"> [Part container](Std_Part.md) will be created which will hold one or more <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Bodies](PartDesign_Body.md), each hosting a chain of features.

## Limitations

-   Before starting the migration process, check if the model was built with automatic refine options enabled (in **Edit → Preferences → Part design → General**), and set your preferences accordingly. This can be easily determined by successively toggling the visibility of the features in the Model tree. If no residual edges are left between features such as Pads and Pockets, the automatic refine options were disabled.
-   If a document to migrate only contains sketches and PartDesign features, the migration process may likely succeed. Some features such as chamfers and fillets may require rebuilding.
-   If the document to migrate has a mixed Part/Part Design/Draft workflow, the conversion will most likely fail or at best produce unexpected results, and will need to be migrated manually.




 {{PartDesign Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Migrate
