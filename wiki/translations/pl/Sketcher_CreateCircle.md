---
 GuiCommand:
   Name: Sketcher CreateCircle
   Name/pl: Szkicownik: Utwórz okrąg
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz okrąg
   Workbenches: Sketcher Workbench/pl
   Shortcut: **G** **C**
   SeeAlso: Sketcher_CreateArc/pl
---

# Sketcher CreateCircle/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:24px;"> **Utwórz okrąg** tworzy okrąg przez jego środek i punkt wzdłuż okręgu. {{Version/pl|1.0}}: Lub opcjonalnie przez trzy punkty wzdłuż okręgu.

![](images/Sketcher_CircleExample1.png‎ )



## Jak używać 

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

Pos-OVP = Pozycyjne [Parametry w widoku](Sketcher_Preferences#Ogólne/pl.md). {{Version/pl|1.0}}
Dim-OVP = Wymiarowe parametry w widoku. {{Version/pl|1.0}}

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreateCircle.svg" width=16px> '''Utwórz okrąg'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreateCircle.svg" width=16px> Utwórz okrąg** z menu.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_CreateCircle.svg" width=16px> Utwórz okrąg** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **C**.
2.  Kursor zmieni się w krzyżyk z ikoną bieżącego trybu narzędzia.
3.  Sekcja **Parametry okręgu** ({{Version/pl|1.0}}) jest dodawana na górze [okna dialogowego](Sketcher_Dialog/pl.md).
4.  Opcjonalnie naciśnij klawisz **M** lub wybierz z rozwijanej listy w sekcji parametrów, aby zmienić tryb narzędzia:
    -   <img alt="" src=images/Sketcher_CreateCircle.svg  style="width:16px;"> **Środek**:
        1.  Wybierz środek okręgu. Lub z Pos-OVP: wprowadź jego współrzędne X i/lub Y.
        2.  Wybierz punkt, aby zdefiniować promień okręgu. Lub za pomocą Dim-OVP: wprowadź ten promień.
    -   <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:16px;"> **trzy punkty na obwodzie**: {{Version/pl|1.0}}.
        1.  Wybierz trzy punkty, aby zdefiniować okrąg. Lub za pomocą Pos-OVP: wprowadź ich współrzędne X i / lub Y. Dla tych punktów nie są tworzone żadne wiązania.
5.  Okrąg jest tworzony i dodawane są odpowiednie wiązania oparte na Pos-OVP i Dim-OVP.
6.  Jeśli narzędzie działa w [Trybie kontynuacji](Sketcher_Workbench/pl#Tryb_kontynuacji.md):
    1.  Opcjonalnie kontynuuj tworzenie okręgów.
    2.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateCircle/pl
