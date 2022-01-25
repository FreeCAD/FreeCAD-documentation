# Expressions/it
{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

È possibile definire le proprietà utilizzando espressioni matematiche. Nella GUI, gli spin box o i campi di input che sono legati alle proprietà contengono un\'icona blu <img alt="" src=images/Bound-expression.svg  style="width:24px;">. Cliccando sull\'icona, oppure digitando il segno di uguale **&#61;**, si porta in primo piano l\'editor delle espressioni per quella particolare proprietà.


</div>

Una espressione di FreeCAD è un\'espressione matematica che segue la notazione per gli operatori matematici standard e le funzioni come descritto in seguito. Inoltre, l\'espressione può fare riferimento ad altre proprietà, e anche utilizzare le condizioni. I numeri di un\'espressione possono opzionalmente essere collegati ad una unità di misura.


<div class="mw-translate-fuzzy">

I numeri possono usare una virgola \',\' o un punto \'.\' per separare le cifre intere dai decimali. Quando viene utilizzato il separatore decimale, esso \"deve\" essere seguito da almeno una cifra. Pertanto, le espressioni **1.+2.** e **1,+2,** non sono valide, ma **1.0+2.0** e **1,0+2,0** sono validi.


</div>


<div class="mw-translate-fuzzy">

Gli operatori e le funzioni sono unit-aware (consapevoli delle unità), e richiedono combinazioni di unità valide, se sono fornite. Ad esempio, **2mm + 4mm** è un\'espressione valida, mentre **2mm + 4** non lo è (il motivo di questo è che un\'espressione come **1in + 4** molto probabilmente viene interpretata come **1in + 4in** da un umano, ma tutte le unità vengono convertite nel sistema SI interno, e il sistema non è in grado di indovinare questo). Queste [unità](#Unità.md) sono attualmente riconosciute.


</div>


<div class="mw-translate-fuzzy">

Si possono usare le [costanti predefinite](#Costanti_supportate.md) e le [funzioni](#Funzioni_supportate.md).


</div>

### Function arguments 


<div class="mw-translate-fuzzy">

Quando una funzione accetta più argomenti, questi possono essere separati da un punto e virgola (\';\') o da una virgola seguita da uno spazio (\", \"). In quest\'ultimo caso, la virgola viene convertita in un punto e virgola dopo la voce. Quando si utilizza un punto e virgola, non è necessario terminare la riga con uno spazio.


</div>

Arguments may include references to cells in a spreadsheet. A cell reference consists of the cell\'s uppercase row letter followed by its column number, for example `A1`. A cell may also be referenced by using the cell\'s alias instead, for example `Spreadsheet.MyPartWidth`.

### Riferimenti a oggetti 


<div class="mw-translate-fuzzy">

Si può fare riferimento a un oggetto tramite il suo `Name` o la sua `Label`. Nel caso di una `Label`, essa deve essere racchiusa tra i simboli `<<` e `>>`, come questa: `<<Label>>`.


</div>


<div class="mw-translate-fuzzy">

È possibile fare riferimento a qualsiasi proprietà numerica di un oggetto. Ad esempio, per fare riferimento all\'altezza di un cilindro, è possibile utilizzare `Cylinder.Height` o `<<Long_name_of_cylinder>>.Height`.


</div>


<div class="mw-translate-fuzzy">

Per fare riferimento agli oggetti dell\'elenco, la sintassi è `<<object_label>>.list[list_index]` o `object_name.list[list_index]`. Se ad esempio si desidera fare riferimento a un vincolo in uno schizzo, si può farlo usando questa sintassi

**>.Constraints[16]**. Se il riferimento si trova nello stesso schizzo, si può ometterne il nome e utilizzare solo **Constraints[16]**.
**Nota:** L'indice inizia con 0, quindi il vincolo 17 ha l'indice 16.


</div>


<div class="mw-translate-fuzzy">

Per ulteriori informazioni sul riferimento a oggetti, vedere [questa sezione](#Riferimento_ai_dati_CAD.md).


</div>


<div class="mw-translate-fuzzy">

## Costanti supportate 


</div>


<div class="mw-translate-fuzzy">

Sono supportate le seguenti costanti:

  Constante   Descrizione
   
  **e**       [Numero di Eulero](https://en.wikipedia.org/wiki/E_(mathematical_constant))
  **pi**      [Pi greco](https://en.wikipedia.org/wiki/Pi)


</div>

## Supported operators 


<div class="mw-translate-fuzzy">

Sono supportati i seguenti operatori:

  Operatore   Descrizione
   
  **+**       [Addizione](https://en.wikipedia.org/wiki/Addition)
  **-**       [Sottrazione](https://en.wikipedia.org/wiki/Subtraction)
  **\***      [Multiplicazione](https://en.wikipedia.org/wiki/Multiplication)
  **/**       [Divisione](https://en.wikipedia.org/wiki/Division_(mathematics)) virgola mobile
  **%**       [Resto](https://en.wikipedia.org/wiki/Remainder)
  **\^**      [Potenze](https://en.wikipedia.org/wiki/Exponentiation)


</div>


<div class="mw-translate-fuzzy">

## Funzioni supportate 


</div>


<div class="mw-translate-fuzzy">

### Funzioni matematiche generali 


</div>

Le funzioni matematiche elencate di seguito sono disponibili.


<div class="mw-translate-fuzzy">

Le [funzioni trigonometriche](https://en.wikipedia.org/wiki/Trigonometric_functions) usano i gradi come unità predefinita. Per le misure in radianti aggiungere **rad** dopo il primo valore in una espressione. Per esempio **cos(45)** è la stessa cosa di **cos(pi rad / 4)**. Se un\'espressione è senza unità e per compatibilità deve essere convertita in gradi o radianti,, moltiplicare per **1 deg**, **1 °** o **1 rad** secondo il caso, ad es. **(360 - X) \* 1deg**; **(360 - X) \* 1°**; **(0.5 + pi / 2) \* 1rad**.
Sono supportate le seguenti funzioni trigonometriche:

  Funzione      Descrizione                                                                                              Intervallo di valori
    
  acos(x)       [Arc cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)             -1 \<= x \<= 1
  asin(x)       [Arc sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)               -1 \<= x \<= 1
  atan(x)       [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)            tutti
  atan2(x, y)   [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties) of *x/y*   tutti, eccetto y = 0
  cos(x)        [Cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)        tutti
  cosh(x)       [Hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)         tutti
  sin(x)        [Sine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)          tutti
  sinh(x)       [Hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)           tutti
  tan(x)        [Tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)       tutti, eccetto x = n·90 con n = intero
  tanh(x)       [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)        tutti


</div>


<div class="mw-translate-fuzzy">

Per esponenziazione e logaritmizzazione sono supportate le seguenti funzioni:

  Funzione    Descrizione                                                                                    Intervallo di valori
    
  exp(x)      [Exponential function](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition)   tutti
  log(x)      [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)                           x \> 0
  log10(x)    [Common logarithm](https://en.wikipedia.org/wiki/Common_logarithm)                             x \> 0
  pow(x, y)   [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                                 all
  sqrt(x)     [Square root](https://en.wikipedia.org/wiki/Square_root)                                       x \>= 0


</div>


<div class="mw-translate-fuzzy">

Per arrotondamento, troncamento e resto sono supportate queste funzioni :

  Funzione    Descrizione                                                                                                                           Intervallo di valori
    
  abs(x)      [Valore assoluto](https://en.wikipedia.org/wiki/Absolute_value)                                                                       tutti
  ceil(x)     [Parte intera superiore](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) valore intero più piccolo maggiore o uguale a x   tutti
  floor(x)    [Parte intera inferiore](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), valore intero più grande minore o uguale a x     tutti
  mod(x, y)   [Resto](https://en.wikipedia.org/wiki/Remainder) dopo aver diviso *x* per *y*                                                         tutti, eccetto y = 0
  round(x)    [Arrotondamento](https://en.wikipedia.org/wiki/Rounding) al numero intero più vicino                                                  tutti
  trunc(x)    [Troncamento](https://en.wikipedia.org/wiki/Truncation) al numero intero più vicino                                                   tutti


</div>

### Statistical / aggregate functions 


<div class="mw-translate-fuzzy">

### Statistica e Funzioni di aggregazione 

Le [funzioni di aggregazione](https://en.wikipedia.org/wiki/Aggregate_function) accettano uno o più argomenti, separati da un punto e virgola \';\' o da una virgola \'\' e \'\' uno spazio \', \'.
Gli argomenti possono includere riferimenti a celle di un foglio di calcolo. I riferimenti alla cella sono costituiti dalla lettera maiuscola seguita dal numero della colonna.
Gli argomenti possono includere intervalli di celle usando due riferimenti di cella separati da due punti, ad esempio **average(B1:B8)**.


</div>

Individual arguments to aggregate functions may consist of ranges of cells. A range of cells is expressed as two cell references separated by a colon {{Incode|:}}, for example {{Incode|average(B1:B8)}} or {{Incode|sum(A1:A4; B1:B4)}}. The cell references may also use cell aliases, for example {{Incode|average(StartTemp:EndTemp)}}.


<div class="mw-translate-fuzzy">

Sono supportate queste funzioni aggregate :

  Funzione       Descrizione                                                                                                                Intervallo di valori
    
  average(x:y)   [Media aritmetica](https://en.wikipedia.org/wiki/Arithmetic_mean) dei valori nelle celle da x a y; sum(x:y) / count(x:y)   tutti
  count(x:y)     [Conteggio](https://en.wikipedia.org/wiki/Counting) di celle da x a y                                                      tutti
  max(x:y)       [Massimo](https://en.wikipedia.org/wiki/Maxima_and_minima) valore nelle celle da x a y                                     tutti
  min(x:y)       [Minimo](https://en.wikipedia.org/wiki/Maxima_and_minima) valore nelle celle da x a y                                      tutti
  stddev(x:y)    [Deviazione standard](https://en.wikipedia.org/wiki/Standard_deviation) dei valori nelle celle da x a y                    tutti
  sum(x: y)      [Somma](https://en.wikipedia.org/wiki/Summation) dei valori nelle celle da x a y                                           tutti


</div>

### String manipulation 

#### String identification 

Strings are identified in expressions by surrounding them with opening/closing double chevrons (as are labels).

In following example, \"TEXT\" is recognized as a string : `<<TEXT>>`

#### String concatenation 

Strings can be concatenated using the \'+\' sign.

Following example `<<MY>> + <<TEXT>>` will be concatenated to \"MYTEXT\".

#### String formatting 

String formatting is supported using the (old) %-style Python way.

All %-specifiers as defined in [Python documentation](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

As an example, supposing you have a default 10mm-side cube named \'Box\' \--default FreeCAD naming\--, following expression `<<Cube length : %s>> % Box.Length` will expand to \"Cube length : 10.0 mm\"

A limitation is that only one %-specifier is allowed in string, thus you have to use string concatenation if more than one is needed. With same above situation, expression `<<Cube length is %s>> % Box.Length + << and width is %s>> % Box.Width` will expand to \"Cube length is 10.0 mm and width is 10.0 mm\".

A FreeCAD sample file using string formatting is available [in the forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657)

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

For readability, you can define vectors and rotations in separate cells, and then reference the cells in your expression.

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

### Tuple & list 

You can create Python `tuple` or `list` objects via their respective functions.


`tuple(2; 1; 2)`


`list(2; 1; 2)`


<div class="mw-translate-fuzzy">

## Espressioni condizionali 


</div>


<div class="mw-translate-fuzzy">

Le espressioni condizionali sono nella forma **condition ? resultTrue : resultFalse**. La condizione è definita come un\'espressione il cui risultato è \'0\' (falso) o diverso da zero (vero). Notare che racchiudere l\'espressione condizionale tra parentesi è attualmente considerato un errore. {{VersionMinus/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

Sono definiti i seguenti [operatori relazionali](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators):

  Operatore   Descrizione
   
  **==**      uguale
  **!=**      diverso
  **\>**      maggiore
  **\<**      minore
  **\>=**     maggiore o uguale
  **\<=**     minore o uguale


</div>

## Unità


<div class="mw-translate-fuzzy">

Le unità possono essere utilizzate direttamente nelle espressioni. Il parser le collega al valore precedente. Quindi **\'2mm**\' o **\'2 mm**\' è valido mentre **\'mm**\' non è valido perché non esiste un valore precedente.


</div>


<div class="mw-translate-fuzzy">

Tutti i valori devono avere un\'unità. Pertanto, in generale è necessario utilizzare un\'unità per i valori nei fogli di calcolo.
In alcuni casi funziona anche senza un\'unità, ad esempio se nella cella B1 del foglio di calcolo si ha solo il numero *1,5* e si fa riferimento ad esso per l\'altezza del pad. Questo funziona perché l\'altezza del pad predispone l\'unità *mm* che viene utilizzata quando non viene fornita alcuna unità. Però fallisce se si utilizza per l\'altezza del pad, ad es. **Sketch1.Constraints.Width - Spreadsheet.B1** perché *Sketch1.Constraints.Width* ha un\'unità e *Spreadsheet.B1* no.


</div>


<div class="mw-translate-fuzzy">

Le unità con esponenti possono essere inserite direttamente. Quindi ad es. **mm\^3** viene riconosciuto come mm³ e **m\^3** viene riconosciuto come m³.


</div>


<div class="mw-translate-fuzzy">

Se una variabile ha il nome di un\'unità di misura, bisogna inserire la variabile in **\<\< \>\>** per impedire che venga riconosciuta come unità di misura. Ad esempio, la dimensione **\'Sketch.Constraints.A**\' verrebbe riconosciuta come unità Ampere. Pertanto è necessario scriverla nell\'espressione in questo modo **\'Sketch.Constraints.\<\>**\'.


</div>

Il parser delle espressioni riconosce le seguenti unità:


<div class="mw-translate-fuzzy">

Quantità di sostanza:

  Unità   Descrizione
   
  mmol    Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol     [Mole](https://en.wikipedia.org/wiki/Mole_(unit))


</div>


<div class="mw-translate-fuzzy">

Angolo:

  Unità   Descrizione
   
  °       [Grado](https://en.wikipedia.org/wiki/Degree_(angle)); alternativa all\'unità *deg*
  deg     [Grado](https://en.wikipedia.org/wiki/Degree_(angle)); alternativa all\'unità *°*
  rad     [Radiante](https://en.wikipedia.org/wiki/Radian)
  gon     [Gradiante](https://en.wikipedia.org/wiki/Gon_(unit))
  S       [Secondo di arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc)
  ″       [Secondo di arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternativa all\'unità *S*
  M       [Minuto di arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc)
  ′       [Minuto di arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternativa all\'unità *M*


</div>


<div class="mw-translate-fuzzy">

Corrente:

  Unità   Descrizione
   
  mA      Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A       [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA      Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA      Mega[ampere](https://en.wikipedia.org/wiki/Ampere)


</div>


<div class="mw-translate-fuzzy">

Energia / Lavoro:

  Unità   Descrizione
   
  mJ      Milli[joule](https://en.wikipedia.org/wiki/Joule)
  J       [Joule](https://en.wikipedia.org/wiki/Joule)
  kJ      Kilo[joule](https://en.wikipedia.org/wiki/Joule), {{Version/it|0.19}}
  eV      [Elettronvolt](https://en.wikipedia.org/wiki/Electronvolt); 1 ev = 1.602176634e-19 J, {{Version/it|0.19}}
  keV     Kilo[elettronvolt](https://en.wikipedia.org/wiki/Electronvolt), {{Version/it|0.19}}
  MeV     Mega[elettronvolt](https://en.wikipedia.org/wiki/Electronvolt), {{Version/it|0.19}}
  kWh     [Kilowattora](https://en.wikipedia.org/wiki/Kilowatt_hour); 1 kWh = 3.6e6 J, {{Version/it|0.19}}
  Ws      [Watt second](https://en.wikipedia.org/wiki/Joule#Watt_second); alternativa all\'unità *Joule*
  VAs     [Volt-ampere-second](https://en.wikipedia.org/wiki/Joule); alternativa all\'unità *Joule*
  CV      [Coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternativa all\'unità *Joule*
  cal     [Calorie](https://en.wikipedia.org/wiki/Calorie); 1 cal = 4.184 J, {{Version/it|0.19}}
  kcal    Kilo[calorie](https://en.wikipedia.org/wiki/Calorie), {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

Forza:

  Unità   Descrizione
   
  mN      Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N       [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN      Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN      Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf     [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))


</div>


<div class="mw-translate-fuzzy">

Lunghezza:

  Unità   Descrizione
   
  nm      Nano[meter](https://en.wikipedia.org/wiki/Metre)
  um      Micro[meter](https://en.wikipedia.org/wiki/Metre); alternativa all\'unità *µm*
  µm      Micro[meter](https://en.wikipedia.org/wiki/Metre); alternativa all\'unità *mu*
  mm      Milli[meter](https://en.wikipedia.org/wiki/Metre)
  cm      Centi[meter](https://en.wikipedia.org/wiki/Metre)
  mm      Milli[meter](https://en.wikipedia.org/wiki/Metre)
  dm      Deci[meter](https://en.wikipedia.org/wiki/Metre)
  m       [Meter](https://en.wikipedia.org/wiki/Metre)
  km      Kilo[meter](https://en.wikipedia.org/wiki/Metre)
  mil     [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternativa all\'unità *thou*
  thou    [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternativa all\'unità *mil*
  in      [Inch](https://en.wikipedia.org/wiki/Inch)
  ft      [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternativa all\'unità \'
  \'      [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternativa all\'unità *ft*
  yd      [Yard](https://en.wikipedia.org/wiki/Yard)
  mi      [Mile](https://en.wikipedia.org/wiki/Mile)


</div>


<div class="mw-translate-fuzzy">

Intensità luminosa:

  Unità   Descrizione
   
  cd      [Candela](https://en.wikipedia.org/wiki/Candela)


</div>


<div class="mw-translate-fuzzy">

Massa:

  Unità   Descrizione
   
  ug      Micro[gram](https://en.wikipedia.org/wiki/Gram); alternativa all\'unità *µg*
  µg      Micro[gram](https://en.wikipedia.org/wiki/Gram); alternativa all\'unità *ug*
  mg      Milli[gram](https://en.wikipedia.org/wiki/Gram)
  g       [Gram](https://en.wikipedia.org/wiki/Gram)
  kg      Kilo[gram](https://en.wikipedia.org/wiki/Gram)
  t       [Tonne](https://en.wikipedia.org/wiki/Tonne)
  oz      [Ounce](https://en.wikipedia.org/wiki/Ounce)
  lb      [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternativa all\'unità *lbm*
  lbm     [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternativa all\'unità *lb*
  st      [Stone](https://en.wikipedia.org/wiki/Stone_(weight))
  cwt     [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)


</div>


<div class="mw-translate-fuzzy">

Potenza:

  Unità   Descrizione
   
  W       [Watt](https://en.wikipedia.org/wiki/Watt)
  kW      Kilo[watt](https://en.wikipedia.org/wiki/Watt), {{Version/it|0.19}}
  VA      [Volt-ampere](https://en.wikipedia.org/wiki/Volt-ampere)


</div>


<div class="mw-translate-fuzzy">

Pressione:

  Unità   Descrizione
   
  Pa      [pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  kPa     Kilo[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  MPa     Mega[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  GPa     Giga[pascal](https://en.wikipedia.org/wiki/Pascal_(unit))
  mbar    Milli[bar](https://en.wikipedia.org/wiki/Bar_(unit)), {{Version/it|0.19}}
  bar     [bar](https://en.wikipedia.org/wiki/Bar_(unit)), {{Version/it|0.19}}
  uTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternativa all\'unità *µTorr*
  µTorr   Micro[torr](https://en.wikipedia.org/wiki/Torr); alternativa all\'unità *uTorr*
  mTorr   Milli[torr](https://en.wikipedia.org/wiki/Torr)
  Torr    [torr](https://en.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [libbre per pollice quadrato](https://en.wikipedia.org/wiki/Pounds_per_square_inch); 1 psi = 6.895 kPa
  ksi     Kilo[libbre per pollice quadrato](https://en.wikipedia.org/wiki/Pounds_per_square_inch)
  Mpsi    Mega[libbre per pollice quadrato](https://en.wikipedia.org/wiki/Pounds_per_square_inch), {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

Temperatura:

  Unità   Descrizione
   
  uK      Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternativa all\'unità *µK*
  µK      Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternativa all\'unità *uK*
  mK      Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K       [Kelvin](https://en.wikipedia.org/wiki/Kelvin)


</div>


<div class="mw-translate-fuzzy">

Tempo:

  Unità      Descrizione
   
  s          [secondo](https://en.wikipedia.org/wiki/Second)
  min        [minuto](https://en.wikipedia.org/wiki/Minute)
  h          [ora](https://en.wikipedia.org/wiki/Hour)
  Hz (1/s)   [Hertz](https://en.wikipedia.org/wiki/Hertz), {{Version/it|0.19}}
  kHz        Kilo[hertz](https://en.wikipedia.org/wiki/Hertz), {{Version/it|0.19}}
  MHz        Mega[hertz](https://en.wikipedia.org/wiki/Hertz), {{Version/it|0.19}}
  GHz        Giga[hertz](https://en.wikipedia.org/wiki/Hertz), {{Version/it|0.19}}
  THz        Tera[hertz](https://en.wikipedia.org/wiki/Hertz), {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

Volume:

  Unità   Descrizione
   
  ml      Milli[litro](https://en.wikipedia.org/wiki/Litre), {{Version/it|0.19}}
  l       [litro](https://en.wikipedia.org/wiki/Litre)
  cft     Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit)) (piede cubico), {{Version/it|0.19}}


</div>


<div class="mw-translate-fuzzy">

Le seguenti unità comunemente utilizzate non sono ancora supportate:

  Unità   Descrizione                                                                                                  Alternativa
    
  °C      [Celsius](https://en.wikipedia.org/wiki/Celsius)                                                             \[°C\] + 273.15 K
  °F      [Fahrenheit](https://en.wikipedia.org/wiki/Fahrenheit);                                                      (\[°F\] + 459.67) × ​5/9
  u       [Atomic mass unit](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit \'Da\'   1.66053906660e-27 kg
  Da      [Dalton](https://en.wikipedia.org/wiki/Unified_atomic_mass_unit); alternative to the unit \'u\'              1.66053906660e-27 kg
  sr      [Steradian](https://en.wikipedia.org/wiki/Steradian)                                                         not directly
  lm      [Lumen](https://en.wikipedia.org/wiki/Lumen_(unit))                                                          not directly
  lx      [Lux](https://en.wikipedia.org/wiki/Lux)                                                                     not directly
  px      [Pixel](https://en.wikipedia.org/wiki/Pixel)                                                                 not directly


</div>

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

### Names

[Names](Object_name#Name.md) of objects like dimensions, sketches, etc. may not have the characters or character sequences listed below, otherwise the name is invalid:

  Characters / Character sequences                                                                                                              Description
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**                  Characters that are math operators or part of mathematical constructs
  **A**, **kA**, **mA**, **MA**, **C**, **G**, **F**, **uF**, **µF**, **J**, **K**, \'\'\' \' \'\'\', \'\'\' ft \'\'\', **°**, and many more!   Characters and character sequences that are [units](Expressions#Units.md)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, and many more!                         Characters used as placeholder or to trigger special operations
  **pi**, **e**                                                                                                                                 Mathematical constants
  **´**, **\**, \'\'\' \' \'\'\', **\"**                                                                                                       Characters used for accents
  space                                                                                                                                         A space defines the end of a name and can therefore not be used

For example, the following name is valid: `<<Sketch>>.Constraints.T2üßµ@`. While these are invalid names: `<<Sketch>>.Constraints.test\result_2` (\\r means \"carriage return\") or `<<Sketch>>.Constraints.mol` (mol is a unit).

Since shorter names (especially if they have only one or two characters) can easily result in invalid names, consider using longer names and/or establishing a suitable naming convention.

### Cell aliases 

For [spreadsheet cell aliases](Spreadsheet_SetAlias.md) only alphanumeric characters and underscores (`A` to `Z`, `a` to `z`, `0` to `9` and `_`) are allowed.


<div class="mw-translate-fuzzy">

## Riferimento ai dati CAD 


</div>


<div class="mw-translate-fuzzy">

In un\'espressione è possibile utilizzare i dati del modello stesso. Per fare riferimento a una proprietà usare object.property. Se la proprietà è un composto di campi, è possibile accedere ai singoli campi come object.property.field.


</div>


<div class="mw-translate-fuzzy">

La tabella seguente mostra alcuni esempi:

++++
| Dati CAD                                  | Chiamata nell\'espressione            | Risultato                                                                                                                                                         |
+===========================================+=======================================+===================================================================================================================================================================+
| Lunghezza parametrica di un Cubo di Parte |                        |                                                                                                                                                    |
|                                           | `Cube.Length`                | `Length`                                                                                                                                                 |
|                                           |                                    |                                                                                                                                                                |
|                                           |                                       | Lunghezza con unità in mm                                                                                                                                         |
++++
| Volume del Cubo                           |                        |                                                                                                                                                    |
|                                           | `Cube.Shape.Volume`          | `Volume`                                                                                                                                                 |
|                                           |                                    |                                                                                                                                                                |
|                                           |                                       | in mm³ senza unità                                                                                                                                                |
++++
| Tipo di forma del Cubo                    |                        | Stringa: Solid                                                                                                                                                    |
|                                           | `Cube.Shape.ShapeType`       |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Etichetta del Cubo                        |                        | Stringa: Label                                                                                                                                                    |
|                                           | `Cube.Label`                 |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Coordinata x del centro di massa del Cubo |                        | Coordinata x in mm senza unità                                                                                                                                    |
|                                           | `Cube.Shape.CenterOfMass.x`  |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Valore di un vincolo in uno schizzo       |                        | Valore numerico del vincolo di nome \'`Width`\' nello schizzo, se l\'espressione è utilizzata nello schizzo stesso.                        |
|                                           | `Constraints.Width`          |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Valore di un vincolo in uno schizzo       |                        | Valore numerico del vincolo di nome \'`Width`\' nello schizzo, se l\'espressione è usata al di fuori dello schizzo.                        |
|                                           | `MySketch.Constraints.Width` |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Valore di un alias in spreadsheet         |                        | Valore dell\'alias \"`Depth`\" nel foglio \"`Spreadsheet`\"                                                         |
|                                           | `Spreadsheet.Depth`          |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++
| Valore di una proprietà locale            |                        | Valore della proprietà `Length` ad es. di un oggetto Pad, se l\'espressione viene utilizzata, ad esempio, in Length2 nello stesso oggetto. |
|                                           | `Length`                     |                                                                                                                                                                   |
|                                           |                                    |                                                                                                                                                                   |
++++


</div>

## Variabili globali nell\'ambito del documento 

Al momento in FreeCAD non esiste il concetto di variabili globali. Invece, utilizzando l\'ambiente [Spreadsheet](Spreadsheet_Workbench/it.md), si possono definire delle variabili arbitrarie come celle in un foglio di calcolo, e poi assegnare loro un nome utilizzando la proprietà alias della cella (tasto destro del mouse sulla cella). Dopo si può accedere alla variabile da qualsiasi espressione, come per qualsiasi altra proprietà di un oggetto.

## Riferimenti incrociati nel documento 


<div class="mw-translate-fuzzy">

È possibile (con limitazioni) definire una proprietà di un oggetto nel documento corrente (file \".FCstd\") utilizzando un\'espressione per fare riferimento a una proprietà di un oggetto contenuto in un documento diverso (file \".FCstd\"). Ad esempio, una cella in un foglio di calcolo o la lunghezza di un cubo di Part, ecc. in un documento può essere definita da un\'espressione che fa riferimento al valore di posizionamento X o ad un\'altra proprietà di un oggetto contenuto in un documento diverso.


</div>

È possibile utilizzare il nome di un documento per fare riferimento ad esso da altri documenti. Quando si salva un documento per la prima volta, si sceglie un nome per il file; questo di solito è diverso dal default iniziale \"Unnamed1\" (o il suo equivalente tradotto). Per evitare la perdita dei collegamenti quando il documento master viene rinominato al momento del salvataggio, si consiglia di creare prima il documento master, creare un foglio di calcolo al suo interno e salvarlo. Successivamente è ancora possibile apportare modifiche e salvare il file, ma non si deve rinominarlo.


<div class="mw-translate-fuzzy">

Una volta creato e salvato (e denominato) il documento master con il foglio di calcolo, è possibile creare dei documenti dipendenti. Supponendo che il documento master sia stato denominato \"`master`\", il foglio di calcolo sia stato rinominato \"`modelConstants`\" e a una cella sia stato assegnato un nome alias \"`Length`\", si può quindi accedere al valore con:


</div>


<div class="mw-translate-fuzzy">


```pythonmaster#modelConstants.Length```


</div>

**Notare** che il documento master deve sempre essere caricato affinché i valori del master siano disponibili per il documento dipendente.

Purtroppo, il checker integrato a volte afferma che un nome valido non esiste. Continuare comunque a digitare. Quando il riferimento è completato, il pulsante **OK** diventa attivo.

Naturalmente, dopo spetta all\'utente il compito di caricare i documenti corrispondenti, quando si desidera cambiare qualcosa.

## Problemi noti / attività rimanenti 


<div class="mw-translate-fuzzy">

-   I grafici delle dipendenze si basano sul rapporto tra gli oggetti del documento, non sulle proprietà. Questo significa che non è possibile fornire i dati a un oggetto e interrogare lo stesso oggetto per i risultati. Ad esempio, anche se non ci sono dipendenze cicliche quando vengono considerate solo le proprietà, non si può avere un oggetto che ottiene le sue dimensioni da un foglio di calcolo e quindi visualizza il volume di tale oggetto nello stesso foglio di calcolo. Per aggirare il problema, utilizzare più fogli di calcolo, ad esempio uno per sviluppare il modello, e uno per i rapporti.
-   Il parser delle espressioni non gestisce bene le parentesi e non è in grado di analizzare correttamente alcune espressioni. Ad esempio: \"**= (A1 \> A2) ? 1 : 0**\" restituisce un errore, mentre \"**= A1 \> A2 ? 1 : 0**\" è accettato. L\'espressione \"**= 5 + ((A1\>A2) ? 1 : 0)**\" non può essere inserita in nessuna forma.
-   Come affermato sopra, sfortunatamente, a volte il controllo integrato afferma che non esiste un nome valido. Continuare comunque a digitare. Dopo aver completato il riferimento completo, il pulsante **OK** diventerà attivo.
-   Non è implementato nessun gestore delle espressioni in cui siano elencate tutte le espressioni di un documento, e possano essere create, eliminate, interrogate, ecc.
-   I nomi dei vincoli di Sketcher non devono contenere spazi vuoti quando il valore è calcolato da un\'espressione, vedere questa \[<https://forum.freecadweb.org/viewtopic.php?p=302500#p302381>; discussione nel forum\].
-   I bug aperti per le espressioni si trovano in [FreeCAD Bugtracker Expressions category](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/it
