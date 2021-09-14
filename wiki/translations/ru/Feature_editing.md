# Feature editing/ru

 {{TOCright}}

## Введение

This page explains the way the <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [PartDesign Workbench](PartDesign_Workbench.md) is intended to be used starting with FreeCAD 0.17.


<div class="mw-translate-fuzzy">

В то время как [верстак Part](Part_Workbench/ru.md) и прочие верстаки FreeCAD конструируют модели комбинированием форм, верстак PartDesign использует **features**. [Feature](https://en.wikipedia.org/wiki/Feature_recognition) это операция, модифицирующая форму модели.


</div>

## Feature editing methodology 

Первая feature обычно называется **base feature**. По мере добавления features к модели, каждая feature берёт форму предыдущей и добавляет или убирает matter, создавая последовательность зависимостей от одной feature к другой. Как результат, эта методология имитирует общие производственные процессы: блок обрезается по одной стороне, затем по другой, добавляются отверстия, скругления и так далее.

Все features перечислены последовательно в древе модели и могут редактироваться в любое время, где последняя feature внизу представляет итоговую деталь.

Возможности могут быть отсортированы по различным категориям:

-   **Profile-based**: эти features основываются на профиле для определения формы добавляемого или удаляемого материала. Профиль может быть эскизом, плоской гранью существующей геометрии (профиль будет выделен из кромки), объект ShapeBinder или Draft, который был включён в активное Тело.

-   **Additive**: добавляют материал к существующей модели. Аддитивные features показываются жёлтыми иконками.

-   **Subtractive**: убирают материал из существующей модели. Субтрактивные features показывают красные и голубые иконки.

-   **Primitive-based**: базирующиеся на геометрических примитивах (куб, цилиндр, конус, тор...). Они могут быть аддитивными или субтрактивными.

-   **Transformation features**: они применяют трансформацию к существующим features (отражение, линейный или полярный паттерн, мультитрансформация).

-   **Dress-up**: features, которые пликладывают обработку к фаскам или граням, такие как скругления, фаски, или drafts.

-   **Procedural**: могут быть отнесены к features, которые не базируются на эскизировании, вроде трансформаций и dress-up features.

## Твёрдое тело 


<div class="mw-translate-fuzzy">

Для работы PartDesign сначала создаётся <img alt="" src=images/PartDesign_Body.png  style="width:24px;"> **[тело](PartDesign_Body/ru.md)**. Тело в PartDesign это контейнер, группирующий последовательность свойств, формирующих единое монолитное тело.


</div>

![](images/PartDesign_Body_tree.png )


<div class="mw-translate-fuzzy">

Что значит **единое монолитное тело**? Это элемент вроде литья или чего-то выточенного из единого блока металла. Если он включает гвозди, винты, клей или пайку, это не **единое монолитное тело**. Например, деревянный стул изготавливается из нескольких тел, по одному для каждого из компонентов (ножки, планки, сиденья и так далее).


</div>

В документе FreeCAD могут быть создано несколько тел, они могут быть скомбинированы для формирования единого монолитного твёрдого тела.

Only one body can be active in a document. The active body gets the new created features. A body can be activated or deactivated by double clicking on it. An activated body is highlighted in light blue. The highlighting color can be set in the preferences under Display/Colors/Active container since version 0.18.


<div class="mw-translate-fuzzy">

Когда модель требует несколько тел, как в предыдущем примере деревянного стула, может быть использован [Part container](Std_Part/ru.md) общего назначения для их группировки и совместного их перемещения как единого целого.


</div>

### Body visibility management 

По умолчанию тело (Body) представляется извне самым последним элементом. Этот элемент определяется по умолчанию как верхушка. Хорошая аналогия - выражение *верхушка айсберга*: только верхушка видна над водой, большая часть объёма айсберга (остальные элементы) скрыты. Когда новые feature добавляются к телу, видимость предыдущих отключается, и верхушкой становятся новые.


<div class="mw-translate-fuzzy">

Только одна feature может быть видима одновременно. Возможно переключение видимости любой feature в теле, выбрав её в древе Модели и нажав пробел, получив в результате откат в истории создания тела.


</div>

### Body Origin 

The body has an Origin which consists of reference planes (XY, XZ, YZ) and axes (X, Y, Z) that can be used by sketches and features. Sketches can be attached to Origin planes, and they no longer need to be mapped to planar faces for features based on them to be added or subtracted from the model.

### Перемещение и реорганизация объектов 

It is possible to temporarily redefine the tip to a feature in the middle of the Body tree to insert new objects (features, sketches or datum geometry). It is also possible to reorder features under a Body, or to move them to a different Body. Select the object and right-click to get a contextual menu that will offer both options. The operation may be prevented if the object has dependencies in the source Body, such as being attached to a face. To move a sketch to another Body, it should not contain links to external geometry.

### Difference with other CAD systems 

A fundamental difference between FreeCAD and other programs, like Catia, is that FreeCAD doesn\'t allow you to have many disconnected solids in the same <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> **[PartDesign Body](PartDesign_Body.md)**. That is, a new feature should always be built on top of the previous one. Or said in a different way, the newer feature should \"touch\" the previous feature, so that both features are fused together and become a single solid. You cannot have \"floating\" solids.

<img alt="" src=images/PartDesign_Body_non-contiguous.png  style="width:550px;">


*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature so that it is fused to it, and becomes a single contiguous solid.*

## Datum geometry 

Datum geometry consists of custom planes, lines, points or externally linked shapes. They can be created for use as reference by sketches and features. There is a multitude of attachment possibilities for datum objects.

In some CAD systems you can define a datum plane that is offset from the previous body and you can create a disconnected solid. So, placing a lot of datum planes, and building objects on them is okay and won\'t cause an error. Typically, you would eventually adjust the planes to their final positions, so that the individual objects are fused together.

In FreeCAD, as mentioned in the previous section, disconnected solids are **NOT** allowed, so a sketch on a datum plane that would create a non-contiguous solid will fail.

In FreeCAD, datum planes make sense if you are placing sketches (and padding, pocketing, etc.) in non-standard orientations, that is, in planes offset or rotated around the three main axes. Since sketches can also be placed in non-standard orientations in the same way as datum planes, often there is no need to use datum planes.

Datum planes also make sense if there will be more than one sketch in the same non-standard orientation. In this case a datum plane can be used and the orientation only needs to be adjusted for the datum plane to adjust all associated sketches and the features created from the sketches.

Both sketches and datum planes should be attached to base planes. Referencing generated geometry (geometry that is the result of a feature creating operation, for example a pad or pocket) should be avoided since faces and edges get renamed and renumbered and the references no longer refer to the same thing. This is called topological instability and is due the way FreeCAD uses some external geometric libraries. Hopefully this will be improved in the future. (See Advice for creating stable models below).

Even if not used for supporting sketches, datum objects are still helpful as visual indicators, to draw attention to important features or distances in the modelling process. (Though, simply adding geometry to a sketch also provides similar visual feedback.)

<img alt="" src=images/PartDesign_Body_non-contiguous_slanted.png  style="width:550px;">


*Difference between Catia and FreeCAD. Left: Catia allows disconnected bodies from the previous features of the body. In FreeCAD this causes an error; Right: the newer feature should always contact or intersect the previous feature, so that it is fused to it, and becomes a single contiguous solid. In this example, the new solid is based on a datum plane that is rotated around the Y axis.*

## Cross-referencing 

It is possible to cross-reference elements from a body in another body via datums. For example the datum shape binder allows to copy over faces from a body as reference in another one. This should make it easy to build a box with fitting cover in two different bodies. FreeCAD helps you to avoid accidentally linking to other bodies by asking for confirmation of your intent.

## Attachment

Object attachment is not a specific PartDesign tool, but rather a Part utility introduced in v0.17 that can be found in the Part menu. It is heavily used in the PartDesign workbench to attach sketches and reference geometry to the standard planes and axes of the Body. Very extensive ways of creating datum points, lines and planes are available. Optional attachment offset parameters make this tool very versatile.

More info can be found in the [Attachment](Part_EditAttachment.md) page and the [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md).

## Advice for creating stable models 

The idea of parametric modeling implies that you can change the values of certain parameters and subsequent steps are changed according to the new values. However, when severe changes are made, the model can break due to the [topological naming problem](topological_naming_problem.md) that is still unresolved in FreeCAD. Breakage can be minimized when you respect the following design principles:

-   Avoid attaching sketches and datum objects to generated geometry of the model. (Generated geometry is any face or edge created as a result of a pad, pocket, etc..)
-   Place your sketches on standard coordinate planes, or on custom datum planes attached to standard planes.
    -   Sketches attached to basic coordinate planes/axes or to datum planes attached to coordinate planes/axes, will not get unexpectedly reattached to a different reference.
-   When creating datum geometry, do not attach it to generated geometry
    -   Attach it to standard planes/axes and/or sketches or datum objects which use attachment offsets to standard planes/axes.
-   Use a \"master sketch\". Since a master sketch is done before rest of the model, it only references the coordinate planes/axes.
    -   A master sketch should be as simple as possible, containing basic geometric elements of your model.
    -   Master sketch elements can be referenced when modelling subsequent features.
    -   A master sketch can be the first sketch in the Body, or outside the body completely
    -   A master sketch can be referenced as external geometry or via a ShapeBinder.
-   Don\'t create ShapeBinders from generated geometry
-   Keep in mind that ShapeBinders can be an issue when geometry is deleted from the sketch it is based on.
-   If you inevitably have to reference an intermediate feature, e.g. the result of a thickness operation
    -   Use the first reference possible in the list of subsequent features where the referenced geometric element occurs.
    -   If you take an early feature as reference, all changes to intermediate steps won\'t break your model.
    -   Try to reference a sketch or sketch geometry rather than generated geometry.
-   Use *dress ups*, like fillets and chamfers, as late in the feature tree as possible
-   Note, using spreadsheets, dynamic data, master sketches, etc. generally produce more parametric models and help avoid the topological naming issue.

## Body building workflow 

There are several workflows that are possible with the [PartDesign Workbench](PartDesign_Workbench.md). What should always be noticed is that all the features created inside a [PartDesign Body](PartDesign_Body.md) will be fused together to obtain the final object.

### Different sketches 

Sketches need to be supported by a plane. This plane can be one of the main planes (XY, XZ, or YZ) defined by the Origin of the Body. A sketch is either extruded into a positive solid (additive), with a tool like <img alt="" src=images/PartDesign_Pad.svg  style="width:24px;"> [PartDesign Pad](PartDesign_Pad.md), or into a negative solid (subtractive), with a tool like <img alt="" src=images/PartDesign_Pocket.svg  style="width:24px;"> [PartDesign Pocket](PartDesign_Pocket.md). The first adds volume to the final shape of the body, while the latter cuts volume from the final shape. Any number of sketches and partial solids can be created in this way; the final shape (tip) is the result of fusing these operations together. Naturally, the Body can\'t consist of only subtractive operations, as the final shape should be a solid with a positive, non-zero volume.

<img alt="" src=images/PartDesign_workflow_1.svg  style="width:600px;">

### Sequential features 

Sketches can be supported by the faces of previous solid operations. This may be necessary if you need to access a face that is only available after a certain feature has been created. However, this workflow isn\'t recommended since, if the original feature is modified, the following features in the sequence may break. This is the [topological naming problem](topological_naming_problem.md).

<img alt="" src=images/PartDesign_workflow_2.svg  style="width:600px;">

### Use of datum planes for support 

Datum planes are useful to support the sketches. These auxiliary planes should be attached to the base planes of the body.

\'\'Note: In many cases, a sketch attached to a base plane with attachment offsets can accomplish the same function. Datums are particularly useful when multiple sketches or other constructs will use the datum. This means all changes to the datum will be apply to attached sketches, etc. Adding a single sketch to a datum, rather than using attachment offsets in the sketch properties, is an extra step and is essentially redundant. \'\'

As with sketches, it is possible to attach Datum planes to generated geometry (edges, faces of previously created solids), ***but this is not recommended*** since it can cause the topological naming problem.

In addition, a <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:24px;"> [PartDesign ShapeBinder](PartDesign_ShapeBinder.md) can be used to import external geometry into the body to serve as reference; then sketches can be attached to this auxiliary body, either using datum planes or not.

*Again, the ShapeBinder should be based on Sketches from the previous body, not generated geometry.*

Using datum objects is often the best way to produce stable models, when used with base planes and attachment offsets, although it requires a bit more work from the user. For details about basic attachment see: [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md) *Note: while this tutorial talks about sketches, datum attachment is done in similar fashion.*

## Tutorials

The [tutorials](Tutorials.md) page provides some examples of using the [feature editing](feature_editing.md) method of the <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign Workbench](PartDesign_Workbench.md).

-   [Creating a simple part with PartDesign](Creating_a_simple_part_with_PartDesign.md)
-   [Basic Part Design Tutorial](Basic_Part_Design_Tutorial.md)
-   [Basic Attachment Tutorial](Basic_Attachment_Tutorial.md)

## Related

-   [Constructive solid geometry](Constructive_solid_geometry.md)

<img alt="" src=images/PartDesign_workflow_3.svg  style="width:600px;">


{{PartDesign Tools navi

}} 

[Category:Common Questions](Category:Common_Questions.md)
