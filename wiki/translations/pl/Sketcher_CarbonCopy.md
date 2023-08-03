---
 GuiCommand:
   Name: Sketcher CarbonCopy
   Name/pl: Szkicownik: Kalka techniczna
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Kalka techniczna
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **W**
   Version: 0.17
---

# Sketcher CarbonCopy/pl



## Opis

Narzędzie **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> '''Kalka techniczna'''** kopiuje całą geometrię i wiązania z innego szkicu do szkicu aktywnego.

Wiązania wymiarowe, które istnieją przed funkcją kopiowania, pozostają powiązane z wiązaniami wymiarowymi oryginalnego szkicu poprzez [wyrażenia](Expressions/pl.md).



## Użycie

1.  Upewnij się, że jesteś w trybie edycji istniejącego **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [szkicu](Sketcher_NewSketch.md)**. Ten szkic jest celem operacji.
2.  Naciśnij przycisk **[<img src=images/Sketcher_CarbonCopy.svg style="width:16px"> '''Kalka techniczna'''**.
3.  Kliknij na krawędź z innego szkicu. Ten szkic jest źródłem operacji.
4.  Elementy geometrii oraz ograniczenia są kopiowane do aktywnego szkicu.
5.  Naciśnij **Esc** lub prawy przycisk myszki, aby zakończyć działanie.



## Uwagi

-   Gdy szkice są używane w środowisku pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), zwykle szkic do kalki powinien znajdować się w tej samej **[<img src=images/PartDesign_Body.svg style="width:16px"> [Zawartości](PartDesign_Body/pl.md)** jak aktualnie aktywny szkic. Jeśli szkic, który ma zostać skopiowany, nie znajduje się w aktywnej [Zawartości](PartDesign_Body/pl.md), kursor myszki nie pozwoli na wybór. W takim przypadku przytrzymaj klawisz **Ctrl**, aby umożliwić wybór szkiców z innych Zawartości.
-   Zazwyczaj wybierany szkic powinien znajdować się w płaszczyźnie równoległej do aktualnie aktywnego szkicu. Jeśli szkic, który ma być skopiowany nie jest równoległy do aktualnie działającego szkicu, przytrzymaj klawisze **Ctrl**+**Alt**, aby umożliwić wybór szkiców nie równoległych. Obiekt zostanie wtedy dopasowany do płaszczyzny aktywnego szkicu. Uwaga: w chwili obecnej, aby obiekt był widoczny, należy zapisać i ponownie załadować dokument. Działa to również dla szkiców znajdujących się poza aktywną [Zawartością](PartDesign_Body/pl.md).
-   Ponieważ skopiowane przez kalkę techniczną wiązania wymiarowe używają wyrażeń, są one renderowane w innym kolorze. Kolor ten można dostosować za pomocą opcji **Edycja → Preferencje → Szkicownik → Kolory → Wiązanie zależne od wyrażenia** w [Edytorze ustawień](Preferences_Editor/pl.md).
-   Jeśli tryb Szkicownika został zmieniony na tryb konstrukcji za pomocą **[<img src=images/Sketcher_ToggleConstruction.svg style="width:24px"> [Przełącz tryb konstrukcji](Sketcher_ToggleConstruction/pl.md)** wszystkie kopiowane geometrie będą tworzone w trybie konstrukcyjnym.



## Ograniczenia

-   Kopiowany jest cały szkic, nie ma możliwości zaznaczenia tylko fragmentu. Po skopiowaniu można jednak usunąć niechciane elementy ze skopiowanego szkicu.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CarbonCopy/pl
