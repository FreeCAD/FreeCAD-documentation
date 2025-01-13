---
 GuiCommand:
   Name: Sketcher ConstrainAngle
   Name/pl: Szkicownik: Wiązanie kąta
   MenuLocation: Szkic , Wiązania szkicownika , Wiązanie kąta
   Workbenches: Sketcher Workbench/pl
   Shortcut: **K** **A**
   SeeAlso: Sketcher_ConstrainPerpendicular/pl
---

# Sketcher ConstrainAngle/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_ConstrainAngle.svg  style="width:24px;"> **Wiązanie kąta** ustala kąt pomiędzy dwiema krawędziami *(linie są wówczas traktowane jako nieskończone, a otwarte krzywe również są wirtualnie wydłużane)*, kąt linii z poziomą osią szkicu lub kątem rozwarcia łuku kołowego.



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).



### [Tryb kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md) 

1.  Upewnij się, że nie ma zaznaczenia.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   
        {{Version/pl|1.0}}
        
        : Jeśli [preferencja](Sketcher_Preferences/pl#Ogólne.md) **Wiązania wymiarów** jest ustawiona na {{Value|Narzędzie pojedyncze}} *(domyślnie)*: naciśnij strzałkę w dół po prawej stronie przycisku **<img src="images/Sketcher_Dimension.svg" width=|x16px><img src="images/Toolbar_flyout_arrow.svg" width=x16px>** i wybierz opcję **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> Wiązanie kąta** z rozwijanej listy.

    -   Jeśli ta preferencja ma inną wartość *(i w {{VersionMinus|0.21}})*: naciśnij **<img src="images/Sketcher_ConstrainAngle.svg" width=16px> '''Wiązanie kąta'''**.

    -   Wybierz z menu opcję **Szkic → Wiązania szkicownika → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Wiązanie kąta**.

    -   
        {{Version/pl|1.0}}
        
        : Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **Wiązania wymiarów → <img src="images/Sketcher_ConstrainAngle.svg" width=16px> Wiązanie kąta** z menu podręcznego.

    -   Użyj skrótu klawiaturowego: **K**, a następnie **A**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wykonaj jedną z następujących czynności:
    -   Wybierz dwie linie.
    -   Wybierz punkt i dwie krawędzie *(w tej kolejności)*.
    -   Wybierz krawędź, punkt i krawędź *(w tej samej kolejności)*.
5.  Jeśli utworzono [konstrukcyjne wiązanie wymiarów](Sketcher_ToggleDrivingConstraint/pl.md), w zależności od [ustawień](Sketcher_Preferences/pl#Wyświetlanie.md), otworzy się okno dialogowe [wstaw kąt](Sketcher_Workbench/pl#Edycja_wiązań.md). Wartość ujemna spowoduje odwrócenie kierunku kąta.
6.  Dodawane jest wiązanie kątowe. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz [przykłady](#Między_dwiema_krawędziami_w_punkcie.md).
7.  Opcjonalnie kontynuuj tworzenie wiązań.
8.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



### Tryb jednorazowy 

1.  Wykonaj jedną z następujących czynności:
    -   Wybierz pojedynczą linię.
    -   Wybierz pojedynczy łuk kołowy.
    -   Wybierz dwie linie.
    -   Wybierz punkt i dwie krawędzie (w dowolnej kolejności).
2.  Wywołaj narzędzie w sposób opisany powyżej.
3.  Opcjonalnie [edytuj wartość wiązania](Sketcher_Workbench/pl#Edycja_wiązań.md).
4.  Dodawane jest wiązanie kątowe. Jeśli wybrano punkt i dwie krawędzie, można również dodać maksymalnie dwa wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md). Zobacz akapit [przykłady](#Między_dwiema_krawędziami_w_punkcie.md).



## Przykłady



### Pojedyncza linia 

<img alt="" src=images/Sketcher_ConsraintAngle_mode1.png  style="width:400px;">

Kąt linii względem dodatniej osi X szkicu jest stały.



### Pojedynczy łuk kołowy 

<img alt="" src=images/Sketcher_ConsraintAngle_mode2.png  style="width:400px;">

Kąt rozwarcia łuku jest stały.



### Pomiędzy dwoma liniami 

<img alt="" src=images/Sketcher_ConsraintAngle_mode3.png  style="width:400px;">

Kąt między dwiema liniami jest stały. Nie jest wymagane, aby linie się przecinały.



### Między dwiema krawędziami w punkcie 

<img alt="" src=images/Sketcher_ConsraintAngle_mode4.png  style="width:400px;">

Kąt między dwiema krawędziami w danym punkcie jest stały. Punktem może być dowolny punkt, np. środek okręgu, punkt końcowy krawędzi lub początek, może on należeć do jednej z krawędzi, a także może być [obiektem punktu](Sketcher_CreatePoint/pl.md). W razie potrzeby dodawane są wiązania [punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md), aby zapewnić, że punkt leży na obu *(przedłużonych)* krawędziach. Te dodatkowe wiązania nazywane są [wiązaniami pomocniczymi](Sketcher_helper_constraint/pl.md).



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
