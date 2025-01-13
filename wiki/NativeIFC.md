# NativeIFC
**Warning**: The NativeIFC functionality is still a work-in-progress and is not finished. Please bear that in mind when using and not rely on it until you are confident it can do what you intend. See the [development roadmap](https://github.com/yorikvanhavre/FreeCAD-NativeIFC/blob/main/doc/roadmap2024.md) to read more about the development, what\'s working and what\'s planned.

## Introduction

Starting from version 1.0, FreeCAD uses the [Native IFC concept](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). It allows FreeCAD users to open, manipulate and create IFC files natively in FreeCAD.

Although FreeCAD already supported opening and saving IFC files through the Arch workbench for a long time, it did so, like most other BIM applications, by translating back and forth between the IFC file format and FreeCAD\'s internal data model. This means two translations, one when opening and another one when saving, which cause data loss, and a complete rewrite of the file each time. This turns it unsuitable for [version control systems](https://en.wikipedia.org/wiki/Version_control) like [Git](https://en.wikipedia.org/wiki/Git), and very hard to locate changes.

Native IFC means that the IFC file is itself the data structure in FreeCAD. When opening an IFC file in FreeCAD, what you see on the screen is a direct rendering of the contents of the IFC file. Anything you modify will directly modify the IFC file. If you open a file, modify one element and save the file, the only thing that will have changed in the file is the line concerning that element. The rest of the file will be 100% identical to how it was before you saved. No data loss, and very identifiable changes.

The Native IFC idea itself comes from [this paper by Bruno Postle](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst). It is heavily inspired by [BlenderBIM](https://blenderbim.org/) and tries as much as possible to use the same concepts and reuse the code. The final goal is to offer in FreeCAD the same level of functionality and performance found in BlenderBIM, and to upstream as much as possible to [IfcOpenShell](https://ifcopenshell.org/), the common IFC engine used by both applications. It started as a [separate project by Yorik](https://github.com/yorikvanhavre/FreeCAD-NativeIFC)

Working with native IFC files in FreeCAD is simple: Open an existing IFC file or create a new project using the [Project tool](BIM_Project.md) from the [BIM Workbench](BIM_Workbench.md). Create new objects with any of the FreeCAD workbenches or tools. Add these objects to your IFC project by dragging them into the project structure. Save the file, and you are done.

Read below for more details.

## Locked and unlocked modes 

The [BIM Workbench](BIM_Workbench.md) offers two modes to work with IFC files. Switching between the two modes is done by clicking the **lock button** on the FreeCAD status bar:

![](images/BIM-statusbar-lock.jpg )

-   **Unlocked mode** (default): You can have both Native IFC projects and non-IFC elements in a same FreeCAD document. You can also work on BIM models without creating any Native IFC project, and still export your model as IFC.
-   **Locked mode**: Your FreeCAD document is an IFC file. Anything you do will cause changes in the IFC file. Any new object you add is instantly converted to IFC.

In locked mode, all the objects you create are immediately converted to IFC, and might therefore loose some of their original properties and some of their parametric behavior when these are not supported by the IFC format. This mode is more restrictive, which is a disadvantage at some points in project development, but becomes an advantage when data integrity and reliability become essential.

It is also possible to create native IFC projects inside an unlocked document. In that case, strict IFC elements coexist with non-IFC elements in your FreeCAD document. Objects within an IFC project are linked to its attached IFC file. Working with IFC projects is often not needed at early stages of a project, but if you work with others and use IFC files as your main communication medium, using native IFC projects can become an advantage, as the changes in each version of the file are much smaller.

You can always export your model to IFC whenever needed, using IFC projects or not. The difference is that when you are using an IFC project, very minimal changes are written to the IFC file. When not, the whole file is rewritten at each export. This might or might not be an issue for you

The general idea is to work in unlocked mode when working on your own projects, so you can have both IFC and non-IFC elements in your documents, and use the locked mode when working on other people\'s IFC files, so you can keep strict control over what you are changing in those files.

## File concepts 

When working with native IFC files in FreeCAD, an IFC project (being locked or unlocked) always has an IFC file attached to it. That IFC file contains all the data of your IFC project inside FreeCAD and is also responsible for providing the geometry of its objects to FreeCAD.

When creating a new IFC project, there is no IFC file yet, the first time you save the file FreeCAD will ask you where to save the IFC file.

In locked mode, you work directly in an IFC file. There is no more FreeCAD file.

In unlocked mode, you have IFC project objects attached to IFC files, and the FreeCAD document is dependent on these IFC files. If you wish to transmit your FreeCAD file to someone else, you need to given them the IFC files too. Alternatively, you can also set the Shape mode of all the objects to \"Shape\" (see below). This will make the FreeCAD file retain the shape of all the IFC objects, and render them correctly even without the attached IFC file. However, the IFC objects inside will no longer be editable.

## IFC objects vs BIM objects 

When a BIM object or any other FreeCAD object is bound to a Native IFC [project](BIM_Project.md), it becomes an IFC object. Binding an object to a Native IFC project is done simply by dragging, in the tree view, the object onto the project or onto any object that is already part of that project, for example a building or a storey.

Once an object has become an IFC object, it is entirely controlled by the IFC data. It looses its former FreeCAD parametric object, and might loose any parametric properties and features that are not supported by the IFC format. The aim here is in the future to render all this seamless and keep the same editing possibilities for both IFC and non-IFC objects.

## Opening and importing IFC files 

You have two options: open or import.

-   If you open, a new document will be created and you will automatically be in **locked mode**
-   If you import, a native IFC [project](BIM_Project.md) object will be added to the current document, but you can still create non-IFC objects outside that project. You will still be in **unlocked mode**

To open an IFC file, use menu File -\> Open and select an IFC file. To import an IFC file, use menu File -\> Import and select an IFC file.

To maximize initial import speed, opening or importing IFC files will by default render only the top-level object (usually a Site) in FreeCAD. To expand the contents of this object, you need to double-click it in the tree view (see below).

Importing or opening an IFC file does not require the setting of any option. However, some defaults can be tweaked under menu Edit -\> Preferences -\> BIM -\> NativeIFC.

## Creating a new IFC document 

You can choose to work in locked or unlocked mode, depending mostly if you need to have non-IFC objects in your FreeCAD document (unlocked) or wish that everything you do in the document happens in the IFC file (locked).

When creating a new IFC project, there is no attached IFC file yet. On first save, FreeCAD will ask you for a location to save an IFC file.

**In locked mode:**

1.  Create a new FreeCAD document with menu File -\> New
2.  Press the <img alt="" src=images/IFC.svg  style="width:24px;"> [IFC Lock](BIM_ToggleNativeIFC.md) button on the status bar to lock the document

**In unlocked mode:**

1.  Press the <img alt="" src=images/BIM_Project.svg  style="width:24px;"> [Project](BIM_Project.md) button to create a native IFC project in the current FreeCAD document. You can have more than one in a same FreeCAD document

## Saving and exporting IFC files 

You can always export any FreeCAD model to IFC, even if it was not built with BIM tools or contains non-BIM elements. The non-BIM objects will simply be exported as generic IfcBuildingElementProxy entities, while BIM objects can have their class (IfcWall, IfcDoor,\...) defined.

NativeIFC projects, be it in locked or unlocked mode, always have an attached IFC file. There is no need to export anything anymore, you just need to save that IFC file. The way you save IFC contents differs depending on the mode:

-   When working in **locked mode**, all of what happens in your FreeCAD document is saved to the IFC file. There is no need to save the FreeCAD file anymore, and the menu entries *File -\> Save* and *File -\> Save As* are replaced with *File -\> Save IFC* and *File -\> Save IFC As*. Saving the IFC file is all that\'s needed, there is no more .FCStd file.

-   When working in **unlocked mode**, each IFC [project](BIM_Project.md) object in your document will be attached to a separate IFC file. A project object keeps track of changes and its icon will show a red dot when it contains unsaved changes. Saving your FreeCAD document will also save all the IFC files attached to IFC projects found in the document.

In unlocked mode, you can also save attached files manually by right-clicking the project and choosing IFC -\> Save

## Expanding file contents 

When opening an IFC file, only the top-level objects (usually the Site and Building) are rendered in FreeCAD by default (this can be changed under menu Edit -\> Preferences -\> BIM -\> NativeIFC), and additional data such as materials, geometric properties, shape, layers, and child objects are not rendered.

To load all the additional data and show the direct children of an object, double-click it in the tree view.

You can also collapse expanded objects by right-clicking them in the tree and selecting IFC -\> collapse children.

## Loading and unloading shapes 

By default, to gain speed, IFC objects don\'t load their full shape. Only a lightweight 3D representation is shown in the 3D view. This warrants fast import and expand operations. However complex geometric operations such as boolean operations or sections performed by [section planes](Arch_SectionPlane.md) require the full shape to be present. In these cases, you might need to load the shape of the objects you need to perform these operations on.

To load the shape of selected objects, simply set their **Shape Mode** property to **Shape**.

To unload the shape and revert to the lightweight 3D representation mode, set the **Shape Mode** property to **Coin**. (Coin is the name of the 3D rendering library used in FreeCAD).

A third shape mode exists, **None**, that switch off completely the visual representation of the IFC objects. These are then solely controlled via the tree view.

## Classes, attributes and properties 

All IFC objects always have at least two properties: **Class** and **Step ID**. The class is the IFC class (IfcWall, IfcWindow, etc\...) and the Step ID is the ID of the element in the IFC file. The Step ID is actually the sole data needed to locate the object in the IFC file. You can change the class of an object anytime, it won\'t have any impact over the geometry or property sets but might change available attributes (see below). You can only change to a sibling class, a parent class or a descendant class. If you want to change to a class that is very distant from the current class, you will need to know the IFC class structure and repeat the operation several times.

**Attributes** are additional hard-coded properties of IFC objects, such as Name, Description or ID. Attributes depend on the class. For example, IfcWindows also have Length and Width, IfcSites have Longitude and Latitude, etc. Attributes are always grouped under the **IFC** group and are always loaded together with an object.

When changing the class of an object, the attributes might change. You can edit the value of attributes, but you cannot add or remove attributes, as those are mandatory and defined by the IFC standard.

IFC **properties**, which are grouped under property sets, are custom properties that can be attributed to any IFC object. They are not loaded by default, but get loaded when you double-click an object. The property sets, which are property packs that get attached to objects, get rendered as property groups inside the FreeCAD properties tree.

## Layers and Materials 

**Layers** get loaded when double-clicking an object. Layers get represented as [normal FreeCAD layers](Draft_Layer.md), but they are hosted inside the IFC project. When using the [BIM Layers](BIM_Layers.md) tool, an additional icon indicates if the layer is part of an IFC project or not.

**Materials** follow the same logic. They are only loaded when double-clicking the object, they are represented as normal [materials](Arch_Material.md), but get hosted inside the IFC project.

## Building structure 

By the IFC standards, all IFC files must contain one and only one IfcProject (or IfcProjectLibrary) object, which constitutes the root of your IFC model. All other IFC objects can be freely aggregated under this root object (an idea we call a \"flat file\"), but the IFC standards require to have at least one building container object (IfcSite, IfcBuilding or IfcBuildingStorey) under the root IfcProject. In FreeCAD, with the default options set, exported IFC files will always contain the IfcProject and at least one building container (default ones will be created if you don\'t have one).

Although it is not mandatory, it is common practice in IFC files to always have a same basic structure:

IfcProject

  -> IfcSite
     -> IfcBuilding
        -> IfcBuildingStorey

You can also use [groups](Std_Group.md) inside your IFC projects. However, the IFC standard does not allow to nest groups inside a building structure. So these groups will be converted to IfcAssemblies. However, since most BIM applications will happily work with nested groups, you can turn off this conversion in IFC export preferences.

## Check for changes in an IFC project 

One of the main advantages of the native IFC system, is that only the things you change in FreeCAD get reflected in the IFC file attached to a project. As a result, that IFC file contains only very few changes, as opposed to traditional BIM applications where the IFC file is completely rewritten at each export.

This allows to precisely locate the changes inside the file. Moving a wall, for example, changes only one line: The placement of that wall. This in turn allows version control systems like Git to precisely identify those changes, and only save the increments of each new version.

You can get a visual representation (diff) of the changes in a selected IFC project by using menu Utils -\> IFC Diff or, in unlocked mode, right-clicking an IFC project and selecting IFC -\> Diff.

## Adding, deleting and modifying objects 

In locked mode, any new object added (BIM or not) gets immediately converted to IFC. There is nothing more to do.

In unlocked mode, any new object (BIM or not) added to the document needs to added to an IFC project. This is done by dragging the object in the tree view and dropping anywhere inside the structure of an IFC project.

Deleting objects that are inside an IFC project will delete them from the IFC file as well.

Once an object becomes an IFC object, it looses its former FreeCAD parametric abilities and inherits all its behaviour from the IFC file. As of FreeCAD 1.0, the editing possibilities of IFC objects are still limited, and are done entirely via properties (no graphical edit available yet). To edit an object, you must have loaded its geometry properties. This is done either by double-clicking it or right-clicking and choosing *IFC -\> add geometric properties* in the tree view.

Editable geometric properties such as \"Height\" or \"Width\" are then added to the object. This is a work in progress, not all properties are supported yet. Changing the value of these properties will change the shape of the object.




 {{BIM_Tools_navi}}



---
⏵ [documentation index](../README.md) > NativeIFC
