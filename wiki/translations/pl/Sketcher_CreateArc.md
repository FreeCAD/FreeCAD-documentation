---
 GuiCommand:
   Name: Sketcher CreateArc
   Name/pl: Szkicownik: Utwórz łuk przez środek
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz łuk przez środek
   Workbenches: Sketcher Workbench/pl
   Shortcut: **G** **A**
   SeeAlso: Sketcher_CreateCircle/pl
---

# Sketcher CreateArc/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> **Utwórz łuk** tworzy łuk przez jego środek i punkty końcowe. {{Version/pl|1.0}}: Lub opcjonalnie przez punkty końcowe i punkt wzdłuż łuku.

<img alt="" src=images/Sketcher_ArcExample3.png  style="width:400px;"> 
*Łuk utworzony w trybie "przez środek" z automatycznie zastosowanymi wiązaniami zdefiniowanymi przez wprowadzenie wszystkich parametrów wyświetlanych na ekranie.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateArc.svg" width=16px> '''Punkt środkowy i punkty końcowe'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateArc.svg" width=16px> Utwórz łuk przez środek**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_CreateArc.svg" width=16px> Utwórz łuk przez środek** z menu podręcznego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **A**.
2.  Kursor zmieni się w krzyżyk z ikoną bieżącego trybu narzędzia.
3.  Sekcja **Parametry łuku** (<small>(v1.0)</small> ) jest dodawana na górze [Sketcher Dialog](Sketcher_Dialog.md).
4.  Opcjonalnie naciśnij klawisz **M** lub wybierz z rozwijanej listy w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateArc.svg  style="width:16px;"> **Wyśrodkowany**:
        1.  Wybierz środek łuku. Lub z Pos-OVP: wprowadź jego współrzędne X i / lub Y.
        2.  Wybierz punkt początkowy łuku, który definiuje również promień. Lub za pomocą Dim-OVP: wprowadź promień i / lub kąt początkowy łuku. Kąt jest odniesiony do osi X szkicu. Dla tego kąta nie jest tworzone żadne wiązanie.
        3.  Wybierz punkt końcowy łuku. Lub z Dim-OVP: wprowadź kąt przysłony łuku.
    -   <img alt="" src=images/Sketcher_Create3PointArc.svg  style="width:16px;"> **Trzy punkty na obwodzie**: {{Version/pl|1.0}}.
        1.  Wybierz punkt początkowy i końcowy łuku. Lub za pomocą Pos-OVP: wprowadź ich współrzędne X i / lub Y.
        2.  Wybierz kolejny punkt, aby zdefiniować promień. Lub za pomocą Pos-OVP: wprowadź jego współrzędne X i / lub Y. Dla tego punktu nie zostaną utworzone żadne wiązania.
5.  Łuk jest tworzony i dodawane są odpowiednie wiązania oparte na Pos-OVP i Dim-OVP.
6.  Jeśli narzędzie działa w [trybie kontynuacji](Sketcher_Workbench/pl#Tryby_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie łuków.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateArc/pl
