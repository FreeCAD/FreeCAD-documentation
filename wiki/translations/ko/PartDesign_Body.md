---
 GuiCommand:
   Name: PartDesign Body
   MenuLocation: Part Design , Create body
   Workbenches: PartDesign_Workbench/ko
   Version: Release_notes_0.17/ko
   SeeAlso: Std_Part/ko, Feature_editing/ko
---

# PartDesign Body/ko



## 설명

**몸통(PartDesign Body)**은 [부품설계 작업대를](PartDesign_Workbench/ko.md) 사용하여 고체 형상을 생성하기 위한 기본 요소입니다. 여기에는 [단일 연속 솔리드를](PartDesign_Body#Single_contiguous_solid.md) 만드는 데 도움이 되는 [스케치](Sketch/ko.md), [기준도형](Datum/ko.md) 및 [도형특징이](PartDesign_Feature/ko.md) 포함될 수 있습니다

몸통은 로컬 X, Y, Z 축과 표준 평면을 포함하는 **Origin** 개체를 제공합니다. 이러한 요소는 [스케치](Sketch/ko.md) 및 [PartDesign_CompPrimitiveAdditive를](PartDesign_CompPrimitiveAdditive.md) 첨부하기 위한 참조로 사용할 수 있습니다.

<img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [몸통을](PartDesign_Body/ko.md) <img alt="" src=images/Std_Part.svg  style="width:24px;"> [표준 부품과](Std_Part/ko.md) 혼동하지 마십시오. 몸통은 <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [부품설계 작업대에서](PartDesign_Workbench/ko.md) 사용되는 것이며, [도형특징을](PartDesign_Feature/ko.md) 통해 [단일 연속 고체를](PartDesign_Body#Single_contiguous_solid.md) 모델링하기 위한 것입니다. [표준 부품은](Std_Part/ko.md) [조립품을](assembly/ko.md) 생성하기 위한 그룹화 개체입니다;모델링에는 사용되지 않으며 단지 공간에 다양한 개체들를 배열하는 데 사용됩니다. 여러 몸통과 기타 [표준 부품을](Std_Part/ko.md) 단일 [표준 부품](Std_Part/ko.md) 내부에 배치하여 복잡한 조립품을 만들 수 있습니다.

![](images/PartDesign_Body_tree.png ) ![](images/PartDesign_Body_example.png ) 
*왼쪽: 물체의 최종 형상을 순차적으로 생성하는 특징을 보여주는 트리 보기. 오른쪽: [3D 보기](3D_view/ko.md)에 표시되는 최종 개체.*



## 용법

이전 고체를 선택하지 않은 경우:

1.  
    **<img src="images/PartDesign_Body.svg" width=16px> 몸통 생성**버튼을 누릅니다. 빈 몸통이 생성되고 자동으로 **[활성화](PartDesign_Body#Active_status.md)**가 됩니다.

2.  
    **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**를 눌러 **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Pad](PartDesign_Pad.md)**작업을 할 수 있는 [스케치를](Sketch/ko.md) 생성합니다.

3.  또는 기본 [도형특징을](PartDesign_Feature/ko.md) 추가합니다(예: **[<img src=images/PartDesign_AdditiveBox.svg style="width:16px"> [Additive box](PartDesign_AdditiveBox.md)**).

고체를 선택한 경우:

1.  
    **<img src="images/PartDesign_Body.svg" width=16px> 몸통 생성**버튼을 누릅니다. 단일 **기반특징**을 포함하는 새 몸통이 생성됩니다. 이 기반특징 요소는 이전에 생성되었거나 문서로 가져온 다른 개체에 대한 간단한 참조입니다. 자세한 내용은 이 페이지의 기반특징(Base Feature)설명 부분을 참조하세요. **<img src="images/PartDesign_Body.svg" width=16px> 몸통 생성**버튼을 누르면 기존 몸통 또는 [도형특징을](PartDesign_Feature/ko.md) 선택할 수 없습니다.



## 보충 설명 

-    **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**버튼을 눌렀을 때 현재 몸통이 존재하지 않는 경우, 새로운 몸통이 자동으로 생성됩니다. 몸통이 이미 존재하는 경우 **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**을 사용하기 전에 몸통을 활성화해야 합니다.

-   [트리 보기에서](tree_view/ko.md) 몸통을 더블클릭하거나 컨텍스트 메뉴를 열고(마우스 오른쪽 버튼 클릭) **Toggle active body**를 선택하여 몸통을 활성화하거나 비활성화합니다. 다른 몸통이 활성화되어 있으면 비활성화됩니다.자세한 내용은 [활성 상태를](PartDesign_Body#Active_status.md) 참조하세요.



## 속성

PartDesign_Body(`PartDesign::Body` 클래스)는 [Part Feature](Part_Feature.md)(`Part::Feature` 클래스)에서 파생됩니다. 후자의 모든 속성을 공유합니다.

[Part Feature에](Part_Feature.md) 설명된 속성 외에도 PartDesign Body는 [속성 편집기에](property_editor/ko.md) 다음과 같은 속성을 가지고 있습니다.



### 정보(Data)


{{TitleProperty|Base}}

-    **Tip|Link**: \"Tip\"으로 정의된 [도형특징은](PartDesign_Feature/ko.md) 일반적으로 몸통에서 생성된 마지막 특징입니다. Tip은 몸통의 최종 형상을 나타내며, **Display Mode Body**가 `Tip`으로 설정되었을 때 [3차원 보기에](3D_view/ko.md) 표시됩니다. 자세한 내용은 [Tip을](PartDesign_Body#Tip.md) 참조하세요.

-    **Base Feature|Link**: 몸통에서 첫 번째 [특징으로](PartDesign_Feature/ko.md) 사용되는 외부 형상입니다. 일반적으로 빈 몸통에 고체를 드래그할 때 설정됩니다. 이 방법으로 고체를 가져오지 않으면 이 속성은 비어 있게 됩니다. 자세한 내용은 이 페이지의 기반특징(Base Feature)부분을 참조하세요.

-    **Placement|Placement**: [3D 보기에](3D_view/ko.md) 보이는 개체의 위치입니다.배치는 `Base` 점(벡터)과 `Rotation`(축 및 각도)에 의해 정의됩니다. [Placement를](Placement.md) 참조하세요.

-    **Group|LinkList**: 몸통의 [특징이](PartDesign_Feature/ko.md) 포함된 목록입니다.



#### 숨겨진 속성 정보 

-    **Origin|Link**: **Group**에 나열된 모든 요소에 대한 위치 참조인 [App Origin](App_OriginGroupExtension.md) 개체입니다.

-    **_ Group Touched|Bool**: 그룹 터치 여부.

또한 [Part Feature에](Part_Feature.md) 설명된 숨겨진 속성도 있습니다.



### 보기


{{TitleProperty|Base}}

-    **Display Mode Body|Enumeration**: 두 가지 유형 중 하나로 몸통에 대한 표시 모드를 구체적으로 설정합니다.

    -   
        `Through`
        
        (기본값)는 몸통 내부의 모든 개체, 즉 [sketch스케치](Sketch/ko.md), [특징](PartDesign_Feature/ko.md), 기준도형 등을 노출합니다. 몸통 내부에서 수행되는 부분적인 작업을 시각화할 수 있는 모드이므로 특징을 추가하거나 편집할 때 권장되는 모드입니다. 특정 특징을 선택하고 **Visibility**를 `True`로 설정하거나 키보드의 **Space** 막대를 누릅니다.

    -   
        `Tip`
        
        은 **Tip** 속성에 정의된 몸통의 최종 형상만 노출합니다. [스케치](Sketch/ko.md), [특징](PartDesign_Feature/ko.md), 기준도형 등을 포함한 다른 모든 항목은 [트리 보기에](tree_view/ko.md) 표시되더라도 보이지 않습니다. 이 모드는 몸통을 더 이상 수정할 필요가 없어 고정된 형태로 보여지는 경우에 권장되는 모드입니다.이 모드는 다른 작업대의 도구와 함께 사용하기 위해 최종 모양의 하위 요소(꼭지점, 모서리 및 면)를 선택하려는 경우에도 권장됩니다.



## 몸통의 개념 



### 단일한 연속된 고체 

부품설계에서 몸통은 단일한 연속된 고체를 모델링하기 위한 것입니다. \"연속\"이라는 의미는 움직이는 부품이나 분리된 고체 없이 일체형으로 만들어진 요소를 의미합니다. 연속 고체의 예로는 주조, 절단 또는 밀링 공정을 통해 단일 원료 조각으로 제조된 고체가 있습니다.예를 들어, 너트, 와셔 및 볼트는 각각 움직이는 부품이 없는 하나의 단단한 강철 조각으로 구성되므로 각각 몸통으로 모델링할 수 있습니다. 두 부분을 용접하여 생성된 물체는 용접 접합이 분리되지 않는 한 단일 몸통으로 모델링할 수도 있습니다.

이러한 인접한 고체들이 어떤 유형의 배열로 결합되면 \"조립체\"가 됩니다. 조립체에서 각각의 고체는 서로 융합되지 않고 단순히 \"쌓이거나\" 서로 옆에 배치되어 개별 부품으로 유지됩니다.

<img alt="" src=images/PartDesign_Body_contiguous_separate.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_contiguous_assembly.png  style="width:" height="200px;"> 
*왼쪽: 3개의 개별적 연속 고체, 각각 몸통으로 모델링됨. 오른쪽: 조립체에 함께 모인 개별 몸통.*



### 도형특징 편집하기 

몸통은 [스케치](Sketch/ko.md) 또는 [PartDesign_CompPrimitiveAdditive에서](PartDesign_CompPrimitiveAdditive.md) 초기 고체를 생성하여 작동하도록 되어 있고,그런 다음 [\"특징\"을](PartDesign_Feature/ko.md) 통해 수정하여 이전 모양에서 재료를 추가하거나 제거합니다.전체 설명을 보려면 [특징 편집하기으로](feature_editing/ko.md) 이동하세요.

몸통은 내부의 고체 요소를 자동으로 융합(결합)합니다. 이는 (1) 부분적인 고체가 생성될 때 서로 접촉해야 하며 (2) 연결되지 않은 고체는 허용되지 않음을 의미합니다.

<img alt="" src=images/PartDesign_Body_two_intersection.png  style="width:" height="200px;"> <img alt="" src=images/PartDesign_Body_two_fusion.png  style="width:" height="200px;"> 
*왼쪽: 서로 교차하는 두 개의 고체. 오른쪽: 두 개의 [덧셈 특징](PartDesign_Feature/ko.md)이 포함된 단일 몸체; 자동으로 서로 융합되므로 교차하는 대신 하나의 인접한 고체를 형성합니다.*

![](images/PartDesign_Body_non-contiguous.png ) 
*왼쪽: 연결되지 않은 두 개의 고체; 이는 유효한 몸통이 아닙니다. 오른쪽: 두 개의 서로 닿는 고체; 유효한 몸통이 생성됩니다.새로운 [도형특징](PartDesign_Feature/ko.md)은 항상 이전 특징과 접촉하거나 교차하여 융합되어 단일 연속 고체가 되어야 합니다.*


**참고:**

Catia와 같은 다른 CAD 프로그램은 동일한 \"몸통\"에서 연속되지 않은 고체를 허용합니다. v0.19부터 FreeCAD는 이를 허용하지 않습니다. [FreeCAD 포럼](https://forum.freecadweb.org/index.php)에서 이 제한을 해제하는 것에 대해 논의가 있었지만 구체적인 결정은 내려지지 않았습니다.더 많은 정보를 알고 싶거나 다른 관점을 제시하고 싶다면 [포럼](https://forum.freecadweb.org/index.php)에서 토론해 주세요.



## 속성에 대한 자세한 설명 



### 활성 상태 

열린 문서에는 여러 개의 몸통이 포함될 수 있습니다. 특정 몸통에 새로운 특징을 추가하려면 **active**로 설정해야 합니다. 활성 몸통은 [환경 설정 편집기의](Preferences_Editor#Colors/ko.md) **Active container** 값에 의해 지정된 배경색으로 [트리 보기에](tree_view/ko.md) 표시됩니다(기본적으로 밝은 파란색).

몸통을 활성화하거나 비활성화하려면:

-   [트리 보기에서](tree_view/ko.md) 더블클릭하거나,
-   컨텍스트 메뉴를 열고(오른쪽 클릭) **Toggle active body**를 선택합니다.

몸통을 활성화하면 자동으로 [부품설계 작업대로](PartDesign_Workbench/ko.md) 전환됩니다. 한 번에 하나의 몸통만 활성화할 수 있습니다.

![](images/PartDesign_Body_active.png )



*두 개의 몸통이 포함된 문서이며 그 중 두 번째 몸통이 활성화되어 있습니다.*



### 원점

원점은 세 개의 표준 축(X, Y, Z)과 세 개의 표준 평면(XY, XZ 및 YZ)으로 구성됩니다. [스케치](Sketch/ko.md) 및 기타 개체를 생성할 때 이러한 요소에 부착할 수 있습니다.

1.  몸통을 생성합니다.
2.  [트리 보기에서](tree_view/ko.md) 몸통을 선택한 경우 **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**버튼을 누릅니다; [작업판이](task_panel/ko.md) 열리고 평면 중 하나를 선택할 수 있습니다.
3.  몸통이 선택되지 않은 경우 대신 원점을 선택하고 키보드의 **Space** 바를 눌러 [3D 보기에](3D_view/ko.md) 표시되도록 합니다. 또한 축과 평면을 보려면 원점 개체를 펼쳐 보세요.
4.  [트리 보기](tree_view/ko.md) 또는 [3D 보기에서](3D_view/ko.md) 평면 중 하나를 선택한 다음 **[<img src=images/PartDesign_NewSketch.svg style="width:16px"> [스케치 생성](PartDesign_NewSketch/ko.md)**버튼을 누릅니다.선택한 평면에 스케치가 생성됩니다.

[PartDesign Lines](PartDesign_Line.md), [PartDesign Planes](PartDesign_Plane.md) 및 [PartDesign CoordinateSystems와](PartDesign_CoordinateSystem.md) 같은 보조 기준도형을 생성할 때도 동일한 과정을 사용할 수 있습니다.


**참고:**

원점은 [App Origin](App_OriginGroupExtension.md) 객체(`App::Origin` 클래스)입이고 축과 평면은 각각 `App::Line` 및 `App::Plane` 유형의 객체입니다. 이러한 각 요소는 **Space** 막대를 사용하여 개별적으로 숨기거나 숨김 해제할 수 있습니다; 이는 다른 객체를 생성할 때 올바른 참조를 선택하는 데 유용합니다.


**참고 2:**

몸통 내부의 모든 요소는 몸통의 원점을 참조합니다. 즉, 몸통은 내부 요소의 배치에 영향을 주지 않고 전역 좌표계를 기준으로 이동 및 회전할 수 있습니다.

<img alt="" src=images/PartDesign_Body_Origin_tree.png ) ![](images/PartDesign_Body_Origin_view.png  style="width:" height="400px;">



*왼쪽: [트리 보기](tree_view/ko.md)에서 몸통의 원점. 오른쪽: [3D 보기](3D_view/ko.md)에서 원점 요소 표현.*



### 기반특징(Base Feature) 

기반특징은 몸통이 다른 고체 형상을 기반으로 할 때 몸통의 첫 번째 [도형특징입니다](PartDesign_Feature/ko.md).

![](images/PartDesign_Body_BaseFeature_tree.png ) 
*두 개의 몸통, 각각 이전에 생성된 고체에서 가져온 기반특징을 하나씩 가지고 있습니다.*

기반특징을 생성하려면:

1.  몸통 외부의 고체 형상을 선택하고

2.  
    **[<img src=images/PartDesign_Body.svg style="width:16px"> 몸통 생성**버튼을 누릅니다. 이렇게 하면 하나의 기반특징과 함께 새 몸통이 생성됩니다.


**참고:**

**[<img src=images/PartDesign_Body.svg style="width:16px"> 몸통생성**버튼을 누를 때, 기존 몸통이나 [특징을](PartDesign_Feature/ko.md) 선택할 수 없습니다.

이미 몸통이 있는 경우 다음과 같은 방법으로 기반특징을 생성할 수 있습니다:

-   [tree view에서](tree_view.md) 객체를 선택하고 몸통 내부로 드래그 앤 드롭합니다. 또는
-   [속성 편집기에서](property_editor/ko.md) 줄임표 **...**를 누르고 목록에서 개체를 선택하여 **Base Feature** 값을 편집합니다. 이 경우 기존 몸통을 기반특징으로 선택할 수 있습니다.


**참고:**

드래그 앤 드롭은 기반특징이 아직 없는 몸통에 대해서만 작동합니다.


**참고 2:**

몸통에 이미 여러 특징이 있는 경우 외부 고체를 끌어서 놓을 때, 기반특징은 특징 목록의 시작 부분에 생성됩니다. 즉, **Group** 속성의 시작 부분에 추가됩니다.

기반특징은 전적으로 선택 사항입니다. 이는 몸통 외부의 객체를 포함할 때만 존재합니다. 외부 고체가 포함되지 않은 경우에도 [스케치](Sketch/ko.md), [PartDesign Pad](PartDesign_Pad.md), [PartDesign_CompPrimitiveAdditive](PartDesign_CompPrimitiveAdditive.md) 및 기타 [도형특징을](PartDesign_Feature/ko.md) 사용하여 형상을 만들 수 있습니다.

![](images/PartDesign_Body_BaseFeature_Tip.svg )



*왼쪽: 외부 고체에서 가져온 기반특징(Base Feature)과 그 위에 많은 후속 [도형특징](PartDesign_Feature/ko.md)이 있는 몸통. 오른쪽:명시적인 기반특징이 없는 몸통*


**참고:**

다른 몸통을 기반특징으로 선택한 경우 형상이 있어야 합니다. 만일 몸통이 비어 있으면(도형특징 없거나 기반특징이 없는 등\...) 오류가 발생합니다.



### 끝단(Tip)

끝단은 몸통 외부에 노출되는 [도형특징입니다](PartDesign_Feature/ko.md); 즉, 작업대의 다른 도구(예를 들어 **[<img src=images/Part_SimpleCopy.svg style="width:16px">[Part Cut](Part_Cut.md)**)가 몸통의 형상을 사용해야 하는 경우, 형상의 끝단을 사용합니다. 다르게 말하면, 끝단은 마치 파라메트릭 이력이 존재하지 않는 것처럼 몸통의 최종 표현입니다.

![](images/PartDesign_Body_Tip_final.svg )



*왼쪽: 중간 특징들을 포함한 전체 파라메트릭 기록이 포함된 몸통. 오른쪽: 끝단(Tip)은 모델의 기록을 생략하고 몸통에서 내보낼 수 있는 최종 형상입니다.*

끝단은 몸통에서 생성된 마지막 특징으로 자동 설정됩니다. 그럼에도 불구하고 [트리 보기](tree_view/ko.md) 컨텍스트 메뉴(우클릭)를 열고 **[<img src=images/PartDesign_MoveTip.svg style="width:16px"> [Set tip](PartDesign_MoveTip.md)**을 선택하여 중간 특징 중 하나로 설정할 수도 있고, 또는 [속성 편집기에서](property_editor/ko.md) 몸통의 **Tip** 값을 변경하면 됩니다.

실제로 끝단을 변경하면 수정이력 되돌아 가므로 이전에 추가했어야 하는 특징을 추가할 수 있습니다. 또한 외부 도구에 다른 형상을 노출합니다.

[트리 보기에서](tree_view/ko.md) 몸통의 끝단은 녹색 원 안에 흰색 화살표로 구성된 아이콘 오버레이가 있는 [도형특징에](PartDesign_Feature/ko.md) 의해 인식됩니다.

![](images/PartDesign_Body_Tip_tree.png ) 
*두 개의 몸통, 각각 [도형특징](PartDesign_Feature/ko.md)을 가집니다. 끝단은 그 중 마지막 특징이며 오버레이 기호로 표시됩니다.*



### 다른 작업대와의 상호작용 

기본적으로 몸통 내부의 [도형특징들을](PartDesign_Feature/ko.md) 선택할 수 있는데 이는 [부품설계 작업대의](PartDesign_Workbench/ko.md) 도구를 사용하여 더 많은 특징을 편집하고 추가하는 데 필요하기 때문입니다. 그렇지만 [부품 작업대](Part_Workbench/ko.md) 및 [설계제도 작업대와](Draft_Workbench/ko.md) 같은 다른 작업대의 도구와 함께 사용하기 위해 개별적으로 특징을 선택하는 것은 권장되지 않는데 예상치 못한 결과가 나올 수도 있기 때문입니다; 그런 경우 [report view에](Report_view.md) **링크가 허용된 범위를 벗어났습니다**라는 오류 메시지가 나타날 수 있습니다.

따라서 다른 작업대와의 상호작용을 위해서는 [tree view에서](tree_view.md) 몸통 자체만 선택해야 합니다.몸통의 특정 하위 요소(꼭지점, 모서리, 면)를 선택해야 하는 경우 몸통의 **Display Mode Body** 속성을 `Tip`으로 전환해야 합니다. 이 모드가 활성화되면 몸통 아래의 객체([특징](PartDesign_Feature/ko.md), 기준도형, [스케치](Sketch/ko.md))에 대한 접근이 비활성화되고 몸통의 [끝단을](PartDesign_Body#Tip.md) 제외한 모든 항목에 대한 접근이 비활성화됩니다. [3D 보기에서](3D_view/ko.md) 숨겨집니다.

하위 요소가 다른 작업대와 함께 사용되면 **Display Mode Body**를 `Through`로 다시 설정할 수 있습니다.

![](images/PartDesign_Body_Tip_Display_mode.svg )



*왼쪽: "Display Mode Body"가 `Through*로 설정되면 개별 [특징](PartDesign_Feature/ko.md)을 선택하고 작업을 수행할 수 있습니다; 일반적으로 이는 권장되지 않습니다. 오른쪽: "Display Mode Body"가 {{incode|Tip`으로 설정되면 몸통에서 수행되는 모든 선택과 작업이 끝단(Tip)에서 수행되므로 몸통의 최종 모양만 노출됩니다.}}



### 가시성 관리 

몸통의 가시성은 포함된 모든 객체의 가시성을 대체합니다. 몸통이 숨겨져 있으면 그 안에 포함된 개체도 숨겨집니다. 개별 **Visibility** 속성이 `True`로 설정되어 있어도 마찬가지입니다.

여러 개의 [스케치가](Sketch/ko.md) 한 번에 표시될 수는 있지만 [도형특징](PartDesign_Feature/ko.md)(고체)는 한 번에 하나만 표시될 수 있습니다. 숨겨진 특징을 선택하고 키보드의 **Space** 막대를 누르면 해당 특징이 표시되고 이전에 표시되었던 특징은 자동으로 숨겨집니다.

![](images/PartDesign_Body_Visibility.png ) 
*몸통: 여러 개의 [스케치](Sketch/ko.md)가 동시에 표시될 수 있습니다. 그러나 끝단인지 여부에 관계없이 한 번에 하나의 고체 [도형특징](PartDesign_Feature/ko.md)만 표시될 수 있습니다.*



## 부착

[도형특징은](PartDesign_Feature/ko.md) [Part_Part2DObject와](Part_Part2DObject.md) 마찬가지로 다른 평면에 부착할 수 있습니다. 일반적으로 몸통의 [원점](PartDesign_Body#Origin.md) 또는 사용자 정의 [PartDesign Planes에](PartDesign_Plane.md) 의해 정의된 표준 평면입니다.

[스케치는](Sketch/ko.md) 생성될 때 일반적으로 평면에 부착됩니다.비슷한 방식으로 [PartDesign_CompPrimitiveAdditive도](PartDesign_CompPrimitiveAdditive.md) 부착할 수 있습니다. 이러한 개체를 평면에 연결하면 **Attachment Offset** 속성을 변경하여 몸통 내에서 이동할 수 있습니다. 부착 모드에 대한 자세한 내용은 [Part EditAttachment를](Part_EditAttachment.md) 참조하세요.

어디에도 부착되지 않은 [도형특징은](PartDesign_Feature/ko.md) [트리 보기에서](tree_view/ko.md) 해당 아이콘 옆에 빨간색 오버레이 기호와 함께 표시됩니다.

![](images/PartDesign_Body_Feature_attachment.png ) 
*몸통: 평면이나 좌표계에 부착되지 않은[도형특징](PartDesign_Feature/ko.md)은 [트리 보기](tree_view/ko.md)에서 해당 아이콘 옆에 오버레이 기호와 함께 표시됩니다.*



## 상속

**몸통(PartDesign Body)**는 프리캐드의 프로그램(소스코드)에서 정식으로는 `PartDesign::Body` 클래스의 인스턴스입니다. 그 조상은 중간의 `Part::BodyBase` 클래스를 거슬러 [Part Feature](Part_Feature.md) (`Part::Feature` 클래스)이며 Origin 확장으로 보강되었습니다.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*프로그램의 핵심 개체 간의 관계를 단순화한 다이어그램입니다. `PartDesign::Body* 객체는 파라메트릭 3D 고체를 구축하기 위한 것이므로 기본 {{incode|Part::Feature` 객체에서 파생됩니다.그리고 내부에 사용되는 기능의 배치를 제어하는 ​​Origin이 있습니다.}}



## 스크립팅


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md) 및 [scripted objects](scripted_objects.md).

문서에 개체를 추가하는 방법에 대한 일반적인 정보는 [Part Feature를](Part_Feature.md) 참조하세요.

몸통(PartDesign Body)은 문서의 `addObject()` 메서드를 사용하여 생성됩니다.몸통이 존재하면 이 몸통의 `addObject()` 또는 `addObjects()` 메서드를 사용하여 [도형특징을](PartDesign_Feature/ko.md) 몸통에 추가할 수 있습니다.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj.Label = "Custom label"

feat1 = App.ActiveDocument.addObject("PartDesign::AdditiveBox", "Box")
feat2 = App.ActiveDocument.addObject("PartDesign::AdditiveCylinder", "Cylinder")

obj.addObjects([feat1, feat2])
App.ActiveDocument.recompute()
```

다수의 몸통이 있는 문서에서는 `ActiveView`의 `setActiveObject` 메서드를 사용하여 [active Body를](PartDesign_Body#Active_status.md) 설정할 수 있습니다. 첫 번째 인수는 고정 문자열 `"pdbody"`이고, 두 번째 인수는 활성화되어야 하는 몸통 개체입니다. 
```python
import FreeCAD as App
import FreeCADGui as Gui

doc = App.newDocument()
obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("PartDesign::Body", "Body")

Gui.ActiveDocument.ActiveView.setActiveObject("pdbody", obj1)
App.ActiveDocument.recompute()
```





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Body/ko
