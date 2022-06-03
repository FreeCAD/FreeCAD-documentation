---
- GuiCommand   */ru
   Name/ru   *Аддитивный профиль
   Name   *PartDesign_AdditiveLoft
   MenuLocation   *Part Design → Create an additive feature → Аддитивный профиль
   Workbenches   *[PartDesign](PartDesign_Workbench/ru.md)
   Version   *0.17
   SeeAlso   *[Аддитивная трубный профиль](PartDesign_AdditivePipe/ru.md), [Субтрактивный профиль](PartDesign_SubtractiveLoft/ru.md)
---

# PartDesign AdditiveLoft/ru

## Описание

**Additive Loft** creates a solid in the active Body by making a transition between two or more sketches (also referred to as cross-sections). If the Body already contains features, the additive loft will be merged to them.

![](images/PartDesign_AddLoft_example.png ) 
*On the left   * cross-sections (A), (B) and (C); created Additive loft on the right.*

## Применение

### Применение через диалог 

1.  Press the **[<img src=images/PartDesign_AdditiveLoft.svg style="width   *24px"> [Additive loft](PartDesign_AdditiveLoft.md)** button.
2.  In the **Select feature** dialog select a sketch to be used as base profile object and click **OK**.
    -   Alternatively, either a single sketch or the face of a 3D object (<small>(v0.20)</small> ) can be selected prior to pressing the Additive loft button.
3.  In the **Loft parameters**, press the **Add Section** button.
4.  Select the next sketch in the [3D view](3D_view.md). Repeat to select more sketches in the order you want them to be lofted through. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
5.  Set options if needed and click **OK**.

### Применение в текущем Виде, напрямую 


<small>(v0.19)</small> 

1.  Select several sketches. It is hereby important in what order you select them   *
    -   The sketch selected at first will become the base profile object in the next step
    -   The sketches selected after the first one will become the loft sections. Also here the selection order is important   * The sketch selected as second will become the first loft section, the one selected as third becomes the second section and so on. (You can change the section order any time later in the loft dialog by dragging sections in the list to the desired position.<small>(v0.19)</small> )
    -   The first or last selection can also be a face of a 3D object (<small>(v0.20)</small> )
2.  Press the **[<img src=images/PartDesign_AdditiveLoft.svg style="width   *24px"> [Additive loft](PartDesign_AdditiveLoft.md)** button.
3.  Set options if needed and click **OK**.

## Опции

-   **Управление поверхностью**   * делает прямолинейные переходы между поперечными сечениями. Не оказывает никакого эффекта, в случае если профиль формируется только по двум поперечными сечениям. Если пункт не установлен, переходы между сечениями будут плавными.
-   **Замкнуть форму**   * выполняет переход от последнего поперечного сечения к первому, создавая замкнутую форму.

## Свойства

-    **Label**   * name given to the operation, this name can be changed at convenience.

-    **Sections**   * lists the sections used.

-    **Ruled**   * see [Options](#Options.md).

-    **Closed**   * see [Options](#Options.md).

-    **Refine**   * true or false. If set to true, cleans the solid from residual edges left by features. See [Part RefineShape](Part_RefineShape.md) for more details.

-    **Profile**   * the see base profile object of the loft.

-    **Midplane**   * non applicable.

-    **Reversed**   * non applicable.

-    **Up To Face**   * non applicable.

-    **Allow Multi Face**   * non applicable.

## Notes


<div class="mw-translate-fuzzy">

-   Эскизы должны иметь замкнутые контуры.
-   Невозможно сделать профиль через в вершину.
-   Поперечное сечение не может лежать в той же плоскости, что и непосредственно предшествующее ему.
-   Чтобы лучше контролировать форму профиля, рекомендуется, чтобы все поперечные сечения имели одинаковое количество сегментов. Например, для профиля создаваемого между прямоугольником и окружностью окружность желательно разбить на 4 соединенные дуги.
-   Профиль будет создан в том порядке, в котором были добавлены поперечные сечения
-   Если эскиз имеет внутреннюю геометрию, т. е. в профиле должны быть отверстия, то порядок создания геометрии эскиза должен быть одинаковым для всех секций   * либо начните все секции с внутренней геометрии, либо начните их все с внешней. В противном случае может быть создан некорректный профиль, в котором пересекаются внутренние и внешние стенки фигуры.


</div>

## Ссылки

-   [Part Loft Technical Details](Part_Loft_Technical_Details.md) explains how a [Part Loft](Part_Loft.md) is created, much of its content is relevant to the PartDesign Additive loft.





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveLoft/ru
