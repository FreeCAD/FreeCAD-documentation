# <img alt="Логотип верстака FEM" src=images/Workbench_FEM.svg  style="width:64px;"> FEM Workbench/ru


{{TOCright}}

## Введение

[Верстак FEM](FEM_Workbench/ru.md) предоставляет современный набор инструментов для анализа [Методом Конечных Элементов](https://en.wikipedia.org/wiki/Метод_конечных_элементов) (finite element analysis, FEA) в FreeCAD. В основном это означает, что все инструменты для проведения анализа объединены в один графический интерфейс пользователя (GUI).

<img alt="" src=images/FemWorkbench.jpg  style="width:300px;">

## Рабочий процесс 

Шаги которые необходимо сделать для выполнению анализа методом конечных элементов:

1.  Предварительная обработка: постановка задачи анализа.
    1.  Моделирование геометрии: создание геометрии с помощью FreeCAD или ее импорт из другого приложения.
    2.  Создание анализа.
        1.  Добавление ограничений моделирования, таких как нагрузки и фиксированные опоры, к геометрической модели.
        2.  Добавление материалов к деталям геометрической модели.
        3.  Создание сетки конечных элементов для геометрической модели или ее импорт из другого приложения.
2.  Решение: запуск внешнего решателя из FreeCAD.
3.  Постобработка: визуализация результатов анализа из FreeCAD или экспорт результатов для их последующей обработки в другом приложении.

В версиях 0.15 и 0,16 FreeCAD верстак FEM может использоваться на Linux, Windows и Mac OSX. Поскольку в рабочей среде используются внешние решатели, объем ручной настройки будет зависеть от используемой вами операционной системы. См. [Установка FEM](FEM_Install/ru.md) для получения инструкций по настройке внешних инструментов.

<img alt="" src=images/FEM_Workbench_workflow_ru.svg  style="width:600px;">



*Рабочий процесс FEM Workbench; верстак вызывает две внешние программы для создания сетки твердого объекта и выполнения фактического решения задачи конечных элементов*

## Меню: Модель 

-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> [Analysis container](FEM_Analysis/ru.md): Создаёт новый контейнер для механического анализа. Если перед кликом на нём было выделено твёрдое тело, будет запущен диалог создания сетки МКЭ.

### Материалы

-   <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> [Material for solid](FEM_MaterialSolid/ru.md): Выберите материал из базы данных.

-   <img alt="" src=images/FEM_MaterialFluid.svg  style="width:32px;"> [Material for fluid](FEM_MaterialFluid/ru.md): Выберите материал из базы данных.

-   <img alt="" src=images/FEM_MaterialMechanicalNonlinear.svg  style="width:32px;"> [Nonlinear mechanical material](FEM_MaterialMechanicalNonlinear/ru.md): Выберите материал из базы данных.

-   <img alt="" src=images/FEM_MaterialReinforced.svg  style="width:32px;"> [Армированный материал (бетон)](FEM_MaterialReinforced/ru.md): Позволяет выбрать из базы данных армированные материалы, состоящие из матрицы и армирования.

-   <img alt="" src=images/Arch_Material_Group.svg  style="width:32px;"> [Material editor](Material_editor/ru.md): Позволяет открыть редактор для редактирования материалов.

### Геометрия элемента 

-   <img alt="" src=images/FEM_ElementGeometry1D.svg  style="width:32px;"> [Поперечное сечение балки](FEM_ElementGeometry1D/ru.md): Создает условие поперечного сечения балки для МКЭ.

-   <img alt="" src=images/FEM_ElementRotation1D.svg  style="width:32px;"> [Вращение балки](FEM_ElementRotation1D/ru.md): Создает условие поворота балки для МКЭ.

-   <img alt="" src=images/FEM_ElementGeometry2D.svg  style="width:32px;"> [Толщины листа кровельного материала](FEM_ElementGeometry2D/ru.md): Создает Условие толщины пластины кровельного материала для расчета МКЭ.

-   <img alt="" src=images/FEM_ElementFluid1D.svg  style="width:32px;"> [Fluid section for 1D flow](FEM_ElementFluid1D/ru.md): Создает элемент жидкостной секции МКЭ для пневматических и гидравлических сетей.

### Электростатические ограничения 

-   <img alt="" src=images/FEM_ConstraintElectrostaticPotential.svg  style="width:32px;"> [Создать электростатический потенциал](FEM_ConstraintElectrostaticPotential/ru.md): Создает граничное условие МКЭ для электростатического потенциала.

### Жидкостные ограничения 

-   <img alt="" src=images/FEM_ConstraintInitialFlowVelocity.svg  style="width:32px;"> [Constraint initial flow velocity](FEM_ConstraintInitialFlowVelocity/ru.md): Используется для определения начальной скорости потока в области.

-   <img alt="" src=images/FEM_ConstraintFlowVelocity.svg  style="width:32px;"> [Constraint flow velocity](FEM_ConstraintFlowVelocity/ru.md): Используется для задания скорости потока как граничного условия на кромке (2D) или грани (3D).

### Геометрические Ограничения 

-   <img alt="" src=images/FEM_ConstraintPlaneRotation.svg  style="width:32px;"> [Constraint plane rotation](FEM_ConstraintPlaneRotation/ru.md): Используется для определения ограничения плоского вращения на плоской поверхности.

-   <img alt="" src=images/FEM_ConstraintSectionPrint.svg  style="width:32px;"> [Constraint sectionprint](FEM_ConstraintSectionPrint/ru.md): Creates a FEM constraint sectionprint {{Version/ru|0.19}}.

-   <img alt="" src=images/FEM_ConstraintTransform.svg  style="width:32px;"> [Constraint transform](FEM_ConstraintTransform/ru.md): Используется для назначения ограничения трансформации на грани.

### Механические ограничения 

-   <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> [Constraint fixed](FEM_ConstraintFixed/ru.md): Используется для определения ограничения с фиксацией точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintDisplacement.svg  style="width:32px;"> [Constraint displacement](FEM_ConstraintDisplacement/ru.md): Используется для определения ограничений смещения для точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintContact.svg  style="width:32px;"> [Constraint contact](FEM_ConstraintContact/ru.md): Используется для определения контактного ограничения между двумя поверхностями.

-   <img alt="" src=images/FEM_ConstraintTie.svg  style="width:32px;"> [Constraint tie](FEM_ConstraintTie/ru.md): Creates a FEM constraint tie {{Version/ru|0.19}}.

-   <img alt="" src=images/FEM_ConstraintSpring.svg  style="width:32px;"> [Constraint spring](FEM_ConstraintSpring.md): Used to define a spring. <small>(v0.20)</small> 

-   <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> [Constraint force](FEM_ConstraintForce/ru.md): Используется для определения силы в \[N\], приложенной равномерно к выбираемой поверхности в определяемом направлении.

-   <img alt="" src=images/FEM_ConstraintPressure.svg  style="width:32px;"> [Constraint pressure](FEM_ConstraintPressure/ru.md): Используется для определения ограничения давления.

-   <img alt="" src=images/FEM_ConstraintSelfWeight.svg  style="width:32px;"> [Constraint self weight](FEM_ConstraintSelfWeight/ru.md): используется для определения ускорения свободного падения, действующего на модель.

### Температурные ограничения 

-   <img alt="" src=images/FEM_ConstraintInitialTemperature.svg  style="width:32px;"> [Constraint initial temperature](FEM_ConstraintInitialTemperature/ru.md): Используется для определения начальной температуры тела.

-   <img alt="" src=images/FEM_ConstraintHeatflux.svg  style="width:32px;"> [Constraint heatflux](FEM_ConstraintHeatflux/ru.md): Используется для определения ограничений тепловых потоков на поверхностях.

-   <img alt="" src=images/FEM_ConstraintTemperature.svg  style="width:32px;"> [Constraint temperature](FEM_ConstraintTemperature/ru.md): Используется для определения температурных ограничений для точки/грани/поверхности.

-   <img alt="" src=images/FEM_ConstraintBodyHeatSource.svg  style="width:32px;"> [Задать тело, являющееся источником тепла](FEM_ConstraintBodyHeatSource/ru.md): Создает граничное условие для МКЭ определяющее тело, являющееся источником тепла.

### Ограничения без решателя 

-   <img alt="" src=images/FEM_ConstraintFluidBoundary.svg  style="width:32px;"> [Fluid boundary condition](FEM_ConstraintFluidBoundary/ru.md): Create fluid boundary condition on face entity for Computional Fluid Dynamics.

-   <img alt="" src=images/FEM_ConstraintBearing.svg  style="width:32px;"> [Constraint bearing](FEM_ConstraintBearing/ru.md): Используется для определения подшипниковых ограничений.

-   <img alt="" src=images/FEM_ConstraintGear.svg  style="width:32px;"> [Constraint gear](FEM_ConstraintGear/ru.md): Используется для определения редукторных ограничений.

-   <img alt="" src=images/FEM_ConstraintPulley.svg  style="width:32px;"> [Constraint pulley](FEM_ConstraintPulley/ru.md): Используется для определения ограничений шкива.

### Overwrite Constants 

-   <img alt="" src=images/FEM_ConstantVacuumPermittivity.svg  style="width:32px;"> [Constant vacuum permittivity](FEM_ConstantVacuumPermittivity/ru.md): Creates a FEM constant vacuum permittivity to overwrite standard value.

## Меню: Сетка 

-   <img alt="" src=images/FEM_MeshNetgenFromShape.svg  style="width:32px;"> [Cетка МКЭ из фигуры генерируемая построителем Netgen](FEM_MeshNetgenFromShape/ru.md): Create a FEM mesh from a solid or face shape by Netgen internal mesher.

-   <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:32px;"> [Сетка МКЭ из фигуры генерируемая построителем Gmsh](FEM_MeshGmshFromShape/ru.md): Создать сетку МКЭ из фигуры с помощью генератора сетки Gmsh.

-   <img alt="" src=images/FEM_MeshBoundaryLayer.svg  style="width:32px;"> [Граничный слой сетки МКЭ](FEM_MeshBoundaryLayer/ru.md): Создает граничный слой сетки МКЭ.

Translations:FEM Module/141/ru

-   <img alt="" src=images/FEM_MeshRegion.svg  style="width:32px;"> [Область сетки МКЭ](FEM_MeshRegion/ru.md): Создать область сетки МКЭ.

-   <img alt="" src=images/FEM_MeshGroup.svg  style="width:32px;"> [Группа сетки МКЭ](FEM_MeshGroup/ru.md): Создает группу сетки МКЭ.

-   <img alt="" src=images/FEM_CreateNodesSet.svg  style="width:32px;"> [Nodes set](FEM_CreateNodesSet/ru.md): Creates a FEM mesh nodes set.

-   <img alt="" src=images/FEM_FemMesh2Mesh.svg  style="width:32px;"> [FEM mesh to mesh](FEM_FemMesh2Mesh/ru.md): Преобразуйте поверхность сетки МКЭ в сетку.

## Меню: Решение 

-   <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> [Solver CalculiX Standard](FEM_SolverCalculixCxxtools/ru.md): Создает новый решатель для этого анализа. В большинстве случаев решатель создается вместе с анализом.

-   <img alt="" src=images/FEM_SolverCalculiX.svg  style="width:32px;"> [Решатель CalculiX (экспериментальный)](FEM_SolverCalculiX/ru.md): Создает решатель МКЭ CalculiX (экспериментальный).

-   <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Solver Elmer](FEM_SolverElmer/ru.md): Создает контроллер решателя для Элмера. Он не зависит от других объектов решателя.

