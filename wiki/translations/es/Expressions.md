# Expressions/es
{{TOCright}}

## Resumen

Es posible definir propiedades utilizando expresiones matemáticas. En la interfaz gráfica de usuario, los cuadros de giro o campos de entrada que están vinculados a las propiedades contienen un icono azul <img alt="" src=images/Bound-expression.svg  style="width:24px;">. Haciendo clic en el icono o escribiendo el signo igual **&#61;** aparece el editor de expresiones para esa propiedad en particular.

Es una expresión matemática que sigue la notación de los operadores y funciones matemáticas estándar, como se describe a continuación. Además, la expresión puede hacer referencia a otras propiedades, y también utilizar condicionales. Los números en una expresión pueden tener una unidad opcional adjunta.

Los número pueden usar ya sea una coma `,` o un punto decimal `.` para separar los dígitos enteros de los decimales. Cuando se usa el marcador decimal, \"debe\" ser seguido por al menos un dígito. Por lo tanto, las expresiones {{incode | 1.+2.}} y {{incode | 1,+2,}} son inválidas, pero {{incode | 1.0+2.0}} y {{incode | 1,0+2,0}} son válidas.

Los operadores y las funciones son conscientes de la unidad y requieren combinaciones válidas de unidades, si se suministran. Por ejemplo, {{incode | 2mm+4mm}} es una expresión válida, mientras que {{incode | 2mm+4}} no lo es (la razón es que una expresión como {{incode | 1in+4}} probablemente será interpretada como {{Incode | 1in+4in}} por los humanos, pero todas las unidades se convierten al sistema métrico internamente, y el sistema no puede adivinar esto). Estas [unidades](#Unidades.md) son reconocidas actualmente.

Puedes usar [constantes predefinidas](#Constantes_soportadas.md) y [funciones](#Funciones_soportadas.md).

### Argumentos de la función 

Múltiples argumentos a una función pueden estar separados por un punto y coma  seguida por un espacio  {{incode |, }}. En el último caso, la coma se convierte a un punto y coma después de la entrada. Cuando se usa un punto y coma, no es necesario un espacio final.

Los argumentos pueden incluir referencias a las celdas en una hoja de cálculo. Una referencia de celda consiste en la letra mayúscula de fila de la celda seguida de su número de columna, por ejemplo {{incode | A1}}. También se puede hacer referencia a una celda utilizando el alias de la celda, por ejemplo, `Spreadsheet.MyPartWidth`.

### Referencia de objetos 

Puede hacer referencia a un objeto por su {{PropertyData | Name}} o por su {{PropertyData | Label}}. En el caso de un {{PropertyData | Label}}, debe estar encerrado en doble símbolos {{incode | <<}} y {{incode | >>}}, como {{incode | <<Label>>}}.

Puede referenciar cualquier propiedad de un objeto. Por ejemplo, para referenciar la altura de un Cilindro puede usar `Cylinder.Height` o `<<Long_name_of_cylinder>>.Height`. Para referenciar al objeto mismo use la pseudo propiedad `_self`. Por ejemplo, puede usar `Cylinder._self` o `<<Label_of_cylinder>>._self`.

Para referenciar una lista de objetos use `<<object_label>>.list[list_index]` or `object_name.list[list_index]`. Si quiere por ejemplo referenciar una restricción de un croquis use `<<MySketch>>.Constraints[16]`. Si está en el mismo croquis puede omitir su nombre y solo usar `Constraints[16]`.
**Nota:** El índice inicia en 0, por lo que la restricción 17 tiene el índice 16.

Para más información de como referenciar objetos, vea [Referencia a los datos CAD](#Referencia_a_los_datos_CAD.md). {{Top}}

## Constantes soportadas 

Las siguientes constantes están soportadas.

  Constant   Description
   
  **e**      [Número de Euler](https://es.wikipedia.org/wiki/N%C3%BAmero_e)
  **pi**     [Pi](https://es.wikipedia.org/wiki/N%C3%BAmero_%CF%80)


{{Top}}

## Operadores soportados 

Los siguientes operadores son soportados.

  Operator   Description
   
  **+**      [Suma](https://es.wikipedia.org/wiki/Adici%C3%B3n_(matem%C3%A1tica))
  **-**      [Resta](https://es.wikipedia.org/wiki/Resta)
  **\***     [Multiplicación](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n)
  **/**      [Division](https://es.wikipedia.org/wiki/Divisi%C3%B3n_(matem%C3%A1tica)) de punto flotante
  **%**      [Residuo](https://es.wikipedia.org/wiki/Resto)
  **\^**     [Potenciación](https://es.wikipedia.org/wiki/Potenciaci%C3%B3n)


{{Top}}

## Funciones soportadas 

### Funciones matemáticas generales 

Las siguientes funciones matemáticas son soportadas:

#### Funciones trigonométricas 

[Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions) use degree as their default unit. For radian measure, add first value in an expression. So e.g. `cos(45)` is the same as `cos(pi rad / 4)`. Expressions in degrees can use either `deg` or `°`, e.g. `360deg - atan2(3; 4)` or `360&deg; - atan2(3; 4)`. If an expression is without units and needs to be converted to degrees or radians for compatibility, multiply by `1&nbsp;deg`, `1&nbsp;°` or `1&nbsp;rad` as appropriate, e.g. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.

  Function      Description                                                                                                                                                                         Input range
    
  acos(x)       [Arc cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)                                                                                        -1 \<= x \<= 1
  asin(x)       [Arc sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)                                                                                          -1 \<= x \<= 1
  atan(x)       [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties), return value in the range -90° \< value \< 90°                                       all
  atan2(y; x)   [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties) of *y/x* accounting for quadrant, return value in the range -180° \< value \<= 180°   all, the invalid input x = y = 0 returns 0
  cos(x)        [Cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                   all
  cosh(x)       [Hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                    all
  sin(x)        [Sine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                     all
  sinh(x)       [Hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                      all
  tan(x)        [Tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)                                                                                  all, except x = n\*90 with n = odd integer
  tanh(x)       [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)                                                                                   all
  hypot(x; y)   [Pythagorean addition](https://en.wikipedia.org/wiki/Pythagorean_addition) (**hypot**enuse), e.g. hypot(4; 3) = 5                                                                   x and y \>= 0
  cath(x; y)    Given hypotenuse, and one side, returns other side of triangle, e.g. cath(5; 3) = 4                                                                                                 x \>= y \>= 0

#### Exponential and logarithmic functions 

  Function    Description                                                                                    Input range
    
  exp(x)      [Exponential function](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition)   all
  log(x)      [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)                           x \> 0
  log10(x)    [Common logarithm](https://en.wikipedia.org/wiki/Common_logarithm)                             x \> 0
  pow(x; y)   [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                                 all
  sqrt(x)     [Square root](https://en.wikipedia.org/wiki/Square_root)                                       x \>= 0

#### Rounding, truncation and remainder functions 

  Function    Description                                                                                                                        Input range
    
  abs(x)      [Absolute value](https://en.wikipedia.org/wiki/Absolute_value)                                                                     all
  ceil(x)     [Ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), smallest integer value greater than or equal to x   all
  floor(x)    [Floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), largest integer value less than or equal to x         all
  mod(x; y)   [Remainder](https://en.wikipedia.org/wiki/Remainder) after dividing *x* by *y*, sign of result is that of the dividend.            all, except y = 0
  round(x)    [Rounding](https://en.wikipedia.org/wiki/Rounding) to the nearest integer                                                          all
  trunc(x)    [Truncation](https://en.wikipedia.org/wiki/Truncation) to the nearest integer in the direction of zero                             all


{{Top}}

### Funciones estadísticas/agregadas 

[Aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function) take one or more arguments.
Individual arguments to aggregate functions may consist of ranges of cells. A range of cells is expressed as two cell references separated by a colon {{Incode|:}}, for example {{Incode|average(B1:B8)}} or {{Incode|sum(A1:A4; B1:B4)}}. The cell references may also use cell aliases, for example {{Incode|average(StartTemp:EndTemp)}}.

The following aggregate functions are supported:

  Function                 Description                                                                                                                          Input range
    
  average(a; b; c; \...)   [Average](https://en.wikipedia.org/wiki/Arithmetic_mean) value of the arguments, same as sum(a; b; c; \...) / count(a; b; c; \...)   all
  count(a; b; c; \...)     [Count](https://en.wikipedia.org/wiki/Counting) of the arguments, typically used for cell ranges                                     all
  max(a; b; c; \...)       [Maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                    all
  min(a; b; c; \...)       [Minimum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                    all
  stddev(a; b; c; \...)    [Standard deviation](https://en.wikipedia.org/wiki/standard_deviation) of the values of the arguments                                all
  sum(a; b; c; \...)       [Sum](https://en.wikipedia.org/wiki/Summation) of the values of the arguments, typically used for cell ranges                        all


{{Top}}

### String manipulation 

#### String identification 

Strings are identified in expressions by surrounding them with opening/closing double chevrons (as are labels).

In following example, \"TEXT\" is recognized as a string : `<<TEXT>>`

#### String concatenation 

Strings can be concatenated using the \'+\' sign.

Following example `<<MY>> + <<TEXT>>` will be concatenated to \"MYTEXT\".

#### String conversion 

Numerical values can be converted to strings with the `str` function:


`str(Box.Length.Value)`

#### String formatting 

String formatting is supported using the (old) %-style Python way.

All %-specifiers as defined in [Python documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

As an example, supposing you have a default 10mm-side cube named \'Box\' (default FreeCAD naming), the following expression `<<Cube length : %s>> % Box.Length` will expand to \"Cube length : 10.0 mm\"

For more than one %-specifier use the following syntax: `<<Cube length is %s and width is %s>> % tuple(Box.Length; Box.Width)`. Or use concatenation: `<<Cube length is %s>> % Box.Length + << and width is %s>> % Box.Width`. Both will expand to \"Cube length is 10.0 mm and width is 10.0 mm\".

A FreeCAD sample file using string formatting is available [in the forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) {{Top}}

### Create function 

The following objects may be created in expressions via the `create` function:

-   Vector
-   Matrix
-   Rotation
-   Placement

The `create` function passes subsequent arguments to the underlying Python constructor when creating the object.

Various mathematical operations such as multiplication, addition, and subtraction are supported via standard mathematical operators (e.g. `*`, `+`, `-`).

#### Vector

When `create` is passed `<<vector>>` as the 1st argument, the next 3 arguments are the X, Y, and Z coordinates for the `Vector` respectively.

Example:


`create(<<vector>>; 2; 1; 2)`

#### Matrix

When `create` is passed `<<matrix>>` as the 1st argument, the next 16 arguments are the elements for the `Matrix` in [row-major order](https://en.wikipedia.org/wiki/Row-_and_column-major_order).

Example:


`create(<<matrix>>; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16)`

#### Rotation

When `create` is passed `<<rotation>>` as the 1st argument, there are two ways to create a `Rotation`:

1\. Specify an axis vector and a rotation angle.

Example:


`create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45)`

2\. Specify 3 rotations about the X, Y, and Z axes as Euler angles.

Example:


`create(<<rotation>>; 30; 30; 30)`

#### Placement

When `create` is passed `<<placement>>` as the 1st argument, there are five ways to create a `Placement`.

These possible combinations are documented in the below table and are based on the [Placement API](Placement_API.md) page.

+++
| Number of arguments | Description                                              |
+=====================+==========================================================+
| 2                   |                                           |
|                     | `create(<<placement>>; Placement)`              |
|                     |                                                       |
+++
| 2                   |                                           |
|                     | `create(<<placement>>; Matrix)`                 |
|                     |                                                       |
+++
| 3                   |                                           |
|                     | `create(<<placement>>; Base; Rotation)`         |
|                     |                                                       |
+++
| 4                   |                                           |
|                     | `create(<<placement>>; Base; Rotation; Center)` |
|                     |                                                       |
+++
| 4                   |                                           |
|                     | `create(<<placement>>; Base; Axis; Angle)`      |
|                     |                                                       |
+++

The following example shows the syntax for creating a `Placement` from a `Base` (vector) and a `Rotation`:


`create(<<placement>>; create(<<vector>>; 2; 1; 2); create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45))`

For readability, you can define vectors and rotations in separate cells, and then reference the cells in your expression. {{Top}}

### Matrix functions 

#### mscale

Scale a `Matrix` with a given `Vector`.


`mscale(Matrix; Vector)`


`mscale(Matrix; x; y; z)`

#### minvert

Invert the given `Matrix`, `Rotation`, or `Placement`.


`minvert(Matrix)`


`minvert(Rotation)`


`minvert(Placement)`


{{Top}}

### Tuple & list 

You can create Python `tuple` or `list` objects via their respective functions.


`tuple(2; 1; 2)`


`list(2; 1; 2)`


{{Top}}

## Expresiones condicionales 

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

## Unidades

Units can be used directly in expressions. The parser connects them to the previous value. So `2mm` or `2 mm` is valid while `mm` is invalid because there is no preceding value.

All values must have a unit. Therefore you must in general use a unit for values in spreadsheets.
In some cases it works even without a unit, for example if you have e.g. in spreadsheet cell B1 just the number `1.5` and refer to it for a pad height. This only works because the pad height predefines the unit `mm` that is used if no unit is given. It will nevertheless fail if you use for the pad height e.g. `Sketch1.Constraints.Width - Spreadsheet.B1` because `Sketch1.Constraints.Width` has a unit and `Spreadsheet.B1` has not.

Units with exponents can directly be entered. So e.g. `mm^3` will be recognized as mm³ and `m^3` will be recognized as m³.

If you have a variable whose name is that of a unit you must put the variable between `<< >>` to prevent it from being recognized as a unit. For example if you have the dimension `Sketch.Constraints.A` it would be recognized as the unit ampere. Therefore you must write it in the expression as `Sketch.Constraints.<<A>>`.

The following units are recognized by the expression parser:

### Amount of substance 

  Unit   Description
   
  mol    [Mole](https://en.wikipedia.org/wiki/Mole_(unit))

### Angle

  Unit   Description
   
  °      [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit deg
  deg    [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit °
  rad    [Radian](https://en.wikipedia.org/wiki/Radian)
  gon    [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  S      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit ″
  ″      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit S
  M      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit ′
  ′      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit M

### Current

  Unit   Description
   
  mA     Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A      [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA     Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA     Mega[ampere](https://en.wikipedia.org/wiki/Ampere)

### Energy/work

  Unit   Description
   
  J      [Joule](https://en.wikipedia.org/wiki/Joule)
  Ws     [Watt second](https://en.wikipedia.org/wiki/Joule#Watt_second); alternative to the unit Joule
  VAs    [Volt-ampere-second](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule
  CV     [Coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternative to the unit Joule

### Force

  Unit   Description
   
  mN     Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N      [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN     Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN     Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf    [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))

### Length

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

### Luminous intensity 

  Unit   Description
   
  cd     [Candela](https://en.wikipedia.org/wiki/Candela)

### Mass

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

### Power

  Unit   Description
   
  W      [Watt](https://en.wikipedia.org/wiki/Watt)
  VA     [Volt-ampere](https://en.wikipedia.org/wiki/Volt-ampere)

### Pressure

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

### Temperature

  Unit   Description
   
  uK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit µK
  µK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit uK
  mK     Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K      [Kelvin](https://en.wikipedia.org/wiki/Kelvin)

### Time

  Unit   Description
   
  s      [Second](https://en.wikipedia.org/wiki/Second)
  min    [Minute](https://en.wikipedia.org/wiki/Minute)
  h      [Hour](https://en.wikipedia.org/wiki/Hour)

### Volume

  Unit   Description
   
  l      [Liter](https://en.wikipedia.org/wiki/Litre)

### Unsupported units 

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

## Caracteres y nombres no válidos 

The expression feature is very powerful but to achieve this power it has some limitations concerning some characters. To overcome this, FreeCAD offers to use labels and reference them instead of the object names. In labels you can use almost all special characters.

In cases where you cannot use a label, such as the name of a sketch\'s constraints, you must be aware what characters are not allowed.

### Etiquetas

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

### Nombres

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

## Referencia a los datos CAD 

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

## Variables globales de todo el documento 

There is no concept of global variables in FreeCAD at the moment. Instead, arbitrary variables can be defined as cells in a spreadsheet using the [Spreadsheet workbench](Spreadsheet_Workbench.md), and then be given a name using the alias property for the cell (right-click on cell). Then they can be accessed from any expression just as any other object property. {{Top}}

## Enlace entre documentos 

It is possible (with limitations) to define a Property of an object in your current document (\".FCstd\" file) by using an Expression to reference a Property of an object contained in a different document (\".FCstd\" file). For example, a cell in a spreadsheet or the **Length** of a Part Cube, etc. in one document can be defined by an Expression that references the X Placement value or another Property of an object contained in a different document.

A document\'s name is used to reference it from other documents. When saving a document the first time, you choose a file name; this is usually different from the initial default \"Unnamed1\" (or its translated equivalent). To prevent links being lost when the master document is renamed upon saving, it is recommended that you first create the master document, create a spreadsheet inside it, and save it. Subsequently, you can still make changes to the file and its spreadsheet but you should not rename it.

Once the master document with the spreadsheet is created and saved (named), it is safe to create dependent documents. For example, assuming you name the master document `master`, the spreadsheet `modelConstants`, and give a cell an alias-name `Length`, you can then access the value as:


`master#modelConstants.Length`

**Note:** that the master document must be loaded for the values in the master to be available to the dependent document.

Unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.

Of course, it\'s up to you to load the corresponding documents later when you want to change anything. {{Top}}

## Problemas conocidos / tareas pendientes 

-   The dependency graph is based on the relationship between document objects, not properties. This means that you cannot provide data to an object and query that same object for results. For example, even though there are no cyclic dependencies when the properties themselves are considered, you may not have an object which gets its dimensions from a spreadsheet and then display the volume of that object in the same spreadsheet. As a work-around use multiple spreadsheets, one to drive your model and the other for reporting.
-   The expression parser does not handle parentheses well, and is unable to properly parse some expressions. For example: `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` results in an error, while `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` is accepted. The expression `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` cannot be entered in any form.
-   As stated above, unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.
-   FreeCAD does not yet have a built-in expression manager where all expressions in a document are listed, and can be created, deleted, queried, etc. But an addon is available: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Open bugs/tickets for Expressions can be found in the [FreeCAD Bugtracker Expressions category](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Top}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/es
