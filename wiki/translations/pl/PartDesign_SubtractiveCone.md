---
- GuiCommand:/pl
   Name:PartDesign SubtractiveCone
   Name/pl:Projekt Części: Subtraktywny stożek
   MenuLocation:Projekt Części → Utwórz cechę przez odjęcie → Subtraktywny stożek
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do odjęcia](PartDesign_CompPrimitiveSubtractive/pl.md), [Addytywny stożek](PartDesign_AdditiveCone/pl.md)
---

# PartDesign SubtractiveCone/pl



## Opis

Funkcja ta wstawia pierwotny stożek odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveCone_example.png )

*Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i stożek do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveCone.svg" width=24px> '''Subtraktywny stożek'''**. **Uwaga**: Subtraktywny stożek jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Stożek, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywny stożek.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Stożek.



## Opcje

Stożek można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Stożka. Zmień zgodnie z własnymi potrzebami.

-    **Promień1**: wartość promienia u podstawy stożka.

-    **Promień2**: wartość promienia na wierzchołku stożka. Wartość większa od zera tworzy stożek ścięty.

-    **Wysokość**: wysokość stożka wzdłuż jego osi.

-    **Kąt**: kąt obrotu przekroju *(360° dla pełnego stożka)*.





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCone/pl
