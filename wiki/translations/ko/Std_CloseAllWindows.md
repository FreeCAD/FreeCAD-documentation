---
- GuiCommand:
   Name:Std CloseAllWindows
   Name/ko:표준 모든 창 닫기
   MenuLocation:파일 - 모두 닫기
   Workbenches:모두
   SeeAlso:[표준 활성 창 닫기](Std_CloseActiveWindow.md)
---

# Std CloseAllWindows/ko

## 설명

**표준 모든 창 닫기(Std CloseAllWindow)** 명령은 모든 창을 닫습니다. 그 결과 모든 문서를 닫습니다.

## 용법

1.  메뉴에서 **파일 → <img src="images/Std_CloseAllWindows.svg" width=16px> 모두 닫기** 옵션을 선택합니다.
2.  저장하지 않은 문서가 있으면 저장할지 묻는 대화상자가 나타납니다:
    -   활성 문서를 저장하려면 **저장** 버튼을 누르십시오. 필요하다면 파일 이름을 먼저 입력하십시오.
    -   변경 내용을 모두 무시하고 문서를 닫으려면 **무시** 버튼을 누르십시오.

## 선택 사항 

-   대화 상자에서 명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.
-   저장하지 않은 문서가 여러 개일 때 각각의 문서에 대해 저장할지 묻는 대화상자가 나타나지 않게 하려면 {{CheckBox|TRUE|모든 문서에 적용}} 체크 상자를 선택합니다.

## 비고

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
![](images/Button_right.svg) [documentation index](../README.md) > Std CloseAllWindows/ko
