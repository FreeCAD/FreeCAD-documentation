---
- GuiCommand:
   Name: Std DuplicateSelection
   Name/ko: 표준 개체 복제
   MenuLocation: 편집 -> 개체 복제
   Workbenches: 모두
   SeeAlso: Std_Cut/ko, Std_Copy/ko, Std_Paste/ko
---

# Std DuplicateSelection/ko


</div>

## 설명

**표준 개체 복제(Std DuplicateSelection)** 명령은 활성 문서의 개체를 복제합니다.

## 용법


<div class="mw-translate-fuzzy">

1.  하나 이상의 개체를 선택합니다..
2.  메뉴에서 **편집 → 개체 복제** 옵션을 선택합니다.
3.  개체에 선택하지 않은 의존성이 있는 경우 포함 할 항목을 지정하라는 대화 상자가 나타납니다.


</div>

## 비고

-   FreeCAD는 이름 충돌을 피하기 위해 환경 설정 값에 따라 개체의 내부 이름과 레이블을 자동으로 변경합니다.

## 환경 설정 

-    **도구 → 파라미터 편집... → BaseApp → Preferences → Document → DuplicateLabels**값이 `True`면 중복 레이블이 허용됩니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std DuplicateSelection/ko
