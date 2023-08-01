---
- GuiCommand:
   Name:PartDesign AdditiveCylinder
   Name/pl:Projekt Części: Addytywny walec
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Addytywny walec
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do dodania](PartDesign_CompPrimitiveAdditive/pl.md), [Subtraktywny walec](PartDesign_SubtractiveCylinder/pl.md)
---

# PartDesign AdditiveCylinder/pl



## Opis

Funkcja ta wstawia pierwotny walec do aktywnej Zawartości jako pierwszy element lub łączy go z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveCylinder_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveCylinder.svg" width=24px> '''Addytywny walec'''**. **Uwaga**: Addytywny walec jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Walec, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Prostopadłościanu.



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
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCylinder/pl
