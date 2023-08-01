---
- GuiCommand:
   Name: Std ViewFitSelection
   Name/ko: 표준 선택 보기
   MenuLocation: 보기 - 표준 보기 - 선택 보기
   Workbenches: 모두
   Shortcut: **V** **S**
   SeeAlso: [표준 전체 보기](Std_ViewFitAll/ko.md)
---

# Std ViewFitSelection/ko



## 설명


<div class="mw-translate-fuzzy">

**표준 선택 보기(Std ViewFitSelection)** 명령은 선택한 개체가 모두 활성 [3D 보기에](3D_view/ko.md) 보이도록 카메라를 확대·축소 하거나 이동합니다.


</div>



## 용법

1.  하나 이상의 개체를 선택합니다.
2.  이 명령을 실행하는 방법은 여러 가지 입니다:
    -   
        **<img src="images/Std_ViewFitSelection.svg" width=16px> [표준 선택 보기](Std_ViewFitSelection/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **보기 → 표준 보기 → <img src="images/Std_ViewFitSelection.svg" width=16px>선택 보기** 옵션을 선택합니다.

    -   [3D 보기의](3D_view/ko.md) 상황에 맞는 메뉴에서 **<img src="images/Std_ViewFitSelection.svg" width=16px> 선택 보기** 옵션을 선택합니다.

    -   단축키를 사용합니다: **V** 다음 **S**.



## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

3D 보기를 \'선택 보기\'로 변경하려면 FreeCADGui 객체의 `SendMsgToActiveView` 메소드를 사용할 수 있습니다. 이 메소드는 FreeCAD 콘솔 모드에서는 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.SendMsgToActiveView('ViewSelection')
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFitSelection/ko
