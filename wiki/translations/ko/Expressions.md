# Expressions/ko
## 개요

수학적 표현식을 사용하여 속성을 정의할 수 있습니다. 표현식으로 속성이 정의되면 GUI 입력란 오른쪽의 수학식을 상징하는 아이콘 <img alt="" src=images/Bound-expression.svg  style="width:16px;">은 회색에서 파란색으로 바뀝니다. 아이콘을 클릭하거나 등호 **&#61;**를 입력하면 해당 속성에 대한 표현식 편집기가 열립니다. 입력란에 아이콘 대신 **...** 버튼이 표시되는 경우 속성을 마우스 오른쪽 버튼으로 클릭하고 상황에 맞는 메뉴에서 **표현식...**을 선택하면 표현식 편집기를 열 수 있습니다.

FreeCAD 표현식은 아래에 설명된 표준 수학 [연산자](#Supported_operators.md), [함수](#Supported_functions.md) 및 [미리 정의된 상수를](#Supported_constants.md) 사용하는 수학적 표현식입니다. 또한 표현식은 개체 속성을 참조할 수도 있고 [조건문을](#조건식.md) 사용할 수도 있습니다. 표현식의 숫자에는 선택적으로 [단위가](#Units.md) 붙을 수 있습니다.

숫자에는 쉼표 `,` 또는 소수점 `.`을 사용하여 숫자와 소수점을 구분할 수 있습니다. 소수점 표시를 사용할 때에는 \'반드시\' 숫자가 하나 이상 뒤에 와야 합니다. 따라서 표현식 `1. + 2.`와 `1, + 2,`는 유효하지 않지만, `1.0 + 2.0`과 `1,0 + 2,0`은 유효한 표현입니다.

연산자와 함수는 단위를 인식하며, 단위를 넣을 경우 유효한 단위 조합이 필요합니다. 예를 들어, `2mm + 4mm`는 유효한 표현식이지만, `2mm + 4`는 유효하지 않습니다. 이 규칙은 길이 속성과 같이 단위가 있는 개체 속성에 대한 참조에도 적용됩니다. 따라서 `Pad001.Length + 1`은 길이 단위가 있는 속성에 순수한 숫자를 추가하므로 유효하지 않습니다. `Pad001.Length + 1mm`처럼 단위를 붙여햐 합니다.

일부 단위 관련 오류는 직관적이지 않은 것처럼 보일 수 있으며, 표현식이 거부되거나 설정된 속성의 단위와 일치하지 않는 결과가 생성될 수 있습니다. 다음은 몇 가지 예입니다.


`1/2mm`

is not interpreted as half a millimeter but as `1/(2mm)`, resulting in: `0.5 mm^-1`.


`sqrt(2)mm`

is not valid because the function call is not a number. This has to be entered as `sqrt(2) * 1mm`.



### 함수의 인수 

함수에 다수의 인수를 전달할 때는 세미콜론 뒤에 공백 `, `으로 구분합니다.(예: `sum(10;20)`또는 `sum(10, 20)` ) 후자의 경우, 쉼표는 입력 후 세미콜론으로 자동으로 변환되며 만일 쉼표 뒤에 공백이 없다면 이 경우 두 개의 인수가 아닌 10.2라는 하나의 인수로 인식하여 의도하지 않은 결과를 얻을 수 있습니다. 세미콜론을 사용하면 공백이 필요하지 않고 실수를 예방할 수 있습니다.

인수에는 스프레드시트의 셀에 대한 참조가 포함될 수 있습니다. 셀 참조시에는 셀의 대문자 열 뒤에 행 번호를 사용합니다(예: A1). 셀은 또한 별칭(예: `Spreadsheet.MyPartWidth`)을 사용하여 참조될 수 있습니다.



### 객체 참조 

위에서 이미 본 것처럼, **Name**으로 객체를 참조할 수 있습니다. 하지만 **Label**을 사용할 수도 있습니다. **Label**의 경우 `<<`와 `>>` 기호를 두 개 사용하여 묶어야 합니다(예: `<<Label>>`).

표현식에서는 객체의 어떤 속성이든 참조할 수 있습니다. 예를 들어, Cylinder의 높이를 참조하려면 `Cylinder.Height` 또는 `<<Label_of_cylinder>>.Height`를 사용할 수 있습니다.

객체 참조에 대한 자세한 내용은 [CAD 데이터 참조를](#Reference_to_CAD_data.md) 부분을 보세요. 

## 지원되는 상수 

다음의 상수들을 표현식에 사용할 수 있습니다.

  상수     설명
   
  **e**    [Euler\'s number](https://en.wikipedia.org/wiki/E_(mathematical_constant))
  **pi**   [Pi](https://en.wikipedia.org/wiki/Pi)


{{Top}}



## 지원되는 연산 

다음 연산들을 사용할 수 있습니다.

  연산자자   설명
   
  **+**      [덧셈](https://en.wikipedia.org/wiki/Addition)
  **-**      [뺄셈](https://en.wikipedia.org/wiki/Subtraction)
  **\***     [곱](https://en.wikipedia.org/wiki/Multiplication)
  **/**      부동 소수점 [나눗셈](https://en.wikipedia.org/wiki/Division_(mathematics))
  **%**      [나머지](https://en.wikipedia.org/wiki/Remainder)
  **\^**     [지수화](https://en.wikipedia.org/wiki/Exponentiation)


{{Top}}



## 지원되는 함수 



### 일반 수학 함수 

표현식에서 다음의 수학 함수들을 사용할 수 있습니다:



#### 삼각 함수 

[삼각 함수](https://en.wikipedia.org/wiki/Trigonometric_functions)는 기본적으로 각도의 단위로 도(度)를 사용합니다. 각도의 단위로 라디안을 사용하는 경우 표현식의 첫 번째 값 뒤에 `rad`를 추가합니다. 예를 들어 `cos(45)`는 `cos(pi rad / 4)`와 동일합니다. 각도 표현에서는 `deg` 또는 `°`를 사용할 수 있습니다(예: `360deg - atan2(3; 4)` 또는 `360&deg; - atan2(3; 4)`). 표현식에 단위가 없고 호환성을 위해 도 또는 라디안으로 변환해야 하는 경우, `1deg`, `1°` 또는 `1rad`를 적절하게 곱합니다(예: `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`).

++++
| 함수                   | 설명                                                                                                                                                                              | 입력값 범위                                |
+========================+===================================================================================================================================================================================+============================================+
|         | [Arc cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)                                                                                      | -1 \<= x \<= 1                             |
| `acos(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Arc sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)                                                                                        | -1 \<= x \<= 1                             |
| `asin(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties), return value in the range -90° \< value \< 90°                                     | all                                        |
| `atan(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties) of *y/x* accounting for quadrant, return value in the range -180° \< value \<= 180° | all, the invalid input x = y = 0 returns 0 |
| `atan2(y; x)` |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                 | all                                        |
| `cos(x)`      |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                  | all                                        |
| `cosh(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Sine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                   | all                                        |
| `sin(x)`      |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                    | all                                        |
| `sinh(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                | all, except x = n\*90 with n = odd integer |
| `tan(x)`      |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                 | all                                        |
| `tanh(x)`     |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | [Pythagorean addition](https://en.wikipedia.org/wiki/Pythagorean_addition) (**hypot**enuse), e.g. hypot(4; 3) = 5                                                                 | x and y \>= 0                              |
| `hypot(x; y)` |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++
|         | Given hypotenuse, and one side, returns other side of triangle, e.g. cath(5; 3) = 4                                                                                               | x \>= y \>= 0                              |
| `cath(x; y)`  |                                                                                                                                                                                   |                                            |
|                     |                                                                                                                                                                                   |                                            |
++++



#### 지수 함수와 대수 함수 

++++
| 함수                           | 설명                                                                                                    | 입력값 범위 |
+================================+=========================================================================================================+=============+
|                 | [지수 함수(Exponential function)](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition) | all         |
| `exp(x)`              |                                                                                                         |             |
|                             |                                                                                                         |             |
++++
|                 | [자연 로그(Natural logarithm)](https://en.wikipedia.org/wiki/Natural_logarithm)                         | x \> 0      |
| `log(x)`              |                                                                                                         |             |
|                             |                                                                                                         |             |
++++
|                 | [상용 로그(Common logarithm)](https://en.wikipedia.org/wiki/Common_logarithm)                           | x \> 0      |
| `log10(x)`            |                                                                                                         |             |
|                             |                                                                                                         |             |
++++
|                 | [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                                          | all         |
| `pow(x; y)`           |                                                                                                         |             |
|                             |                                                                                                         |             |
++++
|                 | [제곱근(Square root)](https://en.wikipedia.org/wiki/Square_root)                                        | x \>= 0     |
| `sqrt(x)`             |                                                                                                         |             |
|                             |                                                                                                         |             |
++++
|                 | [세제곱근(Cubic root)](https://en.wikipedia.org/wiki/Cube_root)                                         | all         |
| `cbrt(x)`             |                                                                                                         |             |
|                             |                                                                                                         |             |
| <small>(v0.21)</small>  |                                                                                                         |             |
++++



#### 반올림, 잘라내기 및 나머지 함수 

++++
| 함수                 | 설명                                                                                                                     | 입력값 범위       |
+======================+==========================================================================================================================+===================+
|       | [절대값(Absolute value)](https://en.wikipedia.org/wiki/Absolute_value)                                                   | all               |
| `abs(x)`    |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++
|       | [천정 함수(Ceiling function)](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), x보다 크거나 같은 최소 정수 값 | all               |
| `ceil(x)`   |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++
|       | [바닥 함수(Floor function)](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), x보다 작거나 같은 최대 정수 값   | all               |
| `floor(x)`  |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++
|       | x를 y로 나눈 [나머지](https://en.wikipedia.org/wiki/Remainder), 결과의 부호는 피제수의 부호와 같습니다.                  | all, except y = 0 |
| `mod(x; y)` |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++
|       | 가장 가까운 정수로 [반올림](https://en.wikipedia.org/wiki/Rounding)                                                      | all               |
| `round(x)`  |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++
|       | 0 방향의 가장 가까운 정수로 [잘라내기](https://en.wikipedia.org/wiki/Truncation)                                         | all               |
| `trunc(x)`  |                                                                                                                          |                   |
|                   |                                                                                                                          |                   |
++++


{{Top}}



### 통계/집계 함수 

[집계 함수](https://en.wikipedia.org/wiki/Aggregate_function)는 하나 이상의 인수를 취합니다.
집계 함수의 개별 인수는 셀 범위로 구성될 수 있습니다. 셀 범위는 콜론 {{Incode|:}}으로 구분된 두 개의 셀 참조로 표현됩니다(예: {{Incode|average(B1:B8)}} 또는 {{Incode|sum(A1:A4; B1:B4)}}). 셀 참조는 셀 별칭(예: {{Incode|average(StartTemp:EndTemp)}})을 사용할 수도 있습니다.

다음과 같은 집계 함수를 사용할 수 있습니다.

++++
| 함수                             | 설명                                                                                                                              | 입력값 범위 |
+==================================+===================================================================================================================================+=============+
|                   | 인수의 [산술 평균](https://en.wikipedia.org/wiki/Arithmetic_mean)값으로 , sum(a; b; c; \...) / count(a; b; c; \...)와 동일합니다. | all         |
| `average(a; b; c; ...)` |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++
|                   | 일반적으로 셀 범위에 사용되는 인수의 [개수(Count)](https://en.wikipedia.org/wiki/Counting)                                        | all         |
| `count(a; b; c; ...)`   |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++
|                   | 인수의 [최대(Maximum)](https://en.wikipedia.org/wiki/Maxima_and_minima)값                                                         | all         |
| `max(a; b; c; ...)`     |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++
|                   | 인수의 [최소(Minimum)](https://en.wikipedia.org/wiki/Maxima_and_minima)값                                                         | all         |
| `min(a; b; c; ...)`     |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++
|                   | [Standard deviation](https://en.wikipedia.org/wiki/standard_deviation) of the values of the arguments                             | all         |
| `stddev(a; b; c; ...)`  |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++
|                   | 인수 값의 [합계(Sum)](https://en.wikipedia.org/wiki/Summation)는 일반적으로 셀 범위에 사용됩니다.                                 | all         |
| `sum(a; b; c; ...)`     |                                                                                                                                   |             |
|                               |                                                                                                                                   |             |
++++


{{Top}}



### 문자열 조작 



#### 문자열 식별 

표현식에서 문자열은 문자열을 여는/닫는 겹화살 괄호로 둘러싸서 식별합니다.

다음 예에서 \"TEXT\"는 문자열로 인식됩니다: `<<TEXT>>`



#### 문자열 연결 

문자열은 \'+\' 기호를 사용하여 연결할 수 있습니다.

다음 예제 `<<MY>> + <<TEXT>>`는 \"MYTEXT\"로 연결됩니다.



#### 문자열 변환 

숫자 값은 `str` 함수를 사용하여 문자열로 변환할 수 있습니다.


`str(Box.Length.Value)`



#### 문자열 서식 

문자열 서식은 (오래된) % 형식의 파이썬 방식을 사용하여 지원됩니다.

모든 %-지정자는 [파이썬 문서](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)에 정의된 대로입니다.

예를 들어, \'Box\'라는 이름(기본 FreeCAD 명명)의 기본 한 변의 길이가10mm인 정육면체가 있다고 가정하면, 다음 표현식 `<<정육면체 길이 : %s>> % Box.Length`는 \"정육면체 길이 : 10.0 mm\"로 치환 됩니다.

\% 지정자가 두 개 이상인 경우 다음 구문을 사용하세요: `<<큐브 길이는 %s이고 너비는 %s입니다>> % tuple(Box.Length; Box.Width)`. 또는 연결을 사용하세요: `<<큐브 길이는 %s입니다>> % Box.Length + << 너비는 %s입니다>> % Box.Width`. 둘 다 \"큐브의 길이는 10.0mm이고 너비는 10.0mm입니다\"로 치환 됩니다.

문자열 서식을 사용하는 FreeCAD 예제는 [포럼](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657)에서 볼 수 있습니다. 

### 객체 생성 함수 

The following objects may be created in expressions using the following functions:

++++
| Type                                                           | Function                                                                           | Description                                                                                                                                                                                                                                                                                                                             |
+================================================================+====================================================================================+=========================================================================================================================================================================================================================================================================================================================================+
|                                                 |                                                                     | Example: `tuple(2; 1; 2)`                                                                                                                                                                                                                                                                                        |
| `Tuple`                                               | `tuple(a; b; ...)`                                                        |                                                                                                                                                                                                                                                                                                                                         |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                 |                                                                     | Example: `list(2; 1; 2)`                                                                                                                                                                                                                                                                                         |
| `List`                                                | `list(a; b; ...)`                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Vector`](Vector_API.md)       |                                                                     | Create a vector using three unit-less or `Length` unit values. Example: `vector(2; 1; 3)`                                                                                                                                                                                                 |
|                                                                | `vector(x; y; z)`                                                         |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `create(<<vector>>; x; y; z)`                                             |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Matrix`](Matrix_API.md)       | matrix(                                                                          | Create a 4x4 matrix in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order): $\begin{bmatrix}                                                                                                                                                                                                                   |
|                                                                |   a~11~; a~12~; a~13~; a~14~;                                    | a_{11} & a_{12} & a_{13} & a_{14} \\                                                                                                                                                                                                                                                                                                    |
|                                                                |   a~21~; a~22~; a~23~; a~24~;                                    | a_{21} & a_{22} & a_{23} & a_{24} \\                                                                                                                                                                                                                                                                                                    |
|                                                                |   a~31~; a~32~; a~33~; a~34~;                                    | a_{31} & a_{32} & a_{33} & a_{34} \\                                                                                                                                                                                                                                                                                                    |
|                                                                |   a~41~; a~42~; a~43~; a~44~                                       | a_{41} & a_{42} & a_{43} & a_{44} \\                                                                                                                                                                                                                                                                                                    |
|                                                                | )                                                                                | \end{bmatrix}$                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | A minimum of 1 argument can be supplied such as `matrix(1)` which creates an identity matrix.                                                                                                                                                                                                                    |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | Example: `matrix(1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16)`                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `create(<<matrix>>; a<sub>11</sub>; a<sub>12</sub>; ...; a<sub>44</sub>)` |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                 |                                                                     | Create a `Rotation` by specifying its `axis` (`Vector`) and `angle` (`Angle` unit or unit-less), or three Euler angles `α`, `β`, `γ`. Examples: |
| `Rotation`                                            | `rotation(axis; angle)`                                                   |                                                                                                                                                                                                                                                                                                                                         |
|                                                             |                                                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `rotation(vector(0; 1; 0); 45)`                                                                                                                                                                                                                                                                                            |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `create(<<rotation>>; 30; 30; 30)`                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `rotation(α; β; γ)`                                                       |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `create(<<rotation>>; axis; angle)`                                       |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `create(<<rotation>>; α; β; γ)`                                           |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Placement`](Placement_API.md) |                                                                     | Create a `Placement` with various parameters, including:                                                                                                                                                                                                                                                         |
|                                                                | `placement(base; rotation)`                                               |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `base`                                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : base location (`Vector`)                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `center`                                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : center location (`Vector`)                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `rotation`                                                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : `Rotation`                                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `axis`                                                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : Rotation axis (`Vector`)                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `angle`                                                                                                                                                                                                                                                                                                                    |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : Rotation angle (unit-less or `Angle` unit value)                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `matrix`                                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |     : `Matrix`                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | Examples:                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `placement(vector(2; 1; 3); rotation(vector(0; 0; 1); 45))`                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |     `create(<<placement>>; create(<<vector>>; 2; 1; 2); create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45))`                                                                                                                                                                                                                |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                      |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `placement(base; rotation; center)`                                       |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `placement(base; axis; angle)`                                            |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `placement(matrix)`                                                       |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                | `create(<<placement>>; ...)`                                              |                                                                                                                                                                                                                                                                                                                                         |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++


{{Top}}



### 향량(Vector) 함수 

함수: <small>(v1.0)</small> .

+++
| 함수 / 연산자                       | 설명                                                                                                                                                                                |
+=====================================+=====================================================================================================================================================================================+
|                      | 두 향량의 덧셈.                                                                                                                                                                     |
| `v1 + v2`                  |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | 두 향량의 뺄셈.                                                                                                                                                                     |
| `v1 - v2`                  |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | 향량을 균일하게 `s` 배율 곱.                                                                                                                                 |
| `v * s`                    |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | 두 향량 사이의 각도                                                                                                                                                                 |
| `vangle(v1; v2)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Cross product of two vectors $v_1 \times v_2$.                                                                                                                                      |
| `vcross(v1; v2)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Dot product of two vectors $v_1 \cdot v_2$.                                                                                                                                         |
| `v1 * v2`                  |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      |                                                                                                                                                                                     |
| `vdot(v1; v2)`             |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Distance between vector `v1` and a line through `v2` in direction `v3`.                                        |
| `vlinedist(v1; v2; v3)`    |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Distance between vector `v1` and the closest point on a line segment from `v2` to `v3`.                        |
| `vlinesegdist(v1; v2; v3)` |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Project vector `v1` on a line through `v2` in direction `v3`.                                                  |
| `vlineproj(v1; v2; v3)`    |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Normalize a vector to a unit vector.                                                                                                                                                |
| `vnormalize(v)`            |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Distance between vector `v1` and a plane defined by a point `v2` and a normal `v3`.                            |
| `vplanedist(v1)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Project vector `v1` on a plane defined by a point `v2` and a normal `v3`.                                      |
| `vplaneproj(v1)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Non-uniformly scale a vector by `sx` in the X direction, `sy` in the Y direction, and `sz` in the Z direction. |
| `vscale(v; sx; sy; sz)`    |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      |                                                                                                                                                                                     |
| `vscalex(v; sx)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      |                                                                                                                                                                                     |
| `vscaley(v; sy)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      |                                                                                                                                                                                     |
| `vscalez(v; sz)`           |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++


{{Top}}



### 행렬 함수 


`Rotation`

and `Placement` can each be represented by a `Matrix`. The following functions all take in a `Matrix`, `Rotation`, or `Placement` as their first parameter denoted in the table below by `m`. The type of the returned object is the same as the object supplied in the first argument except when using `mtranslate` on a `Rotation`, in which case a `Placement` will be returned.

+++
| Function                           | Description                                                                                                                                                                                                                                                                                          |
+====================================+======================================================================================================================================================================================================================================================================================================+
|                     | Calculate the [Inverse matrix](https://en.wikipedia.org/wiki/Invertible_matrix).                                                                                                                                                                                                                     |
| `minvert(m)`              |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Rotate](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) by either:                                                                                                                                                                                                                  |
| `mrotate(m; rotation)`    |                                                                                                                                                                                                                                                                                                      |
|                                 | -   a `Rotation`                                                                                                                                                                                                                                                              |
|                                    | -   an axis (`Vector`) and an angle (`Angle` unit or unit-less)                                                                                                                                                                                        |
|                                    | -   three Euler angles `α`, `β`, `γ`                                                                                                                                                                                            |
+++
|                     |                                                                                                                                                                                                                                                                                                      |
| `mrotate(m; axis; angle)` |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     |                                                                                                                                                                                                                                                                                                      |
| `mrotate(m; α; β; γ)`     |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Rotate](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) around the X axis.                                                                                                                                                                                                          |
| `mrotatex(m; angle)`      |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Rotate](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) around the Y axis.                                                                                                                                                                                                          |
| `mrotatey(m; angle)`      |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Rotate](https://en.wikipedia.org/wiki/Transformation_matrix#Rotation_2) around the Z axis.                                                                                                                                                                                                          |
| `mrotatez(m; angle)`      |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Translate](https://en.wikipedia.org/wiki/Translation_(geometry)#Matrix_representation) by a `vector` (`Vector`) or X, Y, Z values. If a `Rotation` is translated, the returned object is a `Placement`. |
| `mtranslate(m; vector)`   |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     |                                                                                                                                                                                                                                                                                                      |
| `mtranslate(m; x; y; z)`  |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     | [Scale](https://en.wikipedia.org/wiki/Scaling_(geometry)#Matrix_representation) by a `vector` (`Vector`) or X, Y, Z values.                                                                                                                            |
| `mscale(m; vector)`       |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++
|                     |                                                                                                                                                                                                                                                                                                      |
| `mscale(m; x; y; z)`      |                                                                                                                                                                                                                                                                                                      |
|                                 |                                                                                                                                                                                                                                                                                                      |
+++


{{Top}}



## 조건식

조건식은 ` 조건 ? 참인 경우 결과 : 거짓인 경우 결과` 형식입니다. 조건은 `0`(false) 또는 0이 아닌 값(true)으로 평가되는 식으로 정의됩니다.

부울 속성을 조건으로 사용하려면 다음 구문을 사용해야 합니다. `VarSet.MyBool &#61;&#61; 1 ? 10 mm : 15 mm`.

다음의 [관계 연산자](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators) 정의되어 있습니다.

  연산자    설
   
  **==**    양 쪽이 같다
  **!=**    같지 않다
  **\>**    왼쪽이 오른쪽 보다 크다
  **\<**    왼쪽이 오른쪽 보다 작다
  **\>=**   왼쪽이 오른쪽 보다 크거나 같다
  **\<=**   왼족이 오른쪽 보다 작거나 같다


{{Top}}



## 단위

단위는 표현식에서 직접 사용할 수 있습니다. FreeCAD의 구문 분석기는 단위를 앞의 값에 연결합니다. 따라서 `2mm` 또는 `2 mm`는 유효하지만 `mm`는 선행 값이 없기 때문에 유효하지 않습니다.

모든 값에는 단위가 있어야 합니다. 따라서 일반적으로 스프레드시트의 값에는 단위를 사용해야 합니다.
어떤 경우에는 단위가 없어도 작동합니다. 예를 들어, 스프레드시트 셀 B1에 숫자 `1.5`만 있고 깔판(pad) 높이를 참조하는 경우입니다. 단위가 지정되지 않은 경우에 사용되는 단위 `mm`를 미리 정의되었기 때문에 작동합니다. 그럼에도 불구하고 깔판 높이로 `Sketch1.Constraints.Width - Spreadsheet.B1`을 사용하면 실패합니다. 그 이유는 `Sketch1.Constraints.Width`에는 단위가 있지만 `Spreadsheet.B1`에는 단위가 없기 때문입니다.

지수가 있는 단위는 직접 입력할 수 있습니다. 예를 들어 `mm^3`은 mm³로 인식되고 `m^3`은 m³로 인식됩니다.

변수 이름이 단위와 같을 경우 변수를 `<< >>` 사이에 넣어야 단위로 인식되는 것을 방지할 수 있습니다. 예를 들어, 치수 이름이 `Sketch.Constraints.A`이면 전류 단위인 암페어로 인식됩니다. 따라서 표현식에서 `Sketch.Constraints.<<A>>`로 작성해야 합니다.

다음 단위들은 표현식의 구문 분석기에 의해 인식됩니다:



### 물질의 양 

  단위   설명
   
  mmol   밀리[몰(Millimole)](https://en.wikipedia.org/wiki/Mole_(unit))
  mol    [몰(Mole)](https://en.wikipedia.org/wiki/Mole_(unit))



### 각도


<div class="mw-translate-fuzzy">

  단위   설명
   
  °      [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit deg
  deg    [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit °
  rad    [Radian](https://en.wikipedia.org/wiki/Radian)
  gon    [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  S      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit ″
  ″      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit S
  M      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit ′
  ′      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit M


</div>



### 전류

  단위   설명
   
  mA     Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A      [암페어(Ampere)](https://en.wikipedia.org/wiki/Ampere)
  kA     Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA     Mega[ampere](https://en.wikipedia.org/wiki/Ampere)



### 정전 용량 

  단위   설명
   
  pF     Pico[farad](https://en.wikipedia.org/wiki/Farad)
  nF     Nano[farad](https://en.wikipedia.org/wiki/Farad)
  uF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit µF
  µF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit uF
  mF     Milli[farad](https://en.wikipedia.org/wiki/Farad)
  F      [패럿(Farad)](https://en.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg



### 전하량

  단위   설명
   
  C      [쿨롱(Coulomb)](https://en.wikipedia.org/wiki/Coulomb); 1 C = 1 A\*s



### 전기 전도도 

  단위   설명
   
  uS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit µS
  µS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit uS
  mS     Milli[지멘스](https://en.wikipedia.org/wiki/Siemens_(unit))
  S      [Siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS     Kilo[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  MS     Mega[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))



### 전기 유도용량 

  단위   설명
   
  nH     Nano[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  uH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit µH
  µH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit uH
  mH     Milli[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  H      [헨리](https://en.wikipedia.org/wiki/Henry_(unit)); 1 H = 1 kg·m\^2/s\^2/A\^2



### 전위

  단위   설명
   
  mV     Milli[volt](https://en.wikipedia.org/wiki/Volt)
  V      [볼트(Volt)](https://en.wikipedia.org/wiki/Volt)
  kV     Kilo[volt](https://en.wikipedia.org/wiki/Volt)



### 전기 저항 

  단위   설명
   
  Ohm    [옴(Ohm)](https://en.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2
  kOhm   Kilo[ohm](https://en.wikipedia.org/wiki/Ohm)
  MOhm   Mega[ohm](https://en.wikipedia.org/wiki/Ohm)



### 능량(能量, Energy)/일(work) 

  단위   설명
   
  mJ     Milli[joule](https://en.wikipedia.org/wiki/Joule)
  J      [줄(Joule)](https://en.wikipedia.org/wiki/Joule)
  kJ     Kilo[joule](https://en.wikipedia.org/wiki/Joule)
  eV     [Electronvolt](https://en.wikipedia.org/wiki/Electronvolt); 1 eV = 1.602176634e-19 J
  keV    Kilo[electronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  MeV    Mega[electronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  kWh    [Kilowatt hour](https://en.wikipedia.org/wiki/Kilowatt_hour); 1 kWh = 3.6e6 J
  Ws     [와트시](https://en.wikipedia.org/wiki/Joule#Watt_second); alternative to the unit Joule
  VAs    [Volt-ampere-second](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule
  CV     [Coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule
  cal    [칼로리(Calorie)](https://en.wikipedia.org/wiki/Calorie); 1 cal = 4.184 J
  kcal   Kilo[calorie](https://en.wikipedia.org/wiki/Calorie)



### 힘(Force)

  단위   설명
   
  mN     Milli[뉴튼(newton)](https://en.wikipedia.org/wiki/Newton_(unit))
  N      [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN     Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN     Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf    [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))



### 길이

  단위   설명
   
  nm     Nano[meter](https://en.wikipedia.org/wiki/Metre)
  um     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit µm
  µm     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit um
  mm     Milli[meter](https://en.wikipedia.org/wiki/Metre)
  cm     Centi[meter](https://en.wikipedia.org/wiki/Metre)
  dm     Deci[미터(Meter)](https://en.wikipedia.org/wiki/Metre)
  m      [Meter](https://en.wikipedia.org/wiki/Metre)
  km     Kilo[meter](https://en.wikipedia.org/wiki/Metre)
  mil    [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative to the unit thou
  thou   [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative to the unit mil
  in     [Inch](https://en.wikipedia.org/wiki/Inch); alternative to the unit \"
  \"     [Inch](https://en.wikipedia.org/wiki/Inch); alternative to the unit in
  ft     [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternative to the unit \'
  \'     [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternative to the unit ft
  yd     [Yard](https://en.wikipedia.org/wiki/Yard)
  mi     [Mile](https://en.wikipedia.org/wiki/Mile)

### Luminous intensity 

  Unit   Description
   
  cd     [Candela](https://en.wikipedia.org/wiki/Candela)



### 자속(磁束)

  Unit   Description
   
  Wb     [Weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A



### 자속밀도

  Unit   Description
   
  G      [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T
  T      [Tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A



### 질량

  단위   설명
   
  ug     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit µg
  µg     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit ug
  mg     밀리[그램](https://en.wikipedia.org/wiki/Gram)
  g      [그램](https://en.wikipedia.org/wiki/Gram)
  kg     킬로[그램](https://en.wikipedia.org/wiki/Gram)
  t      [톤](https://en.wikipedia.org/wiki/Tonne)
  oz     [Ounce](https://en.wikipedia.org/wiki/Ounce)
  lb     [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit lbm
  lbm    [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit lb
  st     [Stone](https://en.wikipedia.org/wiki/Stone_(weight))
  cwt    [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)



### 전력(電力, Power) 

  단위   설명
   
  W      [와트(Watt)](https://en.wikipedia.org/wiki/Watt)
  kW     킬로[와트](https://en.wikipedia.org/wiki/Watt)



### 압력

  단위    설명
   
  Pa      [파스칼](https://en.wikipedia.org/wiki/Pascal_(unit))
  kPa     Kilo[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  MPa     Mega[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  GPa     Giga[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  uTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit µTorr
  µTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit uTorr
  mTorr   Milli[torr](https://en.wikipedia.org/wiki/Torr)
  Torr    [Torr](https://en.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch); 1 psi = 6.895 kPa
  ksi     Kilo[pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch)



### 온도

  단위   설명
   
  uK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit µK
  µK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit uK
  mK     Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K      [켈빈](https://en.wikipedia.org/wiki/Kelvin)



### 시간

  단위       설명
   
  s          [초](https://en.wikipedia.org/wiki/Second)
  min        [분](https://en.wikipedia.org/wiki/Minute)
  h          [시간](https://en.wikipedia.org/wiki/Hour)
  Hz (1/s)   [헤르츠](https://en.wikipedia.org/wiki/Hertz)
  kHz        Kilo[hertz](https://en.wikipedia.org/wiki/Hertz),
  MHz        Mega[hertz](https://en.wikipedia.org/wiki/Hertz)
  GHz        Giga[hertz](https://en.wikipedia.org/wiki/Hertz)
  THz        Tera[hertz](https://en.wikipedia.org/wiki/Hertz)



### 부피

  단위   설명
   
  ml     Milli[liter](https://en.wikipedia.org/wiki/Litre)
  l      [리터](https://en.wikipedia.org/wiki/Litre)
  cft    Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit))

### Special imperial units 

  Unit   Description
   
  mph    [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour)
  sqft   [Square foot](https://en.wikipedia.org/wiki/Square_foot)



### 지원되지 않는 단위 

다음과 같은 일반적으로 사용되는 단위는 아직 지원되지 않으며, 일부 단위에는 대체 단위가 제공됩니다.

  단위   설명                                                                                                     대체
    
  °C     [Celsius](https://en.wikipedia.org/wiki/Celsius)                                                         \[°C\] + 273.15 K
  °F     [Fahrenheit](https://en.wikipedia.org/wiki/Fahrenheit);                                                  (\[°F\] + 459.67) × ​5/9
  u      [Atomic mass unit](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit Da   1.66053906660e-27 kg
  Da     [Dalton](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit u              1.66053906660e-27 kg
  sr     [Steradian](https://en.wikipedia.org/wiki/Steradian)                                                     not directly
  lm     [Lumen](https://en.wikipedia.org/wiki/Lumen_(unit))                                                      not directly
  lx     [Lux](https://en.wikipedia.org/wiki/Lux)                                                                 not directly
  px     [Pixel](https://en.wikipedia.org/wiki/Pixel)                                                             not directly


{{Top}}



## 잘못된 문자 및 이름 

표현식은 매우 강력하지만,일부 문자 사용에 제약이 있습니다. 이를 극복하기 위해 FreeCAD는 개체 이름 대신 표지(Label)을 사용하고 참조하도록 제안합니다. 표지에서는 거의 모든 특수 문자를 사용할 수 있습니다.

스케치의 구속 이름과 같은 표지(lable)를 사용할 수 없는 경우 어떤 문자가 허용되지 않는지 알고 있어야 합니다.



### 표지(Labels)

[표지에는](Object_name#Label.md) 사용할 수 없는 문자는 없지만 일부 문자는 이스케이프해야 합니다:

+++
| 문자                                                     | 설명                                    |
+==========================================================+=========================================+
|                                           |                          |
| `'`                                             | `\`                            |
|                                                       |                                      |
| , `\`, `"` | 를 앞에 추가하여 이스케이프해야 합니다. |
+++

예를 들어, 표지 `Sketch\002`는 `<<Sketch\\002>>`로 참조되어야 합니다.



### 이름

치수, 스케치 등의 객체의 [이름에는](Object_name#Name.md) 아래에 나열된 문자나 문자열이 ​​없어야 합니다. 그렇지 않은 이름은 유효하지 않습니다.

  문자 / 문자열                                                                                                                  Description
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**   수학 연산자 또는 수학 구성의 일부인 문자
  **A**, **kA**, **mA**, **MA**, **J**, **K**, **\'**, **ft**, **°**, 기타 등등!                                                 단위인 문자 및 문자 시퀀스([단위](#Units.md) 문단 참조)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, 기타 등등!              자리 표시자로 사용하거나 특수 작업을 유발하는 데 사용되는 문자
  **pi**, **e**                                                                                                                  수학 상수
  **´**, **\**, **\'**, **\"**                                                                                                  강조에 사용되는 문자
  공백                                                                                                                           공백은 이름의 끝을 정의하므로 사용할 수 없습니다.

예를 들어, 다음 이름은 유효합니다: `<<Sketch>>.Constraints.T2üßµ@`. 그러나 다음의 이름은 유효하지 않은 이름입니다: `<<Sketch>>.Constraints.test\result_2` (\\r은 \"캐리지 리턴\"을 의미함) 또는 `<<Sketch>>.Constraints.mol` (mol은 단위임).

짧은 이름(특히 문자가 하나 또는 두 개뿐인 경우)은 쉽게 잘못된 이름을 생성할 수 있으므로 더 긴 이름을 사용하거나 적절한 명명 규칙을 수립하는 것을 고려하세요.



### 셀 별명 

[스프레드시트 SetAlias를](Spreadsheet_SetAlias#Usage.md) 참조하세요. 

## CAD 데이터 참조 

모형 자체의 데이터를 표현식에서 사용하는 것이 가능합니다. 속성을 참조하려면 `object_name.property` 또는 `<<object_label>>.property`를 사용하고, 표지는 `<<` 및 `>>`로 묶어야 합니다. 표지를 사용하려면 고유해야 합니다

다음 모든 예에서는 객체를 이름으로 참조하지만, 어떤 경우에도 객체 표지를 사용할 수 있습니다.

속성이 필드의 합성인 경우 개별 필드는 `object_name.property.field`로 액세스할 수 있습니다.

목록 객체를 참조하려면 `object_name.list[list_index]`를 사용합니다. 스케치에서 구속(Constraint)을 참조하려면 `Sketch.Constraints[16]`를 사용합니다.

객체 자체를 참조하려면 `_self` 가상 속성인 `object_name._self`를 사용합니다.

다음 표에서는 몇 가지 예를 더 보여줍니다:

++++
| CAD 데이터                                            | 표현식에서 호출                          | 결과                                                                                                                                                                         |
+=======================================================+==========================================+==============================================================================================================================================================================+
| [상자의](Part_Box/ko.md) 길이                 |                           | 길이 (단위: mm)                                                                                                                                                              |
|                                                       | `Box.Length`                    |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| 상자의 부피                                           |                           | mm&sup3 단위의 부피                                                                                                                                                          |
|                                                       | `Box.Shape.Volume`              |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Shape type of the Box                                 |                           | String: Solid                                                                                                                                                                |
|                                                       | `Box.Shape.ShapeType`           |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Label of the Box                                      |                           | String: Label                                                                                                                                                                |
|                                                       | `Box.Label`                     |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| X-coordinate of center of mass of the Box             |                           | X-coordinate in mm without units                                                                                                                                             |
|                                                       | `Box.Shape.CenterOfMass.x`      |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| X-coordinate of the Box placement                     |                           | X-coordinate with units (mm)                                                                                                                                                 |
|                                                       | `Box.Placement.Base.x`          |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| X-component of the rotation axis of the Box placement |                           | X-component of the unit vector in mm without units                                                                                                                           |
|                                                       | `Box.Placement.Rotation.Axis.x` |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Rotation angle of the Box placement                   |                           | Rotation angle with units (deg)                                                                                                                                              |
|                                                       | `Box.Placement.Rotation.Angle`  |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Full Box object                                       |                                                                                                                                   |
|                                                       | `Box._self`                     |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Value of constraint in a sketch                       |                           | Numeric value of the named constraint `Width` in the sketch, if the expression is used in the sketch itself.                                          |
|                                                       | `Constraints.Width`             |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Value of constraint in a sketch                       |                           | Numeric value of the named constraint `Width` in the sketch, if the expression is used outside of the sketch.                                         |
|                                                       | `MySketch.Constraints.Width`    |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Value of a spreadsheet alias                          |                           | Value of the alias `Depth` in the spreadsheet `Spreadsheet`                                                                    |
|                                                       | `Spreadsheet.Depth`             |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Value of a local property                             |                           | Value of the **Length** property in e.g a Pad object, if the expression is used in e.g **Length2** in the same object. |
|                                                       | `Length`                        |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++



### 순환 종속성 

FreeCAD는 속성이 아닌 문서 객체 간의 관계에 따라 종속성을 확인합니다. 즉, 객체에 데이터를 제공한다면 동일한 객체에 대한 결과를 조회할 수는 없습니다. 예를 들어 속성 자체를 고려할 때 순환 종속성이 없더라도 스프레드시트에서 치수를 가져온 다음 동일한 스프레드시트에 해당 개체의 볼륨을 표시하는 개체가 없을 수 있습니다. 하나는 모델을 구동하는 데, 다른 하나는 보고용으로 두 개의 스프레드시트를 사용해야 합니다.

해결 방법으로, **바인딩 종속성 숨기기** 옵션과 함께 [셀 바인딩을](Spreadsheet_Workbench#Cell_binding.md) 만들어 두 번째 스프레드시트의 셀 범위를 첫 번째 스프레드시트에 표시하거나 그 반대로 표시할 수 있습니다.

순환 종속성을 해결하는 또 다른 방법은 개별 표현식에 대해 `href` 또는 `hiddenref` 함수를 사용하여 참조를 숨기는 것입니다(예: `href(Box.Length)`).

언급된 두 가지 해결 방법은 주의해서 사용해야 하며, 보고된 속성이 동일한 스프레드시트에서 구동되는 차원에 따라 달라지는 경우 작동하지 않습니다. 

## 문서 전체 전역 변수 

현재 FreeCAD에는 전역 변수라는 개념이 없습니다. 대신, 임의의 변수는 [스프레드시트 작업대를](Spreadsheet_Workbench/ko.md) 사용하여 스프레드시트의 셀로 정의될 수 있으며, 셀의 별명 속성을 사용하여 이름을 지정할 수 있습니다(셀을 마우스 오른쪽 버튼으로 클릭). 그러면 다른 객체 속성과 마찬가지로 모든 표현식에서 접근할 수 있습니다. 

## 문서 사이 연결 

다른 문서(.FCstd 파일)에 포함된 개체의 속성을 참조하는 표현식을 사용하여 현재 문서(.FCstd 파일)에 있는 개체의 속성을 정의하는 것은 (제한이 있긴 하지만) 가능합니다. 예를 들어, 스프레드시트의 셀이나 입방체의 **길이** 등입니다. 한 문서에서는 다른 문서에 포함된 객체의 X 배치 값이나 다른 속성을 참조하는 표현식으로 정의할 수 있습니다.

문서의 이름은 다른 문서에서 참조하는 데 사용됩니다. 문서를 처음 저장할 때 파일 이름을 선택합니다; 이는 일반적으로 초기 기본 \"Unnamed1\"(또는 번역된 동등 값)과 다릅니다. 마스터 문서의 이름을 변경하여 저장할 때 링크가 손실되는 것을 방지하려면 먼저 마스터 문서를 만들고, 그 안에 스프레드시트를 만든 다음 저장하는 것이 좋습니다. 이후에도 해당 파일과 스프레드시트를 변경할 수는 있지만 이름을 바꾸면 안 됩니다.

스프레드시트가 포함된 마스터 문서가 만들어지고 저장(이름 지정)되면 종속 문서를 안전하게 만들 수 있습니다. 예를 들어 마스터 문서의 이름을 `master`로, 스프레드시트의 이름을 `모형modelConstants`로, 셀의 별명을 `Lenth`로 지정했다면 다음과 같이 값에 접근할 수 있습니다:


`master#modelConstants.Length`

마스터의 값을 종속 문서에서 사용할 수 있으려면 마스터 문서를 먼저 로드해야 합니다.

물론, 나중에 무엇인가를 변경하고 싶을 때 해당 문서를 로드하는 것은 여러분의 몫입니다. 

## 알려진 문제 / 남은 작업 

-   FreeCAD에는 아직 문서에 있는 모든 표현식을 나열하고, 만들고, 삭제하고, 조회할 수 있는 기본 제공 표현식 관리자가 없습니다. 하지만 애드온을 사용할 수 있습니다: [fcxref 표현식 관리자](https://github.com/gbroques/fcxref).
-   Expressions에 대한 오픈 버그/티켓은 [GitHub](https://github.com/FreeCAD/FreeCAD/labels/Topic%3A%20Expressions)에서 확인할 수 있습니다.


{{Top}}



## 스크립트


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")
cyl = doc.addObject("Part::Cylinder", "Cylinder")
cyl_name = cyl.Name

box.setExpression("Height", f"{cyl_name}.Height / 2")
box.setExpression("Length", f"{cyl_name}.Radius * 2")
box.setExpression("Width", "Length")

doc.recompute()

# Expressions are stored in the ExpressionEngine property:
for prop, exp in box.ExpressionEngine:
    val = getattr(box, prop)
    print(f"Property: '{prop}' -- Expression: '{exp}' -- Current value: {val}")
```


{{Top}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/ko
