---
 GuiCommand:
   Name: Sketcher ToggleDrivingConstraint
   MenuLocation: Sketch , Sketcher constraints , Toggle driving/reference constraint
   Workbenches: Sketcher_Workbench/ko
   Shortcut: **K** **X**
   Version: 0.16
   SeeAlso: Sketcher_ToggleActiveConstraint/ko
---

# Sketcher ToggleDrivingConstraint/ko



## 설명

<img alt="" src=images/Sketcher_ToggleDrivingConstraint.svg  style="width:24px;"> **주도적 구속 전환** 도구는 모든 [치수 구속을](Sketcher_Workbench#Sketcher_CompDimensionTools.md) 주도/참조 모드 간 전환하거나 선택된 치수 구속만 한정하여 두 모드 간에 전환을 합니다.

주도적(driving) 구속과 달리 참조 구속은 실제로는 스케치를 구속하지 않고 다른 구속에 종속적(driven)입니다. 참조 구속은 측정값을 확인하는 데 유용할 수 있습니다. [표현식에서는](Expressions/ko.md) 사용할 수 있지만, but not in the sketch itself.

![](images/Sketcher_ToggleConstraint_example.png )


<div class="mw-translate-fuzzy">



*윤곽(profile)을 정의하기 위해 수평 거리 구속(50mm), 수직 구속(30mm) 및 각도 구속(75°)을 설정했습니다; 이 3가지 구속으로 이미 도형의 윤곽이 정의되었기 때문에 더 이상의 치수 구속은 중복되어 불가능합니다. 기울어진 선분의 길이(31.0583mm)를 알기 위해  치수 구속이 참조 모드(파란색)로 전환되어 추가되었습니다. *


</div>



## 용법



### 치수구속 도구모음을 전환 

1.  아무 치수 구속도 선택되지 않았는지 확인하십시오.
2.  도구를 호출하는 방법에는 여러 가지가 있습니다.
    -   
        **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> '''주도/참조 구속 전환'''
**
        
        단추를 누릅니다.

    -   메뉴에서 **Sketch → Sketcher Constraints → <img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> 주도/참조 구속 전환**을 선택합니다.

    -   키보드 단축키를 사용하세요: **K** 다음 **X**.
3.  치수 구속 생성 도구의 모드가 전환됩니다.
    -   주도 모드에서는 메뉴와 도구 모음 아이콘이 빨간색이며 주도적 구속을 생성합니다(기본값 [color](Sketcher_Preferences#Appearance.md) 빨간색). 그러면 이 도구의 아이콘은 <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:16px;">입니다.
    -   참조 모드에서는 메뉴와 도구 모음 아이콘이 파란색이며 참조적 구속을 생성합니다(기본 색상은 파란색). 그러면 이 도구의 아이콘은 <img alt="" src=images/Sketcher_ToggleConstraint_Driven.svg  style="width:16px;">입니다.



### 선택된 치수 구속만 전환 

1.  하나 이상의 치수 구속을 선택합니다.
2.  위에서 설명한 대로 도구를 호출하거나 다음 방법 중 하나를 사용하여 도구를 호출합니다.
    -   
        <small>(v1.0)</small> 
        
        : [3D 보기를](3D_view/ko.md) 마우스 오른쪽 버튼으로 클릭하여 상황 메뉴에서 **<img src="images/Sketcher_ToggleDrivingConstraint.svg" width=16px> 주도/참조 구속 전환**을 선택합니다.

    -   [스케치 대화상자의](Sketcher_Dialog/ko.md) **구속(Constraints)** 목록에서 선택된 구속 위치에서 마우스 오른쪽 버튼으로 클릭하고 상황 메뉴에서 **참조 전환** 을 선택합니다.
3.  선택한 구속만 주도적 모드에서 참조 모드로 또는 그 반대로 변경되고 그에 따라 그들의 모습도 변합니다.
4.  치수 구속 생성 도구의 모드는 변경되지 않습니다.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/ko
