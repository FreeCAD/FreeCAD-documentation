# FEM Workbench/ru
<div class="mw-translate-fuzzy">





</div>

<img alt="Логотип верстака FEM" src=images/Workbench_FEM.svg  style="width:128px;">


{{TOCright}}



## Введение

[Верстак FEM](FEM_Workbench/ru.md) предоставляет современный набор инструментов для анализа [Методом Конечных Элементов](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D1%8B%D1%85_%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2) (finite element analysis, FEA) в FreeCAD. В основном это означает, что все инструменты для проведения анализа объединены в один графический интерфейс пользователя (GUI).

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">



## Рабочий процесс 


<div class="mw-translate-fuzzy">

Шаги которые необходимо сделать для выполнению анализа методом конечных элементов:

1.  Предварительная обработка: постановка задачи анализа.
    1.  Моделирование геометрии: создание геометрии с помощью FreeCAD или ее импорт из другого приложения.
    2.  Создание анализа.
        1.  Добавление ограничений моделирования, таких как нагрузки и фиксированные опоры, к геометрической модели.
        2.  Добавление материалов к деталям геометрической модели.
        3.  Создание сетки конечных элементов для геометрической модели или ее импорт из другого приложения.
2.  Решение: запуск внешнего решателя из FreeCAD.
3.  Постобработка: визуализация результатов анализа из FreeCAD или экспорт результатов для их последующей обработки в другом приложении.


</div>

Верстак FEM можно использовать в Linux, Windows и Mac OSX. Поскольку данный верстак использует внешние решатели, количество требуемых дополнительных настрлек будет зависеть от используемой вами операционной системы. Инструкции по настройке внешних инструментов смотрите в разделе [Установка FEM](FEM_Install/ru.md).

<img alt="" src=images/FEM_Workbench_workflow.svg  style="width:600px;">



*Рабочий процесс в верстаке FEM ; Верстак обращается к двум внешними программам, к первой для создания сетки твердого объекта и ко второй для выполнения фактического решения задачи методом конечных элементов*



## Меню: Модель 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analysis container](FEM_Analysis/ru.md): Создаёт новый контейнер для механического анализа. Если перед кликом на нём было выделено твёрдое тело, будет запущен диалог создания сетки МКЭ.



### Материалы

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Твердотельный материал](FEM_MaterialSolid/ru.md): Позволяет выбрать твердый материал из базы данных.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Текучий материал](FEM_MaterialFluid/ru.md): Позволяет выбрать текучий материал из базы данных.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Нелинейный механический материал](FEM_MaterialMechanicalNonlinear/ru.md): Позволяет добавить нелинейную механическую модель материала.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Армированный материал (бетон)](FEM_MaterialReinforced/ru.md): Позволяет выбрать из базы данных армированные материалы, состоящие из матрицы и армирования.

-   <img alt="" src=images/FEM_MaterialEditor.svg  style="width:32px;"> [Material editor](FEM_MaterialEditor/ru.md): Открыть редактор материалов для их редактирования.



### Геометрия элемента 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Поперечное сечение балки](FEM_ElementGeometry1D/ru.md): Создает условие поперечного сечения балки для МКЭ.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Вращение балки](FEM_ElementRotation1D/ru.md): Создает условие поворота балки для МКЭ.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Толщина листа материала](FEM_ElementGeometry2D/ru.md): Создает условие толщины листа материала.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Fluid section for 1D flow](FEM_ElementFluid1D/ru.md): Создает элемент жидкостной секции МКЭ для пневматических и гидравлических сетей.


</div>




<div class="mw-translate-fuzzy">

### Электростатические ограничения 


</div>

-   <img alt="" src=images/FEM_CompEmConstraints.png  style="width:" height="32px;"> [Electromagnetic constraints](FEM_CompEmConstraints.md): This is an icon menu in the FEM Constraints toolbar that holds the following constraints:


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Создать электростатический потенциал](FEM_ConstraintElectrostaticPotential/ru.md): Создает граничное условие МКЭ для электростатического потенциала.


</div>

  - <img alt="" src=images/FEM_ConstraintCurrentDensity.svg  style="width:32px;"> [Constraint current density](FEM_ConstraintCurrentDensity.md): Used to define a current density. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_ConstraintMagnetization.svg  style="width:32px;"> [Constraint magnetization](FEM_ConstraintMagnetization.md): Used to define a magnetization. <small>(v0.21)</small> 



### Жидкостные ограничения 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Начальное условие скорости потока](FEM_ConstraintInitialFlowVelocity/ru.md): Применяется для определения начальной скорости потока в области.


</div>

