---
 GuiCommand:
   Name: Sketcher External
   Name/pl: Szkicownik: Utwórz geometrię zewnętrzną
   MenuLocation: Szkic , Narzędzia szkicownika , Utwórz geometrię zewnętrzną
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **X**
   SeeAlso: Sketcher_ToggleConstruction/pl
---

# Sketcher External/pl



## Opis


{{VersionMinus/pl|1.0}}

: Narzędzie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> **Utwórz geometrię zewnętrzną** rzutuje krawędzie i / lub wierzchołki należące do obiektów znajdujących się poza szkicem na płaszczyznę szkicu. Rzutowana geometria nazywana jest „geometrią zewnętrzną". Pozostaje parametrycznie powiązana ze swoimi obiektami źródłowymi. Krawędzie geometrii zewnętrznej są oznaczone dedykowanym [kolorem](Sketcher_Preferences/pl#Wygląd_zewnętrzny.md) *(domyślnie magenta)* i rodzajem linii *({{Version/pl|1.0}})*. Podobnie jak w przypadku geometrii konstrukcyjnej, geometria zewnętrzna nie jest widoczna poza szkicem, ma pomóc w zdefiniowaniu wiązań i innej geometrii wewnątrz samego szkicu.


{{VersionPlus/pl|1.1}}

: Zobacz stronę <img alt="" src=images/Sketcher_Projection.svg  style="width:24px;"> [Rzutowanie](Sketcher_Projection/pl.md)

![](images/Sketcher_ExternalEsempio1.png ) 
*Dwie linie w kolorze magenta to zewnętrzna geometria połączona z krawędziami wcześniej istniejącego [wyciągnięcia](PartDesign_Pad/pl.md). Są one używane do związania okręgów.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów na wywołanie narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_External.svg" width=16px> '''Utwórz geometrię zewnętrzną'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_External.svg" width=16px> Utwórz geometrię zewnętrzną**.
    -   Kliknij prawym przyciskiem myszy w [widoku 3D](3D_view/pl.md) i z menu kontekstowego wybierz opcję **<img src="images/Sketcher_External.svg" width=16px> Utwórz geometrię zewnętrzną**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **X**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Wybierz krawędź zewnętrzną lub wierzchołek. Zobacz [Uwagi](#Uwagi.md).
4.  Zostanie utworzona geometria zewnętrzna.
5.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie można kontynuować wybieranie zewnętrznych krawędzi i / lub wierzchołków.
6.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   Można wybrać tylko krawędzie i wierzchołki z obiektów w tym samym układzie współrzędnych. Szkic i obiekt muszą znajdować się w tej samej [Zawartości](PartDesign_Body/pl.md) lub tej samej [Części](Std_Part/pl.md), lub w obu w globalnym układzie współrzędnych. Użyj [łącznika](PartDesign_SubShapeBinder/pl.md), aby przenieść kopię obiektu do bieżącego układu współrzędnych, jeśli jest to wymagane.
-   Zależności kołowe nie są dozwolone. Nie można utworzyć łącza do obiektu, który zależy od samego szkicu.
-   Łącza do elementów z innych szkiców są możliwe i zalecane, ponieważ są bardziej niezawodne niż łącza do wygenerowanej (bryłowej) geometrii. Te ostatnie mogą cierpieć z powodu [problemu nazewnictwa topologicznego](Topological_naming_problem/pl.md). Zobacz [Porady dotyczące tworzenia stabilnych modeli](Feature_editing/pl#Porady_dotyczące_tworzenia_stabilnych_modeli.md).



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/pl