-   <img alt="" src=images/FEM_SolverMystran.svg  style="width:32px;"> [Solver Mystran](FEM_SolverMystran.md):

-   <img alt="" src=images/FEM_SolverZ88.svg  style="width:32px;"> [Решатель Z88](FEM_SolverZ88/ru.md): Создает задачу для решателя МКЭ Z88 .

-   <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Уравнение гибкости](FEM_EquationElasticity/ru.md): Создает уравнение для расчета упругости МКЭ.

-   <img alt="" src=images/FEM_EquationElectricforce.svg  style="width:32px;"> [Electricforce equation](FEM_EquationElectricforce/ru.md): Creates a FEM equation for electric forces.

-   <img alt="" src=images/FEM_EquationElectrostatic.svg  style="width:32px;"> [Электростатические уравнение](FEM_EquationElectrostatic/ru.md): Создает уравнение для расчета электростатики МКЭ.

-   <img alt="" src=images/FEM_EquationFlow.svg  style="width:32px;"> [Уравнение потока](FEM_EquationFlow/ru.md): Создает уравнение МКЭ для потока вещества.

-   <img alt="" src=images/FEM_EquationFlux.svg  style="width:32px;"> [Flux equation](FEM_EquationFlux/ru.md): Creates a FEM equation for flux.

