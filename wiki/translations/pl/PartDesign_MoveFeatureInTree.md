---
- GuiCommand   */pl
   Name   *PartDesign MoveFeatureInTree
   Name/pl   *Projekt Części   * Przenieś cechę w drzewie
   MenuLocation   *Menu kontekstowe → Przesuń obiekt za inny obiekt
   Workbenches   *[Projekt Części](PartDesign_Workbench/pl.md)
   Version   *0.17
   SeeAlso   *[Ustaw czubek](PartDesign_MoveTip/pl.md), [Przesuń cechę do innej zawartości](PartDesign_MoveFeature/pl.md)
---

# PartDesign MoveFeatureInTree/pl

## Opis

<img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width   *24px;"> [Przesuń obiekt za inny obiekt](PartDesign_MoveFeatureInTree/pl.md), jak to polecenie jest nazwane w menu kontekstowym, pozwala na zmianę kolejności obiektów w Zawartości. Obsługiwane są szkice, geometria punktów odniesienia i cechy.

## Użycie

1.  W drzewie modelu zaznacz obiekt*(y)*, który ma zostać przesunięty, a następnie kliknij prawym przyciskiem myszy, aby otworzyć menu podręczne.
2.  Wybierz opcję **Przesuń obiekt za inny obiekt**.
3.  W oknie dialogowym **Wybierz element** wybierz obiekt, pod który chcesz przesunąć obiekt*(y)*.
4.  Naciśnij przycisk **OK**.

## Przykład

Poniższe trzy obrazki przedstawiają ten sam model z kieszenią zdefiniowaną na szkicu dołączonym do płaszczyzny odniesienia. Na każdym z rysunków zmieniono kolejność elementów. Powoduje to, że kieszeń nie wykonuje żadnego otworu lub wykonuje otwory w różnych wyciągnięciach, w zależności od kolejności cech w drzewie modelu.

![](images/PD_move_feature0.png ) ![](images/Hole_Pad002.png ) ![](images/PD_move_feature2.png )





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveFeatureInTree/pl
