---
 GuiCommand:
   Name: Sketcher ConstrainTangent
   Name/pl: Szkicownik: Wiązanie styczności
   MenuLocation: Sketch , Wiązania szkicownika , Wiązanie styczności
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **T**
   SeeAlso: 
---

# Sketcher ConstrainTangent/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainTangent.svg  style="width:24px;"> **Wiązanie styczności** umożliwia ustawienie dwóch krawędzi lub osi jako stycznych. Linie są traktowane jako nieskończone, a otwarte krzywe są również praktycznie rozszerzone. Wiązanie może również łączyć dwie krawędzie, wymuszając ich styczność w miejscu połączenia. Jeśli wybrane zostaną dwie linie lub linia i punkt końcowy innej linii, linie te staną się współliniowe.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> '''Wiązanie styczności lub współliniowe'''**.

    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Wiązanie styczności lub współliniowe**.

    -   
        <small>(v1.0)</small> 
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view.md) i wybierz **Wiązanie → <img src="images/Sketcher_ConstrainTangent.svg" width=16px> Wiązanie styczności lub współliniowe** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **T**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwie krawędzie. Krawędzie mogą być dowolne z wyjątkiem krawędzi krzywej złożonej.
    -   Wybierz punkt i dwie krawędzie *(w tej kolejności)*.
    -   Wybierz krawędź, punkt i inną krawędź *(w tej samej kolejności)*.
5.  Dodawane jest wiązanie styczne. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz akapit [z przykładem](#Między_dwiema_krawędziami.md).
6.  Opcjonalnie kontynuuj tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwie krawędzie *(patrz wyżej)*.
    -   Wybierz dwa punkty końcowe należące do różnych krawędzi.
    -   Wybierz krawędź i punkt końcowy innej krawędzi *(w dowolnej kolejności)*.
    -   Wybierz punkt i dwie krawędzie *(analogicznie)*.
2.  Wywołaj narzędzie jak wyjaśniono powyżej lub z następującą dodatkową opcją:
    -   
        <small>(v1.0)</small> 
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz **<img src="images/Sketcher_ConstrainTangent.svg" width=16px> Wiązanie styczności lub współliniowe** z menu podręcznego.
3.  Zostanie dodane wiązanie styczności. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz akapit [z przykładem](#Między_dwiema_krawędziami.md).



## Przykłady



### Między dwiema krawędziami 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width:400px;">

Dwie krawędzie stają się styczne. Jeśli jedna z krawędzi jest [stożkiem](Sketcher_Workbench/pl#Sketcher_CompCreateConic.md), dodawany jest [obiekt punktu](Sketcher_CreatePoint/pl.md), który ma [wiązanie punk na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) z obiema *(przedłużonymi)* krawędziami.

Nie zaleca się rekonstrukcji punktu styczności poprzez ręczne utworzenie punktu i związanie go tak, aby leżał na obu krzywych. Będzie to działać, ale zbieżność będzie znacznie wolniejsza, bardziej skokowa i będzie wymagać około dwa razy więcej iteracji niż normalnie. Jeśli potrzebny jest punkt styczny, wybierz dwie krawędzie i istniejący punkt.



### Między dwoma punktami końca 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width:400px;">

Punkty końcowe są zbieżne, a kąt między krawędziami w tym punkcie jest ustawiony na 180° *(gładkie połączenie)* lub 0° *(ostre połączenie)*, w zależności od położenia krawędzi przed zastosowaniem wiązania.



### Między krawędzią a punktem końcowym 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width:400px;">

Punkt końcowy jednej krawędzi jest związany tak, aby leżał na drugiej krawędzi, a krawędzie są styczne w tym punkcie.



### Między dwiema krawędziami w punkcie 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width:400px;">

Dwie krawędzie są styczne w danym punkcie. Punktem może być dowolny punkt, np. środek okręgu, punkt końcowy krawędzi lub początek, może on należeć do jednej z krawędzi, a także może być [obiektem punktu](Sketcher_CreatePoint/pl.md). W razie potrzeby dodawane są wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md), aby zapewnić, że punkt leży na obu *(przedłużonych)* krawędziach. Te dodatkowe wiązania nazywane są [wiązaniami pomocniczymi](Sketcher_helper_constraint/pl.md).

W porównaniu z bezpośrednią stycznością, to wiązanie jest wolniejsze, ponieważ wiąże się z nim więcej stopni swobody, ale jeśli punkt styczności jest potrzebny, jest to zalecane, ponieważ zapewnia lepszą zbieżność.



### Pomiędzy dwiema liniami 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width:400px;">

Obie linie są współliniowe.



## Tworzenie skryptów 

Wiązanie styczności może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji: 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` gdzie:

  - `Sketch` jest obiektem typu szkic

  - `icurve1`, `icurve2` są dwiema liczbami całkowitymi określającymi krzywe, które mają być styczne. Liczby całkowite to wskaźniki w szkicu *(wartość zwracana przez`Sketch.addGeometry`)*.

  - `pointpos1`, `pointpos2` powinny wynosić `1` dla punktu początkowego i `2` dla punktu końcowego.

  - `geoidpoint` oraz `pointpos` w `TangentViaPoint` są wskaźnikami określającymi punkt styczności.

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` i `pointpos`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/pl
