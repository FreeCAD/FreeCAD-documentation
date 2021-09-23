---
- GuiCommand:/ko
   Name:Std SendToPythonConsole
   Name/ko:표준 파이썬 콘솔로 보내기
   MenuLocation:편집 → 파이썬 콘솔로 보내기
   Workbenches:모두
   Shortcut:**Ctrl**+**Shift**+**P**
   Version:0.19
---

# Std SendToPythonConsole/ko

## 설명

**표준 파이썬 콘솔로 보내기(Std SendToPythonConsole)** 명령은 선택한 개체를 참조하는 변수를 [파이썬 콘솔](Python_console/ko.md) 안에 생성합니다. 만약 개체의 하위 셰이프를 선택했다면 변수 2개가 더 생성됩니다. 하나는 개체의 셰이프를 참조하고 다른 하나는 하위 셰이프 자체를 참조합니다. 관련 변수와 코드는 파이썬 코드를 작성하는데 사용할 수 있습니다.

>>> ### Begin command Std_SendToPythonConsole
>>> obj = App.getDocument("Unnamed").getObject("Box")
>>> shp = App.getDocument("Unnamed").getObject("Box").Shape
>>> elt = App.getDocument("Unnamed").getObject("Box").Shape.Edge8
>>> ### End command Std_SendToPythonConsole


*출력 예시: [부품 상자](Part_Box/ko.md)의 모서리가 선택된 경우*

## 용법

1.  단일 개체를 선택합니다.
2.  이 명령을 실행하는 방법은 여러 가지입니다:
    -   메뉴에서 **편집 → <img src="images/Std_SendToPythonConsole.svg" width=16px> 파이썬 콘솔로 보내기** 옵션을 선택합니다.
    -   [트리 보기의](Tree_view/ko.md) 상황에 맞는 메뉴 혹은 [3D 보기의](3D_view/ko.md) 상황에 맞는 메뉴에서 **<img src="images/Std_SendToPythonConsole.svg" width=16px> 파이썬 콘솔로 보내기** 옵션을 선택합니다.
    -   단축키를 사용합니다: **Ctrl**+**Shift**+**P**.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std SendToPythonConsole/ko
