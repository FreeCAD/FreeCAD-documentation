# App GeoFeature

 

## Introduction

 <img alt="" src=images/Feature.svg  style="width:32px;"> 

An [App GeoFeature](App_GeoFeature.md) object, or formally an `App::GeoFeature`, is the base class of most objects that will display geometrical elements in the [3D view](3D_view.md) because it includes the **Placement** property.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::GeoFeature* class is the base class of essentially all objects in the software that will display geometry in the [3D view](3D_view.md).`

## Usage

The [App GeoFeature](App_GeoFeature.md) is an internal object, so it cannot be created from the graphical interface. It is generally not meant to be used directly, rather it can be sub-classed to get a bare-bones object that only has a basic **Placement** property to define its position in the [3D view](3D_view.md).

Some of the most important derived objects are the following:

-   The [Part Feature](Part_Feature.md) class, the parent of most objects with 2D and 3D [topological shapes](Part_TopoShape.md).
-   The [Mesh Feature](Mesh_Feature.md) class, the parent of most objects made from [meshes](Mesh_MeshObject.md), not solids.
-   The [Fem FemMeshObject](FEM_Mesh.md) class, the parent of finite element meshes created with the [FEM Workbench](FEM_Workbench.md).
-   The [Path Feature](Path_Feature.md) class, the parent of paths created with the [Path Workbench](Path_Workbench.md) for use in CNC machining.
-   The [App Part](App_Part.md) class, which defines [Std Parts](Std_Part.md) that can be used as containers of bodies to perform assemblies.

When creating this object in [Python](Python.md), instead of sub-classing `App::GeoFeature`, you should sub-class `App::GeometryPython` because the latter includes a default view provider, and `Proxy` attributes for the object itself, and its view provider. See [Scripting](App_GeoFeature#Scripting.md).

## Properties

An [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares all the latter\'s properties.

In addition to the properties described in [App DocumentObject](App_DocumentObject.md), the GeoFeature has the **Placement** property, which controls its position in the [3D view](3D_view.md).

See [Property](Property.md) for all property types that scripted objects can have.

These are the properties available in the [property editor](property_editor.md). Hidden properties can be shown by using the **Show all** command in the context menu of the [property editor](property_editor.md).

### Data


{{TitleProperty|Base}}

-    **Placement|Placement**: the position of the object in the [3D view](3D_view.md). The placement is defined by a `Base` point (vector), and a `Rotation` (axis and angle). See [Placement](Placement.md).

    -   
        **Angle**
        
        : the angle of rotation around the **Axis**. By default, it is {{value|0°}} (zero degrees).

    -   
        **Axis**
        
        : the unit vector that defines the axis of rotation for the placement. Each component is a floating point value between {{value|0}} and {{value|1}}. If any value is above {{value|1}}, the vector is normalized so that the magnitude of the vector is {{value|1}}. By default, it is the positive Z axis, {{value|(0, 0, 1)}}.

    -   
        **Position**
        
        : a vector with the 3D coordinates of the base point. By default, it is the origin {{value|(0, 0, 0)}}.

-    **Label|String**: the user editable name of this object, it is an arbitrary UTF8 string.

#### Hidden properties Data 

-    **Proxy|PythonObject|Hidden**: a custom class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](App_GeoFeature#Scripting.md).

-    **Label2|String|Hidden**: a longer, user editable description of this object, it is an arbitrary UTF8 string that may include newlines. By default, it is an empty string {{value|""}}.

-    **Expression Engine|ExpressionEngine|Hidden**: a list of expressions. By default, it is empty {{value|[]}}.

-    **Visibility|Bool|Hidden**: whether to display the object or not.

### View


{{TitleProperty|Base}}

-    **Proxy|PythonObject|Hidden**: a custom view provider class associated with this object. This only exists for the [Python](Python.md) version. See [Scripting](App_GeoFeature#Scripting.md).


{{TitleProperty|Display Options}}

-    **Bounding Box|Bool**: if it is `True`, the object will show the bounding box in the [3D view](3D_view.md).

-    **Display Mode|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Show In Tree|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Visibility|Bool**: see the information in [App FeaturePython](App_FeaturePython.md).


{{TitleProperty|Object Style}}

-    **Shape Color|Color**: a tuple of three floating point RGB values  light gray .

-    **Shape Material|Material|Hidden**: an [App Material](App_Material.md) associated with this object. By default it is empty.

-    **Transparency|Percent**: an integer from {{value|0}} to {{value|100}} that determines the level of transparency of the faces in the [3D view](3D_view.md). A value of {{value|100}} indicates completely invisible faces; the faces are invisible but they can still be picked as long as **Selectable** is `True`.


{{TitleProperty|Selection}}

-    **On Top When Selected|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

-    **Selectable|Bool**: if it is `True`, the object can be picked with the pointer in the [3D view](3D_view.md). Otherwise, the object cannot be selected until this option is set to `True`.

-    **Selection Style|Enumeration**: see the information in [App FeaturePython](App_FeaturePython.md).

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md), and [scripted objects](scripted_objects.md).

See [Part Feature](Part_Feature.md) for the general information on adding objects to the program

A GeoFeature is created with the `addObject()` method of the document. If you would like to create an object with a 2D or 3D [topological shape](Part_TopoShape.md), it may be better to create one of the sub-classes specialized for handling shapes, for example, [Part Feature](Part_Feature.md) or [Part Part2DObject](Part_Part2DObject.md).

 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeoFeature", "Name")
obj.Label = "Custom label"
```

This basic `App::GeoFeature` doesn\'t have a default view provider, so no icon will be displayed on the [tree view](tree_view.md), and no **View** properties will be available.

Therefore, for [Python](Python.md) subclassing, you should create the `App::GeometryPython` object.

 
```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::GeometryPython", "Name")
obj.Label = "Custom label"
```

For example, the [Arch BuildingPart](Arch_BuildingPart.md) element of the [Arch Workbench](Arch_Workbench.md) is an `App::GeometryPython` object with a custom icon.

 {{Document objects navi}} 
