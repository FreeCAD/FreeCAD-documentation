# <img alt="부품설계 작업대 아이콘" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/ko






## 소개


<div class="mw-translate-fuzzy">

<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> **부품설계 작업대**에는 복잡한 고체 부품을 만들기 위한 다양한 도구들이 있습니다. 주로 완제품으로 제조 및 조립될 수 있는 기계 부품을 만드는 데 중점을 두고 있지만 생성된 고체는 일반적으로 [건축 작업대](Arch_Workbench/ko.md), [FEM 작업대](FEM_Workbench/ko.md) 또는 [CAM 작업대와](CAM_Workbench/ko.md) 같은 다른 목적의 작업대에서도 사용될 수 있습니다.


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [부품 작업대는](Part_Workbench/ko.md) 형상을 만들기 위해 [구성적 고체 기하학(Constructive solid geometry)](constructive_solid_geometry/ko.md)(CSG) 방법론을 기반으로 하지만, 부품설계 작업대는 매개변수를 사용하여 도형의 특징을 편집하는 방법을 사용하는데, 이는 최종 형상을 얻을 때까지 기본 고체 위에 특징을 추가하여 순차적으로 변형하는 것을 의미합니다. 이 작업과정에 대한 더 자세한 설명은 [특징 편집하기](feature_editing/ko.md) 페이지를 참조하고, 고체 생성을 시작하려면 [부품설계 작업대에서 간단한 부품 만들기를](Creating_a_simple_part_with_PartDesign/ko.md) 참조하세요.


</div>

See the [feature editing](Feature_editing.md) page for a more complete explanation of this process, and then see [Creating a simple component with PartDesign](Creating_a_simple_part_with_PartDesign.md) to get started with creating solids.


<div class="mw-translate-fuzzy">

부품 작업대와 부품설계 작업대에 대한 자세한 설명은 [부품 작업대와 부품설계 작업대에서](Part_and_PartDesign/ko.md) 확인할 수 있습니다.


</div>

![](images/PartDesign_Workbench_Example.jpg )



## 도구

부품설계 작업대의 도구는 모두 **Part Design** 메뉴와 부품설계 작업대를 로드할 때 나타나는 PartDesign 도구 모음에 있습니다.



### 부품설계 도우미 도구 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [몸통 생성](PartDesign_Body/ko.md): 활성 문서에 [몸통(Body)](Body/ko.md) 객체를 생성하고 활성화합니다.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 스케치 생성:




<div class="mw-translate-fuzzy">

  -<img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [스케치 생성](PartDesign_NewSketch/ko.md): 선택한 면이나 평면에 새 스케치를 만듭니다. 이 도구를 실행하는 동안 면을 선택하지 않으면 작업 패널에서 평면을 선택하라는 메시지가 사용자에게 표시됩니다. 그런 다음 인터페이스는 스케치 편집 모드에서 [스케치 작업대로](Sketcher_Workbench/ko.md) 전환됩니다.


</div>

  - <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [스케치 부착하기](Sketcher_MapSketch/ko.md): 활성 몸통에서 선택한 형상에 스케치를 붙입니다.

  - <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [스케치 편집](Sketcher_EditSketch/ko.md): 편집을 위해 선택한 스케치를 엽니다.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [스케치 유효성 검사](Sketcher_ValidateSketch/ko.md): 다양한 점의 공차를 확인하고 조정합니다.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [기하학적 요소 검사](Part_CheckGeometry/ko.md): 선택한 개체의 기하학적 구조에 오류가 있는지 확인합니다.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Create a shape binder](PartDesign_ShapeBinder.md): creates a shape binder referencing geometry from a single parent object.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Create a sub-object(s) shape binder](PartDesign_SubShapeBinder.md): creates a shape binder referencing geometry from one or more parent objects.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [복제하기 ](PartDesign_Clone/ko.md): 선택한 몸통을 복제합니다.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 기준도형 생성:




</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [기준 평면 생성](PartDesign_Plane/ko.md): 기준 평면을 활성 몸통에 생성합니다.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [기준선 생성](PartDesign_Line/ko.md): 기준선을 활성 몸통에 생성합니다.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [기준점 생성](PartDesign_Point/ko.md): 기준점을 활성 몸통에 생성합니다.


</div>


<div class="mw-translate-fuzzy">

  -<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [지역 좌표계 생성](PartDesign_CoordinateSystem/ko.md): 기준도형에 부착된 지역 좌표계를 활성 몸통에 생성합니다.


</div>


