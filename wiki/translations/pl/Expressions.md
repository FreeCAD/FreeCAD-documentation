# Expressions/pl
 {{TOCright}}

## Informacje ogólne 

Możliwe jest definiowanie właściwości za pomocą wyrażeń matematycznych. W GUI, pola wyboru lub pola wejściowe, które są powiązane z właściwościami zawierają niebieską ikonę <img alt="" src=images/Sketcher_Expressions.png  style="width:24px;">. Kliknięcie na ikonę lub wpisanie znaku równości **&#61;** powoduje wyświetlenie edytora wyrażeń dla danej właściwości.

Wyrażenie FreeCAD jest wyrażeniem matematycznym zgodnym z notacją dla standardowych operatorów matematycznych i funkcji opisanych poniżej. Dodatkowo, wyrażenie może odwoływać się do innych właściwości, a także używać warunków. Liczby w wyrażeniu mogą mieć opcjonalnie dołączoną jednostkę.

W liczbach można używać przecinka `,` lub kropki dziesiętnej `.` oddzielającej całe cyfry od części dziesiętnych. Gdy używany jest przecinek, po nim **musi** następować co najmniej jedna cyfra. Zatem wyrażenia `1.+2.` i `1,+2,` są nieprawidłowe, ale `1.0 + 2.0` i `1,0 + 2,0` są już poprawne.

