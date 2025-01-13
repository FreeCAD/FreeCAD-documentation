---
 TutorialInfo:u
   Topic: Product design
   Level: Advanced
   Time: 60 минут
   Author: User:DeepSOIC, User:Murdic, vocx
   FCVersion: 0.19
   Files: https://forum.freecadweb.org/viewtopic.php?f=36&t=44668 Updated: Thread for screw tutorial
---

# Thread for Screw Tutorial/ru




<div class="mw-translate-fuzzy">




</div>



## Введение

Это руководство - собрание методов моделирования наружных резьб в FreeCAD. Оно обновлялось для версии 0.19, хотя процесс существенно не менялся с версии 0.14, для которой изначально и было написано руководство. Обновленное содержание фокусируется на <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [верстаке PartDesign](PartDesign_Workbench/ru.md) для создания резьбы, но не использует <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:24px;"> [PartDesign Аддитивная спираль](PartDesign_AdditiveHelix/ru.md) так как этот инструмент был добавлен позднее.

В традиционных САПР моделирование резьбы не рекомендуется из за большой нагрузки на Геометрическое ядро и необходимости её отрисовки. В этих системах резьба и не должна быть смоделирована в 3D, так как она может быть добавлена в 2D чертеж, который отправляют на производство. Но с популяризацией аддитивного производства (3D печати), появилась необходимость в моделирование резьбы, чтобы напечатать модель какой она задумывалась. Этому и посвящено данное руководство.

Многие приемы, описанные ниже, были собраны на различных ветках форума:

-   [Gathering thread modeling techniques](https://forum.freecad.org/viewtopic.php?f=3&t=12593)
-   [Creating a thread: Unexpected results](https://forum.freecad.org/viewtopic.php?f=3&t=6506)

также можете посмотреть полезное видео:

-   [Introducing a strategy for designing a bolt without the commonly found problems.](https://forum.freecad.org/viewtopic.php?f=8&t=44259)

Держите в уме, что форма резьбы требует много памяти, и даже одна резьба может существенно увеличить размер файла, так что пользователю советуется создавать резьбу только в случае крайней необходимости.



## Способ 1. Используя утилиты и части из рабочих столов 

Используя утилиты и части, созданные другими людьми, легко и экономит время. Посмотрите раздел [Внешние верстаки](External_workbenches/ru.md) для информации о внешних инструментах.

В частности, эти три ресурса рекомендуются к установке из [Менеджера дополнений](Std_AddonMgr/ru.md):

-   [Верстак Стандартные Изделия (Fasteners)](Fasteners_Workbench/ru.md) чтобы добавлять/прикреплять крепеж к деталям. По умолчанию

резьба не отображается на винтах и гайках, но это может быть изменено в настройках.

-   [BOLTSFC Workbench](BOLTSFC_Workbench.md), чтобы размещать крепеж из библиотеки BOLTS.
-   [Верстак ПрофильРезьбы](ThreadProfile_Workbench/ru.md), чтобы создавать стандартные резьбы.

<img alt="" src=images/T13_00_Threads_fasteners.png  style="width:" height="300px;"> 
*Различные стандартные винты, вставленные с помощью Верстака Стандартных Изделий. Параметр контролирует, будет ли объект отображаться с резьбой или без.*



## Способ 2. Используя макрос (устарел) 

-   In the past, the [Macro BOLTS](Macro_BOLTS.md) was used to insert the parts from the BOLTS library. This is now deprecated. Use the [BOLTSFC Workbench](BOLTSFC_Workbench.md) instead.

-   In the past the stand-alone [Screw Maker macro](Macro_screw_maker1_2.md), by ulrich1a, was used to create individual bolts, screws, and washers. This is now deprecated. The [Fasteners workbench](Fasteners_Workbench.md), by shaise, includes the complete screw maker macro, together with a GUI to select the right component.



## Способ 3. Имитация резьбы: нет шага 

В многих ситуациях настоящая резьба не требуется, мы можем просто показать, что резьба должна быть.

Мы можем создать имитацию резьбы, вращая зубчатый профиль, или совмещая диски с коническими краями. Такую резьбу сложно отличить на глаз от настоящей. Этот способ подходит для визуального представления резьбы, однако не годится для 3D печати.

<img alt="" src=images/T13_01_Threads_comparison_fake_real.png  style="width:" height="300px;"> 
*Слева: винт с имитацией резьбы. Справа: винт с настоящей резьбой. Если 3D печать не требуется, часто достаточно имитации резьбы.*



### Вращение зубчатого профиля 

1.  Нажмите на **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Создать тело](PartDesign_Body/ru.md)**.
2.  Нажмите на **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign Создать эскиз](PartDesign_NewSketch.md)**. Select {{Value|XZ_Plane}}.
3.  Создайте эскиз с внутренним диаметром {{Value|10 мм}}, внешним диаметром близким к {{Value|12.6 мм}}, шагом {{Value|3 мм}}, количеством зубьев {{Value|8}}, и общей высотой {{Value|30 мм}}.
4.  Выберете эскиз, затем нажмите на **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Вращение](PartDesign_Revolution/ru.md)**. Выберете {{Value|Вертикальная ось эскиза}}, и нажмите кнопку **OK**.

