# Expressions/it
## Descrizione

È possibile definire le proprietà utilizzando espressioni matematiche. Nella GUI, gli spin box o i campi di input che sono legati alle proprietà contengono un\'icona blu <img alt="" src=images/Bound-expression.svg  style="width:24px;">. Cliccando sull\'icona, oppure digitando il segno di uguale **&#61;**, si porta in primo piano l\'editor delle espressioni per quella particolare proprietà.

Un\'espressione di FreeCAD è un\'espressione matematica che utilizza gli [operatori](#Operatori_supportati.md), le [funzioni](#Funzioni_supportate.md) e le [costanti](#Costanti_supportate.md) standard come descritto di seguito. Inoltre, l\'espressione può fare riferimento a proprietà dell\'oggetto e utilizzare anche [espressioni condizionali](#Espressioni_condizionali.md). I numeri in un\'espressione possono avere una [unità](#Unità.md) facoltativa allegata.

I numeri possono utilizzare una virgola `,` o un punto decimale `.` per separare le cifre intere dai decimali. Quando viene utilizzato il marcatore decimale, *deve* essere seguito da almeno una cifra. Pertanto, le espressioni `1.+2.` e `1,+2,` non sono valide, ma `1.0 + 2.0` e `1,0 + 2 ,0` sono validi.

Gli operatori e le funzioni sono unit-aware (consapevoli delle unità), e richiedono combinazioni di unità valide, se sono necessarie. Ad esempio, `2mm + 4mm` è un\'espressione valida, mentre `2mm + 4` non lo è. Questo vale anche per i riferimenti alle proprietà dell\'oggetto che hanno unità, come la proprietà Length. Pertanto `Pad001.Length + 1` non è valido poiché aggiunge un numero puro a una proprietà con una unità di lunghezza, si richiede `Pad001.Length + 1mm`.

Alcuni errori relativi alle unità possono sembrare non intuitivi, con espressioni respinte o che producono risultati che non corrispondono alle unità della proprietà impostata. Ecco alcuni esempi:


`1/2mm`

non viene interpretato come mezzo millimetro ma come `1/(2mm)`, risultante in: `0.5 mm^-1`.


`sqrt(2)mm`

non è valido perché la chiamata alla funzione non è un numero. Questo deve essere inserito come `sqrt(2) * 1mm`.



### Argomenti delle funzioni 

Quando una funzione accetta più argomenti, questi possono essere separati da un punto e virgola seguita da uno spazio `, `. In quest\'ultimo caso, la virgola viene convertita in un punto e virgola dopo la voce. Quando si utilizza un punto e virgola, non è necessario terminare la riga con uno spazio.

Gli argomenti possono includere riferimenti a celle in un foglio di calcolo. Un riferimento di cella è costituito dalla lettera maiuscola della riga della cella seguita dal suo numero di colonna, ad esempio `A1`. È anche possibile fare riferimento a una cella utilizzando l\'alias della cella, ad esempio `Spreadsheet.MyPartWidth`.



### Riferimenti a oggetti 

Si può fare riferimento a un oggetto tramite il suo **Name** o la sua **Label**. Nel caso di una **Label**, essa deve essere racchiusa tra i simboli `<<` e `>>`, come questa: `<<Label>>`.

È possibile fare riferimento a qualsiasi proprietà di un oggetto. Ad esempio, per fare riferimento all\'altezza di un cilindro, è possibile utilizzare `Cylinder.Height` o `<<Long_name_of_cylinder>>.Height`. Per fare riferimento all\'oggetto stesso si usa la pseudo proprietà `_self`. Ad esempio, puoi utilizzare `Cylinder._self` o `<<Label_of_cylinder>>._self`.

Per fare riferimento agli oggetti dell\'elenco, usa `<<object_label>>.list[list_index]` o `object_name.list[list_index]`. Se ad esempio si desidera fare riferimento a un vincolo in uno schizzo, lo si può fare usando `<<MySketch>>.Constraints[16]`. Se il riferimento si trova nello stesso schizzo, si può ometterne il nome e utilizzare solo `Constraints[16]`.
**Nota:** L\'indice inizia con 0, quindi Constraint17 deve essere referenziato come `Constraints[16]`.