-   <img alt="" src=images/FEM_ConstraintInitialPressure.svg  style="width:32px;"> [Constraint initial pressure](FEM_ConstraintInitialPressure.md): Used to define an initial pressure for a body (volume). <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Граничное условие скорости потока](FEM_ConstraintFlowVelocity/ru.md): Применяется для задания скорости потока как граничного условия на ребре (2D) или грани (3D).



### Геометрические Ограничения 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Constraint plane rotation](FEM_ConstraintPlaneRotation/ru.md): Используется для определения ограничения плоского вращения на плоской поверхности.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Constraint sectionprint](FEM_ConstraintSectionPrint/ru.md): Creates a FEM constraint sectionprint {{Version/ru|0.19}}.


</div>

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Constraint transform](FEM_ConstraintTransform/ru.md): Используется для назначения ограничения трансформации на грани.



### Механические ограничения 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Constraint fixed](FEM_ConstraintFixed/ru.md): Используется для определения ограничения с фиксацией точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Ограничение перемещения](FEM_ConstraintDisplacement/ru.md): Используется для определения ограничений смещения для точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Constraint contact](FEM_ConstraintContact/ru.md): Используется для определения контактного ограничения между двумя поверхностями.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Constraint tie](FEM_ConstraintTie/ru.md): Creates a FEM constraint tie {{Version/ru|0.19}}.


</div>

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Constraint force](FEM_ConstraintForce/ru.md): Используется для определения силы в \[N\], приложенной равномерно к выбираемой поверхности в определяемом направлении.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Constraint pressure](FEM_ConstraintPressure/ru.md): Используется для определения ограничения давления.

-   <img alt="" src=images/FEM_ConstraintCentrif.svg  style="width:32px;"> [Constraint centrif](FEM_ConstraintCentrif.md): Used to define a centrifugal body load constraint. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Constraint self weight](FEM_ConstraintSelfWeight/ru.md): используется для определения ускорения свободного падения, действующего на модель.



### Температурные ограничения 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature/ru.md): Используется для определения начальной температуры тела.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Constraint heatflux](FEM_ConstraintHeatflux/ru.md): Используется для определения ограничений тепловых потоков на поверхностях.

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Constraint temperature](FEM_ConstraintTemperature/ru.md): Используется для определения температурных ограничений для точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Задать тело, являющееся источником тепла](FEM_ConstraintBodyHeatSource/ru.md): Создает граничное условие для МКЭ определяющее тело, являющееся источником тепла.



### Ограничения без решателя 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid boundary condition](FEM_ConstraintFluidBoundary/ru.md): Create fluid boundary condition on face entity for Computional Fluid Dynamics.


</div>

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing/ru.md): Используется для определения подшипниковых ограничений.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear/ru.md): Используется для определения редукторных ограничений.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley/ru.md): Используется для определения ограничений шкива.

### Overwrite Constants 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity/ru.md): Creates a FEM constant vacuum permittivity to overwrite standard value.


</div>



## Меню: Сетка 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Cетка МКЭ из фигуры генерируемая построителем Netgen](FEM_MeshNetgenFromShape/ru.md): Create a FEM mesh from a solid or face shape by Netgen internal mesher.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Сетка МКЭ из фигуры генерируемая построителем Gmsh](FEM_MeshGmshFromShape/ru.md): Создать сетку МКЭ из фигуры с помощью генератора сетки Gmsh.


</div>

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Граничный слой сетки МКЭ](FEM_MeshBoundaryLayer/ru.md): Создает граничный слой сетки МКЭ.

Translations:FEM Module/141/ru

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Область сетки МКЭ](FEM_MeshRegion/ru.md): Создать область сетки МКЭ.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Группа сетки МКЭ](FEM_MeshGroup/ru.md): Создает группу сетки МКЭ.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet/ru.md): Creates a FEM mesh nodes set.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh/ru.md): Преобразуйте поверхность сетки МКЭ в сетку.



## Меню: Решение 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools/ru.md): Создает новый решатель для этого анализа. В большинстве случаев решатель создается вместе с анализом.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Решатель CalculiX (экспериментальный)](FEM_SolverCalculiX/ru.md): Создает решатель МКЭ CalculiX (экспериментальный).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer/ru.md): Создает контроллер решателя для Элмера. Он не зависит от других объектов решателя.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Решатель Mystran](FEM_SolverMystran/ru.md): {{Version/ru|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Решатель Z88](FEM_SolverZ88/ru.md): Создает задачу для решателя МКЭ Z88 .


</div>

