---
- GuiCommand   */pl
   Name   *Std TreeSingleDocument
   Name/pl   *Std   * Jeden dokument w widoku drzewa
   MenuLocation   *Widok → Akcje widoku drzewa → Jeden dokument
   Workbenches   *wszystkie
   Version   *0.19
   SeeAlso   *[Wiele dokumentów](Std_TreeMultiDocument/pl.md), [Zwiń dokument](Std_TreeCollapseDocument/pl.md)
---

# Std TreeSingleDocument/pl

## Opis

Polecenie **Jeden dokument w widoku drzewa** przełącza tryb dokumentu w [Widok drzewa](Tree_view/pl.md) na tryb pojedynczego dokumentu. W tym trybie w widoku Drzewa widoczny jest tylko aktywny dokument. Pozostałe tryby to [Wiele dokumentów](Std_TreeMultiDocument/pl.md) i [Zwiń / Rozwiń](Std_TreeCollapseDocument/pl.md).

W trybie pojedynczego dokumentu możesz przełączyć się na inny dokument, aktywując widok 3D należący do tego dokumentu. Możesz to zrobić w [Głównym obszarze widoku](Main_view_area/pl.md) lub poprzez menu **Okna**.

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia   *
    -   Kliknij czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_TreeSyncView.svg" width=16px>** i wybierz z menu opcję **Jeden dokument**. Uwaga   * ikonka przycisku zmieni się w zależności od wybranej opcji.
    -   Wybierz opcję z menu **Widok → Akcje widoku drzewa → <img src="images/Std_TreeSingleDocument.svg" width=16px> Jeden dokument**.

## Ustawienia

Tryb Tryb dokumentu w widoku drzewa jest zapisywany   * **Przybory → Edycja parametrów ... → BaseApp → Preferencje → TreeView → DocumentMode**. Jest to wartość całkowita. Możliwe wartości to `0` *(Jeden Dokument)*, `1` *(Wiele dokumentów)* lub `2` *(Zwiń / rozwiń)*. Domyślnie jest to wartość `2`.





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TreeSingleDocument/pl
