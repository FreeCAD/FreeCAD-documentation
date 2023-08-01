---
- GuiCommand:
   Name:Std TreeCollapseDocument
   Name/pl:Std: Przeciąganie w widoku drzewa
   MenuLocation:Widok - Akcje widoku drzewa - Rozpocznij przeciąganie
   Workbenches:wszystkie
   Version:0.19
   SeeAlso:[Jeden dokument](Std_TreeSingleDocument/pl.md), [Wiele dokumentów](Std_TreeMultiDocument/pl.md)
---

# Std TreeCollapseDocument/pl

## Opis

Polecenie **Zwiń / rozwiń dokumenty w widoku drzewa** przełącza tryb dokumentu w [Widoku drzewa](Tree_view/pl.md) na zwiń / rozwiń. W tym trybie aktywowanie dokumentu w oknie [widoku 3D](3D_view/pl.md) spowoduje automatyczne rozwinięcie tego dokumentu w widoku drzewa i zwinięcie wszystkich innych dokumentów. Pozostałe tryby to [Jeden dokument](Std_TreeSingleDocument/pl.md) i [Wiele dokumentów](Std_TreeMultiDocument/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Kliknij czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_TreeSyncView.svg" width=16px>** i wybierz z menu opcję **Zwiń / rozwiń**. Uwaga: ikonka przycisku zmieni się w zależności od wybranej opcji.
    -   Wybierz opcję z menu **Widok → Akcje widoku drzewa → <img src="images/Std_TreeCollapseDocument.svg" width=16px> Zwiń / rozwiń**.

## Ustawienia

Tryb Tryb dokumentu w widoku drzewa jest zapisywany: **Przybory → Edycja parametrów ... → BaseApp → Preferencje → TreeView → DocumentMode**. Jest to wartość całkowita. Możliwe wartości to `0` *(Jeden Dokument)*, `1` *(Wiele dokumentów)* lub `2` *(Zwiń / rozwiń)*. Domyślnie jest to wartość `2`.





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std TreeCollapseDocument/pl
