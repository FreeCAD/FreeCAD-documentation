---
 GuiCommand:
   Name: PartDesign SubtractivePrism
   Name/pl: Projekt Części: Subtraktywny graniastosłup
   MenuLocation: Projekt Części , Utwórz cechę przez odjęcie , Subtraktywny graniastosłup
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveSubtractive/pl, v/pl
---

# PartDesign SubtractivePrism/pl



## Opis

Funkcja ta wstawia pierwotny graniastosłup odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractivePrism_example.svg )

*Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i graniastosłup do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractivePrism.svg" width=24px> '''Subtraktywny graniastosłup'''**. **Uwaga**: Subtraktywny graniastosłup jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Graniastosłup, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywny graniastosłup.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Graniastosłup.



## Opcje

Możliwe jest tworzenie przekrzywionych graniastosłupów poprzez określenie kątów w odniesieniu do wektora normalnego wybranego dołaczenia.

Graniastosłup można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Granistosłup. Zmień zgodnie z własnymi potrzebami.

-    **Wielokąt**: liczba boków w wielokącie przekroju pryzmatu.

-    **Obwód**: [promień obwodu](https://en.wikipedia.org/wiki/Circumscribed_circle) wielokąta przekroju poprzecznego graniastosłupa.

-    **Wysokość**: wysokość pryzmatu.

-    **Pierwszy kąt**: kąt w pierwszym kierunku.

-    **Drugi kąt**: kąt w drugim kierunku.



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/pl