-   <img alt="" src=images/FEM_EquationHeat.svg  style="width:32px;"> [Heat equation](FEM_EquationHeat/ru.md): Creates a FEM equation for heat.

-   <img alt="" src=images/FEM_SolverControl.svg  style="width:32px;"> [Solver job control](FEM_SolverControl/ru.md): Открывает меню для настройки и запуска выбранного решателя.

-   <img alt="" src=images/FEM_SolverRun.svg  style="width:32px;"> [Run solver calculations](FEM_SolverRun/ru.md): Запускает выбранный решатель текущего анализа.

## Меню: Результаты 

-   <img alt="" src=images/FEM_ResultsPurge.svg  style="width:32px;"> [Purge results](FEM_ResultsPurge/ru.md): Очищает текущие результаты расчёта (Results в древе проекта).

-   <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;"> [Show result](FEM_ResultShow/ru.md): Используется для показа результатов исследования (Von Mises Stress или Displacement).

-   <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:32px;"> [Apply changes to pipeline](FEM_PostApplyChanges/ru.md): Apply changes to parameters directly and not on recompute only\....

-   <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:32px;"> [Post pipeline from result](FEM_PostPipelineFromResult/ru.md): Creates a post processing pipeline from a result object.

-   <img alt="" src=images/FEM_PostFilterWarp.svg  style="width:32px;"> [Warp filter](FEM_PostFilterWarp/ru.md): Warp the geometry along a vector field by a certain factor.

