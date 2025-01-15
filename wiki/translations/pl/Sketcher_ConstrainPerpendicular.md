---
 GuiCommand:
   Name: Sketcher ConstrainPerpendicular
   Name/pl: Szkicownik: Wiązanie prostopadłości
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie prostopadłości
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **N**
   SeeAlso: Sketcher_ConstrainAngle/pl
---

# Sketcher ConstrainPerpendicular/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainPerpendicular.svg  style="width:24px;"> **Wiązanie prostopadłości** wymusza prostopadłość dwóch linii lub dwóch krawędzi lub osi. Linie są traktowane jako nieskończone, a otwarte krzywe są również wirtualnie wydłużone. Wiązanie może również łączyć dwie krawędzie, wymuszając ich prostopadłość w miejscu połączenia.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> '''Wiązanie prostopadłości'''**.

    -   Wybierz z menu **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Wiązanie prostopadłości**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz **Wiązanie → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Wiązanie prostopadłości** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **N**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwie krawędzie. Jedna z krawędzi musi być linią prostą lub osią. Druga może być dowolną krawędzią z wyjątkiem krzywej złożonej.
    -   Wybierz punkt i dwie krawędzie *(w tej kolejności)*.
    -   Wybierz krawędź, punkt i inną krawędź *(w tej samej kolejności)*.
5.  Dodawane jest wiązanie prostopadłe. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz [przykłady](#Between_two_edges_at_point/pl.md).
6.  Opcjonalnie kontynuuj tworzenie wiązań.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwie krawędzie *(patrz wyżej)*.
    -   Wybierz dwa punkty końcowe należące do różnych krawędzi.
    -   Wybierz krawędź i punkt końcowy innej krawędzi *(w dowolnej kolejności)*.
    -   Wybierz punkt i dwie krawędzie *(analogicznie)*.
2.  Wywołaj narzędzie w sposób opisany powyżej lub z następującą dodatkową opcją:
    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz **Wiązanie → <img src="images/Sketcher_ConstrainPerpendicular.svg" width=16px> Wiązanie prostopadłości** z menu podręcznego.
3.  Dodawane jest wiązanie prostopadłe. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz [przykłady](#Between_two_edges_at_point/pl.md).



## Przykłady



### Między dwiema krawędziami 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:400px;">

Dwie krawędzie są prostopadłe w miejscu ich (wirtualnego) przecięcia. Jeśli jedna z krawędzi jest [stożkiem](Sketcher_Workbench/pl#Sketcher_CompCreateConic.md), dodawany jest [obiekt punktu](Sketcher_CreatePoint/pl.md), który ma [wiązanie punk na obiekcie](Sketcher_ConstrainPointOnObject/pl.md) z obiema *(przedłużonymi)* krawędziami.



### Między dwoma punktami końca 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:400px;">

Punkty końcowe są zbieżne, a krawędzie są prostopadłe w tym punkcie.



### Między krawędzią a punktem końcowym 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:400px;">

Punkt końcowy jednej krawędzi jest ograniczony tak, aby leżał na drugiej krawędzi, a krawędzie są prostopadłe w tym punkcie.



### Między dwiema krawędziami w punkcie 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:400px;">

Dwie krawędzie są prostopadłe w danym punkcie. Punktem może być dowolny punkt, np. środek okręgu, punkt końcowy krawędzi lub początek, może on należeć do jednej z krawędzi, a także może być [obiektem punktu](Sketcher_CreatePoint/pl.md). W razie potrzeby dodawane są wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md), aby zapewnić, że punkt leży na obu *(przedłużonych)* krawędziach. Te dodatkowe wiązania nazywane są [wiązaniami pomocniczymi](Sketcher_helper_constraint/pl.md).



## Tworzenie skryptów 

Ograniczenie prostopadłe może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli Pyton za pomocą następujących narzędzi: 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` Gdzie:

  - `Sketch` jest obiektem szkicu

  - `icurve1`, `icurve2` są dwiema liczbami całkowitymi określającymi krzywe, które mają być wykonane prostopadle. Liczby całkowite są indeksami w szkicu *(wartość zwracana przez Sketch.addGeometry)*.

  - `pointpos1`, `pointpos2` powinny mieć wartość `1` dla punktu początkowego i `2` dla końcowego.

  - `geoid point` i `pointpos` w PerpendicularViaPoint są indeksami określającymi punkt prostopadłościanu.

Strona [skrypty szkicownika](Sketcher_scripting.md) wyjaśnia wartości, które mogą być użyte do `icurve1`, `icurve2`, `pointpos1`, `pointpos2` i `geoidpoint`, i zawiera dalsze przykłady, jak tworzyć wiązania ze skryptów Python.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainPerpendicular/pl
