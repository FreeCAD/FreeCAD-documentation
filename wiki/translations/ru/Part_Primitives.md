---
- GuiCommand:/ru
   Name:Part Primitives
   Name/ru:Создать примитивы
   MenuLocation:Деталь -> Создать примитивы...
   |Workbenches:[Part(Деталь)](Part_Workbench/ru.md)
   SeeAlso:[Построитель форм](Part_Builder/ru.md)
---

## Описание

Инструмент [Создать примитивы](Part_Primitives/ru.md) запускает диалог создания разнообразных геометрических параметризованных примитивов <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстака Part](Part_Workbench/ru.md).

<img alt="" src=images/Part_Primitives_example.png  style="width:800px;"> 
*Формы примитивов которые можно создать в [верстаке Part(Деталь)](Part_Workbench/ru.md).*

## Применение

Примитивы можно создать следующими способами

\#\* нажмите кнопку **<img src="images/Part_Primitives.svg" width=24px> '''Создание примитивов'''** на панели инструментов.

\#\* перейдите **Деталь → Создать примитивы...** в панели меню.

1.  В появившемся диалоговом окне выберите тип примитива, задайте его параметры и местоположение, наконец нажмите кнопку **Создать**

Диалог остаётся открытым, чтобы впоследствии вы могли создать дополнительные примитивы.

Для редактирования примитивов существует два способа:

Используя диалоговое окно: {{Version/ru|0.19}}

1.  Выберите примитив в древе проекта и сделайте по нему двойной щелчок мышью.
2.  Откроется тоже диалоговое окно, что и при создании примитива. Изменяйте параметры, и вы получите мгновенный предварительный просмотр изменённого примитива.
3.  Для завершения редактирования нажмите **OK**.

Используя [редактор свойств](Property_editor/ru.md):

1.  Выберите примитив в древе проекта.
2.  Отредактируйте его свойства в таблице Свойств.

## Геометрические Примитивы 

Можно создать следующие примитивы:

-   <img alt="" src=images/Part_Plane.svg  style="width:32px;"> [Плоскость](Part_Plane/ru.md): Создаёт плоскость.
-   <img alt="" src=images/Tree_Part_Box_Parametric.svg  style="width:32px;"> [Куб](Part_Box/ru.md): Создаёт куб. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Куб](Part_Box/ru.md).
-   <img alt="" src=images/Tree_Part_Cylinder_Parametric.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md): Создаёт цилиндр. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Cylinder.svg  style="width:32px;"> [Цилиндр](Part_Cylinder/ru.md).
-   <img alt="" src=images/Tree_Part_Cone_Parametric.svg  style="width:32px;"> [Конус](Part_Cone/ru.md): Создаёт конус. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Конус](Part_Cone/ru.md).
-   <img alt="" src=images/Tree_Part_Sphere_Parametric.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md): Создаёт сферу. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Sphere.svg  style="width:32px;"> [Сфера](Part_Sphere/ru.md).
-   <img alt="" src=images/Part_Ellipsoid.svg  style="width:32px;"> [Эллипсоид](Part_Ellipsoid/ru.md): Создаёт эллипсоид.
-   <img alt="" src=images/Tree_Part_Torus_Parametric.svg  style="width:32px;"> [Тор](Part_Torus/ru.md): Создаёт тор. Этот объект также может быть создан с помощью инструмента <img alt="" src=images/Part_Torus.svg  style="width:32px;"> [Тор](Part_Torus/ru.md).
-   <img alt="" src=images/Part_Prism.svg  style="width:32px;"> [Призма](Part_Prism/ru.md): Создаёт призму.
-   <img alt="" src=images/Part_Wedge.svg  style="width:32px;"> [Клин](Part_Wedge/ru.md): Создаёт клин.
-   <img alt="" src=images/Part_Helix.svg  style="width:32px;"> [Винтовая спираль(Helix)](Part_Helix/ru.md): Создаёт винтовую спираль.
-   <img alt="" src=images/Part_Spiral.svg  style="width:32px;"> [Плоская спираль(Spiral)](Part_Spiral/ru.md): Создаёт плоскую спираль.
-   <img alt="" src=images/Part_Circle.svg  style="width:32px;"> [Окружность](Part_Circle/ru.md): Создаёт круглое ребро.
-   <img alt="" src=images/Part_Ellipse.svg  style="width:32px;"> [Эллипс](Part_Ellipse/ru.md): Создаёт эллиптическое ребро.
-   <img alt="" src=images/Part_Point.svg  style="width:32px;"> [Точка](Part_Point/ru.md): Создаёт точку (вершину/vertex).
-   <img alt="" src=images/Part_Line.svg  style="width:32px;"> [Линия](Part_Line/ru.md): Создаёт линию (ребро).
-   <img alt="" src=images/Part_RegularPolygon.svg  style="width:32px;"> [Правильный Многоугольник](Part_RegularPolygon/ru.md): Создаёт правильный многоугольник.

## Написание сценариев 


**Смотри так же:**

[Написание сценариев](Part_scripting/ru.md)

Протестируйте создание примитивов с помощью скрипта. {{Version/ru|0.19}}

Его можно запустить из [консоли Python](Python_console/ru.md). 
```python
import parttests.part_test_objects as pto
pto.create_test_file("example_file")
```

Этот скрипт расположен в каталоге установки программы, и может быть изучен, чтобы узнать, как строятся базовые примитивы. 
```python
$INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```

Также он может быть использован в качестве входных данных для программы. 
```python
freecad $INSTALL_DIR/Mod/Part/parttests/part_test_objects.py
```





 
