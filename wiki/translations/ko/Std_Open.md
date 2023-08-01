---
- GuiCommand:
   Name:Std Open
   Name/ko:표준 열기
   MenuLocation:파일 - 열기...
   Workbenches:모두
   Shortcut:**Ctrl**+**O**
   SeeAlso:[표준 가져오기](Std_Import/ko.md), [표준 새 파일](Std_New/ko.md)
---

# Std Open/ko

## 설명

**표준 열기(Std Open)** 명령은 파일을 엽니다. 만약 열려는 파일이 FreeCAD 고유 파일(\*.FCStd)이 아니라면 파일의 지오메트리를 새 문서로 가져옵니다. 자세한 내용은 [표준 가져오기를](Std_Import/ko.md) 참조하십시오.

## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다.
    -   
        **<img src="images/Std_Open.svg" width=16px> [표준 열기](Std_Open/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **파일 → <img src="images/Std_Open.svg" width=16px> 열기...** 옵션을 선택합니다.

    -   단축키를 사용합니다: **Ctrl**+**O**.

2.  필요하다면 알맞는 파일 형식을 대화상자에서 선택합니다.

3.  파일을 선택합니다.

4.  
    **열기**버튼을 누릅니다.

## 선택 사항 

-   명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


<div class="mw-translate-fuzzy">

문서를 열려면 FreeCAD 애플리케이션의 `open` 메소드를 사용하십시오. 스크립트 예제는 [표준 새 파일을](Std_New/ko.md) 참조하십시오.


</div>

These methods create and return a document and load a project file into it. The `filepath` argument must be a string pointing to an existing file. If the file doesn\'t exist or the file cannot be loaded an I/O exception is thrown. In this case the created document is kept, but will be empty. If `hidden<nowiki>=</nowiki>True` is used, the document won\'t be displayed in the GUI and no tab will appear for it. This allows performing automatic operations on a document and closing it without disrupting the user interface.

For a scripting example see [Std New](Std_New#Scripting.md).





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Open/ko