-   <img alt="" src=images/FEM_PostFilterClipScalar.svg  style="width:32px;"> [Scalar clip filter](FEM_PostFilterClipScalar/ru.md):

-   <img alt="" src=images/FEM_PostFilterCutFunction.svg  style="width:32px;"> [Function cut filter](FEM_PostFilterCutFunction/ru.md):

-   <img alt="" src=images/FEM_PostFilterClipRegion.svg  style="width:32px;"> [Region clip filter](FEM_PostFilterClipRegion/ru.md):

-   <img alt="" src=images/FEM_PostFilterDataAlongLine.svg  style="width:32px;"> [Line clip filter](FEM_PostFilterDataAlongLine/ru.md):

-   <img alt="" src=images/FEM_PostFilterLinearizedStresses.svg  style="width:32px;"> [Stress linearization plot](FEM_PostFilterLinearizedStresses/ru.md):

-   <img alt="" src=images/FEM_PostFilterDataAtPoint.svg  style="width:32px;"> [Data at point clip filter](FEM_PostFilterDataAtPoint/ru.md):

-   [Filter functions](FEM_PostCreateFunctions/ru.md):
    -   <img alt="" src=images/Fem-post-geo-plane.svg  style="width:32px;">
    -   <img alt="" src=images/Fem-post-geo-sphere.svg  style="width:32px;">

## Меню: Утилиты 

-   <img alt="" src=images/FEM_ClippingPlaneAdd.svg  style="width:32px;"> [Clipping plane on face](FEM_ClippingPlaneAdd/ru.md):

-   <img alt="" src=images/FEM_ClippingPlaneRemoveAll.svg  style="width:32px;"> [Remove all clipping planes](FEM_ClippingPlaneRemoveAll/ru.md):

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

[FEM Project](FEM_project/ru.md) дополнительная информация о системе единиц измерения, ограничениях, а также об идеях развития и дорожной карте верстака.

