# Part and PartDesign/ru
{{TOCright}}

## Обзор

В течение многих лет широко обсуждались различия и особенности совместного применения верстаков <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> [Part](Part_Workbench/ru.md) и <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> [PartDesign](PartDesign_Workbench/ru.md).

Рекомендуется использовать один из верстаков, пока пользователь не освоится с ним, а затем изучить другой. Также обычно рекомендуется, чтобы новые пользователи не смешивали их, пока не будут понятны последствия этого.

Давайте обсудим эти особенности.

## Концепция Верстака Part 

Верстак Part это по сути [моделирование в стиле КТГ](Constructive_solid_geometry/ru.md). Оператор комбинирует различные примитивы, чтобы в конечном итоге получить представление желаемой формы. (Фактически, Верстак Part идёт на один шаг дальше, чем просто примитивы и позволяет оператору использовать операцию эскиз+выдавливание (или эскиз+вращение, лофт, развертку \...) для создания случайных форм.) При создании каждого примитива или фигуры он не имеет отношения к другим созданным объектам (кроме эскизов и их вложений), является единственным одиночным твердым телом.

![centre\|Solitary solids](images/Part_CSG_Prims.png )

Это условие остается таким до тех пор, пока оператор не использует некоторую операцию для их объединения (обычно это Булева операция, которая складывает или вычитает тела). Каждое твердое тело изначально является отдельным, но операция создает новый объект.

The take away is the single solitary solid bit and the combining them bit.

## Концепция Верстака PartDesign 

В рабочей среде PartDesign объект Body создается, как непосредственное самостоятельное твердое тело.

Первым шагом для создания такого тела может быть аддитивныф примитив, либо форма выдавленная из эскиза, либо из импортированная форма (называемая Base Feature).

Этот исходный блок материала будет последовательно изменяться до тех пор, пока не будет получена желаемая конечная форма (твердая).

Он является совокупностью в том смысле, что каждая операция добавляет или удаляет материал.

По умолчанию \"точка завершения расчета тела\" (tip) - является последней операцией, выполняемой над телом (если она конечно добровольно не сдвинута на определённый шаг построения фигуры). Это текущее и видимое состояние тела, готовое к повторному изменению с помощью следующего инструмента.

Каждый шаг построения тела представляет собой тело сформированное в результате проведения совокупности операций от начального объекта до рассматриваемого объекта.

So **to have the complete solid**, on the one hand the Tip feature must be the last stage of the construction of this solid, and on the other hand **it is the body which must be selected** and not a stage of its construction.

This will make it possible, in the event of a modification, **to always have the last version of the solid represented.**

**Note and additions    *** At each time of the construction, the last function used is the \"Tip\", which can be defined too as \"active stage in the construction of the object\" or \"stage preceding the next action in the construction of the object\". When the object\'s drawing is complete, Tip is naturally the last stage or feature of the construction. But if desired, in case of forgetting, any feature of the construction can be provisionally declared as Tip   * it then becomes the step preceding the next action in the construction of the object, which means that new feature(s) can be inserted anywhere in the construction, **on condition not to create any incompatible with the suite**.

When everything is finished, you have to redeclare the last feature as Tip, which corresponds to the finished object.

![centre\|Твердое тело полученное в результате совокупности операций](images/Part_Design_Cumulativ.png )

На изображении представлено совокупное твердое тело, состоящее из выдавленного эскиза и примитива конуса. Это единое твердое тело.

If Tip on **Pad**, the pad can exist separately, but if Tip on **Cone**, the cone cannot exist separately (Tip on cone = pad + cone).

