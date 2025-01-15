---
 GuiCommand:
   Name: Std Placement
   Name/ko: 표준 배치
   MenuLocation: 편집 , 위치 설정...
   Workbenches: 모두
   SeeAlso: Std_Alignment/ko, Tasks_Placement/ko, Placement/ko
---

# Std Placement/ko


</div>



## 설명

**표준 배치(Std Placement)** 명령은 선택한 개체의 배치 [작업 패널을](Task_panel/ko.md) 표시합니다.

![](images/Std_Placement_taskpanel.png ) 
*배치 작업 패널*



## 용법


<div class="mw-translate-fuzzy">

1.  [속성 편집기에](Property_editor/ko.md) **Placement** 속성이 있는 단일 개체를 선택합니다.
2.  메뉴에서 **편집 → 배치...** 옵션을 선택합니다.
3.  이동 과 회전 파라미터를 변경합니다.
4.  다음 중 하나를 수행합니다:
    -   변경 사항을 적용하고 작업 패널을 닫으려면 **확인** 버튼을 누르십시오.
    -   변경 사항을 적용하되 추가 변경을 위해 작업 패널을 열어두려면 **적용** 버튼을 누르십시오.
5.  작업을 중지하려면 **Esc** 키나 **취소** 버튼을 누르십시오. 적용하지 않은 변경 사항은 모두 실행 취소됩니다.


</div>


<div class="mw-translate-fuzzy">

이 대화 상자는 [속성 편집기의](Property_editor/ko.md) **Placement** 속성을 클릭했을 때 바로 옆에 나오는 생략 부호 버튼 **...**을 눌러 열 수도 있습니다.


</div>



## 비고


<div class="mw-translate-fuzzy">

-   배치 파라미터에 대한 자세한 내용은 [배치 작업과](Tasks_Placement/ko.md) [배치](Placement/ko.md) 페이지 그리고 [비행기](Aeroplane/ko.md) 자습서를 참조하십시오.


</div>



## 스크립트


<div class="mw-translate-fuzzy">


**참조:**

[FreeCAD 스크립트 기초](FreeCAD_Scripting_Basics/ko.md).


</div>

[파이썬 스크립트 자습서를](Python_scripting_tutorial/ko#벡터_및_배치.md) 참조하십시오.

배치는 내부적으로 매트릭스로 정의됩니다. 대부분의 경우 `Base` 점(벡터)과 `Rotation` 값 이라는 두 가지 구성 요소를 사용하여 표현하면 더 간단합니다. `Rotation` 자체는 다른 표현법이 있습니다. \"[사원수(quaternion)](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`로 완전히 정의할 수 있지만 회전 `Axis` (유닛 벡터) 및 회전 `Angle` (라디안)으로 기술할 수도 있습니다.


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

개체의 기준점을 이동한 다음 X 축을 중심으로 개체를 45도 회전합니다.

The math module supplies a method `radians()` to easily convert degrees to radians and has to be imported at first.


```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Std Placement/ko
