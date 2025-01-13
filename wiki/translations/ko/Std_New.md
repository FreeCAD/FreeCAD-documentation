---
 GuiCommand:
   Name: Std New
   Name/ko: 표준 새 파일
   MenuLocation: 파일 , 새 파일
   Workbenches: 모두
   Shortcut: **Ctrl**+**N**
   SeeAlso: Std_Open/ko, Std_Import
---

# Std New/ko



## 설명

**표준 새 파일(Std New)** 명령은 빈 새 문서를 만들고 활성화 시킵니다.



## 용법


<div class="mw-translate-fuzzy">

1.  이 명령을 실행하는 방법은 여러 가지입니다.
    -   
        **<img src="images/Std_New.svg" width=16px> [표준 새 파일](Std_New/ko.md)
**
        
        버튼을 누릅니다.

    -   메뉴에서 **파일 → <img src="images/Std_New.svg" width=16px> 새 파일** 옵션을 선택합니다.

    -   단축키를 사용합니다: **Ctrl**+**N**.


</div>



## 환경 설정 

See also: [Preferences Editor](Preferences_Editor.md).


<div class="mw-translate-fuzzy">

-    **Tools → Edit parameters... → BaseApp → Preferences → Document → CreateNewDoc**를 `True`로 설정한 경우 FreeCAD를 시작할 때 새 문서가 생성됩니다. 이 설정은 [환경설정 편집기에서도](Preferences_Editor/ko#문서.md) 변경할 수 있습니다.

-   작성자 이름, 회사 이름, 라이센스 정보와 같은 일부 문서 속성은 [환경설정 편집기에서](Preferences_Editor/ko#문서.md) 미리 설정할 수 있습니다.


</div>



## 속성

See also: [Property editor](Property_editor.md).

속성은 대부분 [표준 프로젝트 정보](Std_ProjectInfo/ko.md) 명령의 대화 상자에서도 변경할 수 있습니다.

### Data


{{TitleProperty|Base}}


<div class="mw-translate-fuzzy">

-    **Comment**: 적용할 수 있는 모든 설명

-    **Company**: 회사 이름. **미리 설정 가능**.

-    **Created By**: 작성자 이름. **미리 설정 가능**.

-    **Creation Date**: 자동 날짜 스탬프. **편집 불가능**.

-    **File Name**: 파일의 전체 경로. 문서 저장 전에는 비어 있음. **편집 불가능**.

-    **Id**: 미구현.

-    **Label**: [트리 보기에](Tree_view/ko.md) 표시될 이름. 기본적으로는 문서 이름.

-    **Last Modified By**: 최종 수정자 이름. **미리 설정 가능**.

-    **Last Modified Date**: 최종 수정일 자동 날짜 스탬프. **편집 불가능**.

-    **License**: 라이센스 형식. **미리 설정 가능**.

-    **License URL**: 라이센스 URL. **미리 설정 가능**.

-    **Show Hidden**: {{true}}면 [트리 보기에서](Tree_view/ko.md) 숨긴 항목도 표시됨. 트리에서 항목을 숨기는 기능은 큰 모델 작업을 할 때 유용합니다.

-    **Tip**: 미구현.

-    **Tip Name**: 미구현.

-    **Transient Dir**: 복구 데이터를 위한 임시 디렉토리. **편집 불가능**.


</div>



## 스크립트


<div class="mw-translate-fuzzy">


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


</div>


<div class="mw-translate-fuzzy">

새 문서를 만들려면 FreeCAD 애플리케이션의 `newDocument` 메소드를 사용하십시오.


</div>


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std New/ko