Operatory i funkcje są świadome jednostek i wymagają poprawnych kombinacji jednostek, jeśli zostały podane. Na przykład, `2mm + 4mm` jest poprawnym wyrażeniem, podczas gdy `2mm + 4` nie jest *(powodem tego jest to, że wyrażenie takie jak `1in + 4` będzie najprawdopodobniej interpretowane jako `1in + 4in` przez ludzi, ale wszystkie jednostki są konwertowane do układu SI wewnętrznie, a system nie jest w stanie tego odgadnąć)*. Obecnie rozpoznawane są następujące [jednostki](#Jednostki.md).

Możesz użyć [stałych predefiniowanych](#Obs.C5.82ugiwane_sta.C5.82e.md) i [funkcji](#Obsługiwane_funkcje.md).

### Argumenty funkcji 

Wiele argumentów funkcji może być oddzielonych średnikiem po którym następuje spacja `, `. W tym drugim przypadku, po wprowadzeniu przecinek jest konwertowany na średnik. Gdy używany jest średnik, spacja nie jest wymagana.

Argumenty mogą zawierać odwołania do komórek w arkuszu kalkulacyjnym. Odwołanie do komórki składa się z wielkiej litery wiersza, po której następuje numer kolumny, na przykład `A1`. Można też odwołać się do komórki, używając jej aliasu, na przykład `Arkusz_kalkulacyjny.DługośćCzęści`.

### Odwołania do obiektów 

Możesz odwołać się do obiektu przez jego właściwość {{PropertyData/pl|Nazwa}} lub {{PropertyData/pl|Etykieta}}. W przypadku właściwości {{PropertyData/pl|Etykieta}}, musi ona być zamknięta w podwójnych symbolach `<<` i `>>`, na przykład `<<Etykieta>>`.

Możesz odwołać się do dowolnej właściwości numerycznej obiektu. Na przykład, aby odwołać się do wysokości bryły walca, możesz użyć właściwości `Cylinder.Height` lub `<<Etykieta_walca>>.Height`.

Aby odwołać się do obiektów listy, użyj właściwości `<<Etykieta_obiektu>>.lista[index_listy]` lub `Nazwa_obiektu.lista[index_listy]`. Jeśli chcesz na przykład odwołać się do wiązania w szkicu, użyj właściwości `<<Nazwa_szkicu>>.Wiązanie[16]`. Jeśli znajdujesz się w tym samym szkicu, możesz pominąć jego nazwę i po prostu użyć właściwości `Wiązanie[16]`.
**Uwaga:** Numeracja indeksów zaczyna się od **0**, dlatego wiązanie *17* ma indeks **16**.

Więcej informacji na temat odwoływania się do obiektów znajdziesz w akapicie [Odwołanie do danych CAD](#Odwo.C5.82anie_do_danych_CAD.md).

## Obsługiwane stałe 

Obsługiwane są następujące stałe:

  Nazwa stałej   Opis
  -------------- ------------------------------------------------------------------
  **e**          [Liczba Eulera](https://pl.wikipedia.org/wiki/Sta%C5%82a_Eulera)
  **pi**         [Pi](https://pl.wikipedia.org/wiki/Pi)

## Obsługiwane operatory 

Obsługiwane są następujące operatory:

  Operator   Opis
  ---------- -------------------------------------------------------------------------
  **+**      [Dodawanie](https://pl.wikipedia.org/wiki/Dodawanie)
  **-**      [Odejmowanie](https://pl.wikipedia.org/wiki/Odejmowanie)
  **\***     [Mnożenie](https://pl.wikipedia.org/wiki/Mno%C5%BCenie)
  **/**      [Dzielenie](https://pl.wikipedia.org/wiki/Dzielenie) zmiennoprzecinkowe
  **%**      [Modulo](https://pl.wikipedia.org/wiki/Modulo)
  **\^**     [Potęgowanie](https://pl.wikipedia.org/wiki/Pot%C4%99gowanie)

## Obsługiwane funkcje 

### Ogólne funkcje matematyczne 

Dostępne są funkcje matematyczne wymienione poniżej.

[Funkcje trygonometryczne](https://pl.wikipedia.org/wiki/Funkcje_trygonometryczne) używają stopnia jako domyślnej jednostki. W przypadku miary radianowej, dodaj nazwę jednostki pierwszą wartością w wyrażeniu. Tak więc np. `cos(45)` jest tym samym co `cos(pi rad / 4)`. W wyrażeniach w stopniach można używać albo nazwę jednostki `deg` albo symbol jednostki `°`, np. `360deg - atan2(3; 4)` lub `360&deg; - atan2(3; 4)`. Jeśli wyrażenie nie ma jednostek i musi być przeliczone na stopnie lub radiany dla zgodności, pomnóż je przez `1&nbsp;deg`, `1&nbsp;°` lub `1&nbsp;rad`, odpowiednio, np. `(360 - X) * 1deg`; `(360 - X) * 1°`; `(0,5 + pi / 2) * 1rad`.
Obsługiwane są następujące funkcje trygonometryczne:

  Funkcja       Opis                                                                                                     Zakres wartości
  ------------- -------------------------------------------------------------------------------------------------------- ------------------------------------------------------
  acos(x)       [Arc cosine](https://pl.wikipedia.org/wiki/Funkcje_cyklometryczne#Basic_properties)                      -1 \<= x \<= 1
  asin(x)       [Arc sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)               -1 \<= x \<= 1
  atan(x)       [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties)            cały
  atan2(x, y)   [Arc tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions#Basic_properties) do *x/y*   cały, wyjątek y = 0
  cos(x)        [Cosine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)        cały
  cosh(x)       [Hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)         cały
  sin(x)        [Sine](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)          cały
  sinh(x)       [Hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)           cały
  tan(x)        [Tangent](https://en.wikipedia.org/wiki/Trigonometric_functions#Right-angled_triangle_definitions)       cały, z wyjątkiem x = n-90 przy n = liczba całkowita
  tanh(x)       [Hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Trigonometric_definitions)        cały

These functions for exponentiation and logarithmization are supported:

  Function    Description                                                                      Value range
  ----------- -------------------------------------------------------------------------------- -------------
  exp(x)      [Funkcja wykładnicza](https://pl.wikipedia.org/wiki/Funkcja_wyk%C5%82adnicza)    cały
  log(x)      [Logarytm naturalny](https://pl.wikipedia.org/wiki/Logarytm_naturalny)           x \> 0
  log10(x)    [Logarytm dziesiętny](https://pl.wikipedia.org/wiki/Logarytm_dziesi%C4%99tny)    x \> 0
  pow(x, y)   [Potęgowanie](https://pl.wikipedia.org/wiki/Pot%C4%99gowanie)                    cały
  sqrt(x)     [Pierwiastek kwadratowy](https://pl.wikipedia.org/wiki/Pierwiastek_kwadratowy)   x \>= 0

These functions for rounding, truncation and remainder are supported:

  Function    Description                                                                                                                Value range
  ----------- -------------------------------------------------------------------------------------------------------------------------- -------------------------
  abs(x)      [Wartość bezwzględna](https://pl.wikipedia.org/wiki/Warto%C5%9B%C4%87_bezwzgl%C4%99dna)                                    cały
  ceil(x)     [Funkcja sufitu](https://pl.wikipedia.org/wiki/Pod%C5%82oga_i_sufit), najmniejsza wartość całkowita większa lub równa x    cały
  floor(x)    [Funkcja podłogi](https://pl.wikipedia.org/wiki/Pod%C5%82oga_i_sufit), największa wartość całkowita mniejsza lub równa x   cały
  mod(x, y)   [Reszta](https://pl.wikipedia.org/wiki/Reszta) po podzieleniu \"\'x\'\" przez \"\'y\'                                      cały, z wyjątkiem y = 0
  round(x)    [Zaokrąglanie](https://pl.wikipedia.org/wiki/Zaokr%C4%85glanie) do najbliższej liczby całkowitej                           cały
  trunc(x)    [Obcinanie](https://pl.wikipedia.org/wiki/Obcinanie) do najbliższej liczby całkowitej w kierunku zera                      cały

### Funkcje statystyczne / agregujące 

[Funkcje agregujące](https://en.wikipedia.org/wiki/Aggregate_function) przyjmują jeden lub więcej argumentów.
Poszczególne argumenty funkcji agregujących mogą składać się z zakresów komórek. Zakres komórek jest wyrażony jako dwa odwołania do komórek oddzielone dwukropkiem {{Incode|:}}, na przykład {{Incode|average(B1:B8)}} lub {{Incode|sum(A1:A4; B1:B4)}}. Odwołania do komórek mogą również wykorzystywać aliasy komórek, na przykład {{Incode|average(StartTemp:KoniecTemp)}}. {{Version/pl|0.19}}.

Obsługiwane są następujące funkcje agregacji:

  Funkcja                  Opis                                                                                                                                            Zakres wartości
  ------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------- -----------------
  average(a; b; c; \...)   [Średnia](https://pl.wikipedia.org/wiki/%C5%9Arednia_arytmetyczna) wartość argumentów, tak samo jak sum(a; b; c; \...) / count(a; b; c; \...)   cały
  count(a; b; c; \...)     [Zlicz](https://en.wikipedia.org/wiki/Counting) wartość argumentów, zwykle używane dla zakresów komórek                                         cały
  max(a; b; c; \...)       [Maksimum](https://pl.wikipedia.org/wiki/Funkcje_minimum_i_maksimum) wartość argumentów                                                         cały
  min(a; b; c; \...)       [Minimum](https://pl.wikipedia.org/wiki/Funkcje_minimum_i_maksimum) wartość argumentów                                                          cały
  stddev(a; b; c; \...)    [Odchylenie standardowe](https://pl.wikipedia.org/wiki/Odchylenie_standardowe) wartości argumentów                                              cały
  sum(a; b; c; \...)       [Suma](https://pl.wikipedia.org/wiki/Sumowanie) wartości argumentów, typowo stosowane dla zakresów komórek                                      cały

### Operacje na ciągach znaków 

#### Rozpoznawanie łańcucha znaków 

Łańcuchy są identyfikowane w wyrażeniach przez otoczenie ich podwójnymi daszkami otwierającymi/zamykającymi *(podobnie jak etykiety)*.

W poniższym przykładzie \"TEXT\" jest rozpoznawany jako ciąg znaków : `<<TEXT>>`.

#### Łączenie łańcuchów znaków 

Łańcuchy mogą być sumowane przy użyciu znaku **+**.

Na przykład `<<Mój>> + <<TEKST>>` będzie złączone do \"MójTEKST\".

#### Formatowanie łańcucha znaków 

Formatowanie ciągów jest obsługiwane za pomocą *(starego)* sposobu środowiska Python w %-styl.

Wszystkie specyfikatory % są zdefiniowane w [dokumentacji](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting) środowiska Python.

Na przykład, zakładając, że masz sześcian o domyślnej długości boków 10 mm o nazwie \"Sześcian\" \--domyślne nazewnictwo FreeCAD\--, następujące wyrażenie `<<Długość sześcianu : %s>> % Box.Length` zostanie rozwinięte do \"Długość sześcianu : 10.0 mm\".

Ograniczeniem jest to, że tylko jeden %-specyfikator jest dozwolony w łańcuchu, więc musisz użyć łączenia łańcuchów, jeżeli potrzebujesz więcej niż jeden. W powyższej sytuacji, wyrażenie `<<Długość sześcianu wynosi %s>> % Box.Length + << a szerokość wynosi %s>> % Box.Width` zostanie rozwinięte do \"Długość sześcianu wynosi 10.0 mm a szerokość 10.0 mm\".

[Na forum](https://forum.freecadweb.org/viewtopic.php?f=8&t=58657) dostępny jest przykładowy plik FreeCAD wykorzystujący formatowanie ciągów znaków.

## Wyrażenia warunkowe 

Wyrażenia warunkowe mają postać `condition ? resultTrue : resultFalse`. Warunek jest zdefiniowany jako wyrażenie, które oblicza się albo jako `0` *(Fałsz)* lub niezerowe *(Prawda)*. Zauważ, że zamknięcie wyrażenia warunkowego w nawiasach jest obecnie uważane za błąd. {{VersionMinus/pl|0.19}}

Zdefiniowane są następujące [operatory relacyjne](https://en.wikipedia.org/wiki/Relational_operator#Standard_relational_operators):

  Operator   Opis
  ---------- --------------------
  **==**     jest równy
  **!=**     nie jest równy
  **\>**     większy niż
  **\<**     mniejszy niż
  **\>=**    większy lub równy
  **\<=**    mniejszy lub równy

## Jednostki

Jednostki mogą być używane bezpośrednio w wyrażeniach. Parser łączy je z poprzedzającą wartością. Tak więc wartość `2mm` lub `2 mm` jest zapisana poprawne, podczas gdy `mm` jest niepoprawna, ponieważ nie ma poprzedzającego określenia wielkości / ilości.

Wszystkie wartości muszą mieć swoją jednostkę. Dlatego musisz generalnie używać jednostki dla wartości w arkuszach kalkulacyjnych.
W niektórych przypadkach działa to nawet bez jednostki, na przykład jeśli masz np. w komórce B1 arkusza kalkulacyjnego tylko liczbę `1.5` i odnosisz się do niej jako do wysokości wyciągnięcia. Działa to tylko dlatego, że wysokość wyciągnięcia określa wstępnie jednostkę `mm`, która jest używana, jeśli nie podano jednostki. Nie powiedzie się jednak, jeśli jako wysokości wyciągnięcia użyjesz np. `Szkic1.Constraints.Width - Arkusz_kalkulacyjny.B1`, ponieważ `Szkic1.Constraints.Width` ma określoną jednostkę, a `Arkusz_kalkulacyjny.B1` nie.

Jednostki z wykładnikami mogą być wprowadzane bezpośrednio. Tak więc np. `mm^3` zostanie rozpoznane jako **mm³**, a `m^3` jako **m³**.

Jeśli masz zmienną, której nazwa jest jednostką, musisz umieścić ją pomiędzy `<< >>`, aby zapobiec rozpoznaniu jej jako jednostki. Na przykład, jeśli masz wymiar `Szkic.Constraints.A` to zostałby on rozpoznany jako jednostka ampera. Dlatego musisz zapisać go w wyrażeniu jako `Szkic.Constraints.<<A>>`.

Parser wyrażeń rozpoznaje następujące jednostki:

Ilość materii:

  Jednostka   Opis
  ----------- -----------------------------------------------
  mmol        Milli[mol](https://pl.wikipedia.org/wiki/Mol)
  mol         [Mol](https://pl.wikipedia.org/wiki/Mol)

Kąt:

  Jednostka   Opis
  ----------- ----------------------------------------------------------------------------------------------------
  °           [Stopień](https://pl.wikipedia.org/wiki/Stopie%C5%84_(k%C4%85t)); alternatywa dla jednostki *deg*
  deg         [Stopień](https://pl.wikipedia.org/wiki/Stopie%C5%84_(k%C4%85t)); alternatywa dla jednostki *°*
  rad         [Radian](https://pl.wikipedia.org/wiki/Radian)
  gon         [Gradian](https://en.wikipedia.org/wiki/Gon_(unit))
  S           [Sekunda kątowa](https://pl.wikipedia.org/wiki/Sekunda_k%C4%85towa)
  ″           [Sekunda kątowa](https://pl.wikipedia.org/wiki/Sekunda_k%C4%85towa); alternatywa dla jednostki *S*
  M           [Minuta kątowa](https://pl.wikipedia.org/wiki/Minuta_k%C4%85towa)
  ′           [Minuta kątowa](https://pl.wikipedia.org/wiki/Minuta_k%C4%85towa); alternatywa dla jednostki *M*

Prąd:

  Jednostka   Opis
  ----------- ---------------------------------------------------
  mA          Milli[amper](https://pl.wikipedia.org/wiki/Amper)
  A           [Amper](https://pl.wikipedia.org/wiki/Amper)
  kA          Kilo[amper](https://pl.wikipedia.org/wiki/Amper)
  MA          Mega[amper](https://pl.wikipedia.org/wiki/Amper)

Pojemność elektryczna:

  Jednostka   Opis
  ----------- ----------------------------------------------------------------------------------------------------------------------
  pF          Piko[farad](https://pl.wikipedia.org/wiki/Farad), {{Version/pl|0.19}}
  nF          Nano[farad](https://pl.wikipedia.org/wiki/Farad), {{Version/pl|0.19}}
  uF          Mikro[farad](https://pl.wikipedia.org/wiki/Farad); alternatywa dla jednostki *µF*, {{Version/pl|0.19}}
  µF          Mikro[farad](https://pl.wikipedia.org/wiki/Farad); alternatywa dla jednostki *uF*, {{Version/pl|0.19}}
  mF          Milli[farad](https://pl.wikipedia.org/wiki/Farad), {{Version/pl|0.19}}
  F           [Farad](https://pl.wikipedia.org/wiki/Farad); 1 F = 1 s\^4·A\^2/m\^2/kg, {{Version/pl|0.19}}

Przewodność elektryczna:

  Jednostka   Opis
  ----------- -------------------------------------------------------------------------------------------------------------------------
  uS          Mikro[siemens](https://pl.wikipedia.org/wiki/Simens); alternatywa dla jednostki *µS*, {{Version/pl|0.19}}
  µS          Mikro[siemens](https://pl.wikipedia.org/wiki/Simens); alternatywa dla jednostki *uS*, {{Version/pl|0.19}}
  mS          Milli[siemens](https://pl.wikipedia.org/wiki/Simens), {{Version/pl|0.19}}
  S           [Siemens](https://pl.wikipedia.org/wiki/Simens); 1 S = 1 s\^3·A\^2/kg/m\^2, {{Version/pl|0.19}}
  kS          Kilo[siemens](https://pl.wikipedia.org/wiki/Simens), {{Version/pl|0.20}}
  MS          Mega[siemens](https://pl.wikipedia.org/wiki/Simens), {{Version/pl|0.20}}

Indukcyjność elektryczna:

  Jednostka   Opis
  ----------- --------------------------------------------------------------------------------------------------------------------
  nH          Nano[henr](https://pl.wikipedia.org/wiki/Henr), {{Version/pl|0.19}}
  uH          Mikro[henr](https://pl.wikipedia.org/wiki/Henr); alternatywa dla jednostki *µH*, {{Version/pl|0.19}}
  µH          Mikro[henr](https://pl.wikipedia.org/wiki/Henr); alternatywa dla jednostki *uH*, {{Version/pl|0.19}}
  mH          Milli[henr](https://pl.wikipedia.org/wiki/Henr), {{Version/pl|0.19}}
  H           \[v Henry\]; 1 H = 1 kg·m\^2/s\^2/A\^2, {{Version/pl|0.19}}

Rezystancja elektryczna:

  Jednostka   Opis
  ----------- --------------------------------------------------------------------------------------------------------------------
  Ohm         [Om](https://pl.wikipedia.org/wiki/Om_(jednostka)); 1 Ohm = 1 kg·m\^2/s\^3/A\^2, {{Version/pl|0.19}}
  kOhm        Kilo[om](https://pl.wikipedia.org/wiki/Om_(jednostka)), {{Version/pl|0.19}}
  MOhm        Mega[om](https://pl.wikipedia.org/wiki/Om_(jednostka)), {{Version/pl|0.19}}

Ładunek elektryczny:

  Jednostka   Opis
  ----------- ------------------------------------------------------------------------------------------------
  C           [Kolumb](https://pl.wikipedia.org/wiki/Kulomb); 1 C = 1 A·s, {{Version/pl|0.19}}

Potencjał elektryczny:

  Jednostka   Opis
  ----------- -------------------------------------------------
  mV          Milli[wolt](https://pl.wikipedia.org/wiki/Wolt)
  V           [Wolt](https://pl.wikipedia.org/wiki/Wolt)
  kV          Kilo[wolt](https://pl.wikipedia.org/wiki/Wolt)

Energia / praca:

  Jednostka   Opis
  ----------- ---------------------------------------------------------------------------------------------------------------------------
  mJ          Milli[dżul](https://pl.wikipedia.org/wiki/D%C5%BCul)
  J           [Dżul](https://pl.wikipedia.org/wiki/D%C5%BCul)
  kJ          Kilo[dżul](https://en.wikipedia.org/wiki/Joule), {{Version/pl|0.19}}
  eV          [Elektronowolt](https://pl.wikipedia.org/wiki/Elektronowolt), 1 ev = 1.602176634e-19 J, {{Version/pl|0.19}}
  keV         Kilo[elektronowolt](https://pl.wikipedia.org/wiki/Elektronowolt), {{Version/pl|0.19}}
  MeV         Mega[elektronowolt](https://pl.wikipedia.org/wiki/Elektronowolt), {{Version/pl|0.19}}
  kWh         [Kilowatogodzina](https://pl.wikipedia.org/wiki/Kilowatogodzina), 1 kWh = 3.6e6 J, {{Version/pl|0.19}}
  Ws          [Watosekunda](https://pl.wikipedia.org/wiki/D%C5%BCul), alternatywa dla jednostki *Dżul*
  VAs         [Woltoamperosekunda](https://pl.wikipedia.org/wiki/D%C5%BCul), alternatywa dla jednostki *Dżul*
  CV          [Kulomb-wolt](https://pl.wikipedia.org/wiki/D%C5%BCul), alternatywa dla jednostki *Dżul*
  cal         [Kaloria](https://pl.wikipedia.org/wiki/Kaloria), 1 cal = 4.184 J, {{Version/pl|0.19}}
  kcal        Kilo[kaloria](https://pl.wikipedia.org/wiki/Kaloria), {{Version/pl|0.19}}

Siła:

  Jednostka   Opis
  ----------- -----------------------------------------------------------
  mN          Milli[niuton](https://pl.wikipedia.org/wiki/Niuton)
  N           [Niuton](https://pl.wikipedia.org/wiki/Niuton)
  kN          Kilo[niuton](https://pl.wikipedia.org/wiki/Niuton)
  MN          Mega[niuton](https://pl.wikipedia.org/wiki/Niuton)
  lbf         [Funt-siła](https://pl.wikipedia.org/wiki/Funt-si%C5%82a)

Długość:

  Jednostka   Opis
  ----------- ----------------------------------------------------------------------------------------------------------------
  nm          Nano[metr](https://pl.wikipedia.org/wiki/Metr)
  mu          Micro[metr](https://pl.wikipedia.org/wiki/Metr), alternatywa dla jednostki *µm*
  µm          Micro[metr](https://pl.wikipedia.org/wiki/Metr), alternatywa dla jednostki *mu*
  mm          Milli[metr](https://pl.wikipedia.org/wiki/Metr)
  cm          Centi[metr](https://pl.wikipedia.org/wiki/Metr)
  dm          Deci[metr](https://pl.wikipedia.org/wiki/Metr)
  m           [Metr](https://pl.wikipedia.org/wiki/Metr)
  km          Kilo[metr](https://pl.wikipedia.org/wiki/Metr)
  mil         [Tysięczne części cala](https://en.wikipedia.org/wiki/Thousandth_of_an_inch), alternatywa dla jednostki *thou*
  thou        [Tysięczne części cala](https://en.wikipedia.org/wiki/Thousandth_of_an_inch), alternatywa dla jednostki *mil*
  in          [Cal](https://pl.wikipedia.org/wiki/Cal)
  ft          [Stopa](https://pl.wikipedia.org/wiki/Stopa_(miara)), alternatywa dla jednostki \'
  \'          [Stopa](https://pl.wikipedia.org/wiki/Stopa_(miara)), alternatywa dla jednostki *ft*
  yd          [Jard](https://pl.wikipedia.org/wiki/Jard)
  mi          [Mila](https://pl.wikipedia.org/wiki/Mila_(jednostka_d%C5%82ugo%C5%9Bci))

Natężenie światła:

  Jednostka   Opis
  ----------- --------------------------------------------------
  cd          [Kandela](https://pl.wikipedia.org/wiki/Kandela)

Natężenie pola magnetycznego:

  Jednostka   Opis
  ----------- --------------------------------------------------------------------------------------------------------
  Oe          [Ersted](https://pl.wikipedia.org/wiki/Ersted); 1 Oe = 79.57747 A/m, {{Version/pl|0.19}}

Strumień magnetyczny:

  Jednostka   Opis
  ----------- -----------------------------------------------------------------------------------------------------------------------
  Wb          [Weber](https://pl.wikipedia.org/wiki/Weber_(jednostka)); 1 Wb = 1 kg\*m\^2/s\^2/A, {{Version/pl|0.19}}

Gęstość strumienia magnetycznego:

  Jednostka   Opis
  ----------- ----------------------------------------------------------------------------------------------------------------
  G           [Gaus](https://pl.wikipedia.org/wiki/Gaus); 1 G = 1 e-4 T, {{Version/pl|0.19}}
  T           [Tesla](https://pl.wikipedia.org/wiki/Tesla_(jednostka)); 1 T = 1 kg/s\^2/A, {{Version/pl|0.19}}

Masa:

  Jednostka   Opis
  ----------- ------------------------------------------------------------------------------------
  ug          Micro[gram](https://pl.wikipedia.org/wiki/Gram), alternatywa dla jednostki *µg*
  µg          Micro[gram](https://pl.wikipedia.org/wiki/Gram), alternatywa dla jednostki *ug*
  mg          Milli[gram](https://pl.wikipedia.org/wiki/Gram)
  g           [Gram](https://pl.wikipedia.org/wiki/Gram)
  kg          Kilo[gram](https://pl.wikipedia.org/wiki/Gram)
  t           [Tona](https://pl.wikipedia.org/wiki/Tona)
  oz          [Uncja](https://pl.wikipedia.org/wiki/Uncja)
  lb          [Funt](https://pl.wikipedia.org/wiki/Funt_(masa)), alternatywa dla jednostki *lbm*
  lbm         [Funt](https://pl.wikipedia.org/wiki/Funt_(masa)), alternatywa dla jednostki *lb*
  st          [Kamień](https://pl.wikipedia.org/wiki/Kamie%C5%84_(miara))
  cwt         [Waga stu-kilowa *(kwintał)*](https://pl.wikipedia.org/wiki/Kwintal)

Siła:

  Jednostka   Opis
  ----------- ---------------------------------------------------------------------------------
  W           [Wat](https://pl.wikipedia.org/wiki/Wat)
  kW          Kilo[wat](https://pl.wikipedia.org/wiki/Wat), {{Version/pl|0.19}}
  VA          [Voltamper](https://pl.wikipedia.org/wiki/Woltamper)

Ciśnienie:

  Jednostka   Opis
  ----------- -------------------------------------------------------------------------------------------------------------
  Pa          [Paskal](https://pl.wikipedia.org/wiki/Paskal)
  kPa         Kilo[paskal](https://pl.wikipedia.org/wiki/Paskal)
  MPa         Mega[paskal](https://pl.wikipedia.org/wiki/Paskal)
  GPa         Giga[paskal](https://pl.wikipedia.org/wiki/Paskal)
  mbar        Milli[Bar](https://pl.wikipedia.org/wiki/Bar_(jednostka)), {{Version/pl|0.19}}
  bar         [Bar](https://en.wikipedia.org/wiki/Bar_(unit)), {{Version/pl|0.19}}
  uTorr       Micro[tor](https://pl.wikipedia.org/wiki/Tor_(jednostka)), alternatywa dla jednostki *µTorr*
  µTorr       Micro[tor](https://pl.wikipedia.org/wiki/Tor_(jednostka)), alternatywa dla jednostki *uTorr*
  mTorr       Milli[tor](https://pl.wikipedia.org/wiki/Tor_(jednostka))
  Torr        [Tor](https://pl.wikipedia.org/wiki/Tor_(jednostka)); 1 Torr = 133.32 Pa
  psi         [Funt na cal kwadratowy](https://pl.wikipedia.org/wiki/Psi_(jednostka)); 1 psi = 6.895 kPa
  kpsi        Kilo[Funt na cal kwadratowy](https://pl.wikipedia.org/wiki/Psi_(jednostka))
  Mpsi        Mega[Funt na cal kwadratowy](https://pl.wikipedia.org/wiki/Psi_(jednostka)), <small>(v0.19)</small> 

Temperatura:

  Jednostka   Opis
  ----------- -------------------------------------------------------------------------------------
  uK          Micro[kelwin](https://pl.wikipedia.org/wiki/Kelwin), alternatywa dla jednostki *µK*
  µK          Micro[kelwin](https://pl.wikipedia.org/wiki/Kelwin), alternatywa dla jednostki *uK*
  mK          Milli[kelwin](https://pl.wikipedia.org/wiki/Kelwin)
  K           [Kelwin](https://pl.wikipedia.org/wiki/Kelwin)

Czas:

  Jednostka   Opis
  ----------- -----------------------------------------------------------------------------------
  s           [Second](https://pl.wikipedia.org/wiki/Sekunda)
  min         [Minuta](https://pl.wikipedia.org/wiki/Minuta)
  h           [Godzina](https://pl.wikipedia.org/wiki/Godzina)
  Hz (1/s)    [Herc](https://pl.wikipedia.org/wiki/Herc), {{Version/pl|0.19}}
  kHz         Kilo[herc](https://pl.wikipedia.org/wiki/Herc), {{Version/pl|0.19}}
  MHz         Mega[herc](https://pl.wikipedia.org/wiki/Herc), {{Version/pl|0.19}}
  GHz         Giga[herc](https://pl.wikipedia.org/wiki/Herc), {{Version/pl|0.19}}
  THz         Tera[herc](https://pl.wikipedia.org/wiki/Herc), {{Version/pl|0.19}}

Objętość:

  Jednostka   Opis
  ----------- --------------------------------------------------------------------------------------------------
  ml          Milli[litr](https://pl.wikipedia.org/wiki/Litr), {{Version/pl|0.19}}
  l           [Litr](https://pl.wikipedia.org/wiki/Litr)
  cft         [stopa sześcienna](https://en.wikipedia.org/wiki/Foot_(unit)), {{Version/pl|0.19}}

Specjalne jednostki brytyjskie:

  Jednostka   Opis
  ----------- ----------------------------------------------------------------------------------------------------------
  mph         [Mila na godzinę](https://pl.wikipedia.org/wiki/Mila_na_godzin%C4%99), {{Version/pl|0.19}}
  sqft        [Stopa kwadratowa](https://pl.wikipedia.org/wiki/Stopa_angielska), {{Version/pl|0.19}}

Poniższe popularnie używane jednostki nie są jeszcze obsługiwane:

  Jednostka   Opis                                                                                                                 Zamiennik
  ----------- -------------------------------------------------------------------------------------------------------------------- --------------------------
  °C          [Celsjusz](https://pl.wikipedia.org/wiki/Skala_Celsjusza)                                                            \[°C\] + 273.15 K
  °F          [Fahrenheit](https://pl.wikipedia.org/wiki/Skala_Fahrenheita);                                                       (\[°F\] + 459.67) × ​5/9
  u           [Jednostka masy atomowej](https://pl.wikipedia.org/wiki/Jednostka_masy_atomowej), alternatywa dla jednostki \'Da\'   1.66053906660e-27 kg
  Da          [Dalton](https://pl.wikipedia.org/wiki/Jednostka_masy_atomowej), alternatywa dla jednostki \'u\'                     1.66053906660e-27 kg
  sr          [Steradian](https://pl.wikipedia.org/wiki/Steradian)                                                                 nie bezpośrednio
  lm          [Lumen](https://pl.wikipedia.org/wiki/Lumen)                                                                         nie bezpośrednio
  lx          [Luks](https://pl.wikipedia.org/wiki/Luks_(fotometria))                                                              nie bezpośrednio
  px          [Piksel](https://pl.wikipedia.org/wiki/Piksel)                                                                       nie bezpośrednio

## Nieprawidłowe znaki i nazwy 

Funkcja wyrażeń jest bardzo potężna, ale aby osiągnąć tę moc, ma pewne ograniczenia dotyczące niektórych znaków. Aby temu zaradzić, FreeCAD oferuje możliwość używania etykiet i odwoływania się do nich zamiast do nazw obiektów. W etykietach można używać prawie wszystkich znaków specjalnych.

W przypadkach, w których nie można użyć etykiety, takich jak nazwa wiązań szkicu, należy być świadomym, których znaków nie wolno używać.

### Etykiety

Dla [etykiet](Object_name/pl#Etykieta.md) nie ma nieprawidłowych znaków, jednak niektóre znaki muszą być wyprowadzone:

+----------------------------------------------------------+----------------------------------------------------------------------------------------+
| Znak                                                     | Opis                                                                                   |
+==========================================================+========================================================================================+
|                                           | Wymaga wyprowadzenia poprzez dodanie znaku poprzedzającego `\`. |
| `'`                                             |                                                                                        |
|                                                       |                                                                                        |
| , `\`, `"` |                                                                                        |
+----------------------------------------------------------+----------------------------------------------------------------------------------------+

Na przykład etykieta `Sketch\002` musi być określona jako `<<Sketch\\002>>`.

### Nazwy

[Nazwy](Object_name#Name.md) obiektów takich jak wymiary, szkice itp. nie mogą posiadać znaków lub sekwencji znaków wymienionych poniżej, w przeciwnym razie nazwa jest niepoprawna:

  Znak / Ciąg znaków                                                                                                                             Opis
  ---------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  **+**, **-**, **\***, **/**, **\^**, **\_**, **\<**, **\>**, **(**, **)**, **{**, **}**, **\[**, **\]**, **.**, **,**, **=**                   Znaki, które są operatorami matematycznymi lub częścią konstrukcji matematycznych
  **A**, **kA**, **mA**, **MA**, **C**, **G**, **F**, **mF**, **µF**, **J**, **K**, \'\'\' \' \'\'\', \'\'\' ft \'\'\', **°**, i wiele więcej!   Znaki i ich ciągi, które są [jednostkami](Expressions/pl#Jednostki.md)
  **\#**, **!**, **?**, **§**, **\$**, **%**, **&**, **:**, **;**, **\\**, **\|**, **\~**, **∆**, **¿**, i wiele więcej!                         Znaki używane jako symbol listy lub wyzwalają specjalne operacje
  **pi**, **e**                                                                                                                                  Stałe matematyczne
  **´**, **\**, \'\'\' \' \'\'\', **\"**                                                                                                        Znaki używane do akcentowania
  spacja                                                                                                                                         Spacja określa koniec nazwy i dlatego nie może być użyta

Na przykład, prawidłowa jest następująca nazwa: `<<Sketch>>.Constraints.T2üßµ@`. Natomiast następujące nazwy są niepoprawne: `<<Sketch>>.Constraints.test\result_2` *(\\r oznacza \"powrót karetki\")* lub `<<Sketch>>.Constraints.mol` *(mol to jednostka)*.

Ponieważ krótsze nazwy *(zwłaszcza jeśli mają tylko jeden lub dwa znaki)* mogą łatwo doprowadzić do nieprawidłowych nazw, rozważ użycie dłuższych nazw i / lub ustalenie odpowiedniej konwencji nazewnictwa.

### Przypisania do komórek 

Dla [aliasów komórek arkusza kalkulacyjnego](Spreadsheet_SetAlias/pl.md) dozwolone są tylko znaki alfanumeryczne i podkreślenia (`A` do `Z`, `a` do `z`, `0` do `9` oraz `_`).

## Odwołanie do danych CAD 

Możliwe jest użycie danych zawartych w samym modelu w wyrażeniu. Aby odwołać się do właściwości użyj`object.property`. Jeśli właściwość jest złożeniem pól, poszczególne pola mogą być dostępne jako `object.property.field`.

Poniższa tabela przedstawia kilka przykładów:

+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dane CAD                                           | Odwołanie do wyrażenia                | Wynik                                                                                                                                                                        |
+====================================================+=======================================+==============================================================================================================================================================================+
| Parametr długości sześcianu środowiska pracy Część |                        | Długość w mm                                                                                                                                                                 |
|                                                    | `Cube.Length`                |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Objętość sześcianu                                 |                        | Objętość w mm³ bez jednostek                                                                                                                                                 |
|                                                    | `Cube.Shape.Volume`          |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Typ kształtu sześcianu                             |                        | String: Bryła                                                                                                                                                                |
|                                                    | `Cube.Shape.ShapeType`       |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Etykieta sześcianu                                 |                        | String: Etykieta                                                                                                                                                             |
|                                                    | `Cube.Label`                 |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Współrzędna x środka masy sześcianu                |                        | Współrzędna x w mm, bez jednostek                                                                                                                                            |
|                                                    | `Cube.Shape.CenterOfMass.x`  |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wartość wiązania w szkicu                          |                        | Wartość numeryczna nazwanego wiązania `Width` w szkicu, jeśli wyrażenie jest używane w samym szkicu.                                                  |
|                                                    | `Constraints.Width`          |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wartość wiązania w szkicu                          |                        | Wartość numeryczna nazwanego wiązania `Width` w szkicu, jeśli wyrażenie jest używane poza szkicem.                                                    |
|                                                    | `MySketch.Constraints.Width` |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wartość aliasu arkusza kalkulacyjnego              |                        | Wartość aliasu `Depth` w arkuszu kalkulacyjnym `Spreadsheet`                                                                   |
|                                                    | `Spreadsheet.Depth`          |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Wartość lokalnej właściwości                       |                        | Wartość właściwości **Length** np. w obiekcie Pad, jeżeli wyrażenie jest użyte np. w **Length2** w tym samym obiekcie. |
|                                                    | `Length`                     |                                                                                                                                                                              |
|                                                    |                                    |                                                                                                                                                                              |
+----------------------------------------------------+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## Zmienne globalne w obrębie dokumentu 

W tej chwili w programie FreeCAD nie ma koncepcji zmiennych globalnych. Zamiast tego zmienne mogą być definiowane jako komórki w arkuszu kalkulacyjnym za pomocą środowiska roboczego [Arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md), a następnie można im nadać nazwę za pomocą właściwości aliasu dla komórki *(kliknij prawym przyciskiem myszy na komórkę)*. Następnie można się do nich odwoływać z dowolnego wyrażenia, tak jak do innych właściwości obiektu.

## Powiązania między dokumentami 

Możliwe jest *(z ograniczeniami)* zdefiniowanie właściwości obiektu w bieżącym dokumencie *(plik \".FCstd\")* za pomocą Wyrażenia odwołującego się do właściwości obiektu znajdującego się w innym dokumencie *(plik \".FCstd\")*. Na przykład, komórka w arkuszu kalkulacyjnym lub właściwość {{PropertyData/pl|Długość}} sześcianu środowiska Część itp. w jednym dokumencie mogą być zdefiniowane przez Wyrażenie, które odwołuje się do wartości X Umiejscowienia lub innej właściwości obiektu znajdującego się w innym dokumencie.

Nazwa dokumentu jest używana do odwoływania się do jego zawartości z innych dokumentów. Przy pierwszym zapisie dokumentu wybieramy nazwę pliku, która zazwyczaj różni się od początkowej domyślnej nazwy \"Nienazwany1\". Aby uniknąć utraty linków w przypadku zmiany nazwy dokumentu głównego przy zapisie, zaleca się najpierw utworzenie dokumentu głównego, utworzenie w nim arkusza kalkulacyjnego i zapisanie go. Następnie można nadal wprowadzać zmiany w pliku i jego arkuszu kalkulacyjnym, ale nie należy modyfikować jego nazwy.

Po utworzeniu i zapisaniu *(nazwaniu)* dokumentu głównego z arkuszem kalkulacyjnym można bezpiecznie tworzyć dokumenty zależne. Na przykład, zakładając, że nazwiesz dokument główny `master`, arkusz kalkulacyjny `modelConstants` i nadasz komórce alias nazwy `Length`, możesz następnie uzyskać dostęp do wartości jako:

`master#modelConstants.Length`

**Uwaga:**, Dokument źródłowy musi być wczytany, aby wartości z dokumentu źródłowego były dostępne dla dokumentu powiązanego.

Niestety, zintegrowany program sprawdzający czasami twierdzi, że prawidłowa nazwa nie istnieje. Mimo to kontynuuj wpisywanie. Po wprowadzeniu kompletnego odwołania, przycisk **OK** stanie się aktywny.

Oczywiście, to do Ciebie zależy, czy wczytasz odpowiednie dokumenty później, gdy będziesz chciał coś zmienić.

## Znane problemy / niezrealizowane zadania 

-   Graf zależności oparty jest na relacjach pomiędzy obiektami dokumentu, a nie na właściwościach. Oznacza to, że nie można dostarczać danych do obiektu i odpytywać tego samego obiektu o wyniki. Na przykład, nawet jeśli nie ma cyklicznych zależności, gdy brane są pod uwagę same właściwości, nie można mieć obiektu, który pobiera swoje wymiary z arkusza kalkulacyjnego, a następnie wyświetlać objętość tego obiektu w tym samym arkuszu kalkulacyjnym. Aby obejść ten problem, należy użyć wielu arkuszy kalkulacyjnych, jednego do napędzania modelu, a drugiego do raportowania.
-   Parser wyrażeń nie radzi sobie dobrze z nawiasami i nie jest w stanie poprawnie przetworzyć niektórych wyrażeń. Na przykład: `<nowiki>=</nowiki> (A1 > A2) ? 1 : 0` skutkuje błędem, podczas gdy `<nowiki>=</nowiki> A1 > A2 ? 1 : 0` jest akceptowane. Wyrażenie `<nowiki>=</nowiki> 5 + ((A1>A2) ? 1 : 0)` nie może być wprowadzone w żadnej formie.
-   Jak wspomniano powyżej, niestety zintegrowany moduł sprawdzający czasami twierdzi, że prawidłowa nazwa nie istnieje. Mimo to kontynuuj wpisywanie. Po wpisaniu pełnego odwołania, przycisk **OK** stanie się aktywny.
-   FreeCAD nie ma zaimplementowanego menedżera wyrażeń, w którym wszystkie wyrażenia w dokumencie byłyby wymienione i mogłyby być tworzone, usuwane, wyszukiwane itd. Ale jest dostępny odpowiedni dodatek: [fcxref](https://github.com/gbroques/fcxref).
-   Otwarte błędy/tickety dotyczące wyrażeń można znaleźć w [FreeCAD Bugtracker kategoria Wyrażenia](https://freecadweb.org/tracker/set_project.php?project_id=4;20)


{{Powerdocnavi

}} 

[Category:Spreadsheet](Category:Spreadsheet.md)
