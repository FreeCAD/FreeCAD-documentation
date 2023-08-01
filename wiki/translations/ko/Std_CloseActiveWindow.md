---
- GuiCommand:/ko
   Name:Std CloseActiveWindow
   Name/ko:표준 활성 창 닫기
   MenuLocation:파일 → 닫기
   Workbenches:모두
   Shortcut:**Ctrl**+**F4**
   SeeAlso:[표준 모든 창 닫기](Std_CloseAllWindows/ko.md)
---

# Std CloseActiveWindow/ko

## 설명

**표준 활성 창 닫기(Std CloseActiveWindow)** 명령은 활성 창을 닫습니다. 문서를 닫으려면 그 문서에 속한 창을 모두 닫아야 합니다.

## 용법

1.  이 명령을 실행하는 방법은 여러가지입니다:
    -   메뉴에서 **파일 → <img src="images/Std_CloseActiveWindow.svg" width=16px> 닫기** 옵션을 선택합니다.
    -   단축키를 사용합니다: **Ctrl**+**F4**.
2.  문서를 닫으려면 그 문서에 속한 모든 창에 이 작업을 반복합니다.
3.  저장하지 않은 문서의 마지막 창을 닫을 때 저장할지 묻는 대화상자가 나타납니다:
    -   문서를 저장하려면 **저장** 버튼을 누르십시오. 필요하다면 먼저 파일 이름을 입력하십시오.
    -   변경 내용을 모두 무시하고 문서를 닫으려면 **무시** 버튼을 누르십시오.

## 선택 사항 

-   대화 상자에서 명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 비고

-   이 명령어는 [고정된](Std_ViewDockUndockFullscreen.md) 창만 닫을 수 있습니다.
-   [트리 보기에서](Tree_view/ko.md) 문서를 오른쪽 클릭하면 나오는 메뉴에서 **문서 닫기**를 선택하여 해당 문서를 닫을 수도 있습니다.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서를 닫으려면 FreeCAD 애플리케이션의 `closeDocument` 메소드를 사용하십시오. 스크립트 예제는 [표준 새 파일을](Std_New/ko.md) 참조하십시오.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std CloseActiveWindow/ko
