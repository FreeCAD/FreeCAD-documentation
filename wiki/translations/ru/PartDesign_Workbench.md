# PartDesign Workbench/ru

 

<img alt="Иконка верстака PartDesign" src=images/Workbench_PartDesign.svg  style="width:128px;">


{{TOCright}}

## Введение


<div class="mw-translate-fuzzy">

<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">[Верстак PartDesign](PartDesign_Workbench/ru.md) предоставляет расширенные инструменты для моделирования сложных твердых деталей. Он в основном сосредоточен на создании механических деталей, которые можно изготовить и собрать в готовый продукт. Тем не менее, созданные тела могут быть использованы в целом для любых других целей, таких как [архитектурный дизайн](Arch_Workbench/ru.md), [анализ методом конечных элементов](FEM_Workbench/ru.md) или [механической обработки и 3D-печати](Path_Workbench/ru.md).


</div>

PartDesign Workbench неразрывно связан с [верстаком Sketcher](Sketcher_Workbench/ru.md). Пользователь обычно создает эскиз, затем использует инструмент [PartDesign Pad](PartDesign_Pad/ru.md) для его выдавливания и создания простого объемного тела, далее это тело дополнительно модифицируется.

While the <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Workbench](Part_Workbench.md) is based on a [constructive solid geometry](constructive_solid_geometry.md) (CSG) methodology for building shapes, the PartDesign Workbench uses a parametric, feature editing methodology, which means a basic solid is sequentially transformed by adding features on top until the final shape is obtained. See the [feature editing](feature_editing.md) page for a more complete explanation of this process, and then see [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md) to get started with creating solids.

A more detailed discussion of Part workbench versus Part Design workbench can be found here: [Part and Part Design](Part_and_PartDesign.md).

The bodies created with PartDesign are often subject to the [topological naming problem](Topological_naming_problem.md) which causes internal features to be renamed when the parametric operations are modified. This problem can be minimized by following the best practices described in the [feature editing](feature_editing.md) page, and by taking advantage of datum objects as support for sketches and features.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Инструменты

Все инструменты проектирования деталей находятся в меню **Part Design** и на панели инструментов PartDesign, которая появляется при загрузке рабочей среды проектирования деталей.

### Инструменты упорядочивания 

These tools are in fact not part of the PartDesign Workbench. They belong to the [Std Base](Std_Base.md) system. They were developed in v0.17 with the intention that they would be useful to organize a model, and create [assemblies](Assembly.md); as such, they are very useful when working with bodies created with this workbench.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Создать деталь](Std_Part/ru.md): создает новую Деталь в текущем документе и делает её активной.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Создать группу](Std_Group/ru.md): создает в текужем документе объединяющий контейнер группу, что позволяет упорядочить объекты в [дереве просмотра](Tree_view.md).

### Вспомогательные инструменты для моделирования Детали 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Create body](PartDesign_Body.md): creates a [Body](Body.md) object in the active document and makes it active.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Create sketch](PartDesign_NewSketch.md): creates‎ a new sketch on a selected face or plane. If no face is selected while this tool is executed, the user is prompted to select a plane from the Tasks panel. The interface then switches to the [Sketcher Workbench](Sketcher_Workbench.md) in sketch editing mode.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edit sketch](Sketcher_EditSketch.md): Edit the selected Sketch.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Map sketch to face](Sketcher_MapSketch.md): Maps a sketch to a previously selected plane or a face of the active body.

### Инструменты для моделирования Детали 

#### Инструменты создания опорных элементов 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Создать опорную точку](PartDesign_Point/ru.md): создает опорную точку в активном теле.

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Создать опорную линию](PartDesign_Line/ru.md): создает опорную линию в активном теле.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Создать опорную плоскость](PartDesign_Plane/ru.md): создает опорную плоскость в активном теле.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Создать локальную систему координат](PartDesign_CoordinateSystem/ru.md): создает локальную систему координат прикрепленную к опорной геометрии в активном теле.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Создать связующую форму](PartDesign_ShapeBinder/ru.md): создает связующую форму в активном теле.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Создать связующую форму к подэлементу](PartDesign_SubShapeBinder/ru.md): создает связующую форму к подэлементу, например к краю или грани другого тела, сохраняя при этом относительное положение этого элемента.{{Version/ru|0.19}}

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Создать нового клона](PartDesign_Clone/ru.md): клонирует выбранное тело.

#### Инструменты добавления (наращивания) материала (Additive tools) 

Это инструменты для создания базовых элементов или добавления материала к существующему твердому телу.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [Выдавить эскиз](PartDesign_Pad/ru.md): выдавливает форму из выбранного эскиза.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Выдавить эскиз вокруг оси](PartDesign_Revolution/ru.md): создает твердое тело, вращая эскиз вокруг оси. Эскиз должен иметь замкнутый контур.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Создание переходной формы](PartDesign_AdditiveLoft/ru.md): создание переходной формы, между двумя и более переходными контурами.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Additive pipe](PartDesign_AdditivePipe.md): creates a solid by sweeping one or more sketches along an open or closed path.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Additive helix](PartDesign_AdditiveHelix.md): creates a solid by sweeping a sketch along a helix. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Create an additive primitive](PartDesign_CompPrimitiveAdditive.md): adds an additive primitive to the active body.

:\*<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Additive box](PartDesign_AdditiveBox.md): creates an additive box.

:\*<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Additive cone](PartDesign_AdditiveCone.md): creates an additive cone.

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Additive cylinder](PartDesign_AdditiveCylinder.md): creates an additive cylinder.

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Additive ellipsoid](PartDesign_AdditiveEllipsoid.md): creates an additive ellipsoid.

