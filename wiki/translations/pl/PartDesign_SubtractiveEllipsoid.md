---
- GuiCommand:
   Name:PartDesign SubtractiveEllipsoid
   Name/pl:Projekt Części: Subtraktywna elipsoida
   MenuLocation:Projekt Części → Utwórz cechę przez odjęcie → Subtraktywna elipsoida
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do odjęcia](PartDesign_CompPrimitiveSubtractive/pl.md), [Addytywna elipsoida](PartDesign_AdditiveEllipsoid/pl.md)
---

# PartDesign SubtractiveEllipsoid/pl



## Opis

Funkcja ta wstawia pierwotną elipsoidę odejmowaną od aktywnej Zawartości. Jej kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

*Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i elipsoida do odjęcia (B) pokazana w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveEllipsoid.svg" width=24px> '''Subtraktywna elipsoida'''**. **Uwaga**: Subtraktywna elipsoida jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Elipsoia, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywna elipsoida.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Elipsoia.



## Opcje

Elipsoidę można edytować po jej utworzeniu na dwa sposoby:

-   Klikając ją dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Elipsoida. Zmień zgodnie z własnymi potrzebami.

-    **Promień1**: wartość promienia wzdłuż pionowej osi elipsoidy; domyślnie równoległa do osi Z.

-    **Promień2**: wartość promienia wzdłuż długości elipsoidy; domyślnie równoległa do osi X.

-    **Promień3**: wartość promienia wzdłuż szerokości elipsoidy, domyślnie równolegle do osi Y. Przy domyślnej wartości zero, elipsoida tworzy [spłaszczoną sferoidę](http://en.wikipedia.org/wiki/Oblate_spheroid).

-    **Kąt1**: *(oznaczony jako **parametr V** w parametrach Prymitywu)* dolne obcięcie elipsoidy, równoległe do przekroju kołowego *(-90° w pełnej sferoidzie)*.

-    **Kąt2**: *(nieoznaczone w parametrach Prymitywu)* górne obcięcie elipsoidy, równoległe do przekroju kołowego *(90° w pełnej sferoidzie)*.

-    **Kąt3**: *(oznaczony jako **parametr U** w parametrach Prymitywu)* kąt obrotu eliptycznego przekroju poprzecznego *(360° w pełnej sferoidzie)*.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveEllipsoid/pl
