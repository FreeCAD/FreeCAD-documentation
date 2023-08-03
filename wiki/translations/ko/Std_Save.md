---
 GuiCommand:
   Name: Std Save
   Name/ko: 표준 저장
   MenuLocation: 파일 , 저장
   Workbenches: 모두
   Shortcut: **Ctrl**+**S**
   SeeAlso: Std_SaveAs/ko, Std_SaveCopy/ko, Std_SaveAll/ko
---

# Std Save/ko

## 설명

**표준 저장(Std Save)** 명령은 활성 문서를 저장합니다.

## 용법

1.  이 명령어를 실행하는 방법은 여러가지입니다:
    -   
        **<img src="images/Std_Save.svg" width=16px> [표준 저장](Std_Save/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **파일 → <img src="images/Std_Save.svg" width=16px> 저장** 옵션을 선택합니다.

    -   단축키를 사용합니다: **Ctrl**+**S**.
2.  새로 만든 문서라면 대화 상자에서 파일 이름을 입력하고 **저장** 버튼을 누릅니다.

## 선택 사항 

-   새로 만든 문서인 경우 명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누르십시오.

## 비고

-   이 명령어는 의존성 그래프를 저장하려고 사용할 수도 있습니다. [표준 의존성 그래프를](Std_DependencyGraph/ko.md) 참조하십시오.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서를 저장하려면 문서 객체의 `save` 메소드를 사용하십시오. 새 문서는 먼저 문서 객체의 `saveAs` 메소드를 이용하여 저장해야 합니다. 스크립트 예제는 [표준 새 파일을](Std_New/ko.md) 참조하십시오.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Save/ko
