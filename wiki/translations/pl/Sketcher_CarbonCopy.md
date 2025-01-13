---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/pl: Szkicownik: Kalka techniczna
   MenuLocation: Szkic , Narzędzia szkicownika , Kalka techniczna
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CarbonCopy.svg  style="width:24px;"> **Kalka techniczna** kopiuje całą geometrię i wiązania z innego szkicu do aktywnego szkicu.

Wiązania wymiarowe, które istnieją przed funkcją kopiowania, pozostają powiązane z wiązaniami wymiarowymi oryginalnego szkicu poprzez [wyrażenia](Expressions/pl.md).



## Użycie

1.  Upewnij się, że jesteś w trybie edycji istniejącego [szkicu](Sketcher_NewSketch/pl.md). Ten szkic jest celem operacji.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CarbonCopy.svg" width=16px> '''Kalka techniczna'''**.
    -   Wybierz z menu opcję **Szkic → Narzędzia szkicownika → <img src="images/Sketcher_CarbonCopy.svg" width=16px> Kalka techniczna**.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **W**.
3.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
4.  Wybierz krawędź z innego szkicu. Szkic ten jest źródłem operacji. Zobacz [Uwagi](#Uwagi.md).
5.  Elementy geometrii oraz wiązania są kopiowane do aktywnego szkicu.
6.  To narzędzie zawsze działa w trybie kontynuacji: opcjonalnie można skopiować dodatkowe szkice.
7.  Aby zakończyć, kliknij prawym przyciskiem myszy lub naciśnij **Esc**, lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.



## Uwagi

-   W środowisku pracy [Projekt Części](PartDesign_Workbench/pl.md) możliwe jest wybranie szkicu do skopiowania spoza [zawartością](PartDesign_Body/pl.md) aktualnie aktywnego szkicu, ale tylko wtedy, gdy klawisz **Ctrl** jest przytrzymany podczas wyboru.
-   Szkic do skopiowania powinien być płaszczyzną równoległą do aktualnie aktywnego szkicu. Jeśli tak nie jest, klawisze **Ctrl** i **Alt** muszą być wciśnięte podczas zaznaczania. Działa to również w przypadku szkiców znajdujących się poza aktywną Zawartością.
-   Jeśli [tryb konstrukcyjny](Sketcher_ToggleConstruction/pl.md) jest aktywny, kopiowana geometria jest tworzona jako geometria konstrukcyjna.
-   Kopiowany jest cały szkic, nie jest możliwe wybranie tylko jego części. Po skopiowaniu można jednak usunąć niechciane elementy.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/pl
