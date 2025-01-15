---
 GuiCommand:
   Name: Std Edit
   Name/ko: 표준 편집 모드 전환
   MenuLocation: 편집 , 편집 모드 전환
   Workbenches: 모두
---

# Std Edit/ko


</div>



## 설명

**표준 편집 모드 전환(Std Edit)** 명령은 개체의 편집모드를 활성화하거나 비활성화합니다.



## 용법


<div class="mw-translate-fuzzy">

1.  편집 모드인 개체가 없다면: 단일 개체를 선택합니다.
2.  메뉴에서 **편집 → <img src="images/Std_Edit.svg" width=16px> 편집 모드 전환** 옵션을 선택합니다.
3.  선택한 개체의 편집 모드가 활성화되거나 기존 편집 모드가 비활성화 됩니다.


</div>



## 비고


<div class="mw-translate-fuzzy">

-   개체의 편집 모드가 활성화되면 사용자 인터페이스의 일부 도구는 비활성화(회색으로 표시됨)됩니다.
-   모든 개체 유형에 편집 모드가 있는 것은 아닙니다.
-   편집 모드에서 사용할 수 있는 기능은 개체 유형마다 다릅니다.
-   [트리 보기에서](Tree_view/ko.md) 개체를 더블 클릭하여 편집모드를 활성화할 수도 있습니다.


</div>



## 스크립트


<div class="mw-translate-fuzzy">


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


</div>

개체의 편집 모드를 활성화 하려면 문서 객체의 `setEdit` 메소드를 사용하십시오. FreeCAD가 콘솔 모드일 때는 이 메소드를 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.setEdit("myObjectName",0)
```

The second argument is the EditMode. The following options are available:

0 = Default
1 = Transform
2 = Cutting
3 = Color

개체의 편집 모드를 비활성화 하려면 문서 객체의 `resetEdit` 메소드를 사용하십시오.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.resetEdit()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std Edit/ko
