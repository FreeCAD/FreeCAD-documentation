---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/pl: Rysunek Techniczny: Wstaw grupę wycinków
   MenuLocation: Rysunek Techniczny , Widoki wycinków , Wstaw grupę wycinków
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_ClipGroupAdd/pl, TechDraw_ClipGroupRemove/pl
---

# TechDraw ClipGroup/pl



## Opis

Narzędzie **Wstaw grupę wycinków** tworzy okno wycinka, które może zawierać Widoki.

![](images/TechDraw_Clipview.png ) 
*Okno widoku rzutni obejmujące różne istniejące widoki*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ClipGroup.svg" width=16px> '''Wstaw grupę wycinków'''**, aby utworzyć nowy wycinek.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki wycinków → <img src="images/TechDraw_ClipGroup.svg" width=16px> Wstaw grupę wycinków**.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.



## Właściwości

-    **Szerokość**: Szerokość okna wycinka w jednostkach.

-    **Wysokość**: Wysokość okna wycinka w jednostkach.

-    **WyświetlRamkę**: Gdy wartość jest ustawiona na {{true/pl}}, pokazuje ramkę wokół okna wycinka.

-    **WyświetlEtykiety**: Gdy wartość jest ustawiona na {{true/pl}}, pokazuje etykiety widoków w oknie przycinania. **UWAGA:** usunięto w wersji 0.19.

-    **Widoki**: Widoki zawarte w oknie przycinania.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/pl
