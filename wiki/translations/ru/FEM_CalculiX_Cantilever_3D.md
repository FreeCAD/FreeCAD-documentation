# FEM CalculiX Cantilever 3D/ru
<div class="mw-translate-fuzzy">


{{TutorialInfo/ru
|Topic=Finite Element Analysis
|Level=Beginner
|Time=10 minutes
|Author=[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
|FCVersion=0.16.6377 or above
|Files=
}}


</div>

## Введение


<div class="mw-translate-fuzzy">

## Введение 

Этот пример предназначен для того, чтобы показать, как выглядит простой анализ методом конечных элементов (МКЭ/FEA) в [верстаке FEM](FEM_Workbench/ru.md) в интерфейсе FreeCAD, и как можно визуализировать результаты. Показывается, как запустить (МКЭ) и как изменить значение нагрузки и направление нагрузки. Более того, поскольку файл примера предоставляется при любой установке FreeCAD, это полезная и простая проверка, позволяющая убедиться в правильности настройки верстака FEM.


</div>

<img alt="" src=images/FEM_example01_pic00.jpg  style="width:700px;">

## Требования


<div class="mw-translate-fuzzy">

## Требования 

-   Совместимая версия FreeCAD, указанная в описании учебника.
-   Ипользуйте **Справка → О FreeCAD** для просмотра версии установленного FreeCAD
-   Не требуется никакого внешнего программного обеспечения для загрузки файла примера, просмотра сетки и геометрии, а также для визуализации результатов.
-   Для повторного запуска FEA на вашем компьютере должно быть установлено программное обеспечение CalculiX. Возможно, решатель уже установлен вместе с FreeCAD. Если решатель CalculiX не установлен, см. [ FEM Install](FEM_Install.md).


</div>

## Настройка файла примера 

### Load Start Workbench 


<div class="mw-translate-fuzzy">

### Загрузка верстака Start 

-   Запустите FreeCAD
-   Должен быть загружен верстак Start


</div>

### Load the example file 


<div class="mw-translate-fuzzy">

### Загрузить файл примера 

-   Перейдите к примерам проектов и нажмите «Загрузить пример анализа МКЭ».
-   Если из-за дальнейших операций некоторая геометрия, ограничения или результаты будут нарушены или удалены, просто повторите шаги, описанные выше.


</div>

<img alt="" src=images/FEM_example01_pic01.jpg  style="width:700px;">

### Activate the analysis container 


<div class="mw-translate-fuzzy">

### Активировать контейнер анализа 

-   Для работы с анализом необходимо активировать анализ.
-   В [древе проекта](tree_view/ru.md) щелкните правой кнопкой мыши <img alt="" src=images/FEM_Analysis.png  style="width:32px;"> MechanicalAnalysis → Активировать анализ


</div>

<img alt="" src=images/FEM_example01_pic02.jpg  style="width:700px;">

### Analysis container and its objects 


<div class="mw-translate-fuzzy">

### Контейнер анализа и его объекты 

-   Если анализ активирован, FreeCAD сам изменит текущую рабочую среду на FEM.
-   Для статического механического анализа необходимо как минимум 5 объектов.
-   <img alt="" src=images/FEM_Analysis.png  style="width:32px;"> контейнер анализа

1.  <img alt="" src=images/FEM_Solver.png  style="width:32px;"> решатель
2.  <img alt="" src=images/FEM_Material.png  style="width:32px;"> материал
3.  <img alt="" src=images/FEM_FixedConstraint.png  style="width:32px;"> фиксированные ограничения
4.  <img alt="" src=images/FEM_ForceConstraint.png  style="width:32px;"> ограничения силы
5.  <img alt="" src=images/FEM_Create.png  style="width:32px;"> сетка МКЭ

-   Поскольку в приведённом здесь примере так же присутствуют результаты, имеется шестой объект, результаты <img alt="" src=images/FEM_ShowResult.png  style="width:16px;">.


</div>

### Visualizing Results 


<div class="mw-translate-fuzzy">

### Визуализация результатов 

-   Убедитесь, что анализ активирован.
-   Убедитесь, что анализ все еще содержит объект результата, если нет, просто перезагрузите файл примера.
-   Щелкните значок панели инструментов на <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Show result](FEM_ResultShow/ru.md)
-   В окне задач выбоерите z-Displacement. Он покажет -88.443 mm в отрицательном направлении по оси Z.
-   Это разумно, поскольку сила также направлена в отрицательном направлении оси Z.
-   Установите флажок рядом с нижним ползунком отображения смещения.
-   Ползунок можно использовать для изменения сетки, чтобы упростить просмотр деформации.
-   Выберите один из различных типов результатов, чтобы просмотреть все доступные типы результатов в графическом интерфейсе пользователя.


</div>

<img alt="" src=images/FEM_example01_pic03.jpg  style="width:400px;">

