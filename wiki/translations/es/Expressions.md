# Expressions/es
## Resumen


<div class="mw-translate-fuzzy">

Es posible definir propiedades utilizando expresiones matemáticas. En la interfaz gráfica de usuario, los cuadros de giro o campos de entrada que están vinculados a las propiedades contienen un icono azul <img alt="" src=images/Bound-expression.svg  style="width:24px;">. Haciendo clic en el icono o escribiendo el signo igual **&#61;** aparece el editor de expresiones para esa propiedad en particular.


</div>

Es una expresión matemática que usa la notación de los [operadores](#Supported_operators.md), [funciones](#Supported_functions.md) y [constantes predefinidas](#Supported_constants.md) matemáticas estándar como se describe a continuación. Además, la expresión puede hacer referencia a otras propiedades de objetos, y también utilizar [condicionales](#Conditional_expressions.md). Los números en una expresión pueden tener una [unidad](#Units.md) opcional adjunta.

Los números pueden usar ya sea una coma `,` o un punto decimal `.` para separar los dígitos enteros de los decimales. Cuando se usa el marcador decimal, *debe* ser seguido por al menos un dígito. Por lo tanto, las expresiones {{incode | 1.+2.}} y {{incode | 1,+2,}} son inválidas, pero {{incode | 1.0+2.0}} y {{incode | 1,0+2,0}} son válidas.

Los operadores y las funciones son conscientes de la unidad y requieren combinaciones válidas de unidades, si se suministran. Por ejemplo, {{incode | 2mm+4mm}} es una expresión válida, mientras que {{incode | 2mm+4}} no lo es. Esto también se aplica a las referencias a propiedades de objetos que tienen unidades, como las propiedades de longitud. Por lo tanto, `Pad001.Length + 1` es inválido ya que agrega un número puro a una propiedad con unidades de longitud, se requiere `Pad001.Length + 1mm`.

Algunos errores relacionados con las unidades pueden parecer poco intuitivos, ya que las expresiones se rechazan o producen resultados que no coinciden con las unidades de la propiedad que se establece. Aquí hay unos ejemplos:


`1/2mm`

no se interpreta como medio milímetro sino como `1/(2mm)`, lo que da como resultado: `0.5 mm^-1`.


`sqrt(2)mm`

no es válido porque la llamada a la función no es un número. Esto debe ingresarse como `sqrt(2) * 1mm`.



### Argumentos de la función 

Múltiples argumentos a una función pueden estar separados por un punto y coma  seguida por un espacio  {{incode |, }}. En el último caso, la coma se convierte a un punto y coma después de la entrada. Cuando se usa un punto y coma, no es necesario un espacio final.

Los argumentos pueden incluir referencias a las celdas en una hoja de cálculo. Una referencia de celda consiste en la letra mayúscula de fila de la celda seguida de su número de columna, por ejemplo {{incode | A1}}. También se puede hacer referencia a una celda utilizando el alias de la celda, por ejemplo, `Spreadsheet.MyPartWidth`.



### Referencia de objetos 

Como ya se mostró arribam puede hacer referencia a un objeto por su {{PropertyData | Name}}. Pero también puedes usar su {{PropertyData | Label}}. En el caso de un {{PropertyData | Label}}, debe estar encerrado en doble símbolos {{incode | <<}} y {{incode | >>}}, como {{incode | <<Label>>}}.

Puede referenciar cualquier propiedad de un objeto. Por ejemplo, para referenciar la altura de un Cilindro puede usar `Cylinder.Height` o `<<Label_of_cylinder>>.Height`.

Para más información de como referenciar objetos, vea [Referencia a los datos CAD](#Referencia_a_los_datos_CAD.md). 

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

Las [Funciones trigonométricas](https://es.wikipedia.org/wiki/Funci%C3%B3n_trigonom%C3%A9trica) utilizan el grado sexagesimal como unidad predeterminada. Para radianes, agregue primer valor de una expresión. Entonces, por ejemplo, `cos(45)` es lo mismo que `cos(pi rad / 4)`. Las expresiones en grados pueden usar `deg` o `°`, por ejemplo, `360deg - atan2(3; 4)` o `360&deg;  - atan2(3; 4)`. Si una expresión no tiene unidades y debe convertirse a grados o radianes para garantizar la compatibilidad, multiplíquela por `1deg`, `1°` o `1rad` como apropiado, por ejemplo, `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0,5 + pi / 2) * 1rad`.

++++
| Function               | Description                                                                                                                                                                       | Input range                                |
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



#### Funciones exponenciales y logarítmicas 

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



#### Funciones de redondeo, truncamiento y resto. 

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



### Funciones estadísticas/agregadas 

[Aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function) take one or more arguments.
Individual arguments to aggregate functions may consist of ranges of cells. A range of cells is expressed as two cell references separated by a colon {{Incode|:}}, for example {{Incode|average(B1:B8)}} or {{Incode|sum(A1:A4; B1:B4)}}. The cell references may also use cell aliases, for example {{Incode|average(StartTemp:EndTemp)}}.

Las siguientes funciones agregadas son soportadas:

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



### Manipulación de cadenas 



#### Identificación de cadena 

Las cadenas se identifican en las expresiones rodeándolas con comillas angulares dobles de apertura/cierre (al igual que las etiquetas).

En el siguiente ejemplo, \"TEXTO\" se reconoce como una cadena: `<<TEXTO>>`



#### Concatenación de cadenas 

Las cadenas se pueden concatenar usando el signo \'+\'.

El siguiente ejemplo `<<MI>> + <<TEXTO>>` se concatenará con \"MITEXTO\".



#### Conversión de cadenas 

Los valores numéricos se pueden convertir en cadenas con la función `str`:


`str(Box.Length.Value)`



#### Formato de cadena 

El formato de cadena se admite utilizando el estilo (antiguo) % de Python.

Todos los especificadores % tal como se definen en la [documentación de Python](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Como ejemplo, supongamos que tiene un cubo predeterminado de 10 mm de lado llamado \'Box\' (nombramiento predeterminado de FreeCAD), la siguiente expresión `<<Longitud del cubo: %s>> % Box.Length` se expandirá a \"Longitud del cubo: 10.0 mm\"

Para más de un especificador % utilice la siguiente sintaxis: `<<La longitud del cubo es %s y el ancho es %s>> % tuple(Box.Length; Box.Width)`. O use concatenación: `<<La longitud del cubo es %s>> % Box.Length + << y el ancho es %s>> % Box.Width`. Ambos se expandirán a \"La longitud del cubo es de 10.0 mm y el ancho es de 10.0 mm\".

Está disponible un archivo de muestra de FreeCAD que utiliza formato de cadena [en el foro](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) 

### Funciones de creación de objetos 

Los siguientes objetos se pueden crear en expresiones utilizando las siguientes funciones:

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
|                                                                |                                                                                    | Se puede proporcionar un mínimo de 1 argumento, como `matrix(1)`, que crea una matriz de identidad.                                                                                                                                                                                                              |
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



### Funciones vectoriales 


<div class="mw-translate-fuzzy">

Funciones: <small>(v0.22)</small> .


</div>

+++
| Function / Operator                 | Description                                                                                                                                                                         |
+=====================================+=====================================================================================================================================================================================+
|                      | Add two vectors.                                                                                                                                                                    |
| `v1 + v2`                  |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Subtract two vectors.                                                                                                                                                               |
| `v1 - v2`                  |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Uniformly scale a vector by `s`.                                                                                                                             |
| `v * s`                    |                                                                                                                                                                                     |
|                                  |                                                                                                                                                                                     |
+++
|                      | Angle between two vectors in degrees.                                                                                                                                               |
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



### Funciones matriciales 


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



## Expresiones condicionales 

Conditional expressions are of the form `condition ? resultTrue : resultFalse`. The condition is defined as an expression that evaluates to either `0` (false) or non-zero (true).

Note that to use a boolean property as the condition this syntax must be used: `VarSet.MyBool &#61;&#61; 1 ? 10 mm : 15 mm`.

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

Las unidades se pueden utilizar directamente en expresiones. El analizador los conecta con el valor anterior. Entonces `2mm` o `2 mm` es válido mientras que `mm` no es válido porque no hay un valor anterior.

All values must have a unit. Therefore you must in general use a unit for values in spreadsheets.
In some cases it works even without a unit, for example if you have e.g. in spreadsheet cell B1 just the number `1.5` and refer to it for a pad height. This only works because the pad height predefines the unit `mm` that is used if no unit is given. It will nevertheless fail if you use for the pad height e.g. `Sketch1.Constraints.Width - Spreadsheet.B1` because `Sketch1.Constraints.Width` has a unit and `Spreadsheet.B1` has not.

Se pueden ingresar directamente unidades con exponentes. Entonces, por ejemplo, `mm^3` se reconocerá como mm³ y `m^3` se reconocerá como m³.

Si tienes una variable cuyo nombre es el de una unidad debes poner la variable entre `<< >>` para evitar que sea reconocida como una unidad. Por ejemplo, si tiene la dimensión `Sketch.Constraints.A`, se reconocerá como la unidad amperio. Por lo tanto debes escribirlo en la expresión como `Sketch.Constraints.<<A>>`.

El analizador de expresiones reconoce las siguientes unidades:



### Cantidad de sustancia 

  Unit   Description
   
  mmol   Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol    [Mole](https://en.wikipedia.org/wiki/Mole_(unit))



### Ángulo

  Unit   Description
   
  °      [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit deg
  deg    [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternative to the unit °
  rad    [Radian](https://en.wikipedia.org/wiki/Radian)
  gon    [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  M      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternative to the unit ′
  ′      [Minute of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); this is the prime symbol (U+2032); alternative to the unit M
  S      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); **DOES NOT WORK**; alternative to the unit ″
  ″      [Second of arc](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); this is the double prime symbol (U+2033); alternative to the unit S



### Corriente

  Unit   Description
   
  mA     Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A      [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA     Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA     Mega[ampere](https://en.wikipedia.org/wiki/Ampere)



### Capacitancia electrica 

  Unit   Description
   
  pF     Pico[farad](https://en.wikipedia.org/wiki/Farad)
  nF     Nano[farad](https://en.wikipedia.org/wiki/Farad)
  uF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit µF
  µF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit uF
  mF     Milli[farad](https://en.wikipedia.org/wiki/Farad)
  F      [Farad](https://en.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg



### Carga eléctrica 

  Unit   Description
   
  C      [Coulomb](https://en.wikipedia.org/wiki/Coulomb); 1 C = 1 A\*s



### Conductividad eléctrica 

  Unit   Description
   
  uS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit µS
  µS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit uS
  mS     Milli[siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  S      [Siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS     Kilo[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  MS     Mega[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))



### Inductancia eléctrica 

  Unit   Description
   
  nH     Nano[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  uH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit µH
  µH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit uH
  mH     Milli[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  H      [Henry](https://en.wikipedia.org/wiki/Henry_(unit)); 1 H = 1 kg·m\^2/s\^2/A\^2



### Potencial eléctrico 

  Unit   Description
   
  mV     Milli[volt](https://en.wikipedia.org/wiki/Volt)
  V      [Volt](https://en.wikipedia.org/wiki/Volt)
  kV     Kilo[volt](https://en.wikipedia.org/wiki/Volt)



### Resistencia electrica 

  Unit   Description
   
  Ohm    [Ohm](https://en.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2
  kOhm   Kilo[ohm](https://en.wikipedia.org/wiki/Ohm)
  MOhm   Mega[ohm](https://en.wikipedia.org/wiki/Ohm)



### Energía/trabajo

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



### Fuerza

  Unit   Description
   
  mN     Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N      [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN     Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN     Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf    [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))



### Longitud

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



### Intensidad luminosa 

  Unit   Description
   
  cd     [Candela](https://en.wikipedia.org/wiki/Candela)



### Flujo magnético 

  Unit   Description
   
  Wb     [Weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A



### Densidad de flujo magnético 

  Unit   Description
   
  G      [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T
  T      [Tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A



### Masa

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



### Potencia

  Unit   Description
   
  W      [Watt](https://en.wikipedia.org/wiki/Watt)
  kW     Kilo[watt](https://en.wikipedia.org/wiki/Watt)



### Presión

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



### Temperatura

  Unit   Description
   
  uK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit µK
  µK     Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternative to the unit uK
  mK     Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K      [Kelvin](https://en.wikipedia.org/wiki/Kelvin)



### Tiempo

  Unit       Description
   
  s          [Second](https://en.wikipedia.org/wiki/Second)
  min        [Minute](https://en.wikipedia.org/wiki/Minute)
  h          [Hour](https://en.wikipedia.org/wiki/Hour)
  Hz (1/s)   [Hertz](https://en.wikipedia.org/wiki/Hertz)
  kHz        Kilo[hertz](https://en.wikipedia.org/wiki/Hertz),
  MHz        Mega[hertz](https://en.wikipedia.org/wiki/Hertz)
  GHz        Giga[hertz](https://en.wikipedia.org/wiki/Hertz)
  THz        Tera[hertz](https://en.wikipedia.org/wiki/Hertz)



### Volumen

  Unit   Description
   
  ml     Milli[liter](https://en.wikipedia.org/wiki/Litre)
  l      [Liter](https://en.wikipedia.org/wiki/Litre)
  cft    Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit))



### Unidades imperiales especiales 

  Unit   Description
   
  mph    [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour)
  sqft   [Square foot](https://en.wikipedia.org/wiki/Square_foot)



### Unidades no compatibles 

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

See [Spreadsheet SetAlias](Spreadsheet_SetAlias#Usage.md). 

## Referencia a los datos CAD 

It is possible to use data from the model itself in an expression. To reference a property use `object_name.property` or `<<object_label>>.property`, labels must be enclosed in `<<` and `>>`. If you want to use labels they must be unique.

All next examples reference the object by its name, but in all cases the object label can also be used.

If the property is a compound of fields, the individual fields can be accessed as `object_name.property.field`.

Para referenciar una lista de objetos use `object_label.list[list_index]`. Si quiere por ejemplo referenciar una restricción de un croquis use `Sketch.Constraints[16]`. Si está en el mismo croquis puede omitir su nombre y solo usar `Constraints[16]`.Note que el índice inicia en 0, por lo que la restricción 17 tiene que ser referenciada como `Constraints[16]`

To reference the object itself use the `_self` pseudo property: `object_name._self`.

The following table shows some more examples:

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

### Cyclic dependencies 

FreeCAD checks dependencies based on the relationship between document objects, not properties. This means that you cannot provide data to an object and query that same object for results. For example, even though there are no cyclic dependencies when the properties themselves are considered, you may not have an object which gets its dimensions from a spreadsheet and then display the volume of that object in the same spreadsheet. You have to use two spreadsheets, one to drive your model and the other for reporting.

As a workaround it is possible to display a cell range from the second spreadsheet in the first (or vice versa) by creating a [cell binding](Spreadsheet_Workbench#Cell_binding.md) with the **Hide dependency of binding** option.

Another way to workaround cyclic dependencies is to hide the reference by using the `href` or `hiddenref` function for individual expressions, for example: `href(Box.Length)`.

Please note that both mentioned workarounds should be used with caution, and that they do not work if the properties that are reported depend on dimensions that are driven from the same spreadsheet. 

## Variables globales de todo el documento 

There is no concept of global variables in FreeCAD at the moment. Instead, arbitrary variables can be defined as cells in a spreadsheet using the [Spreadsheet workbench](Spreadsheet_Workbench.md), and then be given a name using the alias property for the cell (right-click on cell). Then they can be accessed from any expression just as any other object property. 

## Enlace entre documentos 

It is possible (with limitations) to define a Property of an object in your current document (\".FCstd\" file) by using an Expression to reference a Property of an object contained in a different document (\".FCstd\" file). For example, a cell in a spreadsheet or the **Length** of a Part Cube, etc. in one document can be defined by an Expression that references the X Placement value or another Property of an object contained in a different document.

A document\'s name is used to reference it from other documents. When saving a document the first time, you choose a file name; this is usually different from the initial default \"Unnamed1\" (or its translated equivalent). To prevent links being lost when the master document is renamed upon saving, it is recommended that you first create the master document, create a spreadsheet inside it, and save it. Subsequently, you can still make changes to the file and its spreadsheet but you should not rename it.

Once the master document with the spreadsheet is created and saved (named), it is safe to create dependent documents. For example, assuming you name the master document `master`, the spreadsheet `modelConstants`, and give a cell an alias-name `Length`, you can then access the value as:


`master#modelConstants.Length`

Note that the master document must be loaded for the values in the master to be available to the dependent document.

Of course, it\'s up to you to load the corresponding documents later when you want to change anything. 

## Problemas conocidos / tareas pendientes 

-   FreeCAD does not yet have a built-in expression manager where all expressions in a document are listed, and can be created, deleted, queried, etc. But an addon is available: [fcxref expression manager](https://github.com/gbroques/fcxref).
-   Open bugs/tickets for Expressions can be found on [GitHub](https://github.com/FreeCAD/FreeCAD/labels/Topic%3A%20Expressions).


{{Top}}

## Scripting


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
⏵ [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/es
