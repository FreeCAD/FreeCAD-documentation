---
- GuiCommand:/ru
   Name/ru:Проверить эскиз
   Name:Sketcher_ValidateSketch
   MenuLocation:Sketch → Проверить эскиз
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md), [PartDesign](PartDesign_Workbench/ru.md)
   SeeAlso:[Ограничить совпадение](Sketcher_ConstrainCoincident/ru.md), [Topological naming problem](Topological_naming_problem/ru.md)
---

# Sketcher ValidateSketch/ru


</div>

## Описание


<div class="mw-translate-fuzzy">

Утилита **Проверить эскиз** может использоваться для анализа и восстановления эскиза, который больше не редактируется, имеет неверные ограничения, или для добавления утерянных [ограничений совпадения](Sketcher_ConstrainCoincident/ru.md) в эскизе, созданном из импортированной геометрии, такой как файлы DXF. Он также может быть полезен при поиске отсутствующих совпадений в собственных эскизах, которые генерирует ошибку «невозможно проверить сломанную грань» при попытке применить инструмент PartDesign-а.


</div>

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*The Sketcher validation task panel*

## Применение


<div class="mw-translate-fuzzy">

1.  Выберите эскиз для проверки, либо в [дереве модели](Tree_view/ru.md), либо щелкнув по одному из его ребер в [3D-виде](3D_view/ru.md).

    :   **Примечание:** эскиз не должен быть в режиме редактирования. Если вы находитесь в режиме редактирования эскиза, вам нужно использовать кнопку **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Покинуть эскиз](Sketcher_LeaveSketch/ru.md)**, или кнопку **Close** наверху панели задач.
2.  Откройте утилиту проверки эскиза либо:
    -   из ниспадающего меню **Sketch → Проверить набросок**
    -   нажав кнопку <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> в <img alt="Sketcher\_Workbench" src=images/Workbench_Sketcher.svg  style="width:16px;"> [верстаке Sketcher](Sketcher_Workbench/ru.md).
3.  Ознакомьтесь с [Параметрами](#Options/ru.md) для работы, ниже.
4.  Нажмите кнопку **Закрыть** когда закончите.


</div>

## Опции

### Пропавшие совпадения 

Обнаружение пропущенных совпадений для перекрывающихся вершин и добавление их. Нажмите кнопку **Найти**; появится всплывающее диалоговое окно, с сообщением, сколько пропущенных совпадений было найдено; они будут показаны в 3D виде желтыми крестиками. Нажмите кнопку **OK** что бы закрыть диалог, потом нажмите кнопку **Исправить** что бы добавить недостающие совпадения.

При необходимости определите большее значение допуска в выпадающем поле.

Press **Highlight open vertexes** to highlight vertexes that are outside this tolerance.

This tolerance is also used by the **Find**/**Fix** process.

Установите флажок \"Игнорировать вспомогательную геометрию\", чтобы игнорировать вспомогательную геометрию при анализе.

### Неверные ограничения 

Проверяет наличие некорректных ограничений.

For example, if there is a Circle-Line-Tangent constraint, but it references two lines, it is considered invalid.

(This sometimes happens due to the [Topological naming problem](Topological_naming_problem.md), i.e. the external geometry changes type).

It also does other checks, such as for empty links.

### Degenerated geometry 

Degenerated geometry can result from solver actions in a sketch.

For instance, if a line is forced to shorten to become almost a point.

Other examples: a zero length line or zero radius circle/arc.

### Перевернутая внешняя геометрия 

Перевернутая внешняя геометрия может произойти из-за того, что обработка перевернутой геометрии была изменена около версии 0.15.

This process might be helpful if sketches with external-geometry fail to solve because of these changes.

### Блокировка ориентации ограничений 

Реализованы касательные и перпендикулярные ограничения (через точку).

Internally they work by constraining the angle between tangent vectors. With tangent constraint for example, the angle can be 0 or 180 degrees (co-directed or opposed vectors). The actual angle is remembered in the constraint data (\"constraint orientation is locked\"), it guards against flipping. But the angle can be erased (\"constraint orientation unlock\") or updated; these tools do exactly that.

The locking mechanism typically works well and this tool should not be needed. **It should only used after making a backup of the open document.**





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/ru
