---
 GuiCommand:
   Name: Sketcher ConstrainAngle
   Name/pl: Szkicownik: Wiązanie kąta
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie kąta
   Workbenches: Sketcher Workbench/pl
   Shortcut: **K** **A**
   SeeAlso: Sketcher_ConstrainDistance/pl, Sketcher_ConstrainPerpendicular/pl
---

# Sketcher ConstrainAngle/pl



## Opis

Wiązanie kąta jest [wiązaniem odniesienia](Sketcher_Workbench/pl#Wiązania_w_szkicowniku.md) przeznaczonym do ustalania kątów na szkicach. Jest w stanie wyznaczyć nachylenia poszczególnych linii, kąty między liniami, kąty przecięcia łuków oraz rozpiętości kątowe łuków kołowych.



## Użycie

Istnieją cztery różne sposoby zastosowania tego wiązania:

-   do pojedynczych linii
-   pomiędzy liniami
-   do przecinających się krzywych
-   do łuków okręgów

Aby zastosować wiązanie kąta, należy wykonać następujące czynności:

1.  Wybierz jeden, dwa lub trzy elementy na szkicu. Tryb wiązania zostanie wybrany automatycznie w zależności od dokonanego wyboru.
2.  Wywołaj wiązanie za pomocą kilku metod:
    -   Wciskając przycisk **[<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> [Wiązanie kąta](Sketcher_ConstrainAngle/pl.md)** na pasku narzędzi.
    -   Używając skrótu klawiaturowego **K** kolejnie **A**.
    -   Używając z menu głównego **Szkicownik → Wiązania szkicownika → [<img src=images/Sketcher_ConstrainAngle.svg style="width:16px"> Wiązanie kąta**
3.  Zostanie wywołane okno dialogowe edycji danych.
4.  Zmodyfikuj wartość kąta, jeśli to konieczne. Kąt może być wprowadzony jako wyrażenie, które zostanie obliczone i wynik zostanie zapisany.
5.  Kliknij przycisk **OK**.

Jak w przypadku każdego wiązania odniesienia, istnieje możliwość późniejszej zmiany wartości kąta poprzez dwukrotne kliknięcie na pozycji wiązania w liście wiązań lub oknie widoku 3d. Wprowadzenie ujemnej wartości spowoduje odwrócenie kierunku kąta.



## Tryby wiązania 



### Kąt nachylenia linii 

**Wybór zaakceptowany:** linia

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:600px;">

Wiązanie to określa kąt biegunowy kierunku linii. Jest to kąt pomiędzy linią a osią X szkicu.



### Rozpiętość łuku okręgu 

**Wybór zaakceptowany:** łuk koła

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:600px;">

W tym trybie wiązanie ustala rozpiętość kątową łuku koła.



### Pomiędzy liniami 

**Wybór zaakceptowany:** linia + linia

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:600px;">

W tym trybie wiązanie ustawia kąt pomiędzy dwoma liniami. Nie jest wymagane, aby te linie się przecinały.



### Między krzywymi na przecięciu *(kąt w punkcie)* 

**Wybór zaakceptowany:** dowolna linia / krzywa + dowolna linia / krzywa + dowolny punkt

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:600px;">

W tym trybie, kąt pomiędzy dwoma krzywymi jest związany w punkcie ich przecięcia. Punkt przecięcia może znajdować się na przedłużeniach krzywych. Punkt ten powinien być wyraźnie określony, ponieważ krzywe zwykle przecinają się w więcej niż jednym punkcie.

Aby wiązanie działało prawidłowo, punkt musi znajdować się na obu krzywych. Tak więc, w miarę wywoływania wiązania, punkt będzie automatycznie powiązany z obiema krzywymi *([wiązanie pomocnicze](Sketcher_helper_constraint.md) zostanie dodane, jeśli będzie to konieczne)*, a kąt pomiędzy krzywymi będzie powiązany w tym punkcie. Te [wiązania pomocnicze](Sketcher_helper_constraint.md) są zwykłymi wiązaniami regularnymi. Mogą być dodane ręcznie lub usunięte. Na przykładowym rysunku powyżej nie ma żadnych wiązań pomocniczych, ponieważ wybrany punkt jest już punktem przecięcia krzywych.



## Tworzenie skryptów 

Ograniczenie kąta może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli [Pyton](Python/pl.md) za pomocą następujących narzędzi: 
```python
# line slope angle
Sketch.addConstraint(Sketcher.Constraint('Angle',iline,angle))

# angular span of arc
Sketch.addConstraint(Sketcher.Constraint('Angle',iarc,angle))

# angle between lines
Sketch.addConstraint(Sketcher.Constraint('Angle',iline1,pointpos1,iline2,pointpos2,angle))

# angle-via-point (no helper constraints are added automatically when from python)
Sketch.addConstraint(Sketcher.Constraint('AngleViaPoint',icurve1,icurve2,geoidpoint,pointpos,angle))
``` gdzie:

  - `Sketch` jest obiektem typu szkic,

  - `iline, iline1, iline2` są liczbami całkowitymi określającymi wiersze za pomocą ich liczb porządkowych w obiekcie `Sketch`.

  - `pointpos1, pointpos2` przyjmuje wartość 1 dla punktu początkowego i 2 dla końcowego. Wybór punktów końcowych pozwala na ustawienie kąta wewnętrznego *(lub zewnętrznego)*, a także wpływa na sposób narysowania wiązania na ekranie,

  - `geoidpoint` oraz `pointpos` w `AngleViaPoint` są indeksami określającymi punkt przecięcia,

  - `angle` to wartość kąta w radianach. Kąt jest liczony pomiędzy wektorami stycznymi w kierunku przeciwnym do ruchu wskazówek zegara. to wartość kąta w radianach. Kąt jest liczony pomiędzy wektorami stycznymi w kierunku przeciwnym do ruchu wskazówek zegara. Wektory styczne dla linii są wskazywane od punktu początkowego do końcowego *(lub odwrotnie, jeżeli punkt końcowy jest podany w trybie kąta między liniami)*, zgodnie z kierunkiem przeciwnym do ruchu wskazówek zegara. Ilość jest również przyjmowana jako kąt (np. `App.Units.Quantity('45 deg')`)

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `iline`, `iline1`, `iline2`, `pointpos1`, `pointpos2`, `geoidpoint` i `pointpos`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainAngle/pl
