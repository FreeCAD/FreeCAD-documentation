# Manual:Creating FEM analyses/ru
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

[Метод конечных элементов](https://ru.wikipedia.org/wiki/Метод_конечных_элементов) (сокращённо МКЭ) это большой раздел математики, но в FreeCAD мы подразумеваем его как способ подсчитать распространение воздействий в объёмном объекте нарезанием его на малые участки, и анализируя влияние каждого элемента на своих соседей. У него есть много приложений в проектировании и электромагнитных полях, но сфокусируемся на том, что используется в FreeCAD, расчёт деформаций объектов под воздействием силы и веса.


</div>


<div class="mw-translate-fuzzy">

В FreeCAD такое моделирование сделано через [верстак FEM](FEM_Workbench/ru.md). Существует ряд шагов: подготовка геометрии, установка материала, создание полигональной сетки, деление на малые участки, как это делалось в главе [Подготовка для объёмной печати](Manual:Preparing_models_for_3D_printing/ru.md), и в конце калькуляция модели.


</div>

Obtaining such simulations in FreeCAD is done using the <img alt="" src=images/Workbench_FEM.svg  style="width:16px;"> [FEM](FEM_Workbench.md) Workbench, which is specifically designed for performing finite element analysis (FEA). It provides a comprehensive set of tools for preparing the model, assigning material properties, meshing, and running simulations. The FEM Workbench is versatile, supporting a wide range of simulations such as structural, thermal, and dynamic analyses, with solvers like [CalculiX](https://www.calculix.de/) and others available.

This workbench allows for the integration of other FreeCAD workbenches, enabling seamless model preparation and analysis. It also provides powerful post-processing tools to visualize and interpret simulation results, such as stress, deformation, and thermal distributions. The workflow follows these steps:

-   **Preparing the Geometry**: The model must be simplified or optimized for FEM analysis. This often includes removing unnecessary details or features that don\'t contribute to the simulation but could make it computationally expensive. You can use tools from other workbenches, like <img alt="" src=images/Workbench_PartDesign.svg  style="width:16px;"> [PartDesign](PartDesign_Workbench.md) or <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Part](Part_Workbench.md), to prepare your 3D geometry.

-   **Assigning Material Properties** :Material definitions are critical for accurate simulations. Properties such as Young\'s modulus, Poisson's ratio, and density are assigned for structural simulations, or thermal conductivity and specific heat capacity for thermal analysis. Materials can be selected from FreeCAD's material library or customized as needed.

-   **Meshing**: Meshing divides the geometry into finite elements, allowing the solver to analyze the object. Mesh quality is crucial, as finer meshes result in more accurate simulations but require more computational power. Tools are available to refine the mesh locally, focusing on areas where stress or deformation is expected to be higher.

-   **Applying Loads and Constraints**: In this step, physical conditions such as forces, pressures, moments, or thermal loads are applied to the model. Boundary conditions are also defined, such as fixing points, applying symmetry constraints, or restricting movement, depending on the scenario being simulated.

-   **Running the Solver**: Once the setup is complete, the solver calculates the model\'s response to the applied conditions. Solvers like CalculiX compute displacements, stresses, and other quantities, depending on the type of analysis performed. The process can take varying amounts of time depending on the mesh density and model complexity.

-   **Post-Processing**: After the simulation, results are visualized using tools in the FEM Workbench. Stress, strain, and displacement fields are represented as color maps and deformation plots can be generated. These visualizations allow for a thorough analysis of the model\'s performance, highlighting areas of high stress or deformation.

<img alt="" src=images/FreeCAD_FEMBeam.png  style="width:600px;">



### Подготовка FreeCAD 


<div class="mw-translate-fuzzy">

Моделирование производится сторонней программой, используемой FreeCAD для получения результатов. Поскольку симуляторов для моделирования по МКЭ с открытыми исходными кодами несколько, [верстак FEM](FEM_Workbench/ru.md) позволяет выбирать между ними. Тем не менее, пока полностью поддерживается только [CalculiX](http://www.calculix.de/). Так же для генерации разделяющей сетки требуется другая программа, [NetGen](https://sourceforge.net/projects/netgen-mesher/). Детальная инструкция для установки этих двух компонентов дана в [документации FreeCAD](FEM_Install/ru.md).


</div>



### Подготовка геометрии 


<div class="mw-translate-fuzzy">

Начнём с дома, который мы моделировали в разделе [Моделирование BIM](Manual:BIM_modeling/ru.md). Нам потребуются некоторые изменения для приспособления модели к расчёту по МКЭ. В это входит исключение объектов, которые мы не хотим учитывать при вычислении, таких как двери и окна, и объединение всех остальных объектов в один.


</div>


<div class="mw-translate-fuzzy">

-   Загрузим [модель дома](https://github.com/yorikvanhavre/FreeCAD-manual/blob/master/files/house.FCStd), которую мы сделали ранее
-   Удалим или скроем страницу, сечения и виды сверху с размерными линиями, оставив только саму модель
-   Скроем окно, дверь и плиту пола
-   Так же скроем металлические балки крыши. Они сильно отличаются от остального дома, этим исключением мы упростим наши вычисления. Вместо этого мы предположим что плита крыши напрямую положена на стены.
-   Теперь положим плиту крыши вниз, чтобы она легла на верх стен: Редактируем объект **Rectangle**, который взят как база для плиты, и изменим его параметр **Placement-\>Position-\>X** с 3.18m на 3.00m
-   Теперь наша модель очищена:


</div>


<div class="mw-translate-fuzzy">


:   <img alt="" src=images/Exercise_fem_02.jpg  style="width:600px;">


</div>



### Создание анализа 


<div class="mw-translate-fuzzy">

-   Теперь мы готовы начать анализ по МКЭ. Переключимся на [верстак FEM](FEM_Workbench/ru.md)
-   Выделим объединённый объект
-   Нажмём кнопку <img alt="" src=images/Fem_Analysis.png  style="width:16px;"> [New Analysis](FEM_Analysis/ru.md)
-   Будет создан новый механический анализ и будет открыта панель установок. Здесь Вы сможете определить параметры создания полигональной сетки для МКЭ. Важнее всего для настройки отредактировать параметр **Max Size**, который определяет в миллиметрах максимальный размер каждого элемента сетки. Сейчас мы оставим значение по умолчанию, равное 1000:


</div>


<div class="mw-translate-fuzzy">

-   После нажатия OK нескольких секунд вычислений наша сетка МКЭ готова:


</div>

<img alt="" src=images/FreeCAD_FEM_MesherParameters.png  style="width:600px;">

-   Our mesh is ready.


<div class="mw-translate-fuzzy">

-   Теперь мы можем определить материал нашей сетки. Это нужно, поскольку наш объект реагирует на приложенные силы по-разному в зависимости от прочности материала. Выберем объект анализа, и нажмём кнопку <img alt="" src=images/FEM_MaterialSolid.png  style="width:16px;"> [New Material](FEM_MaterialSolid/ru.md).
-   Будет открыта панель задач, позволяющая выбрать материал. В списке материалов выберем **Concrete-generic** (бетон), и нажмём OK.


</div>

-   We can now define the material to be applied to our mesh by pressing on the <img alt="" src=images/FEM_MaterialSolid.svg  style="width:16px;"> [New Material](FEM_MaterialSolid.md) option. The choice of material is crucial in any analysis, as different materials with varying properties will behave differently under the same conditions. Factors like strength, elasticity, and density play a significant role in how a material responds to forces, pressures, or temperatures. Selecting the appropriate material ensures accurate simulation results, reflecting how the object would react in real-world scenarios.
-   A task panel will open to allow us to choose a material. In the Material drop-down list, choose the **Steel-1C22** material, and press the **OK**.

<img alt="" src=images/FreeCAD_FEM_material.png  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Теперь мы готовы приложить силы. Начнем с указания неподвижных поверхностей, опирающихся на землю. Нажмём кнопку <img alt="" src=images/FEM_ConstraintFixed.png  style="width:16px;"> [Constraint fixed](FEM_ConstraintFixed/ru.md).
-   Выделим нижнюю поверхность строения и нажмём OK. Нижняя поверхность обозначена как неподвижная:


</div>

<img alt="" src=images/FreeCAD_FEM_Beam_FC.png  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Теперь мы добавим нагрузку на верхнюю поверхность, которая должна представлять, например, большой вес, расположенный крыше. Для этого мы используем ограничение давления. Нажмём кнопку <img alt="" src=images/FEM_ConstraintPressure.png  style="width:16px;"> [Constraint pressure](FEM_ConstraintPressure/ru.md).
-   Нажмём верхнюю поверхность крыши, установим давление на **10MPa** и кликнем кнопку OK. Сила приложена:


</div>

<img alt="" src=images/_FreeCAD_FEM_Beam_force.png  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Теперь мы готовы начать вычисления. Выделим объект **CalculiX**, и нажмём кнопку <img alt="" src=images/FEM_ControlSolver.png  style="width:32px;"> [Start Calculation](FEM_SolverControl/ru.md).
-   В панели задач, которая будет открыта, нажмите сначала кнопку **Write .inp file** для создания входного файла для CalculiX, затем кнопку **Run CalculiX**. Несколькими мгновениями позднее вычисления будут выполнены:


</div>

<img alt="" src=images/FreeCAD_FEM_Calculix.png  style="width:600px;">


<div class="mw-translate-fuzzy">

-   Теперь можно посмотреть результаты. Закройте панель задач, и Вы увидите новый объект **Results**, который добавлен к вашему анализу.
-   Дважды кликните объект Results.
-   Установите тип результата, который Вы хотите увидеть на сетки, например, \"abs displacement\", отметтьте под заголовком **Водоизмещение** чекбокс **show**, и передвигайте слайдер возле него. Вы сможете увидеть деформацию, увеличивающуюся по мере увеличения силы:


</div>

<img alt="" src=images/FreeCAD_FEM_Results.png  style="width:600px;">

Показываемые верстаком FEM результаты, разумеется, пока не достаточны для принятия реальных решений о размерах и материалах, тем не менее, они уже дают точную информацию о том, как силы проходят через структуру и где находятся слабые места, которые будут ощущать наибольшее воздействие.

**Читать далее**


<div class="mw-translate-fuzzy">

-   [Верстак FEM (метода конечных элементов - МКЭ)](FEM_Workbench/ru.md)
-   [Установка требуемых компонентов МКЭ](FEM_Install/ru.md)
-   [CalculiX](http://www.calculix.de)
-   [NetGen](https://sourceforge.net/projects/netgen-mesher)


</div>



---
⏵ [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > Manual:Creating FEM analyses/ru
