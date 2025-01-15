---
 GuiCommand:
   Name: BIM ProjectManager
   MenuLocation: Manage , Manage project...
   Workbenches: BIM_Workbench
---

# BIM ProjectManager

## Description

The **BIM Project Setup** dialog allows you to create a basic set of guide objects in the current document or in a new document, that will help you to start modeling a BIM project.

 <img alt="" src=images/BIM_project_screenshot.png  style="width:600px;">  
*BIM Project Setup*

## Usage

The project setup dialog can create:

-   A new [document](Document_structure.md). Alternatively, the other objects will be created in the currently opened document.
-   A [site](Arch_Site.md). The Site object represents a piece of terrain, where your project will be located. You can give it a number of useful properties, such as street address and earth coordinates. Upon creation, the site is just an empty container for other BIM objects, but a 3D object representing the actual terrain can be attached to it later on.
-   A [building](Arch_Building.md). The Building object is a container for all the BIM objects that will belong to a same building. You can define a building type, and give it gross rectangular dimensions, that will be represented as a rectangle drawn on the ground (X,Y) plane.
-   A set of [axes](Arch_Axis.md), by defining their number and spacing. Axes are used as guidelines to align 2D and 3D objects. These axes can be modified or new axes introduced later on.
-   A set of [BuildingParts](Arch_BuildingPart.md) to represent levels. BuildingParts are generic BIM container objects that can be used to group other BIM objects in a number of meaningful ways, such as repeatable components or building levels.
-   A set of default [groups](Std_Group.md) inside each level. Groups can be used to organize your BIM objects in clearer categories, such as \"Walls\" or \"Columns\". They have no impact on the model itself, but often help to make your model structure clearer when it contains a lot of objects.

## Templates

The Project tool supports two kinds of templates:

-   Once you have filled the different options, the contents of the BIM project setup wizard can be **saved** as a template. These templates can be **restored** and adapted at a later time. Project templates are stored as plain text files in your FreeCAD user folder.
-   Alternatively, you can also save the contents of the current document as a template. This will save the currently opened document as a standard **.FCStd** file, but also include additional BIM settings like the current working plane, or current units. By using the **restore** option anytime, the contents of that template file will be merged into the active document and all settings found in it applied.



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM ProjectManager
