---
- GuiCommand:
   Name: PartDesign AdditiveWedge
   Name/pl: Projekt Części: Addytywny klin
   MenuLocation: Projekt Części -> Utwórz cechę przez dodanie -> Addytywny klin
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/pl, PartDesign_SubtractiveWedge/pl
---

# PartDesign AdditiveWedge/pl



## Opis

Funkcja ta wstawia pierwotny klin do aktywnej Zawartości jako pierwszy element lub łączy go z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveWedge.svg" width=24px> '''Addytywny klin'''**. **Uwaga**: Addytywny klin jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Klin, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Klin.



## Opcje

Klin można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

Korzystając z domyślnego rozmieszczenia, poniższe dane wejściowe są następujące:

-    **X min/max**: Rozpiętość osi X ściany bazowej.

-    **Y min/max**: Rozpiętość wysokości klina

-    **Z min/max**: rozpiętość osi Z ściany bazowej

-    **X2 min/max**: Rozpiętość osi X ściany górnej

-    **Z2 min/max**: Rozpiętość osi Z górnej ściany



## Piramidy

Kliny mogą być używane do tworzenia piramid poprzez ustawienie **X2 min/max** i **Z2 min/max** tak, aby wartość min = max.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/pl
