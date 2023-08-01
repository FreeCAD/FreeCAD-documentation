---
- GuiCommand:
   Name: Std SetAppearance
   Name: Std: Wygląd zewnętrzny
   MenuLocation: Widok - Wygląd zewnętrzny ...
   Workbenches: wszystkie
   Shortcut: **Ctrl**+**D**
   SeeAlso: [Kolor powierzchni](Part_FaceColors/pl.md)
---

# Std SetAppearance/pl

## Opis

Polecenie **Wygląd zewnętrzny** pokazuje [Panel zadań](Task_panel/pl.md) właściwości wyświetlania dla wybranych obiektów.

<img alt="" src=images/DlgDisplayProperties.png  style="width:250px;"> 
*Panel zadań Właściwości wyświetlania*

## Użycie

1.  Wybierz jeden lub więcej obiektów.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Wybierz opcję z menu **Widok → <img src="images/Std_SetAppearance.svg" width=16px> Wygląd zewnętrzny ...**.
    -   Wybierz opcję **<img src="images/Std_SetAppearance.svg" width=16px> Wygląd zewnętrzny ...** z menu kontekstowego okna [Widoku Drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
    -   Użyj skrótu klawiaturowego: **Ctrl**+**D**.
3.  Zmień jedną lub więcej właściwości wyświetlania. Zobacz dostępne [Opcje](#Opcje.md). Obiekty zostaną natychmiast zaktualizowane.
4.  Opcjonalnie wybierz jeden lub więcej nowych obiektów, których właściwości wyświetlania chcesz zmienić.
5.  Naciśnij przycisk **Zamknij**, aby zamknąć panel zadań i zakończyć polecenie.

## Opcje

### Ustawienia trybu wyświetlania 

-   Wybierz **Tryb wyświetlania** z rozwijanej listy. Dostępne opcje to: *Cieniowany z krawędziami*, *Cieniowany* *(nie dotyczy obiektów środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md))*, *Szkielet* i *Tylko punkty*. Więcej informacji znajdziesz w opisie polecenia [Styl kreślenia](Std_DrawStyle/pl.md).

### Materiał

-   Wybierz predefiniowany materiał z listy rozwijanej *(\"Domyślny\", \"Aluminium\", \"Mosiądz\", \"Brąz\", itd.)*.
-   Naciśnij przycisk **...**, aby otworzyć okno dialogowe właściwości materiału i edytować kolory otoczenia, rozproszenia, emisyjności i odbicia, a także połysk.
-   **Kolor na wydruku:** nieobsługiwane w tym momencie.
-   **Kolor kształtu:** ustawia właściwość **Kolor kształtu**. Naciśnij przycisk, aby otworzyć okno dialogowe Wybierz kolor.
-   **Kolor linii:** ustawia właściwość **Kolor linii**. Naciśnij przycisk, aby otworzyć okno dialogowe Wybierz kolor.
-   **Kolor punktu:** ustawia właściwość **Kolor punktu**. Naciśnij przycisk, aby otworzyć okno dialogowe Wybór koloru.

### Wyświetlanie

-   **Wielkość punktu:** ustawia właściwość **Rozmiar punktu** *(w pikselach)*.
-   **Szerokość linii:** ustawia właściwość **Szerokość linii** *(w pikselach)*.
-   **Przezroczystość:** ustawia właściwość **Przezroczystość** *(w procentach)*. 0% to brak przezroczystości, 100% to pełna przezroczystość.
-   **Przezroczystość linii:** obecnie nie jest obsługiwana.

## Uwagi

-   Wymienione właściwości widoku można również zmienić w oknie [Edytora właściwości](Property_editor/pl.md) lub [Widoku połączonego](Combo_view/pl.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SetAppearance/pl