<img alt="" src=images/T13_02_Threads_Sawtooth_sketch_profile.png  style="width:" height="300px;"> 
*Профиль используемый для вращения и имитации резьбы.*

<img alt="" src=images/T13_03_Threads_Sawtooth_revolution_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_04_Threads_Sawtooth_revolution_2.png  style="width:" height="300px;"> 
*Вид в разрезе резьбы без шага, созданной с помощью вращения зубчатого профиля, вокруг вертикальной оси.*



### Укладка дисков 

1.  Повторите первые два шага из предыдущей секции.
2.  Создайте эскиз с внутренним диаметром {{Value|10 мм}}, внешним диаметром близким к {{Value|12.6 мм}}, шагом {{Value|3 мм}}, но в этот раз создайте только один зуб зубчатого профиля.
3.  Выберете эскиз, затем нажмите на **[<img src=images/PartDesign_Revolution.svg style="width:16px"> [PartDesign Вращение](PartDesign_Revolution/ru.md)**. Выберете {{Value|Вертикальная ось эскиза}}, и нажмите кнопку **OK**.
4.  Выберете {{Value|Вращение}}, затем нажмите на **[<img src=images/PartDesign_LinearPattern.svg style="width:16px"> [PartDesign Линейный массив](PartDesign_LinearPattern/ru.md)**. Выберете {{Value|Вертикальную ось}}. Для имитации резьбы с шагом {{Value|3 мм}}, выставите значение **Длина** на {{Value|3}}, и **События** на {{Value|2}}, затем нажмите **OK**. Так вы создадите два диска, один на другом.
5.  Вы можете добавить больше дисков, увеличив значение **События** в линейной зависимости от**Длина**, которая будет полной диной имитации резьбы.

Параметры **Длина** и **События** связанны. Если длина слишком велика, а количество событий недостаточно, диски не соединятся и создать тело не удастся, так полученный объект должен быть [сплошным телом](PartDesign_Body/ru.md). В примере, чтобы получить высоту {{Value|30 мм}}, установите параметр **Длина** на {{Value|27 мм}} а параметр **События** на {{Value|10}}.

Если хотите, вы можете добавить **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Аддитивный цилиндр](PartDesign_AdditiveCylinder/ru.md)** с диаметром, равным внутреннему диаметру дисков, и высотой, равной высоте резьбы. Эта операция объединит все диски в одно тело, и гарантирует, что они не рассоединятся.

<img alt="" src=images/T13_05_Threads_Stacked_discs_sketch.png  style="width:" height="300px;"> 
*Профиль, который использовался для создания диска, с помощью которого имитировалась резьба.*

<img alt="" src=images/T13_06_Threads_Stacked_discs_1.png  style="width:" height="300px;"> <img alt="" src=images/T13_07_Threads_Stacked_discs_2.png  style="width:" height="282px;"> 
*Слева: один диск, созданный вращением. Справа: несколько дисков, собранные в линейный массив в направление Z, имитирующие резьбу.*



## Способ 4. Вращение вертикального профиля 



### Верстак PartDesign 

Настоящая резьба состоит из профиля вращаемого по спиральному пути.

1.  В <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстаке Part](Part_Workbench/ru.md), нажмите на **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Создать примитивы](Part_Primitives/ru.md)** чтобы создать **[<img src=images/Part_Helix.svg style="width:16px"> [Part Спираль](Part_Helix.md)**. Задайте необходимое значение для **Шаг** {{Value|3 мм}}, **Высота** {{Value|23 мм}}, и **Радиус** {{Value|10 мм}}.
2.  Переместитесь в <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Верстак PartDesign](PartDesign_Workbench/ru.md), и нажмите на **[<img src=images/PartDesign_Body.svg style="width:16px"> [PartDesign Создать тело](PartDesign_Body.md)**.
3.  Click on **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign создать эскиз](PartDesign_NewSketch/ru.md)**. Выберете {{Value|XZ_Plane}}.
4.  Создайте эскиз необходимого для выступа резьбы, обычно треугольной формы. В нашем случае высота будет {{Value|2.9 мм}}, немного меньше чем шаг спирали {{Value|3.0 мм}}. Профиль не должен пересекаться сам с собой, ни при каких обстоятельствах, эскиз, использованный для укладки дисков не подойдет.
5.  Выберете эскиз, нажмите на **[<img src=images/PartDesign_AdditivePipe.svg style="width:16px"> [PartDesign Аддитивный профиль по траектории](PartDesign_AdditivePipe/ru.md)**. В меню **путь для выдавливания вдоль него**, нажмите на **Объект**, и выберите спираль, которую создал ранее. Затем измените **Режим ориентации** на {{Value|Френе}} для того того, чтобы профиль не изгибался во время вращения; Затем нажмите **OK**.
6.  В диалоговом окне выберите {{Value|Создать перекрестную ссылку}}.
7.  Создалась спиральная катушка, с полостью внутри.
8.  Нажмите на **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Аддитивный цилиндр](PartDesign_AdditiveCylinder/ru.md)** с подходящем значением **Радиус** {{Value|10 мм}} и **Высота** {{Value|29.9 мм}} чтобы он касался винтовой катушкой и автоматически соединился с ней.
9.  Дополнительные булевы операции необходимы, чтобы сравнять резкие концы катушки. К примеру, вы можете использовать аддитивные операции, для формирования головки и наконечника винта.

