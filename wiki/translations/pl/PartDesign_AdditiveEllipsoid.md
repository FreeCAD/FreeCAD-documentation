---
- GuiCommand:
   Name: PartDesign AdditiveEllipsoid
   Name/pl: Projekt Części: Addytywna elipsoida
   MenuLocation: Projekt Części -> Utwórz cechę przez dodanie -> Addytywna elipsoida
   Workbenches: PartDesign_Workbench/pl
   Version: 0.17
   SeeAlso: PartDesign_CompPrimitiveAdditive/pl, PartDesign_SubtractiveEllipsoid/pl
---

# PartDesign AdditiveEllipsoid/pl



## Opis

Funkcja ta wstawia pierwotną elipsoidę do aktywnej Zawartości jako pierwszy element lub łączy ją z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveEllipsoid_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveEllipsoid.svg" width=24px> '''Addytywna elipsoida'''**. **Uwaga**: Addytywna elipsoida jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywna elipsoida wyświetlana jest na pasku narzędzi domyślnie. Aby przejść do funkcji Elipsoia, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Prostopadłościanu.



## Opcje

Elipsoidę można edytować po jej utworzeniu na dwa sposoby:

-   Klikając ją dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Elipsoida. Zmień zgodnie z własnymi potrzebami.

-    **Promień1**: wartość promienia wzdłuż pionowej osi elipsoidy; domyślnie równoległa do osi Z.

-    **Promień2**: wartość promienia wzdłuż długości elipsoidy; domyślnie równoległa do osi X.

-    **Promień3**: wartość promienia wzdłuż szerokości elipsoidy; domyślnie równolegle do osi Y. Przy domyślnej wartości zero, elipsoida tworzy [spłaszczoną sferoidę](http://en.wikipedia.org/wiki/Oblate_spheroid). Ma to taką samą postać, jak gdyby parametr Promień3 był identyczny z Promień2.

-    **Kąt1**: *(oznaczony jako **parametr V** w parametrach Prymitywu)* dolne obcięcie elipsoidy, równoległe do przekroju kołowego *(-90° w pełnej sferoidzie)*.

-    **Kąt2**: *(nieoznaczone w parametrach Prymitywu)* górne obcięcie elipsoidy, równoległe do przekroju kołowego *(90° w pełnej sferoidzie)*.

-    **Kąt3**: *(oznaczony jako **parametr U** w parametrach Prymitywu)* kąt obrotu eliptycznego przekroju poprzecznego *(360° w pełnej sferoidzie)*.





{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveEllipsoid/pl
