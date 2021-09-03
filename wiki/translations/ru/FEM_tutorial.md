


<div class="mw-translate-fuzzy">


{{TutorialInfo/ru
|Topic= Анализ методом конечных элементов
|Level= Новичок
|Time= 10 минут + время работы Решателя
|Author=[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
|FCVersion=0.16.6700 и выше
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Введение

Это руководство предназначено для того чтобы ознакомить с основными принципами работы с верстаком FEM, а также большинством доступных инструментов для статического анализа.


</div>

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">

## Требования


<div class="mw-translate-fuzzy">

## Требования 

-   Версия FreeCAD 0.16.6700 и выше
-   [Netgen](http://sourceforge.net/projects/netgen-mesher/) и/или [GMSH](http://geuz.org/gmsh/) установленные в вашей системе
-   В случаем когда используется GMSH, рекомендуется установить в [AddonManager](Std_AddonMgr/ru.md) [Macro GMSH](Macro_GMSH/ru.md), разработанный [psicofil](https://github.com/psicofil/Macros_FreeCAD)
-   [Calculix](http://www.calculix.de/) установленный в вашей системе
-   Читатель должен обладать базовыми понятиями о том как использовать верстаки [Part](Part_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md).


</div>

## Последовательность действий 

### Modeling


<div class="mw-translate-fuzzy">

### Моделирование

В этом примере в качестве объекта исследования используется Куб, но также вместо него могут быть использованы модели созданные в Верстаках Part или PartDesign.


</div>


<div class="mw-translate-fuzzy">

1.  Создать новый документ
2.  Активировать верстак Part
3.  Создать Куб
4.  Изменить его размеры (**Box**) на следующие:
    1.  Length: 8000 мм
    2.  Width: 1000 мм
    3.  Height: 1000 мм


</div>

Теперь у нас есть модель с которой можно работать.

### Creating the Analysis 

#### Netgen


<div class="mw-translate-fuzzy">

### Создание Анализа 

#### Netgen 

1.  Выбрать модель
2.  Кликнуть в меню <img alt="" src=images/FEM_Analysis.png  style="width:16px;"> [New mechanical analysis](FEM_Analysis/ru.md), чтобы создать анализ из выбранного объекта
3.  В диалоге создания сетки кликнуть **OK**


</div>


<div class="mw-translate-fuzzy">

Вы также можете перетащить сетку в Mechanical Analysis, у которого нет сетки, внутри древа проекта.


</div>

#### GMSH


<div class="mw-translate-fuzzy">

#### GMSH 

Макросы от psicofil\'s - строго рекомендуются и используется в данном примере.

1.  Активировать макрос
2.  Выбрать объект, который вы хотите использовать. В нашем случае это Куб
3.  Выберете пункт **Create Mechanical Analysis from mesh**
4.  Кликните **OK**


</div>

Мы создали сетку для нашего объекта и готовы добавить к нему ограничения и действующие силы.

### Constraints and Forces 


<div class="mw-translate-fuzzy">

### Ограничения и силы 

1.  Скройте сетку внутри древа проекта.
2.  Откройте оригинальную модель
3.  Выберите <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Создать МКЭ с фиксированными ограничениями](FEM_ConstraintFixed/ru.md)
4.  Выберите заднюю поверхность Куба (поверхность осей **YZ**) и кликните OK
5.  Выберите <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Создать МКЭ с ограничениями силы](FEM_ConstraintForce/ru.md)
6.  Выберите фронтальную поверхность Куба (грань, параллельная задней поверхности) и установите значение **Area load** в 9000000,00
7.  Установите **Direction** в **-Z** выбором одной из граней параллельно этому направлеию.
8.  Кликните OK


</div>

Теперь мы установили ограничения и силы для нашего статического анализа.

### Final preparations 


<div class="mw-translate-fuzzy">

### Последние приготовления 

1.  Нажмите <img alt="" src=images/FEM_Material.png  style="width:16px;"> [Mechanical material\...](FEM_MaterialSolid/ru.md) и выберете Calculix-Steel в качестве материала.
2.  Нажмите **OK**


</div>

### Running the Solver 

#### Стандартная Процедура 


<div class="mw-translate-fuzzy">

### Запуск решателя 

#### Стандартная процедура 

1.  Выберите объект решателя <img alt="" src=images/FEM_Solver.png  style="width:16px;">, находящийся в 
**Mechanical Analysis**
2.  Выберите в меню <img alt="" src=images/FEM_Calculation.png  style="width:16px;"> [Start solver job control](FEM_SolverControl/ru.md)
3.  Выберите **Write Calculix Input File**
4.  Выберите **Run Calculix**
5.  Кликните **Close**


</div>

#### Быстрая Процедура 


<div class="mw-translate-fuzzy">

#### Быстрая процедура 

1.  Выберите объект решателя <img alt="" src=images/FEM_Solver.png  style="width:16px;">, находящийся в 
**Mechanical Analysis**
2.  Кликните на <img alt="" src=images/FEM_RunCalculiXccx.png  style="width:16px;"> [Run CalculiX ccx](FEM_SolverRun/ru.md).


</div>

### Анализ Результатов 


<div class="mw-translate-fuzzy">

### Анализ результатов 

1.  Выберите объект **Results** из **Object Tree**
2.  Выберите <img alt="" src=images/FEM_ShowResult.png  style="width:16px;"> [Show result](FEM_ResultShow/ru.md)
3.  Выберите для просмотра из различных типов результата нужные
4.  Движок внизу может использоваться для изменения визуализации сетки. Это позволяет визуализировать деформацию, испытываемую объектом, учитывая, что это приближение.
5.  Для удаления результатов выберите <img alt="" src=images/FEM_PurgeResults.png  style="width:16px;"> [Purge results](FEM_ResultsPurge/ru.md)


</div>


{{Note|Сравнение с предшествующим файлом примера|Если Вы тип результата выбрали '''Z displacement''', Вы увидите, что полученное значение почти идентично тестовому примеру, предоставляемому FreeCAD. Различия могут быть из-за качества сетки и числа обрабатываемых узлов.}}


<div class="mw-translate-fuzzy">

Теперь мы закончили с основными принципами работы [FEM Module](FEM_Module/ru.md).


</div>


{{Tutorials navi

}} {{FEM Tools navi}} 
