---
- GuiCommand:
   Name:PartDesign SubtractiveWedge
   Name/pl:Projekt Części: Subtraktywny klin
   MenuLocation:Projekt Części → Utwórz cechę przez odjęcie → Subtraktywny klin
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do odjęcia](PartDesign_CompPrimitiveSubtractive/pl.md), [Addytywny klin](PartDesign_AdditiveWedge/pl.md)
---

# PartDesign SubtractiveWedge/pl



## Opis

Funkcja ta wstawia pierwotny klin odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveWedge_example.svg ) *Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i klin do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveWedge.svg" width=24px> '''Subtraktywny klin'''**. **Uwaga**: Subtraktywny klin jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, na pasku narzędzi domyślnie wyświetlany jest Subtraktywny prostopadłościan. Aby przejść do funkcji Klin, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywny klin.
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
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/pl