(Another thing mentioned often is a Body ***MUST*** be a single contiguous solid. This means all geometry created by a feature in the Body *must* touch it\'s predecessor.)

## Совместное применение 

Хотя это и не рекомендуется для новичков, но инструменты из верстаков Part и Part Design можно комбинировать, при условии, что вы знаете, что делаете. Например    *

Люди попадают в ловушку, когда пытаются использовать какую-либо функцию под телом (а не само тело) в качестве одного выбора Булевой операции верстака Part. Это проблема, потому что выбранный элемент не представляет единое твердотельное тело.


<div class="mw-translate-fuzzy">

В некотором смысле, с точки зрения Part Workbench, Body представляет собой еще один примитив. Таким образом, использование Body (помните, что это прокси для подсказки) и объекта Part Workbench для выполнения логического значения допустимо. Но результирующий объект является частью объекта Part Workbench. И, таким образом, инструменты PartDesign Workbench больше нельзя использовать на нем.


</div>

И это может стать еще более сложным. Если вы создадите новое тело и перетащите в него результат из предыдущего абзаца, будет создан базовый объект. И вы можете использовать на нем инструменты PartDesign Workbench.

## Предупреждение

There is a caveat with the Tip and it\'s representation of the single solid in the Body. *If* the tip is a subtractive feature and is used in a dress up operation, for instance a Mirror, the Mirror is operating on the underlying feature (a pocket for example). Thus the cumulative solid is not mirrored, but the subtractive feature is. The result of this must create a single solid.

In this example, a mirror of the tip (which is the pocket of the slot) around any of the base planes, or even a face of the solid will not produce a mirrored solid of the entire model. (In fact, it will produce a Mirrored feature in the tree that is essentially empty.)

![centre\|Обособленные твердые тела](images/PhantomMirror.png )

In this example, a mirror of the tip (which is the pocket of the slot) is performed around the datum plane and produces a mirrored slot   *

![centre\|Обособленные твердые тела](images/PhantomMirror.png )

See the <img alt="" src=images/PartDesign_Mirrored.svg  style="width   *24px;"> [PartDesign Mirrored](PartDesign_Mirrored.md) tool wiki page for more information.

## Сравнение

You can see below the same example built with each of the two workbenches. Of course, there are always several possible construction timelines with each workbench. ![Compare constructions with Part workbench and PartDesign workbench](images/PartWBvsPartDesignWBexample.jpg )

  In <img alt="" src=images/Workbench_PartDesign.svg  style="width   *24px;"> PartDesign workbench                                                                         In <img alt="" src=images/Workbench_Part.svg  style="width   *24px;"> Part workbench
   
  01- <img alt="" src=images/PartDesign_Body.svg  style="width   *32px;"> New body \> <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XZ plane   01- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> Sketch in XZ plane
  ![](images/01sketchXZ_PartWBvsPartDesignWBn.jpg )                                                                                     ![](images/01Psketch_PartWBvsPartDesignWBn.jpg )
                                                                                                                                                                       

   
  02- <img alt="" src=images/PartDesign_Revolution.svg  style="width   *32px;"> Revolution / Z   02- <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> Revolve / Z
  ![](images/02revolutionZ_PartWBvsPartDesignWBn.jpg )      ![](images/02revolveZ_PartWBvsPartDesignWBn.jpg )
                                                                                              
   

   
  03- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XY plane   03- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XY plane
  ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )              ![](images/03sketchXY_PartWBvsPartDesignWBn.jpg )
                                                                                                
   

   
  04- <img alt="" src=images/PartDesign_Pocket.svg  style="width   *32px;"> Pocket      04a- <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> Extrude
  ![](images/04pocket_PartWBvsPartDesignWBn.jpg )   ![](images/04aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
                                                                                 04b- <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> Cut
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/04bCut_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  05- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch in XZ plane   05- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XZ plane
  ![](images/05sketchXZ_PartWBvsPartDesignWB.jpg )                ![](images/05PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                
   

   
  06- <img alt="" src=images/PartDesign_Pad.svg  style="width   *32px;"> Pad sym/XZ          06a- <img alt="" src=images/Part_Extrude.svg  style="width   *32px;"> Extrude sym/XZ
  ![](images/06padSymXZ_PartWBvsPartDesignWB.jpg )   ![](images/06aExtrude_PartWBvsPartDesignWB.jpg )
                                                                                   
   

   
                                                                                 06b- <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width   *32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
                                                                                 06c- <img alt="" src=images/Part_Fuse.svg  style="width   *32px;"> Fusion
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/06cFusion_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  07- <img alt="" src=images/Sketcher_NewSketch.svg  style="width   *32px;"> New Sketch on base planar face   07- <img alt="" src=images/Workbench_Sketcher.svg  style="width   *24px;"> Sketcher workbench \> <img alt="" src=images/Sketcher_NewSketch.svg‎‎  style="width   *32px;"> New Sketch in XZ plane
  ![](images/07sketchBaseSupFace_PartWBvsPartDesignWB.jpg )      ![](images/07PsketchXZ_PartWBvsPartDesignWB.jpg )
                                                                                                        
   

   
  08- <img alt="" src=images/PartDesign_Hole.svg  style="width   *32px;"> Hole - counterbore                08a- <img alt="" src=images/Part_Revolve.svg  style="width   *32px;"> Revolve
  ![](images/08hole-counterbore_PartWBvsPartDesignWB.jpg )   ![](images/08aRevolve_PartWBvsPartDesignWB.jpg )
                                                                                                   
   

   
                                                                                 08b- <img alt="" src=images/Workbench_Draft.svg  style="width   *24px;"> Draft <img alt="" src=images/Draft_PolarArray.svg  style="width   *32px;"> Polar Pattern
  ![](images/00nothing_PartWBvsPartDesignWB.jpg )   ![](images/08bDraftPolarPattern_PartWBvsPartDesignWB.jpg )
                                                                                 
   

   
  09- <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *32px;"> Polar Pattern of Hole and Pad   09- <img alt="" src=images/Part_Cut.svg  style="width   *32px;"> Cut
  ![](images/09polarPatternHoleAndPad_PartWBvsPartDesignWB.jpg )     ![](images/09Cut_PartWBvsPartDesignWB.jpg )
                                                                                                                 
   

Compare the construction trees in the two workbenches as well as their organization and reading timeline    *

   
  10- Construction tree in PartDesign workbench                                        10- Construction tree in Part workbench
  ![](images/PartvsPartDesign_TreePartDesignWB.jpg )   ![](images/PartvsPartDesign_TreePartWB.jpg )
                                                                                       
   

## Заключение

Part and PartDesign workbenches can be used together with some care, creating quite complex models.

[Top](#Top.md)


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Part](Part_Workbench.md) > Part and PartDesign/ru
