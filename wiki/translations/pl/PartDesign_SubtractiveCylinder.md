---
 GuiCommand:
   Name: PartDesign SubtractiveCylinder
   Name/pl: Projekt Części: Subtraktywny walec
   MenuLocation: Projekt Części , Utwórz cechę przez odjęcie , Subtraktywny walec
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/pl, PartDesign_AdditiveCylinder/pl
---

# PartDesign SubtractiveCylinder/pl



## Opis

Funkcja ta wstawia pierwotny walec odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i walec do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveCylinder.svg" width=24px> '''Subtraktywny walec'''**. **Uwaga**: Subtraktywny walec jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Walec, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Walec.



## Opcje

Możliwe jest tworzenie przekrzywionych walców poprzez określenie kątów w odniesieniu do wektora normalnego wybranego dołaczenia. {{Version/pl|0.20}}

Walec można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Walca. Zmień zgodnie z własnymi potrzebami.

-    **Promień**: wartość promienia cylindra.

-    **Kąt**: kąt obrotu przekroju *(360° tworzy pełny walec)*.

-    **Wysokość**: wysokość walca wzdłuż jego osi.

-    **Pierwszy kąt**: kąt w pierwszym kierunku. {{Version/pl|0.20}}

-    **Drugi kąt**: kąt w drugim kierunku. {{Version/pl|0.20}}





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/pl
