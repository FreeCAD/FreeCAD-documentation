# Lattice2 Workbench/ru
} <img alt="" src=images/Lattice2_Lattice2.svg  style="width   *240px;"> 
*align=center|Иконка внешнего верстака FreeCAD Lattice2*

## Введение


**Lattice2 застабилизирован. Новые возможности могут быть добавлены, но революционных изменений не ожидается.**


{{TOCright}}


<div class="mw-translate-fuzzy">

Верстак Lattice2 это [внешний верстак](external_workbenches/ru.md) FreeCADа, который служит для работы с размещением и матрицами размещений. Это похоже на верстак сборок, но с упором на массивы. Ограничений и связей нет, здесь только матрицы размещений, которые могут создаваться, комбинироваться, преобразовываться, накладываться и заполняться фигурами.


</div>

Когда-то думали, как создать угломер с помощью FreeCAD? Это задача для данного верстака (включая разметку делений). Разнесённые сборки так же могут быть созданы с помощью этого верстака.

Кроме того, в верстаке есть несколько инструментов общего назначения, таких как параметрическое понижение, ограничивающие рамки, инструмент информации о фигуре и инструменты для работы с наборами фигур (составов).

Одна из главных целей верстака - быть как можно более параметрическим.

## Справки

-   Автор   * DeepSOIC
-   Домашняя страница   * <https   *//github.com/DeepSOIC/Lattice2>
-   Исходный код на github   * <https   *//github.com/DeepSOIC/Lattice2>

## Инструменты

