# Part and PartDesign/ru
## Обзор

В течение многих лет широко обсуждались различия и особенности совместного применения верстаков <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part](Part_Workbench/ru.md) и <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/ru.md).

Рекомендуется использовать один из верстаков, пока пользователь не освоится с ним, а затем изучить другой. Также обычно рекомендуется, чтобы новые пользователи не смешивали их, пока не будут понятны последствия этого.

Давайте обсудим эти особенности.



## Концепция Верстака Part 

Верстак Part это по сути [моделирование в стиле КТГ](Constructive_solid_geometry/ru.md). Оператор комбинирует различные примитивы, чтобы в конечном итоге получить представление желаемой формы. (Фактически, Верстак Part идёт на один шаг дальше, чем просто примитивы, и позволяет оператору использовать операцию эскиз+выдавливание (или эскиз+вращение, профиль (loft), профиль по траектории (sweep) \...) для создания случайных форм.) При создании каждого примитива или фигуры он не имеет отношения к другим созданным объектам (кроме эскизов и их вложений), является единым твёрдым телом.

![centre\|Одиночные твёрдые тела](images/Part_CSG_Prims.png )

Это условие остается таким до тех пор, пока оператор не использует некоторую операцию для их объединения (обычно это Булева операция, которая складывает или вычитает тела). Каждое твёрдое тело изначально является отдельным, но операция создает новый объект.

Результатом является единый твёрдый объект и комбинация объектов.



## Концепция Верстака PartDesign 

В Верстаке PartDesign объект Body создаётся непосредственно как одиночное самостоятельное твёрдое тело.

Первым шагом в теле должен быть блок материала, созданного либо из аддитивного примитива, либо из выдавленного эскиза, либо из импортированной формы (далее называемая Базовым Элементом).

Этот исходный блок материала будет последовательно изменяться до тех пор, пока не будет получено желаемое конечное твёрдое тело.

Он является совокупностью операций в том смысле, что каждая операция добавляет или удаляет материал.

По умолчанию \"точка завершения расчета тела\" (tip) - является последней операцией, выполняемой над телом (если она конечно добровольно не сдвинута на определённый шаг построения фигуры). Это текущее и видимое состояние тела, готовое к повторному изменению с помощью добавления следующего конструктивного элемента.

Каждый шаг построения тела представляет собой тело сформированное в результате проведения совокупности операций от начального конструктивного элемента до текущего конструктивного элемента.

Таким образом, **чтобы иметь законченное твёрдое тело**, с одной стороны точка завершения расчёта должна быть последним этапом построения этого тела, а с другой стороны **должно быть выбрано тело**, а не этап его построения.

Это позволит в случае изменений **всегда иметь последнюю версию твёрдого тела**.

**Note and additions :** At each time of the construction, the last function used is the \"Tip\", which can be defined too as \"active stage in the construction of the object\" or \"stage preceding the next action in the construction of the object\". When the object\'s drawing is complete, Tip is naturally the last stage or feature of the construction. But if desired, in case of forgetting, any feature of the construction can be provisionally declared as Tip: it then becomes the step preceding the next action in the construction of the object, which means that new feature(s) can be inserted anywhere in the construction, **on condition not to create any incompatible with the suite**.

When everything is finished, you have to redeclare the last feature as Tip, which corresponds to the finished object.

![centre\|Твердое тело полученное в результате совокупности операций](images/Part_Design_Cumulativ.png )

На изображении представлено совокупное твердое тело, состоящее из выдавленного эскиза и примитива конуса. Это единое твердое тело.

Если конечной точкой расчёта тела является **выдавленный эскиз**, то выдавленный эскиз будет отображен как отдельное тело, однако если конечной точкой расчета является **Конус**, то конус не будет отображен как отдельное тело (а будет отображен, как конус соединенный с выдавленным эскизом).

(Еще одно важное замечание: Тело ***ДОЛЖНО*** быть монолитным. Это означает, что новые, создаваемые конструктивные элементы, *всегда должны* соприкасаться с Телом к которому они применены.)



## Совместное применение 

Хотя это и не рекомендуется для новичков, но инструменты из верстаков Part и PartDesign можно комбинировать, при условии, что вы знаете, что делаете. Например :

Люди попадают в ловушку, когда пытаются использовать какой-либо конструктивный элемент из Тела (а не само Тело) в качестве одного из объектов Булевой операции верстака Part. Это проблема, потому что выбранный конструктивный элемент не является **ПОЛНОЦЕННЫМ** твёрдое тело.

В некотором смысле, с точки зрения верстака Part, Тело представляет собой ещё один примитив. Таким образом, использование Тела (помните, что это прокси для точки завершения расчёта тела) и объекта верстака Part для выполнения Булевых операций допустимо. Но результирующий объект является частью объекта верстака Part. Поэтому инструменты верстака PartDesign больше нельзя использовать на нём.

И это может стать ещё сложнее. Если вы создадите новое Тело и перетащите в него результат из предыдущего абзаца, будет создан BaseObject. И вы можете перейти к использованию инструментов Верстака PartDesign на нём.