-   <img alt="" src=images/FEM_CompMechEquations.png  style="width:" height="32px;"> [Mechanical equations](FEM_CompMechEquations.md): This is an icon menu in the FEM Equations toolbar that holds the following equations: <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Уравнение гибкости](FEM_EquationElasticity/ru.md): Создает уравнение для расчета упругости МКЭ.


</div>

  - <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Deformation equation](FEM_EquationDeformation.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to perform nonlinear mechanical analyses (deformations). <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_CompEmEquations.png  style="width:" height="32px;"> [Electromagnetic equations](FEM_CompEmEquations.md): This is an icon menu in the FEM Equations toolbar that holds the following equations: <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Электростатические уравнение](FEM_EquationElectrostatic/ru.md): Создает уравнение для расчета электростатики МКЭ.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce/ru.md): Creates a FEM equation for electric forces.


</div>

  - <img alt="" src=images/FEM_EquationMagnetodynamic.svg  style="width:32px;"> [Magnetodynamic equation](FEM_EquationMagnetodynamic.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_EquationMagnetodynamic2D.svg  style="width:32px;"> [Magnetodynamic 2D equation](FEM_EquationMagnetodynamic2D.md): Equation for the <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer.md) to calculate magnetodynamics in 2D. <small>(v0.21)</small> 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Уравнение потока](FEM_EquationFlow/ru.md): Создает уравнение МКЭ для потока вещества.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux/ru.md): Creates a FEM equation for flux.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat/ru.md): Creates a FEM equation for heat.


</div>

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solver job control](FEM_SolverControl/ru.md): Открывает меню для настройки и запуска выбранного решателя.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Run solver calculations](FEM_SolverRun/ru.md): Запускает выбранный решатель текущего анализа.



## Меню: Результаты 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purge results](FEM_ResultsPurge/ru.md): Очищает текущие результаты расчёта (Results в древе проекта).


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow/ru.md): Используется для показа результатов исследования (Von Mises Stress или Displacement).


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Apply changes to pipeline](FEM_PostApplyChanges/ru.md): Apply changes to parameters directly and not on recompute only\....


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post pipeline from result](FEM_PostPipelineFromResult/ru.md): Creates a post processing pipeline from a result object.


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp filter](FEM_PostFilterWarp/ru.md): Warp the geometry along a vector field by a certain factor.


</div>

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar/ru.md): Применяется для обрезки поля с заданным скалярным значением.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction/ru.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion/ru.md):


</div>

-   <img alt="" src=images/FEM_PostFilterContours.svg  style="width:32px;"> [Contours filter](FEM_PostFilterContours.md): Used to display iso-lines (for analyses in 2D) or iso-contours. <small>(v0.21)</small> 

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine/ru.md): Применяется для построения цветовой диаграммы вдоль указанной линии.

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses/ru.md): Создает график линеаризации напряжений.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint/ru.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;"> [Filter functions](FEM_PostCreateFunctions/ru.md): Used to define how the result mesh is cut for the [Function cut filter](FEM_PostFilterCutFunction/ru.md) and [Region clip filter](FEM_PostFilterClipRegion/ru.md).


</div>

  - <img alt="" src=images/FEM_PostCreateFunctionPlane.svg  style="width:32px;"> [Filter function plane](FEM_PostCreateFunctionPlane.md): Cuts the result mesh with a plane.

  - <img alt="" src=images/FEM_PostCreateFunctionSphere.svg  style="width:32px;"> [Filter function sphere](FEM_PostCreateFunctionSphere.md): Cuts the result mesh with a sphere.

  - <img alt="" src=images/FEM_PostCreateFunctionCylinder.svg  style="width:32px;"> [Filter function cylinder](FEM_PostCreateFunctionCylinder.md): Cuts the result mesh with a cylinder. <small>(v0.21)</small> 

  - <img alt="" src=images/FEM_PostCreateFunctionBox.svg  style="width:32px;"> [Filter function box](FEM_PostCreateFunctionBox.md): Cuts the result mesh with a box. <small>(v0.21)</small> 



## Меню: Утилиты 


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Clipping plane on face](FEM_ClippingPlaneAdd/ru.md):


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Remove all clipping planes](FEM_ClippingPlaneRemoveAll/ru.md):


</div>

-   <img alt="" src=images/FEM_Examples.svg  style="width:32px;"> [Open FEM examples](FEM_Examples/ru.md): Открыть графический интерфейс для доступа к примерам МКЭ.



## Контекстное меню 

-   <img alt="" src=images/FEM_MeshClear.svg  style="width:32px;"> [Clear FEM mesh](FEM_MeshClear/ru.md):