<img alt="" src=images/T13_08_Threads_Helical_thread_profile.png  style="width:" height="300px;"> <img alt="" src=images/T13_09_Threads_Helical_thread_path.png  style="width:" height="300px;"> 
*Слева: Профиль для спиральной резьбы. Справа: Спиральный путь, который будет использован для создания катушки*

<img alt="" src=images/T13_10_Threads_Helical_thread_coil.png  style="width:" height="300px;"> <img alt="" src=images/T13_11_Threads_Helical_thread_coil_sliced.png  style="width:" height="300px;"> 
*Слева: катушка, образованная вращением профиля резьбы по винтовой траектории. Справа: вид катушки, полученной вращением, в разрезе.*

<img alt="" src=images/T13_12_Threads_Helical_thread_cylinder.png  style="width:" height="300px;"> <img alt="" src=images/T13_13_Threads_Helical_thread_finished.png  style="width:" height="300px;"> 
*Слева: Винтообразная катушка, соединенная с центральным цилиндром, для создания тела винта. Справа: больше операций, головка и наконечник были добавленный для улучшения формы винта.*



### Верстак Part 

Этот процесс также может быть проделан с использованием инструментов [Верстака Part](Part_Workbench.md)

1.  В <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстаке Part](Part_Workbench/ru.md), нажмите на **[<img src=images/Part_Primitives.svg style="width:16px"> [Part Создать примитивы...](Part_Primitives/ru.md)** чтобы создать **[<img src=images/Part_Helix.svg style="width:16px"> [Part Спираль](Part_Helix/ru.md)**. Задайте значения **Шаг** {{Value|3 мм}}, **Высота** {{Value|23 мм}}, и **Радиус** {{Value|10 мм}}.
2.  В этом случае вам не нужно **[<img src=images/PartDesign_Body.svg style="width:16px">**. Перейдите на <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Верстак Sketcher](Sketcher_Workbench/ru.md), затем нажмите на **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Sketcher Создать эскиз](Sketcher_NewSketch.md)**, и выберете плоскость XZ.
3.  Затем вернитесь в <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак Part](Part_Workbench.md), и воспользуйтесь инструментом **[<img src=images/Part_Sweep.svg style="width:16px"> [Part Профиль по траектории](Part_Sweep/ru.md)**.
4.  Выберете подходящий эскиз из **Доступные профили** и нажмите на стрелочку, чтобы переместить его в **Выбранные профили**.
5.  Нажмите на **Траектории построения**, и выберете все грани спирали с помощью [3D вида](3D_view.md). Нажмите на кнопку **Готово**.
6.  убедитесь, что чек боксы {{CheckBox|TRUE|Создать твёрдое тело}} и {{CheckBox|TRUE|Френе}} активны. Получение тела необходимо, для использования [Part Булевы операции](Part_Boolean.md) с получившейся катушкой, в противном случае создадутся только поверхности, ограничивающие катушку.
7.  Нажмите на **OK** чтобы выйти из меню и создать катушку.

Теперь вы можете добавить другие примитивы, к примеру **[<img src=images/Part_Cylinder.svg style="width:16px"> [Part Цилиндр](Part_Cylinder/ru.md)**, или другие, чтобы применить **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Объединение](Part_Fuse/ru_.md)** или **[<img src=images/Part_Cut.svg style="width:16px"> [Part Обрезать](Part_Cut/ru.md)** чтобы закончить создание винта.

<img alt="" src=images/T13_14_Threads_components.png  style="width:" height="300px;"> 
*Creating a thread coil by sweeping a vertical profile, (1) the [sketch profile](sketch.md), (2) the [helical](Part_Helix.md) sweeping path, and (3) the result of the [sweep](Part_Sweep.md).*



### Ключи к успеху 

-    **Rule 1.**When the profile sweeps the helix, the resulting solid coil must not touch or self-intersect as it will be an invalid solid. This holds for the profile moving along the helix, as well as intersections in the center of the helix. Attempts to do boolean operations with it (fuse or cut) are very likely to fail. Check the quality of the coil with **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part CheckGeometry](Part_CheckGeometry.md)**; if self-intersections are reported, you must increase the pitch of the helix.

<img alt="" src=images/T13_15_Threads_self_intersection.png  style="width:" height="300px;"> <img alt="" src=images/T13_16_Threads_no_self_intersections_OK.png  style="width:" height="300px;"> 
*Left: invalid sweep generated by using a very small pitch of the helix compared to the height of the triangular profile. Right: pitch that is sufficiently large and doesn't cause self-intersections.*

-    **Rule 2.**When a cylinder is added to a coil to form the main shaft of a screw, the cylinder must not be tangent to the coil profile. That is, the cylinder must not have the same radius as the inner radius of the thread, as this is very likely to fail a fuse operation. In general, avoid geometry coincident to elements of the sweep, such as tangent faces, or edges tangent to faces they are not connected to. In order to produce a good boolean union, the swept coil and the cylinder must intersect. Check the quality of the fusion with **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part CheckGeometry](Part_CheckGeometry.md)**; if coplanar faces are reported increase the cylinder\'s radius by a small amount.

