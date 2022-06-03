---
- GuiCommand   */ru
   Name/ru   *График кривизны
   Name   *Mesh_VertexCurvature
   MenuLocation   *Полигональные Сетки → График кривизны
   Workbenches   *[Mesh](Mesh_Workbench/ru.md)
   SeeAlso   *[Mesh CurvatureInfo](Mesh_CurvatureInfo/ru.md)
---

# Mesh VertexCurvature/ru


</div>

## Описание

The **Mesh VertexCurvature** command creates Mesh Curvature objects for mesh objects. A curvature object displays the curvature of a mesh using different colors for the convex, flat and concave parts.

![](images/Mesh_VertexCurvature_example.png ) 
*Example of a Mesh Curvature object*

## Применение

1.  Select one or more mesh objects.
2.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Mesh_VertexCurvature.svg" width=16px> [Mesh VertexCurvature](Mesh_VertexCurvature.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_VertexCurvature.svg" width=16px> Curvature plot** option from the menu.
    -   Select the **<img src="images/Mesh_VertexCurvature.svg" width=16px> Curvature plot** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu.

## Свойства

For a Mesh Curvature object the following properties are available in the [Property editor](Property_editor.md). Select the **Show all** option from the Property editor context menu to display the hidden properties.

### Данные


{{TitleProperty|Основные}}

-    **Label|String**   * a user editable name for the object, an arbitrary UTF8 string.

-    **Source|Link**   * a link to the mesh object.

#### Данные скрытые свойства 


{{TitleProperty|Основные}}

-    **Curv Info|CurvatureList**   * a list of curvature information.

-    **Expression Engine|ExpressionEngine**   * a list of expressions.

-    **Label2|String**   * a user editable description for the object, an arbitrary UTF8 string that may include newlines.

-    **Visibility|Bool**   * if set to `True`, the object appears in the [3D view](3D_view.md).

### Вид


{{TitleProperty|Основные}}

-    **Display Mode|Enumeration**   * {{value|Absolute curvature}} (default), {{value|Mean curvature}}, {{value|Gaussian curvature}}, {{value|Maximum curvature}}, {{value|Minimum curvature}}.

-    **On Top When Selected|Enumeration**   * {{value|Disabled}} (default), {{value|Enabled}}, {{value|Object}}, {{value|Element}}.

-    **Selection Style|Enumeration**   * {{value|Shape}}, {{value|BoundBox}} (default).

-    **Show In Tree|Bool**   * if set to `True`, the object appears in the [Tree view](Tree_view.md).

-    **Visibility|Bool**   * if set to `True`, the object appears in the [3D view](3D_view.md).

#### Вид скрытые свойства 


{{TitleProperty|Основные}}

-    **Texture Material|Material**   * an [App Material](App_Material.md) associated with the object.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh VertexCurvature/ru