## Учебники

Учебник 1: [FEM CalculiX Cantilever 3D](FEM_CalculiX_Cantilever_3D/ru.md), базовый анализ балки с простой опорой.

Учебник 2: [Учебник по МКЭ](FEM_tutorial/ru.md), простой анализ натяжения конструкции.

Учебник 3: [FEM Tutorial Python](FEM_Tutorial_Python/ru.md), настроить пример консоли только с помощью скриптов на Python, включая сетку.

Учебник 4: [FEM Shear of a Composite Block](FEM_Shear_of_a_Composite_Block/ru.md); увидеть деформацию блока, состоящего из двух материалов.

Учебник 5: [Переходный анализ методом конечных элементов](Transient_FEM_analysis/ru.md)

Учебник 6: [Постобработка результатов МКЭ с помощью Paraview](Post-Processing_of_FEM_Results_with_Paraview/ru.md)

Учебник 7: [FEM Example Capacitance Two Balls](FEM_Example_Capacitance_Two_Balls/ru.md), Учебное пособие по графическому интерфейсу Элмера 6 «Электростатическая емкость двух шариков» с использованием примеров МКЭ.

Набор учебников по термомеханическому анализу от [openSIM](https://opensimsa.github.io/training.html)

Video tutorial 1: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499#p158353) (including YouTube link)

Video tutorial 2: [FEM video for beginner](https://forum.freecadweb.org/viewtopic.php?f=18&t=20499&start=10#p162321) (including YouTube link)

Many video tutorials: [anisim Open Source Engineering Software](https://www.youtube.com/channel/UCnvFCm2BbXOVI3ObfXcxXhw) (in German)

## Расширение верстака FEM 

Верстак FEM находится в постоянном развитии. Цель проекта - найти способы простого взаимодействия с различными решателями МКЭ, чтобы конечный пользователь мог упростить процесс создания, построения сетки, моделирования и оптимизации задачи инженерного проектирования, и все это внутри FreeCAD.

Дальнейшая информация предназначена для опытных пользователей и разработчиков, которые хотят расширить верстак FEM. Ожидается знакомство с C ++ и Python, а также необходимы некоторые знания о системе «объект документа», используемой в FreeCAD; эта информация доступна в [Центре опытных пользователей](Power_users_hub/ru.md) и [Центре разработчиков](Developer_hub/ru.md). Обратите внимание: поскольку FreeCAD находится в активной разработке, некоторые статьи могут быть слишком старыми и, следовательно, устаревшими. Самая последняя информация обсуждается на [форумах FreeCAD](https://forum.freecadweb.org/index.php) в разделе «Разработка». Для обсуждения FEM, советов или помощи в расширении верстака читателю следует обратиться к [подфоруму FEM](https://forum.freecadweb.org/viewforum.php?f=18).


<div class="mw-translate-fuzzy">

В следующих статьях объясняется, как можно расширить рабочую среду, например, путем добавления новых типов граничных условий (ограничений) или уравнений.

-   [Extend FEM Module](Extend_FEM_Module/ru.md)
-   [Добавление ограничений в верстак FEM](Add_FEM_Constraint_Tutorial/ru.md)
-   [Учебник по добавлению уравнений в верстак FEM](Add_FEM_Equation_Tutorial/ru.md)


</div>

Руководство разработчика было написано, чтобы помочь опытным пользователям разобраться в сложной кодовой базе FreeCAD и взаимодействиях между основными элементами и отдельными рабочими средами. Книга размещена на github, поэтому несколько пользователей могут вносить в нее свой вклад и постоянно обновлять.

-   [Early preview of ebook: Module developer\' guide to FreeCAD source](https://forum.freecadweb.org/viewtopic.php?t=17581) (тема форума)
-   [FreeCAD Mod Dev Guide](https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide) (хранилище github)

## Расшириенная информация о Верстаке FEM 

-   More information regarding extending or missing FEM documentation can be found in the forum: [FEM documentation missing on the Wiki](https://forum.freecadweb.org/viewtopic.php?f=18&t=20823)





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [FEM](Category_FEM.md) > FEM Workbench/ru