### Purging Results 


<div class="mw-translate-fuzzy">

### Очистка Результатов 

-   Убедитесь, что анализ активирован.
-   Чтобы удалить результаты, выберите значок на панели инструментов <img alt="" src=images/FEM_PurgeResults.png  style="width:32px;"> [Purge results](FEM_ResultsPurge/ru.md).


</div>

### Running the FEA 


<div class="mw-translate-fuzzy">

### Запуск анализа конечных элементов 

-   Дважды щелкните объект решателя в [древе проекта](Tree_view/ru.md) <img alt="" src=images/FEM_Solver.png  style="width:32px;">.
-   Убедитесь, что в [панели задач](task_panel/ru.md) объекта решателя выбран статический анализ.
-   Нажмите на запись файла .inp в том же окне задачи. Следите за окном журнала, пока оно не напечатает «запись завершена».
-   Щелкните **Run CalculiX**. Поскольку это очень небольшой анализ, его выполнение займет меньше секунды.
-   В текстовом окне зелеными буквами должно быть напечатано \"CalculiX done!\" а в следующей строке «загрузка наборов результатов\...»
-   Если не было никаких сообщений об ошибках, то Вы только что закончили свой первый анализ методом конечных элементов во FreeCAD.
-   Щелкните **Close** в окне задачи.
-   Должен быть создан новый объект результата. Вы уже знаете как визуализировать результаты.
-   Если при запуске анализа вы получаете сообщение об ошибке отсутствия исполняемого файла решателя или тому подобное, проверьте [установку FEM](FEM_Install/ru.md).


</div>

<img alt="" src=images/FEM_example01_pic04.jpg  style="width:400px;">

### Running the FEA the fast Way 


<div class="mw-translate-fuzzy">

### Быстрый запуск конечноэлементного анализа 

-   В древе проекта выберите объект решателя <img alt="" src=images/FEM_Solver.png  style="width:32px;"> анализа <img alt="" src=images/FEM_Analysis.png  style="width:32px;">.
-   На панели инструментов значка щелкните <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:32px;"> [Quick Analysis](FEM_SolverRun/ru.md).
-   Будет записан входной файл и запущен CalculiX, и должен быть создан объект результата.


</div>

### Changing Load Direction and Load Value 


<div class="mw-translate-fuzzy">

### Изменение направления и значения нагрузки 

-   В [древе проекта](tree_view/ru.md) выберите объект сетки FEM <img alt="" src=images/FEM_Create.png  style="width:32px;"> и нажмите клавишу **Space**.
    -   **Результат:** Видимость сетки FEM будет отключена. Геометрическая модель останется видна.
-   В [древе проекта](tree_view/ru.md) дважды щелкните объект ограничения силы, чтобы открыть его [панель задач](task_panel/ru.md)
-   В окне задачи измените значение нагрузки на **500000000 N = 500 MN** (**Примечание:** единица силы в окне задачи должна быть в N)
-   Нажмите кнопку **Direction**.
-   На геометрической модели щелкните по одной из длинных кромок в направлении оси x.
    -   **Результат:** Красные стрелки, показывающие силу, изменят свое направление в направлении оси x. Они указывают фиксированное направление.
-   Если напряжение должно быть приложено к коробке, надо активировать Reverse Direction, щелкнув по нему.
-   Красные стрелки силы изменят свое направление.
-   Нажмите в окне задачи **OK**.

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Включите [видимость](Std_ToggleVisibility/ru.md) сетки FEM <img alt="" src=images/FEM_Create.png  style="width:32px;">, выбрав ее в дереве и нажав клавишу **Пробел**.
-   Вы уже знаете, как запустить анализ и как визуализировать результаты.
-   Деформация по оси x должна оказаться 19,05 мм.


</div>

<img alt="" src=images/FEM_example01_pic05.jpg  style="width:700px;">

-   Toggle the [visibility](Std_ToggleVisibility.md) of the FEM mesh <img alt="" src=images/FEM_FEMMesh.svg  style="width:24px;"> \'On\' by selecting it in tree view and pressing the **Space** key.
-   You know how to trigger an analysis and how to visualize results already.
-   The deformation in x-direction should be 19.05 mm.

<img alt="" src=images/FEM_example01_pic06.jpg  style="width:400px;">

## Что дальше? 


<div class="mw-translate-fuzzy">

## Что дальше? 

-   Теперь мы закончили с основным рабочим процессом для [верстака FEM](FEM_Workbench/ru.md).
-   Теперь вы готовы проделать второй [учебник FEM](FEM_tutorial/ru.md).
-   Мы создадим консоль CalculiX самостоятельно и сравним результаты с теорией балки.


</div>


{{Tutorials navi

}} {{FEM Tools navi}}

---
[documentation index](../README.md) > FEM CalculiX Cantilever 3D/ru