-   If the coil and the cylinder are tangent, even if the first fusion succeeds, it may fail in subsequent boolean operations with a third solid.

-   This is a limitation of the OpenCASCADE Technology (OCCT) kernel; in general, it doesn\'t handle well operations between coplanar surfaces.

<img alt="" src=images/T13_17_Threads_tangent_faces.png  style="width:" height="300px;"> <img alt="" src=images/T13_18_Threads_no_tangent_faces_OK.png  style="width:" height="300px;"> 
*Left: the solid cylinder is tangent to the inner radius of the thread; this may result in an invalid boolean union. Right: the cylinder has a slightly larger radius, so the two solids intersect; this will result in a valid fusion.*

-    **Rule 3.**The inner cylinder has a seamline. You should avoid placing the start of the helix along that seam. Either turn the helix or the cylinder by some degrees.

-    **Tip 1.**The radius of the helical path does not matter, unless the helix is tapered. All that matters is the pitch and the height of the helix. This means that you can use a single **[<img src=images/Part_Helix.svg style="width:16px"> [Part Helix](Part_Helix.md)** to generate several threads with equal pitch. What determines the position of the resulting coil is the position of the profile [sketch](Sketch.md).

-    **Tip 2.**Keep the thread short, that is, with a low number of turns. Long threads tend to fail with boolean operations. If you need to add many turns, consider creating first a short thread, and then using **[<img src=images/Draft_OrthoArray.svg style="width:16px"> [Draft OrthoArray](Draft_OrthoArray.md)** to duplicate the same pattern several times.

-    **Tip 3.**For 3D visualization and 3D printing it may be okay to leave the cylinder and the thread unfused, that is, with intersections between the two solids. Reducing the amount the boolean operations results in less memory consumption and smaller files.

### Pros and cons 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Easy to understand.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> Very natural way of defining a thread profile.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> No problems with meshing of the resulting object, unlike method 5.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Due to invalidity of self-intersecting sweeps, it is next to impossible to generate a thread with no gap between each tooth, that is, with no straight cylindrical face at the inner sides of the thread.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Boolean operations are required to obtain a single contiguous solid. Boolean operations take a relatively long time to calculate, and fail often.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> Threads with a high number of turns are problematic.

## Method 5. Sweeping a horizontal profile 

### General

The idea is to sweep a horizontal cross-section of the thread along a helix. The main problem here is figuring out the profile to use to obtain such thread.

<img alt="" src=images/thread-by-horz-profile.png  style="width:600px;">

If one uses a circle as a horizontal profile (the circle has to be placed off the origin, that offset defines the depth of the thread), the thread profile will be sinusoidal.

To obtain a standard sawtooth profile, a pair of mirrored archimedean spirals need to be fused into a wire. The resulting figure is a heart shape, which becomes barely distinguishable from a circle when the depth of the thread is small compared to its diameter, this is why a \"thick\" thread is shown on the picture above.

### Generating the profile 

Figuring out the horizontal profile to obtain a certain vertical profile is not easy. For simple cases like triangular or trapezoidal it can be constructed manually. Alternatively, it can be constructed by creating a short thread with method 4, and getting a slice of it by doing a [Part Common](Part_Common.md) between a horizontal plane face and the thread.

#### Profile for triangular thread 

1.  First create an Archimedian spiral in the XY plane.
    1.  Set the number of turns to 0.5.
    2.  Set the radius to the inner radius of the thread, the outer radius will be this plus the depth of the cut.
    3.  Set the growth to double the depth of cut of the thread.
2.  [Part Mirror](Part_Mirror.md) the spiral against the XY plane
3.  [Part Fuse](Part_Fuse.md) the spiral and the mirror to obtain a closed wire, shaped like a heart.

#### Profile for arbitrary cross-section 

<img alt="" src=images/thread-by-horz-profile-profileMake.png  style="width:1000px;">

1.  Make a vertical cut profile. Make sure that the height of the sketch matches the pitch of the thread you need.
2.  Make a helix1 with height identical to the pitch and the pitch identical to the thread pitch, and a helix radius of 0.42\*nominal diameter of the thread.
3.  Sweep the cut profile along the helix1. Set {{CheckBox|TRUE|Create solid}} and {{CheckBox|TRUE|Frenet}}.
4.  Make a circle with nominal radius of the thread in the XY plane.
5.  Make a face from the circle. This can be done with **[<img src=images/Part_Builder.svg style="width:16px"> [Part Builder](Part_Builder.md)** or **[<img src=images/Draft_Upgrade.svg style="width:16px"> [Draft Upgrade](Draft_Upgrade.md)**, then set **MakeFace** to `True`.
6.  Cut the face with the sweep profile.
7.  Make a **[<img src=images/Draft_Clone.svg style="width:16px"> [Draft Clone](Draft_Clone.md)** from the cut.
8.  Use **[<img src=images/Draft_Downgrade.svg style="width:16px"> [Draft Downgrade](Draft_Downgrade.md)** on the clone in order to get a wire. This wire is the horizontal profile needed for this method.
9.  Make a helix with radius of nominal radius of the thread and a pitch of the thread and the height of the needed thread.
10. Sweep the wire along the helix. Set {{CheckBox|TRUE|Create solid}} and {{CheckBox|TRUE|Frenet}}.
11. You are done.

The step-by-step guide was taken from this [forum post by Ulrich1a](http://forum.freecad.org/viewtopic.php?f=3&t=6506#p52558) (\"Creating a thread: Unexpected results\"), slightly modified.

The steps are also shown in action on [this video by Gaurav Prabhudesai](http://www.youtube.com/watch?v=fxKxSOGbDYs) (\"FreeCAD : How to make threads\").

### Pros and cons 

-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> a ready-to-use thread-on-a-rod solid shape is created by the sweep directly.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> fewer or even no boolean operations are required, so generation speed is very high compared to Method 4.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> thread ends are nicely cut straight away
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> long threads are not a problem, unless a boolean operation is needed. Otherwise, it is not going to be much better than Method 4.
-   <img alt="" src=images/Edit_OK.svg  style="width:24px;"> threads without a gap are not a problem.

-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> defining thread profile is complicated.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> using the standard mesher with a thread created in this way generates ugly meshes, which can lead to problems. Other meshers are better, for example, Mefisto seems to give the best results.
-   <img alt="" src=images/Edit_Cancel.svg  style="width:24px;"> large memory footprint according to [Gathering thread modeling techniques](http://forum.freecad.org/viewtopic.php?f=3&t=12593&start=10#p101197).

## Method 6. Lofting between helical extruded faces 

### General 

Helical splines will extrude coaxial faces that are able to be lofted, while FreeCAD\'s parametric helix won\'t. It takes two helical splines to define a thread. Those two can be scaled from a library spline, then located and extruded appropriately to get the form right.

FreeCAD\'s parametric helixes aren\'t truly helical, but helical b-splines aren\'t difficult to lay out. One manual method is to array dodecagons (12-sided polygons) with 5mm radius/10mm diameter at 1/12mm (0.08333.mm) z intervals and trace splines from vertex to vertex in ascending and rotating order, and to consider doing it once with, say, 10 turns, so that that spline can be re-used as a library file for import and reuse. It\'s convenient to use 10mm diameter/1mm pitch for ease of scaling. If you are doing it manually, drawing a Dwire and then converting it to a b-spline is easier than drawing a spline. Dwires don\'t have curvature computed while being drawn, so they follow the cursor and snap more obediently.

Once the splines are scaled to the right size and located so that the loft will have the right included angle between the thread flanks, they\'re extruded along their axis, a pitch length\'s worth for the inner spline, the outer pitch/8.

<img alt="" src=images/splineextrudeloft.png  style="width:912px;">

ISO and other threads have relieved, ie flat, inner and outer edges rather than sharp, which suits FreeCAD users with this method, because we can loft to the helical face at the nominal fastener size, while an inner face can\'t be lofted to an outer edge spline because a face is a closed profile, a spline is open. ISO standard says the nominal size of external threads have a face width pitch/8. The picture shows how the geometry is arranged, and the helical faces that result. Then, loft between the faces, and then a cylinder that gives the inner helical face, which ISO puts at pitch/4 width, is added to the threads.

![761PX](images/Threadform.PNG )

This method produces reliable solids that boolean properly. While it doesn\'t produce \"parametric\" screw threads in standard sizes in the sense of having simple access to form by fastener size, it\'s an easy way of producing an accurate library for reuse, and models of specialised forms like ACME, or Archimedian screws, are also uncomplicated as one-offs.


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > Thread for Screw Tutorial/ru
