---
- GuiCommand:/ru
   Name:Part Slice
   Name/ru:Part Slice
   MenuLocation:Деталь → Split → Slice
   Workbenches:[Part](Part_Workbench/ru.md)
   Version:0.17
   SeeAlso:[Part Boolean Fragments](Part_BooleanFragments/ru.md), [Part XOR](Part_XOR/ru.md), [Part Join features](Part_CompJoinFeatures/ru.md), [Part Boolean](Part_Boolean/ru.md)
---

# Part Slice/ru


</div>

## Описание

Команда <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Разрезать](Part_Slice/ru.md), которую также можно применить, чтобы \"сделать надрез\", это инструмент, используемый для разделения фигур через пересечение с другими фигурами. Например, из куба будет создана композиция из двух тел, если разрезать его плоскостью.

![600px](images/Part_Slice_Demo.png)


*Выше: части были впоследствии раздвинуты вручную, чтобы показать разрез*


<div class="mw-translate-fuzzy">

Имеются две команды для разделения фигуры: <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> _. Они оба создают параметрический объект «Срез», который объединяет разрезанные части в компаунд. В то же время <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Slice Apart](Part_SliceApart/ru.md) разбивает полученное соединение на отдельные объекты. «Slice to compound» полностью параметрический, и не имеет проблем при изменении количества частей. «Slice apart» не будет обновлять количество объектов при изменении числа частей.


</div>


<div class="mw-translate-fuzzy">

Итоговая форма занимают то же место, что и оригинал. Но она разделена там, где пересекается с другими формами. Разделенные части складываются в компаунд (или композит), поэтому кажется, что объект остается одним целым. Вам нужно взорвать соединение, чтобы получить отдельные части. Если вы хотите получить доступ к отдельным частям параметрическим способом, вы можете использовать для этой цели <img alt="" src=images/Part_CompoundFilter.svg  style="width:24px;"> _.


</div>

Инструмент имеет три режима: «Standard», «Split» и «CompSolid». Формы выбора нет, они предопределены, но доступны после операции на уровне результирующих срезов.

«Standard» и «Split» различаются действием инструмента на рёбра, оболочки и составные тела: если «Split», они разделяются; если «Standard», они остаются вместе (получают дополнительные сегменты).

Составная структура в режимах «Standard» и «Split» следует за составной структурой разрезаемой формы.

В режиме «CompSolid» на выходе получается compsolid (или соединение compsolids, если полученные твердые тела образуют более одного острова связности). Compsolid - это набор тел, соединенных гранями; они связаны с твердыми телами, как полилинии связаны с ребрами, а оболочки связаны с гранями; название, вероятно, является сокращённым словосочетанием «композитное твердое тело».


<div class="mw-translate-fuzzy">

Общее действие инструмента очень похоже на <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Boolean Fragments](Part_BooleanFragments/ru.md), за исключением того, что в результате получаются части только из первой формы.


</div>

## Применение


<div class="mw-translate-fuzzy">

1.  Сначала выберите объект для нарезки, а затем несколько объектов чтобы резать.
    Порядок выбора важен. Соединения с самопересечениями не допускаются (самопересечения иногда можно учесть, передав соединение через <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [BooleanFragments](Part_BooleanFragments/ru.md))
2.  Вызвать команду Part Slice одним из способов:
    -   Нажмите кнопку <img alt="" src=images/Part_Slice.svg  style="width:24px;"> [Part Slice](Part_Slice/ru.md) на панели инструментов Part
    -   Используйте пункт **Деталь → Разделить → Slice apart** в меню Деталь


</div>

1.  Примечаниеː Объекты для разрезания должны полностью разделять объект, который нужно нарезать. Таким образом, куб не может быть разрезан проволокой, а может быть разрезан, например, плоскостью, полученной экструдированием проволоки.


<div class="mw-translate-fuzzy">

Создается параметрический объект Slice. Исходные объекты скрываются, а результат пересечения показываются в [Окне трёхмерного вида](3D_view/ru.md).


</div>


<div class="mw-translate-fuzzy">

### Древовидная структура Slice 

Команда Slice создаёт нарезанный объект. В следующем примере куб разрезается гранью.


</div>

Создаётся ннарезка, и каждый её фрагмент объединяется в компаунд.

![](images/Part_SliceTree.png )

## Свойства


{{TitleProperty|Slice}}

-    **Base**: объект для нарезки.

-    **Tools**: список объектов для нарезки. (начиная с FreeCAD v0.17.8053, это свойство не отображается в редакторе свойств и доступно только через Python).

