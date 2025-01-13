---
 GuiCommand:
   Name: Part ColorPerFace
   Name/pl: Część: Kolor dla ściany
   MenuLocation: Widok , Kolor dla ściany
   Workbenches: Part_Workbench/pl, PartDesign_Workbench/pl
   SeeAlso: Std_SetAppearance/pl
---

# Part ColorPerFace/pl



## Opis

Polecenie **Kolor dla ściany** ustawia właściwości wyświetlania wybranych powierzchni. Aby dokonać zmiany całego obiektu, należy użyć [Wygląd zewnętrzny](Std_SetAppearance/pl.md).

Ta strona została zaktualizowana do wersji 1.0.

![](images/Part_ColorPerFace_Taskpanel.png ) 
*Panel zadaniowy Ustaw wygląd dla ściany.*



## Użycie

1.  Wybierz pojedynczy obiekt.
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Jeśli aktywne jest [środowisko pracy Część](Part_Workbench/pl.md): wciśnij przycisk **<img src="images/Part_ColorPerFace.svg" width=16px> [Kolor dla ściany](Part_ColorPerFace/pl.md)**.
    -   Wybierz opcję **Widok → <img src="images/Part_ColorPerFace.svg" width=16px> Kolor dla ściany** z menu.
    -   Wybierz opcję **<img src="images/Part_ColorPerFace.svg" width=16px> Ustaw wygląd dla ściany...** z menu kontekstowego [widoku drzewa](Tree_view/pl.md).
3.  Otworzy się panel zadań **Ustaw wygląd dla ściany**.
4.  Wybierz jedną lub więcej ścian:
    -   Przytrzymaj **Ctrl**, aby wybrać wiele ścian.
    -   Opcjonalnie naciśnij przycisk **Zaznacz obszarem**, kliknij w pustym obszarze i przeciągnij pole zaznaczenia, aby zaznaczyć wszystkie powierzchnie należące do obiektu, które znajdują się *(częściowo)* wewnątrz obszaru prostokąta. Możliwe jest zaznaczenie wielu pól.
5.  Wykonaj jedną z następujących czynności:
    -   Wybierz materiał z listy.
        1.  Opcjonalnie naciśnij przycisk **Uruchom edytor**, aby uruchomić [Edytor materiałów](Materials_Edit/pl.md).
    -   Określ **Wygląd niestandardowy**:
        1.  Naciśnij przycisk **...**.
        2.  Otworzy się okno dialogowe **Właściwości materiału**:
            ![](images/Material_Properties_Dialog.png )
        3.  Te właściwości można edytować:
            -   **Kolor otoczenia**: kolor cieni na obiekcie.
            -   **Kolor rozproszenia**: rzeczywisty/podstawowy kolor obiektu.
            -   **Kolor emisji**: kolor światła promieniującego z obiektu.
            -   **Kolor odbicia**: kolor podświetlenia (odbicia) na połyskliwej powierzchni obiektu.
            -   **Stopień połysku**
            -   **Przezroczystość**
        4.  Opcjonalnie naciśnij przycisk **Reset**, aby zmienić wygląd na taki, jaki został zdefiniowany przez materiał.
        5.  Opcjonalnie naciśnij przycisk **Domyślny**, aby zmienić wygląd tak, aby odpowiadał bieżącym [preferencjom](PartDesign_Preferences/pl#Shape_appearance.md).
        6.  Naciśnij przycisk **Zamknij** po zakończeniu.
    -   Naciśnij przycisk **Ustaw na domyślne**, aby zmienić wygląd na taki, jaki został zdefiniowany przez materiał.
6.  Opcjonalnie wybierz jedną lub więcej nowych powierzchni, których właściwości chcesz zmienić.
7.  Naciśnij przycisk **OK**, aby zamknąć panel zadań i zakończyć polecenie.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ColorPerFace/pl
