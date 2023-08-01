---
- GuiCommand:
   Name: Part FaceColors
   Name/pl: Część: Kolor dla ściany
   MenuLocation: Menu podręczne - Ustaw kolory ...
   Workbenches: [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso: [Wygląd zewnętrzny](Std_SetAppearance/pl.md)
---

# Part FaceColors/pl



## Opis

Funkcja **Kolor dla ściany** umożliwia zdefiniowanie koloru dla każdej powierzchni obiektu. W ten sposób możesz przypisać wiele kolorów do jednej części. Aby pokolorować całe części, użyj zamiast tego właściwości *[Wygląd zewnętrzny](Std_SetAppearance/pl.md)*.



## Użycie

Aby kolorować powierzchnie:

1.  Kliknij prawym przyciskiem myszy na pozycję w [widoku drzewa](Tree_view/pl.md). Jeśli dany element obsługuje funkcję **FaceColors**, w menu kontekstowym znajduje się pozycja **Ustaw kolory\...** i można na nią kliknąć.
2.  Aby wybrać powierzchnię:
    -   Dla pojedynczej ściany po prostu kliknij na nią.
    -   Aby wybrać wiele ścian:
        -   Trzymaj wciśnięty klawisz **Ctrl** i klikaj w kilka powierzchni.
        -   Lub kliknij w oknie panelu zadań na przycisk **Zaznacz obszar**. Następnie można przeciągnąć myszą prostokąt zaznaczenia w oknie [widoku 3D](3D_view/pl.md). Zostanie zaznaczona każda powierzchnia, która częściowo znajduje się w obrębie zaznaczenia.
3.  Wybierz w oknie panelu zadań kolor dla zaznaczonych powierzchni. {{Version/pl|0.20}} Kolorowi można również nadać przezroczystość, definiując kanał alfa.
4.  Kliknij przycisk **OK**, aby zamknąć okno panelu zadań i zaakceptować wprowadzone zmiany.

Aby zresetować wszystkie kolory powierzchni:

1.  Kliknij w opcję **Ustaw na domyślne**. Spowoduje to ustawienie kolorów wszystkich powierzchni części na kolor domyślny. Przycisk działa od razu, tzn. nie można powstrzymać efektu za pomocą przycisku **Anuluj**.

![](images/Part_FaceColors-dialog.png ) 
*Panel zadań Kolor powierzchni*



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Command_Reference](Category_Command_Reference.md) > [Part](Part_Workbench.md) > Part FaceColors/pl
