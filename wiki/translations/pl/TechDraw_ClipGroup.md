---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/pl: Rysunek Techniczny: Wstaw grupę wycinków
   MenuLocation: Rysunek Techniczny , Rysunek Techniczny – Widoki , Wstaw grupę wycinków
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: 
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
    -   Wybierz opcję z menu **Rysunek Techniczny → Rysunek Techniczny – widoki → <img src="images/TechDraw_ClipGroup.svg" width=16px> Wstaw grupę wycinków**.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**:
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Widoki można przeciągać i upuszczać do i z grupy klipów w widoku drzewa. {{Version/pl|1.0}}



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Grupa wycinków, formalnie obiekt {{Incode|TechDraw::DrawViewClip}} ma [właściwości](TechDraw_View/pl#Właściwości_-_Widok_części.md) wspólne dla wszystkich typów Widoków. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Grupa wycinków}}

-    **Szerokość|Length**: Szerokość okna wycinka w jednostkach.

-    **Wysokość|Length**: Wysokość okna wycinka w jednostkach.

-    **WyświetlRamkę|Bool**: Gdy wartość jest ustawiona na {{true/pl}}, pokazuje ramkę wokół okna wycinka.

-    **Widoki|LinkList**: Widoki zawarte w oknie przycinania





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/pl
