---
- GuiCommand:
   Name: Std Refresh
   Name/ko: 표준 새로 고침
   MenuLocation: 편집 -> 새로 고침
   Workbenches: 모두
   Shortcut: **F5**
---

# Std Refresh/ko



## 설명

**표준 새로 고침(Std Refresh)** 명령은 활성 문서를 다시 계산합니다. 문서를 다시 계산할 필요가 없으면 이 명령은 비활성화됩니다.



## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다:
    -   
        **<img src="images/Std_Refresh.svg" width=16px> [표준 다시 계산](Std_Refresh/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **편집 → <img src="images/Std_Refresh.svg" width=16px> 새로 고침** 옵션을 선택합니다.

    -   단축키를 사용합니다: **F5**.



## 선택 사항 


<div class="mw-translate-fuzzy">

-   다시 계산이 강제로 이루어지게 하려면 [트리 보기에서](Tree_view/ko.md) 문서나 하나 이상의 개체를 선택한 뒤 상황에 맞는 메뉴에서 **다시 계산 필요** 옵션을 선택하여 명령을 실행합니다.
-   문서가 아닌 객체의 경우 상황에 맞는 메뉴에서 **개체 다시 계산** 옵션을 선택할 수도 있습니다({{Version/ko|0.19}}).


</div>



## 비고

-   활성 문서를 다시 계산하는 매크로는 다음을 참조하십시오: [Macro ForceRecompute](Macro_ForceRecompute.md).



## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서를 다시 계산하려면 문서 객체의 `recompute` 메소드를 사용하십시오.


```python
import FreeCAD

doc = FreeCAD.newDocument()
doc.recompute()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Refresh/ko
