---
 GuiCommand:
   Name: Part BooleanFragments
   Name/ru: Part BooleanFragments
   MenuLocation: Деталь , Разделить , Boolean Fragments
   Workbenches: Part_Workbench/ru
   SeeAlso: Part_Slice/ru   Part Slice, Part_XOR/ru, Part_CompJoinFeatures/ru, Part Boolean/ru|Version: 0.17.8053
---

# Part BooleanFragments/ru


</div>



## Описание


<div class="mw-translate-fuzzy">

Инструмент для вычисления всех фрагментов, которые могут возникнуть в результате применения логических операций между входными фигурами. Например, для двух пересекающихся сфер создаются три неперекрывающихся, но соприкасающихся твердых тела.


</div>

![600px](images/Part_BooleanFragments_Demo.png)


<div class="mw-translate-fuzzy">

(на картинке выше части были впоследствии раздвинуты вручную, чтобы показать разрез)


</div>


<div class="mw-translate-fuzzy">

Итоговая форма всегда является компаундом. Состав компаунда зависит от типов входных фигур и режима работы. Это означает, что вы не сразу получаете доступ к отдельным частям результата - части остаются сгруппированными вместе. Отдельные части могут быть извлечены путем применения разбивки соединения ([Draft Downgrade](Draft_Downgrade/ru.md)).


</div>

У инструмента три режима: \"Standard\", \"Split\", and \"CompSolid\".

«Standard» и «Split» различаются действием инструмента на рёбра, оболочки и составные тела: если «Split», они разделяются; если «Standard», они остаются вместе (получают дополнительные сегменты).

Компаундная структура в режимах «Standard» и «Split» следует компаундной структуре на входе. То есть, если вы обработаете два компаунда, каждый из которых содержит сферу, как в примере выше, результат также будет содержать два компаунда, каждый из которых содержит куски изначально входившей в них сферы. Это значит, что общий кусок будет повторен в результате дважды. Только если обе входные сферы не входят в компаунды, результат будет содержать общий кусок единожды.

В режиме «CompSolid» твердые тела объединяются в compsolid (compsolid - это набор твердых тел, соединенных гранями; они связаны с твердыми телами, как полилинии связаны с ребрами, а оболочки связаны с гранями; название, вероятно, является сокращенной фразой «композитное твердое тело»). На выходе получается невложенное соединение compsolids.



## Применение


<div class="mw-translate-fuzzy">

1.  Выбрать объекты для пересечения.
    Порядок выделения не важен, поскольку действие инструмента симметрично. Достаточно выделить по одной подфигуре каждого объекта (например, лица). Вы также можете выбрать соединение, содержащее все соединяемые фигуры, например [Массив](Draft_Array/ru.md).
2.  Вызвать команду Part BooleanFragments несколькими способами:
    -   Нажатие кнопки <img alt="" src=images/Part_BooleanFragments.svg  style="width:24px;"> на панели инструментов
    -   Использование пункта **Деталь → Разделить → Boolean Fragments** в меню Деталь


</div>



## Свойства


{{TitleProperty|Boolean Fragments}}

-    **Objects**: список объектов для пересечения. Обычно требуется как минимум два объекта, но подойдет и одно соединение, содержащее пересекаемые формы. (начиная с FreeCAD v0.17.8053, это свойство не отображается в редакторе свойств и доступно только через Python).

-    **Mode**: «Standard», «Split» или «CompSolid». «Standard» - по умолчанию. «Standard» и «Split» отличаются действием инструмента на фигуры типа агрегирования: если «Split», они разделяются; в противном случае они хранятся вместе (получаются дополнительные сегменты).

-    **Tolerance**: значение \"нечеткости\". Это дополнительный допуск, который следует применять при поиске пересечений в дополнение к допускам, сохраненным во входных формах.



## Детали реализации 


<div class="mw-translate-fuzzy">

Инструмент «Boolean Fragments» в «Стандартном режиме» - это общий оператор Fuse (GFA) из OpenCascade. Он принимает комбинацию, вероятно, всех типов фигур, а логика вывода довольно запутанная. Смотрите [Руководство пользователя OpenCascade: логические операции](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__boolean_operations.html).


</div>

Для режимов «Split» и «CompSolid» FreeCAD выполняет дополнительную постобработку.



## Программирование

Инструмент можно использовать в [макросах](macros/ru.md) и из консоли Python, используя следующую функцию:

**BOPTools.SplitFeatures.makeBooleanFragments(name)**

-   Создает пустую функцию BooleanFragments. Свойство «Объекты» должно быть назначено впоследствии явно.
-   Возвращает вновь созданный объект.

BooleanFragments также может применяться к простым формам, без необходимости наличия объекта документа, с помощью:


{{code|code=
import BOPTools.SplitAPI
BOPTools.SplitAPI.booleanFragments(list_of_shapes, mode, tolerance = 0.0)

# OR, for Standard mode:

list_of_shapes = [App.ActiveDocument.Sphere.Shape, App.ActiveDocument.Sphere001.Shape]
pieces, map = list_of_shapes[0].generalFuse(list_of_shapes[1:], tolerance)
# pieces receives a compound of shapes; map receives a list of lists of shapes, defining list_of_shapes <--> pieces correspondence 
}}

Это может быть полезно для создания пользовательских сценариев Python.

Пример: {{code|code=
import BOPTools.SplitFeatures
j = BOPTools.SplitFeatures.makeBooleanFragments(name= 'BooleanFragments')
j.Objects = FreeCADGui.Selection.getSelection() 
}}

Инструмент сам реализован на Python, см. /Mod/Part/BOPTools/SplitFeatures.py там, где установлен FreeCAD.



## Примечания

Инструмент появился в FreeCAD v0.17.8053. FreeCAD необходимо скомпилировать с OCC 6.9.0 или новее, иначе инструмент будет недоступен.


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part BooleanFragments/ru
