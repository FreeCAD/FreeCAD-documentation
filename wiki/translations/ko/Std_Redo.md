---
 GuiCommand:
   Name: Std Redo
   Name/ko: 표준 다시 실행
   MenuLocation: 편집 , 다시 실행
   Workbenches: 모두
   Shortcut: **Ctrl**+**Y**
   SeeAlso: Std_Undo/ko
---

# Std Redo/ko

## 설명

**표준 다시 실행(Std Redo)** 명령은 [표준 실행 취소](Std_Undo/ko.md) 명령을 되돌립니다.

## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다:
    -   
        **<img src="images/Std_Redo.svg" width=16px> [표준 다시 실행](Std_Redo/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **편집 → <img src="images/Std_Redo.svg" width=16px> 다시 실행** 옵션을 선택합니다.

    -   단축키를 사용합니다: **Ctrl**+**Y**.

## 선택 사항 

-   여러 작업을 다시 실행하려면 **<img src="images/Std_Redo.svg" width=16px> [표준 다시 실행](Std_Redo/ko.md)** 버튼 오른쪽의 검은색 역삼각형을 클릭한 뒤 목록에서 선택합니다.

## 환경 설정 

-   실행 취소/다시 실행 기능은 **도구 → 파라미터 편집... → BaseApp → Preferences → Document → UsingUndo**를 `False`로 설정하여 비활성화할 수 있지만 권장하지 않습니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.
-   실행 취소/다시 실행의 최대 횟수는 **도구 → 파라미터 편집... → BaseApp → Preferences → Document → MaxUndoSize**로 조절합니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

실행 취소한 작업을 다시 실행하려면 문서 객체의 `redo` 메소드를 사용합니다.


```python
import FreeCAD

FreeCAD.ActiveDocument.redo()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Redo/ko
