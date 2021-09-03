---
- GuiCommand:/ko
   Name:Std Quit
   Name/ko:표준 종료
   MenuLocation:파일 → 종료
   Workbenches:모두
   Shortcut:**Alt**+**F4**
   SeeAlso:[표준 닫기](Std_CloseActiveWindow/ko.md)
---

## 설명

**표준 닫기(Std Quit)** 명령은 FreeCAD 애플리케이션을 닫고 필요한 경우 저장하지 않은 문서를 저장합니다.

## 용법

1.  이 명령어를 실행하는 방법은 여러가지입니다:
    -   메뉴에서 **파일 → <img src="images/Std_Quit.svg" width=16px> 종료** 옵션을 선택합니다.
    -   단축키를 사용합니다: **Alt**+**F4**.
2.  저장하지 않은 문서가 있다면 저장할지 묻는 대화 상자가 나타납니다:
    -   활성 문서를 저장하려면 **저장** 버튼을 누르십시오. 필요하다면 파일 이름을 입력하십시오.
    -   변경 내용을 모두 무시하고 활성 문서를 닫으려면 **무시** 버튼을 누릅니다.

## 선택 사항 

-   저장하지 않은 문서가 여러 개일 때: 저장하지 않은 문서 각각에 대해서 저장할지 묻는 대화 상자가 나타나지 않게 하려면 {{CheckBox|TRUE|모든 문서에 적용}} 체크 상자를 선택합니다.
-   저장하지 않은 문서가 있을 때: 명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.





{{Std Base navi

}}  