Per ulteriori informazioni sui riferimenti agli oggetti, vedere [Riferimento ai dati_CAD](#Riferimento_ai_dati_CAD.md). 

## Costanti supportate 

Sono supportate le seguenti costanti:

  Constante   Descrizione
   
  **e**       [Numero di Eulero](https://en.wikipedia.org/wiki/E_(mathematical_constant))
  **pi**      [Pi greco](https://en.wikipedia.org/wiki/Pi)


{{Top}}



## Operatori supportati 

Sono supportati i seguenti operatori:

  Operatore   Descrizione
   
  **+**       [Addizione](https://en.wikipedia.org/wiki/Addition)
  **-**       [Sottrazione](https://en.wikipedia.org/wiki/Subtraction)
  **\***      [Multiplicazione](https://en.wikipedia.org/wiki/Multiplication)
  **/**       [Divisione](https://en.wikipedia.org/wiki/Division_(mathematics)) virgola mobile
  **%**       [Resto](https://en.wikipedia.org/wiki/Remainder)
  **\^**      [Potenze](https://en.wikipedia.org/wiki/Exponentiation)


{{Top}}



## Funzioni supportate 



### Funzioni matematiche generali 

Sono supportate le seguenti funzioni matematiche:



#### Funzioni trigonometriche 

[Le funzioni trigonometriche](https://en.wikipedia.org/wiki/Trigonometric_functions) usano il grado come unità predefinita. Per la misura in radianti, aggiungi primo valore in un\'espressione. Quindi ad es. `cos(45)` è uguale a `cos(pi rad / 4)`. Le espressioni in gradi possono utilizzare `deg` o `°`, ad es. `360deg - atan2(3; 4)` o `360&deg; - atan2(3; 4)`. Se un\'espressione è senza unità e deve essere convertita in gradi o radianti per compatibilità, moltiplicare per `1&nbsp;deg`, `1&nbsp;°` o `1&nbsp;rad` in modo appropriato, ad es. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.


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



#### Funzioni esponenziali e logaritmiche 


<div class="mw-translate-fuzzy">

Per esponenziazione e logaritmizzazione sono supportate le seguenti funzioni:

  Funzione    Descrizione                                                                                    Intervallo di valori
    
  exp(x)      [Exponential function](https://en.wikipedia.org/wiki/Exponential_function#Formal_definition)   tutti
  log(x)      [Natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm)                           x \> 0
  log10(x)    [Common logarithm](https://en.wikipedia.org/wiki/Common_logarithm)                             x \> 0
  pow(x, y)   [Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)                                 all
  sqrt(x)     [Square root](https://en.wikipedia.org/wiki/Square_root)                                       x \>= 0


</div>



#### Funzioni di arrotondamento, troncamento e resto 


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


{{Top}}



### Funzioni statistiche / aggregate 

Le [funzioni di aggregazione](https://it.wikipedia.org/wiki/Funzione_di_aggregazione) prendono uno o più argomenti.
I singoli argomenti per le funzioni di aggregazione possono essere costituiti da intervalli di celle. Un intervallo di celle è espresso come due riferimenti di cella separati da due punti {{Incode|:}}, ad esempio {{Incode|average(B1:B8)}} o {{Incode|sum(A1:A4; B1:B4 )}}. I riferimenti di cella possono anche utilizzare alias di cella, ad esempio {{Incode|average(StartTemp:EndTemp)}}.

Sono supportate le seguenti funzioni di aggregazione:


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


{{Top}}



### Manipolazione delle stringhe 



#### Identificazione della stringa 

Le stringhe sono identificate nelle espressioni con doppi chevron di apertura/chiusura (così come le etichette).

Nell\'esempio seguente, \"TEXT\" è riconosciuto come una stringa: `<<TEXT>>`



#### Concatenazione di stringhe 

Le stringhe possono essere concatenate utilizzando il segno \'+\'.

L\'esempio seguente `<<MY>> + <<TEXT>>` sarà concatenato a \"MYTEXT\".



#### Conversione di stringhe 

I valori numerici possono essere convertiti in stringhe con la funzione `str`:


`str(Box.Length.Value)`



#### Formattazione della stringa 

La formattazione delle stringhe è supportata utilizzando il (vecchio) stile Python col %.

Tutti gli %-specifiers come definiti nella [documentazione di Python](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Ad esempio, supponendo di avere un cubo predefinito di 10 mm di lato denominato \'Box\' (denominazione predefinita di FreeCAD), la seguente espressione `<<Cube length : %s>> % Box.Length` si espanderà in \"Cube length: 10,0 mm\"

Per più di uno specificatore % utilizzare la seguente sintassi: `<<La lunghezza del cubo è %s e la larghezza è %s>> % tuple(Box.Length; Box.Width)`. Oppure usa la concatenazione: `<<La lunghezza del cubo è %s>> % Box.Length + << e la larghezza è %s>> % Box.Width`. Entrambi si espandono in \"La lunghezza del cubo è 10,0 mm e la larghezza è 10,0 mm\".

È disponibile un file di esempio di FreeCAD che utilizza la formattazione delle stringhe [nel forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) 

### Funzioni per la creazione di oggetti 

I seguenti oggetti possono essere creati nelle espressioni utilizzando le seguenti funzioni:

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
|                                                                                    |                                                 | È possibile fornire un minimo di 1 argomento come `matrix(1)` che crea una matrice identità.                                                                                                                                                                                                                     |
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
|                                                                                    |                                                 | Esempi:                                                                                                                                                                                                                                                                                                                                 |
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



### Funzioni matriciali 


`Rotation`

e `Placement` possono essere rappresentati ciascuno da una `Matrix`. Le seguenti funzioni accettano tutte `Matrix`, `Rotation` o `Placement` come primo parametro indicato nella tabella seguente da `m`. Il tipo dell\'oggetto restituito è lo stesso dell\'oggetto fornito nel primo argomento tranne quando si utilizza `mtranslate` su `Rotation`, nel qual caso sarà restituito `Placement`.

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



## Espressioni condizionali 

Le espressioni condizionali hanno la forma `condition ? resultTrue : resultFalse`. La condizione è definita come un\'espressione che restituisce `0` (falso) o diverso da zero (vero). Si noti che racchiudere l\'espressione condizionale tra parentesi è attualmente considerato un errore.


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


{{Top}}



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



### Quantità di sostanza 


<div class="mw-translate-fuzzy">

Quantità di sostanza:

  Unità   Descrizione
   
  mmol    Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol     [Mole](https://en.wikipedia.org/wiki/Mole_(unit))


</div>



### Angolo


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



### Attuale


<div class="mw-translate-fuzzy">

Corrente:

  Unità   Descrizione
   
  mA      Milli[ampere](https://en.wikipedia.org/wiki/Ampere)
  A       [Ampere](https://en.wikipedia.org/wiki/Ampere)
  kA      Kilo[ampere](https://en.wikipedia.org/wiki/Ampere)
  MA      Mega[ampere](https://en.wikipedia.org/wiki/Ampere)


</div>



### Capacità elettrica 

  Unit   Description
   
  pF     Pico[farad](https://en.wikipedia.org/wiki/Farad)
  nF     Nano[farad](https://en.wikipedia.org/wiki/Farad)
  uF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit µF
  µF     Micro[farad](https://en.wikipedia.org/wiki/Farad); alternative to the unit uF
  mF     Milli[farad](https://en.wikipedia.org/wiki/Farad)
  F      [Farad](https://en.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg



### Carica elettrica 

  Unit   Description
   
  C      [Coulomb](https://en.wikipedia.org/wiki/Coulomb); 1 C = 1 A\*s



### Conducibilità elettrica 

  Unit   Description
   
  uS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit µS
  µS     Micro[siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); alternative to the unit uS
  mS     Milli[siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  S      [Siemens](https://en.wikipedia.org/wiki/Siemens_(unit)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS     Kilo[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))
  MS     Mega[Siemens](https://en.wikipedia.org/wiki/Siemens_(unit))



### Induttanza elettrica 

  Unit   Description
   
  nH     Nano[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  uH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit µH
  µH     Micro[henry](https://en.wikipedia.org/wiki/Henry_(unit)); alternative to the unit uH
  mH     Milli[henry](https://en.wikipedia.org/wiki/Henry_(unit))
  H      [Henry](https://en.wikipedia.org/wiki/Henry_(unit)); 1 H = 1 kg·m\^2/s\^2/A\^2



### Potenziale elettrico 

  Unit   Description
   
  mV     Milli[volt](https://en.wikipedia.org/wiki/Volt)
  V      [Volt](https://en.wikipedia.org/wiki/Volt)
  kV     Kilo[volt](https://en.wikipedia.org/wiki/Volt)



### Resistenza elettrica 

  Unit   Description
   
  Ohm    [Ohm](https://en.wikipedia.org/wiki/Ohm); 1 Ohm = 1 kg·m\^2/s\^3/A\^2
  kOhm   Kilo[ohm](https://en.wikipedia.org/wiki/Ohm)
  MOhm   Mega[ohm](https://en.wikipedia.org/wiki/Ohm)



### Energia/lavoro


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



### Forza


<div class="mw-translate-fuzzy">

Forza:

  Unità   Descrizione
   
  mN      Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N       [Newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN      Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN      Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf     [Pound of force](https://en.wikipedia.org/wiki/Pound_(force))


</div>



### Lunghezza


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



### Intensità luminosa 


<div class="mw-translate-fuzzy">

Intensità luminosa:

  Unità   Descrizione
   
  cd      [Candela](https://en.wikipedia.org/wiki/Candela)


</div>



### Flusso magnetico 

  Unit   Description
   
  Wb     [Weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A



### Densità del flusso magnetico 

  Unit   Description
   
  G      [Gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T
  T      [Tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A



### Massa


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



### Potenza


<div class="mw-translate-fuzzy">

Potenza:

  Unità   Descrizione
   
  W       [Watt](https://en.wikipedia.org/wiki/Watt)
  kW      Kilo[watt](https://en.wikipedia.org/wiki/Watt), {{Version/it|0.19}}
  VA      [Volt-ampere](https://en.wikipedia.org/wiki/Volt-ampere)


</div>



### Pressione


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



### Temperatura


<div class="mw-translate-fuzzy">

Temperatura:

  Unità   Descrizione
   
  uK      Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternativa all\'unità *µK*
  µK      Micro[kelvin](https://en.wikipedia.org/wiki/Kelvin); alternativa all\'unità *uK*
  mK      Milli[kelvin](https://en.wikipedia.org/wiki/Kelvin)
  K       [Kelvin](https://en.wikipedia.org/wiki/Kelvin)


</div>



### Tempo


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

### Volume


<div class="mw-translate-fuzzy">

Volume:

  Unità   Descrizione
   
  ml      Milli[litro](https://en.wikipedia.org/wiki/Litre), {{Version/it|0.19}}
  l       [litro](https://en.wikipedia.org/wiki/Litre)
  cft     Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit)) (piede cubico), {{Version/it|0.19}}


</div>



### Unità imperiali speciali 

  Unità   Descrizione
   
  mph     [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour)
  sqft    [Square foot](https://en.wikipedia.org/wiki/Square_foot)



### Unità non supportate 

Le seguenti unità di uso comune non sono ancora supportate, per alcune viene fornita un\'alternativa:


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


{{Top}}



## Caratteri e nomi non validi 

La funzionalità delle espressioni è molto potente, ma per raggiungere questo potere ha alcune limitazioni relative ad alcuni caratteri. Per ovviare a questo, FreeCAD offre la possibilità di utilizzare etichette e fare riferimento ad esse invece che ai nomi degli oggetti. Nelle etichette puoi usare quasi tutti i caratteri speciali.

Nei casi in cui non è possibile utilizzare un\'etichetta, come il nome dei vincoli di uno schizzo, è necessario sapere quali caratteri non sono consentiti.



### Etichette

For [labels](Object_name#Label.md) there are no invalid characters, however some characters need to be escaped:

+++
| Characters                                               | Description                                                               |
+==========================================================+===========================================================================+
|                                           | Need to be escaped by adding `\` in front of them. |
| `'`                                             |                                                                           |
|                                                       |                                                                           |
| , `\`, `"` |                                                                           |
+++

Ad esempio, l\'etichetta `Sketch\002` deve essere referenziata come `<<Sketch\\002>>`.



### Nomi

[Nomi](Object_name#Nome.md) di oggetti come dimensioni, schizzi, ecc. non devono avere i caratteri o le sequenze di caratteri elencati di seguito, perchè altrimenti il nome non è valido:

  Characters / Character sequences                                                                                               Description
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**   Characters that are math operators or part of mathematical constructs
  **A**, **kA**, **mA**, **MA**, **J**, **K**, **\'**, **ft**, **°**, and many more!                                             Characters and character sequences that are units (see the [Units](#Units.md) paragraph)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, and many more!          Characters used as placeholder or to trigger special operations
  **pi**, **e**                                                                                                                  Mathematical constants
  **´**, **\**, **\'**, **\"**                                                                                                  Characters used for accents
  space                                                                                                                          A space defines the end of a name and can therefore not be used

For example, the following name is valid: `<<Sketch>>.Constraints.T2üßµ@`. While these are invalid names: `<<Sketch>>.Constraints.test\result_2` (\\r means \"carriage return\") or `<<Sketch>>.Constraints.mol` (mol is a unit).

Poiché i nomi più brevi (soprattutto se hanno solo uno o due caratteri) possono facilmente risultare in nomi non validi, prendere in considerazione l\'utilizzo di nomi più lunghi e/o stabilire una convenzione di denominazione adeguata.



### Alias di cella 

See [Spreadsheet SetAlias](Spreadsheet_SetAlias#Usage.md). 

## Riferimento ai dati CAD 

È possibile utilizzare i dati del modello stesso in un\'espressione. Per fare riferimento a una proprietà utilizzare `object.property`. Se la proprietà è un composto di campi, è possibile accedere ai singoli campi come `object.property.field`.


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


{{Top}}



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


`master#modelConstants.Length`

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


{{Top}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/it
