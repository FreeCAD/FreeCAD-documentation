---
- GuiCommand   */ru
   Name   *Part_Chamfer
   Name/ru   *Фаска
   MenuLocation   *Деталь → Фаска
   Workbenches   *[Part(Деталь)](Part_Workbench/ru.md)
   SeeAlso   *[Скругление](Part_Fillet/ru.md)
---

# Part Chamfer/ru

## Описание

Снимает фаски с выбранных рёбер объекта. Диалоговое окно позволяет выбрать, с какой кромкой(кромками) работать, а также изменить различные параметры фаски.

![Chamfer example](images/Chamfer-example.png )

## Применение

1.  Существует несколько способов для вызова данной команды   *
    -   Нажатием кнопки **<img src="images/Part_Chamfer.svg" width=16px> Фаска** на панели инструментов.
    -   Через пункт главного меню **Деталь → Фаска**.
2.  В открывшемся диалоговом окне выберите фигуру для снятия фаски.
3.  Выберите кромки для снятия фаски, установив соответствующий флажок в диалоговом окне \"Снятие фаски\" или выбрав их непосредственно на модели.
4.  Отредактируйте параметры фаски.
5.  Нажмите **OK**, чтобы закрыть диалоговое окно Фаска и применить её.

## Опции

![Dialog-chamfer](images/Dialog-chamfer-ru.png )

-   При выборе кромок на модели у вас есть возможность выбрать по кромке или по грани. При выборе по грани будут выбраны все граничные края этой грани.
-   Фаска постоянной длины или фаска переменной длины.
    -   Фаска постоянной длины создаст фаску с краями, равноудаленными от исходной кромки на указанном расстоянии.
    -   Фаска переменной длины будет иметь кромки, которые могут быть установлены на разных расстояниях от исходной кромки, что позволяет создавать фаску под переменным углом.

## Свойства

![Свойства Фаски](images/Part_Chamfer-Properties-ru.png )


{{Properties_Title|Основание}}

-    {{PropertyData/ru|Основание}}   * Форма, к которой должна быть применена фаска.

-    {{PropertyData/ru|Placement}}   * Задаёт ориентацию и положение фигуры в 3D-пространстве.

-    {{PropertyData/ru|Label}}   * Ярлык, присвоенный объекту. Можете изменить его в соответствии с вашими потребностями.




## Ограничения

Фаска может не сработать, если результат будет касаться или пересечёт следующее соседнее ребро. Поэтому, если вы не получили ожидаемого результата, попробуйте использовать меньшее значение. Это относится и для <img alt="" src=images/Part_Fillet.svg  style="width   *24px;"> [Скругления](Part_Fillet/ru.md).

Также обратите внимание, что на функцию фаски детали влияет [Topological naming problem (Проблема топологического именования)](Topological_naming_problem/ru.md), когда любое изменение выполняется на этапе моделирования ранее в цепочке, которое влияет на количество граней или вершин. Это может привести к непредсказуемому результату. До тех пор, пока это не будет решено (возможно, с V0.20), рекомендуется применять операции фаски и [Скругление](Part_Fillet/ru.md) на последних этапах цепочки моделирования.

## Программирование

Инструмент Фаски можно использовать в [Макросах](Macros/ru.md) и из консоли [Python](Python/ru.md), добавив объект Фаска в документ.

**Пример сценария(скрипта)   ***


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part   *   *Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
chmfr = FreeCAD.ActiveDocument.addObject("Part   *   *Chamfer", "myChamfer")
chmfr.Base = FreeCAD.ActiveDocument.myCube
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
chmfr.Edges = myEdges
FreeCADGui.ActiveDocument.myCube.Visibility = False
FreeCAD.ActiveDocument.recompute()
```

**Объяснения к Сценарию из примера   ***


```python
import Part
cube = FreeCAD.ActiveDocument.addObject("Part   *   *Feature", "myCube")
cube.Shape = Part.makeBox(5, 5, 5)
```

-   Создаёт куб размером 5 мм, к которому мы можем применить фаски. Смотри [Part\_API](Part_API/ru.md) для объяснения метода makeBox.


```python
chmfr = FreeCAD.ActiveDocument.addObject("Part   *   *Chamfer", "myChamfer")
```

-   Добавляет в документ новый объект типа Chamfer/Фаска (из модуля Part/Деталь) с ярлыком \"myChamfer\".


```python
chmfr.Base = FreeCAD.ActiveDocument.myCube
```

-   Указывает, что базовая форма объекта фаски должна быть \"myCube\".


```python
myEdges = []
myEdges.append((1, 1.5, 1.25)) # (edge number, chamfer start length, chamfer end length)
myEdges.append((2, 1.5, 1.25))
myEdges.append((3, 1.5, 1.25))
myEdges.append((4, 1.5, 1.25))
myEdges.append((5, 1.5, 1.25))
myEdges.append((6, 1.5, 1.25))
myEdges.append((7, 1.5, 1.25))
myEdges.append((8, 1.5, 1.25))
myEdges.append((9, 1.5, 1.25))
myEdges.append((10, 1.5, 1.25))
myEdges.append((11, 1.5, 1.25))
myEdges.append((12, 1.5, 1.25))
```

-   Создаёт пустой массив \"myEdges\", а затем наполняет массив с параметрами фаски для каждого края.
-   Синтаксис для каждого элемента должен быть следующим (edge\#, chamfer start length, chamfer end length)/(номер кромки, длина начала фаски, длина окончания фаски).


```python
chmfr.Edges = myEdges
```

-   Устанавливает атрибут Edges/Рёбра нашего объекта Chamfer/Фаска равным массиву, который мы только что создали.


```python
FreeCADGui.ActiveDocument.myCube.Visibility = False
```

-   Эта строка просто скрывает \"myCube\", так что наш недавно созданный объект \"myChamfer\" является единственным видимым.


```python
FreeCAD.ActiveDocument.recompute()
```

-   Пересчитывает все измененные компоненты на экране и обновляет дисплей.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Chamfer/ru
