---
 GuiCommand:
   Name: PartDesign AdditivePrism
   Name/pl: Projekt Części: Addytywny graniastosłup
   MenuLocation: Projekt Części , Utwórz cechę przez dodanie , Addytywny graniastosłup
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/pl, PartDesign_SubtractivePrism/pl
---

# PartDesign AdditivePrism/pl



## Opis

Funkcja ta wstawia pierwotny graniastosłup do aktywnej Zawartości jako pierwszy element lub łączy go z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditivePrism.svg" width=24px> '''Addytywny graniastosłup'''**. **Uwaga**: Addytywny graniastosłup jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Graniastosłup, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Torus.



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





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditivePrism/pl
