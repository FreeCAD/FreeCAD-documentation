---
- TutorialInfo:/ru
   Topic: Анализ методом конечных элементов
   Level: Новичок
   Time: 10 минут + время работы Решателя
   Author:[http://freecadweb.org/wiki/index.php?title=User:Drei Drei]
   FCVersion:0.16.6700 и выше
   Files:
---

# FEM tutorial/ru




<div class="mw-translate-fuzzy">




</div>



## Введение

Данное руководство знакомит пользователя с основными принципами работы верстака FEM, а также с большинством доступных инструментов, предназначенных для выполнения статического анализа.

<img alt="" src=images/FEM_tutorial_result.png  style="width:600px;">



## Требования


<div class="mw-translate-fuzzy">

-   Версия FreeCAD должна быть 0.17 и старше.
-   Наличие [Netgen](http://sourceforge.net/projects/netgen-mesher/) и/или [GMSH](http://geuz.org/gmsh/) в системе (устанавливаются вместе с FreeCAD).
-   Наличие [Calculix](http://www.calculix.de/) в системе (устанавливается вместе с FreeCAD).
-   Пользователь изучающий данный пример должен обладать базовыми понятиями о том, как использовать верстаки [Part](Part_Workbench/ru.md) и [PartDesign](PartDesign_Workbench/ru.md).


</div>



## Последовательность действий 



### Моделирование


<div class="mw-translate-fuzzy">

В этом примере в качестве объекта исследования используется Куб, но также вместо него могут быть использованы любые другие модели созданные в Верстаках Part или PartDesign.


</div>


<div class="mw-translate-fuzzy">

1.  Создайте [новый документ](Std_New/ru.md) (нажатием на кнопку <img alt="" src=images/Std_New.svg  style="width:24px;">).
2.  Активировать <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [верстак Part](Part_Workbench/ru.md).
3.  Создайте Куб.
4.  Измените его **Размеры** на следующие:
    1.  Length: 8.000 м.
    2.  Width: 1.000 м.
    3.  Height: 1.000 м.


</div>


<div class="mw-translate-fuzzy">

Теперь у нас есть модель с которой можно работать.


</div>



### Проведение анализа 

1.  Activate the <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM Workbench](FEM_Workbench.md).
2.  Select the **Model → <img src="images/FEM_Analysis.svg" width=16px> Analysis container‏‎** option from the menu.



### Установка ограничений и приложение силы 

1.  Скройте сетку внутри древа проекта.
2.  Откройте оригинальную модель
3.  Выберите <img alt="" src=images/FEM_FixedConstraint.png  style="width:16px;"> [Создать МКЭ с фиксированными ограничениями](FEM_ConstraintFixed/ru.md)
4.  Выберите заднюю поверхность Куба (поверхность осей **YZ**) и кликните OK
5.  Выберите <img alt="" src=images/FEM_ForceConstraint.png  style="width:16px;"> [Создать МКЭ с ограничениями силы](FEM_ConstraintForce/ru.md)
6.  Выберите фронтальную поверхность Куба (грань, параллельная задней поверхности) и установите значение **Area load** в 9000000,00
7.  Установите **Direction** в **-Z** выбором одной из граней параллельно этому направлеию.
8.  Кликните OK

Теперь мы установили ограничения и силы для нашего статического анализа.



### Выбор материала 


<div class="mw-translate-fuzzy">

### Последние приготовления 

1.  Нажмите <img alt="" src=images/FEM_Material.png  style="width:16px;"> [Mechanical material\...](FEM_MaterialSolid/ru.md) и выберете Calculix-Steel в качестве материала.
2.  Нажмите **OK**


</div>



### Создание Mesh 

Рекомендуется создавать mesh в качестве последнего шага при подготовке к анализу из-за привязки к геометрии в FreeCAD. В зависимости от установки FreeCAD, mesh может быть с Netgen или GMSH, вы можете использовать любую из них.

#### Netgen

1.  Выбрать модель
2.  Кликнуть в меню <img alt="" src=images/FEM_Analysis.png  style="width:16px;"> [New mechanical analysis](FEM_Analysis/ru.md), чтобы создать анализ из выбранного объекта
3.  В диалоге создания сетки кликнуть **OK**


<div class="mw-translate-fuzzy">

Вы также можете перетащить сетку в Mechanical Analysis, у которого нет сетки, внутри древа проекта.


</div>

#### GMSH

1.  Select the model
2.  <img alt="" src=images/FEM_MeshGmshFromShape.svg  style="width:24px;"> [FEM mesh from shape by Gmsh](FEM_MeshGmshFromShape.md): Generates a finite element mesh for a model using Gmsh.
3.  In the meshing dialog, click **Apply** and **OK**.

Мы создали сетку для нашего объекта и готовы добавить к нему ограничения и действующие силы.



### Запуск решателя 



#### Стандартный способ 

1.  Выберите объект решателя <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;">, находящийся в контейнере **Analysis**.
2.  Выберите в меню <img alt="" src=images/FEM_SolverControl.svg  style="width:24px;"> [Solver job control](FEM_SolverControl.md)
3.  Выберите **Write .inp File**.
4.  Выберите **Run Calculix**.
5.  Click **OK**.



#### Быстрый способ 


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

Теперь мы закончили с основными принципами работы [FEM Module](FEM_Workbench/ru.md).


</div>


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM tutorial/ru
