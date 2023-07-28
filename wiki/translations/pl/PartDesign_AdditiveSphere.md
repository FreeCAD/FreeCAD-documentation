---
- GuiCommand:/pl
   Name:PartDesign AdditiveSphere
   Name/pl:Projekt Części: Addytywna sfera
   MenuLocation:Projekt Części → Utwórz cechę przez dodanie → Addytywna sfera
   Workbenches:[Projekt Części](PartDesign_Workbench/pl.md)
   Version:0.17
   SeeAlso:[Komponent bryła pierwotna do dodania](PartDesign_CompPrimitiveAdditive/pl.md), [Subtraktywna sfera](PartDesign_SubtractiveSphere/pl.md)
---

# PartDesign AdditiveSphere/pl



## Opis

Funkcja ta wstawia pierwotną sferę do aktywnej Zawartości jako pierwszy element lub łączy ją z istniejącymi elementami.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">



## Użycie

1.  Naciśnij przycisk **<img src="images/PartDesign_AdditiveCylinder.svg" width=24px> '''Addytywna sfera'''**. **Uwaga**: Addytywna sfera jest częścią menu narzędzi o nazwie **Utwórz bryłę pierwotną do dodania**. Po uruchomieniu programu FreeCAD, Addytywny prostopadłościan wyświetlany jest na pasku narzędzi domyślnie. Aby przejść do funkcji Sfera, kliknij strzałkę w dół na widocznej ikonce i wybierz z menu opcję Addytywny walec.
2.  Ustaw parametry bryły i [dołączenia](Part_EditAttachment/pl.md).
3.  Kliknij **OK**.
4.  Pod aktywnym obiektem Zawartość pojawi się element Sfera.



## Opcje

Sferę można edytować po jej utworzeniu na dwa sposoby:

-   Klikając go dwukrotnie w drzewie modelu lub klikając prawym przyciskiem myszy i wybierając **Edytuj bryłę pierwotną** z menu podręcznego. Spowoduje to wyświetlenie parametrów bryły pierwotnej.
-   Poprzez [Edytor właściwości](Property_editor/pl.md).



## Właściwości

-    **Dołączenie**: definiuje tryb dołączania, a także przesunięcie dołączania. Zobacz też [Część: Edycja mocowania](Part_EditAttachment/pl.md).

-    **Etykieta**: Etykieta nadana obiektowi Sfery. Zmień zgodnie z własnymi potrzebami.

-    **Promień**: Promień sfery.

-    **Kąt1**: *(oznaczony jako **parametr V** w parametrach Primitywu)* dolne obcięcie kuli, równoległe do przekroju kołowego *(-90° w pełnej kuli)*.

-    **Kąt2**: *(nieoznaczony w parametrach Primitywu)* górne obcięcie sfery, równoległe do przekroju kołowego *(90° w pełnej sferze)*.

-    **Kąt3**: *(oznaczony jako **parameter U** w parametrach Primitywu)* kąt obrotu przekroju poprzecznego *(360° w pełnej kuli)*.





{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/pl
