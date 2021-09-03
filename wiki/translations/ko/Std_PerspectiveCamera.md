---
- GuiCommand:/ko
   Name:Std PerspectiveCamera
   Name/ko:표준 원근투영 카메라
   MenuLocation:보기 → 원근투영
   Workbenches:모두
   Shortcut:**V** **P**
   SeeAlso:[표준 직교투영 카메라](Std_OrthographicCamera/ko.md)
---

## 설명

**표준 원근투영 카메라(Std PerspectiveCamera)** 명령은 활성 [3D 보기의](3D_view/ko.md) 카메라를 원근투영 보기 모드로 전환합니다. 이 모드에서는 카메라에서 먼 개체가 가까운 개체보다 더 작게 보입니다.

![](images/Std_PerspectiveCamera_example.svg ) *원근 투영 보기에서 크기가 같은 두 육면체*

## 용법

1.  이 명령을 실행하는 방법은 여러 가지입니다:
    -   메뉴에서 {{MenuCommand|보기 → <img src="images/Std_PerspectiveCamera.svg" width=16px> 원근투영}} 옵션을 선택합니다.
    -   단축키를 사용합니다: **V** 를 누른 다음 **P**.

## 비고

-   [네비게이션 큐브의](Navigation_Cube/ko.md) 미니-큐브 메뉴를 이용하여 원근투영 보기 모드로 변경할 수도 있습니다.

## 환경 설정 {#환경_설정}

-   카메라 유형은 환경 설정에서 변경할 수 있습니다: {{MenuCommand|편집 → 환경설정... → Display → 3D 보기 → 카메라 유형}}. 선택한 유형은 모든 열린 문서 및 새로 열리는 문서의 3D 보기에 적용됩니다. [환경 설정 편집기를](Preferences_Editor/ko#3D_보기.md) 참조하십시오.

## 스크립트


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).

3D 보기를 원근투영으로 변경하려면 ActiveView 객체의 `setCameraType` 메소드를 사용하십시오. FreeCAD가 콘솔 모드인 경우 이 메소드는 사용할 수 없습니다.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.setCameraType('Perspective')
FreeCADGui.ActiveDocument.ActiveView.getCameraType()
```





{{Std Base navi

}}  
