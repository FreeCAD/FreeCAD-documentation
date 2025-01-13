# Manual:Preparing models for 3D printing/ru
<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}


<div class="mw-translate-fuzzy">

Одна из основных применений FreeCAD - создание реальных объектов. Они могут быть спроектированы в нём, а затем созданы в реальности различными способами, передачей другим людям, кто изготовит их, или, всё чаще и чаще, прямой посылкой на [3D-принтер](https://ru.wikipedia.org/wiki/3D-принтер) или [фрезерованием на станке с ЧПУ](https://ru.wikipedia.org/wiki/Фрезерование). Эта статья покажет, как приготовить Ваши модели для отправки на подобные устройства.


</div>


<div class="mw-translate-fuzzy">

Если Вы были внимательны во время моделирования, большинства сложностей, с которыми Вы могли бы встретиться при печати Ваших моделей Вы уже избежали. Они включают следующее:


</div>


<div class="mw-translate-fuzzy">

-   Убедитесь, что Ваш трёхмерных объект представляет собой **твёрдое тело**. Трёхмерные модели должны быть телами так же как объекты реального мира. Мы видели в предыдущих главах, что FreeCAD сильно помогает в этом вопросе, и что [верстак PartDesign](PartDesign_Workbench/ru.md) предупредит Вас, если производимая Вами операция помешает вашей модели оставаться твердотельной. [Верстак Part](Part_Workbench/ru.md) так же содержит инструмент <img alt="" src=images/Part_CheckGeometry.svg  style="width:16px;"> [Проверка геометрии](Part_CheckGeometry/ru.md), полезный для дальнейших проверок возможных дефектов.
-   Убедитесь насчёт **размерности** ваших объектов. Один миллиметр должен быть одним миллиметром в реальной жизни. Все размеры важны.
-   Управление **деградацией**. Никакие системы трёхмерной печати или фрезерования ЧПУ не воспринимают файлы FreeCAD напрямую. Большинство из них понимают только машинный язык, называемый [G-код](https://ru.wikipedia.org/wiki/G-код). У G-кода имеется несколько различных диалектов, каждая машина или поставщик обычно имеют свой собственный. Преобразование Вашей модели в G-код может быть лёгким и автоматическим, но Вы можете так же делать это вручную, с полным контролем выхода. В любом случае, некоторая потеря качества Вашей модели неизбежна. При объёмной печати Вы должны всегда проверять, что потеря качества остаётся в пределах допустимого.


</div>

-   **Confirming the Accuracy of Dimensions**: Precision is critical---what you design in FreeCAD will translate directly to real-world measurements. A millimeter in FreeCAD is a millimeter in the physical object, so each dimension must be carefully considered and verified to ensure accuracy.

-   **Managing Degradation**: It\'s important to remember that no 3D printer or CNC mill can directly process FreeCAD files. These machines use G-Code, a machine language with various dialects depending on the machine or vendor. The process of converting your model into G-Code can often be done automatically through slicer software, but you also have the option to do it manually for greater control. However, during this conversion, some loss of detail or quality is inevitable, particularly when converting the model to a mesh format for printing. You must ensure that this degradation remains within acceptable limits and doesn't affect the functionality or appearance of your final object.

-   **Export Format Compatibility**: For 3D printing, STL is the most commonly used format, but it inherently converts your model into a mesh of triangles, which can result in some loss of detail. It's essential to choose the right resolution when exporting to STL, balancing between detail retention and file size. Similarly, for CNC machining, formats like STEP or IGES are preferable as they maintain the original geometric integrity of the design better than STL. Choosing the right format ensures that the conversion to G-Code remains accurate.

-   **Mesh Analysis and Calibration**: Before exporting your model to a slicer or CNC toolpath generator, it's advisable to run a mesh analysis using FreeCAD's [Mesh Workbench](Mesh_Workbench.md) to detect irregularities, non-manifold edges, or other mesh issues that might complicate the manufacturing process. Additionally, even with a perfect model, make sure your 3D printer or CNC machine is properly calibrated (e.g., for bed leveling, stepper motor settings, or extruder configuration) to avoid quality problems in the final product.

In the following sections, we\'ll assume that you\'ve already taken care of creating solid models with the correct dimensions. Our focus will now shift to managing the conversion process to G-Code, ensuring that your model maintains the necessary quality for 3D printing or CNC machining. By addressing these considerations, you\'ll be better equipped to produce successful physical objects directly from your FreeCAD models.



### Экспорт в слайсеры 


<div class="mw-translate-fuzzy">

Это техника, чаще всего используемая для трёхмерной печати. Объёмный объект экспортируется в другую программу (слайсер), который создаёт из объекта G-код, нарезая (to slice) его на тонкие слои (откуда и имя), которые повторяют будущие движения объёмного принтера. Поскольку многие из этих принтеров домашнего изготовления, обычно между ними есть небольшие отличия. Эти программы обычно предлагают продвинутые возможности конфигурации, позволяющие настроить выход в точности под особенности вашего принтера.


</div>


<div class="mw-translate-fuzzy">

Реальная объёмная печать, однако, слишком обширная тема для этого руководства. Но мы посмотрим, как экспортировать и использовать слайсеры для проверки корректности выхода.


</div>

Slicers often include additional insights, such as estimating print time, material usage, and cost based on the filament or resin being used. This allows you to make informed decisions about the printing process and tweak settings for efficiency or material conservation. Although the deeper intricacies of 3D printing---such as machine calibration, material selection, and post-processing---are beyond the scope of this guide, we will focus on how to properly export your FreeCAD model and use slicer software to ensure the output is correct and optimized for your specific printer



### Преобразование объектов в сетки 


<div class="mw-translate-fuzzy">

Ни один из слайсеров не использует твердотельную геометрию, создаваемую FreeCAD, напрямую. Так что сначала нам нужно конвертировать объекты, которые мы хотим печатать, в [сетки](https://ru.wikipedia.org/wiki/Полигональная_сетка), которые может открыть слайсер. По счастью, в то время как конвертация сетки в твердое тело - операция сложная, обратная ей операция преобразования в сетку очень прямолинейная. Всё, о чём мы должны заботиться, это об упомянутой выше деградации. Нам следует убедиться, что деградация остаётся в приемлемых рамках.


</div>


<div class="mw-translate-fuzzy">

Вся обработка сеток в FreeCAD производится специальным верстаком [Mesh](Mesh_Workbench/ru.md). Этот верстак содержит, кроме наиболее важных инструментов для конвертации между объектами Part и Mesh, несколько утилит для анализа и исправления сеток. Хотя работа с сетками не главная для FreeCAD, при работе с трёхмерном моделированием часто требуется обрабатывать сетки, поскольку они очень широко распространены среди других приложений. Этот верстак обеспечивает их полную поддержку в FreeCAD.


</div>


<div class="mw-translate-fuzzy">

-   Давайте конвертируем один из объектов, которые мы смоделировали в предыдущей главе, вроде кирпичика Lego (который может быть загружен в конце предыдущей главы).
-   Откроем файл FreeCAD с кирпичиком Lego.
-   Переключимся на [верстак Mesh](Mesh_Workbench/ru.md)
-   Выделим кирпичик Lego
-   Выберем в меню **Сетки -\> Создайте сетку из фигуры**
-   Откроется панель задач с несколькими опциями. Некоторые дополнительные механизмы создания сеток (Mefisto или Netgen) могут быть недоступны, в зависимости от того, как скомпилирована Ваша версия FreeCAD. Алгоритм создания сеток \"По умолчанию\" доступен всегда. Он предлагает меньше возможностей, чем два других, но полностью отвечает потребностям для малых объектов, которые могут быть напечатаны объёмными принтерами.


</div>

In FreeCAD, the [Mesh Workbench](Mesh_Workbench.md) handles all mesh-related tasks. This workbench contains tools not only for converting between Part and Mesh objects but also for analyzing and repairing meshes. While mesh manipulation isn't the primary focus of FreeCAD, it becomes essential when preparing models for 3D printing. Mesh objects are widely used in other applications, and the Mesh Workbench allows you to fully manage and adjust these objects, ensuring they are ready for the next step in the printing process.

-   Let\'s convert the Lego piece we created in the last chapter into an STL mesh. The geometry can be downloaded at the end of said chapter.
-   Open the FreeCAD file containing the Lego piece.
-   Switch to the [Mesh Workbench](Mesh_Workbench.md)
-   Select the Lego brick
-   Select menu **Meshes → Create Mesh from Shape**
-   A task panel will open with several options. Some additional meshing algorithms (Mefisto or Netgen) might not be available, depending on how your version of FreeCAD was compiled. The Standard meshing algorithm will always be present. It offers fewer possibilities than the two others, but is totally sufficient for small objects that fit into the maximum print size of a 3D printer.

![](images/FreeCAD_MeshLego.png )


<div class="mw-translate-fuzzy">

-   Выберите преобразователь в сетки **По умолчанию**, и оставьте отклонение поверхности в значении по умолчанию, равном **0.10**. Нажмите **Ok**.
-   Будет создана сеточный объект, прямо на поверхности твердотельного. Скройте тело, или уберите один из объектов в сторону, чтобы сравнить оба.
-   Измените параметр **Вид -\> Display Mode** сеточного объекта на **Flat Lines**, чтобы увидеть составные треугольники.
-   Если Вы не довольны, и считаете, что результат слишком груб, можете повторить операцию, уменьшив значение отклонения. В примере ниже левая сетка использует значение по умолчанию в **0.10**, а правая - **0.01**:


</div>

![](images/Exercise_meshing_02.jpg )

В большинстве случаев, тем не менее, значения по умолчанию дают удовлетворительный результат.


<div class="mw-translate-fuzzy">

Теперь мы можем экспортировать нашу сетку в сеточный файловый формат, например, [STL](https://ru.wikipedia.org/wiki/STL_(формат_файла)), который сейчас наиболее широко используется для трёхмерной печати, через меню **Файл -\> Экспортировать**, и выбрав формат файлов STL.


</div>


<div class="mw-translate-fuzzy">

Если у Вас нет объёмного принтера, можно найти коммерческий сервис, который напечатает и пришлёт по почте ваш объект. Кроме наиболее известных американской [Shapeways](http://www.shapeways.com/) ([в Россию не присылает](https://www.shapeways.com/support/faq?li=footer#faq-shippingcountries)) и французской [Sculpteo](http://www.sculpteo.com/), Вы можете найти и другие в Вашем городе. В крупных городах, в частности, в Москве, Вы найдёте [Fab lab](https://ru.wikipedia.org/wiki/Fab_lab), мастерские, оборудованные множеством станков, среди которых обязательно найдётся хотя бы один принтер трёхмерной печати. Обычно Fab labы представляют собой сообщества, позволяющие использовать их машины, платно или бесплатно в зависимости от мастерской, но как минимум научат Вас использовать их, и популяризуют другие виды деятельности в области трёхмерного изготовления.


</div>




<div class="mw-translate-fuzzy">

### Использование Slic3r 


</div>


<div class="mw-translate-fuzzy">

[Slic3r](http://slic3r.org/) это приложение, которое конвертирует объекты STL в G-код, который может быть отправлен прямо в объемный принтер. Подобно FreeCAD, это свободное программное обеспечение с открытыми кодами, и работает под Windows, Mac OS и Linux. Корректная настройка трёхмерной печати это сложный процесс, где Вы должны иметь немало познаний о Вашем принтере, так что это не слишком правильно создавать G-код, если Вы не готовы к печати (Ваш файл G-кода может неправильно работать на другом принтере), но это полезно для нас в любом случае, чтобы убедиться в беспроблемной пригодности нашего файла STL для печати.


</div>


<div class="mw-translate-fuzzy">

Это наш экспортированный файл STL, открытый в Slic3r. Используя вкладку **preview**, и передвигая правую полосу прокрутки, мы можем визуализировать путь, который пройдёт головка принтера для создания нашего объекта.


</div>

This is our exported STL file opened in PrusaSlicer. By just pressing on the **slice** button, the software divides your model into layers, generates the toolpaths for the 3D printer, and applies the necessary speed and temperature settings. It calculates the infill, support structures, and perimeters, then creates the G-code, which contains detailed instructions for the printer. You can preview the sliced model layer by layer, check estimated print time and filament usage, and finally save or send the G-code to your printer for the actual printing process.

![](images/FreeCAD_PrusaSlicer.png )


<div class="mw-translate-fuzzy">

[Cura](https://ultimaker.com/en/products/cura-software) это другое приложение нарезки для Windows, Mac и Linux, поддерживаемое производителем принтеров [Ultimaker](https://ultimaker.com). Некоторые пользователи FreeCAD создали [верстак Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin), который использует использует его внутри. Верстак Cura доступен из репозитория [расширений FreeCAD](https://github.com/FreeCAD/FreeCAD-addons). Для использования верстака Cura, у Вас так же должна быть установлена Cura, не включённая в верстак.


</div>

### Generating G-code 


<div class="mw-translate-fuzzy">

FreeCAD так же предлагает более продвинутый путь для прямой генерации G-кода. Это обычно сложнее чем использование автоматических инструментов, которые мы видели выше, но имеет преимущество в том, что Вы имеете полный контроль за выходом. Это обычно не нужно при использовании объёмных принтеров, но становится очень важным при фрезеровании на станках с ЧПУ, поскольку эти машины сложнее.


</div>


<div class="mw-translate-fuzzy">

Генерация трасс фрезерования на станке с ЧПУ это ещё одна тема, которая слишком обширна для этого руководства, так что мы собираемся показать только простой проект Path, не обращая внимания на детали реального производства с помощью ЧПУ.


</div>


<div class="mw-translate-fuzzy">

-   Загружаем файл, содержащий наш элемент Lego, и переключаемся на [верстак Path](Path_Workbench/ru.md).
-   Поскольку конечный элемент не содержит прямоугольный верх, скрываем конечный элемент, и показываем первое из сделанных нами кубических выдавливаний, имеющее прямоугольный верх.
-   Выделяем верхнюю поверхность и нажимаем кнопку <img alt="" src=images/Path_Profile.svg  style="width:16px;"> [Profile](Path_Profile/ru.md).
-   Устанавливаем его параметр **Offset** в 1 мм.


</div>

Though generating CNC milling paths is a topic too broad to cover in detail here, we'll demonstrate how to create a simple CAM project in FreeCAD. While we won't focus on every detail of real-world CNC machining, this guide will introduce you to the essential steps, emphasizing the level of input required to ensure accurate and efficient results. This added complexity is essential for CNC projects, where precision and customizability are critical to achieving desired machining outcomes.

-   Load the file containing our Lego piece, and switch to the <img alt="" src=images/Workbench_CAM.svg  style="width:16px;"> [CAM Workbench](CAM_Workbench.md).
-   Press on the <img alt="" src=images/CAM_Job.svg  style="width:16px;"> [Job](CAM_Job.md) button and select our lego piece.
-   Since this section doesn't aim to provide an in-depth tutorial of the CAM Workbench, we will be using the default values. If you would like a more detailed tutorial, please refer to [CAM walk-through](CAM_Walkthrough_for_the_Impatient.md). Keep in mind that in the CAM Workbench, a stock body is automatically created around your object, representing the raw material that will be machined. Right now, this stock body extends 1 mm in all directions from the object.

![](images/FreeCAD_CAM1.png )


<div class="mw-translate-fuzzy">

-   Затем дублируем первую петлю несколько раз, чтобы инструмент выпилил целый блок. Выберем трассу FaceProfile, и нажмём <img alt="" src=images/Path_Array.svg  style="width:16px;"> [Array](Path_Array/ru.md) button.
-   Установим параметр массива **Copies** на 8, и смещение на **Offset** -2 мм в направлении Z, и переместим положение массива на 2 мм в направлении Z, так чтобы вырезание началось немного выше выдавки, учитывая высоту точек.


</div>

-   The following image shows the FreeCAD CAM Workbench setup for machining a Lego block. The model tree includes solid modeling operations like Pad, Pocket, and LinearPattern, which were used to shape the part. A Job is created, containing toolpaths under Operations that define how the material will be removed from the Stock. The Default Tool is selected for machining, and the Model-Body represents the 3D part being worked on. This setup prepares the object for generating G-code to control the CNC machine.

![](images/FreeCAD_CAMtree.png )


<div class="mw-translate-fuzzy">

-   Теперь у нас определена трасса, следуя по которой фрезерный станок выпилит из заготовки прямоугольный блок. Теперь надо выфрезеровать пространство между точками, чтобы высвободить их. Скройте выдавку, и снова сделайте видимой конечный кирпичик, чтобы мы могли выделить поверхность, лежащую между точками.
-   Выделите верхнюю поверхность, и нажмите кнопку <img alt="" src=images/Path_Pocket_Shape.svg  style="width:16px;"> [Face Pocket](Path_Pocket_Shape/ru.md). Установите параметр **Offset** в 1 мм, а **retraction height** в 20 мм. Это высота, на которой фреза пройдёт при переходе с одной петли к другой. Без него фреза может прорезать прямо через одну из наших точек:


</div>


<div class="mw-translate-fuzzy">

-   Теперь всё, что осталось сделать, это объединить эти операции. Это можно сделать через [Path Compound](Path_Compound/ru.md) или [Path Job](Path_Job/ru.md). Поскольку нам больше ничего не нужно и мы уже готовы к экспорту, мы используем Job. Нажмите кнопку <img alt="" src=images/Path_Job.svg  style="width:16px;"> [Job](Path_Job/ru.md).
-   Установите параметр **Use Placements** проекта в True, поскольку мы изменили положение массивов, и мы хотим, чтобы это было учтено в проекте.
-   В древе проекта перетащим два массива в проект. Если нужно, массивы внутри проекта можно переупорядочить двойным кликом по ним.
-   Проект теперь можно экспортировать в G-код, выбрав его, выделив в меню **Файл -\> Экспорт**, выбрав формат G-код, и выбрав скрипт постобработки в соответствии с Вашей машиной в открывшемся всплывающем диалоге.


</div>


<div class="mw-translate-fuzzy">

Для симуляции реальной резки доступно много приложений, одно из них [Camotics](http://camotics.org/), такое же мультиплаформенное и разрабатываемое на принципах открытых исходных кодов, как и FreeCAD.


</div>


<div class="mw-translate-fuzzy">

**Загрузки**


</div>


<div class="mw-translate-fuzzy">

-   Созданный в этом упражнении файл STL: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   Файл, созданный в этом упражнении: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   Файл G-кода, созданный в этом упражнении: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>


</div>


<div class="mw-translate-fuzzy">

**Читать далее**


</div>

**Downloads**

-   The STL file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.stl>
-   The file generated during this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/path.FCStd>
-   The G-code file generated in this exercise: <https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/lego.gcode>

**Read more**


<div class="mw-translate-fuzzy">

-   [Верстак Mesh](Mesh_Workbench/ru.md)
-   [Формат файлов STL](https://en.wikipedia.org/wiki/STL_%28file_format%29)
-   [Slic3r](http://slic3r.org/)
-   [Cura](https://ultimaker.com/en/products/cura-software)
-   [Верстак Cura](https://github.com/cblt2l/FreeCAD-CuraEngine-Plugin)
-   [Верстак Path](Path_Workbench/ru.md)
-   [Camotics](http://camotics.org/)


</div>

### Videos

-   [How To Use FreeCAD For 3D Printing \| Using The Realthunder Branch](https://www.youtube.com/playlist?list=PL6Fiih6ItYsWCE20KtUJYpiDPrCA2rVpN) A video playlist by Maker Tales about how to use FreeCAD for 3D printing.


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [CAM](Category_CAM.md) > [Mesh](Category_Mesh.md) > [Tutorials](Category_Tutorials.md) > Manual:Preparing models for 3D printing/ru
