# PartDesign Feature/ko
## 소개

부품설계 작업에서 **특징(PartDesign Feature)**은 [몸통(PartDesign Body)](PartDesign_Body/ko.md) 내부에서 발생하는 모델링 과정에서의 (도형의 기하학적 특징을 추가하는)\"단계\"를 나타냅니다. 예를 들어, [PartDesign AdditiveBox를](PartDesign_AdditiveBox.md) 사용하여 고체 상자를 추가할 때마다 여러분은 도형의 기하학적 특징(Feature)을 추가하는 것입니다; [모따기를](PartDesign_Chamfer/ko.md) 사용하여 가장자리에 모따기를 추가하면 (도형의) 다른 특징이 추가됩니다. [스케치](Sketch/ko.md) 및 [PartDesign Pocket을](PartDesign_Pocket.md) 사용하여 구멍을 만들면 여러분은 또 다른 특징을 추가한 것입니다.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:600px;"> 
*3개의 순차적 특징이 있는 [몸통](PartDesign_Body/ko.md)에서 특징 편집.*

초기 고체에 부피를 추가하거나 제거할 수 있는 다양한 유형의 특징들이 있습니다. \"특징(Feature)\"라는 단어는 작업 자체를 의미하며 해당 작업 이후에 생성되는 고체도 의미합니다.

[부품설계 작업대를](PartDesign_Workbench/ko.md) 사용하여 고체를 생성하는 방법에 대해 자세히 알아보려면 [특징 편집하기를](feature_editing/ko.md) 참조하세요.



## 용법

[부품설계 작업대에](PartDesign_Workbench/ko.md) 있는 거의 모든 도구는 도형의 [몸통에](PartDesign_Body/ko.md) 기하학적 특징을 추가하기 위한 것입니다. 이러한 도구는 개체나 하위 요소(꼭지점, 모서리, 면)가 선택되어 있는 동안 메뉴 및 도구 모음 버튼을 통해 접근할 수 있습니다.

도형의 특징들은 다양한 범주에 배치될 수 있습니다.

-   특징 기반: [몸통에서](PartDesign_Body/ko.md) 생성할 수 있는 기반 특징(Base Feature) 객체를 말합니다.
-   덧셈과 뺄셈 특징
    -   기본 형상: [Box](PartDesign_AdditiveBox.md), [Cone](PartDesign_AdditiveCone.md), [Cylinder](PartDesign_AdditiveCylinder.md), [Ellipsoid](PartDesign_AdditiveEllipsoid.md), [Prism](PartDesign_AdditivePrism.md), [Sphere](PartDesign_AdditiveSphere.md), [Torus](PartDesign_AdditiveTorus.md), 그리고 [Wedge](PartDesign_AdditiveWedge.md).
    -   기본 형상 뺄셈: [Subtractive Box](PartDesign_SubtractiveBox.md), [Subtractive Cone](PartDesign_SubtractiveCone.md), [Subtractive Cylinder](PartDesign_SubtractiveCylinder.md), [Subtractive Ellipsoid](PartDesign_SubtractiveEllipsoid.md), [Subtractive Prism](PartDesign_SubtractivePrism.md), [Subtractive Sphere](PartDesign_SubtractiveSphere.md), [Subtractive Torus](PartDesign_SubtractiveTorus.md), 그리고 [Subtractive Wedge](PartDesign_SubtractiveWedge.md).
    -   프로파일 기반: [Pad](PartDesign_Pad.md), [Revolution](PartDesign_Revolution.md), [Loft](PartDesign_AdditiveLoft.md), [Pipe](PartDesign_AdditivePipe.md).
    -   프로파일 기반 뺄셈: [Pocket](PartDesign_Pocket.md), [Hole](PartDesign_Hole.md), [Groove](PartDesign_Groove.md), [Subtractive Loft](PartDesign_SubtractiveLoft.md), [Subtractive Pipe](PartDesign_SubtractivePipe.md).
-   [Boolean](PartDesign_Boolean.md), 결합, 잘라내기 및 교차를 포함합니다.
-   꾸밈
    -   [모따기](PartDesign_Chamfer/ko.md)
    -   [PartDesign_Draft](PartDesign_Draft.md)
    -   [모깎기](PartDesign_Fillet/ko.md)
    -   [PartDesign_Thickness](PartDesign_Thickness.md)
-   변환
    -   [대칭복사](PartDesign_Mirrored/ko.md)
    -   [선형복사](PartDesign_LinearPattern/ko.md)
    -   [원형복사](PartDesign_PolarPattern/ko.md)
    -   [다중변환](PartDesign_MultiTransform/ko.md)
    -   [배율변환](PartDesign_Scaled/ko.md)



## 상속

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*프로그램의 핵심 개체 간의 관계를 단순화한 다이어그램입니다. `PartDesign::Feature* 객체는 파라메트릭 3D 솔리드를 만드는 데 사용되므로 기본 {{incode|Part::Feature` 객체에서 파생됩니다.}}



## 스크립팅


**참고**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md), 그리고 [scripted objects](scripted_objects.md).

[파이썬 콘솔에서](Python_console/ko.md) 개체를 추가하는 방법에 대한 일반적인 정보는 [Part Feature를](Part_Feature.md) 참조하세요.

몸통(Body) 추가에 대한 일반적인 정보는 [부품설계 작업대에서의 몸통을](PartDesign_Body/ko.md) 참조하세요. 몸통이 존재하면 몸통의 `addObject()` 메서드를 사용하여 도형의 특징을 추가할 수 있습니다.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign::Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign::AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign::SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/ko
