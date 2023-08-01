---
- GuiCommand:
   Name:PartDesign AdditiveBox
   Name/pl:Projekt Części: Addytywny prostopadłościan
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Addytywny prostopadłościan
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do dodania](PartDesign_CompPrimitiveAdditive/pl.md), [Subtraktywny prostopadłościan](PartDesign_SubtractiveBox/pl.md)
---

# PartDesign AdditiveBox/pl



## Opis

Funkcja ta wstawia pierwotny prostopadłościan do aktywnej Zawartości jako pierwszy element lub łączy go z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveBox_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveBox.svg" width=24px> '''Addytywny prostopadłościan'''**. **Uwaga**: Addytywny prostopadłościan jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Jeśli wyświetlany jest inny prymityw, kliknij strzałkę w dół obok ikony i wybierz Addytywny prostopadłościan z menu.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Prostopadłościanu.



## Opcje

Prostopadłościan można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Prostopadłościanu. Zmień zgodnie z własnymi potrzebami.

-    **Długość**: wymiar prostopadłościanu w kierunku X.

-    **Szerokość**: wymiar prostopadłościanu w kierunku Y.

-    **Wysokość**: wymiar prostopadłościanu w kierunku Z.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveBox/pl
