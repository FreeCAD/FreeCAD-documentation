# Drawing/ko
## 소개

FreeCAD에서 \"도면(Drawing)\"이라는 단어는 일반적으로 [3D 모델의](model/ko.md) 2D 투영을 나타내는 데 사용됩니다. 이는 일반적으로 [기술도면 작업대에서](TechDraw_Workbench/ko.md) 생성됩니다.



## 용법

1.  [부품설계 작업대등을](PartDesign_Workbench/ko.md) 통해 만들어진 [3D 모델로](model/ko.md) 시작합니다. 사실은 2D 개체를 포함하여 [형상이](Shape/ko.md) 있는 것이면 어느 것이나 가능합니다.

2.  [기술도면 작업대로](TechDraw_Workbench/ko.md) 전환합니다.

3.  
    **[<img src=images/TechDraw_PageDefault.svg style="width:16px"> [TechDraw PageDefault](TechDraw_PageDefault.md)**또는 **[<img src=images/TechDraw_PageTemplate.svg style="width:16px"> [TechDraw PageTemplate](TechDraw_PageTemplate.md)**을 눌러서 페이지를 생성합니다.

4.  기존 모델을 선택한 다음 **[<img src=images/TechDraw_View.svg style="width:16px"> [TechDraw View](TechDraw_View.md)** 또는 **[<img src=images/TechDraw_ProjectionGroup.svg style="width:16px">[TechDraw_ProjectionGroup](TechDraw_ProjectionGroup.md)**를 누릅니다.

5.  페이지에 2D 투영이 생성됩니다. 이제 **Scale**, **Rotation** 및 **Direction**과 같은 속성을 조정할 수 있습니다.

6.  도면이 준비되면 이를 다른 소프트웨어에서 추가로 사용하거나 인쇄하기 위해 페이지를 SVG, DXF 또는 PDF 형식으로 내보냅니다. **[<img src=images/TechDraw_ExportPageSVG.svg style="width:16px"> [TechDraw ImportPageSVG](TechDraw_ExportPageSVG.md)**, **[<img src=images/TechDraw_ExportPageDXF.svg style="width:16px"> [TechDraw_ExportPageDXF](TechDraw_ExportPageDXF.md)**를 누를 수 있습니다. 또는 [Std Export를](Std_Export.md) 사용합니다.



## 보충 설명 

일상적 용법에서 \"도면(Drawing)\"은 [3D 보기에](3D_view/ko.md) 표시되는 기하학적 도형일 수 있습니다. 따라서 그 개념은 \"[몸통](Body/ko.md)\", \"[부품](Part/ko.md)\" 또는 \"[모델](Model/ko.md)\"의 개념과 혼동될 수 있습니다.

그러나 보다 정밀한 작업이 필요한 경우에는 구분이 필요합니다.

-   \"[몸통](Body/ko.md)\"([부품설계 작업에서의 몸통](PartDesign_Body/ko.md))은 [부품설계 작업대에서](PartDesign_Workbench/ko.md) 만들어지는 [Part Feature](Part_Feature.md)(`Part::Feature` 클래스)에서 파생되어 생성된 객체입니다.
-   \"[부품(Part)](Part/ko.md)\"([App Part](App_Part.md))은 여러 \"[몸통들](Body/ko.md)\"를 그룹화하여 조립품를 구성하는 데 사용됩니다.
-   \"도면\"은 \"몸통\" 또는 \"부품\"의 2D 투영입니다.


{{TechDraw Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [TechDraw](Category_TechDraw.md) > Drawing/ko
