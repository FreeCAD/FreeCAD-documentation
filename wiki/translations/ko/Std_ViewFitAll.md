---
- GuiCommand   */ko
   Name   *Std ViewFitAll
   Name/ko   *표준 전체 보기
   MenuLocation   *보기 → 표준 보기 → 전체 보기
   Workbenches   *모두
   Shortcut   ***V** **F**
   SeeAlso   *[표준 선택 보기](Std_ViewFitSelection/ko.md)
---

# Std ViewFitAll/ko

## 설명


<div class="mw-translate-fuzzy">

**표준 전체 보기(Std ViewFitAll)** 명령은 숨기지 않은 개체가 모두 활성 [3D 보기에](3D_view/ko.md) 보이도록 카메라를 확대·축소 하거나 이동합니다.


</div>

## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다   *
    -   
        **<img src="images/Std_ViewFitAll.svg" width=16px> [표준 전체 보기](Std_ViewFitAll.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **보기 → 표준 보기 → <img src="images/Std_ViewFitAll.svg" width=16px> 전체 보기** 옵션을 선택합니다.

    -   [3D 보기의](3D_view.md) 상황에 맞는 메뉴에서 **<img src="images/Std_ViewFitAll.svg" width=16px> 전체 보기** 옵션을 선택합니다.

    -   단축키를 사용합니다   * **V** 다음 **F**.

## 비고


<div class="mw-translate-fuzzy">

-   [네비게이션 큐브의](Navigation_Cube/ko.md) 미니-큐브 메뉴를 이용하여 \'전체 보기\'로 맞출 수 있습니다.


</div>

## 스크립트


**참조   ***

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

3D 보기를 \'전체 보기\'로 변경하려면 ActiveView 객체의 `fitAll` 메소드를 사용하십시오. 이 메소드는 FreeCAD가 콘솔 모드일 때는 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.fitAll()
```

또는 FreeCADGui 객체의 `SendMsgToActiveView` 메소드를 사용할 수도 있습니다. 이 메소드는 FreeCAD가 콘솔 모드일 때는 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewFit')
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewFitAll/ko
