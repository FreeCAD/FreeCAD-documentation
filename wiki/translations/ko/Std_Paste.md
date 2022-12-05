---
- GuiCommand:/ko
   Name:Std Paste
   Name/ko:표준 붙여넣기
   MenuLocation:편집 → 붙여넣기
   Workbenches:모두
   Shortcut:**Ctrl**+**V**
   SeeAlso:[표준 잘라내기](Std_Cut/ko.md), [표준 복사](Std_Copy/ko.md), [표준 개체 복제](Std_DuplicateSelection/ko.md)
---

# Std Paste/ko

## 설명

**표준 붙여넣기(Std Paste)** 명령은 클립보드의 개체를 활성 문서에 붙여 넣습니다.

## 용법


<div class="mw-translate-fuzzy">

1.  이 명령을 실행하는 방법은 여러가지입니다:
    -   
        **<img src="images/Std_Paste.svg" width=16px> [표준 붙여넣기](Std_Paste/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **편집 → <img src="images/Std_Paste.svg" width=16px> 붙여넣기** 옵션을 선택합니다.

    -   [트리 보기의](Tree_view/ko.md) 상황에 맞는 메뉴에서 **<img src="images/Std_Paste.svg" width=16px> 붙여넣기** 옵션을 선택합니다. 이 옵션은 기존에 선택한 개체가 있을 때에만 사용할 수 있습니다.

    -   단축키를 사용합니다: **Ctrl**+**V**.


</div>

## 비고

-   FreeCAD는 이름 충돌을 피하기 위해 환경 설정 값에 따라 개체의 내부 이름과 레이블을 자동으로 변경합니다.
-   스프레드시트에 이미 존재하는 스프레드시트 셀 별명은 붙여 넣지 않습니다.
-   FreeCAD 텍스트 창, 입력 박스 또는 스프레드시트에서 작업할 때 표준 단축키 **Ctrl**+**V**는 대부분의 경우 **표준 붙여넣기(Std Paste)** 명령을 호출하는 대신 OS의 붙여넣기(Paste) 기능을 사용합니다.
-   FreeCAD와 다른 응용 프로그램간에 기본 개체를 복사, 붙여넣기 할 수 없습니다.

## 환경 설정 

-    **도구 → 파라미터 편집... → BaseApp → Preferences → Document → DuplicateLabels**값이 `True`면 중복 레이블이 허용됩니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Paste/ko
