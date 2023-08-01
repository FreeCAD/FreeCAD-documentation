---
- GuiCommand:
   Name:Std MergeProjects
   Name/ko:표준 프로젝트 병합
   MenuLocation:파일 - 프로젝트 병합...
   Workbenches:모두
---

# Std MergeProjects/ko



## 설명

**표준 프로젝트 병합(Std MergeProjects)** 명령은 FreeCAD 파일의 내용을 활성 문서에 추가합니다.



## 용법

1.  메뉴에서 **파일 → <img src="images/Std_MergeProjects.svg" width=16px> 프로젝트 병합...** 옵션을 선택합니다.

2.  대화 상자에서 FreeCAD 파일을 선택합니다.

3.  
    **열기**버튼을 누릅니다.



## 선택 사항 

-   명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.



## 비고

-   프로젝트는 자신과 병합할 수 없으며 현재 파일을 선택할 수 없습니다.
-   FreeCAD는 이름 충돌을 피하기 위해 환경 설정에 따라 개체의 내부 이름과 레이블을 자동으로 변경합니다.



## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

-    **도구 → 파라미터 편집... → BaseApp → Preferences → Document → DuplicateLabels**가 `True`면 중복 레이블이 허용됩니다. 이 설정은 [환경 설정 편집기에서도](Preferences_Editor#문서.md) 변경할 수 있습니다.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To merge a project use the {{Incode|mergeProject}} method of the document object.


```python
import FreeCAD

FreeCAD.ActiveDocument.mergeProject("Path_to_FCStd_project_file")
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std MergeProjects/ko
