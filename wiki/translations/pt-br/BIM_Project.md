---
 GuiCommand:
   Name: BIM Project
   MenuLocation: 3D/BIM , Project
   Workbenches: BIM_Workbench
   Shortcut: 
   SeeAlso: 
---

# BIM Project/pt-br


</div>



## Descrição


<div lang="en" dir="ltr" class="mw-content-ltr">

The **BIM Project** tool creates a [native IFC](NativeIFC.md) project in the current document. In IFC, a project (IfcProject) is the root object of all the contents of the model. It is mandatory to have one in each IFC file.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

It is not necessary to create a project to export a FreeCAD model to IFC, as a default one will be added each time you export an IFC file. However, when working with [NativeIFC](NativeIFC.md), an IFC file is attached to the model, and all the geometry and properties of that model and its components come from the attached IFC file. The project is where the IFC file is attached to the document.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Typically, you create a BIM project to attach an IFC file. When creating the project, the attached IFC file is blank, and not saved. The next time you will save the FreeCAD file, you will also be asked to save the IFC file.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

If you distribute the FreeCAD file, all attached IFC files must be distributed together, otherwise FreeCAD won\'t be able to extract the geometry. However, if the **shape mode** property of all objects contained in a project is set to **Shape**, then the FreeCAD file can be distributed without the accompanying IFC file, and will still open correctly on other computers. The IFC objects, however, won\'t be editable anymore.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

When inserting an IFC file, a project object is created, that contains all the contents of the file. Like all NativeIFC objects, the project can be expanded by double-clicking it in the tree.


</div>



## Utilização


<div lang="en" dir="ltr" class="mw-content-ltr">

1.  Make sure you have a FreeCAD document open.
2.  Press the **<img src="images/BIM_Project.svg" width=16px> [Project](BIM_Project.md)** button.
3.  Optionally, lock the document by pressing the **<img src="images/IFC.svg" width=16px> [IFC Lock](NativeIFC#Locked_and_unlocked_modes.md)** button.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Locked and unlocked mode 


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

In the [BIM Workbench](BIM_Workbench.md), the status bar features an **<img src="images/IFC.svg" width=16px> [IFC Lock](NativeIFC#Locked_and_unlocked_modes.md)** button that allows to toggle between **locked** and **unlocked** modes. When unlocked, you can have several [projects](BIM_Project.md) inside your FreeCAD document, and also have both IFC and non-IFC elements.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

In locked mode, the data attached to your project object becomes attached directly to the FreeCAD document. The FreeCAD document acts as a faithful replica, or rendering, of the IFC document. The project object is therefore removed. You can have only one project in your FreeCAD document, and you cannot have non-IFC objects anymore (every new object is instantly converted to IFC).


</div>



## Adicionando objetos a um projeto 


<div lang="en" dir="ltr" class="mw-content-ltr">

Objects are added to a project simply by dragging and dropping them onto the project in the tree view. These objects will be converted to IFC and might loose some of their former parametric behaviours when those are not supported by IFC.


</div>



## Diferença


<div lang="en" dir="ltr" class="mw-content-ltr">

When the project contains unsaved changes, a red dot will appear on its tree icon. Right-clicking the project and choosing **IFC → Diff** will open a dialog to see a [diff](https://en.wikipedia.org/wiki/Diff) of what has changed in the attached IFC file. This is a good way to make sure what you changed is really what you intended.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

## Saving


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

IFC files attached to a project are automatically saved each time you save the FreeCAD file. They can also be saved manually anytime by right-clicking the project and choosing **IFC → Save**.


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">





</div>


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [BIM](BIM_Workbench.md) > BIM Project/pt-br
