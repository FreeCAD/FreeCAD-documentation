# Feature/ko
## 소개

FreeCAD에서 **특징(Feature)**라는 단어는 일반적으로 [부품설계 작업대에서](PartDesign_Workbench/ko.md) 만들어지는 [PartDesign Feature](PartDesign_Feature/ko.md) 객체(`PartDesign::Feature` 클래스)를 가리키는 데 사용됩니다. 이것은[특징 편집하기](feature_editing/ko.md) 패러다임에 따라 고체 [형상을](Shape/ko.md) 생성하거나 수정하기 위해 수행하는 작업 또는 모델링 단계를 뜻합니다.

이러한 유형의 개체에 대한 자세한 내용은 [도형특징(PartDesign Feature)를](PartDesign_Feature/ko.md) 참조하세요.



## 용법

1.  <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [부품설계 작업대로](PartDesign_Workbench/ko.md) 전환합니다.

2.  
    **[<img src=images/PartDesign_Body.svg style="width:16px">[PartDesign Body](PartDesign_Body.md)**을 누릅니다.

3.  
    **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [PartDesign NewSketch](PartDesign_NewSketch.md)**을 눌러서 새 [스케치를](Sketch/ko.md) 시작합니다.

4.  닫힌 와이어를 그리고, **[<img src=images/PartDesign_Pad.svg style="width:16px"> [PartDesign Pad](PartDesign_Pad.md)** 를 이용해 스케치를 돌출시켜 초기 고체를 만든다. 이 초기 고체는 우리가 만드려는 도형의 초기 특징이 됩니다.

5.  더 많은 스케치와 패드를 추가하고 [부품설계 작업대의](PartDesign_Workbench/ko.md) 다른 도구를 사용하여 초기 고체를 수정하고 변형합니다. 이러한 각 단계는 도형의 [몸통의](Body/ko.md) 특징에 해당합니다.

6.  또는 **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [PartDesignAdditiveBox](PartDesign_AdditiveBox.md)** 및 **[<img src=images/PartDesign_SubtractiveCylinder.svg style="width:16px">[PartDesign Subtractive cylinder](PartDesign_SubtractiveCylinder.md)**와 같은 원시 도형 개체를 추가합니다. 모든 덧셈 및 뺄셈 단계는 최종 볼륨을 만드는 데 사용되는 특징이 됩니다.



## 보충 설명 

일반적인 의미에서 \"특징\"은 [작업대의](Workbenches/ko.md) 도구를 사용하여 최종 [형상을](Shape/ko.md) 만드는 데 사용되는 모든 모델링 단계가 될 수 있습니다.

-   예를 들면, [부품 작업대에서](Part_Workbench/ko.md), [constructive solid geometry](constructive_solid_geometry.md) 작업흐름에서, \"특징\"은 **[<img src=images/Part_Fuse.svg style="width:16px"> [Part Fuse](Part_Fuse.md)**, **[<img src=images/Part_Cut.svg style="width:16px"> [Part Cut](Part_Cut.md)**, 또는 **[<img src=images/Part_Common.svg style="width:16px"> [Part Common](Part_Common.md)**과 같은 부울 연산이 될 수도 있습니다.

보다 구체적인 의미에서 \"특징\"은 [몸통](PartDesign_Body/ko.md) 내부에서 사용되는 모델링 단계를 뜻합니다.

-   예를 들면, **[<img src=images/PartDesign_AdditiveCylinder.svg style="width:16px"> [PartDesign Additive cylinder](PartDesign_AdditiveCylinder.md)**, **[<img src=images/PartDesign_AdditiveLoft.svg style="width:16px"> [PartDesign Additive loft](PartDesign_AdditiveLoft.md)**, **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [PartDesign Pocket](PartDesign_Pocket.md)**, **[<img src=images/PartDesign_SubtractiveCone.svg style="width:16px"> [PartDesign Subtractive cone](PartDesign_SubtractiveCone.md)**, 등은 모두 우리가 만드는 도형의 (기하학적) \"특징\"들입니다.


{{PartDesign Tools navi

}}  {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [PartDesign](Category_PartDesign.md) > [Part](Category_Part.md) > Feature/ko
