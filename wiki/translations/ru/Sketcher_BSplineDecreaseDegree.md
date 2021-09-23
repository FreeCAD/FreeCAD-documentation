---
- GuiCommand:/ru
   Name/ru:Уменьшить степень B-сплайна
   Name:Sketcher_BSplineDecreaseDegree
   MenuLocation:Sketch → B-сплйан инструменты эскиза → Уменьшить степень B-сплайна
   Workbenches:[Sketcher](Sketcher_Workbench/ru.md)
   Version:0.19
   SeeAlso:[Показать/скрыть степень B-сплайна](Sketcher_BSplineDegree/ru.md), [Увеличить степень B-сплайна](Sketcher_BSplineIncreaseDegree/ru.md)
---

# Sketcher BSplineDecreaseDegree/ru

## Описание

Уменьшает степень (порядок) B-сплайна (дополнительную информацию о B-сплайнах см. [на этой странице](B-Splines/ru.md)).

B-сплайны в основном представляют собой комбинацию [кривых Безье](https://en.wikipedia.org/wiki/Bezier_curve#Constructing_B%C3%A9zier_curves) (хорошо рассмотренных в [этом](https://www.youtube.com/watch?v=bE1MrrqBAl8) и [этом](https://www.youtube.com/watch?v=xXJylM2S72s) видео).

В кубическом сплайне (3-ей степени) представленном ниже, есть 3 сегмента, то есть 3 кривые соединены в 2 узла (степень обозначена числом, отображение может быть изменено с помощью кнопки на панели инструментов **<img src=images/Sketcher_BSplineDegree.svg style="width:24px"> [Показать/скрыть степень B-сплайна](Sketcher_BSplineDegree/ru.md)**):

<img alt="" src=images/Sketcher_BSplineDegree3.png  style="width:400px;"> 
*B-сплайн со степенью 3 и 2 узлами, каждый из которых имеет кратность 1.*

The outer segments have each 2 control points, the inner one none to fulfill the constraint that the knots have multiplicity 1. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) for an explanation of the multiplicity)

Decreasing the degree will not delete control points but try instead to conserve the shape of the spline. Therefore segments will be added. For our example you see a lot of new spline segments with each one control point and the shape of the spline has only slightly been changed:

<img alt="" src=images/Sketcher_BSplineDegree2.png  style="width:400px;"> 
*Same B-spline where the degree was changed from 3 to 2. Note that also the knot multiplicity was increased to conserve the spline shape. In effect the knots have now ''C''<sup>0</sup> continuity so that the spline will get "edges" when you move a control point. (see [this page](Sketcher_BSplineDecreaseKnotMultiplicity#Description.md) to for an explanation of the continuity)*

If you take this result and increase the degree, you cannot get the initial state of the spline because information was lost by the prior decrease of the degree. For our example increasing the degree again leads to this:

<img alt="" src=images/Sketcher_BSplineDegree3again.png  style="width:400px;"> 
*Same B-spline where the degree was changed back from 2 to 3. Note that the knot multiplicity increased too because the information for a possible higher continuity was lost.*

## Применение

1.  Выберите ребро существующего B-сплайна и нажмите **<img src=images/Sketcher_BSplineDecreaseDegree.svg style="width:24px"> '''Decrease B-spline degree'''**





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher BSplineDecreaseDegree/ru
