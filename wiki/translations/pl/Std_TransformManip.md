---
 GuiCommand:
   Name: Std TransformManip
   Name/pl: Std: Przemieszczenie
   MenuLocation: Edycja , Przemieszczenie
   Workbenches: Wszystkie
   SeeAlso: Std_UserEditMode/pl
---

# Std TransformManip/pl



## Opis

Narzędzie **Przemieszczenie** pozwala na stosowanie przyrostów obrotu oraz przesunięcia względem obiektu.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">



## Użycie

1.  Wybierz obiekt z właściwością **Umiejscowienie**. Zobacz [Uwagi](#Uwagi.md).
2.  Istnieje kilka sposobów wywołania polecenia:
    -   Wybierz opcję z menu **Edycja → <img src="images/Std_TransformManip.svg" width=16px> Przemieszczenie**.
    -   Wybierz opcję **<img src="images/Std_TransformManip.svg" width=16px> Przemieszczenie** z menu podręcznego [Widoku drzewa](Tree_view/pl.md).
    -   Jeśli [tryb edycji](Std_UserEditMode/pl.md) jest ustawiony na **<img src="images/Std_UserEditModeTransform.svg" width=16px> Przemieszczenie** można również kliknąć dwukrotnie obiekt w widoku drzewa.
3.  Otworzy się panel zadań **Przyrosty**.
4.  Opcjonalnie dostosuj parametry przyrostów.
5.  Wykonaj jedną lub więcej z poniższych czynności:
    -   Naciśnij i przytrzymaj lewy przycisk myszy na strzałce osi i przeciągnij, aby przesunąć obiekt wzdłuż tej osi.
    -   Naciśnij i przytrzymaj lewy przycisk myszy na płaszczyźnie i przeciągnij, aby przesunąć obiekt wzdłuż tej płaszczyzny.
    -   Naciśnij i przytrzymaj lewy przycisk myszy na kuli i przeciągnij, aby obrócić obiekt wokół tej osi.
6.  Wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk **OK**, aby potwierdzić i zakończyć polecenie.
    -   Naciśnij przycisk **Anuluj**, aby przywrócić zastosowane przekształcenia i zakończyć polecenie. {{Version/pl|1.0}}



## Uwagi

-   Gdy tylko obrócisz/przesuniesz obiekt w oknie [widoku 3D](3D_view/pl.md), zmiany zostaną zastosowane.
-   Niektóre obiekty z właściwością **Umiejscowienie**, takie jak szkice, nie mogą być manipulowane, podobnie jak obiekty dołączone do innych obiektów.
-   W {{VersionMinus/pl|0.21}} nie ma przycisku **Anuluj**, w tych wersjach można nacisnąć przycisk **OK** i użyć <img alt="" src=images/Std_Undo.svg  style="width:16px;"> [Cofnij](Std_Undo/pl.md), aby cofnąć zmiany.



---
⏵ [documentation index](../README.md) > Std TransformManip/pl
