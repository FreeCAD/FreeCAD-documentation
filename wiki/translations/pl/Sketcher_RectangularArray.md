---
 GuiCommand:
   Name: Sketcher RectangularArray
   Name/pl: Szkicownik: Szyk prostokątny
   MenuLocation: Szkic , Narzędzia szkicownika , Szyk prostokątny
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **Z** **A**
   Version: 0.16
---

# Sketcher RectangularArray/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_RectangularArray.svg  style="width:32px;"> **Szyk prostokątny** tworzy tablicę wybranych elementów szkicu.



## Użycie

1.  Wybierz elementy szkicownika w oknie [panelu zadań](Task_panel/pl.md) lub w [widoku 3D](3D_view/pl.md).
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **[<img src=images/Sketcher_RectangularArray.svg style="width:16px"> [Szyk prostokątny](Sketcher_RectangularArray/pl.md)**.
    -   Wybierz opcję z menu **Szkic → Narzędzia szkicownika → [<img src=images/Sketcher_RectangularArray.svg style="width:16px"> Szyk prostokątny**.
3.  Określ opcje dla szyku w oknie dialogowym, które się otworzy.
4.  Naciśnij przycisk **OK**.
5.  Przesuń kursor myszki w oknie [widoku 3D](3D_view/pl.md) w kierunku żądanego punktu odniesienia.
    Przez przytrzymanie klawisza **Ctrl**, kąt do punktu odniesienia może być ustalony w krokach co 5°. {{Version/pl|0.20}}
6.  Kliknij lewym przyciskiem myszy w oknie widoku 3D, aby utworzyć szyk.
7.  Aby ustalić odległości pomiędzy elementami szyku, edytuj wiązania wymiarowe szyku.



## Opcje

![](images/Sketcher_RectangularArray_Options.jpg )

**Szyk prostokątny** ma następujące opcje:

-   **Kolumny**\': Liczba kolumn w szyku.
-   **Wiersze**: Liczba rzędów w szyku.
-   **Równe odstępy pionowe / poziome**: Jeśli odstęp pionowy między elementami szyku ma być taki sam jak odstęp poziomy.
-   **Zwiąż odległości między elementami**: Po zaznaczeniu tej opcji, odległość między elementami tablicy będzie związana. Jeśli na przykład wiesz tylko, że potrzebujesz tablicy 23 x 15 mm, użyj tej opcji, aby później móc zmienić te więzy na wymiary, których potrzebujesz.
-   **Klonuj**: Po wybraniu tej opcji, wiązania wymiarowe są zastępowane wiązaniami geometrycznymi w kopiach, tak że każda zmiana w oryginalnym elemencie jest również odzwierciedlona w kopiach.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher RectangularArray/pl
