---
- GuiCommand:
   Name: PartDesign MoveTip
   Name/pl: Projekt Części: Ustaw czubek
   MenuLocation: Menu kontekstowe - Ustaw czubek
   Workbenches: [Projekt Części](PartDesign_Workbench/pl.md)
   Version: 0.17
   SeeAlso: [Przenieś cechę](PartDesign_MoveFeature/pl.md), [Przenieś cechę w drzewie](PartDesign_MoveFeatureInTree/pl.md)
---

# PartDesign MoveTip/pl



## Opis

<img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;"> [Ustaw czubek](PartDesign_MoveTip/pl.md), jak jest opisane to polecenie w menu kontekstowym, redefiniuje czubek, który jest cechą widoczną na zewnątrz Zawartości. Domyślnie czubek jest ostatnią cechą dodaną do Zawartości, ale czasami może być przydatne chwilowe ustawienie czubka na wcześniejszą cechę w drzewie. To może zostać wykonane w celu dodania szkicu, geometrii bazowej czy cechy, które w retrospektywie powinny być stworzone wcześniej w historii Zawartości.

Czubek jest wizualnie wyróżniony w drzewie modelu przez małą strzałkę w dół w zielonym okręgu nałożonym na ikonę cechy, Dla przykładu, poniższa cecha jest czubkiem:

![](images/PartDesign_Body_tree-04.png )



## Użycie

1.  W drzewie modelu, kliknij prawym przyciskiem na cechę by ustawić ją jako czubek.
2.  Z listy w menu kontekstowym wybierz <img alt="" src=images/PartDesign_MoveTip.svg  style="width:24px;">**Ustaw czubek**.
3.  Nowy czubek jest ustawiony jako widzialny i wszystkie elementy poniżej czubka zostają ukryte w widoku. Elementy stworzone od tego momentu będą umieszczone poniżej czubka, a powyżej innych istniejących elementów.

**Uwaga**: Ważnie jest by nie zapomnieć ustawić czubka ponownie na ostatniej cesze, na dole drzewa Zawartości.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign MoveTip/pl
