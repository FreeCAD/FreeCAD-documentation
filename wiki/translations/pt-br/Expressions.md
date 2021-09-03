 {{TOCright}}

## Visão geral {#visão_geral}

It is possible to define properties using mathematical expressions. In the GUI, spin boxes or input fields that are bound to properties contain a blue icon <img alt="" src=images/Sketcher_Expressions.png  style="width:24px;">. Clicking on the icon or typing the equal sign **&#61;** brings up the expression editor for that particular property.

A FreeCAD expression is a mathematical expression following notation for the standard mathematical operators and functions as described below. In addition, the expression may reference other properties, and also use conditionals. Numbers in an expression may have an optional unit attached to them.

Numbers may use either a comma `,` or a decimal point `.` separating whole digits from decimals. When the decimal marker is used, it *must* be followed by at least one digit. Thus, the expressions `1.+2.` and `1,+2,` are invalid, but `1.0 + 2.0` and `1,0 + 2,0` are valid.

Operators and functions are unit-aware, and require valid combinations of units, if supplied. For example, `2mm + 4mm` is a valid expression, while `2mm + 4` is not (the reason for this is that an expression like `1in + 4` will most likely be interpreted as `1in + 4in` by humans, but all units are converted to the SI system internally, and the system is not able to guess this). These [units](#Units.md) are currently recognized.

You can use [predefined constants](#Supported_constants.md) and [functions](#Supported_functions.md).

### Function Arguments {#function_arguments}

Multiple arguments to a function may be separated by either a semicolon followed by a space `, `. In the latter case, the comma is converted to a semicolon after entry. When a semicolon is used, no trailing space is necessary.

Arguments may include references to cells in a spreadsheet. A cell reference consists of the cell\'s uppercase row letter followed by its column number, for example `A1`. A cell may also be referenced by using the cell\'s alias instead, for example `Spreadsheet.MyPartWidth`.

### Referencing objects {#referencing_objects}

You can reference an object by its **Name** or by its **Label**. In the case of a **Label**, it must be enclosed in double `<<` and `>>` symbols, such as `<<Label>>`.

You can reference any numerical property of an object. For example, to reference a Cylinder\'s height, you may use `Cylinder.Height` or `<<Long_name_of_cylinder>>.Height`.

To reference list objects, use `<<object_label>>.list[list_index]` or `object_name.list[list_index]`. If you want for example to reference a constraint in a sketch, use `<<MySketch>>.Constraints[16]`. If you are in the same sketch you may omit its name and just use `Constraints[16]`.
**Note:** The index starts with 0, therefore constraint 17 has the index 16.

For more information about referencing objects, see [Reference to CAD\_data](#Reference_to_CAD_data.md).

## Supported constants {#supported_constants}

The following constants are supported:

  Constant   Description
  ---------- ----------------------------------------------------------------------------
  **e**      [Euler\'s number](https://en.wikipedia.org/wiki/E_(mathematical_constant))
  **pi**     [Pi](https://en.wikipedia.org/wiki/Pi)

## Supported operators {#supported_operators}

The following operators are supported:

  Operator   Description
  ---------- ---------------------------------------------------------------------------------
  **+**      [Addition](https://en.wikipedia.org/wiki/Addition)
  **-**      [Subtraction](https://en.wikipedia.org/wiki/Subtraction)
  **\***     [Multiplication](https://en.wikipedia.org/wiki/Multiplication)
  **/**      Floating point [Division](https://en.wikipedia.org/wiki/Division_(mathematics))
  **%**      [Remainder](https://en.wikipedia.org/wiki/Remainder)
  **\^**     [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)

## Supported functions {#supported_functions}

### General mathematical functions {#general_mathematical_functions}

The mathematical functions listed below are available.

[Trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions) use degree as their default unit. For radian measure, add first value in an expression. So e.g. `cos(45)` is the same as `cos(pi rad / 4)`. Expressions in degrees can use either `deg` or `°`, e.g. `360deg - atan2(3; 4)` or `360&deg; - atan2(3; 4)`. If an expression is without units and needs to be converted to degrees or radians for compatibility, multiply by `1&nbsp;deg`, `1&nbsp;°` or `1&nbsp;rad` as appropriate, e.g. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.
These trigonometric functions are supported:

  Function      Description                                                                                              Value range
  ------------- -------------------------------------------------------------------------------------------------------- ------------------------------------------
  acos(x)       [Arc cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)             -1 \<= x \<= 1
  asin(x)       [Arc sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)               -1 \<= x \<= 1
  atan(x)       [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)            all
  atan2(x, y)   [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties) of *x/y*   all, except y = 0
  cos(x)        [Cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)        all
  cosh(x)       [Hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)         all
  sin(x)        [Sine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)          all
  sinh(x)       [Hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)           all
  tan(x)        [Tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)       all, except of x = n·90 with n = integer
  tanh(x)       [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)        all

These functions for exponentiation and logarithmization are supported:

  Function    Description                                                                                    Value range
  ----------- ---------------------------------------------------------------------------------------------- -------------
  exp(x)      [Exponential function](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition)   all
  log(x)      [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)                           x \> 0
  log10(x)    [Common logarithm](https://en.wikipedia.org/wiki/Common_logarithm)                             x \> 0
  pow(x, y)   [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                                 all
  sqrt(x)     [Square root](https://en.wikipedia.org/wiki/Square_root)                                       x \>= 0

These functions for rounding, truncation and remainder are supported:

  Function    Description                                                                                                                        Value range
  ----------- ---------------------------------------------------------------------------------------------------------------------------------- -------------------
  abs(x)      [Absolute value](https://en.wikipedia.org/wiki/Absolute_value)                                                                     all
  ceil(x)     [Ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), smallest integer value greater than or equal to x   all
  floor(x)    [Floor function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), largest integer value less than or equal to x         all
  mod(x, y)   [Remainder](https://en.wikipedia.org/wiki/Remainder) after dividing *x* by *y*                                                     all, except y = 0
  round(x)    [Rounding](https://en.wikipedia.org/wiki/Rounding) to the nearest integer                                                          all
  trunc(x)    [Truncation](https://en.wikipedia.org/wiki/Truncation) to the nearest integer in the direction of zero                             all

### Statistical / aggregate functions {#statistical_aggregate_functions}

[Aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function) take one or more arguments.
Individual arguments to aggregate functions may consist of ranges of cells. A range of cells is expressed as two cell references separated by a colon {{Incode|:}}, for example {{Incode|average(B1:B8)}} or {{Incode|sum(A1:A4; B1:B4)}}. The cell references may also use cell aliases, for example {{Incode|average(StartTemp:EndTemp)}} <small>(v0.19)</small> .

These aggregate functions are supported:

  Function                 Description                                                                                                                          Value range
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------ -------------
  average(a; b; c; \...)   [Average](https://en.wikipedia.org/wiki/Arithmetic_mean) value of the arguments; same as sum(a; b; c; \...) / count(a; b; c; \...)   all
  count(a; b; c; \...)     [Count](https://en.wikipedia.org/wiki/Counting) of the arguments; typically used for cell ranges                                     all
  max(a; b; c; \...)       [Maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                    all
  min(a; b; c; \...)       [Minimum](https://en.wikipedia.org/wiki/Maxima_and_minima) value of the arguments                                                    all
  stddev(a; b; c; \...)    [Standard deviation](https://en.wikipedia.org/wiki/standard_deviation) of the values of the arguments                                all
  sum(a; b; c; \...)       [Sum](https://en.wikipedia.org/wiki/Summation) of the values of the arguments; typically used for cell ranges                        all

### String manipulation {#string_manipulation}

#### String identification {#string_identification}

Strings are identified in expressions by surrounding them with opening/closing double chevrons (as are labels).

In following example, \"TEXT\" is recognized as a string : `<<TEXT>>`

#### String concatenation {#string_concatenation}

Strings can be concatenated using the \'+\' sign.

Following example `<<MY>> + <<TEXT>>` will be concatenated to \"MYTEXT\".

#### String formatting {#string_formatting}

String formatting is supported using the (old) %-style Python way.

All %-specifiers as defined in [Python documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

As an example, supposing you have a default 10mm-side cube named \'Box\' \--default FreeCAD naming\--, following expression `<<Cube length : %s>> % Box.Length` will expand to \"Cube length : 10.0 mm\"

A limitation is that only one %-specifier is allowed in string, thus you have to use string concatenation if more than one is needed. With same above situation, expression `<<Cube length is %s>> % Box.Length + << and width is %s>> % Box.Width` will expand to \"Cube length is 10.0 mm and width is 10.0 mm\".

A FreeCAD sample file using string formatting is available [in the forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657)

## Conditional expressions {#conditional_expressions}

Conditional expressions are of the form `condition ? resultTrue : resultFalse`. The condition is defined as an expression that evaluates to either `0` (false) or non-zero (true). Note that enclosing the conditional expression in parentheses is currently considered an error. {{VersionMinus|0.19}}

The following [relational operators](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators) are defined:

  Unit      Description
  --------- --------------------------
  **==**    equal to
  **!=**    not equal to
  **\>**    greater than
  **\<**    less than
  **\>=**   greater than or equal to
  **\<=**   less than or equal to

## Units

Units can be used directly in expressions. The parser connects them to the previous value. So `2mm` or `2 mm` is valid while `mm` is invalid because there is no preceding value.

All values must have a unit. Therefore you must in general use a unit for values in spreadsheets.
In some cases it works even without a unit, for example if you have e.g. in spreadsheet cell B1 just the number `1.5` and refer to it for a pad height. This only works because the pad height predefines the unit `mm` that is used if no unit is given. It will nevertheless fail if you use for the pad height e.g. `Sketch1.Constraints.Width - Spreadsheet.B1` because `Sketch1.Constraints.Width` has a unit and `Spreadsheet.B1` has not.

Units with exponents can directly be entered. So e.g. `mm^3` will be recognized as mm³ and `m^3` will be recognized as m³.

If you have a variable whose name is that of a unit you must put the variable between `<< >>` to prevent it from being recognized as a unit. For example if you have the dimension `Sketch.Constraints.A` it would be recognized as the unit ampere. Therefore you must write it in the expression as `Sketch.Constraints.<<A>>`.

The following units are recognized by the expression parser:

Amount of substance:

  Unit   Description
  ------ --------------------------------------------------------
  mmol   Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol    [Mole](https://en.wikipedia.org/wiki/Mole_(unit))

Angle:

  Unit   Description
  ------ ------------------------------------------------------------------------------------------------------
  °      [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit *deg*
  deg    [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit *°*
  rad    [Radian](https://en.wikipedia.org/wiki/Radian)
  gon    [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  S      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc)
  ″      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit *S*
  M      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc)
  ′      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit *M*

Current:

  Unit   Description
  ------ -----------------------------------------------------
  mA     Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A      [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA     Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA     Mega[ampere](https://en.wikipedia.org/wiki/Ampere)

Electrical capacitance:

  Unit   Description
  ------ -----------------------------------------------------------------------------------------------------------------
  pF     Pico[farad](https://en.wikipedia.org/wiki/Farad), <small>(v0.19)</small> 
  nF     Nano[farad](https://en.wikipedia.org/wiki/Farad), <small>(v0.19)</small> 
  uF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit *µF*, <small>(v0.19)</small> 
  µF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit *uF*, <small>(v0.19)</small> 
  mF     Milli[farad](https://en.wikipedia.org/wiki/Farad), <small>(v0.19)</small> 
  F      [Farad](https://en.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg, <small>(v0.19)</small> 

Electrical conductance:

  Unit   Description
  ------ ----------------------------------------------------------------------------------------------------------------------------
  uS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit *µS*, <small>(v0.19)</small> 
  µS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit *uS*, <small>(v0.19)</small> 
  mS     Milli[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)), <small>(v0.19)</small> 
  S      [Siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); 1 S = 1 s\^3·A\^2/kg/m\^2, <small>(v0.19)</small> 
  kS     Kilo[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)), <small>(v0.20)</small> 
  MS     Mega[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)), <small>(v0.20)</small> 

Electrical inductance:

  Unit   Description
  ------ ------------------------------------------------------------------------------------------------------------------------
  nH     Nano[henry](https://en.wikipedia.org/wiki/Henry_(unit)), <small>(v0.19)</small> 
  uH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit *µH*, <small>(v0.19)</small> 
  µH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit *uH*, <small>(v0.19)</small> 
  mH     Milli[henry](https://en.wikipedia.org/wiki/Henry_(unit)), <small>(v0.19)</small> 
  H      [Henry](https://en.wikipedia.org/wiki/Henry_(unit)); 1 H = 1 kg·m\^2/s\^2/A\^2, <small>(v0.19)</small> 

Electrical resistance:

  Unit   Description
  ------ -------------------------------------------------------------------------------------------------------
  Ohm    [Ohm](https://en.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2, <small>(v0.19)</small> 
  kOhm   Kilo[ohm](https://en.wikipedia.org/wiki/Ohm), <small>(v0.19)</small> 
  MOhm   Mega[ohm](https://en.wikipedia.org/wiki/Ohm), <small>(v0.19)</small> 

Electric charge:

  Unit   Description
  ------ -----------------------------------------------------------------------------------------------
  C      [Coulomb](https://en.wikipedia.org/wiki/Coulomb); 1 C = 1 A·s, <small>(v0.19)</small> 

Electric potential:

  Unit   Description
  ------ -------------------------------------------------
  mV     Milli[volt](https://en.wikipedia.org/wiki/Volt)
  V      [Volt](https://en.wikipedia.org/wiki/Volt)
  kV     Kilo[volt](https://en.wikipedia.org/wiki/Volt)

Energy / work:

  Unit   Description
  ------ ----------------------------------------------------------------------------------------------------------------------
  mJ     Milli[joule](https://en.wikipedia.org/wiki/Joule)
  J      [Joule](https://en.wikipedia.org/wiki/Joule)
  kJ     Kilo[joule](https://en.wikipedia.org/wiki/Joule), <small>(v0.19)</small> 
  eV     [Electronvolt](https://en.wikipedia.org/wiki/Electronvolt); 1 ev = 1.602176634e-19 J, <small>(v0.19)</small> 
  keV    Kilo[electronvolt](https://en.wikipedia.org/wiki/Electronvolt), <small>(v0.19)</small> 
  MeV    Mega[electronvolt](https://en.wikipedia.org/wiki/Electronvolt), <small>(v0.19)</small> 
  kWh    [Kilowatt hour](https://en.wikipedia.org/wiki/Kilowatt_hour); 1 kWh = 3.6e6 J, <small>(v0.19)</small> 
  Ws     [Watt second](https://en.wikipedia.org/wiki/Joule#Watt_second); alternative to the unit *Joule*
  VAs    [Volt-ampere-second](https://en.wikipedia.org/wiki/Joule); alternative to the unit *Joule*
  CV     [Coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternative to the unit *Joule*
  cal    [Calorie](https://en.wikipedia.org/wiki/Calorie); 1 cal = 4.184 J, <small>(v0.19)</small> 
  kcal   Kilo[calorie](https://en.wikipedia.org/wiki/Calorie), <small>(v0.19)</small> 

Force:

  Unit   Description
  ------ ---------------------------------------------------------------
  mN     Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N      [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN     Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN     Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf    [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))

Length:

  Unit   Description
  ------ --------------------------------------------------------------------------------------------------------------
  nm     Nano[meter](https://en.wikipedia.org/wiki/Metre)
  mu     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit *µm*
  µm     Micro[meter](https://en.wikipedia.org/wiki/Metre); alternative to the unit *mu*
  mm     Milli[meter](https://en.wikipedia.org/wiki/Metre)
  cm     Centi[meter](https://en.wikipedia.org/wiki/Metre)
  dm     Deci[meter](https://en.wikipedia.org/wiki/Metre)
  m      [Meter](https://en.wikipedia.org/wiki/Metre)
  km     Kilo[meter](https://en.wikipedia.org/wiki/Metre)
  mil    [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative to the unit *thou*
  thou   [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternative to the unit *mil*
  in     [Inch](https://en.wikipedia.org/wiki/Inch)
  ft     [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternative to the unit \'
  \'     [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternative to the unit *ft*
  yd     [Yard](https://en.wikipedia.org/wiki/Yard)
  mi     [Mile](https://en.wikipedia.org/wiki/Mile)

Luminous intensity:

  Unit   Description
  ------ --------------------------------------------------
  cd     [Candela](https://en.wikipedia.org/wiki/Candela)

Magnetic field strength:

  Unit   Description
  ------ -------------------------------------------------------------------------------------------------------
  Oe     [Oersted](https://en.wikipedia.org/wiki/Oersted); 1 Oe = 79.57747 A/m, <small>(v0.19)</small> 

Magnetic flux:

  Unit   Description
  ------ ---------------------------------------------------------------------------------------------------------------
  Wb     [Weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A, <small>(v0.19)</small> 

Magnetic flux density:

  Unit   Description
  ------ --------------------------------------------------------------------------------------------------------
  G      [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T, <small>(v0.19)</small> 
  T      [Tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A, <small>(v0.19)</small> 

Mass:

  Unit   Description
  ------ ------------------------------------------------------------------------------------
  ug     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit *µg*
  µg     Micro[gram](https://en.wikipedia.org/wiki/Gram); alternative to the unit *ug*
  mg     Milli[gram](https://en.wikipedia.org/wiki/Gram)
  g      [Gram](https://en.wikipedia.org/wiki/Gram)
  kg     Kilo[gram](https://en.wikipedia.org/wiki/Gram)
  t      [Tonne](https://en.wikipedia.org/wiki/Tonne)
  oz     [Ounce](https://en.wikipedia.org/wiki/Ounce)
  lb     [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit *lbm*
  lbm    [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternative to the unit *lb*
  st     [Stone](https://en.wikipedia.org/wiki/Stone_(weight))
  cwt    [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)

Power:

  Unit   Description
  ------ --------------------------------------------------------------------------------
  W      [Watt](https://en.wikipedia.org/wiki/Watt)
  kW     Kilo[watt](https://en.wikipedia.org/wiki/Watt), <small>(v0.19)</small> 
  VA     [Volt-ampere](https://en.wikipedia.org/wiki/Volt-ampere)

Pressure:

  Unit    Description
  ------- -------------------------------------------------------------------------------------------------------------------------
  Pa      [Pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  kPa     Kilo[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  MPa     Mega[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  GPa     Giga[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  mbar    Milli[Bar](https://en.wikipedia.org/wiki/Bar_(unit)), <small>(v0.19)</small> 
  bar     [Bar](https://en.wikipedia.org/wiki/Bar_(unit)), <small>(v0.19)</small> 
  uTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit *µTorr*
  µTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternative to the unit *uTorr*
  mTorr   Milli[torr](https://en.wikipedia.org/wiki/Torr)
  Torr    [Torr](https://en.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [Pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch); 1 psi = 6.895 kPa
  ksi     Kilo[pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch)
  Mpsi    Mega[pound-force per square inch](https://en.wikipedia.org/wiki/Pounds_per_square_inch), <small>(v0.19)</small> 

Temperature:

  Unit   Description
  ------ -----------------------------------------------------------------------------------
  uK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit *µK*
  µK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit *uK*
  mK     Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K      [Kelvin](https://en.wikipedia.org/wiki/Kelvin)

Time:

  Unit       Description
  ---------- ----------------------------------------------------------------------------------
  s          [Second](https://en.wikipedia.org/wiki/Second)
  min        [Minute](https://en.wikipedia.org/wiki/Minute)
  h          [Hour](https://en.wikipedia.org/wiki/Hour)
  Hz (1/s)   [Hertz](https://en.wikipedia.org/wiki/Hertz), <small>(v0.19)</small> 
  kHz        Kilo[hertz](https://en.wikipedia.org/wiki/Hertz), <small>(v0.19)</small> 
  MHz        Mega[hertz](https://en.wikipedia.org/wiki/Hertz), <small>(v0.19)</small> 
  GHz        Giga[hertz](https://en.wikipedia.org/wiki/Hertz), <small>(v0.19)</small> 
  THz        Tera[hertz](https://en.wikipedia.org/wiki/Hertz), <small>(v0.19)</small> 

Volume:

  Unit   Description
  ------ ----------------------------------------------------------------------------------------
  ml     Milli[liter](https://en.wikipedia.org/wiki/Litre), <small>(v0.19)</small> 
  l      [Liter](https://en.wikipedia.org/wiki/Litre)
  cft    Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit)), <small>(v0.19)</small> 

Special imperial units:

  Unit   Description
  ------ ------------------------------------------------------------------------------------------------
  mph    [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour), <small>(v0.19)</small> 
  sqft   [Square foot](https://en.wikipedia.org/wiki/Square_foot), <small>(v0.19)</small> 

The following commonly used units are not yet supported:

  Unit   Description                                                                                                  Alternative
  ------ ------------------------------------------------------------------------------------------------------------ --------------------------
  °C     [Celsius](https://en.wikipedia.org/wiki/Celsius)                                                             \[°C\] + 273.15 K
  °F     [Fahrenheit](https://en.wikipedia.org/wiki/Fahrenheit);                                                      (\[°F\] + 459.67) × ​5/9
  u      [Atomic mass unit](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit \'Da\'   1.66053906660e-27 kg
  Da     [Dalton](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit \'u\'              1.66053906660e-27 kg
  sr     [Steradian](https://en.wikipedia.org/wiki/Steradian)                                                         not directly
  lm     [Lumen](https://en.wikipedia.org/wiki/Lumen_(unit))                                                          not directly
  lx     [Lux](https://en.wikipedia.org/wiki/Lux)                                                                     not directly
  px     [Pixel](https://en.wikipedia.org/wiki/Pixel)                                                                 not directly

## Invalid characters and names {#invalid_characters_and_names}

The expression feature is very powerful but to achieve this power it has some limitations concerning some characters. To overcome this, FreeCAD offers to use labels and reference them instead of the object names. In labels you can use almost all special characters.

In cases where you cannot use a label, such as the name of a sketch\'s constraints, you must be aware what characters are not allowed.

### Labels

For [labels](Object_name#Label.md) there are no invalid characters, however some characters need to be escaped:

+----------------------------------------------------------+---------------------------------------------------------------------------+
| Characters                                               | Description                                                               |
+==========================================================+===========================================================================+
|                                           | Need to be escaped by adding `\` in front of them. |
| `'`                                             |                                                                           |
|                                                       |                                                                           |
| , `\`, `"` |                                                                           |
+----------------------------------------------------------+---------------------------------------------------------------------------+

For example, the label `Sketch\002` must be referenced as `<<Sketch\\002>>`.

### Names

[Names](Object_name#Name.md) of objects like dimensions, sketches, etc. may not have the characters or character sequences listed below, otherwise the name is invalid:

  Characters / Character sequences                                                                                                              Description
  --------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**                  Characters that are math operators or part of mathematical constructs
  **A**, **kA**, **mA**, **MA**, **C**, **G**, **F**, **uF**, **µF**, **J**, **K**, \'\'\' \' \'\'\', \'\'\' ft \'\'\', **°**, and many more!   Characters and character sequences that are [units](Expressions#Units.md)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, and many more!                         Characters used as placeholder or to trigger special operations
  **pi**, **e**                                                                                                                                 Mathematical constants
  **´**, **\**, \'\'\' \' \'\'\', **\"**                                                                                                       Characters used for accents
  space                                                                                                                                         A space defines the end of a name and can therefore not be used

For example, the following name is valid: `<<Sketch>>.Constraints.T2üßµ@`. While these are invalid names: `<<Sketch>>.Constraints.test\result_2` (\\r means \"carriage return\") or `<<Sketch>>.Constraints.mol` (mol is a unit).

Since shorter names (especially if they have only one or two characters) can easily result in invalid names, consider using longer names and/or establishing a suitable naming convention.

### Cell aliases {#cell_aliases}

For [spreadsheet cell aliases](Spreadsheet_SetAlias.md) only alphanumeric characters and underscores (`A` to `Z`, `a` to `z`, `0` to `9` and `_`) are allowed.

## Reference to CAD data {#reference_to_cad_data}

It is possible to use data from the model itself in an expression. To reference a property use`object.property`. If the property is a compound of fields, the individual fields can be accessed as `object.property.field`.

The following table shows some examples:

+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CAD data                                   | Call in expression                    | Result                                                                                                                                                                       |
+============================================+=======================================+==============================================================================================================================================================================+
| Parametric Length of a Part-Workbench Cube |                        | Length with units mm                                                                                                                                                         |
|                                            | `Cube.Length`                |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume of the Cube                         |                        | Volume in mm³ without units                                                                                                                                                  |
|                                            | `Cube.Shape.Volume`          |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Type of the Cube-shape                     |                        | String: Solid                                                                                                                                                                |
|                                            | `Cube.Shape.ShapeType`       |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Label of the Cube                          |                        | String: Label                                                                                                                                                                |
|                                            | `Cube.Label`                 |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| x-coordinate of center of mass of the Cube |                        | x-coordinate in mm without units                                                                                                                                             |
|                                            | `Cube.Shape.CenterOfMass.x`  |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value of constraint in a sketch            |                        | Numeric value of the named constraint `Width` in the sketch, if the expression is used in the sketch itself.                                          |
|                                            | `Constraints.Width`          |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value of constraint in a sketch            |                        | Numeric value of the named constraint `Width` in the sketch, if the expression is used outside of the sketch.                                         |
|                                            | `MySketch.Constraints.Width` |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value of a spreadsheet alias               |                        | Value of the alias `Depth` in the spreadsheet `Spreadsheet`                                                                    |
|                                            | `Spreadsheet.Depth`          |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value of a local property                  |                        | Value of the **Length** property in e.g a Pad object, if the expression is used in e.g **Length2** in the same object. |
|                                            | `Length`                     |                                                                                                                                                                              |
|                                            |                                    |                                                                                                                                                                              |
+--------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Document-wide global variables {#document_wide_global_variables}

There is no concept of global variables in FreeCAD at the moment. Instead, arbitrary variables can be defined as cells in a spreadsheet using the [Spreadsheet workbench](Spreadsheet_Workbench.md), and then be given a name using the alias property for the cell (right-click on cell). Then they can be accessed from any expression just as any other object property.

## Cross-document linking {#cross_document_linking}

It is possible (with limitations) to define a Property of an object in your current document (\".FCstd\" file) by using an Expression to reference a Property of an object contained in a different document (\".FCstd\" file). For example, a cell in a spreadsheet or the **Length** of a Part Cube, etc. in one document can be defined by an Expression that references the X Placement value or another Property of an object contained in a different document.

A document\'s name is used to reference it from other documents. When saving a document the first time, you choose a file name; this is usually different from the initial default \"Unnamed1\" (or its translated equivalent). To prevent links being lost when the master document is renamed upon saving, it is recommended that you first create the master document, create a spreadsheet inside it, and save it. Subsequently, you can still make changes to the file and its spreadsheet but you should not rename it.

Once the master document with the spreadsheet is created and saved (named), it is safe to create dependent documents. For example, assuming you name the master document `master`, the spreadsheet `modelConstants`, and give a cell an alias-name `Length`, you can then access the value as:

`master#modelConstants.Length`

**Note:** that the master document must be loaded for the values in the master to be available to the dependent document.

Unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.

Of course, it\'s up to you to load the corresponding documents later when you want to change anything.

## Known issues / remaining tasks {#known_issues_remaining_tasks}

-   The dependency graph is based on the relationship between document objects, not properties. This means that you cannot provide data to an object and query that same object for results. For example, even though there are no cyclic dependencies when the properties themselves are considered, you may not have an object which gets its dimensions from a spreadsheet and then display the volume of that object in the same spreadsheet. As a work-around use multiple spreadsheets, one to drive your model and the other for reporting.
-   The expression parser does not handle parentheses well, and is unable to properly parse some expressions. For example: `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` results in an error, while `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` is accepted. The expression `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` cannot be entered in any form.
-   As stated above, unfortunately, the integrated checker sometimes claims that a valid name doesn\'t exist. Continue typing anyway. When you have completed the full reference, the **OK** button will become active.
-   FreeCAD does not yet have a built-in expression manager where all expressions in a document are listed, and can be created, deleted, queried, etc. But an addon is available: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Open bugs/tickets for Expressions can be found in the [FreeCAD Bugtracker Expressions category](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Powerdocnavi

}} 

[Category:Spreadsheet{{\#translation:}}](Category:Spreadsheet.md)
