---
- GuiCommand:
   Name:PartDesign SubtractiveTorus
   Name/pl:Projekt Części: Subtraktywny torus
   MenuLocation:Projekt Części → Utwórz cechę przez odjęcie → Subtraktywny torus
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do odjęcia](PartDesign_CompPrimitiveSubtractive/pl.md), [Addytywny torus](PartDesign_AdditiveTorus/pl.md)
---

# PartDesign SubtractiveTorus/pl



## Opis

Funkcja ta wstawia pierwotny torus odejmowany od aktywnej Zawartości. Jego kształt jest odejmowany od istniejącej bryły.

![](images/PartDesign_SubtractiveTorus_example.svg ) *Po lewej: aktywna zawartość (A) pokazana w kolorze szarym i torus do odjęcia (B) pokazany w kolorze czerwonym z przeźroczystością. Wynik po prawej*.



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_SubtractiveTorus.svg" width=24px> '''Subtraktywny torus'''**. **Uwaga**: Subtraktywny torus jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do odjęcia**. Po uruchomieniu programu FreeCAD, Subtraktywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Torus, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Subtraktywny torus.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Torus.



## Opcje

Torus można edytować po jego utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Stożka. Zmień zgodnie z własnymi potrzebami.

-    **Promiień1**: Promień umownej orbity, wokół której obraca się przekrój kołowy. *(Odległość między środkiem torusa a środkiem obracającego się przekroju)*

-    **Promiień2**: Promień okrągłego przekroju definiującego kształt torusa.

-    **Kąt1**: *(oznaczony jako **parametr V** w parametrach Prymitywu)* dolne obcięcie torusa, równoległe do przekroju kołowego *(-180° w pełnym torusie)*. Błąd w źródłach powoduje nieoczekiwane wyniki przy zmianie parametru Kąt1.

-    **Kąt2**: *(nieoznaczone w parametrach Prymitywu)* górne obcięcie elipsoidy, równoległe do przekroju kołowego *(180° w pełnym torusie)*. Błąd w źródłach powoduje nieoczekiwane wyniki przy zmianie parametru Kąt2.

-    **Kąt3**: *(oznaczony jako **parametr U** w parametrach Prymitywu)* kąt obrotu przekroju kołowego *(360° dla pełnego torusa)*.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/pl
