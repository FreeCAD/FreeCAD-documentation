# Assembly/ko
## 소개




FreeCAD에서 \"조립품\"이라는 단어는 일반적으로 여러 개의 구별 가능한 부분으로 구성된 [3D 모델을](model/ko.md) 지칭하는 데 사용됩니다. 이 부분은 어떤 방식으로든 함께 결합되어 기능적인 객체를 생성합니다. 실제 제품이 만들어지는 것처럼요.

예를 들어, 볼트, 와셔 및 너트는 함께 조립할 때 조립품을 구성하는 세 개의 별도 몸통들입니다.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;">



*왼쪽: 3개의 개별 연속 고체, 각각 [몸통](PartDesign_Body/ko.md)으로 모델링됨. 오른쪽: 조립품을 생성하기 위해 [표준 부품](Std_Part/ko.md) 내부에 결합된 개별 몸통.*



## 용법



### 수동 조립 

일반적으로 조립품을 생성하는 데 특별한 도구가 필요하지 않으며, 단지 여러 가지 다른 [몸통들을](Body/ko.md) 어떤 방식으로든 배열하면 됩니다.

원하는 위치에 몸통을 배치하려면

-   [Std TransformManip](Std_TransformManip.md) 도구를 사용하거나
-   <img alt="" src=images/Std_Placement.svg  style="width:16px;"> [Std Placement](Std_Placement.md) 대화상자를 사용할 수 있고 또는
-   [속성 편집기에서](Property_editor/ko.md) [placement](Placement.md) 속성을 직접 수정하면 됩니다.

Lattice2, Manipulator, Part-o-magic 또는 WorkFeature와 같은 유사 조립품 [외부 작업대](external_workbenches/ko.md) 중 하나를 사용하여 교차점을 찾고, 거리를 측정하고, 원하는 방식으로 개체를 배포할 수 있습니다.

일반적으로 **[<img src=images/Std_Part.svg style="width:16px"> [표준부품](Std_Part/ko.md)** 객체는 조립품을 생성하기 위한 기본 빌딩 블록 역할을 하도록 설계되었습니다. 이 객체는 여러 개의 [몸통들을](body/ko.md) 그룹화하여 하나의 단위, 즉 하위 조립품으로 함께 이동하는 데 사용됩니다. 그런 다음 이 하위 어셈블리를 다른 하위 조립품 옆에 배치하거나 다른 하위 조립품 내부에 사용하여 최종 조립품을 만들 수 있습니다.



### 구속조건 지어진 조립 


<div class="mw-translate-fuzzy">

<img alt="" src=images/A2p_workbench.svg  style="width:24px;"> [A2plus](A2plus_Workbench.md), <img alt="" src=images/Assembly3_workbench_icon.svg  style="width:24px;"> [Assembly3](Assembly3_Workbench.md), <img alt="" src=images/Assembly4_workbench_icon.svg  style="width:24px;"> [Assembly4와](Assembly4_Workbench.md) 같은 전용 조립 작업대를 사용할 수도 있습니다. [Assembly2작업대는](Assembly2_Workbench.md) 유지 관리되지 않으므로 새 모델에는 권장되지 않습니다.


</div>

조립 작업대는 수학적으로 객체를 제자리에 묶기 위해 구속조건과 표현식을 사용하여 모델의 객체 간의 관계를 생성합니다. 예를 들면, \"이 면은 다른 면에 달라붙어야 합니다.\", \"이 원통은 저 원과 중심이 같아야 합니다.\", \"이 점은 이 가장자리를 따라야 합니다.\" 등이 있습니다.

이는 복잡한 기계 시스템에서 일반적으로 사용되는 소프트웨어의 고급 사용법입니다. [모델이](mod;e/ko.md) 그다지 복잡하지 않다면 조립 작업대를 사용할 필요가 없을 수도 있습니다.



## 보충 설명 


<div class="mw-translate-fuzzy">

FreeCAD 0.19부터 시스템에 기본적으로 포함된 공식 조립 작업대가 없습니다. 조립 작업대는 모델에서 [몸통](Body/ko.md) 및 [부품의](Part/ko.md) 효율적인 사용과 관련하여 해결해야 할 문제가 많기 때문에 프로그래밍하기 어렵지만 [App Link](App_Link.md) 객체의 도입으로 상황이 개선되었습니다.


</div>


<div class="mw-translate-fuzzy">

조립 작업대는 일반적으로 서로 호환되지 않는 것에 주의 하세요. 이러한 작업대 중 하나를 사용하여 조립품을 생성하는 경우 해당 작업대를 고수해야 하며 동일한 문서 작업에 다른 조립 작업대를 사용해서는 안 됩니다.


</div>


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > Assembly/ko
