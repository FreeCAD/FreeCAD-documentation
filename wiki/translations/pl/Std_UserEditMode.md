---
 GuiCommand:
   Name: Std UserEditMode
   Name/pl: Std: Tryb edycji
   MenuLocation: Edycja , Przełącz tryb edycji , ...
   Workbenches: wszystkie
   Version: 0.20
   SeeAlso: Std_Edit/pl
---

# Std UserEditMode/pl



## Opis

Polecenie **Std: Tryb edycji użytkownika** definiuje tryb edycji, który będzie używany, gdy dwukrotnie kliknie się na obiekt w [widoku drzewa](Tree_view/pl.md).



## Użycie

1.  W menu głównym przejdź do **Edycja → Przełącz tryb Edycji** i wybierz tryb edycji.



## Dostępne tryby edycji 



### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> Domyślny 

Obiekt będzie edytowany w trybie domyślnym. Ten tryb edycji jest zdefiniowany wewnętrznie jako najbardziej odpowiedni dla typu obiektu. Na przykład, będzie to edycja właściwości kształtu dla [brył pierwotnych](Part_Primitives/pl.md) środowiska Część i [cech](PartDesign_Feature/pl.md) środowiska Projekt Części, edycja umiejscowienia dla [operacji logicznych](Part_Boolean.md) środowiska Część, itd.



### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width:24px;"> Przemieszczenie 

Obiekt będzie miał swoje umiejscowienie, które można edytować za pomocą polecenia [Std: Przemieszczenie](Std_TransformManip.md).



### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width:24px;"> Cięcie 

Ten tryb edycji jest zaimplementowany jako dostępny, ale obecnie nie wydaje się być używany przez żaden obiekt.



### <img alt="" src=images/Std_UserEditModeColor.svg  style="width:24px;"> Kolor 

Obiekt będzie miał kolor poszczególnych ścian, który można edytować za pomocą polecenia [Kolor powierzchni](Part_ColorPerFace/pl.md).



## Uwagi

-   Nie wszystkie obiekty obsługują dostępne tryby edycji. Jeśli wybrany tryb nie jest obsługiwany przez obiekt, zostanie użyty jego domyślny tryb edycji.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby wyświetlić listę dostępnych trybów edycji:


```python
import FreeCADGui
FreeCADGui.listUserEditModes()
```

Aby przejść do aktywnego trybu edycji:


```python
import FreeCADGui
FreeCADGui.getUserEditMode()
```

Aby ustawić aktywny tryb edycji:


```python
import FreeCADGui
FreeCADGui.setUserEditMode(MODENAME)  # Where MODENAME is a string available in the list of edit modes
```





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std UserEditMode/pl
