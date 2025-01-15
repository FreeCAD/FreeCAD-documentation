---
 GuiCommand:
   Name: 스케치 변환
   MenuLocation: Sketch , Sketcher tools , Array transform
   Workbenches: Sketcher_Workbench/ko
   Shortcut: **W**
   Version: 1.0
   SeeAlso: 
---

# Sketcher Translate/ko



## 설명

<img alt="" src=images/Sketcher_Translate.svg  style="width:24px;"> **스케치 변환** 도구는 선택한 요소를 이동하거나 선택적으로 복사본을 만듭니다. 복사본은 한 방향 또는 두 방향으로 균등하게 배치됩니다.



## 용법


<div lang="en" dir="ltr" class="mw-content-ltr">

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).


</div>


<div lang="en" dir="ltr" class="mw-content-ltr">

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md).
Dim-OVP = Dimensional On-View-Parameters.


</div>



### 도형 이동하기 

1.  하나 이상의 모서리 및 [점을](Sketcher_CreatePoint/ko.md) 선택합니다. 선택한 요소에 적용된 구속도 함께 처리됩니다. 그 외의 다른 모든 구속(원점에서의 거리 구속 등)은 삭제됩니다.
2.  도구를 호출하는 방법에는 여러 가지가 있습니다.
    -   
        **<img src="images/Sketcher_Translate.svg" width=16px> [이동/배열 변환](Sketcher_Translate.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **Sketch → Sketcher tools → <img src="images/Sketcher_Translate.svg" width=16px> 이동/배열 변환** 옵션을 선택합니다.

    -   [3D 보기영역에서](3D_view/ko.md) 마우스 오른쪽 버튼으로 클릭하고 상황 메뉴에서 **<img src="images/Sketcher_Translate.svg" width=16px> 이동/배열 변환** 옵션을 선택합니다.

    -   키보드 단축키: **W**를 사용하세요.
3.  커서가 십자 모양으로 바뀌고 도구 아이콘이 커서 옆에 표시됩니다.
4.  **변환 매개변수** 입력창이 [스케치 대화상자](Sketcher_Dialog/ko.md) 상단에 추가됩니다.
5.  변환 방향(vector)의 시작점을 선택합니다. 또는 Pos-OVP의 경우: X 및 Y 좌표를 입력합니다.
6.  변환 방향의 끝점을 선택합니다. 또는 Dim-OVP의 경우: 변환 방향의 길이 및 각도를 입력합니다. 각도는 스케치의 X축을 기준으로 합니다.
7.  요소가 이동됩니다. Pos-OVP 또는 Dim-OVP 기반 제약 조건은 추가되지 않습니다.



### 도형 복사하기 

1.  하나 이상의 모서리 및 [점을](Sketcher_CreatePoint/ko.md) 선택합니다. 선택한 요소에 적용된 구속도 함께 처리됩니다.
2.  위에서 설명한 대로 도구를 호출합니다.
3.  커서가 십자 모양으로 바뀝니다.
4.  **변환 매개변수** 입력창이 [스케치 대화상자](Sketcher_Dialog/ko.md) 상단에 추가됩니다.
5.  선택적으로 첫 번째 변환방향을 따라 복사본 수를 입력합니다.
    -   숫자를 입력합니다.
    -   숫자를 늘리려면 **U** 키를 누르세요.
    -   숫자를 줄이려면 **J** 키를 누르세요.
6.  선택적으로 두 번째 방향을 따라 행 수를 변경합니다.
    -   숫자를 입력합니다.
    -   숫자를 늘리려면 **R** 키를 누르세요.
    -   숫자를 줄이려면 **F** 키를 누르세요.
7.  필요에 따라 작업에서 치수 구속조건을 제외하려면 **동일 구속 적용** 확인란을 선택합니다. 대신 원본 개체와 복사본 사이에 <img alt="" src=images/Sketcher_ConstrainEqual.svg  style="width:24px;"> [동일 구속을](Sketcher_ConstrainEqual/ko.md) 적용합니다.
8.  첫 번째 벡터의 시작점을 선택합니다. 또는 Pos-OVP의 경우: X 및 Y 좌표를 입력합니다. 이 벡터는 복사본 간의 오프셋을 정의합니다.
9.  첫 번째 벡터의 끝점을 선택합니다. 또는 Dim-OVP의 경우: 벡터의 길이 및 각도를 입력합니다. 각도는 스케치의 X축을 기준으로 합니다.
10. 행이 두 개 이상인 경우: 두 번째 벡터의 끝점을 선택합니다. 또는 Dim-OVP의 경우: 벡터의 길이 및/또는 각도를 입력합니다. 각도는 스케치의 X축을 기준으로 합니다. 이 벡터는 행 사이의 오프셋을 정의합니다.
11. 요소가 복사됩니다. Pos-OVP 또는 Dim-OVP 기반의 구속은 추가되지 않습니다.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Translate/ko
