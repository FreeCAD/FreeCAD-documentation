---
 GuiCommand:
   Name: CAM Helix
   Name/pl: CAM: Helisa
   MenuLocation: CAM , Helisa
   Workbenches: CAM_Workbench/pl
---

# CAM Helix/pl



## Opis

Narzędzie <img alt="" src=images/CAM_Helix.svg  style="width:24px;"> [CAM: Helisa](CAM_Helix/pl.md) dodaje operację spiralnego czyszczenia do zadania. Spiralny ruch zgodnie z ruchem wskazówek zegara generuje komendy G-code (G2), natomiast przeciwny ruch generuje komendy (G3). Procent naddatku określa koncentryczne nadkładanie jako procent średnicy narzędzia. Zostaną utworzone jedne lub więcej ścieżek spiralnych o różnych średnicach, aby oczyścić otwór.



## Użycie

-   Wybierz **[<img src=images/Workbench_CAM.svg style="width:16px"> [środowisko pracy CAM](CAM_Workbench/pl.md)**.
-   Wybierz ikonę **<img src="images/CAM_Helix.svg" width=24px>** lub **CAM** → **<img src="images/CAM_Helix.svg" width=24px> Helisa** z górnego menu. Otworzy się panel konfiguracji **<img src="images/CAM_Helix.svg" width=24px>** Helisy.
-   Wykoczy okno \"Wybierz kontroler narzędzia\", aby wybrać kontroler narzędzia. W starszych wersjach, w zakładce **<img src="images/CAM_Helix.svg" width=24px>** Operacja, wybierz kontroler narzędzia i potwierdź, klikając **Zastosuj**.
-   Otwórz zakładkę Geometria podstawowa. Wszystkie dostępne otwory zgodne z narzędziem Helisa w modelu zadania będą możliwe do wybrania do obróbki. W [widoku 3D](3D_view/pl.md) wybierz otwory po ich krawędzi lub ścianie i dodaj je przyciskiem **Dodaj**. Upewnij się, że pojawiają się na liście. Sprawdź, czy lista zgadza się z otworami przeznaczonymi do obróbki.
-   Aby usunąć otwory, wybierz je na liście i naciśnij przycisk **Usuń**.
-   Upewnij się, że parametry Głębokość początkowa, Głębokość końcowa oraz Krok w dół (skok helisy) są poprawne i dostosuj je, jeśli to konieczne.
-   Upewnij się, że parametry Wysokość bezpieczna i Odstęp bezpieczeństwa są poprawne i dostosuj je w razie potrzeby.
-   W zakładce Operacja określ powierzchnię początkową helisy (zewnętrzna/wewnętrzna), kierunek oraz procent nadkładania.
-   Kliknij **Zastosuj**, aby utworzyć lub zaktualizować ścieżkę, **OK**, aby zastosować i zamknąć panel, lub **Anuluj**, aby przerwać i zamknąć panel.



## Opcje

Dodatkowe Odsunięcie dodaje margines materiału do pozostawienia bez obróbki. Zwykle ma to na celu umożliwienie lekkiego przejścia wykańczającego jako odrębnej operacji.



## Komentarze

-   Krok w dół nie jest przestrzegany dokładnie. Zawsze podlega zaokrągleniu aby uzyskać pełną liczbę obrotów od Głębokości początkowej do końcowej.
-   Podobnie Naddatek nie jest przestrzegany dokładnie. Zawsze podlega zaokrągleniu aby uzyskać liczbę równych kroków.

Parametr prędkości posuwu jest stały dla wszystkich cięć i opiera się na położeniu osi narzędzia, co oznacza, że rzeczywista prędkość skrawania krawędzi narzędzia może się znacznie różnić pomiędzy wewnętrznym cięciem a powierzchnią zewnętrzną. Jeśli wymiary zadania generują średnicę ścieżki mniejszą niż średnica narzędzia, może to prowadzić do znacznie większych prędkości skrawania niż prędkość posuwu podana dla narzędzia w kontrolerze narzędzi. Może to wymagać uwzględnienia podczas dobierania „prędkości i posuwów" dla danego zadania.



## Właściwości



### Dane

Pusto



### Widok

Pusto



## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Przykład:


```python
#Place code example here.
```





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Helix/pl
