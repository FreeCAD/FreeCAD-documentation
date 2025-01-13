---
 GuiCommand:
   Name: Sketcher ReorientSketch
   MenuLocation: Sketch , Reorient sketch
   Workbenches: Sketcher_Workbench/ko, PartDesign_Workbench/ko
   SeeAlso: Sketcher_MapSketch/ko, Sketcher_NewSketch/ko
---

# Sketcher ReorientSketch/ko



## 설명

<img alt="" src=images/Sketcher_ReorientSketch.svg  style="width:24px;"> **스케치 방향 재설정** 도구는 (선택적) 편차를 적용하여 기본 평면 중 하나에 스케치를 재배치합니다. 스케치를 분리하는 데에도 사용할 수 있습니다.



## 용법

1.  스케치를 선택합니다.

2.  도구를 호출하는 방법에는 여러 가지가 있습니다.
    -   
        **<img src="images/Sketcher_ReorientSketch.svg" width=16px> 스케치 방향 재설정
**
        
        버튼을 누릅니다([부품설계 작업대에서는](PartDesign_Workbench/ko.md) 사용할 수 없음).

    -   메뉴에서 **Sketch → <img src="images/Sketcher_ReorientSketch.svg" width=16px> 스케치 방향 재설정** 을 선택합니다.

3.  스케치가 이미 어떤 것에 부착되어 있다면
    1.  **스케치에 받침이 있음** 대화상자가 열립니다.
    2.  스케치를 부착되어 있는 받침에서 떼내려면 **Yes** 단추를 누릅니다.

4.  **방향 선택** 대화상자가 열립니다.

5.  선택적으로 **Cancel** 단추를 눌러 스케치만 분리할 수 있습니다.

6.  방향에 대한 평면을 지정합니다. 평면은 스케치가 있는 지역 좌표계를 기준으로 합니다.
    -   **역방향** 확인란이 선택되어 있지 않은 경우:
        -   윗면: **XY 평면**
        -   정면: **XZ 평면**
        -   우면: **YZ 평면**
    -   **역방향** 확인란이 선택된 경우:
        -   밑면: **XY-평면**
        -   후면: **XZ-Plane**
        -   좌면: **YZ-평면**

7.  선택적으로 **편차(Offset)**를 변경합니다. 편차는 지역 좌표계의 Z, Y 또는 X 축을 따라 측정됩니다.

8.  
    **OK**단추를 누릅니다.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ReorientSketch/ko
