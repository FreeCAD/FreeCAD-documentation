# Expressions/it
## Descrizione

È possibile definire le proprietà utilizzando espressioni matematiche. Nella GUI, le caselle di selezione o i campi di input associati alle proprietà mostrano un\'icona blu <img alt="" src=images/Bound-expression.svg  style="width:16px;"> quando sono attivati. Facendo clic sull\'icona o digitando il segno uguale **&#61;** si apre l\'editor delle espressioni per quella particolare proprietà. Se il campo di input mostra un pulsante **...** invece di un\'icona, l\'editor delle espressioni può essere aperto facendo clic con il pulsante destro del mouse sulla proprietà e selezionando **Expression...** dal menu contestuale.

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

Come già mostrato sopra,S si può fare riferimento a un oggetto tramite il suo **Name**. Ma si può anche usare la sua **Label**. Nel caso di una **Label**, essa deve essere racchiusa tra i simboli `<<` e `>>`, come questa: `<<Label>>`.

È possibile fare riferimento a qualsiasi proprietà di un oggetto. Ad esempio, per fare riferimento all\'altezza di un cilindro, è possibile utilizzare `Cylinder.Height` o `<<Label_of_cylinder>>.Height`

Per ulteriori informazioni sui riferimenti agli oggetti, vedere [Riferimento ai dati CAD](#Riferimento_ai_dati_CAD.md). 

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

[Le funzioni trigonometriche](https://en.wikipedia.org/wiki/Trigonometric_functions) usano il grado come unità predefinita. Per i radianti, aggiungere primo valore in un\'espressione. Quindi ad es. `cos(45)` è uguale a `cos(pi rad / 4)`. Le espressioni in gradi possono utilizzare `deg` o `°`, ad es. `360deg - atan2(3; 4)` o `360&deg; - atan2(3; 4)`. Se un\'espressione è senza unità e deve essere convertita in gradi o radianti per compatibilità, moltiplicare per `1deg`, `1°` o `1rad` in modo appropriato, ad es. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0.5 + pi / 2) * 1rad`.

++++
| Funzione               | Descrizione                                                                                                                                                                | Intervallo di valori                               |
+========================+============================================================================================================================================================================+====================================================+
|         | [Arco seno](https://it.wikipedia.org/wiki/Funzione_trigonometrica_inversa)                                                                                                 | -1 \<= x \<= 1                                     |
| `acos(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Arco coseno](https://it.wikipedia.org/wiki/Funzione_trigonometrica_inversa)                                                                                               | -1 \<= x \<= 1                                     |
| `asin(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Arco tangente](https://it.wikipedia.org/wiki/Funzione_trigonometrica_inversa), restituisce un valore con -90° \< valore \< 90°                                            | tutti                                              |
| `atan(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Arco tangente 2](https://it.wikipedia.org/wiki/Funzione_trigonometrica_inversa) con *y/x* tenendo conto del quadrante, restituisce un valore con -180° \< valore \<= 180° | tutti, l\'input non valido x = y = 0 restituisce 0 |
| `atan2(y; x)` |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Coseno](https://it.wikipedia.org/wiki/Funzione_trigonometrica#Definizioni_tramite_triangoli_rettangoli)                                                                   | tutti                                              |
| `cos(x)`      |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Coseno iperbolico](https://it.wikipedia.org/wiki/Funzioni_iperboliche#Definizioni)                                                                                        | tutti                                              |
| `cosh(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Seno](https://it.wikipedia.org/wiki/Funzione_trigonometrica#Definizioni_tramite_triangoli_rettangoli)                                                                     | tutti                                              |
| `sin(x)`      |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Seno iperbolico](https://it.wikipedia.org/wiki/Funzioni_iperboliche#Definizioni)                                                                                          | tutti                                              |
| `sinh(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Tangente](https://it.wikipedia.org/wiki/Funzione_trigonometrica#Definizioni_tramite_triangoli_rettangoli)                                                                 | tutti, eccetto x = n\*90 con = intero dispari      |
| `tan(x)`      |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Tangente iperbolica](https://it.wikipedia.org/wiki/Funzioni_iperboliche#Definizioni)                                                                                      | tutti                                              |
| `tanh(x)`     |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | [Addizione pitagorica](https://en.wikipedia.org/wiki/Pythagorean_addition) (utilizzo di **hypot**), e.g. hypot(4; 3) = 5                                                   | x e y \>= 0                                        |
| `hypot(x; y)` |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++
|         | Data l\'ipotenusa e un lato, restituisce l\'altro lato del triangolo rettangolo, per esempio cath(5; 3) = 4                                                                | x \>= y \>= 0                                      |
| `cath(x; y)`  |                                                                                                                                                                            |                                                    |
|                     |                                                                                                                                                                            |                                                    |
++++



#### Funzioni esponenziali e logaritmiche 

++++
| Funzione                          | Descrizione                                                                     | Intervallo di valori |
+===================================+=================================================================================+======================+
|                    | [Esponenziale](https://it.wikipedia.org/wiki/Funzione_esponenziale#Definizioni) | tutti                |
| `exp(x)`                 |                                                                                 |                      |
|                                |                                                                                 |                      |
++++
|                    | [Logaritmo naturale](https://it.wikipedia.org/wiki/Logaritmo_naturale)          | x \> 0               |
| `log(x)`                 |                                                                                 |                      |
|                                |                                                                                 |                      |
++++
|                    | [Logaritmo in base 10](https://it.wikipedia.org/wiki/Logaritmo)                 | x \> 0               |
| `log10(x)`               |                                                                                 |                      |
|                                |                                                                                 |                      |
++++
|                    | [Potenza](https://it.wikipedia.org/wiki/Potenza_(matematica))                   | tutti                |
| `pow(x; y)`              |                                                                                 |                      |
|                                |                                                                                 |                      |
++++
|                    | [Radice quadrata](https://it.wikipedia.org/wiki/Radice_quadrata)                | x \>= 0              |
| `sqrt(x)`                |                                                                                 |                      |
|                                |                                                                                 |                      |
++++
|                    | [Radice cubica](https://it.wikipedia.org/wiki/Radicale_(matematica))            | tutti                |
| `cbrt(x)`                |                                                                                 |                      |
|                                |                                                                                 |                      |
| {{Version/it|0.21}} |                                                                                 |                      |
++++



#### Funzioni di arrotondamento, troncamento e resto 

++++
| Funzione             | Descrizione                                                                                                                               | Intervallo di valori |
+======================+===========================================================================================================================================+======================+
|       | [Valore assoluto](https://it.wikipedia.org/wiki/Valore_assoluto)                                                                          | tutti                |
| `abs(x)`    |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++
|       | [Approssimazione per difetto](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), valore intero più piccolo maggiore o uguale a x | tutti                |
| `ceil(x)`   |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++
|       | [Approssimazione in eccesso](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions), valore intero più grande minore o uguale a x     | tutti                |
| `floor(x)`  |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++
|       | [Resto](https://it.wikipedia.org/wiki/Resto) dopo aver diviso *x* per *y*, il segno del risultato è quello del dividendo.                 | tutti, eccetto y = 0 |
| `mod(x; y)` |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++
|       | [Arrotondamento](https://it.wikipedia.org/wiki/Arrotondamento) all\'intero più vicino                                                     | tutti                |
| `round(x)`  |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++
|       | [Troncamento](https://it.wikipedia.org/wiki/Troncamento_(matematica)) all\'intero più vicino nella direzione dello zero                   | tutti                |
| `trunc(x)`  |                                                                                                                                           |                      |
|                   |                                                                                                                                           |                      |
++++


{{Top}}



### Funzioni statistiche / aggregate 

Le [funzioni di aggregazione](https://it.wikipedia.org/wiki/Funzione_di_aggregazione) prendono uno o più argomenti.
I singoli argomenti per le funzioni di aggregazione possono essere costituiti da intervalli di celle. Un intervallo di celle è espresso come due riferimenti di cella separati da due punti {{Incode|:}}, ad esempio {{Incode|average(B1:B8)}} o {{Incode|sum(A1:A4; B1:B4 )}}. I riferimenti di cella possono anche utilizzare alias di cella, ad esempio {{Incode|average(StartTemp:EndTemp)}}.

Sono supportate le seguenti funzioni di aggregazione:

++++
| Funzione                         | Descrizione                                                                                                                                                                | Intervallo di valori |
+==================================+============================================================================================================================================================================+======================+
|                   | [Media aritmetica](https://it.wikipedia.org/wiki/Media_(statistica)#Media_aritmetica) del valore degli argomenti, calcolato come sum(a; b; c; \...) / count(a; b; c; \...) | tutti                |
| `average(a; b; c; ...)` |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++
|                   | [Conteggio](https://it.wikipedia.org/wiki/Statistica) degli argomenti, generalmente utilizzato su intervalli di celle                                                      | tutti                |
| `count(a; b; c; ...)`   |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++
|                   | [Massimo](https://it.wikipedia.org/wiki/Massimo_e_minimo_di_una_funzione) valore tra gli argomenti                                                                         | tutti                |
| `max(a; b; c; ...)`     |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++
|                   | [Minimo](https://it.wikipedia.org/wiki/Massimo_e_minimo_di_una_funzione) valore tra gli argomenti                                                                          | tutti                |
| `min(a; b; c; ...)`     |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++
|                   | [Deviazione standard](https://it.wikipedia.org/wiki/Scarto_quadratico_medio) dei valori degli argomenti                                                                    | tutti                |
| `stddev(a; b; c; ...)`  |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++
|                   | [Sommatoria](https://it.wikipedia.org/wiki/Sommatoria) dei valori degli argomenti, tipicamente utilizzato su intervalli di celle                                           | tutti                |
| `sum(a; b; c; ...)`     |                                                                                                                                                                            |                      |
|                               |                                                                                                                                                                            |                      |
++++


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
| Tipo                                                           | Funzione                                                                           | Descrizione                                                                                                                                                                                                                                                                                                                                    |
+================================================================+====================================================================================+================================================================================================================================================================================================================================================================================================================================================+
|                                                 |                                                                     | Esempio: `tuple(2; 1; 2)`                                                                                                                                                                                                                                                                                               |
| `Tuple`                                               | `tuple(a; b; ...)`                                                        |                                                                                                                                                                                                                                                                                                                                                |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                 |                                                                     | Esempio: `list(2; 1; 2)`                                                                                                                                                                                                                                                                                                |
| `List`                                                | `list(a; b; ...)`                                                         |                                                                                                                                                                                                                                                                                                                                                |
|                                                             |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
| [`Vector`](Vector_API.md)       |                                                                     | Crea un vettore senza unità o utilizzando tre valori con unità di `Lunghezza`. Esempio: `vector(2; 1; 3)`                                                                                                                                                                                        |
|                                                                | `vector(x; y; z)`                                                         |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `create(<<vector>>; x; y; z)`                                             |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
| [`Matrix`](Matrix_API.md)       | matrix(                                                                          | Crea una matrice 4x4 [ordinata per riga](https://en.wikipedia.org/wiki/Row-_and_column-major_order): $\begin{bmatrix}                                                                                                                                                                                                                          |
|                                                                |   a~11~; a~12~; a~13~; a~14~;                                    | a_{11} & a_{12} & a_{13} & a_{14} \\                                                                                                                                                                                                                                                                                                           |
|                                                                |   a~21~; a~22~; a~23~; a~24~;                                    | a_{21} & a_{22} & a_{23} & a_{24} \\                                                                                                                                                                                                                                                                                                           |
|                                                                |   a~31~; a~32~; a~33~; a~34~;                                    | a_{31} & a_{32} & a_{33} & a_{34} \\                                                                                                                                                                                                                                                                                                           |
|                                                                |   a~41~; a~42~; a~43~; a~44~                                       | a_{41} & a_{42} & a_{43} & a_{44} \\                                                                                                                                                                                                                                                                                                           |
|                                                                | )                                                                                | \end{bmatrix}$                                                                                                                                                                                                                                                                                                                                 |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | È possibile fornire un minimo di 1 argomento come `matrix(1)` che crea una matrice identità.                                                                                                                                                                                                                            |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | Esempio: `matrix(1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16)`                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `create(<<matrix>>; a<sub>11</sub>; a<sub>12</sub>; ...; a<sub>44</sub>)` |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                 |                                                                     | Crea una `Rotation` specificando il suo `axis` (`Vector`) e `angle` (`Angle` senza unità o con unità), o i tre angoli di Eulero `α`, `β`, `γ`. Esempi: |
| `Rotation`                                            | `rotation(axis; angle)`                                                   |                                                                                                                                                                                                                                                                                                                                                |
|                                                             |                                                                                 | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `rotation(vector(0; 1; 0); 45)`                                                                                                                                                                                                                                                                                                   |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `create(<<rotation>>; 30; 30; 30)`                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `rotation(α; β; γ)`                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `create(<<rotation>>; axis; angle)`                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `create(<<rotation>>; α; β; γ)`                                           |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
| [`Placement`](Placement_API.md) |                                                                     | Crea un `Placement` con vari parametri, inclusi:                                                                                                                                                                                                                                                                        |
|                                                                | `placement(base; rotation)`                                               |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `base`                                                                                                                                                                                                                                                                                                                            |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : posizione di base (`Vector`)                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `center`                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : posizione centrale (`Vector`)                                                                                                                                                                                                                                                                                     |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `rotation`                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : `Rotation`                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `axis`                                                                                                                                                                                                                                                                                                                            |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : asse di rotazione (`Vector`)                                                                                                                                                                                                                                                                                      |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `angle`                                                                                                                                                                                                                                                                                                                           |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : angolo di rotazione (senza unità o con unità `Angle`)                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `matrix`                                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |     : `Matrix`                                                                                                                                                                                                                                                                                                          |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | Esempi:                                                                                                                                                                                                                                                                                                                                        |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `placement(vector(2; 1; 3); rotation(vector(0; 0; 1); 45))`                                                                                                                                                                                                                                                                       |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                    | -                                                                                                                                                                                                                                                                                                                               |
|                                                                |                                                                                    |     `create(<<placement>>; create(<<vector>>; 2; 1; 2); create(<<rotation>>; create(<<vector>>; 0; 1; 0); 45))`                                                                                                                                                                                                                       |
|                                                                |                                                                                    |                                                                                                                                                                                                                                                                                                                                             |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `placement(base; rotation; center)`                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `placement(base; axis; angle)`                                            |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `placement(matrix)`                                                       |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++
|                                                                |                                                                     |                                                                                                                                                                                                                                                                                                                                                |
|                                                                | `create(<<placement>>; ...)`                                              |                                                                                                                                                                                                                                                                                                                                                |
|                                                                |                                                                                 |                                                                                                                                                                                                                                                                                                                                                |
++++


{{Top}}



### Funzioni vettoriali 

Funzioni: {{Version/it|1.0}}.

+++
| Funzione / Operatore                | Descrizzione                                                                                                                                                                                  |
+=====================================+===============================================================================================================================================================================================+
|                      | Somma vettoriale.                                                                                                                                                                             |
| `v1 + v2`                  |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Sottrazione vettoriale.                                                                                                                                                                       |
| `v1 - v2`                  |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Prodotto scalare per `s`.                                                                                                                                              |
| `v * s`                    |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Angolo tra due vettori in gradi.                                                                                                                                                              |
| `vangle(v1; v2)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Prodotto vettoriale tra due vettori $v_1 \times v_2$.                                                                                                                                         |
| `vcross(v1; v2)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Prodotto scalare tra due vettori $v_1 \cdot v_2$.                                                                                                                                             |
| `v1 * v2`                  |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      |                                                                                                                                                                                               |
| `vdot(v1; v2)`             |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Distanza tra `v1` e una linea attraverso `v2` in direzione di `v3`.                                                      |
| `vlinedist(v1; v2; v3)`    |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Distanza tra il vettore `v1` e il punto più vicino su un segmento di linea da `v2` a `v3`.                               |
| `vlinesegdist(v1; v2; v3)` |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Proiezione di un vettore `v1` su una linea attraverso `v2` in direzione `v3`.                                            |
| `vlineproj(v1; v2; v3)`    |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Normalizza un vettore in un vettore unitario.                                                                                                                                                 |
| `vnormalize(v)`            |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Distanza tra il vettore `v1` e un piano definito da un punto `v2` e una normale `v3`.                                    |
| `vplanedist(v1)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Proietta il vettore `v1` su un piano definito da un punto `v2` e una normale `v3`.                                       |
| `vplaneproj(v1)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      | Ridimensiona in modo non uniforme un vettore di `sx` nella direzione X, `sy` nella direzione Y e `sz` nella direzione Z. |
| `vscale(v; sx; sy; sz)`    |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      |                                                                                                                                                                                               |
| `vscalex(v; sx)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      |                                                                                                                                                                                               |
| `vscaley(v; sy)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++
|                      |                                                                                                                                                                                               |
| `vscalez(v; sz)`           |                                                                                                                                                                                               |
|                                  |                                                                                                                                                                                               |
+++


{{Top}}



### Funzioni matriciali 


`Rotation`

e `Placement` possono essere rappresentati ciascuno da una `Matrix`. Le seguenti funzioni accettano tutte `Matrix`, `Rotation` o `Placement` come primo parametro indicato nella tabella seguente da `m`. Il tipo dell\'oggetto restituito è lo stesso dell\'oggetto fornito nel primo argomento tranne quando si utilizza `mtranslate` su `Rotation`, nel qual caso sarà restituito `Placement`.

+++
| Funzione                           | Descrizione                                                                                                                                                                                                                                                                                                                   |
+====================================+===============================================================================================================================================================================================================================================================================================================================+
|                     | Calcola la [Matrice inversa](https://it.wikipedia.org/wiki/Matrice_invertibile).                                                                                                                                                                                                                                              |
| `minvert(m)`              |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Rotazione](https://it.wikipedia.org/wiki/Matrice_di_trasformazione) con:                                                                                                                                                                                                                                                     |
| `mrotate(m; rotation)`    |                                                                                                                                                                                                                                                                                                                               |
|                                 | -   una `Rotazione`                                                                                                                                                                                                                                                                                    |
|                                    | -   un asse (`Vettore`) e un angolo (`Angolo` con unità o adimensionale)                                                                                                                                                                                                        |
|                                    | -   i tre angoli di Eulero `α`, `β`, `γ`                                                                                                                                                                                                                 |
+++
|                     |                                                                                                                                                                                                                                                                                                                               |
| `mrotate(m; axis; angle)` |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     |                                                                                                                                                                                                                                                                                                                               |
| `mrotate(m; α; β; γ)`     |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Rotazione](https://it.wikipedia.org/wiki/Matrice_di_trasformazione) attorno all\'asse X.                                                                                                                                                                                                                                     |
| `mrotatex(m; angle)`      |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Rotazione](https://it.wikipedia.org/wiki/Matrice_di_trasformazione) attorno all\'asse Y.                                                                                                                                                                                                                                     |
| `mrotatey(m; angle)`      |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Rotazione](https://it.wikipedia.org/wiki/Matrice_di_trasformazione) attorno all\'asse Z.                                                                                                                                                                                                                                     |
| `mrotatez(m; angle)`      |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Traslazione](https://it.wikipedia.org/wiki/Traslazione_(geometria)#Rappresentazione_con_matrici) con un `vector` (`Vector`) o con i valori X, Y, Z. Se una `Rotazione` è anche traslata, l\'oggetto restituito è un `Placement`. |
| `mtranslate(m; vector)`   |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     |                                                                                                                                                                                                                                                                                                                               |
| `mtranslate(m; x; y; z)`  |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     | [Scala](https://en.wikipedia.org/wiki/Scaling_(geometry)#Matrix_representation) per un `vector` (`Vector`) o per i valori X, Y, Z.                                                                                                                                              |
| `mscale(m; vector)`       |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++
|                     |                                                                                                                                                                                                                                                                                                                               |
| `mscale(m; x; y; z)`      |                                                                                                                                                                                                                                                                                                                               |
|                                 |                                                                                                                                                                                                                                                                                                                               |
+++


{{Top}}



## Espressioni condizionali 

Le espressioni condizionali hanno la forma `condizione ? resultTrue : resultFalse`. La condizione è definita come un\'espressione che restituisce `0` (false) o diverso da zero (true).

Tenere presente che per utilizzare una proprietà booleana come condizione è necessario utilizzare questa sintassi: `VarSet.MyBool &#61;&#61; 1? 10 mm: 15 mm`.

Sono definiti i seguenti [operatori relazionali](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators):

  Operatore   Descrizione
   
  **==**      uguale
  **!=**      diverso
  **\>**      maggiore
  **\<**      minore
  **\>=**     maggiore o uguale
  **\<=**     minore o uguale


{{Top}}



## Unità

Le unità possono essere utilizzate direttamente nelle espressioni. Il parser le collega al valore precedente. Quindi `2mm` o `2 mm` è valido mentre `mm` non è valido perché non esiste un valore precedente.

Tutti i valori devono avere un\'unità. Pertanto, in generale è necessario utilizzare un\'unità per i valori nei fogli di calcolo.
In alcuni casi funziona anche senza un\'unità, ad esempio se nella cella B1 del foglio di calcolo si ha solo il numero `1.5` e si fa riferimento ad esso per l\'altezza del pad. Questo funziona perché l\'altezza del pad predispone l\'unità `mm` che viene utilizzata quando non viene fornita alcuna unità. Però fallisce se si utilizza per l\'altezza del pad, ad es. `Sketch1.Constraints.Width - Spreadsheet.B1` perché `Sketch1.Constraints.Width` ha un\'unità e `Spreadsheet.B1` no.

Le unità con esponenti possono essere inserite direttamente. Quindi ad es. `mm^3` viene riconosciuto come mm³ e `m^3` viene riconosciuto come m³.

Se si ha una variabile il cui nome è quello di un\'unità di misura, si deve inserire la variabile tra `<< >>` per evitare che venga riconosciuta come un\'unità di misura. Ad esempio, la dimensione `Sketch.Constraints.A` verrebbe riconosciuta come l\'unità ampere. Quindi è necessario scriverla nell\'espressione come `Sketch.Constraints.<<A>>`.

Il parser delle espressioni riconosce le seguenti unità:



### Quantità di sostanza 

  Unità   Descrizione
   
  mmol    Milli[mole](https://en.wikipedia.org/wiki/Mole_(unit))
  mol     [Mole](https://en.wikipedia.org/wiki/Mole_(unit))



### Angolo

  Unità   Descrizione
   
  °       [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternativa all\'unità deg
  deg     [Degree](https://en.wikipedia.org/wiki/Degree_(angle)); alternativa all\'unità °
  rad     [Radiante](https://en.wikipedia.org/wiki/Radian)
  gon     [Gradianti](https://en.wikipedia.org/wiki/Gon_(unità))
  M       [Minuto d\'arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); alternativa all\'unità ′
  \'      [Minuto d\'arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); questo è il simbolo primo (U+2032); alternativa all\'unità M
  S       [Secondo d\'arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); **NON FUNZIONA**; alternativa all\'unità″
  \"      [Secondo d\'arco](https://en.wikipedia.org/wiki/Minute_and_second_of_arc); questo è il simbolo del doppio primo (U+2033); alternativa all\'unità S



### Corrente

  Unità   Descrizione
   
  mA      Milli[ampere](https://it.wikipedia.org/wiki/Ampere)
  A       [ampere](https://it.wikipedia.org/wiki/Ampere)
  kA      Kilo[ampere](https://it.wikipedia.org/wiki/Ampere)
  MA      Mega[ampere](https://it.wikipedia.org/wiki/Ampere)



### Capacità elettrica 

  Unità   Descrizione
   
  pF      Pico[farad](https://it.wikipedia.org/wiki/Farad)
  nF      Nano[farad](https://it.wikipedia.org/wiki/Farad)
  uF      Micro[farad](https://it.wikipedia.org/wiki/Farad); alternativa all\'unità µF
  µF      Micro[farad](https://it.wikipedia.org/wiki/Farad); alternativa all\'unità uF
  mF      Milli[farad](https://it.wikipedia.org/wiki/Farad)
  F       [Farad](https://it.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg



### Carica elettrica 

  Unità   Descrizione
   
  C       [coulomb](https://it.wikipedia.org/wiki/Coulomb); 1 C = 1 A\*s



### Conducibilità elettrica 

  Unità   Descrizione
   
  uS      Micro[siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura)); alternative to the unit µS
  µS      Micro[siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura)); alternative to the unit uS
  mS      Milli[siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura))
  S       [siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura)); 1 S = 1 s\^3·A\^2/kg/m\^2
  kS      Kilo[siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura))
  MS      Mega[siemens](https://it.wikipedia.org/wiki/Siemens_(unit%C3%A0_di_misura))



### Induttanza elettrica 

  Unità   Descrizione
   
  nH      Nano[henry](https://it.wikipedia.org/wiki/Henry_(unit%C3%A0_di_misura))
  uH      Micro[henry](https://it.wikipedia.org/wiki/Henry_(unit%C3%A0_di_misura)); alternativa all\'unità µH
  µH      Micro[henry](https://it.wikipedia.org/wiki/Henry_(unit%C3%A0_di_misura)); alternativa all\'unità uH
  mH      Milli[henry](https://it.wikipedia.org/wiki/Henry_(unit%C3%A0_di_misura))
  H       [henry](https://it.wikipedia.org/wiki/Henry_(unit%C3%A0_di_misura)); 1 H = 1 kg·m\^2/s\^2/A\^2



### Potenziale elettrico 

  Unità   Descrizione
   
  mV      Milli[volt](https://it.wikipedia.org/wiki/Volt)
  V       [volt](https://it.wikipedia.org/wiki/Volt)
  kV      Kilo[volt](https://it.wikipedia.org/wiki/Volt)



### Resistenza elettrica 

  Unità   Descrizione
   
  ohm     [ohm](https://it.wikipedia.org/wiki/Ohm); 1 ohm = 1 kg·m\^2/s\^3/A\^2
  kohm    Kilo[ohm](https://it.wikipedia.org/wiki/Ohm)
  Mohm    Mega[ohm](https://it.wikipedia.org/wiki/Ohm)



### Energia/lavoro

  Unità   Descrizione
   
  mJ      Milli[joule](https://en.wikipedia.org/wiki/Joule)
  J       [joule](https://en.wikipedia.org/wiki/Joule)
  kJ      Kilo[joule](https://en.wikipedia.org/wiki/Joule)
  eV      [Elettronvolt](https://en.wikipedia.org/wiki/Electronvolt); 1 eV = 1.602176634e-19 J
  keV     Kilo[elettronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  MeV     Mega[elettronvolt](https://en.wikipedia.org/wiki/Electronvolt)
  kWh     [kilowattora](https://en.wikipedia.org/wiki/Kilowatt_hour); 1 kWh = 3.6e6 J
  Ws      [Watt secondo](https://en.wikipedia.org/wiki/Joule#Watt_second); alternativa all\'unità *Joule*
  VAs     [volt-ampere-secondo](https://en.wikipedia.org/wiki/Joule); alternativa all\'unità *Joule*
  CV      [coulomb-volt](https://en.wikipedia.org/wiki/Joule); alternativa all\'unità *Joule*
  cal     [calorie](https://en.wikipedia.org/wiki/Calorie); 1 cal = 4.184 J
  kcal    Kilo[calorie](https://en.wikipedia.org/wiki/Calorie)



### Forza

  Unità   Descrizione
   
  mN      Milli[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  N       [newton](https://en.wikipedia.org/wiki/Newton_(unit))
  kN      Kilo[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  MN      Mega[newton](https://en.wikipedia.org/wiki/Newton_(unit))
  lbf     [Libbra forza](https://en.wikipedia.org/wiki/Pound_(force))



### Lunghezza

  Unità   Descrizione
   
  nm      Nano[metro](https://en.wikipedia.org/wiki/Metre)
  um      Micro[metro](https://en.wikipedia.org/wiki/Metre); alternativa all\'unità µm
  µm      Micro[metro](https://en.wikipedia.org/wiki/Metre); alternativa all\'unità *mu*
  mm      Milli[metro](https://en.wikipedia.org/wiki/Metre)
  cm      Centi[metro](https://en.wikipedia.org/wiki/Metre)
  dm      Deci[metro](https://en.wikipedia.org/wiki/Metre)
  m       [metro](https://en.wikipedia.org/wiki/Metre)
  km      Kilo[metro](https://en.wikipedia.org/wiki/Metre)
  mil     [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternativa all\'unità thou
  thou    [Thousandth of an inch](https://en.wikipedia.org/wiki/Thousandth_of_an_inch); alternativa all\'unità mil
  in      [Inch](https://en.wikipedia.org/wiki/Inch); alternativa all\'unità \"
  ft      [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternativa all\'unità \'
  \'      [Foot](https://en.wikipedia.org/wiki/Foot_(unit)); alternativa all\'unità *ft*
  yd      [Yard](https://en.wikipedia.org/wiki/Yard)
  mi      [Mile](https://en.wikipedia.org/wiki/Mile)



### Intensità luminosa 

  Unità   Descrizione
   
  cd      [candela](https://en.wikipedia.org/wiki/Candela)



### Flusso magnetico 

  Unità   Descrizione
   
  Wb      [weber](https://en.wikipedia.org/wiki/Weber_(unit)); 1 Wb = 1 kg\*m\^2/s\^2/A



### Densità del flusso magnetico 

  Unità   Descrizione
   
  G       [gauss](https://en.wikipedia.org/wiki/Gauss_(unit)); 1 G = 1 e-4 T
  T       [tesla](https://en.wikipedia.org/wiki/Tesla_(unit)); 1 T = 1 kg/s\^2/A



### Massa

  Unità   Descrizione
   
  ug      Micro[grammo](https://it.wikipedia.org/wiki/Grammo); alternativa all\'unità µg
  µg      Micro[grammo](https://it.wikipedia.org/wiki/Grammo); alternativa all\'unità ug
  mg      Milli[grammo](https://it.wikipedia.org/wiki/Grammo)
  g       [grammo](https://it.wikipedia.org/wiki/Grammo)
  kg      Kilo[grammo](https://it.wikipedia.org/wiki/Grammo)
  t       [Tonnellata](https://it.wikipedia.org/wiki/Tonnellata)
  oz      [Ounce](https://en.wikipedia.org/wiki/Ounce)
  lb      [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternativa all\'unità lbm
  lbm     [Pound](https://en.wikipedia.org/wiki/Pound_(mass)); alternativa all\'unità lb
  st      [Stone](https://en.wikipedia.org/wiki/Stone_(weight))
  cwt     [Hundredweight](https://en.wikipedia.org/wiki/Hundredweight)



### Potenza

  Unità   Descrizione
   
  W       [watt](https://en.wikipedia.org/wiki/Watt)
  kW      Kilo[watt](https://en.wikipedia.org/wiki/Watt), {{Version/it|0.19}}
  VA      [volt-ampere](https://en.wikipedia.org/wiki/Volt-ampere)



### Pressione

  Unità   Descrizione
   
  Pa      [pascal](https://it.wikipedia.org/wiki/Pascal_(unit%C3%A0_di_misura))
  kPa     Kilo[pascal](https://it.wikipedia.org/wiki/Pascal_(unit%C3%A0_di_misura))
  MPa     Mega[pascal](https://it.wikipedia.org/wiki/Pascal_(unit%C3%A0_di_misura))
  GPa     Giga[pascal](https://it.wikipedia.org/wiki/Pascal_(unit%C3%A0_di_misura))
  uTorr   Micro[torr](https://it.wikipedia.org/wiki/Torr); alternativa all\'unità µTorr
  µTorr   Micro[torr](https://it.wikipedia.org/wiki/Torr); alternativa all\'unità uTorr
  mTorr   Milli[torr](https://it.wikipedia.org/wiki/Torr)
  Torr    [Torr](https://it.wikipedia.org/wiki/Torr); 1 Torr = 133.32 Pa
  psi     [Libbra-forza per pollice quadrato](https://it.wikipedia.org/wiki/Psi_(unit%C3%A0_di_misura)); 1 psi = 6.895 kPa
  ksi     Kilo[Libbra-forza per pollice quadrato](https://it.wikipedia.org/wiki/Psi_(unit%C3%A0_di_misura))



### Temperatura

  Unità   Descrizione
   
  uK      Micro[kelvin](https://it.wikipedia.org/wiki/Kelvin); alternativa all\'unità µK
  µK      Micro[kelvin](https://it.wikipedia.org/wiki/Kelvin); alternativa all\'unità uK
  mK      Milli[kelvin](https://it.wikipedia.org/wiki/Kelvin)
  K       [Kelvin](https://it.wikipedia.org/wiki/Kelvin)



### Tempo

  Unità      Descrizione
   
  s          [secondo](https://it.wikipedia.org/wiki/Secondo)
  min        [minuto](https://it.wikipedia.org/wiki/Minuto)
  h          [ora](https://it.wikipedia.org/wiki/Ora)
  Hz (1/s)   [Hertz](https://it.wikipedia.org/wiki/Hertz)
  kHz        Kilo[hertz](https://it.wikipedia.org/wiki/Hertz)
  MHz        Mega[hertz](https://it.wikipedia.org/wiki/Hertz)
  GHz        Giga[hertz](https://it.wikipedia.org/wiki/Hertz)
  THz        Tera[hertz](https://it.wikipedia.org/wiki/Hertz)

### Volume

  Unità   Descrizione
   
  ml      Milli[litro](https://en.wikipedia.org/wiki/Litre)
  l       [litro](https://en.wikipedia.org/wiki/Litre)
  cft     Cubic[foot](https://en.wikipedia.org/wiki/Foot_(unit)) (piede cubico)



### Unità imperiali speciali 

  Unità   Descrizione
   
  mph     [Miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour)
  sqft    [Square foot](https://en.wikipedia.org/wiki/Square_foot)



### Unità non supportate 

Le seguenti unità di uso comune non sono ancora supportate, per alcune viene fornita un\'alternativa:

  Unità   Descrizione                                                                                                      Alternativa
    
  °C      [Grado Celsius](https://it.wikipedia.org/wiki/Grado_Celsius)                                                     \[°C\] + 273.15 K
  °F      [Grado Fahrenheit](https://it.wikipedia.org/wiki/Grado_Fahrenheit);                                              (\[°F\] + 459.67) × ​5/9
  u       [Unità di massa atomica](https://it.wikipedia.org/wiki/Unit%C3%A0_di_massa_atomica); alternativa all\'unità Da   1.66053906660e-27 kg
  Da      [dalton](https://it.wikipedia.org/wiki/Unit%C3%A0_di_massa_atomica); alternativa all\'unità u                    1.66053906660e-27 kg
  sr      [steradiante](https://it.wikipedia.org/wiki/Steradiante)                                                         not directly
  lm      [lumen](https://it.wikipedia.org/wiki/Lumen)                                                                     non direttamente
  lx      [lux](https://it.wikipedia.org/wiki/Lux)                                                                         non direttamente
  px      [pixel](https://it.wikipedia.org/wiki/Pixel)                                                                     non direttamente


{{Top}}



## Caratteri e nomi non validi 

La funzionalità delle espressioni è molto potente, ma per raggiungere questo potere ha alcune limitazioni relative ad alcuni caratteri. Per ovviare a questo, FreeCAD offre la possibilità di utilizzare etichette e fare riferimento ad esse invece che ai nomi degli oggetti. Nelle etichette puoi usare quasi tutti i caratteri speciali.

Nei casi in cui non è possibile utilizzare un\'etichetta, come il nome dei vincoli di uno schizzo, è necessario sapere quali caratteri non sono consentiti.



### Etichette

Per le [etichette](Object_name/it#Etichette.md) non ci sono caratteri non validi, tuttavia è necessario eseguire l\'escape di alcuni caratteri:

+++
| Caratteri                                                | Descrizione                                                                |
+==========================================================+============================================================================+
|                                           | È necessario inserire l\'escape aggiungendogli `\`. |
| `'`                                             |                                                                            |
|                                                       |                                                                            |
| , `\`, `"` |                                                                            |
+++

Ad esempio, l\'etichetta `Sketch\002` deve essere referenziata come `<<Sketch\\002>>`.



### Nomi

[Nomi](Object_name#Nome.md) di oggetti come dimensioni, schizzi, ecc. non devono avere i caratteri o le sequenze di caratteri elencati di seguito, perchè altrimenti il nome non è valido:

  Caratteri / Sequenze di caratteri                                                                                              Descrizione
   
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**   Caratteri che sono operatori matematici o parte di costrutti matematici
  **A**, **kA**, **mA**, **MA**, **J**, **K**, **\'**, **ft**, **°**, and many more!                                             Caratteri e sequenze di caratteri che sono unità (vedere paragrafo [Unità](#Unità.md).)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, e molti altri!          Caratteri usati come segnaposto o per attivare operazioni speciali
  **pi**, **e**                                                                                                                  Costanti matematiche
  **´**, **\**, **\'**, **\"**                                                                                                  Caratteri usati per gli accenti
  spazio                                                                                                                         Uno spazio definisce la fine di un nome e pertanto non può essere utilizzato

Ad esempio, è valido il seguente nome: `<<Sketch>>.Constraints.T2üßµ@`. Mentre questi sono nomi non validi: `<<Sketch>>.Constraints.test\result_2` (\\r significa \"ritorno a capo\") o `<<Sketch>>.Constraints.mol` (mol è un\'unità).

Poiché i nomi più brevi (soprattutto se hanno solo uno o due caratteri) possono facilmente risultare in nomi non validi, prendere in considerazione l\'utilizzo di nomi più lunghi e/o stabilire una convenzione di denominazione adeguata.



### Alias di cella 

Vedere [Spreadsheet SetAlias](Spreadsheet_SetAlias/it#Utilizzo.md). 

## Riferimento ai dati CAD 

È possibile utilizzare i dati del modello stesso in un\'espressione. Per fare riferimento a una proprietà utilizzare `object_name.property` o `<<object_label>>.property`, le etichette devono essere racchiuse tra `<<` e `>>} }. Se si desidera utilizzare le etichette, queste devono essere univoche.

Tutti gli esempi successivi fanno riferimento all'oggetto con il suo nome, ma in tutti i casi è possibile utilizzare anche l'etichetta dell'oggetto.

Se la proprietà è un composto di campi, è possibile accedere ai singoli campi come {{incode|object_name.property.field`.

Per fare riferimento agli oggetti dell'elenco utilizzare `object_name.list[list_index]`. Se si vuole fare riferimento a un vincolo in uno schizzo, usare `Sketch.Constraints[16]`. Se ci si trova nello stesso sketch è possibile ometterne il nome e usare semplicemente `Constraints[16]`. Tenere presente che l'indice inizia con 0, pertanto è necessario fare riferimento a Constraint17 come `Constraints[16]`.

Per fare riferimento all'oggetto stesso utilizzare la pseudo proprietà `_self`: `object_name._self`.

La tabella seguente mostra alcuni ulteriori esempi:
{| class="wikitable"
 !Dati CAD
 !Chiamata nell'espressione
 !Risultato
 |-
 |Lunghezza di un [Box di Part](Part_Box/it.md)
 |`Box.Length`
 |Lunghezza con unità (mm)
 |-
 |Volume di un Box
 |`Box.Shape.Volume`
 |Volume in mm&sup3; senza unità
 |-
 |Tipo di Shape di un Box
 |`Box.Shape.ShapeType`
 |Stringa: Solid
 |-
 |Etichetta di una Box
 |`Box.Label`
 |Stringa: Label
 |-
 |Coordinata X del centro di massa di un Box
 |`Box.Shape.CenterOfMass.x`
 |Coordinata X in mm senza unità
 |-
 |Coordinata X del Box placement
 |`Box.Placement.Base.x`
 |Coordinata X con l'unità (mm)
 |-
 |Componente X dell'asse di rotazione del placement di un Box
 |`Box.Placement.Rotation.Axis.x`
 |Componente X del vettore unitario in mm senza unità
 |-
 |Angolo di rotazione del placemente di un Box
 |`Box.Placement.Rotation.Angle`
 |Angolo di rotazione con unità (deg)
 |-
 |Oggetto Full Box
 |`Box._self`
 |Oggetto del tipo <Part::PartFeature>
 |-
 |Valore di un vincolo in uno schizzo
 |`Constraints.Width`
 |Valore numerico di un vincolo denominato `Width` nello sketch, se l'espressione è utilizzata nello sketch stesso.
 |-
 |Valore di un vincolo in uno schizzo
 |`MySketch.Constraints.Width`
 |Valore numerico di un vincolo denominato `Width` nello sketch, se l'espressione viene utilizzata all'esterno dello sketch.
 |-
 |Valore di un alias in uno Spreadsheet
 |`Spreadsheet.Depth`
 |Valore dell'alias `Depth` nel foglio di calcolo `Spreadsheet`
 |-
 |Valore di una proprietà locale
 |`Length`
 |Valore della proprietà **Length**, ad esempio in un oggetto Pad, se l'espressione è utilizzata ad esempio in **Length2** nello stesso oggetto.
 |}

<span id="Cyclic_dependencies"></span>
=== Dipendenze cicliche ===

FreeCAD controlla le dipendenze in base alla relazione tra gli oggetti del documento, non alle proprietà. Ciò significa che non è possibile fornire dati a un oggetto ed eseguire query sullo stesso oggetto per ottenere risultati. Ad esempio, anche se non esistono dipendenze cicliche quando vengono considerate le proprietà stesse, potresti non avere un oggetto che ottiene le sue dimensioni da un foglio di calcolo e quindi visualizza il volume di quell'oggetto nello stesso foglio di calcolo. Si devono utilizzare due fogli di calcolo, uno per gestire il proprio modello e l'altro per i report.

Come soluzione alternativa è possibile visualizzare un intervallo di celle dal secondo foglio di calcolo nel primo (o viceversa) creando un [associazione di celle](Spreadsheet_Workbench#Cell_binding.md) con l'opzione **Nascondi dipendenza dell'associazione**.

Un altro modo per aggirare le dipendenze cicliche è nascondere il riferimento utilizzando la funzione `href` o `hiddenref` per le singole espressioni, ad esempio: `href(Box.Length)`.

Tenere presente che entrambe le soluzioni alternative menzionate devono essere utilizzate con cautela e che non funzionano se le proprietà segnalate dipendono da dimensioni determinate dallo stesso foglio di calcolo.
{{Top}}
<span id="Document-wide_global_variables"></span>
== Variabili globali nell'ambito del documento ==

Al momento in FreeCAD non esiste il concetto di variabili globali. Invece, utilizzando l'ambiente [Spreadsheet](Spreadsheet_Workbench/it.md), si possono definire delle variabili arbitrarie come celle in un foglio di calcolo, e poi assegnare loro un nome utilizzando la proprietà alias della cella (tasto destro del mouse sulla cella). Dopo si può accedere alla variabile da qualsiasi espressione, come per qualsiasi altra proprietà di un oggetto.
{{Top}}
<span id="Cross-document_linking"></span>
== Riferimenti incrociati nel documento ==

È possibile (con limitazioni) definire una proprietà di un oggetto nel documento corrente (file ".FCstd") utilizzando un'espressione per fare riferimento a una proprietà di un oggetto contenuto in un documento diverso (file ".FCstd"). Ad esempio, una cella in un foglio di calcolo o la {{PropertyData/it|lunghezza}} di un cubo di Part, ecc. in un documento può essere definita da un'espressione che fa riferimento al valore di posizionamento X o ad un'altra proprietà di un oggetto contenuto in un documento diverso.

È possibile utilizzare il nome di un documento per fare riferimento ad esso da altri documenti. Quando si salva un documento per la prima volta, si sceglie un nome per il file; questo di solito è diverso dal default iniziale "Unnamed1" (o il suo equivalente tradotto). Per evitare la perdita dei collegamenti quando il documento master viene rinominato al momento del salvataggio, si consiglia di creare prima il documento master, creare un foglio di calcolo al suo interno e salvarlo. Successivamente è ancora possibile apportare modifiche e salvare il file, ma non si deve rinominarlo.

Una volta creato e salvato (e denominato) il documento master con il foglio di calcolo, è possibile creare dei documenti dipendenti. Supponendo che il documento master sia stato denominato `master`, il foglio di calcolo sia stato rinominato `modelConstants` e a una cella sia stato assegnato un nome alias `Length`, si può quindi accedere al valore con:

`master#modelConstants.Length`

Notare che il documento master deve sempre essere caricato affinché i valori del master siano disponibili per il documento dipendente.

Naturalmente, dopo spetta all'utente il compito di caricare i documenti corrispondenti, quando si desidera cambiare qualcosa.
{{Top}}
<span id="Known_issues_/_remaining_tasks"></span>
== Problemi noti / attività rimanenti ==

* FreeCAD non dispone ancora di un gestore di espressioni integrato in cui tutte le espressioni in un documento sono elencate e possono essere create, cancellate, interrogate, ecc. Ma è disponibile un componente aggiuntivo: [https://github.com/gbroques/fcxref fcxref expression manager].
* I bug/ticket aperti per le espressioni possono essere trovati su [https://github.com/FreeCAD/FreeCAD/labels/Topic%3A%20Expressions GitHub].
{{Top}}
<span id="Scripting"></span>
== Script ==

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
⏵ [documentation index](../README.md) > [Spreadsheet](Category_Spreadsheet.md) > Expressions/it
