---
 GuiCommand:
   Name: TechDraw PageDefault
   Name/pl: Rysunek Techniczny: Wstaw nową domyślną stronę rysunku
   MenuLocation: Rysunek Techniczny , Strona , Wstaw nową domyślną stronę rysunku
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_PageTemplate/pl, TechDraw_Templates/pl
---

# TechDraw PageDefault/pl



## Opis

Narzędzie **Wstaw nową domyślna stronę rysunku** tworzy nowy obiekt Strony używając pliku szablonu określonego w [Ustawieniach](TechDraw_Preferences/pl.md) dla środowiska pracy Rysunek Techniczny.

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Domyślny szablon dołączony do środowiska pracy Rysunek Techniczny: Strona A4 w orientacji poziomej, A4_LandscapeTD.svg*



## Użycie

1.  Wymagany jest aktywny dokument.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_PageDefault.svg" width=16px> [Wstaw nową domyślna stronę rysunku](TechDraw_PageDefault/pl.md)**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Strona → <img src="images/TechDraw_PageDefault.svg" width=16px> Wstaw nową domyślna stronę rysunku**.



## Uwagi

-   Jeśli strona jest oznaczona jako \"nie aktualizuj na bieżąco\" za pomocą właściwości **Aktualizuj na bieżąco**, opcji **Włącz / wyłącz automatyczną aktualizację** z menu kontekstowego okna lub ustawienia w Preferencjach, będzie ona ignorować zmiany w modelu 3D. Możesz zauważyć anomalie (brakująca geometria, brakujące wartości wymiarów itp.) w wyglądzie strony. Zostaną one skorygowane, gdy strona zostanie zaktualizowana za pomocą narzędzia [Przerysuj stronę](TechDraw_RedrawPage/pl.md). Strona będzie miała tę ikonę <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> w [Widoku drzewa](Tree_view/pl.md) podczas wstrzymania aktualizacji. To ustawienie wpływa również na proces uruchamiania. Jeśli strona jest oznaczona jako \"nie aktualizuj\", nie zostanie ona rysowana podczas uruchamiania programu.

-   Jeśli domyślny szablon nie został określony w pliku konfiguracyjnym użytkownika `user.cfg`, narzędzie spróbuje:

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    

\" Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład:

:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Typ projekcji**: Domyślny typ projekcji *(kąt pierwszy lub trzeci)* dla tej strony.


{{TitleProperty|Strona}}

-    **Utrzymuj aktualizację**: Jeśli opcja przyjmuje wartość {{false/pl}}, Strona nie jest aktualizowana o zmiany w modelu 3D. Przydatne dla skomplikowanych/wolnych rysunków. Zobacz uwagi.

-    **Szablon**: Link do obiektu [szablonu](TechDraw_Templates/pl.md) tej Strony.

-    **Widoki**: Lista linków do Widoków na tej Stronie.

-    **Skala**: Domyślna skala dla Widoków na tej Stronie.

-    **Następny numer dymka**: Autonumeracja dla dymków.



### Widok


{{TitleProperty|Siatka}}

-    **Pokaż siatkę**: Pokaż siatkę na Stronie.

-    **Rozstaw siatki**: Odległość między liniami siatki.



## Tworzenie skryptów 

Zobacz informacje na stronie [Wstaw nową stronę przy użyciu szablonu](TechDraw_PageTemplate/pl#Tworzenie_skryptów.md)





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/pl
