---
 GuiCommand:
   Name: Sketcher RestoreInternalAlignmentGeometry
   Name/pl: Szkicownik: Pokaż / ukryj geometrię wewnętrzną
   MenuLocation: Szkic , Narzędzia szkicownika , Pokaż / ukryj geometrię wewnętrzną
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **I**
   SeeAlso: 
---

# Sketcher RestoreInternalAlignmentGeometry/pl



## Opis

Polecenie usuwa nieużywane elementy wyrównane do geometrii wewnętrznej lub odtwarza brakujące.



## Użycie

-   Wybierz element szkicu, który obsługuje wewnętrzne wyrównanie *([Elipsa](Sketcher_CreateEllipseByCenter/pl.md), [Łuk elipsy](Sketcher_CreateArcOfEllipse/pl.md) [Okrąg hiperboli](Sketcher_CreateArcOfHyperbola/pl.md), [Okrąg paraboli](Sketcher_CreateArcOfParabola/pl.md) lub [krzywa złożona](Sketcher_CreateBSpline/pl.md))*.
-   Wywołaj polecenie, klikając **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md)** lub wybierając **Szkic → Narzędzia szkicownika → [<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> Pokaż / ukryj geometrię wewnętrzną** lub za pomocą skrótu klawiaturowego.

Jeśli istnieją wolne miejsca wyrównania dla wybranego elementu, tworzona jest nowa geometria konstrukcji i wyrównywana do dostępnych miejsc. Jeśli wszystkie miejsca wyrównania są zajęte, nieużywana geometria wewnętrzna jest usuwana *(element jest traktowany jako nieużywany, jeśli nie jest ograniczony do niczego innego)*.



## Przykład

1.  Utwórz nową elipsę. Nowe elipsy są zawsze w pełni upakowane. Zobaczysz elipsę i garść geometrii konstrukcyjnej: główną średnicę, małą średnicę, punkty centralne.
2.  Wybierz linię o mniejszej średnicy i naciśnij klawisz **Del**. Średnica zniknęła, ale elipsa pozostała. Jak odzyskać średnicę?
3.  Wybierz elipsę i wywołaj polecenie **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md)**. Średnica zostaje przywrócona.
4.  Teraz zwiąż główną średnicę elipsy do pewnej długości. Zaznacz elipsę i wywołaj polecenie **[<img src=images/Sketcher_RestoreInternalAlignmentGeometry.svg style="width:16px"> [Pokaż / ukryj geometrię wewnętrzną](Sketcher_RestoreInternalAlignmentGeometry/pl.md)**.

**Wynik:** Średnica mniejsza i ogniska zostają usunięte, ale średnica większa zostaje zachowana, ponieważ uczestniczy w innych wiązaniach. Środek elipsy też pozostaje, bo jest nieodłączny, jak środek okręgu.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RestoreInternalAlignmentGeometry/pl
