# <img alt="스케치 작업대 아이콘" src=images/Workbench_Sketcher.svg  style="width:64px;"> Sketcher Workbench/ko






## 소개

<img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;"> 스케치 작업대에서는 다른 작업대에서 사용하기 위한 2D 스케치를 생성할 수 있습니다. 2D 스케치는 많은 CAD 모형의 출발점입니다. 스케치는 일반적으로 3D 형상을 생성하는 작업에 필요한 윤곽선(profile)과 경로를 정의합니다. 모형의 최종 형상은 다수의 스케치에 의존할 수 있습니다.

<img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [부품 작업대에서](Part_Workbench/ko.md) 정의된 부울 연산과 함께 스케치 작업대는 고체를 구축하는 [구성적 고체 기하학(SCG:Constructive Solid Geometry)방법의](Constructive_solid_geometry/ko.md) 기초를 형성합니다. 그러나 다른 많은 작업대에서도 스케치를 사용합니다.

스케치 작업대에는 2D 도형이 길이, 각도, 관계(수평, 수직, 직각 등) 측면에서 정확한 기하학적 정의를 따를 수 있도록 하는 [구속](#Constraints.md) 기능이 있습니다. 구속 조건 해결사는 2D 기하의 구속 범위를 계산하고 스케치의 자유도를 대화식으로 탐색할 수 있습니다.

스케치 작업대는 2D 설계도면 제작용이 아닙니다. 스케치를 사용하여 3D 고체 도형을 생성하면 스케치는 자동으로 숨겨지고 구속조건은 스케치 편집 모드에서만 볼 수 있게 됩니다. 인쇄용 2D 보기만 생성해야 하고 3D 모형을 생성하고 싶지 않은 경우 [설계제도 작업대(Draft Workbench)를](Draft_Workbench/ko.md) 활용하세요.

<img alt="" src=images/FC_ConstrainedSketch.png  style="width:450px;"> 
*완전히 구속된 스케치*



## 구속(拘束, Constraint) 

구속은 개체의 자유도를 제한하는 데 사용됩니다. 예를 들어, 구속이 없는 선분의 자유도(Degrees of Freedom 약어로 \"DoF\")는 4입니다: 수평 또는 수직으로 움직일 수 있고, 늘릴 수 있고, 회전할 수 있습니다.

수평 또는 수직 구속 또는 각도 구속(다른 선 또는 축 중 하나에 대한 기준)을 적용하면 회전 가능성을 제한하게 되고, 따라서 3개의 자유도를 갖게 됩니다. 선분의 양 끝점 중 하나를 원점에 대해 고정하면 2개의 자유도가 추가로 제거됩니다. 치수 구속을 적용하면 마지막 남은 자유도가 제거됩니다. 그러면 선이 **완전히 구속**된 것으로 간주됩니다.

개체는 서로 연관되어 구속될 수 있습니다. 일치점 구속조건을 사용하면 두 선이 해당 점 중 하나를 통해 결합될 수 있습니다. 그들 사이에 각도를 설정하거나 수직으로 설정할 수 있습니다. 선은 호나 원 등에 접할 수 있습니다. 여러 개체가 포함된 복잡한 스케치에는 완전 구속에 이르는 다양한 해결책이 있을 수 있습니다.

구속에는 기하학적 구속과 치수 구속의 두 가지 종류가 있습니다. 아래의 [도구](#Tools.md) 부분에 자세히 설명되어 있습니다.



### 구속 편집 

[주도적 치수 구속이](Sketcher_ToggleDrivingConstraint/ko.md) 생성될 때, **Ask for value after create a Dimension Constraint** [설정이](Sketcher_Preferences#Display/ko.md) 되어 있으면(기본 설정됨) 해당 값을 편집할 수 있는 대화상자가 열립니다.

![](images/Sketcher_Edit_Constraint.png )


<div class="mw-translate-fuzzy">

숫자 값이나 [표현식을](Expressions/ko.md) 입력할 수 있으며, 다른 표현식에서 쉽게 사용할 수 있도록 구속에 이름을 지정할 수도 있습니다. 또한 **참조(Reference)** 확인란을 선택하여 구속을 참조 모드로 전환할 수도 있습니다.


</div>

기존의 치수 구속값을 편집하려면 다음 중 하나를 하세요.

-   [3D 보기에서](3D_view/ko.md) 구속값을 두 번 클릭합니다.
-   [스케치 대화상자에서](Sketcher_Dialog/ko.md) 구속을 두 번 클릭합니다.
-   스케치 대화상자에서 구속을 마우스 오른쪽 버튼으로 클릭하고 상황에 메뉴에서 **값 변경**을 선택합니다.



### 구속 재배치 

치수 구속은 3D 보기에서 수동으로 위치를 변경할 수 있습니다. 구속 값 위에 마우스 왼쪽 버튼을 누른 채 마우스를 이동합니다. 기하학적 구속 기호는 자동으로 배치되며 이동할 수 없습니다.



## 윤곽(Profile) 스케치 

고체 생성을 위한 윤곽으로 사용할 수 있는 스케치를 생성하려면 다음과 같은 특정 규칙을 따라야 합니다.

-   스케치에는 단일 폐곡선만 포함되어야 합니다. 끝점 사이의 간격은 작더라도 허용되지 않습니다.
-   단일 폐곡선을 중첩하여 공백을 만들 수 있지만(예: 원 안에 작은 원) 스스로 교차하거나 다른 경계선과 교차해서는 안 됩니다.
-   하나의 단일 폐곡선은 다른 단일 폐곡선과 모서리를 공유할 수 없습니다. 중복된 모서리는 피해야 합니다.
-   공통점을 공유하는 두 개 이상의 모서리 또는 모서리에 닿는 점이 T-연결은 허용되지 않습니다.

이러한 규칙은 편집 모드 외부에 표시되지 않는 보조선(기본 색상 파란색)이나 스케치가 다른 용도로 사용되는 경우에는 적용되지 않습니다. 윤곽 스케치를 사용할 작업대 및 도구에 따라 추가 제한 사항이 적용될 수 있습니다.



## 그리기 보조도구 

스케치 작업대에는 기하 요소를 생성하고 구속을 적용할 때 도움이 될 수 있는 여러 가지 그리기 보조 도구와 기타 기능이 있습니다.



### 계속 모드 

두 가지 계속 모드가 있습니다: **도형 생성 \"계속 모드\"** 와 **구속 생성 \"계속 모드\"**. [환경설정에서](Sketcher_Preferences#Display/ko.md) 이를 선택하면(기본 설정됨) 관련 도구가 생성 완료 후 다시 시작됩니다. 계속되는 도구를 종료하려면 **Esc** 또는 마우스 오른쪽 버튼을 누르세요. 계속되는 도형 생성 도구가 이미 치수 입력을 받는 상태라면 이 작업을 반복해야 합니다. 다른 도형 또는 구속 생성 도구를 시작하여 계속 모드를 종료할 수도 있습니다. 도구가 활성화되지 않은 경우 **Esc**를 누르면 스케치 편집 모드가 종료됩니다. 실수로 **Esc**를 너무 많이 누르는 경우가 많다면 **Esc로 스케치 편집 모드를 나갈 수 있음** [설정을](Sketcher_Preferences#General/ko.md) 선택 취소하세요.



### 자동 구속 

**자동 구속**이 설정된(기본 설정됨) 스케치에서는 몇 가지 구속이 자동으로 적용됩니다.제안된 자동 구속의 아이콘은 올바르게 배치되면 커서 옆에 표시됩니다. 이 때 마우스 왼쪽 단추를 누르면 해당 구속이 적용됩니다. 이는 [스케치 대화상자에서](Sketcher_Dialog#Constraints/ko.md) 변경하거나 스케치의 **자동구속** [속성에서](Property_editor/ko.md) 변경할 수 있는 각각의 스케치별 설정입니다.

아래의 구속이 자동으로 적용됩니다:

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:16px;"> [점일치 구속](Sketcher_ConstrainCoincident/ko.md)

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:16px;"> [선위에 점 구속](Sketcher_ConstrainPointOnObject/ko.md)

-   <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:16px;"> [수평 구속](Sketcher_ConstrainHorizontal/ko.md)

-   <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:16px;"> [수직 구속](Sketcher_ConstrainVertical/ko.md)

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:16px;"> [접선 구속](Sketcher_ConstrainTangent/ko.md)

-    <small>(v1.0)</small> : <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:16px;"> [대칭 구속](Sketcher_ConstrainSymmetric/ko.md) (선 중점)



### 포착하기(捕捉,Snapping)


<small>(v0.21)</small> 

스케치에서 그리려는 도형을 격자선과 격자 교차점, 형상의 모서리, 선과 호의 중간점, 특정 각도에 [포착하는](Sketcher_Snap/ko.md) 것이 가능합니다. 포착 자체로는 구속이 생성되지 않는다는 점을 유의하세요. 예를 들어, [자동 구속이](#Auto_Constraints.md) 켜져 있는 경우에만 모서리에 포착하면 [선 위의 점 구속이](Sketcher_ConstrainPointOnObject/ko.md) 생성됩니다. 모서의 한 점을 선택해도 동일한 결과를 얻을 수 있습니다.



### 즉석 매개변수 


<small>(v1.0)</small> 

[기본 설정에서](Sketcher_Preferences#General.md) 선택한 옵션에 따라 스케치에서 즉석 입력 가능한 치수 매개변수만 활성화하거나 치수 및 위치 매개변수를 모두 활성화할 수 있습니다. 위치 매개변수를 사용하면 원의 중심이나 선의 시작점 등 정확한 좌표를 도형을 그릴 때 바로 입력할 수 있고, 치수 매개변수를 사용하면 원의 반지름, 선의 길이 및 각도 등 정확한 치수를 입력할 수 있습니다. 즉석 매개변수는 모든 도형 생성 도구에 대해서 가능하지는 않습니다.(예를 들면 꺾은선(Polyline) )

![](images/Sketcher_On_view_parameters_positional.png ) 
*위치 매개변수가 활성화로 원의 중심점 결정하기*

![](images/Sketcher_On_view_parameters_dimensional.png ) 
*치수 매개변수 활성화로 원의 반지름 결정하기*

값을 입력하고 **Enter** 또는 **Tab**을 눌러 확인하면 관련 구속이 자동으로 추가됩니다. 두 개의 매개변수(예: 점의 X 및 Y 좌표)가 동시에 표시되는 경우 한 값을 입력하고 점을 선택하여 다른 값을 정의할 수 있습니다. 객체에 따라 완전히 구속하려면 추가 구속이 필요할 수 있습니다. 즉석 매개변수로 인한 구속은 [자동 구속으로](Sketcher_Dialog#Constraints.md) 인해 발생할 수 있는 구속보다 우선합니다.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:300px;"> 
*모든 즉석 매개변수를 입력하여 생성된 호와 그 결과 자동으로 생성된 구속들*



### 좌표 표시 

**편집 중일 때 커서 옆에 좌표를 표시** [기본 설정가](Sketcher_Preferences#Display.md) 선택된 경우(기본값), 현재 도형 생성 도구의 매개변수(좌표, 반지름, 길이 및 각도)가 커서 옆에 표시됩니다. 이것은 즉석 매개변수가 표시되는 동안에는 비활성화됩니다.



## 선택 방법 

스케치가 편집 모드에 있는 동안 다음 선택 방법을 사용할 수 있습니다:



### 3D 보기 요소 선택 

FreeCAD의 다른 곳과 마찬가지로, 한 번의 마우스 왼쪽 클릭으로 [3D 보기에서](3D_view/ko.md) 요소를 선택할 수 있습니다. 그러나 여러 요소를 선택할 때 **Ctrl** 키를 누르고 있을 필요는 없습니다. 하지만 해당 키를 누르고 있는 것이 가능하며 선택 항목을 잃지 않고 클릭을 놓칠 수 있다는 이점이 있습니다. 모서리, 점 및 구속들을 같은 방식으로 선택할 수 있습니다.



### 3D 보기 박스 선택 

3D 보기의 박스 선택은 [표준 박스 선택](Std_BoxSelection/ko.md) 또는 [표준 박스요소 선택을](Std_BoxElementSelection/ko.md) 사용하지 않고도 작동합니다:

1.  활성화된 도구가 없도록 확인하십시오.
2.  다음 중 하나를 수행합니다:
    -   빈 영역을 클릭하고 직사각형을 왼쪽에서 오른쪽으로 드래그하여 직사각형 내부에 도형 요소들이 완전히 포함되도록 선택합니다.
    -   빈 영역을 클릭하고 직사각형을 오른쪽에서 왼쪽으로 드래그하여 직사각형에 닿거나 교차하도록 도형 요소들을 선택합니다.

모서리와 점을 박스 선택할 수 있지만 구속은 박스 선택할 수 없습니다.



### 3D 보기 연결된 도형 선택 


<small>(v1.0)</small> 

3D 보기에서 모서리를 두 번 클릭하면 끝점을 통해 해당 모서리와 직접 및 간접적으로 연결된 모든 모서리가 한번에 선택됩니다. [동일 구속을](Sketcher_ConstrainCoincident/ko.md) 사용하여 모서리를 연결할 필요가 없으며 끝점에는 동일한 좌표만 있으면 됩니다.



### 대화상자 선택 

모서리와 점은 [스케치 대화상자의](Sketcher_Dialog/ko.md) 요소 부문에서 선택할 수도 있고 대화상자의 구속 부문에서는 구속을 선택할 수 있습니다.



## 복사, 잘라내기, 붙여넣기 


<small>(v1.0)</small> 

선택한 스케치의 도형과 관련된 구속들을 복사하고, 잘라내고, 붙여넣는 데 표준 키보드 단축키, **Ctrl**+**C**, **Ctrl**+**X** 및 **Ctrl**+**V **를 사용할 수 있습니다. 이러한 도구는 **Sketch → Sketcher tools** 메뉴에서도 사용할 수도 있습니다. 동일한 스케치 내에서 사용할 수 있지만 다른 스케치나 FreeCAD의 별도 인스턴스 간에도 사용할 수 있습니다. 데이터는 Python 코드 형태로 오림판에 복사되므로 다른 방법으로도 사용할 수 있습니다(예: 포럼에 공유).



## 도구

스케치 작업대의 도구는 스케치 메뉴 및/또는 여러 도구 모음에 있습니다. <small>(v0.21)</small> : 거의 모든 스케치 도구 모음은 스케치가 편집 모드에 있는 동안에만 표시됩니다. 유일한 예외는 편집 모드에 스케치가 없는 경우에만 표시되는 [스케치 도구 모음입니다](#Sketcher_toolbar.md).

일부 도구는 스케치가 편집 모드에 있는 동안 [3D 보기](3D_view/ko.md) 상황에 맞는 메뉴나 [스케치 대화상자의](Sketcher_Dialog/ko.md) 상황에 맞는 메뉴에서도 사용할 수 있습니다.


<small>(v0.21)</small> 

: 스케치가 편집 모드에 있는 경우 구조 도구 모음은 해당 도구를 사용할 수 없으므로 숨겨집니다.



### 일반



#### 스케치 도구 모음 

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [스케치 생성](Sketcher_NewSketch/ko.md): 새 스케치를 생성하고 편집을 위한 [스케치 대화상자를](Sketcher_Dialog/ko.md) 엽니다.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [스케치 편집](Sketcher_EditSketch/ko.md): 기존 스케치를 편집하기 위해 스케치 대화상자를 엽니다.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [스케치 부착](Sketcher_MapSketch/ko.md): 선택한 도형에 스케치를 부착합니다.

-   <img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:32px;"> [스케치 방향 재설정](Sketcher_ReorientSketch/ko.md): 선택적 편차를 사용하여 기본 평면 중 하나에 스케치를 배치합니다. 스케치를 부착된 도형에서 분리하는 데에도 사용할 수 있습니다.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [스케치 유효성 검사](Sketcher_ValidateSketch/ko.md): 더 이상 편집할 수 없거나 잘못된 구속이 있는 스케치를 분석 및 복구하거나 누락된 일치 구속을 추가할 수 있습니다.

-   <img alt="" src=images/Sketcher_MergeSketches.svg  style="width:32px;"> [스케치 병합](Sketcher_MergeSketches/ko.md): 두 개 이상의 스케치를 병합하여 하나의 스케치를 생성합니다.

-   <img alt="" src=images/Sketcher_MirrorSketch.svg  style="width:32px;"> [스케치 대칭](Sketcher_MirrorSketch/ko.md): X축, Y축 또는 원점을 기준으로 대칭되는 스케치를 생성합니다.

#### Sketcher Edit Mode toolbar 

-   <img alt="" src=images/Sketcher_LeaveSketch.svg  style="width:32px;"> [스케치 닫기](Sketcher_LeaveSketch/ko.md): 스케치 편집 모드를 종료하고 [스케치 대화 상자를](Sketcher_Dialog/ko.md) 닫습니다.

-   <img alt="" src=images/Sketcher_ViewSketch.svg  style="width:32px;"> [스케치 보기](Sketcher_ViewSketch/ko.md): [3D 보기를](3D_view/ko.md) 스케치와 정렬합니다.

-   <img alt="" src=images/Sketcher_ViewSection.svg  style="width:32px;"> [스케치 단면 보](Sketcher_ViewSection/ko.md): 스케치 평면 앞쪽에 있는 객체와 객체의 일부를 숨기는 임시 절단 평면의 가시성을 전환합니다.

#### Sketcher edit tools toolbar 

-   <img alt="" src=images/Sketcher_Grid.svg  style="width:32px;"> [격자 전환](Sketcher_Grid/ko.md): 현재 편집 중인 스케치의 격자 보기를 전환합니다. 관련 메뉴에서 설정을 변경할 수 있습니다.<small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_Snap.svg  style="width:32px;"> [포착 전환](Sketcher_Snap/ko.md): 모든 스케치에서 포착기능을 전환 합니다. 관련 메뉴에서 설정을 변경할 수 있습니다. <small>(v0.21)</small> 

-   <img alt="" src=images/Sketcher_RenderingOrder.svg  style="width:32px;"> [렌더링 순서 구성](Sketcher_RenderingOrder/ko.md): 모든 스케치의 렌더링 순서는 관련 메뉴에서 변경할 수 있습니다. <small>(v0.21)</small> 



#### 기타

-   <img alt="" src=images/Sketcher_StopOperation.svg  style="width:32px;"> [작업 중지](Sketcher_StopOperation/ko.md): 현재 실행 중인 도형 또는 구속 생성 도구를 중지합니다.



### 스케치할 수 있는 도형들 

아래는 스케치 작업대에서 도형을 생성하는 도구들입니다.

-   <img alt="" src=images/Sketcher_CreatePoint.svg  style="width:32px;"> [점](Sketcher_CreatePoint/ko.md): 점을 생성합니다.

-   <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:32px;"> [꺾은선](Sketcher_CreatePolyline/ko.md): 끝점으로 연결된 일련의 선과 호를 만듭니다. 이 도구에는 여러 가지 모드가 있습니다.

-   <img alt="" src=images/Sketcher_CreateLine.svg  style="width:32px;"> [선](Sketcher_CreateLine/ko.md): 선을 생성합니다. <small>(v1.0)</small> : 이 도구에는 세 가지 모드가 있습니다.

-   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 호 생성:

  - <img alt="" src=images/Sketcher_CreateArc.svg  style="width:32px;"> [중심 기준 호](Sketcher_CreateArc.md): 중심과 끝점을 기준으로 호를 생성합니다.

  - <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:32px;"> [3점 기준 호](Sketcher_Create3PointArc/ko.md): 양 끝점과 호를 따라 한 점을 사용하여 호를 만듭니다. <small>(v1.0)</small> : 이것은 [중심 기준 호와](Sketcher_CreateArc/ko.md) 동일한 도구이지만 초기 모드가 다릅니다.

  - <img alt="" src=images/Sketcher_CreateArcOfEllipse.svg  style="width:32px;"> [타원호](Sketcher_CreateArcOfEllipse/ko.md): 타원호를 생성합니다.

  - <img alt="" src=images/Sketcher_CreateArcOfHyperbola.svg  style="width:32px;"> [쌍곡선 호](Sketcher_CreateArcOfHyperbola/ko.md): 쌍곡선 호를 생성합니다.

  - <img alt="" src=images/Sketcher_CreateArcOfParabola.svg  style="width:32px;"> [포물선 호](Sketcher_CreateArcOfParabola/ko.md): 포물선 호를 생성합니다.

-   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 원/타원 생성:

  - <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:32px;"> [중심 기준 원](Sketcher_CreateCircle/ko.md): 중심을 기준으로 반지름의 한 점을 잡아 원을 생성합니다.

  - <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:32px;"> [3점 기준 원](Sketcher_Create3PointCircle/ko.md): 원을 따라 3점으로 원을 만듭니다. <small>(v1.0)</small> : 이것은 [중심 기준 원과](Sketcher_CreateCircle.md) 동일한 도구이지만 초기 모드가 다릅니다.

  - <img alt="" src=images/Sketcher_CreateEllipseByCenter.svg  style="width:32px;"> [중심기준 타원](Sketcher_CreateEllipseByCenter/ko.md): 중심, 축 중 하나의 끝점 및 타원을 따라 있는 점을 기준으로 타원을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateEllipseBy3Points.svg  style="width:32px;"> [3점 기준 타원](Sketcher_CreateEllipseBy3Points/ko.md): 축 중 하나의 끝점과 타원을 따라 있는 점으로 타원을 생성합니다. <small>(v1.0)</small> : 이것은 [중심기준 타원과](Sketcher_CreateEllipseByCenter/ko.md) 동일한 도구이지만 초기 모드가 다릅니다.

-   <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 사각형 생성:

  - <img alt="" src=images/Sketcher_CreateRectangle.svg  style="width:32px;"> [사각형](Sketcher_CreateRectangle/ko.md): 사각형을 생성합니다. <small>(v1.0)</small> : 이 도구에는 네 가지 모드가 있습니다. 둥근 모퉁이와 편차 사본 생성은 선택적 기능입니다.

  - <img alt="" src=images/Sketcher_CreateRectangle_Center.svg  style="width:32px;"> [중심기준 직사각형](Sketcher_CreateRectangle_Center/ko.md): 중심기준으로 사각형을 생성합니다. <small>(v1.0)</small> : 이것은 [사각형과](Sketcher_CreateRectangle/ko.md) 동일한 도구이지만 초기 모드가 다릅니다.

  - <img alt="" src=images/Sketcher_CreateOblong.svg  style="width:32px;"> [둥근 사각형](Sketcher_CreateOblong/ko.md): 모퉁이가 둥근 사각형을 만듭니다.

-   <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 정다각형 생성:

  - <img alt="" src=images/Sketcher_CreateTriangle.svg  style="width:32px;"> [삼각형](Sketcher_CreateTriangle/ko.md): 정삼각형을 생성합니다. <small>(v1.0)</small> : 이것은 [정다각형과](Sketcher_CreateRegularPolygon/ko.md) 동일한 도구이지만 변의 갯수가 특정 값으로 미리 설정되어 있습니다.

  - <img alt="" src=images/Sketcher_CreateSquare.svg  style="width:32px;"> [사각형](Sketcher_CreateSquare/ko.md): 정사각형을 생성합니다.

  - <img alt="" src=images/Sketcher_CreatePentagon.svg  style="width:32px;"> [오각형](Sketcher_CreatePentagon/ko.md): 정오각형을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateHexagon.svg  style="width:32px;"> [육각형](Sketcher_CreateHexagon/ko.md): 정육각형을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateHeptagon.svg  style="width:32px;"> [칠각형](Sketcher_CreateHeptagon/ko.md): 정칠각형을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateOctagon.svg  style="width:32px;"> [팔각형](Sketcher_CreateOctagon/ko.md): 정팔각형을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateRegularPolygon.svg  style="width:32px;"> [정다각형](Sketcher_CreateRegularPolygon/ko.md): 정다각형을 생성합니다. 변의 갯수를 지정할 수 있습니다.

-   <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 홈 생성:

  - <img alt="" src=images/Sketcher_CreateSlot.svg  style="width:32px;"> [홈](Sketcher_CreateSlot/ko.md): 직선형의 홈을 생성합니다.

  - <img alt="" src=images/Sketcher_CreateArcSlot.svg  style="width:32px;"> [호 형 홈](Sketcher_CreateArcSlot/ko.md): 호 형태의 홈을 생성합니다.<small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-조절곡선 생성:

  - <img alt="" src=images/Sketcher_CreateBSpline.svg  style="width:32px;"> [조절점이 있는 B-조절곡선](Sketcher_CreateBSpline/ko.md): 조절점으로 곡률을 조절할 수 있는 B-조절곡선을 생성합니다. <small>(v1.0)</small> : 또는 매듭점으로 조절 가능한 곡선을 생성합니다.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSpline.svg  style="width:32px;"> [조절점이 있는 주기적인 B-조절곡선](Sketcher_CreatePeriodicBSpline/ko.md): 조절점으로 곡률을 조절할 수 있는 주기적인(닫힌) B-조절곡선을 생성합니다.<small>(v1.0)</small> : 이것은 [조절점이 있는 B-조절곡선과](Sketcher_CreateBSpline/ko.md) 동일한 도구이지만 초기 모드가 다릅니다.

  - <img alt="" src=images/Sketcher_CreateBSplineByInterpolation.svg  style="width:32px;"> [매듭 있는 B-조절곡선](Sketcher_CreateBSplineByInterpolation/ko.md): 매듭점으로 곡률을 조절할 수 있는 B-조절곡선 을 생성합니다.

  - <img alt="" src=images/Sketcher_CreatePeriodicBSplineByInterpolation.svg  style="width:32px;"> [매듭 있는 주기적인 B-조절곡선](Sketcher_CreatePeriodicBSplineByInterpolation/ko.md): 매듭점으로 곡률을 조절할 수 있는 주기적인(닫힌) B-조절곡선을 생성합니다.

-   <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:32px;"> [보조선 전환](Sketcher_ToggleConstruction/ko.md): 도형 생성 도구 전체를 보조선 모드로 전환하거나 선택한 도형만 보조선으로/에서 전환합니다.



### 스케치 구속 

아래는 [구속을](#Constraints.md) 생성하기 위한 도구입니다. 일부 구속에는 [도우미 구속을](Sketcher_helper_constraint/ko.md) 사용해야 합니다.

-   <img alt="" src=images/Sketcher_Dimension.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 치수 구속:

  - <img alt="" src=images/Sketcher_Dimension.svg  style="width:32px;"> [치수는](Sketcher_Dimension/ko.md) 스케치 작업대의 상황에 맞는 구속도구입니다. 현재 선택을 기반으로 적절한 치수 구속뿐만 아니라 기하학적 구속도 제공합니다. <small>(v1.0)</small> 

  - <img alt="" src=images/Sketcher_ConstrainDistanceX.svg  style="width:32px;"> [수평 거리](Sketcher_ConstrainDistanceX/ko.md): 두 점 또는 선의 끝점 사이의 수평 거리를 고정합니다. 하나의 점이 미리 선택된 경우 거리는 스케치 원점을 기준으로 합니다.

  - <img alt="" src=images/Sketcher_ConstrainDistanceY.svg  style="width:32px;"> [수직 거리](Sketcher_ConstrainDistanceY/ko.md): 두 점 또는 선의 끝점 사이의 수직 거리를 고정합니다. 한 점이 미리 선택된 경우 거리는 스케치 원점을 기준으로 합니다.

  - <img alt="" src=images/Sketcher_ConstrainDistance.svg  style="width:32px;"> [거리](Sketcher_ConstrainDistance/ko.md): 선의 길이, 두 점 사이의 거리, 점과 선 사이의 수직 거리를 고정합니다. 또는 <small>(v0.21)</small> , 두 원이나 호의 가장자리 사이, 또는 원이나 호의 가장자리와 선 사이의 거리를 고정합니다; 또는 <small>(v1.0)</small> , 호의 길이를 고정합니다.

  - <img alt="" src=images/Sketcher_ConstrainRadiam.svg  style="width:32px;"> [자동 반/지름](Sketcher_ConstrainRadiam/ko.md): 호 및 B-조절곡선 가중치 원의 반지름 또는 지름을 고정합니다.

  - <img alt="" src=images/Sketcher_ConstrainRadius.svg  style="width:32px;"> [반지름](Sketcher_ConstrainRadius/ko.md): 원, 호 및 B-조절곡선 가중치 원의 반지름을 고정합니다.

  - <img alt="" src=images/Sketcher_ConstrainDiameter.svg  style="width:32px;"> [지름](Sketcher_ConstrainDiameter/ko.md): 원과 호의 지름을 고정합니다.

  - <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:32px;"> [각도](Sketcher_ConstrainAngle/ko.md): 두 모서리 사이의 각도, 스케치의 수평 축과 선의 각도 또는 원호의 개구각도를 고정합니다.

  - <img alt="" src=images/Sketcher_ConstrainLock.svg  style="width:32px;"> [잠금](Sketcher_ConstrainLock/ko.md): 점에 [수평 거리](Sketcher_ConstrainDistanceX/ko.md) 및 [수직 거리](Sketcher_ConstrainDistanceY/ko.md) 구속을 적용합니다. 단일 점을 선택한 경우 구속은 스케치 원점을 참조합니다. 두 개 이상의 점이 선택된 경우 구속은 선택 항목의 마지막 점을 참조합니다.

-   <img alt="" src=images/Sketcher_ConstrainCoincidentUnified.svg  style="width:32px;"> [(통합된)일치](Sketcher_ConstrainCoincidentUnified/ko.md): 점 사이에 일치 구속을 생성하거나 모서리 또는 축의 점을 고정하거나 동심 구속을 생성합니다. 이것은 기존의[일치](Sketcher_ConstrainCoincident/ko.md) 및 [선위에 점](Sketcher_ConstrainPointOnObject/ko.md) 도구를 결합한 것입니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_ConstrainCoincident.svg  style="width:32px;"> [일치](Sketcher_ConstrainCoincident/ko.md): 점 사이에 일치 구속 또는 동심 구속을 생성합니다.

-   <img alt="" src=images/Sketcher_ConstrainPointOnObject.svg  style="width:32px;"> [선위에 점](Sketcher_ConstrainPointOnObject/ko.md): 점을 모서리나 축 위에 고정합니다.

-   <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;">수평/수직 구속:

  - <img alt="" src=images/Sketcher_ConstrainHorVer.svg  style="width:32px;"> [수평/수직](Sketcher_ConstrainHorVer/ko.md): 선이나 점 쌍을 수평 또는 수직 중 현재 정렬에 가장 가까운 쪽으로 구속합니다. 이것은 [수평](Sketcher_ConstrainHorizontal/ko.md) 및 [수직](Sketcher_ConstrainVertical/ko.md) 도구를 결합한 것입니다. <small>(v1.0)</small> 

  - <img alt="" src=images/Sketcher_ConstrainHorizontal.svg  style="width:32px;"> [수평](Sketcher_ConstrainHorizontal/ko.md): 선이나 점 쌍이 수평이 되도록 구속합니다.

  - <img alt="" src=images/Sketcher_ConstrainVertical.svg  style="width:32px;"> [수직](Sketcher_ConstrainVertical/ko.md): 선이나 점 쌍이 수직이 되도록 구속합니다.

-   <img alt="" src=images/Sketcher_ConstrainParallel.svg  style="width:32px;"> [평행](Sketcher_ConstrainParallel/ko.md): 선이 평행하도록 구속합니다.

-   <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:32px;"> [직교](Sketcher_ConstrainPerpendular/ko.md): 두 선이 직교 하도록 구속하거나, 두 모서리 또는 모서리와 축이 교차점에서 직교 하도록 구속합니다. 이 구속은 두 개의 모서리를 연결하여 두 모서리가 접합점에서 직교 하도록 강제할 수도 있습니다.

-   <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:32px;"> [접선 또는 동일선상](Sketcher_ConstrainTangent/ko.md): 두 모서리 또는 모서리와 축이 접하도록 구속합니다. 이 구속은 또한 두 모서리를 연결하여 두 모서리가 접합점에서 접하도록 할 수도 있습니다. 두 개의 선을 선택하면 동일 선상에 놓이게 됩니다.

-   <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:32px;"> [동일](Sketcher_ConstrainEqual/ko.md): 모서리가 동일한 길이(선) 또는 곡률(B-조절곡선을 제외한 다른 곡선)을 갖도록 제한합니다.

-   <img alt="" src=images/Sketcher_ConstrainSymmetric.svg  style="width:32px;"> [대칭](Sketcher_ConstrainSymmetric/ko.md): 두 점이 선이나 축을 기준으로 또는 세 번째 점을 기준으로 대칭이 되도록 구속합니다.

-   <img alt="" src=images/Sketcher_ConstrainBlock.svg  style="width:32px;"> [차단](Sketcher_ConstrainBlock/ko.md): 단 하나의 구속으로 선택된 다수의 모서리들을 그자리에 고정합니다. 주로 B-조절곡선용으로 사용됩니다.

-   <img alt="" src=images/Sketcher_ConstrainSnellsLaw.svg  style="width:32px;"> [굴절 (스넬의 법칙)](Sketcher_ConstrainSnellsLaw/ko.md): 두 개의 선이 경계선을 통과할 때 빛의 굴절 법칙을 따르도록 제한합니다.

-   <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 구속 전환:

  - <img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:32px;"> [주도/참조 구속 전환](Sketcher_ToggleDrivingConstraint/ko.md): 치수 구속 생성 도구를주도 모드와 참조 모드 간에 전환하거나 선택된 치수 구속만을 해당 모드 간에 전환합니다.

  - <img alt="" src=images/Sketcher_ToggleActiveConstraint.svg  style="width:32px;"> [구속 활성/비활성화](Sketcher_ToggleActiveConstraint/ko.md): 선택한 구속을 활성화하거나 비활성화합니다.

### Sketcher tools 

-   <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 모깎기/모따기:

  - <img alt="" src=images/Sketcher_CreateFillet.svg  style="width:32px;"> [모깎기](Sketcher_CreateFillet/ko.md): 평행하지 않은 두 모서리 사이에 모깎기를 만듭니다. <small>(v1.0)</small> : 이 도구는 모따기를 생성할 수도 있습니다.

  - <img alt="" src=images/Sketcher_CreateChamfer.svg  style="width:32px;"> [모따기](Sketcher_CreateChamfer/ko.md): 평행하지 않은 두 가장자리 사이에 모따기를 생성합니다. 이것은 [모깎기와](Sketcher_CreateFillet/ko.md) 동일한 도구이지만 초기 모드가 다릅니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Trimming.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> 모서리 편집:

  - <img alt="" src=images/Sketcher_Trimming.svg  style="width:32px;"> [다듬기](Sketcher_Trimming/ko.md): 다른 모서리와 가장 가까운 교차점에서 가장자리를 잘라 다듬습니다.

  - <img alt="" src=images/Sketcher_Split.svg  style="width:32px;"> [분할](Sketcher_Split/ko.md): Splits an edge while transferring most constraints.

  - <img alt="" src=images/Sketcher_Extend.svg  style="width:32px;"> [연장](Sketcher_Extend/ko.md): 선이나 호를 임의의 위치나 대상 모서리나 점까지 연장하거나 줄입니다.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Sketcher_External.svg  style="width:32px;"> [외부 도형](Sketcher_External/ko.md): 스케치 외부 객체에 속하는 모서리 및 꼭지점을 현재 스케치 평면에 투영합니다.


</div>

-   <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> External geometry:

  - <img alt="" src=images/Sketcher_Projection.svg  style="width:32px;"> [Create external projection geometry](Sketcher_Projection.md): Creates the projection edges of external geometry. <small>(v1.1)</small> 

  - <img alt="" src=images/Sketcher_Intersection.svg  style="width:32px;"> [Create external intersection geometry](Sketcher_Intersection.md): Creates the intersection edges of external geometry with the sketch plane. <small>(v1.1)</small> 

-   <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:32px;"> [먹지 복사](Sketcher_CarbonCopy/ko.md): 다른 스케치의 모든 형상과 구속을 활성 스케치에 복사합니다.

-   <img alt="" src=images/Sketcher_SelectOrigin.svg  style="width:32px;"> [원점 선택](Sketcher_SelectOrigi/ko.md): 스케치의 원점을 선택합니다.

-   <img alt="" src=images/Sketcher_SelectHorizontalAxis.svg  style="width:32px;"> [수평축 선택](Sketcher_SelectHorizontalAxis/ko.md): 스케치의 수평축을 선택합니다.

-   <img alt="" src=images/Sketcher_SelectVerticalAxis.svg  style="width:32px;"> [수직축 선택](Sketcher_SelectVerticalAxis/ko.md): 스케치의 수직축을 선택합니다.

-   <img alt="" src=images/Sketcher_Translate.svg  style="width:32px;"> [배열 변환](Sketcher_Translate/ko.md): 선택한 요소를 이동하거나 선택적으로 복사본을 만듭니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Rotate.svg  style="width:32px;"> [회전 변환](Sketcher_Rotate/ko.md): 선택한 요소를 회전하거나 선택적으로 회전된 사본을 생성합니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Scale.svg  style="width:32px;"> [배율 변환](Sketcher_Scale/ko.md): 선택한 요소의 크기 배율을 조정하거나 필요한 경우 배율이 조정된 사본을 생성합니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Offset.svg  style="width:32px;"> [도형 편차](Sketcher_Offset/ko.md): 선택한 모서리 주위에 등거리 모서리를 만듭니다.<small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_Symmetry.svg  style="width:32px;"> [대칭](Sketcher_Symmetry/ko.md): 선택한 요소의 대칭 사본을 만듭니다.

-   <img alt="" src=images/Sketcher_RemoveAxesAlignment.svg  style="width:32px;"> [축정렬 제거](Sketcher_RemoveAxesAlignment/ko.md): [수평](Sketcher_ConstrainHorizontal/ko.md) 및 [수직](Sketcher_ConstrainVertical/ko.md) 구속을 [평행및](Sketcher_ConstrainParallel.md) [수직](Sketcher_ConstrainPerpendicular.md) 구속으로 바꿔서 선택한 모서리의 축 정렬을 제거합니다.

-   <img alt="" src=images/Sketcher_DeleteAllGeometry.svg  style="width:32px;"> [모든 도형 삭제](Sketcher_DeleteAllGeometry/ko.md): 스케치에서 모든 도형과 구속을 삭제합니다.

-   <img alt="" src=images/Sketcher_DeleteAllConstraints.svg  style="width:32px;"> [모든 구속 삭제](Sketcher_DeleteAllConstraints/ko.md): 스케치에서 모든 구속을 삭제합니다.

-   <img alt="" src=images/Edit-copy.svg  style="width:32px;"> 스케치에서 복사: [복사, 잘라내기, 붙여넣기](#Copy,_cut_and_paste.md) 참고.

-   <img alt="" src=images/Edit-cut.svg  style="width:32px;"> 스케치에서 잘라내기: [복사, 잘라내기, 붙여넣기](#Copy,_cut_and_paste.md) 참고.

-   <img alt="" src=images/Edit-paste.svg  style="width:32px;"> 스케치에 붙여넣기: [복사, 잘라내기, 붙여넣기](#Copy,_cut_and_paste.md) 참고.



### B-조절곡선 도구 

-   <img alt="" src=images/Sketcher_BSplineConvertToNURBS.svg  style="width:32px;"> [도형을 B-조절곡선으로 변환](Sketcher_BSplineConvertToNURBS/ko.md): 곡선을 B-조절곡선으로 변환합니다.

-   <img alt="" src=images/Sketcher_BSplineIncreaseDegree.svg  style="width:32px;"> [Increase B-spline degree](Sketcher_BSplineIncreaseDegree.md): Increases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineDecreaseDegree.svg  style="width:32px;"> [Decrease B-spline degree](Sketcher_BSplineDecreaseDegree.md): Decreases the degree (order) of B-splines.

-   <img alt="" src=images/Sketcher_BSplineIncreaseKnotMultiplicity.svg  style="width:32px;"> [Increase knot multiplicity](Sketcher_BSplineIncreaseKnotMultiplicity.md): Increases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineDecreaseKnotMultiplicity.svg  style="width:32px;"> [Decrease knot multiplicity](Sketcher_BSplineDecreaseKnotMultiplicity.md): Decreases the multiplicity of a B-spline knot.

-   <img alt="" src=images/Sketcher_BSplineInsertKnot.svg  style="width:32px;"> [Insert knot](Sketcher_BSplineInsertKnot.md): Inserts a knot into a B-spline or increases the multiplicity of an existing knot.

-   <img alt="" src=images/Sketcher_JoinCurves.svg  style="width:32px;"> [Join curves](Sketcher_JoinCurves.md): Creates a B-spline by joining two existing B-splines or other edges. <small>(v0.21)</small> 

### Sketcher visual 

-   <img alt="" src=images/Sketcher_SelectElementsWithDoFs.svg  style="width:32px;"> [불구속된 요소 선택](Sketcher_SelectElementsWithDoFs/ko.md): 스케치에서 완전히 구속되지 않은 요소를 모두 선택해 표시합니다.

-   <img alt="" src=images/Sketcher_SelectConstraints.svg  style="width:32px;"> [관련된 구속 선택](Sketcher_SelectConstraints/ko.md): 선택한 도형과 관련된 구속을 모두 선택해 표시합니다.

-   <img alt="" src=images/Sketcher_SelectElementsAssociatedWithConstraints.svg  style="width:32px;"> [관련된 도형 선택](Sketcher_SelectElementsAssociatedWithConstraints/ko.md): 선택한 구속과 관련된 도형을 모두 선택해 표시합니다.

-   <img alt="" src=images/Sketcher_SelectRedundantConstraints.svg  style="width:32px;"> [중복된 구속 선택](Sketcher_SelectRedundantConstraints/ko.md): 스케치에서 중복되는 구속을 모두 선택해 표시합니다.

-   <img alt="" src=images/Sketcher_SelectConflictingConstraints.svg  style="width:32px;"> [충돌하는 구속 선택](Sketcher_SelectConflictingConstraints/ko.md): 스케치에서 충돌하는 구속을 모두 선택해 표시합니다.

-   <img alt="" src=images/Sketcher_ArcOverlay.svg  style="width:32px;"> [호의 연장선 보이기/숨기기](Sketcher_ArcOverlay/ko.md): 스케치에서 모든 호의 연장선(호 아래 놓인 가상 원)을 표시하거나 숨깁니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> B-조절곡선 정보층 보이기/숨기기:

  - <img alt="" src=images/Sketcher_BSplineDegree.svg  style="width:32px;"> [Show/hide B-spline degree](Sketcher_BSplineDegree.md): Shows or hides the B-spline degree in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePolygon.svg  style="width:32px;"> [B-조절곡선 조절 다각형 보이기/숨기기](Sketcher_BSplinePolygon/ko.md): 모든 스케치에서 B-조절곡선 제어 다각형을 표시하거나 숨깁니다.

  - <img alt="" src=images/Sketcher_BSplineComb.svg  style="width:32px;"> [B-조절곡선 곡률빗살 보이기/숨기기](Sketcher_BSplineComb/ko.md): 모든 스케치에서 B-조절곡선의 곡률 빗살을 표시하거나 숨깁니다

  - <img alt="" src=images/Sketcher_BSplineKnotMultiplicity.svg  style="width:32px;"> [Show/hide B-spline knot multiplicity](Sketcher_BSplineKnotMultiplicity.md): Shows or hides the B-spline knot multiplicity in all sketches.

  - <img alt="" src=images/Sketcher_BSplinePoleWeight.svg  style="width:32px;"> [B-조절곡선 조절점 가중치 보이기/숨기기](Sketcher_BSplinePoleWeight/ko.md): 모든 스케치에서 B-조절곡선 제어점의 가중치를 표시하거나 숨깁니다.

-   <img alt="" src=images/Sketcher_RestoreInternalAlignmentGeometry.svg  style="width:32px;"> [내부 도형 보이기/숨기기](Sketcher_RestoreInternalAlignmentGeometry/ko.md): 도형의 내부 기하 구조를 숨기거나, 누락된 내부 기하 구조를 다시 보입니다.

-   <img alt="" src=images/Sketcher_SwitchVirtualSpace.svg  style="width:32px;"> [Switch virtual space](Sketcher_SwitchVirtualSpace.md): (un)hides constraints or switches the visible virtual space.



### 폐기된 도구들 

-   <img alt="" src=images/Sketcher_Clone.svg  style="width:32px;"> [Clone](Sketcher_Clone.md): Clones a Sketcher element. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_CloseShape.svg  style="width:32px;"> [Close shape](Sketcher_CloseShape.md): Creates a closed shape by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_CreatePointFillet.svg  style="width:32px;"> [Corner-preserving fillet](Sketcher_CreatePointFillet.md): Creates a fillet between two non-parallel lines while preserving their corner point. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_ConnectLines.svg  style="width:32px;"> [Connect edges](Sketcher_ConnectLines.md): Connect Sketcher elements by applying coincident constraints to endpoints. Not available in <small>(v0.21)</small> .

-   <img alt="" src=images/Sketcher_Copy.svg  style="width:32px;"> [Copy](Sketcher_Copy.md): Copies a Sketcher element. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_Move.svg  style="width:32px;"> [Move](Sketcher_Move.md): Moves the selected geometry taking as reference the last selected point. Not available in <small>(v1.0)</small> .

-   <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> [Rectangular array](Sketcher_RectangularArray.md): Creates an array of selected Sketcher elements. Not available in <small>(v1.0)</small> .



## 환경설정

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [환경 설정](Sketcher_Preferences/ko.md): 스케치 작업대의 기본 설정입니다.



## 모범 사례 

모든 CAD 사용자는 시간이 지남에 따라 자신만의 작업 방식을 개발하지만 따라야 할 몇 가지 유용한 일반 원칙이 있습니다.

-   일련의 간단한 스케치는 복잡한 단일 스케치보다 관리하기가 더 쉽습니다. 예를 들어, 첫 번째 스케치는 기본 3D 도형의 특징(깔판 또는 회전)을 위해 만들고 두 번째 스케치에는 구멍이나 잘라내기(오목 자리)를 포함할 수 있습니다. 일부 세부 사항은 나중에 3D 도형특징으로 구현하기 위해 생략할 수 있습니다. 스케치에 모깎기가 너무 많은 경우 이를 피하고 3D 도형특징으로 추가하도록 선택할 수 있습니다.
-   항상 닫힌 윤곽선(Profile)을 그립니다. 그렇지 않으면 스케치가 고체가 아니라 열린 면 세트를 생성합니다. 일부 개체를 고체 생성에 포함하지 않으려면 구성 모드 도구를 사용하여 해당 개체를 구성 요소로 전환합니다.
-   자동 구속 기능을 사용하면 수동으로 추가해야 하는 구속의 수를 줄일 수 있습니다.
-   일반적 규칙은 기하학적 구속을 먼저 적용한 다음 치수 구속을 적용하고 마지막으로 스케치를 잠급니다. 하지만 기억하세요: 규칙은 절대적인 것이 아닙니다. 스케치를 조작하는 데 문제가 있는 경우 윤곽을 완성하기 전에 먼저 몇 가지 개체를 구속하는 것이 유용할 수 있습니다.
-   가능하다면 잠금 구속을 사용하여 스케치의 중심을 원점(0,0)에 두십시오. 스케치가 대칭이 아니라면 스케치의 점 중 하나를 원점에 두거나,적당한 정수 숫자 거리에 두고 잠금 구속을 합니다.
-   길이 구속과 수평(또는 수직) 거리 구속 중에서 선택할 수 있는 경우 후자를 선호하십시오. 수평 및 수직 거리 구속은 컴퓨터가 더 빠르게 계산합니다.
-   일반적으로 사용하기에 가장 좋은 구속은 다음과 같습니다.
    -   수평 및 수직 구속
    -   수평 및 수직 길이 구속
    -   점대점 접선 구속.
-   가능하다면 다음의 사용을 제한하십시오:
    -   (기울기가 있는)일반 길이 구속
    -   모서리 간 접선 구속
    -   객체 위의 점 구속
    -   대칭 구속
-   스케치가 완료된 후(녹색으로 변함) 스케치의 유효성이 의심스러운 경우 스케치 편집 작업을 종료하고<img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:24px;"> [스케치 유효성 검사를](Sketcher_ValidateSketch/ko.md) 합니다.



## 자습서

[Sketcher 강의](https://forum.freecadweb.org/viewtopic.php?f=36&t=30104) by chrisb. 스케치에 대한 자세한 매뉴얼 역할을 하는 80쪽이 넘는 PDF 문서입니다. 스케치의 기본 사항을 설명하고 기하학적 모양 생성 및 각각의 구속에 대해 자세히 설명합니다.

-   [기본 스케치 자습서](Basic_Sketcher_Tutorialko.md) - 초보자용
-   [스케치 완전 초보 자습서](Sketcher_Micro_Tutorial_-_Constraint_Practices/ko.md) - 구속 연습
-   [스케치 요구사항](Sketcher_requirement_for_a_sketch/ko.md) - 스케치에 최소 요구사항 및 스케치의 완전한 결정



## 스크립팅

[스케치 스크립팅](Sketcher_scripting/ko.md) 페이지에는 Python 스크립트에서 구속을 생성하는 방법에 대한 예가 포함되어 있습니다.



## 예제

스케치 도구를 사용하여 얻을 수 있는 작업에 대한 아이디어를 보려면 [스케치 예제를](Sketcher_Examples/ko.md) 참조하세요.

<img alt="" src=images/Sketcher_ExampleHinge-01.gif  style="width:80px;"> <img alt="" src=images/Sketcher_ExampleHinge-15.png  style="width:90px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Sketcher](Category_Sketcher.md) > Sketcher Workbench/ko
