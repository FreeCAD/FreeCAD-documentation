---
 GuiCommand:
   Name: Arch Component‏‎‏‎
   Name/ru: Arch Component‏‎‏‎
   Icon: Arch_Component.svg
   MenuLocation: Arch , Вспомогательные , Компонент
   Workbenches: Arch_Workbench/ru
   Shortcut: **C** **M**
   SeeAlso: 
---

# Arch Component/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Создаёт непараметрический [архитектурный](Arch_Workbench/ru.md) компонент из любого объекта [верстака Part](Part_Workbench/ru.md). Это придаёт объекту Part такие же атрибуты и свойства, как и у других архитектурных объектов и позволяет указать, каким образом он должен экспортироваться в IFC с помощью настройки его **Role** свойства.


</div>



## Применение


<div class="mw-translate-fuzzy">

1.  Выделите объект созданный в верстаке [Part](Part_Workbench/ru.md).
2.  Применить инструмент \"Компонент\" можно одним из способов:
    -   Нажатием кнопки **<img src="images/Arch_Component.svg" width=16px>** на панели инструментов.
    -   Используя комбинацию клавиш **C** **M**.
    -   Через пункт **Arch** → **Вспомогательные** → **<img src="images/Arch_Component.svg" width=16px> [Компонент](Arch_Component/ru.md)** основного меню.


</div>

## Properties

The Arch component object is also a base shared by all other Arch objects ([Arch Wall](Arch_Wall.md), [Arch Structure](Arch_Structure.md), etc). Therefore some of its properties and behaviours are common to all Arch objects (except tools that don\'t produce solid objects, like [Arch Section Plane](Arch_SectionPlane.md) or [Arch Axis](Arch_Axis.md)).

### Data


{{TitleProperty|Component}}

-    **Additions|LinkList**: Arch Components have an addition property, that can hold reference to any number of other [Shape](Part_Workbench.md)-based objects. The shape of these additions will be united with the base shape of the component, to produce the final shape. See [Notes](#Notes.md).

-    **Axis|Link**: An optional axis or axis system on which this object should be duplicated.

-    **Base|Link**: Arch Components are always based on a [Shape](Part_Workbench.md)-based base object. Some types of Arch objects will just use the Base shape as is, others (for example [Arch Wall](Arch_Wall.md)) will do some additional operations on it, such as an extrusion. For some types, having a base object is not mandatory ([Arch Structure](Arch_Structure.md)).

-    **Clone Of|Link**: Any Arch Component can be a clone of another Arch Component of the same type (a Wall can only be a clone of another Wall, etc.). The only exception is the generic Arch Component (as produced by this command), that can be clone of any other type (Wall, structure, window, etc). This allows to use a generic Arch Component to override the type of another one.

-    **Hi Res|Link**: Arch Components can use the shape of another object as a higher-resolution version of themselves. For this, both the Hi Res property and the Hi Res display mode must be set. This allows, for example, to make a simple wall, and then model every brick that composes the wall, for example with [Part Box](Part_Box.md). Then, use a compound of those bricks as a high-resolution version of the wall. The shape of the wall is not modified by adding a Hi-Res object. Only its representation in the [3D view](3D_view.md) will change by adopting the representation of the high-resolution version instead of its own.

-    **Horizontal Area|Area**: The area of the projection of this object onto the XY plane (read-only).

-    **Material|Link**: All Arch Components have a Material slot, that can contain either a [Material](Arch_SetMaterial.md) or a [MultiMaterial](Arch_MultiMaterial.md) (not all Arch object type support the use of [MultiMaterials](Arch_MultiMaterial.md)). The DiffuseColor and Transparency properties of the attached material will define the Shape color and transparency of the Arch component. The material will be imported and exported to [IFC](Arch_IFC.md), [OBJ](Arch_OBJ.md) and [DAE](Arch_DAE.md).

-    **Move Base|Bool**: Specifies if moving this object moves its base instead.

-    **Move With Host|Bool**: When a component is embedded inside another (for example a window inside a wall), setting this property to True will make the object move and rotate together when its host object is moved or rotated using [Draft Move](Draft_Move.md) or [Draft Rotate](Draft_Rotate.md).

-    **Perimeter Length|Length**: The perimeter length of the horizontal area (read-only).

-    **Standard Code|String**: An optional standard (OmniClass, etc\...) code for this component.

-    **Subtractions|LinkList**: Arch Components have an subtraction property, that can hold reference to any number of other [Shape](Part_Workbench.md)-based objects. The shape of these objects will be subtracted from the base shape of the component, to produce the final shape. See [Notes](#Notes.md).

-    **Vertical Area|Area**: The area of all vertical faces of this object (read-only).


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**:

-    **Ifc Properties|Map|Hidden**:

-    **Ifc Type|Enumeration**: Each Arch Component, besides the function defined by its type (wall, window, etc), also has a Role property, that can define further which kind of function it performs. For example, an [Arch Structure](Arch_Structure.md) can have a beam or column role. Generic Arch Components (as produced by this command) can have any role available in the whole Arch workbench. The role is what is used to define the type of IFC object to export to when [exporting to IFC](Arch_IFC.md).


{{TitleProperty|IFC Attributes}}

-    **Description|String**: All Arch Components have a Description field, that can contain any text. This is used when [exporting to IFC](Arch_IFC.md).

-    **Global Id|String**:

-    **Object Type|String**:

-    **Predefined Type|Enumeration**:

-    **Tag|Enumeration**: The Tag property is another text field, which can be used to give an additional custom identity to objects.

## Notes

-   The Placement of the Arch Component is applied after the additions and subtractions are done, so these are performed against the base object at its base location. Then the result is moved to the location of the Placement.

-   Objects can be added or removed to/from a Component\'s Additions and Subtractions lists by selecting both the object and the component, and using the [Arch Add](Arch_Add.md) or [Arch Remove](Arch_Remove.md) commands, or from the task panel by double-clicking the Component in the [Tree view](Tree_view.md). The task panel also allows to check which object is currently part of these lists.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Arch Component/ru
