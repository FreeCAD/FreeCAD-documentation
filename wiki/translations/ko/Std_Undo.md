---
 GuiCommand:
   Name: Std Undo
   Name/ko: 표준 실행 취소
   MenuLocation: 편집 , 실행 취소
   Workbenches: 모두
   Shortcut: **Ctrl**+**Z**
   SeeAlso: Std_Redo/ko
---

# Std Undo/ko



## 설명

**표준 실행 취소(Std Undo)** 명령은 마지막 작업을 실행 취소합니다.



## 용법


<div class="mw-translate-fuzzy">

1.  이 명령을 실행하는 방법은 여러가지입니다.:
    -   
        **<img src="images/Std_Undo.svg" width=16px> [표준 실행 취소](Std_Undo/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **편집 → <img src="images/Std_Undo.svg" width=16px> 실행 취소** 옵션을 선택합니다..

    -   단축키를 사용합니다: **Ctrl**+**Z**.


</div>



## 선택 사항 


<div class="mw-translate-fuzzy">

-   여러 작업을 실행 취소하려면 **<img src="images/Std_Undo.svg" width=16px> [표준 실행 취소](Std_Undo/ko.md)** 버튼 오른쪽의 검은색 역삼각형을 클릭한 뒤 목록에서 선택합니다.


</div>



## 환경 설정 

See also: [Preferences Editor](Preferences_Editor.md).


<div class="mw-translate-fuzzy">

-   실행 취소/다시 실행 기능은 **도구 → 파라미터 편집... → BaseApp → Preferences → Document → UsingUndo**를 `False`로 설정하여 비활성화할 수 있지만 권장하지 않습니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.
-   실행 취소/다시 실행의 최대 횟수는 **도구 → 파라미터 편집... → BaseApp → Preferences → Document → MaxUndoSize**로 조절합니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.


</div>



## 스크립트


<div class="mw-translate-fuzzy">


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


</div>


<div class="mw-translate-fuzzy">

마지막 작업을 실행 취소하려면 문서 객체의 `undo` 메소드를 사용합니다.


</div>


```python
import FreeCAD

FreeCAD.ActiveDocument.undo()
```

When running FreeCAD in pure console mode (CLI), the undo/redo mechanism isn\'t enabled by default. It must be explicitly activated for each document.


```python
import FreeCAD

FreeCAD.ActiveDocument.UndoMode = 1
```



---
⏵ [documentation index](../README.md) > Std Undo/ko
