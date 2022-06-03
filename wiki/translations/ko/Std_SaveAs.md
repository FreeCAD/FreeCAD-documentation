---
- GuiCommand   */ko
   Name   *Std SaveAs
   Name/ko   *표준 다른 이름으로 저장
   MenuLocation   *파일 → 다른 이름으로 저장...
   Workbenches   *모두
   SeeAlso   *[표준 사본 저장](Std_SaveCopy/ko.md), [표준 저장](Std_Save/ko.md)
---

# Std SaveAs/ko

## 설명

**표준 다른 이름으로 저장(Std SaveAs)** 명령은 활성 문서를 새 파일 이름으로 저장합니다.

## 용법

1.  메뉴에서 **파일 → <img src="images/Std_SaveAs.svg" width=16px> 다른 이름으로 저장...** 옵션을 선택합니다.

2.  대화 상자에서 파일 이름을 입력합니다.

3.  
    **저장**버튼을 클릭합니다.

## 선택 사항 

-   명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 비고

-   이 명령어는 의존성 그래프를 저장하려고 사용할 수도 있습니다. [표준 의존성 그래프를](Std_DependencyGraph/ko.md) 참조하십시오.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다   * **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조   ***

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서를 새 이름으로 저장하려면 문서 객체의 `saveAs` 메소드를 사용하십시오. 스크립트 예제는 [표준 새 파일을](Std_New/ko.md) 참조하십시오.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveAs/ko
