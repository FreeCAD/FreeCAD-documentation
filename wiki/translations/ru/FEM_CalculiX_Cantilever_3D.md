---
- TutorialInfo:/ru
   Topic:Finite Element Analysis
   Level:Beginner
   Time:10 minutes
   Author:[http://www.freecadweb.org/wiki/index.php?title=User:Berndhahnebach Bernd]
   FCVersion:0.16.6377 or above
   Files:
---

# FEM CalculiX Cantilever 3D/ru




<div class="mw-translate-fuzzy">




</div>



## Введение

Данный пример предназначен для того, чтобы показать, как выглядит простой анализ методом конечных элементов (МКЭ/FEA) в [верстаке FEM](FEM_Workbench/ru.md) в интерфейсе FreeCAD, и как можно визуализировать результаты. Показывается, как запустить (МКЭ) и как изменить значение нагрузки и направление нагрузки. Более того, поскольку файл примера предоставляется при любой установке FreeCAD, это полезная и простая проверка, позволяющая убедиться в правильности настройки верстака FEM.

<img alt="" src=images/FEM_example01_pic10.png  style="width:700px;">



## Требования


<div class="mw-translate-fuzzy">

-   Совместимая версия FreeCAD, указанная в описании данного руководства.
-   Используйте **Справка → О FreeCAD** для просмотра версии установленного FreeCAD
-   Не требуется никакого внешнего программного обеспечения для загрузки файла примера, просмотра сетки и геометрии, а также для визуализации результатов.
-   Для повторного запуска FEA на вашем компьютере должно быть установлено программное обеспечение CalculiX. Возможно, решатель уже установлен вместе с FreeCAD. Если решатель CalculiX не установлен, см. [ FEM Install](FEM_Install.md).


</div>



## Настройка файла примера 




<div class="mw-translate-fuzzy">

### Загрузка верстака Start 


</div>


<div class="mw-translate-fuzzy">

-   Запустите FreeCAD
-   Откройте верстак Start


</div>

<img alt="" src=images/FEM_example01_pic11.png  style="width:700px;">



### Активация контейнера для анализа 


<div class="mw-translate-fuzzy">

-   Для работы с анализом необходимо активировать анализ.
-   В [древе проекта](tree_view/ru.md) щелкните правой кнопкой мыши <img alt="" src=images/FEM_Analysis.png  style="width:32px;"> MechanicalAnalysis → Активировать анализ


</div>

<img alt="" src=images/FEM_example01_pic12.png  style="width:700px;">



### Контейнер для анализа и его объекты 


<div class="mw-translate-fuzzy">

-   Если анализ активирован, FreeCAD сам изменит текущую рабочую среду на FEM.
-   Для статического механического анализа необходимо как минимум 5 объектов.
-   <img alt="" src=images/FEM_Analysis.svg  style="width:32px;"> контейнер анализа

1.  <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:32px;"> решатель
2.  <img alt="" src=images/FEM_MaterialSolid.svg  style="width:32px;"> материал
3.  <img alt="" src=images/FEM_ConstraintFixed.svg  style="width:32px;"> фиксированные ограничения
4.  <img alt="" src=images/FEM_ConstraintForce.svg  style="width:32px;"> ограничения силы
5.  <img alt="" src=images/FEM_FEMMesh.svg  style="width:32px;"> сетка МКЭ

-   Поскольку в приведённом здесь примере так же присутствуют результаты, имеется шестой объект, результаты <img alt="" src=images/FEM_ResultShow.svg  style="width:24px;">.


</div>



### Визуализация результатов 


<div class="mw-translate-fuzzy">

-   Убедитесь, что анализ активирован.
-   Убедитесь, что анализ все еще содержит объект результата, если нет, просто перезагрузите файл примера.
-   Щелкните значок панели инструментов на <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Show result](FEM_ResultShow/ru.md)
-   В окне задач выбоерите z-Displacement. Он покажет -88.443 mm в отрицательном направлении по оси Z.
-   Это разумно, поскольку сила также направлена в отрицательном направлении оси Z.
-   Установите флажок рядом с нижним ползунком отображения смещения.
-   Ползунок можно использовать для изменения сетки, чтобы упростить просмотр деформации.
-   Выберите один из различных типов результатов, чтобы просмотреть все доступные типы результатов в графическом интерфейсе пользователя.


</div>

<img alt="" src=images/FEM_example01_pic13.png  style="width:400px;">



### Удаление результатов расчета 

-   Убедитесь, что анализ активирован.
-   Чтобы удалить результаты, выберите значок на панели инструментов <img alt="" src=images/FEM_PurgeResults.png  style="width:32px;"> [Purge results](FEM_ResultsPurge/ru.md).



### Запуск анализа конечных элементов 


<div class="mw-translate-fuzzy">

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

<img alt="" src=images/FEM_example01_pic14.png  style="width:400px;">



### Быстрый запуск анализа конечных элементов 


<div class="mw-translate-fuzzy">

-   В древе проекта выберите объект решателя <img alt="" src=images/FEM_Solver.png  style="width:32px;"> анализа <img alt="" src=images/FEM_Analysis.png  style="width:32px;">.
-   На панели инструментов значка щелкните <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:32px;"> [Quick Analysis](FEM_SolverRun/ru.md).
-   Будет записан входной файл и запущен CalculiX, и должен быть создан объект результата.


</div>



### Изменение прилагаемой силы и направления нагрузки 


<div class="mw-translate-fuzzy">

-   В [древе проекта](tree_view/ru.md) выберите объект сетки FEM <img alt="" src=images/FEM_FEMMesh.svg  style="width:32px;"> и нажмите клавишу **Space**.
    -   **Результат:** Видимость сетки FEM будет отключена. Геометрическая модель останется видна.
-   В [древе проекта](tree_view/ru.md) дважды щелкните объект ограничения силы, чтобы открыть его [панель задач](task_panel/ru.md)
-   В окне задачи измените значение нагрузки на **500000000 N = 500 MN** (**Примечание:** единица силы в окне задачи должна быть в N)
-   Нажмите кнопку **Direction**.
-   На геометрической модели щелкните по одной из длинных кромок в направлении оси x.
    -   **Результат:** Красные стрелки, показывающие силу, изменят свое направление в направлении оси x. Они указывают фиксированное направление.
-   Если напряжение должно быть приложено к коробке, надо активировать Reverse Direction, щелкнув по нему.
-   Красные стрелки силы изменят свое направление.
-   Нажмите в окне задач **OK**.


</div>

<img alt="" src=images/FEM_example01_pic15.png  style="width:700px;">


<div class="mw-translate-fuzzy">

-   Включите [видимость](Std_ToggleVisibility/ru.md) сетки FEM <img alt="" src=images/FEM_FEMMesh.svg  style="width:32px;">, выбрав ее в дереве и нажав клавишу **Пробел**.
-   Вы уже знаете, как запустить анализ и как визуализировать результаты.
-   В результате деформации смещение по оси x должно быть равно 19,05 мм.


</div>

<img alt="" src=images/FEM_example01_pic16.png  style="width:400px;">



## Что дальше? 


<div class="mw-translate-fuzzy">

-   Вы усвоили простые методы работы с [верстаком FEM](FEM_Workbench/ru.md).
-   Теперь вы готовы к выполнению [второго задания](FEM_tutorial/ru.md).
-   Мы создадим консоль CalculiX самостоятельно и сравним результаты с теорией балки.


</div>


{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM CalculiX Cantilever 3D/ru