:\*<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Additive prism](PartDesign_AdditivePrism.md): creates an additive prism.

:\*<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Additive sphere](PartDesign_AdditiveSphere.md): creates an additive sphere.

:\*<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Additive torus](PartDesign_AdditiveTorus.md): creates an additive torus.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Additive wedge](PartDesign_AdditiveWedge.md): creates an additive wedge.

#### Инструменты вычитания (съёма) материала (Subtractive tools) 

Это инструменты для вычитания материала из существующего тела.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Вырез](PartDesign_Pocket/ru.md): создает вырез на основе выбранного эскиза.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Hole](PartDesign_Hole.md): creates a hole feature from a selected sketch. The sketch must contain one or multiple circles.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Groove](PartDesign_Groove.md): creates a groove by revolving a sketch around an axis.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [Subtractive loft](PartDesign_SubtractiveLoft.md): creates a solid shape by making a transition between two or more sketches and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Subtractive pipe](PartDesign_SubtractivePipe.md): creates a solid shape by sweeping one or more sketches along an open or closed path and subtracts it from the active body.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtractive helix](PartDesign_SubtractiveHelix.md): creates a solid shape by sweeping a sketch along a helix and subtracts it from the active body. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Create a subtractive primitive](PartDesign_CompPrimitiveSubtractive.md): adds a subtractive primitive to the active body.

:\*<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [Субтрактивный параллепипед](PartDesign_SubtractiveBox/ru.md): онтнимает заданный прямоугольный параллепипед от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [Субтрактивный конус](PartDesign_SubtractiveCone/ru.md): отнимает заданный конус от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Субтрактивный цилиндр](PartDesign_SubtractiveCylinder/ru.md): отнимает заданный цилиндр от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [Субтрактивный эллипсоид](PartDesign_SubtractiveEllipsoid/ru.md): отнимает заданный эллипсод от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Субтрактивная призма](PartDesign_SubtractivePrism/ru.md): отнимает призму от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Субтрактивная сфера](PartDesign_SubtractiveSphere/ru.md): отнимает сферу от активного тела.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Subtractive torus](PartDesign_SubtractiveTorus.md): adds a subtractive torus to the active body.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Subtractive wedge](PartDesign_SubtractiveWedge.md): adds a subtractive wedge to the active body.

#### Инструменты преобразования форм 

Это инструменты для преобразования существующих форм. Они позволят выбрать способы преобразования форм.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Симметрия](PartDesign_Mirrored/ru.md): создает один или несколько симметричных элементов.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Linear Pattern](PartDesign_LinearPattern.md): creates a linear pattern based on one or more features.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Polar Pattern](PartDesign_PolarPattern.md): creates a polar pattern of one or more features.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Create MultiTransform](PartDesign_MultiTransform.md): creates a pattern with any combination of the other transformations.

#### Инструменты для обработки граней тела 

These tools apply a treatment to the selected edges or faces.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Скругление](PartDesign_Fillet/ru.md): скругление граней активного тела.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Фаска](PartDesign_Chamfer/ru.md): снимает фаску с граней активного тела.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Draft](PartDesign_Draft.md): applies an angular draft to selected faces of the active body.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Thickness](PartDesign_Thickness.md): creates a thick shell from the active body and opens selected face(s).

### Булевы операции 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Boolean operation](PartDesign_Boolean.md): imports one or more Bodies or PartDesign Clones into the active body and applies a Boolean operation.

#### Дополнительные

Некоторые дополнительные функции в меню \"Part Design\":

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrate](PartDesign_Migrate.md): migrates files created with older FreeCAD versions. If the file is pure PartDesign feature-based, migration should succeed. If the file contains mixed Part/Part Design/Draft objects, the conversion will most likely fail.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Sprocket design wizard](PartDesign_Sprocket.md): creates a sprocket profile that can be padded. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Involute gear design wizard](PartDesign_InvoluteGear.md): creates an involute gear profile that can be padded.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Shaft design wizard](PartDesign_WizardShaft.md): Generates a shaft from a table of values and allows to analyze forces and moments. The shaft is made with a revolved sketch that can be edited.

### Инструменты из Контекстного Меню 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [Set tip](PartDesign_MoveTip.md): redefines the tip, which is the feature exposed outside of the Body.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Move object to other body](PartDesign_MoveFeature.md): moves the selected sketch, datum geometry or feature to another Body.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Move object after other object](PartDesign_MoveFeatureInTree.md): allows reordering of the Body tree by moving the selected sketch, datum geometry or feature to another position in the list of features.

#### Items shared with the Part workbench 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Appearance](Std_SetAppearance.md): determines appearance of the whole part (color transparency etc.).

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Set colors](Part_FaceColors.md): assigns colors to part faces.

### Настройки

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Preferences](PartDesign_Preferences.md): preferences available for PartDesign Tools.
-   [Fine tuning](Fine-tuning.md): some extra parameters to fine-tune PartDesign behavior.

## Учебники


<div class="mw-translate-fuzzy">

-   [Использование FreeCAD](http://help-freecad-jpg87.fr/), вебсайт, описывающий рабочий процесс проектирования механики.
-   [Создание простейшей детали с помощью PartDesign v0.17](Creating_a_simple_part_with_PartDesign/ru.md)
-   [Базовый учебник Part Design 017](Basic_Part_Design_Tutorial_017/ru.md)
-   [Учебник PartDesign Bearingholder I](PartDesign_Bearingholder_Tutorial_I/ru.md) (требует обновления)
-   [Учебник PartDesign Bearingholder II](PartDesign_Bearingholder_Tutorial_II/ru.md) (требует обновления)


</div>





 {{PartDesign Tools navi}}

[Category:Workbenches](Category:Workbenches.md)
