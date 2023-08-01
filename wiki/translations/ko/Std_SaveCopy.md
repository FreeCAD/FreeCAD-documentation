---
- GuiCommand:
   Name: Std SaveCopy
   Name/ko: 표준 사본 저장
   MenuLocation: 파일 - 사본 저장...
   Workbenches: 모두
   SeeAlso: [표준 다른 이름으로 저장](Std_SaveAs/ko.md), [표준 저장](Std_Save/ko.md)
---

# Std SaveCopy/ko

## 설명

**표준 사본 저장(Std SaveAs)** 명령은 활성 문서의 사본을 새 파일 이름으로 저장합니다.

## 용법

1.  메뉴에서 **파일 → <img src="images/Std_SaveCopy.svg" width=16px> 사본 저장...** 옵션을 선택합니다.

2.  대화 상자에서 파일 이름을 입력합니다.

3.  
    **저장**버튼을 클릭합니다.

## 선택 사항 

-   명령을 중지하려면 **Esc** 키나 **취소** 버튼을 누릅니다.

## 환경 설정 

-   마지막으로 사용한 파일의 위치가 다음에 저장됩니다: **도구 → 파라미터 편집... → BaseApp → Preferences → General → FileOpenSavePath**.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

문서의 사본을 저장하려면 문서 객체의 `saveCopy` 메소드를 사용하십시오.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SaveCopy/ko
