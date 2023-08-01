---
- GuiCommand:/pl
   Name:PartDesign SubtractiveBox
   Name/pl:Projekt Części: Subtraktywny prostopadłościan
   MenuLocation:Projekt Części → Utwórz cechę przez odjęcie → Subtraktywny prostopadłościan
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do odjęcia](PartDesign_CompPrimitiveSubtractive/pl.md), [Addytywny prostopadłościan](PartDesign_AdditiveBox/pl.md)
---

# PartDesign SubtractiveBox/pl



## Opis

Funkcja ta wstawia pierwotny prostopadłościan odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveBox_example.png ) *Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i prostopadłościan do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveBox.svg" width=24px> '''Subtraktywny prostopadłościan'''**. **Uwaga**: Subtraktywny prostopadłościan jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Jeśli wyświetlany jest inny prymityw, kliknij strzałkę w dół obok ikony i wybierz Addytywny prostopadłościan z menu.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Prostopadłościan.



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
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveBox/pl
