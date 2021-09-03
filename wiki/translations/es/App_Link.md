 {{TOCright}}

## Introducción

<img alt="" src=images/Link.svg  style="width:32px;">

Un [Enlace de aplicación](App_Link/es.md), o formalmente un `App::Link`, es un tipo de objeto que hace referencia o enlace a otro objeto, en el mismo documento, o en otro documento. Está especialmente diseñado para duplicar eficientemente un único objeto varias veces, lo que ayuda a la creación de [ensamblajes](assembly/es.md) complejos a partir de subensamblajes más pequeños, y de múltiples componentes reutilizables como tornillos, tuercas y elementos de fijación similares.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Simplified diagram of the relationships between the core objects in the program. The `App::Link* object is a core component of the system, it does not depend on any workbench, but it can be used with most objects created in all workbenches.`

## Utilización

1.  Select an object in the [tree view](tree_view.md) or [3D view](3D_view.md) for which you wish to create a Link.
2.  Press the **<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)** button. The produced object has the same icon as the original object, but has an arrow overlay indicating it is a Link.

See the [Std LinkMake](Std_LinkMake.md) page for the complete information, including its use in [Scripting](Std_LinkMake#Scripting.md).

## Propiedades

An [App Link](App_Link.md) (`App::Link` class) is derived from the basic [App DocumentObject](App_DocumentObject.md) (`App::DocumentObject` class), therefore it shares most of the latter\'s properties.

See the full list of properties in the [Std LinkMake](Std_LinkMake.md) page.


{{Std Base

}} {{Document objects navi}} 
