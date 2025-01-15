---
 GuiCommand:
   Name: Sketcher CreatePoint
   MenuLocation: Sketch , Sketcher geometries , Create point
   Workbenches: Sketcher_Workbench/ko
   Shortcut: **G** **Y**
---

# Sketcher CreatePoint/ko



## 설명

<img alt="" src=images/Sketcher_CreatePoint.svg  style="width:24px;"> **점 생성** 도구로 점을 생성합니다.



## 용법

See also: [Drawing aids](Sketcher_Workbench#Drawing_aids.md).

Pos-OVP = Positional [On-View-Parameters](Sketcher_Preferences#General.md). <small>(v1.0)</small> 

1.  이 도구를 호출하는 방법에는 여러 가지가 있습니다:
    -   
        **<img src="images/Sketcher_CreatePoint.svg" width=16px> 점 생성
**
        
        버튼을 누릅니다.

    -   메뉴에서 **Sketcher → Sketcher geometries → <img src="images/Sketcher_CreatePoint.svg" width=16px> 점 생성**을 선택합니다.

    -   [3D 보기영역에서](3D_view/ko.md) 마우스 오른쪽 버튼을 클릭하여 상황 메뉴에서 **<img src="images/Sketcher_CreatePoint.svg" width=16px> 점 생성**을 선택합니다.

    -   키보드 단축키를 사용하세요: **G** 다음 **Y**.
2.  커서가 점 생성 아이콘이 있는 십자 모양으로 바뀝니다.
3.  점을 선택합니다. 또는 Pos-OVP의 경우: X 및 Y 좌표를 입력합니다.
4.  점이 생성되고 적용 가능한 Pos-OVP 기반의 구속이 추가됩니다.
5.  만일 도구가 [계속 모드에서](Sketcher_Workbench#Continue_modes.md) 실행되는 경우:
    1.  선택적으로 점을 계속 생성합니다.
    2.  마치려면 마우스 오른쪽 버튼을 클릭하거나 **Esc**를 누르거나 다른 형상 또는 구속 도구를 시작하세요.



## 보충 설명 

-    {{VersionMinus|0.21}}: 점은 항상 스케치의 보조적 요소로 생성됩니다. 선택적으로 [Sketcher ToggleConstruction을](Sketcher_ToggleConstruction/ko.md) 사용하여 일반 형상으로 변경하여 스케치 편집 모드 외부에서 볼 수 있도록 합니다.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/ko
