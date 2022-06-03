---
- GuiCommand   */ko
   Name   *Std ViewIsometric
   Name/ko   *표준 등각투영
   MenuLocation   *보기 → 표준 보기 → Axonometric → Isometric
   Workbenches   *모두
   Shortcut   ***0**
   SeeAlso   *[표준 등각투영](Std_ViewDimetric/ko.md), [표준 삼각투영](Std_ViewTrimetric/ko.md)
---

# Std ViewIsometric/ko

## 설명

**표준 등각투영(Std ViewIsometric)** 명령은 [3D 보기의](3D_view/ko.md) 카메라를 재조정하여 등각투영([isometric](https   *//en.wikipedia.org/wiki/Isometric_projection)) 보기 각도로 전환합니다. 진정한 등각투영(isometric) 보기를 하려면 3D 보기가 [직교투영(orthographic) 모드이어야](Std_OrthographicCamera/ko.md) 하지만 이 명령은 [원근투영(perspective) 모드일](Std_PerspectiveCamera/ko.md) 때도 작동합니다.

![](images/Std_ViewIsometric_example.svg ) 
*등각투영(isometric) 일 때 [좌표축](Std_AxisCross/ko.md)과 육면체*

## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다   *
    -   
        **<img src="images/Std_ViewIsometric.svg" width=16px> [표준 등각투영](Std_ViewIsometric/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **보기 → 표준 보기 → Axonometric → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** 옵션을 선택합니다.

    -   [3D 보기의](3D_view/ko.md) 상황에 맞는 메뉴에서 **표준 보기 → <img src="images/Std_ViewIsometric.svg" width=16px> Isometric** 옵션을 선택합니다.

    -   단축키를 사용합니다   * **0**.

## 비고

-   [네비게이션 큐브의](Navigation_Cube/ko.md) 미니-큐브 메뉴를 이용하여 등각투영(isometric) 각도로 변경할 수도 있습니다.

## 스크립트


**참조   ***

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

등각투영(isometric) 보기로 변경하려면 ActiveView 객체의 `viewIsometric` 메소드를 사용하십시오. 이 메소드는 FreeCAD가 콘솔 모드일 때는 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewIsometric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewIsometric/ko
