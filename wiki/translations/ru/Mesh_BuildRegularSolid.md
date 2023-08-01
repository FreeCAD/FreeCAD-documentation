---
- GuiCommand:
   Name/ru: Правильное геометрическое тело
   Name: Mesh_BuildRegularSolid
   MenuLocation: Полигональные Сетки - Правильное геометрическое тело...
   Workbenches: [Mesh](Mesh_Workbench/ru.md)
---

# Mesh BuildRegularSolid/ru

## Описание

The **Mesh BuildRegularSolid** command creates a regular parametric solid mesh object.

## Применение

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Mesh_BuildRegularSolid.svg" width=16px> [Mesh BuildRegularSolid](Mesh_BuildRegularSolid.md)** button.
    -   Select the **Meshes → <img src="images/Mesh_BuildRegularSolid.svg" width=16px> Regular solid...** option from the menu.
2.  The **Regular Solid** dialog box opens.
3.  First select a mesh object type from the dropdown list:
    -   
        **<img src="images/Mesh_Cube.svg" width=16px> Cube
**
        

    -   
        **<img src="images/Mesh_Cylinder.svg" width=16px> Cylinder
**
        

    -   
        **<img src="images/Mesh_Cone.svg" width=16px> Cone
**
        

    -   
        **<img src="images/Mesh_Sphere.svg" width=16px> Sphere
**
        

    -   
        **<img src="images/Mesh_Ellipsoid.svg" width=16px> Ellipsoid
**
        

    -   
        **<img src="images/Mesh_Torus.svg" width=16px> Torus
**
        
4.  Specify the required settings. The available settings depend on the mesh object type. See [Properties](#Properties.md).
5.  For meshes with curved surfaces: a higher **Sampling** value results in a finer mesh.
6.  Press the {{button|Create}} button to create the mesh object.
7.  Optionally create more mesh objects.
8.  Press the {{button|Close}} button to close the dialog box and finish the command.

## Примечания

-   Mesh objects created with this command are parametric. Whenever they are recomputed, for example after changing one of their parameters, their mesh is reconstructed. This means that manipulating them with commands such as [Mesh RemeshGmsh](Mesh_RemeshGmsh.md), [Mesh Scale](Mesh_Scale.md) etc. usually does not make sense.

## Свойства

Mesh objects created with this command inherit all [Mesh Feature](Mesh_Feature.md) properties. In addition each mesh object type has a number of properties to control its parametric behavior:

### <img alt="" src=images/Mesh_Cube.svg  style="width:32px;"> Куб 

#### Данные


{{TitleProperty|Cube}}

-    **Height|FloatConstraint**: the height of the cube.

-    **Length|FloatConstraint**: the length of the cube.

-    **Width|FloatConstraint**: the width of the cube.

### <img alt="" src=images/Mesh_Cylinder.svg  style="width:32px;"> Цилиндр 

#### Данные 


{{TitleProperty|Основные}}

-    **Closed|Bool**: if set to `False`, the planar ends of the cylinder are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cylinder.

-    **Radius|FloatConstraint**: the radius of the cylinder.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Cone.svg  style="width:32px;"> Конус 

#### Данные 


{{TitleProperty|Основные}}

-    **Closed|Bool**: if set to `False`, the planar end(s) of the cone are left open.

-    **Edge Length|FloatConstraint**: the edge length of the faces in the mesh.

-    **Length|FloatConstraint**: the length of the cone.

-    **Radius 1|FloatConstraint**: the first radius of the cone. Can be {{value|0}}.

-    **Radius 2|FloatConstraint**: the second radius of the cone. Can be {{value|0}}.

-    **Sampling|IntegerConstraint**: the number of faces along the curved surface.

### <img alt="" src=images/Mesh_Sphere.svg  style="width:32px;"> Сфера 

#### Данные 


{{TitleProperty|Основные}}

-    **Radius|FloatConstraint**: the radius of the sphere.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Ellipsoid.svg  style="width:32px;"> Эллипсоид 

#### Данные 


{{TitleProperty|Основные}}

-    **Radius 1|FloatConstraint**: the first radius of the ellipsoid.

-    **Radius 2|FloatConstraint**: the second radius of the ellipsoid.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.

### <img alt="" src=images/Mesh_Torus.svg  style="width:32px;"> Тор 

#### Данные 


{{TitleProperty|Основные}}

-    **Radius 1|FloatConstraint**: the first (main) radius the torus.

-    **Radius 2|FloatConstraint**: the second radius of the torus.

-    **Sampling|IntegerConstraint**: the number of faces along both directions of the curved surface.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh BuildRegularSolid/ru