-   <img alt="" src=images/FEM_MeshDisplayInfo.svg  style="width:32px;"> [Display FEM mesh info](FEM_MeshDisplayInfo/ru.md):



## Настройки

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferences\...](FEM_Preferences/ru.md): Доступные настройки инструментов FEM.



## Информация

На следующих страницах объясняются различные темы верстака FEM.

[Установка FEM](FEM_Install/ru.md): подробное описание по установке(настройке) внешних программ используемых для работы верстака.

[FEM Mesh](FEM_Mesh/ru.md): дополнительная информация о получении сетки для анализа методом конечных элементов.

[FEM Solver](FEM_Solver/ru.md): дополнительная информация о различных решателях метода конечных элементов, доступных в верстаке, и о тех, которые могут быть использованы в будущем.

[FEM CalculiX](FEM_CalculiX/ru.md) дополнительная информация о CalculiX, решателе по умолчанию, используемом в инструментальных средствах для расчета конструкций.

[FEM Concrete](FEM_Concrete/ru.md): интересная информация по теме моделирования бетонных конструкций.



## Учебные материалы для самостоятельного изучения 

Пример 1: [Анализ деформации консольной балки (CalculiX)](FEM_CalculiX_Cantilever_3D/ru.md), простейший анализ деформации консольной балки под воздействием нагрузки.

Пример 2: [Учебник по МКЭ](FEM_tutorial/ru.md), простой анализ натяжения конструкции.

Пример 3: [FEM Tutorial Python](FEM_Tutorial_Python/ru.md), настроить пример консоли только с помощью скриптов на Python, включая сетку.

Пример 4: [Анализ деформации композитного блока](FEM_Shear_of_a_Composite_Block/ru.md); анализ деформации композитного блока, состоящего из двух материалов.


<div class="mw-translate-fuzzy">

Пример 5: [Переходный анализ методом конечных элементов](Transient_FEM_analysis/ru.md)


</div>


<div class="mw-translate-fuzzy">

Пример 6: [Постобработка результатов МКЭ с помощью Paraview](Post-Processing_of_FEM_Results_with_Paraview/ru.md)


</div>


<div class="mw-translate-fuzzy">

Пример 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls/ru.md), Учебное пособие по графическому интерфейсу Элмера 6 «Электростатическая емкость двух шариков» с использованием примеров МКЭ.


</div>

Набор руководств по термомеханическому анализу от [openSIM](https://opensimsa.github.io/training.html)

Video tutorial 1: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (including YouTube link)

Video tutorial 2: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (including YouTube link)

Many video tutorials: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in German)



## Развитие верстака FEM 

Верстак FEM находится в постоянном развитии. Цель проекта - найти способы простого взаимодействия с различными решателями МКЭ, чтобы конечный пользователь мог упростить процесс создания, построения сетки, моделирования и оптимизации задачи инженерного проектирования, и все это внутри FreeCAD.


<div class="mw-translate-fuzzy">

Дальнейшая информация предназначена для опытных пользователей и разработчиков, которые хотят расширить верстак FEM. Ожидается знакомство с C ++ и Python, а также необходимы некоторые знания о системе «объект документа», используемой в FreeCAD; эта информация доступна в [Центре опытных пользователей](Power_users_hub/ru.md) и [Центре разработчиков](Developer_hub/ru.md). Обратите внимание: поскольку FreeCAD находится в активной разработке, некоторые статьи могут быть слишком старыми и, следовательно, устаревшими. Самая последняя информация обсуждается на [форумах FreeCAD](https://forum.freecadweb.org/index.php) в разделе «Разработка». Для обсуждения FEM, советов или помощи в расширении верстака читателю следует обратиться к [подфоруму FEM](https://forum.freecadweb.org/viewforum.php?f=18).


</div>


<div class="mw-translate-fuzzy">

В следующих статьях объясняется, как можно расширить рабочую среду, например, путем добавления новых типов граничных условий (ограничений) или уравнений.

-   [Extend FEM Module](Extend_FEM_Module/ru.md)
-   [Добавление ограничений в верстак FEM](Add_FEM_Constraint_Tutorial/ru.md)
-   [Учебник по добавлению уравнений в верстак FEM](Add_FEM_Equation_Tutorial/ru.md)


</div>

Руководство разработчика было написано, чтобы помочь опытным пользователям разобраться в сложной кодовой базе FreeCAD и взаимодействиях между основными элементами и отдельными рабочими средами. Книга размещена на github, поэтому несколько пользователей могут вносить в нее свой вклад и постоянно обновлять.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) (тема форума)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (хранилище github)



## Дополнительная документация к Верстаку FEM 

-   More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/ru
