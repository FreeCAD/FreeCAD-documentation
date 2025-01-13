---
 GuiCommand:
   Name: Std Delete
   Name/ko: 표준 삭제
   MenuLocation: 편집 , 삭제
   Workbenches: 모두
   Shortcut: **Del**
---

# Std Delete/ko



## 설명

**표준 삭제(Std Delete)** 명령은 선택한 개체를 삭제합니다.



## 용법

1.  하나 이상의 개체를 선택합니다..
2.  이 명령을 실행하는 방법은 여러 가지입니다:
    -   메뉴에서 **편집 → <img src="images/Std_Delete.svg" width=16px> 삭제** 옵션을 선택합니다.
    -   [트리 보기의](Tree_view/ko.md) 상황에 맞는 메뉴 혹은 [3D 보기의](3D_view/ko.md) 상황에 맞는 메뉴에서 **<img src="images/Std_Delete.svg" width=16px> 삭제** 옵션을 선택합니다.
    -   단축키를 사용합니다: **Del**.



## 스크립트


<div class="mw-translate-fuzzy">


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


</div>

개체를 삭제하려면 문서 객체의 `removeObject` 메소드를 사용하십시오.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Delete/ko
