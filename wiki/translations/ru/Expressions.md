# Expressions/ru
{{TOCright}}



## Обзор

Некоторые свойства объектов могут быть определены с помощью математических выражений. В графическом интерфейсе счетчики или поля ввода свойств которые поддерживают выражения, содержат синий значок <img alt="" src=images/Bound-expression.svg  style="width:24px;">. Щелчок по значку или ввод знака равенства **&#61;** вызывает редактор выражений для этого конкретного свойства.


<div class="mw-translate-fuzzy">

Выражение FreeCAD - это математическое выражение, следующее за обозначениями стандартных математических операторов и функций, как описано ниже. Кроме того, выражение может ссылаться на другие свойства, а также использовать условные выражения. К числам в выражении может быть добавлена необязательная единица измерения.


</div>

В числах, для отделение целых цифр от десятичных, можно использовать запятую `,` или десятичную точку `.`. Когда используется такой разделитель (точка или запятая), за ним *должна* следовать хотя бы одна цифра. Таким образом, выражения **1.+2.** и **1,+2,** недопустимы, но **1.0 + 2.0** и **1,0 + 2,0** действительны.


<div class="mw-translate-fuzzy">

Операторы и функции зависят от единиц измерения и требуют допустимых комбинаций единиц, если таковые имеются. Например, `2mm + 4mm` является допустимым выражением, а `2mm + 4` - нет (причина в том, что выражение типа `1in + 4` люди обычно интерпретируют как `1 дюйм + 4 дюйма`, но все единицы внутренне преобразуются в систему СИ, и система не может это угадать). В настоящее время распознаются такие [единицы](#Единицы_измерения.md).


</div>

Some unit related errors can seem unintuitive, with expressions either being rejected or producing results that do not match the units of the property being set. Here are some examples:


`1/2mm`

is not interpreted as half a millimeter but as `1/(2mm)`, resulting in: `0.5 mm^-1`.


`sqrt(2)mm`

is not valid because the function call is not a number. This has to be entered as `sqrt(2) * 1mm`.



### Аргументы функции 

Multiple arguments to a function may be separated by either a semicolon followed by a space `, `. In the latter case, the comma is converted to a semicolon after entry. When a semicolon is used, no trailing space is necessary.

Arguments may include references to cells in a spreadsheet. A cell reference consists of the cell\'s uppercase row letter followed by its column number, for example `A1`. A cell may also be referenced by using the cell\'s alias instead, for example `Spreadsheet.MyPartWidth`.



### Ссылка на объект в выражении 

You can reference an object by its **Name** or by its **Label**. In the case of a **Label**, it must be enclosed in double `<<` and `>>` symbols, such as `<<Label>>`.

You can reference any property of an object. For example, to reference a Cylinder\'s height, you may use `Cylinder.Height` or `<<Long_name_of_cylinder>>.Height`. To reference the object itself use the `_self` pseudo property. For example, you may use `Cylinder._self` or `<<Label_of_cylinder>>._self`.

To reference list objects, use `<<object_label>>.list[list_index]` or `object_name.list[list_index]`. If you want for example to reference a constraint in a sketch, use `<<MySketch>>.Constraints[16]`. If you are in the same sketch you may omit its name and just use `Constraints[16]`.
**Note:** The index starts with 0, therefore Constraint17 has to be referenced as `Constraints[16]`.

For more information about referencing objects, see [Reference to CAD_data](#Reference_to_CAD_data.md). 

## Поддерживаемые константы 

Поддерживаются следующие константные значения:

  Constant   Description
   
  **e**      [Euler\'s number](https://en.wikipedia.org/wiki/E_(mathematical_constant))
  **pi**     [Pi](https://en.wikipedia.org/wiki/Pi)


{{Top}}



## Поддерживаемые операторы 

Поддерживаются следующие операторы:

  Оператор   Описание
   
  **+**      [Сложение](https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)
  **-**      [Вычитание](https://ru.wikipedia.org/wiki/%D0%92%D1%8B%D1%87%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5)
  **\***     [Умножение](https://ru.wikipedia.org/wiki/%D0%A3%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)
  **/**      [Деление](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0))
  **%**      [Остаток от деления](https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81_%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BA%D0%BE%D0%BC)
  **\^**     [Возведение в степень](https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D1%81%D1%82%D0%B5%D0%BF%D0%B5%D0%BD%D1%8C)


{{Top}}



## Поддерживаемые функции 



### Основные математические функции 

Поддерживаются следующие математические функции:



#### Функции тригонометрии 

[Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions) use degree as their default unit. For radian measure, add first value in an expression. So e.g. `cos(45)` is the same as `cos(pi rad / 4)`. Expressions in degrees can use either `deg` or `°`, e.g. `360deg - atan2(3; 4)` or `360&deg; - atan2(3; 4)`. If an expression is without units and needs to be converted to degrees or radians for compatibility, multiply by `1&nbsp;deg`, `1&nbsp;°` or `1&nbsp;rad` as appropriate, e.g. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.


<div class="mw-translate-fuzzy">

  Функция       Описание                                                                                                                                                                                                                                                                                                 Допустимый диапазон значений
    
  acos(x)       [Арккосинус](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5_%D1%82%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8#%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_arccos)   -1 \<= x \<= 1
  asin(x)       [Арксинус](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5_%D1%82%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8#%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_arcsin)     -1 \<= x \<= 1
  atan(x)       [Арктангенс](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5_%D1%82%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8#%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F_arctg)    любое значение
  atan2(x; y)   [Функция Atan2](https://en.wikipedia.org/wiki/Atan2) of *x/y*                                                                                                                                                                                                                                            любое значение, за исключением y = 0
  cos(x)        [Косинус](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                         любое значение
  cosh(x)       [Гиперболический косинус](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%B5%D1%80%D0%B1%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                           любое значение
  sin(x)        [Синус](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                           любое значение
  sinh(x)       [Гиперболический синус](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%B5%D1%80%D0%B1%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                             любое значение
  tan(x)        [Тангенс](https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                         любое значение, за исключением x = n\*90, где n = целое число
  tanh(x)       [Гиперболический тангенс](https://ru.wikipedia.org/wiki/%D0%93%D0%B8%D0%BF%D0%B5%D1%80%D0%B1%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8)                                                                                                           любое значение
  hypot(x; y)   [Сумма Пифагора](https://en.wikipedia.org/wiki/Pythagorean_addition) (**hypot**инуза). Например, hypot(4; 3) = 5.                                                                                                                                                                                        x и y \> 0
  cath(x; y)    Учитывая гипотенузу и одну сторону, возвращает другую сторону треугольника. Например, cath (5; 3) = 4.                                                                                                                                                                                                   x и y \> 0, x \>= y


</div>



#### Экспоненциальные и логарифмические функции 

++++
| Function                       | Description                                                                                  | Input range |
+================================+==============================================================================================+=============+
|                 | [Exponential function](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition) | all         |
| `exp(x)`              |                                                                                              |             |
|                             |                                                                                              |             |
++++
|                 | [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)                         | x \> 0      |
| `log(x)`              |                                                                                              |             |
|                             |                                                                                              |             |
++++
|                 | [Common logarithm](https://en.wikipedia.org/wiki/Common_logarithm)                           | x \> 0      |
| `log10(x)`            |                                                                                              |             |
|                             |                                                                                              |             |
++++
|                 | [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                               | all         |
| `pow(x; y)`           |                                                                                              |             |
|                             |                                                                                              |             |
++++
|                 | [Square root](https://en.wikipedia.org/wiki/Square_root)                                     | x \>= 0     |
| `sqrt(x)`             |                                                                                              |             |
|                             |                                                                                              |             |
++++
|                 | [Cubic root](https://en.wikipedia.org/wiki/Cube_root)                                        | all         |
| `cbrt(x)`             |                                                                                              |             |
|                             |                                                                                              |             |
| <small>(v0.21)</small>  |                                                                                              |             |
++++



#### Функции округления, усечения и вычисления остатка от деления 

++++
| Function             | Description                                                                                                                      | Input range       |
+======================+==================================================================================================================================+===================+
|       | [Absolute value](https://en.wikipedia.org/wiki/Absolute_value)                                                                   | all               |
| `abs(x)`    |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++
|       | [Ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), smallest integer value greater than or equal to x | all               |
| `ceil(x)`   |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++
|       | [Floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), largest integer value less than or equal to x       | all               |
| `floor(x)`  |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++
|       | [Remainder](https://en.wikipedia.org/wiki/Remainder) after dividing *x* by *y*, sign of result is that of the dividend.          | all, except y = 0 |
| `mod(x; y)` |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++
|       | [Rounding](https://en.wikipedia.org/wiki/Rounding) to the nearest integer                                                        | all               |
| `round(x)`  |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++
|       | [Truncation](https://en.wikipedia.org/wiki/Truncation) to the nearest integer in the direction of zero                           | all               |
| `trunc(x)`  |                                                                                                                                  |                   |
|                   |                                                                                                                                  |                   |
++++


{{Top}}



### Функции агрегирования и статистики 

[Aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function) take one or more arguments.
Individual arguments to aggregate functions may consist of ranges of cells. A range of cells is expressed as two cell references separated by a colon {{Incode|:}}, for example {{Incode|average(B1:B8)}} or {{Incode|sum(A1:A4; B1:B4)}}. The cell references may also use cell aliases, for example {{Incode|average(StartTemp:EndTemp)}}.

Поддерживаются следующие функции агрегирования:

++++
| Function                         | Description                                                                                                                        | Input range |
+==================================+====================================================================================================================================+=============+
|                   | [Average](https://en.wikipedia.org/wiki/Arithmetic_mean) value of the arguments, same as sum(a; b; c; \...) / count(a; b; c; \...) | all         |
| `average(a; b; c; ...)` |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++
|                   | [Count](https://en.wikipedia.org/wiki/Counting) of the arguments, typically used for cell ranges                                   | all         |
| `count(a; b; c; ...)`   |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++
|                   | [Maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                  | all         |
| `max(a; b; c; ...)`     |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++
|                   | [Minimum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                  | all         |
| `min(a; b; c; ...)`     |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++
|                   | [Standard deviation](https://en.wikipedia.org/wiki/standard_deviation) of the values of the arguments                              | all         |
| `stddev(a; b; c; ...)`  |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++
|                   | [Sum](https://en.wikipedia.org/wiki/Summation) of the values of the arguments, typically used for cell ranges                      | all         |
| `sum(a; b; c; ...)`     |                                                                                                                                    |             |
|                               |                                                                                                                                    |             |
++++


{{Top}}



### Операции со строками 



#### Идентификация строк 

Strings are identified in expressions by surrounding them with opening/closing double chevrons (as are labels).

In following example, \"TEXT\" is recognized as a string : `<<TEXT>>`



#### Объединение строк 

Строки могут быть объединены с помощью символа \"+\".

Например строки `<<МОЙ>> + <<ТЕКСТ>>` будут объединены в \"МОЙТЕКСТ\".



#### Преобразование числа в строку 

Числовые значения могут быть преобразованы в строки с помощью функции `str`:


`str(Box.Length.Value)`



#### Форматирование строк 

Форматирование строк поддерживается с использованием (старого) Python способа в стиле %.

Сведения о всех %-спецификаторах, можно узнать из [документации Python](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

As an example, supposing you have a default 10mm-side cube named \'Box\' (default FreeCAD naming), the following expression `<<Cube length : %s>> % Box.Length` will expand to \"Cube length : 10.0 mm\"

For more than one %-specifier use the following syntax: `<<Cube length is %s and width is %s>> % tuple(Box.Length; Box.Width)`. Or use concatenation: `<<Cube length is %s>> % Box.Length + << and width is %s>> % Box.Width`. Both will expand to \"Cube length is 10.0 mm and width is 10.0 mm\".

Пример файла FreeCAD с применением форматирования строк доступен [на форуме](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) 


<div class="mw-translate-fuzzy">

### Функция Create 


</div>


<div class="mw-translate-fuzzy">

С помощью функции `create` в выражениях могут быть созданы следующие объекты :

-   Vector
-   Matrix
-   Rotation
-   Placement


</div>

++++
| Type                                                                               | Function                                        | Description                                                                                                                                                                                                                                                                                                                             |
+====================================================================================+=================================================+=========================================================================================================================================================================================================================================================================================================================================+
|                                                                     |                                  | Example: `tuple(2; 1; 2)`                                                                                                                                                                                                                                                                                        |
| `Tuple`                                                                   | `tuple(a; b; ...)`                     |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                              |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                  | Example: `list(2; 1; 2)`                                                                                                                                                                                                                                                                                         |
| `List`                                                                    | `list(a; b; ...)`                      |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                              |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Vector`](Vector_API.md)                           |                                  | Create a vector using three unit-less or `Length` unit values. Example: `vector(2; 1; 3)`                                                                                                                                                                                                 |
|                                                                                    | `vector(x; y; z)`                      |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                              |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `create(<<vector>>; x; y; z)`                                             |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Matrix`](Matrix_API.md)                           | matrix(                                       | Create a 4x4 matrix in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order): $\begin{bmatrix}                                                                                                                                                                                                                   |
|                                                                                    |   a~11~; a~12~; a~13~; a~14~; | a_{11} & a_{12} & a_{13} & a_{14} \\                                                                                                                                                                                                                                                                                                    |
|                                                                                    |   a~21~; a~22~; a~23~; a~24~; | a_{21} & a_{22} & a_{23} & a_{24} \\                                                                                                                                                                                                                                                                                                    |
|                                                                                    |   a~31~; a~32~; a~33~; a~34~; | a_{31} & a_{32} & a_{33} & a_{34} \\                                                                                                                                                                                                                                                                                                    |
|                                                                                    |   a~41~; a~42~; a~43~; a~44~    | a_{41} & a_{42} & a_{43} & a_{44} \\                                                                                                                                                                                                                                                                                                    |
|                                                                                    | )                                             | \end{bmatrix}$                                                                                                                                                                                                                                                                                                                          |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | A minimum of 1 argument can be supplied such as `matrix(1)` which creates an identity matrix.                                                                                                                                                                                                                    |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | Example: `matrix(1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16)`                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `create(<<matrix>>; a<sub>11</sub>; a<sub>12</sub>; ...; a<sub>44</sub>)` |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                  | Create a `Rotation` by specifying its `axis` (`Vector`) and `angle` (`Angle` unit or unit-less), or three Euler angles `α`, `β`, `γ`. Examples: |
| `Rotation`                                                                | `rotation(axis; angle)`                |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                              | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `rotation(vector(0; 1; 0); 45)`                                                                                                                                                                                                                                                                                            |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `create(<<rotation>>; 30; 30; 30)`                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `rotation(α; β; γ)`                                                       |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `create(<<rotation>>; axis; angle)`                                       |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `create(<<rotation>>; α; β; γ)`                                           |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
| [`Placement`](Placement_API.md)                     |                                  | Create a `Placement` with various parameters, including:                                                                                                                                                                                                                                                         |
|                                                                                    | `placement(base; rotation)`            |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                              | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `base`                                                                                                                                                                                                                                                                                                                     |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : base location (`Vector`)                                                                                                                                                                                                                                                                                   |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `center`                                                                                                                                                                                                                                                                                                                   |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : center location (`Vector`)                                                                                                                                                                                                                                                                                 |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `rotation`                                                                                                                                                                                                                                                                                                                 |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : `Rotation`                                                                                                                                                                                                                                                                                                 |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `axis`                                                                                                                                                                                                                                                                                                                     |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : Rotation axis (`Vector`)                                                                                                                                                                                                                                                                                   |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `angle`                                                                                                                                                                                                                                                                                                                    |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : Rotation angle (unit-less or `Angle` unit value)                                                                                                                                                                                                                                                           |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `matrix`                                                                                                                                                                                                                                                                                                                   |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |     : `Matrix`                                                                                                                                                                                                                                                                                                   |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | Examples:                                                                                                                                                                                                                                                                                                                               |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `placement(vector(2; 1; 3); rotation(vector(0; 0; 1); 45))`                                                                                                                                                                                                                                                                |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                    |                                                 | -                                                                                                                                                                                                                                                                                                                        |
|                                                                                    |                                                 |     `create(<<placement>>; create(<<vector>>; 2; 1; 2); create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45))`                                                                                                                                                                                                                |
|                                                                                    |                                                 |                                                                                                                                                                                                                                                                                                                                      |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `placement(base; rotation; center)`                                       |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `placement(base; axis; angle)`                                            |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `placement(matrix)`                                                       |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++
|                                                                     |                                                 |                                                                                                                                                                                                                                                                                                                                         |
| `create(<<placement>>; ...)`                                              |                                                 |                                                                                                                                                                                                                                                                                                                                         |
|                                                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                         |
++++


{{Top}}

### Matrix functions 


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



## Условные выражения 

Conditional expressions are of the form `condition ? resultTrue : resultFalse`. The condition is defined as an expression that evaluates to either `0` (false) or non-zero (true). Note that enclosing the conditional expression in parentheses is currently considered an error.

The following [relational operators](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators) are defined:

  Unit      Description
   
  **==**    equal to
  **!=**    not equal to
  **\>**    greater than
  **\<**    less than
  **\>=**   greater than or equal to
  **\<=**   less than or equal to


{{Top}}



## Единицы измерений 

Units can be used directly in expressions. The parser connects them to the previous value. So `2mm` or `2 mm` is valid while `mm` is invalid because there is no preceding value.

All values must have a unit. Therefore you must in general use a unit for values in spreadsheets.
In some cases it works even without a unit, for example if you have e.g. in spreadsheet cell B1 just the number `1.5` and refer to it for a pad height. This only works because the pad height predefines the unit `mm` that is used if no unit is given. It will nevertheless fail if you use for the pad height e.g. `Sketch1.Constraints.Width - Spreadsheet.B1` because `Sketch1.Constraints.Width` has a unit and `Spreadsheet.B1` has not.

Units with exponents can directly be entered. So e.g. `mm^3` will be recognized as mm³ and `m^3` will be recognized as m³.

If you have a variable whose name is that of a unit you must put the variable between `<< >>` to prevent it from being recognized as a unit. For example if you have the dimension `Sketch.Constraints.A` it would be recognized as the unit ampere. Therefore you must write it in the expression as `Sketch.Constraints.<<A>>`.

The following units are recognized by the expression parser:



### Количество вещества 

  Unit   Description
   
  mmol   Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol    [Mole](https://en.wikipedia.org/wiki/Mole_(unit))



### Угол

  Единица измерения   Описание
   
  °                   [Градус](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)); тоже самое, что и deg
  deg                 [Градус](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)); тоже самое, что и °
  rad                 [Радиан](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B4%D0%B8%D0%B0%D0%BD)
  gon                 [Град](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F))
  S                   [Угловая секунда](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)#%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F_%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D0%B0); тоже самое, что и ″
  ″                   [Угловая секунда](https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_(%D0%B3%D0%B5%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%8F)#%D0%A3%D0%B3%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F_%D1%81%D0%B5%D0%BA%D1%83%D0%BD%D0%B4%D0%B0); тоже самое, что и S
  M                   [Минута дуги](https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BD%D1%83%D1%82%D0%B0_%D0%B4%D1%83%D0%B3%D0%B8); тоже самое, что и ′
  ′                   [Минута дуги](https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BD%D1%83%D1%82%D0%B0_%D0%B4%D1%83%D0%B3%D0%B8); тоже самое, что и M



### Ток

  Unit   Description
   
  mA     Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A      [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA     Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA     Mega[ampere](https://en.wikipedia.org/wiki/Ampere)

### Electric capacitance 

  Unit   Description
   
  pF     Pico[farad](https://en.wikipedia.org/wiki/Farad)
  nF     Nano[farad](https://en.wikipedia.org/wiki/Farad)
  uF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit µF
  µF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit uF
  mF     Milli[farad](https://en.wikipedia.org/wiki/Farad)
  F      [Farad](https://en.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg

### Electric charge 


<div class="mw-translate-fuzzy">

Электрический заряд:

  Единица измерения   Описание
   
  C                   [Кулон](https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%BB%D0%BE%D0%BD); 1 C = 1 A·s, {{Version/ru|0.19}}


</div>

### Electric conductivity 

  Unit   Description
   
  uS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit µS
  µS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit uS
  mS     Milli[siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  S      [Siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS     Kilo[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  MS     Mega[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))

### Electric inductance 

  Unit   Description
   
  nH     Nano[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  uH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit µH
  µH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit uH
  mH     Milli[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  H      [Henry](https://en.wikipedia.org/wiki/Henry_(unit)); 1 H = 1 kg·m\^2/s\^2/A\^2

### Electric potential 

Электрический потенциал:

  Единица измерения   Описание
   
  mV                  Милли[вольт](https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%BB%D1%8C%D1%82)
  V                   [Вольт](https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%BB%D1%8C%D1%82)
  kV                  Кило[вольт](https://ru.wikipedia.org/wiki/%D0%92%D0%BE%D0%BB%D1%8C%D1%82)

### Electric resistance 


<div class="mw-translate-fuzzy">

Электрическое сопротивление:

  Единица измерения   Описание
   
  Ohm                 [Ом](https://ru.wikipedia.org/wiki/%D0%9E%D0%BC); 1 Ohm = 1 kg·m\^2/s\^3/A\^2, {{Version/ru|0.19}}
  kOhm                Кило[ом](https://ru.wikipedia.org/wiki/%D0%9E%D0%BC), {{Version/ru|0.19}}
  MOhm                Мега[ом](https://ru.wikipedia.org/wiki/%D0%9E%D0%BC), {{Version/ru|0.19}}


</div>



### Энергия/работа

  Unit   Description
   
  mJ     Milli[joule](https://en.wikipedia.org/wiki/Joule)
  J      [Joule](https://en.wikipedia.org/wiki/Joule)
  kJ     Kilo[joule](https://en.wikipedia.org/wiki/Joule)
  eV     [Electronvolt](https://en.wikipedia.org/wiki/Electronvolt); 1 eV = 1.602176634e-19 J
  keV    Kilo[electronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  MeV    Mega[electronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  kWh    [Kilowatt hour](https://en.wikipedia.org/wiki/Kilowatt_hour); 1 kWh = 3.6e6 J
  Ws     [Watt second](https://en.wikipedia.org/wiki/Joule#Watt_second); alternative to the unit Joule
  VAs    [Volt-ampere-second](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule
  CV     [Coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule
  cal    [Calorie](https://en.wikipedia.org/wiki/Calorie); 1 cal = 4.184 J
  kcal   Kilo[calorie](https://en.wikipedia.org/wiki/Calorie)



### Сила

  Единица измерения   Описание
   
  mN                  Милли[ньютон](https://ru.wikipedia.org/wiki/%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F))
  N                   [Ньютон](https://ru.wikipedia.org/wiki/%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F))
  kN                  Кило[ньютон](https://ru.wikipedia.org/wiki/%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F))
  MN                  Мега[ньютон](https://ru.wikipedia.org/wiki/%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD_(%D0%B5%D0%B4%D0%B8%D0%BD%D0%B8%D1%86%D0%B0_%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F))
  lbf                 [Фунт-сила](https://en.wikipedia.org/wiki/Pound_(force))(Английская единица)



### Длина

  Unit   Description
   
  nm     Nano[meter](https://en.wikipedia.org/wiki/Metre)
  um     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit µm
  µm     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit um
  mm     Milli[meter](https://en.wikipedia.org/wiki/Metre)
  cm     Centi[meter](https://en.wikipedia.org/wiki/Metre)
  dm     Deci[meter](https://en.wikipedia.org/wiki/Metre)
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



### Интенсивность света 

  Unit   Description
   
  cd     [Candela](https://en.wikipedia.org/wiki/Candela)

### Magnetic flux 

  Unit   Description
   
  Wb     [Weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A

### Magnetic flux density 

  Unit   Description
   
  G      [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T
  T      [Tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A



### Масса

  Unit   Description
   
  ug     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit µg
  µg     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit ug
  mg     Milli[gram](https://en.wikipedia.org/wiki/Gram)
  g      [Gram](https://en.wikipedia.org/wiki/Gram)
  kg     Kilo[gram](https://en.wikipedia.org/wiki/Gram)
  t      [Tonne](https://en.wikipedia.org/wiki/Tonne)
  oz     [Ounce](https://en.wikipedia.org/wiki/Ounce)
  lb     [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit lbm
  lbm    [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit lb
  st     [Stone](https://en.wikipedia.org/wiki/Stone_(weight))
  cwt    [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)



### Мощность

  Unit   Description
   
  W      [Watt](https://en.wikipedia.org/wiki/Watt)
  kW     Kilo[watt](https://en.wikipedia.org/wiki/Watt)



### Давление

  Unit    Description
   
  Pa      [Pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  kPa     Kilo[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  MPa     Mega[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  GPa     Giga[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  uTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit µTorr
  µTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit uTorr
  mTorr   Milli[torr](https://en.wikipedia.org/wiki/Torr)
  Torr    [Torr](https://en.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch); 1 psi = 6.895 kPa
  ksi     Kilo[pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch)



### Температура

  Unit   Description
   
  uK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit µK
  µK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit uK
  mK     Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K      [Kelvin](https://en.wikipedia.org/wiki/Kelvin)



### Время

  Unit       Description
   
  s          [Second](https://en.wikipedia.org/wiki/Second)
  min        [Minute](https://en.wikipedia.org/wiki/Minute)
  h          [Hour](https://en.wikipedia.org/wiki/Hour)
  Hz (1/s)   [Hertz](https://en.wikipedia.org/wiki/Hertz)
  kHz        Kilo[hertz](https://en.wikipedia.org/wiki/Hertz),
  MHz        Mega[hertz](https://en.wikipedia.org/wiki/Hertz)
  GHz        Giga[hertz](https://en.wikipedia.org/wiki/Hertz)
  THz        Tera[hertz](https://en.wikipedia.org/wiki/Hertz)



### Объем

  Unit   Description
   
  ml     Milli[liter](https://en.wikipedia.org/wiki/Litre)
  l      [Liter](https://en.wikipedia.org/wiki/Litre)
  cft    Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit))

### Special imperial units 

  Unit   Description
   
  mph    [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour)
  sqft   [Square foot](https://en.wikipedia.org/wiki/Square_foot)



### Неподдерживаемые единицы измерения 

The following commonly used units are not yet supported, for some an alternative is provided:

  Unit   Description                                                                                              Alternative
    
  °C     [Celsius](https://en.wikipedia.org/wiki/Celsius)                                                         \[°C\] + 273.15 K
  °F     [Fahrenheit](https://en.wikipedia.org/wiki/Fahrenheit);                                                  (\[°F\] + 459.67) × ​5/9
  u      [Atomic mass unit](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit Da   1.66053906660e-27 kg
  Da     [Dalton](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit u              1.66053906660e-27 kg
  sr     [Steradian](https://en.wikipedia.org/wiki/Steradian)                                                     not directly
  lm     [Lumen](https://en.wikipedia.org/wiki/Lumen_(unit))                                                      not directly
  lx     [Lux](https://en.wikipedia.org/wiki/Lux)                                                                 not directly
  px     [Pixel](https://en.wikipedia.org/wiki/Pixel)                                                             not directly


{{Top}}

## Invalid characters and names 

The expression feature is very powerful but to achieve this power it has some limitations concerning some characters. To overcome this, FreeCAD offers to use labels and reference them instead of the object names. In labels you can use almost all special characters.

In cases where you cannot use a label, such as the name of a sketch\'s constraints, you must be aware what characters are not allowed.

### Labels

For [labels](Object_name#Label.md) there are no invalid characters, however some characters need to be escaped:

+++
| Characters                                               | Description                                                               |
+==========================================================+===========================================================================+
|                                           | Need to be escaped by adding `\` in front of them. |
| `'`                                             |                                                                           |
|                                                       |                                                                           |
| , `\`, `"` |                                                                           |
+++

For example, the label `Sketch\002` must be referenced as `<<Sketch\\002>>`.



### Названия

[Names](Object_name#Name.md) of objects like dimensions, sketches, etc. may not have the characters or character sequences listed below, otherwise the name is invalid:

  Characters / Character sequences                                                                                               Description
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**   Characters that are math operators or part of mathematical constructs
  **A**, **kA**, **mA**, **MA**, **J**, **K**, **\'**, **ft**, **°**, and many more!                                             Characters and character sequences that are units (see the [Units](#Units.md) paragraph)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, and many more!          Characters used as placeholder or to trigger special operations
  **pi**, **e**                                                                                                                  Mathematical constants
  **´**, **\**, **\'**, **\"**                                                                                                  Characters used for accents
  space                                                                                                                          A space defines the end of a name and can therefore not be used

For example, the following name is valid: `<<Sketch>>.Constraints.T2üßµ@`. While these are invalid names: `<<Sketch>>.Constraints.test\result_2` (\\r means \"carriage return\") or `<<Sketch>>.Constraints.mol` (mol is a unit).

Since shorter names (especially if they have only one or two characters) can easily result in invalid names, consider using longer names and/or establishing a suitable naming convention.

### Cell aliases 

See [Spreadsheet SetAlias](Spreadsheet_SetAlias#Usage.md). {{Top}}

## Reference to CAD data 

It is possible to use data from the model itself in an expression. To reference a property use`object.property`. If the property is a compound of fields, the individual fields can be accessed as `object.property.field`.

The following table shows some examples:

++++
| CAD data                                              | Call in expression                       | Result                                                                                                                                                                       |
+=======================================================+==========================================+==============================================================================================================================================================================+
| Length of a [Part Box](Part_Box.md)           |                           | Length with units (mm)                                                                                                                                                       |
|                                                       | `Box.Length`                    |                                                                                                                                                                              |
|                                                       |                                       |                                                                                                                                                                              |
++++
| Volume of the Box                                     |                           | Volume in mm³ without units                                                                                                                                                  |
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


{{Top}}

## Document-wide global variables 

There is no concept of global variables in FreeCAD at the moment. Instead, arbitrary variables can be defined as cells in a spreadsheet using the [Spreadsheet workbench](Spreadsheet_Workbench.md), and then be given a name using the alias property for the cell (right-click on cell). Then they can be accessed from any expression just as any other object property. {{Top}}

## Cross-document linking 

It is possible (with limitations) to define a Property of an object in your current document (\".FCstd\" file) by using an Expression to reference a Property of an object contained in a different document (\".FCstd\" file). For example, a cell in a spreadsheet or the **Length** of a Part Cube, etc. in one document can be defined by an Expression that references the X Placement value or another Property of an object contained in a different document.

A document\'s name is used to reference it from other documents. When saving a document the first time, you choose a file name; this is usually different from the initial default \"Unnamed1\" (or its translated equivalent). To prevent links being lost when the master document is renamed upon saving, it is recommended that you first create the master document, create a spreadsheet inside it, and save it. Subsequently, you can still make changes to the file and its spreadsheet but you should not rename it.

Once the master document with the spreadsheet is created and saved (named), it is safe to create dependent documents. For example, assuming you name the master document `master`, the spreadsheet `modelConstants`, and give a cell an alias-name `Length`, you can then access the value as:


`master#modelConstants.Length`

**Note:** that the master document must be loaded for the values in the master to be available to the dependent document.

Unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.

Of course, it\'s up to you to load the corresponding documents later when you want to change anything. 

## Известные проблемы / нерешённые задачи 

-   The dependency graph is based on the relationship between document objects, not properties. This means that you cannot provide data to an object and query that same object for results. For example, even though there are no cyclic dependencies when the properties themselves are considered, you may not have an object which gets its dimensions from a spreadsheet and then display the volume of that object in the same spreadsheet. As a work-around use multiple spreadsheets, one to drive your model and the other for reporting.
-   The expression parser does not handle parentheses well, and is unable to properly parse some expressions. For example: `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` results in an error, while `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` is accepted. The expression `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` cannot be entered in any form.
-   As stated above, unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.
-   FreeCAD does not yet have a built-in expression manager where all expressions in a document are listed, and can be created, deleted, queried, etc. But an addon is available: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Open bugs/tickets for Expressions can be found in the [FreeCAD Bugtracker Expressions category](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/ru
