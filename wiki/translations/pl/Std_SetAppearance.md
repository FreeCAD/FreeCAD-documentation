---
 GuiCommand:
   Name: Std SetAppearance
   Name: Std: Wygląd zewnętrzny
   MenuLocation: Widok , Wygląd zewnętrzny ...
   Workbenches: Material_Workbench/pl, Part_Workbench/pl, PartDesign_Workbench/pl i inne
   Shortcut: **Ctrl** + **D**
   SeeAlso: Std_SetMaterial/pl,Part_ColorPerFace/pl
---

# Std SetAppearance/pl



## Opis

Polecenie **Wygląd zewnętrzny** ustawia właściwości wyświetlania wybranych obiektów.

Ta strona została zaktualizowana do wersji 1.0.

![](images/Std_SetAppearance_Taskpanel.png ) 
*Panel zadań Właściwości wyświetlania*



## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz opcję **Widok → <img src="images/Std_SetAppearance.svg" width=16px> Wygląd zewnętrzny ...** z menu.
    -   Wybierz opcję **<img src="images/Std_SetAppearance.svg" width=16px> Wygląd zewnętrzny ...** z menu kontekstowego [widoku drzewa](Tree_view/pl.md) lub [widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiszowego: **Ctrl**+**D**.
3.  Otwarty zostanie panel zadań **Wyświetl właściwości**. Zobacz [Opcje](#Opcje.md).
4.  Zmień jedną lub więcej właściwości.
5.  Obiekty zostaną natychmiast zaktualizowane.
6.  Opcjonalnie wybierz jeden lub więcej dodatkowych obiektów, których właściwości chcesz zmienić.
7.  Wciśnij przycisk **Zamknij** aby zamknąć panel zadań i zakończyć polecenie.



## Opcje



### Ustawienia trybu wyświetlania 

-   Wybierz **Tryb wyświetlania** z rozwijanej listy. Dostępne opcje to: {{Value|Cieniowany z krawędziami}}, {{Value|Cieniowany}} *(nie dotyczy obiektów środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md))*, {{Value|Szkielet}} i {{Value|Tylko punkty}}. Więcej informacji znajdziesz w opisie polecenia [Styl kreślenia](Std_DrawStyle/pl.md).



### Materiał

-   Wybierz materiał z listy.
    1.  Opcjonalnie wybierz kategorię z listy rozwijanej pod listą materiałów aby przefiltrować materiały. Dostępne kategorie to {{Value|Podstawowy wygląd}}, {{Value|Wygląd tekstury}} (takie materiały nie są jeszcze dostępne) i {{Value|Wszystkie materiały}}.
    2.  Opcjonalnie wciśnij przycisk **Uruchom edytor** aby uruchomić [Edytor materiałów](Materials_Edit/pl.md).
-   **Własny wygląd:** wciśnij przycisk **...** aby nadpisać wygląd materiału. Zostanie otwarte okno dialogowe **Właściwości materiału**. Zobacz [Kolor dla ściany](Part_ColorPerFace/pl#Użycie.md).
-   **Kolor na wydruku:** nieobsługiwane w tym momencie.
-   **Kolor linii:** ustawia właściwość **Kolor linii**. Naciśnij przycisk, aby otworzyć okno dialogowe Wybierz kolor.
-   **Kolor punktu:** ustawia właściwość **Kolor punktu**. Naciśnij przycisk, aby otworzyć okno dialogowe Wybierz kolor.



### Wyświetlanie

-   **Wielkość punktu:** ustawia właściwość **Rozmiar punktu** *(w pikselach)*.
-   **Szerokość linii:** ustawia właściwość **Szerokość linii** *(w pikselach)*.
-   **Przezroczystość:** ustawia właściwość **Przezroczystość** *(w procentach)*. 0% to brak przezroczystości, 100% to pełna przezroczystość.
-   **Przezroczystość linii:** obecnie nie jest obsługiwana.



## Uwagi

-   Wymienione właściwości widoku można również zmienić w oknie [Edytora właściwości](Property_editor/pl.md).



---
⏵ [documentation index](../README.md) > Std SetAppearance/pl
