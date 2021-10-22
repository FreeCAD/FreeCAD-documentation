---
- GuiCommand:/pl
   Name:Std UserEditMode
   Name/pl:Std: Tryb edycji użytkownika
   MenuLocation:Edycja → Tryb edycji → ...
   Workbenches:wszystkie
   Version:0.20
   SeeAlso:[Edycja](Std_Edit/pl.md)
---

# Std UserEditMode/pl

## Opis

Polecenie **Std: Tryb edycji użytkownika** definiuje tryb edycji, który będzie używany, gdy dwukrotnie kliknie się na obiekt w [widoku drzewa](Tree_view/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Kliknij na czarną strzałkę w dół po prawej stronie przycisku **<img src="images/Std_UserEditModeDefault.svg" width=24px> [Std Tryb edycji użytkownika](Std_UserEditMode/pl.md)** a następnie wybierz tryb edycji z menu rozwijanego. Uwaga: ikonka przycisku będzie się zmieniać w zależności od wybranej opcji.
    -   W menu głównym przejdź do **Edycja → Tryb Edycji** i wybierz tryb edycji.

## Dostępne tryby edycji 

### <img alt="" src=images/Std_UserEditModeDefault.svg  style="width:24px;"> Domyślny 

Obiekt będzie edytowany w trybie domyślnym. Ten tryb edycji jest zdefiniowany wewnętrznie jako najbardziej odpowiedni dla typu obiektu. Na przykład, będzie to edycja właściwości kształtu dla [brył pierwotnych](Part_Primitives/pl.md) środowiska Część i [cech](PartDesign_Feature/pl.md) środowiska Projekt Części, edycja umiejscowienia dla [operacji logicznych](Part_Boolean.md) środowiska Część, itd.

### <img alt="" src=images/Std_UserEditModeTransform.svg  style="width:24px;"> Przemieszczenie 

Obiekt będzie miał swoje umiejscowienie, które można edytować za pomocą polecenia [Std: Przemieszczenie](Std_TransformManip.md).

### <img alt="" src=images/Std_UserEditModeCutting.svg  style="width:24px;"> Cięcie 

Ten tryb edycji jest zaimplementowany jako dostępny, ale obecnie nie wydaje się być używany przez żaden obiekt.

### <img alt="" src=images/Std_UserEditModeColor.svg  style="width:24px;"> Kolor 

Obiekt będzie miał kolor poszczególnych ścian, który można edytować za pomocą polecenia [kolor powierzchni](Part_FaceColors/pl.md) środowiska Część.

## Uwagi

-   Nie wszystkie obiekty obsługują dostępne tryby edycji. Jeśli wybrany tryb nie jest obsługiwany przez obiekt, zostanie użyty jego domyślny tryb edycji.

## Ustawienia

-   Używany tryb edycji jest zapisywany w: **Przybory → Edycja parametrów → BaseApp → Preferences → General → UserEditMode**. Jest to wartość całkowita. Możliwe wartości to {{Incode|0}} *(tryb domyślny)*, {{Incode|1}} *(przemieszczenie)*, {{Incode|2}} *(cięcie)* lub {{Incode|3}} *(kolor)*. Domyślnie jest to wartość {{Incode|0}}.

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics.md).

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
FreeCADGui.setUserEditMode(MODENAME) # Where MODENAME is a string available in the list of edit modes
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std UserEditMode/pl
