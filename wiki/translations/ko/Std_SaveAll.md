---
- GuiCommand:/ko
   Name:Std SaveAll
   Name/ko:표준 모두 저장
   MenuLocation:파일 → 모두 저장
   Workbenches:모두
   SeeAlso:[표준 저장](Std_Save.md)
---

## 설명

**표준 모두 저장(Std SaveAll)** 명령은 모든 문서를 저장합니다.

## 용법

1.  메뉴에서 **파일 → <img src="images/Std_SaveAll.svg" width=16px> 모두 저장** 옵션을 선택합니다.
2.  새로 만든 문서라면 대화 상자에서 파일 이름을 입력하고 **저장** 버튼을 누릅니다.

## 선택 사항 

-   새로 만든 문서인 경우 명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누르십시오.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서를 저장하려면 문서 객체의 `save` 메소드를 사용하십시오. 새 문서는 먼저 문서 객체의 `saveAs` 메소드를 이용하여 저장해야 합니다. 스크립트 예제는 [표준 새 파일을](Std_New/ko.md) 참조하십시오.





{{Std Base navi

}}  
