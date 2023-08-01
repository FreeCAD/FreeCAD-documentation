---
- GuiCommand:
   Name: PartDesign AdditiveCone
   Name/pl: Projekt Części: Addytywny stożek
   MenuLocation: Projekt Części - Utwórz cechę przez dodanie - Addytywny stożek
   Workbenches: [Projekt Części](PartDesign_Workbench/pl.md)
   Version: 0.17
   SeeAlso: [Komponent bryła pierwotna do dodania](PartDesign_CompPrimitiveAdditive/pl.md), [Subtraktywny stożek](PartDesign_SubtractiveCone/pl.md)
---

# PartDesign AdditiveCone/pl



## Opis

Funkcja ta wstawia pierwotny stożek do aktywnej Zawartości jako pierwszy element lub łączy go z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveCone.svg" width=24px> '''Addytywny stożek'''**. **Uwaga**: Addytywny stożek jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Walec, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny stożek.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Prostopadłościanu.



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
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/pl
