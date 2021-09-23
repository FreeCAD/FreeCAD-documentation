# Mesh Workbench/ru
<div class="mw-translate-fuzzy">





</div>

<img alt="Логотип верстака Mesh" src=images/Workbench_Mesh.svg  style="width:128px;">


{{TOCright}}

## Введение

<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Верстак Mesh](Mesh_Workbench/ru.md) оперирует с [треугольными сетками](https://ru.wikipedia.org/wiki/Полигональная_сетка). Сетки (Meshes) - это особый тип 3D объектов, составленный из треугольных граней, соединенных по ребрам и вершинам.

Многие из 3D приложений, такие, как [sketchup](http://ru.wikipedia.org/wiki/Sketchup), [blender](http://ru.wikipedia.org/wiki/Blender), [maya](http://ru.wikipedia.org/wiki/Autodesk_Maya) или [3d studio max](http://ru.wikipedia.org/wiki/Autodesk_3ds_Max) используют сетки (meshes) в качестве основного типа 3D объекта. Сетки это очень простые объекты, содержащие только вершины (точки), ребра и (треугольные) грани, их очень легко создать, модифицировать, разбивать, растягивать, и можно легко передаваться из одного приложения в другое без потерь в деталях. Кроме того, поскольку сетки определяются очень простыми данными, 3D приложения обычно могут управляться с очень большими их количеством без использования чрезмерных ресурсов. По этим причинам сетки как 3D объекты часто выбирают для приложений, работающих с кино, анимацией и созданием изображений.


<div class="mw-translate-fuzzy">

**Однако Для инженерных применений, сетки обладают очень большим ограничением:** они только создают поверхность, и не содержат информацию о массе, так что они не ведут себя как [твердые тела](Glossary/ru#Solid.md). Это означает что все твердотельные операции, такие как сложение, вычитание, на сетках выполнять всегда труднее. Верстак Mesh полезен для импорта трёхмерных данных в формате сеток, для их анализа, обнаружения ошибок, и в итоге конвертирует их в твёрдые тела для использования в <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [верстаке Part](Part_Workbench/ru.md).


</div>

<img alt="" src=images/Mesh_example.jpg  style="width:500px;">

## Инструменты


<div class="mw-translate-fuzzy">

Модуль полигонального моделирования сейчас обладает очень простым интерфейсом, все его функции сгруппированы в меню **Сетки**.


</div>

-   <img alt="" src=images/Mesh_Import.svg  style="width:32px;"> [Import mesh\...](Mesh_Import.md): Imports a mesh object from a file.

-   <img alt="" src=images/Mesh_Export.svg  style="width:32px;"> [Export mesh\...](Mesh_Export.md): Exports a mesh object to a file.

-   <img alt="" src=images/Mesh_FromPartShape.svg  style="width:32px;"> [Create mesh from shape\...](Mesh_FromPartShape.md): Creates mesh objects from shape objects.

-   <img alt="" src=images/Mesh_RemeshGmsh.svg  style="width:32px;"> [Refinement\...](Mesh_RemeshGmsh.md): Remeshes a mesh object. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

### Анализ

Анализ кривизны, граней и проверка может ли сетка безопасно преобразована в твердое тело

-   [Оценить и отремонтировать сетку\...](Mesh_EvaluateRepair/ru.md): Анализирует и чинит сетку
-   <img alt="" src=images/Mesh_EvaluateFacet.svg  style="width:32px;"> [Информация о поверхности](Mesh_EvaluateFacet/ru.md): Даёт информацию о поверхностях
-   [Данные о кривизне](Mesh_EvaluateCurvature/ru.md): Даёт информацию о кривизне
-   [Проверить прочность сетки](Mesh_EvaluateSolid/ru.md): Проверить, можно ли тело превратить в сетку
-   [Информация о структуре\...](Mesh_BoundingBox/ru.md): Вычисляет границы сетки


</div>

-   <img alt="" src=images/Mesh_VertexCurvature.svg  style="width:32px;"> [Curvature plot](Mesh_VertexCurvature.md): Creates Mesh Curvature objects for mesh objects.

-   <img alt="" src=images/Mesh_HarmonizeNormals.svg  style="width:32px;"> [Harmonize normals](Mesh_HarmonizeNormals.md): Harmonizes the normals of mesh objects.

-   <img alt="" src=images/Mesh_FlipNormals.svg  style="width:32px;"> [Flip normals](Mesh_FlipNormals.md): Flips the normals of mesh objects.

-   <img alt="" src=images/Mesh_FillupHoles.svg  style="width:32px;"> [Fill holes\...](Mesh_FillupHoles.md): Fills holes in mesh objects.

-   <img alt="" src=images/Mesh_FillInteractiveHole.svg  style="width:32px;"> [Close hole](Mesh_FillInteractiveHole.md): Fills selected holes in mesh objects.

-   <img alt="" src=images/Mesh_AddFacet.svg  style="width:32px;"> [Add triangle](Mesh_AddFacet.md): Adds faces along a boundary of an open mesh object.

-   <img alt="" src=images/Mesh_RemoveComponents.svg  style="width:32px;"> [Remove components\...](Mesh_RemoveComponents.md): Removes faces from mesh objects.

-   <img alt="" src=images/Mesh_RemoveCompByHand.svg  style="width:32px;"> [Remove components by hand\...](Mesh_RemoveCompByHand.md): Removes components from mesh objects.

-   <img alt="" src=images/Mesh_Segmentation.svg  style="width:32px;"> [Create mesh segments\...](Mesh_Segmentation.md): Creates separate mesh segments for specified surface types of a mesh object.

-   <img alt="" src=images/Mesh_SegmentationBestFit.svg  style="width:32px;"> [Create mesh segments from best-fit surfaces\...](Mesh_SegmentationBestFit.md): Creates separate mesh segments for specified surface types of a mesh object, and can identify their parameters.

-   <img alt="" src=images/Mesh_Smoothing.svg  style="width:32px;"> [Smooth\...](Mesh_Smoothing.md): Smooths mesh objects.

-   <img alt="" src=images/Mesh_Decimating.svg  style="width:32px;"> [Decimation\...](Mesh_Decimating.md): Reduces the number of faces in mesh objects. <small>(v0.19)</small> 

-   <img alt="" src=images/Mesh_Scale.svg  style="width:32px;"> [Scale\...](Mesh_Scale.md): Scales mesh objects.

-   <img alt="" src=images/Mesh_BuildRegularSolid.svg  style="width:32px;"> [Regular solid\...](Mesh_BuildRegularSolid.md): Creates a regular parametric solid mesh object.


<div class="mw-translate-fuzzy">

### Булевы операции 

-   [Объединение](Mesh_Union/ru.md): объединить сетки
-   [Пересечение](Mesh_Intersection/ru.md): выделить пересечение полигональных сеток
-   [Разность](Mesh_Difference/ru.md): выполнить вычитание (вырезание) из полигональных сеток


</div>


<div class="mw-translate-fuzzy">

### Резание

-   <img alt="" src=images/Mesh_Cut.png  style="width:32px;"> [Обрезать сетку](Mesh_PolyCut/ru.md): Обрезать сетку по линии
-   [Подрезать сетку](Mesh_TrimMesh/ru.md): Подрезать сетку
-   [Подрезать сетку плоскостью](Mesh_TrimMeshWithPlane/ru.md): Подрезать сетку плоскостью
-   [Создание сегментов сетки\...](Mesh_CreateMeshSegment/ru.md): Создание сегментов сетки
-   Создаёт сечение из сетки и плоскости


</div>

-   <img alt="" src=images/Mesh_Merge.svg  style="width:32px;"> [Merge](Mesh_Merge.md): Creates a mesh object by combining the meshes of two or more mesh objects.

-   <img alt="" src=images/Mesh_SplitComponents.svg  style="width:32px;"> [Split by components](Mesh_SplitComponents.md): Splits a mesh object into its components. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatMesh.svg  style="width:32px;"> [Unwrap Mesh](MeshPart_CreateFlatMesh.md): Creates a flat representation of a mesh object. <small>(v0.19)</small> 

-   <img alt="" src=images/MeshPart_CreateFlatFace.svg  style="width:32px;"> [Unwrap Face](MeshPart_CreateFlatFace.md): Creates a flat representation of a face of a shape object. <small>(v0.19)</small> 

## Preferences

There are some [export preferences related to Mesh Formats](Import_Export_Preferences#Mesh_Formats.md) but these are not used by commands belonging to this workbench. They are used by the [Std Export](Std_Export.md) command.

Mesh Workbench preferences can be found in the following categories of the [Preferences Editor](Preferences_Editor.md):

-   <img alt="" src=images/Preferences-display.svg  style="width:32px;"> [Display](Preferences_Editor#Display_settings.md): On the [Mesh view](Preferences_Editor#Mesh_view.md) tab several preferences can be set.
-   <img alt="" src=images/Preferences-openscad.svg  style="width:32px;"> [OpenSCAD](OpenSCAD_Preferences.md): The [Mesh Union](Mesh_Union.md), [Mesh Intersection](Mesh_Intersection.md) and [Mesh Difference](Mesh_Difference.md) commands require [OpenSCAD](http://www.openscad.org/) and use the **OpenSCAD executable** preference to find its executable.


<div class="mw-translate-fuzzy">

## Ссылки


</div>


<div class="mw-translate-fuzzy">

-   [Импорт сеток в FreeCAD](FreeCAD_and_Mesh_Import/ru.md)


</div>


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}} 

[Category:Workbenches](Category:Workbenches.md)

---
[documentation index](../README.md) > Mesh Workbench/ru