Детальное описание на [Lattice2 Github wiki](https   *//github.com/DeepSOIC/Lattice2/wiki)

### Панель инструментов 

![](images/Lattice2-menu-orizz.png ) 
*Панель инструментов Lattice2*

### Команды

-   <img alt="" src=images/Lattice2_Placement.svg  style="width   *32px;"> [Placement](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * Custom](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * XY plane](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * XZ plane](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * YZ plane](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * along X](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * along Y](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * along Z](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_Placement.svg  style="width   *24px;"> [Single Placement   * Euler angles](Lattice2_Placement/ru.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width   *32px;"> [Placement of shape   * Copy object.Placement](Lattice2_PlacementFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width   *32px;"> [Placement of shape   * Center of bounding box](Lattice2_PlacementFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width   *32px;"> [Placement of shape   * Center of mass](Lattice2_PlacementFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_PlacementFromShape.svg  style="width   *32px;"> [Placement of shape   * Inertial axis system](Lattice2_PlacementFromShape/ru.md)
-   <img alt="" src=images/Lattice2_AttachablePlacement.svg  style="width   *32px;"> [Attachable Placement](Lattice2_AttachablePlacement/ru.md)
-   <img alt="" src=images/Lattice2_LinearArray.svg  style="width   *32px;"> [Generate linear array](Lattice2_LinearArray/ru.md)
-   <img alt="" src=images/Lattice2_PolarArray.svg  style="width   *32px;"> [Generate polar array](Lattice2_PolarArray/ru.md)
-   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width   *32px;"> [Array from shape](Lattice2_ArrayFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width   *32px;"> [Internal placements](Lattice2_ArrayFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width   *32px;"> [Center of bounding box](Lattice2_ArrayFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width   *32px;"> [Center of mass](Lattice2_ArrayFromShape/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFromShape.svg  style="width   *32px;"> [Inertial axis system](Lattice2_ArrayFromShape/ru.md)
-   <img alt="" src=images/Lattice2_InvertLattice.svg  style="width   *32px;"> [Invert lattice](Lattice2_InvertLattice/ru.md)
-   <img alt="" src=images/Lattice2_JoinArrays.svg  style="width   *32px;"> [Join arrays](Lattice2_JoinArrays/ru.md)
-   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width   *32px;"> [Array filter](Lattice2_ArrayFilter/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width   *32px;"> [Selected items](Lattice2_ArrayFilter/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width   *32px;"> [Touching](Lattice2_ArrayFilter/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width   *32px;"> [Within distance window](Lattice2_ArrayFilter/ru.md)
    -   <img alt="" src=images/Lattice2_ArrayFilter.svg  style="width   *32px;"> [Pointing at shape](Lattice2_ArrayFilter/ru.md)
-   <img alt="" src=images/Lattice2_ExplodeArray.svg  style="width   *32px;"> [Explode array](Lattice2_ExplodeArray/ru.md)
-   <img alt="" src=images/Lattice2_ProjectArray.svg  style="width   *32px;"> [Project array](Lattice2_ProjectArray/ru.md)
-   <img alt="" src=images/Lattice2_ResampleArray.svg  style="width   *32px;"> [Resample array](Lattice2_ResampleArray/ru.md)
-   <img alt="" src=images/Lattice2_PopulateCopiesNormal.svg  style="width   *32px;"> [Populate with copies](Lattice2_PopulateCopiesNormal/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesNormal.svg  style="width   *32px;"> [Populate with copies](Lattice2_PopulateCopiesNormal/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesArray.svg  style="width   *32px;"> [Populate with copies   * Build array](Lattice2_PopulateCopiesArray/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateCopiesMove.svg  style="width   *32px;"> [Moved object](Lattice2_PopulateCopiesMove/ru.md)
-   <img alt="" src=images/Lattice2_PopulateChildrenNormal.svg  style="width   *32px;"> [Populate with children](Lattice2_PopulateChildrenNormal/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenNormal.svg  style="width   *32px;"> [Populate with children](Lattice2_PopulateChildrenNormal/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenArray.svg  style="width   *32px;"> [Populate with children   * Build array](Lattice2_PopulateChildrenArray/ru.md)
    -   <img alt="" src=images/Lattice2_PopulateChildrenMove.svg  style="width   *32px;"> [Moved children](Lattice2_PopulateChildrenMove/ru.md)
-   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Parametric downgrade](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to ](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Leaves](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to CompSolids](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Shells](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to OpenWires](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Faces](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Wires](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Edges](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Seam edges](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Non-seam edges](Lattice2_ParametricDowngrade/ru.md)
    -   <img alt="" src=images/Lattice2_ParametricDowngrade.svg  style="width   *24px;"> [Downgrade to Vertices](Lattice2_ParametricDowngrade/ru.md)
-   <img alt="" src=images/Lattice2_SubLink.svg  style="width   *32px;"> [Sub link](Lattice2_SubLink/ru.md)
-   <img alt="" src=images/Lattice2_MakeCompound.svg  style="width   *32px;"> [Make compound](Lattice2_MakeCompound/ru.md)
-   <img alt="" src=images/Lattice2_ExplodeCompound.svg  style="width   *32px;"> [Explode compound](Lattice2_ExplodeCompound/ru.md)
-   <img alt="" src=images/Lattice2_FuseCompound.svg  style="width   *32px;"> [Fuse compound](Lattice2_FuseCompound/ru.md)
-   <img alt="" src=images/Lattice2_BoundingBox.svg  style="width   *32px;"> [Bounding box](Lattice2_BoundingBox/ru.md)
    -   <img alt="" src=images/Lattice2_BoundingBox.svg  style="width   *32px;"> [Whole](Lattice2_BoundingBox/ru.md)
    -   <img alt="" src=images/Lattice2_BoundingBoxCompound.svg  style="width   *32px;"> [Children](Lattice2_BoundingBoxCompound/ru.md)
-   <img alt="" src=images/Lattice2_ShapeString.svg  style="width   *32px;"> [Shape string for array](Lattice2_ShapeString/ru.md)
-   <img alt="" src=images/Lattice2_ParaSeries.svg  style="width   *32px;"> [Para series](Lattice2_ParaSeries/ru.md)
-   <img alt="" src=images/Lattice2_Inspect.svg  style="width   *32px;"> [Inspect](Lattice2_Inspect/ru.md)
    -   <img alt="" src=images/Lattice2_InspectSelection.svg  style="width   *32px;"> [Inspect seletion](Lattice2_InspectSelection/ru.md)
    -   <img alt="" src=images/Lattice2_InspectShape.svg  style="width   *32px;"> [Shape info (feature)](Lattice2_InspectShape/ru.md)
-   <img alt="" src=images/Lattice2_SubstituteObject.svg  style="width   *32px;"> [Substitute object](Lattice2_SubstituteObject/ru.md)
-   Expose links to subelements

Other

-   Recomputes
    -   <img alt="" src=images/Lattice2_RecomputeMakeFeature.svg  style="width   *32px;"> [Make recompute locher object](Lattice2_RecomputeMakeFeature/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeLock.svg  style="width   *32px;"> [Lock recomputes](Lattice2_RecomputeLock/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeUnlock.svg  style="width   *32px;"> [Unlock recomputes](Lattice2_RecomputeUnlock/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeFeature.svg  style="width   *32px;"> [Recompute feature](Lattice2_RecomputeFeature/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeDocument.svg  style="width   *32px;"> [Recompute document](Lattice2_RecomputeDocument/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeForce.svg  style="width   *32px;"> [Force recompute](Lattice2_RecomputeForce/ru.md)   *
    -   <img alt="" src=images/Lattice2_RecomputeTouch.svg  style="width   *32px;"> [Touch selected feature](Lattice2_RecomputeTouch/ru.md)   *
-   <img alt="" src=images/Lattice2_Lattice2.svg  style="width   *32px;"> Lattice2 Workbench icon

## Установка

**Prerequisites** Lattice2 Workbench requires FreeCAD \>= v0.16.5155.

### Автоматическая установка 


<div class="mw-translate-fuzzy">

Начиная с v0.17 можно использовать для установки <img alt="" src=images/Lattice2_Lattice2.svg  style="width   *24px;"> верстака Lattice2 <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon Manager](Std_AddonMgr/ru.md). Используйте {MenuCommand\|инструменты → Addon Manager}}


</div>

### Ручная установка 

-   Scroll to the top of the page, and click \'download zip\' button
-   Unpack the contents into a \"Lattice2\" folder created in \\Path\\to\\FreeCAD\\Mod, and restart FreeCAD.
-   Note that InitGui.py (and the rest of .py files) should end up directly under Mod\\Lattice2 (not under nested directory like Mod\\Lattice2\\Lattice2).

After you install the workbench, it should appear at the bottom of list of workbench selector in FreeCAD.

## Учебники

-   Tutorials   * [Gallery](https   *//github.com/DeepSOIC/Lattice2/wiki/Gallery)
-   [Basic Tutorial](https   *//github.com/DeepSOIC/Lattice2/wiki/Basic-Tutorial)
-   [Lattice2 in PartDesign](https   *//github.com/DeepSOIC/Lattice2/wiki/PartDesign-Pattern-Tutorial)
-   [Making a Cogset](https   *//github.com/DeepSOIC/Lattice2/wiki/Cogset-Tutorial)
-   [Feature Patterns in Lattice2 Workbench](https   *//www.youtube.com/watch?v=BXmeEGnhszo) by \@sliptonic

## Links to Lattice2 WB 

-   Lattice2 Wiki   * <https   *//github.com/DeepSOIC/Lattice2/wiki>
-   FreeCAD Wiki   * <https   *//www.freecadweb.org/wiki/Lattice2_Workbench>
-   FreeCAD Forum   * [Lattice workbench - v2.0 is becoming stable](http   *//forum.freecadweb.org/viewtopic.php?t=12464)
-   Gallery   * <https   *//github.com/DeepSOIC/Lattice2/wiki/Gallery>
-   Report bugs   * Please report bugs at <https   *//github.com/DeepSOIC/Lattice2/issues>

## Other useful links 


<div class="mw-translate-fuzzy">

-   [Lattice aka Lattice1 Workbench (obsolete)](https   *//github.com/DeepSOIC/Lattice)
-   [Внешние верстаки](External_Workbenches/ru.md)   * Список верстаков FreeCAD.
-   [Рецепты макросов](Macros_recipes/ru.md)
-   [Портал сообщества FreeCAD](FreeCAD_Community_Portal/ru.md)


</div>




[Category   *Addons](Category_Addons.md) [Category   *External Workbenches](Category_External_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Lattice2 Workbench/ru