## Предупреждение

There is a caveat with the Tip and it\'s representation of the single solid in the Body. *If* the tip is a subtractive feature and is used in a dress up operation, for instance a Mirror, the Mirror is operating on the underlying feature (a pocket for example). Thus the cumulative solid is not mirrored, but the subtractive feature is. The result of this must create a single solid.

In this example, a mirror of the tip (which is the pocket of the slot) around any of the base planes, or even a face of the solid will not produce a mirrored solid of the entire model. (In fact, it will produce a Mirrored feature in the tree that is essentially empty.)

![centre\|Одиночные твёрдые тела](images/PhantomMirror.png )

In this example, a mirror of the tip (which is the pocket of the slot) is performed around the datum plane and produces a mirrored slot:

![centre\|Одиночные твёрдые тела](images/MirroredSlot.png )

Дополнительные сведения смотри на вики-странице инструмента <img alt="" src=images/PartDesign_Mirrored.svg  style="width:24px;"> [Симметрия PartDesign](PartDesign_Mirrored/ru.md).



## Сравнение

Ниже представлен один и тот же пример, созданный и тем и другим верстаком. Конечно, помимо ниже представленных способов для каждого из верстаков всегда существует множество возможных способов для построения данного Тела. ![Сравнение построения верстаками Part и PartDesign](images/PartWBvsPartDesignWBexample.jpg )

+++
| В <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> верстаке PartDesign                                                                                    | В <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> верстаке Part                                                                                                                |
+===============================================================================================================================================================================+=========================================================================================================================================================================================+
| 01- <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> Создать тело \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Создать эскиз на плоскости XZ | 01- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> верстак Sketcher \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Создать эскиз на плоскости XZ |
+++
| ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                              | ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )                                                                                                          |
+++
|                                                                                                                                                                               |                                                                                                                                                                                         |
+++

+++
| 02- <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> Вращение / Z | 02- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Вращать / Z             |
+++
| ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )  | ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg ) |
+++
|                                                                                         |                                                                                  |
+++

+++
| 03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Создать эскиз на плоскости XY | 03- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> верстак Sketcher \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Создать эскиз на плоскости XY |
+++
| ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                   | ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )                                                                                                        |
+++
|                                                                                                    |                                                                                                                                                                                         |
+++

+++
| 04- <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> Вырез     | 04a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Выдавить             |
+++
| ![](images/04pocket_PartWBvsPartDesignWBn.jpg ) | ![](images/04aExtrude_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                                |
+++

+++
|                                                                              | 04b- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Обрезать             |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/04bCut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                        |
+++

+++
| 05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Создать эскиз на плоскости XZ | 05- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> верстак Sketcher \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Создать эскиз на плоскости XZ |
+++
| ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                     | ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                        |
+++
|                                                                                                    |                                                                                                                                                                                         |
+++

+++
| 06- <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> Выдавливание sym/XZ | 06a- <img alt="" src=images/Part_Extrude.svg  style="width:32px;"> Выдавить sym/XZ      |
+++
| ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )   | ![](images/06aExtrude_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                  |                                                                                |
+++

+++
|                                                                              | 06b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> верстак Draft <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Массив вращения |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                         |
+++
|                                                                              |                                                                                                                                                            |
+++

+++
|                                                                              | 06c- <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> Объединение              |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/06cFusion_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                              |                                                                              |
+++

+++
| 07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> Создать эскиз на базовой плоской грани | 07- <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> верстак Sketcher \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width:32px;"> Создать эскиз на плоскости XZ |
+++
| ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )            | ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )                                                                                                        |
+++
|                                                                                                             |                                                                                                                                                                                         |
+++

+++
| 08- <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> Отверстие - цековка             | 08a- <img alt="" src=images/Part_Revolve.svg  style="width:32px;"> Вращать              |
+++
| ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg ) | ![](images/08aRevolve_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                |                                                                                |
+++

+++
|                                                                              | 08b- <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> верстак Draft <img alt="" src=images/Draft_PolarArray.svg  style="width:32px;"> Массив вращения |
+++
| ![](images/00nothing_PartWBvsPartDesignWB.jpg ) | ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )                                                         |
+++
|                                                                              |                                                                                                                                                            |
+++

+++
| 09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> Круговой массив Отверстия и Выдавливания | 09- <img alt="" src=images/Part_Cut.svg  style="width:32px;"> Обрезать            |
+++
| ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )              | ![](images/09Cut_PartWBvsPartDesignWB.jpg ) |
+++
|                                                                                                                         |                                                                      |
+++

Сравните древа построения на двух верстаках, а также их организацию и посмотрите график :

+++
| 10- Древо построения в верстаке PartDesign                                         | 10- Древо построения в верстаке Part                                   |
+++
| ![](images/PartvsPartDesign_TreePartDesignWB.jpg ) | ![](images/PartvsPartDesign_TreePartWB.jpg ) |
+++
|                                                                                    |                                                                        |
+++



## Заключение

Верстаки Part и PartDesign можно с осторожностью использовать вместе, создавая довольно сложные модели.

[Наверх](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/ru