:   
    <small>(v1.1)</small> : these tools have been replaced by new [datum tools](Std_Base#Part_Datums.md).



### 조형 도구 



#### 덧셈적 도구 

아래는 기본적인 도형특징을 생성하거나 기존 몸통에 재료를 더하기 위한 도구입니다.

-   <img alt="" src=images/PartDesign_Pad.svg  style="width:32px;"> [깔판](PartDesign_Pad/ko.md): 선택한 (닫힌) 스케치를 돌출하여 평평한 고체 판을 만듭니다.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [회전](PartDesign_Revolution/ko.md): 축을 중심으로 스케치를 회전하여 고체를 생성합니다. 스케치는 닫힌 윤곽선을 만들어야 합니다.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [로프트 추가](PartDesign_AdditiveLoft/ko.md): 두 개 이상의 스케치 사이를 전환하여 고체를 생성합니다.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [파이프 추가](PartDesign_AdditivePipe/ko.md): 열려 있거나 닫힌 경로를 따라 하나 이상의 스케치를 쓸어 나가며 고체를 생성합니다.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [나선 추가](PartDesign_AdditiveHelix/ko.md): 나선을 따라 스케치를 쓸어 나가며 고체를 생성합니다.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 기본 입체도형 추가:

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [상자 추가](PartDesign_AdditiveBox/ko.md): 상자를 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [원통 추가](PartDesign_AdditiveCylinder/ko.md): 원통을 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [구체 추가](PartDesign_AdditiveSphere/ko.md): 구체를 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [원뿔 추가](PartDesign_AdditiveCone/ko.md): 원뿔을 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [타원체 추가](PartDesign_AdditiveEllipsoid/ko.md): 타원체를 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [원환체 추가](PartDesign_AdditiveTorus/ko.md): 원환체를 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [각기둥 추가](PartDesign_AdditivePrism/ko.md): 각기둥을 만들어 활성 몸통에 더합니다.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [쐐기 추가](PartDesign_AdditiveWedge/ko.md): 쐐기를 만들어 활성 몸통에 더합니다.



#### 뺄셈적 도구 

아래는 기존 몸통에서 재료를 빼는 도구입니다.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [오목 자리](PartDesign_Pocket/ko.md): 선택한 스케치에서 오목한 자리를 생성합니다.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [구멍](PartDesign_Hole/ko.md): 선택한 스케치에서 구멍을 생성합니다. 스케치에는 하나 이상의 원이 포함되어야 합니다.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [홈파기](PartDesign_Groove/ko.md): 축을 중심으로 스케치를 회전시켜 홈을 생성합니다.

-   <img alt="" src=images/PartDesign_SubtractiveLoft.svg  style="width:32px;"> [로프트 빼기](PartDesign_SubtractiveLoft/ko.md): 두 개 이상의 스케치 사이를 전환하여 고체 형상을 만들고 활성 몸통에서 뺍니다.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [파이프 빼기](PartDesign_SubtractivePipe/ko.md): 열려 있거나 닫힌 경로를 따라 하나 이상의 스케치를 쓸어 나가며 고체 형상을 만들고 활성 몸통에서 뺍니다.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [나선 빼기](PartDesign_SubtractiveHelix/ko.md): 나선을 따라 스케치를 쓸어 나가며 고체 형상을 만들고 활성 몸통에서 뺍니다.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 기본 입체도형 빼기:

  -<img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:32px;"> [상자 빼기](PartDesign_SubtractiveBox/ko.md): 상자를 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [원통 빼기](PartDesign_SubtractiveCylinder/ko.md): 원통을 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [구체 빼기](PartDesign_SubtractiveSphere/ko.md): 구체를 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveCone.svg  style="width:32px;"> [원뿔 빼기](PartDesign_SubtractiveCone/ko.md): 원뿔을 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveEllipsoid.svg  style="width:32px;"> [타원체 빼기](PartDesign_SubtractiveEllipsoid/ko.md): 타원체를 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [원환체 빼기](PartDesign_SubtractiveTorus//ko.md): 원환체를 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [각기둥 빼기](PartDesign_SubtractivePrism/ko.md): 각기둥을 만들어 활성 몸통에서 뺍니다.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[쐐기 빼기](PartDesign_SubtractiveWedge/ko.md): 쐐기를 만들어 활성 몸통에서 뺍니다.



#### 부울(Boolean) 도구 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [부울 연산](PartDesign_Boolean/ko.md): 하나 이상의 몸통 또는 복제품을 활성 몸통으로 가져와 부울 연산을 적용합니다.



### 꾸밈 도구 

아래 도구는 모서리나 면에 처리를 적용합니다.

-   <img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [모깎기](PartDesign_Fillet/ko.md): 활성 본체의 모서리를 (둥글게) 깎아냅니다.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [모따기](PartDesign_Chamfer/ko.md): 활성 몸통의 모서리를 (평평하게) 따냅니다.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [구배](PartDesign_Draft/ko.md): 활성 몸통의 선택한 면에 각도 구배를 적용합니다.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [두께](PartDesign_Thickness/ko.md): 활성 몸통에서 두께가 있는 껍질을 만들고 선택한 면은 개방합니다.



### 변환 도구 

아래는 이미 생성된 도형특징을 몇 가지 방식으로 복사 변환하기 위한 도구입니다.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [대칭 복사](PartDesign_Mirrored/ko.md): 하나 이상의 도형특징을 대칭 복사 변환합니다.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [선형 복사](PartDesign_LinearPattern/ko.md): 하나 이상의 도형특징을 선형으로 복사 변환합니다.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [원형 복사](PartDesign_PolarPattern/ko.md): 하나 이상의 도형특징을 원형으로 복사 변환합니다.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [다중 변환](PartDesign_MultiTransform/ko.md): 위에서 언급한 변환과 [배율변환](PartDesign_Scaled/ko.md) 을 결합하여 도형특징을 복사 변환합니다.
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [배율변환](PartDesign_Scaled/ko.md): 하나 이상의 도형특징을 배율변환합니다. 개별적으로는 사용할 수 없습니다.



#### 기타 도구 

부품 설계 메뉴에 있는 몇 가지 추가 기능은 다음과 같습니다.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [사슬톱니바퀴](PartDesign_Sprocket/ko.md): 사슬톱니바퀴 윤곽선을 생성합니다.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [점개선 기어](PartDesign_InvoluteGear/ko.md): 점개선(漸開線 involute curve) 기어 윤곽선을 생성합니다.


</div>

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [축 설계 마법사](PartDesign_WizardShaft/ko.md): 값 테이블에서 축을 생성하고 힘과 모멘트를 분석할 수 있습니다. 축은 편집할 수 있는 회전된 스케치로 만들어집니다.



### 상황에 맞는 메뉴 항목 

-   [Suppressed](PartDesign_Suppressed.md): checkbox to disable a specific feature without deleting it. <small>(v1.0)</small> 

-   <img alt="" src=images/PartDesign_MoveTip.svg  style="width:32px;"> [끝단(tip)설정](PartDesign_MoveTip/ko.md) : 몸통이 외부에 노출되는 도형특징인 Tip을 재정의합니다.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [다른 몸통으로 이동](PartDesign_MoveFeature/ko.md): 선택한 스케치, 기준 도형 또는 도형특징을 다른 몸통으로 이동합니다.

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [다른 개체 뒤로 개체 이동](PartDesign_MoveFeatureInTree/ko.md): 선택한 스케치, 기준도형 또는 도형특징을 목록의 다른 위치로 이동하여 몸통 트리의 순서를 변경할 수 있습니다.



#### 부품 작업대와 공유되는 항목 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [외관 설정](Std_SetAppearance/ko.md): 전체 부품의 외관(색상 투명도 등)을 결정합니다.

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [면색상](Part_ColorPerFace/ko.md): 개체의 개별 면에 색상을 할당합니다.



### 오래된 도구 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Migrate](PartDesign_Migrate.md): migrates files from FreeCAD versions below 0.17 to version 0.17. This tool is not available in <small>(v1.0)</small> .



## 환경설정

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [환경설정](PartDesign_Preferences/ko.md): 부품설계 작업대 도구에 사용할 수 있는 기본 설정입니다.
-   [미세 조정](Fine-tuning/ko.md): 부품설계 작업대의 동작을 미세 조정하기 위한 몇 가지 추가 매개변수입니다.



## 자습서


<div class="mw-translate-fuzzy">

-   [How to use FreeCAD](http://help-freecad-jpg87.fr/), 기계 설계 작업 흐름을 설명하는 웹 사이트.
-   [부품설계 작업대에서 간단한 부품 만들기](Creating_a_simple_part_with_PartDesign/ko.md)
-   [기초적인 부품설계 작업대 자습서](Basic_Part_Design_Tutorial/ko.md)
-   [PartDesign Bearingholder Tutorial I](PartDesign_Bearingholder_Tutorial_I.md) (needs updating)
-   [PartDesign Bearingholder Tutorial II](PartDesign_Bearingholder_Tutorial_II.md) (needs updating)


</div>



## 예제

부품 설계 도구로 무엇을 얻을 수 있는지에 대한 몇 가지 아이디어를 보려면 다음을 살펴보십시오: [부품설계 예제](PartDesign_Examples/ko.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">





 {{PartDesign_Tools_navi}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/ko
