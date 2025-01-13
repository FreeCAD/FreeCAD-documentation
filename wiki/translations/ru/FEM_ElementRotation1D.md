---
 GuiCommand:
   Name: FEM ElementRotation1D
   Name/ru: FEM ElementRotation1D
   Icon: Fem-beam-rotation.svg
   MenuLocation:  Model , Element Geometry , Beam rotation
   Workbenches: FEM_Workbench/ru
   SeeAlso: FEM_tutorial/ru
---

# FEM ElementRotation1D/ru


</div>



## Описание

**ElementRotation1D** применяется для поворота профиля балки вокруг оси элементов балки.



## Применение


<div class="mw-translate-fuzzy">

1.  Существует несколько способов вызова команды
    -   Нажмите **<img src="images/FEM_ElementRotation1D.svg" width=16px> [FEM ElementRotation1D](FEM_ElementRotation1D/ru.md)** button.
    -   Выберите в меню опцию **Model → Element Geometry → <img src="images/FEM_ElementRotation1D.svg" width=16px> Beam rotation**.
2.  Укажите угол, на который должен быть повернут профиль балки.


</div>



## Свойства


**Rotation**

: specifies the angle of rotation.



## Ограничения

-   Currently, multiple rotations are not supported (a single rotation is applied to all beams in the model).



## Примечания

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.
-   This feature uses the [\*BEAM SECTION card in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/ru