-    **Mode**: «Standard», «Split» или «CompSolid». \"Разделить\" по умолчанию. Стандартный и Разделить отличаются действием инструмента на фигуры типа агрегирования: если Разделить, они разделяются; в противном случае они хранятся вместе (получаются дополнительные сегменты).

-    **Tolerance**: значение \"нечеткости\". Это дополнительный допуск, который следует применять при поиске пересечений в дополнение к допускам, сохраненным во входных формах.

̈Примечаниеː Свойства доступны на внутреннем объекте срезов, а не на уровне результата.

## Пример

### Создание головоломки 


<div class="mw-translate-fuzzy">

1.  Переключитесь на <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [Sketcher Workbench](Sketcher_Workbench/ru.md)
    -   Создайте новый эскиз.
    -   Нарисуйте прямоугольник, который обозначит общую форму головоломки.
    -   Закройте эскиз.
        ![320px](images/slice_example_step1.png)
2.  Переключитесь на <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак Part](Part_Workbench/ru.md).
    -   Выберите эскиз и выберите **Деталь → Create face from sketch**.
        ![320px](images/slice_example_step2.png)
3.  Вернитесь к <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> [верстаку Sketcher](Sketcher_Workbench/ru.md)
    -   Создайте еще один эскиз на той же плоскости.
    -   Используя инструмент полилинии, нарисуйте линии, которые разделят головоломку на части.
        ![320px](images/slice_example_step3.png)
4.  Вернитесь к <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Верстак Part](Part_Workbench/ru.md).
    -   Выделите эскиз разделителя и используйте <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> [Part Boolean Fragments](Part_BooleanFragments/ru.md). Это вставит вершины в места пересечения линий эскиза разделителя. Их наличие необходимо для работы на следующем этапе.
        ![320px](images/slice_example_step4.png)
5.  Выберите прямоугольную грань и BooleanFragments эскиза разделителя и используйте <img alt="" src=images/Part_Slice.svg  style="width:24px;"> Part Slice.
    ![320px](images/slice_example_step5.png)
6.  Используйте <img alt="" src=images/Part_ExplodeCompound.svg  style="width:24px;"> [Part ExplodeCompound](Part_ExplodeCompound/ru.md) к разрезанной грани, чтобы разбить соединение, созданное Part Slice, на отдельные части.


</div>


<div class="mw-translate-fuzzy">

**Примечание:** Шаги 5 и 6 можно выполнить одним щелчком мыши, используя <img alt="" src=images/Part_SliceApart.svg  style="width:24px;"> [Part SliceApart](Part_SliceApart/ru.md)


</div>

## Примечания


<div class="mw-translate-fuzzy">

-   Инструмент был представлен в FreeCAD v0.17.8053. FreeCAD необходимо скомпилировать с OCC 6.9.0 или новее; иначе инструмент будет недоступен.
-   ̈Свойства доступны на внутреннем объекте срезов, а не на уровне результата.
-   Нарезающие объекты должны полностью разделять объект, который нужно нарезать. Таким образом, куб не может быть разрезан проволокой, а может быть разрезан, например, плоскостью, полученной из экструдированной проволоки.
-   Нарезанный объект должен пройти проверку BOP. См. <img alt="" src=images/Part_CheckGeometry.svg  style="width:24px;"> [Part CheckGeometry](Part_CheckGeometry/ru.md).


</div>

## Программирование


<div class="mw-translate-fuzzy">

Инструмент можно использовать в [макросах](macros/ru.md) и из консоли Python, используя следующую функцию:


</div>


```pythonBOPTools.SplitFeatures.makeSlice(name)```

-   Создает пустую функцию Slice. Свойства \'Base\' и \'Tools\' должны быть назначены впоследствии явно.
-   Возвращает вновь созданный объект.

Slice также может применяться к простым формам, без необходимости наличия объекта документа, с помощью: 
```pythonBOPTools.SplitAPI.slice(base_shape, tool_shapes, mode, tolerance = 0.0)``` Это может быть полезно для создания пользовательских сценарных атрибутов на Python.

Пример: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeSlice(name= 'Slice')
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tools = FreeCADGui.Selection.getSelection()[1:]
}}

Сам инструмент выполнен на Python, смотрите {{FileName|/Mod/Part/BOPTools/SplitFeatures.py}} ([GitHub link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/SplitFeatures.py)) внутри каталога установки FreeCAD.

## Учебники

-   [FreeCad 0.18 Part WB using Slice and Slice Apart](https://www.youtube.com/watch?v=tzHkQaHgrfQ) (English language), author: Ha Gei

-   [FreeCAD Slice und Slice Apart und andere Tricks](https://www.youtube.com/watch?v=JJAL5JmqqKQ) (German language), author: Ha Gei


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Slice/ru
