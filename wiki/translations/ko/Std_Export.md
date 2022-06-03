---
- GuiCommand   */ko
   Name   *Std Export
   Name/ko   *표준 내보내기
   MenuLocation   *파일 → 내보내기...
   Workbenches   *모두
   Shortcut   ***Ctrl**+**E**
   SeeAlso   *[Std PrintPdf](Std_PrintPdf.md), [Import Export](Import_Export.md), [Import Export Preferences](Import_Export_Preferences.md)
---

# Std Export/ko

## 설명

**표준 내보내기(Std Export)** 명령은 선택한 개체를 다른 형식의 파일로 내보냅니다. 다양한 파일 형식이 지원되며 어떤 형식에는 내보내기 옵션이 여러 가지 존재합니다. 자세한 내용은 [가져오기 내보내기를](Import_Export/ko.md) 참조하십시오.

## 용법

1.  하나 이상의 개체를 선택합니다. 안 보이는 개체 또는 중복된 개체가 내보내기 되는 것을 피하려면 다음을 주의하십시오   *
    -   모든 개체를 선택하려고 **Ctrl**+**A**를 사용할 때 주의하십시오. 이 단축키는 안 보이는 개체도 선택할 수 있습니다.
    -   바디 자체 또는 마지막 피처만 선택하여 [부품 설계 바디를](PartDesign_Body/ko.md) 선택하십시오.
    -   상위 개체 자체 또는 내부에 중첩된 개체만을 선택하여 [표준 그룹](Std_Group/ko.md) 또는 [표준 부품을](Std_Part/ko.md) 선택하십시오.
    -   [표준 모두 선택](Std_SelectAll/ko.md) 명령은 부품 설계 바디의 하위 요소도 선택하므로 사용하지 마십시오.
    -   같은 이유로 FreeCAD 0.18 이전 버전에서는 [개체 선택](Std_BoxSelection/ko.md) 명령을 사용하지 말아야 합니다.

2.  이 명령을 실행하는 방법은 여러가지입니다   *
    -   메뉴에서 **파일 → <img src="images/Std_Export.svg" width=16px> 내보내기...** 옵션을 선택합니다.
    -   단축키를 사용합니다   * **Ctrl**+**E**.

3.  대화 상자에서 알맞는 파일 형식을 선택합니다.

4.  파일 이름을 입력합니다.

5.  
    **저장**버튼을 누릅니다.

## 선택 사항 

-   명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 비고

-   [메시 개체를](Mesh_Workbench/ko.md) 솔리드 파일 형식으로 내보내기 하려면 먼저 변환해야 합니다. [STL이나 OBJ 가져오기](Import_from_STL_or_OBJ.md) 자습서를 참조하십시오.
-   일부 작업대에는 추가적인 내보내기 명령어가 있습니다. 참조   * [가져오기 내보내기](Import_Export/ko.md).

## 환경 설정 

-   참조   * [가져오기 내보내기 환경설정](Import_Export_Preferences/ko.md).
-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다   * **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.
-   마지막으로 가져온 파일의 위치가 다음에 저장됩니다   * **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileExportFilter**.





{{Std Base navi

}}  

[Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Std Export/ko
