# Python/ko
## 설명

[파이썬(Python)](https://www.python.org)은 스크립트나 [매크로를](macros/ko.md) 생성하여 일부 작업을 자동화하는 대규모 애플리케이션에서 매우 일반적으로 사용되는 범용 고급 프로그래밍 언어입니다.

FreeCAD에서는 파이썬 코드를 사용하면 그래픽 사용자 인터페이스를 클릭하지 않고도 다양한 요소를 프로그래밍 방식으로 만들 수 있습니다. 게다가, FreeCAD의 많은 도구와 작업대는 파이썬으로 프로그래밍되어 있습니다.

파이썬 프로그래밍 언어에 대해 알아보려면 [파이썬 소개를](Introduction_to_Python/ko.md) 참조하세요.그런 다음 [파이썬 스크립팅 자습서와](Python_scripting_tutorial/ko.md) [FreeCAD 스크립팅 기초를](FreeCAD_Scripting_Basics/ko.md) 참조하여 FreeCAD에서 스크립팅을 시작하세요.



## 가독성

파이썬 코드의 가독성은 이 언어의 가장 중요한 측면 중 하나입니다. 파이썬 커뮤니티에서 명확하고 일관된 스타일을 사용하면 다양한 개발자의 기여가 용이해집니다. 대부분의 숙련된 파이썬 프로그래머는 코드가 특정 방식으로 포맷되고 특정 규칙을 따르기를 기대하기 때문입니다. 파이썬 코드를 작성할 때는 [PEP8: 파이썬 코드 스타일 가이드](https://www.python.org/dev/peps/pep-0008/)와 [PEP257: 문서문자열 규칙](https://www.python.org/dev/peps/pep-0257/)을 따르는 것이 좋습니다.

다음 문서에서는 더욱 사용자 친화적인 방식으로 설명을 제공합니다.

-   [PEP 8을 사용하여 아름다운 파이썬 코드를 작성하는 방법](https://realpython.com/python-pep8/)
-   [파이썬 코드 문서화: 완벽 가이드](https://realpython.com/documenting-python-code/).

## 규칙

이 문서에서는 따라야 하는 파이썬 예제에 대한 몇 가지 규칙을 보여줍니다.

아래는 일반적인 함수 서명입니다.


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None, support=None)
```

-   키-값 쌍이 있는 인수는 선택 사항이며, 기본값은 서명에 표시됩니다. 즉, 다음 호출은 동등합니다.


```python
Wire = make_wire(pointslist, False, None, None, None)
Wire = make_wire(pointslist, False, None, None)
Wire = make_wire(pointslist, False, None)
Wire = make_wire(pointslist, False)
Wire = make_wire(pointslist)
```


:   이 예에서 첫 번째 인수에는 기본값이 없으므로 항상 포함되어야 합니다.

-   인수가 명시적 키와 함께 주어지면, 선택적 인수는 어떤 순서로든 주어질 수 있습니다. 즉, 다음 호출은 동등합니다.


```python
Wire = make_wire(pointslist, closed=False, placement=None, face=None)
Wire = make_wire(pointslist, closed=False, face=None, placement=None)
Wire = make_wire(pointslist, placement=None, closed=False, face=None)
Wire = make_wire(pointslist, support=None, closed=False, placement=None, face=None)
```

-   파이썬의 가이드라인은 코드의 가독성을 강조합니다; 특히, 함수 이름 바로 뒤에 괄호가 와야 하고, 쉼표 뒤에는 공백이 와야 합니다.


```python
p1 = Vector(0, 0, 0)
p2 = Vector(1, 1, 0)
p3 = Vector(2, 0, 0)
Wire = make_wire([p1, p2, p3], closed=True)
```

-   코드를 여러 줄에 걸쳐 나누어야 하는 경우, 괄호나 소괄호 안에 쉼표를 찍어야 합니다. 두 번째 줄은 이전 줄에 맞춰야 합니다.


```python
a_list = [1, 2, 3,
          2, 4, 5]

Wire = make_wire(pointslist,
                False, None,
                None, None)
```

-   함수는 또다른 그리기 함수의 기반으로 사용될 수 있는 객체를 반환할 수 있습니다.


```python
Wire = make_wire(pointslist, closed=True, face=True)
Window = make_window(Wire, name="Big window")
```



## 가져오기(import)

파이썬 함수는 모듈이라는 파일에 저장됩니다. 해당 모듈의 어떤 기능을 사용하려면 먼저 해당 모듈을 `import` 명령어로 문서에 포함해야 합니다.

이렇게 하면 접두사가 붙은 함수, 즉 `module.function()`가 생성됩니다. 이 시스템은 서로 다른 모듈에서 온 동일한 이름을 가진 함수들 간의 이름 충돌을 방지합니다. 예를 들어, 두 함수 `Arch.make_window()`와 `myModule.make_window()`는 문제 없이 공존할 수 있습니다.

전체 예시에는 필요한 가져오기와 접두사가 붙은 함수가 포함되어야 합니다.


```python
import FreeCAD as App
import Draft

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 1, 0)
p3 = App.Vector(2, 0, 0)
Wire = Draft.make_wire([p1, p2, p3], closed=True)
```


```python
import FreeCAD as App
import Draft
import Arch

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1, 0, 0)
p3 = App.Vector(1, 1, 0)
p4 = App.Vector(0, 2, 0)
pointslist = [p1, p2, p3, p4]

Wire = Draft.make_wire(pointslist, closed=True, face=True)
Structure = Arch.make_structure(Wire, name="Big pillar")
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [API](Category_API.md) > [Python Code](Category_Python Code.md) > [Glossary](Category_Glossary.md) > Python/ko
