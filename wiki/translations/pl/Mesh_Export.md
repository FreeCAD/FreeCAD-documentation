---
- GuiCommand:
   Name:Mesh Export
   Name/pl:Siatka: Eksportuj
   MenuLocation:Siatki - Eksportuj siatkę ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Eksport](Std_Export/pl.md), [Import Eksport](Import_Export/pl.md)
---

# Mesh Export/pl

## Opis

Polecenie **Eksportuj siatkę \...** eksportuje obiekt siatkowy do formatu pliku siatkowego. Obsługiwanych jest kilka formatów plików.

## Użycie

1.  Wybierz pojedynczy obiekt siatki.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_Export.svg" width=16px> [Eksportuj siatkę ...](Mesh_Export/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_Export.svg" width=16px> Eksportuj siatkę ...**.
    -   Wybierz opcję **<img src="images/Mesh_Export.svg" width=16px> Eksportuj siatkę ...** z menu kontekstowego okna [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md).
3.  Wybierz odpowiedni format pliku w oknie dialogowym.
4.  Wprowadź nazwę pliku. Jeśli w poprzednim kroku wybrałeś opcję {{Value|Wszystkie pliki (*.*)}} i nie podałeś tutaj rozszerzenia pliku, zostanie użyte rozszerzenie **.stl**.
5.  Naciśnij przycisk **Zapisz**.

## Uwagi

Istnieje kilka [preferencji eksportu związanych z formatami siatki](Import_Export_Preferences/pl#Formaty_Siatki.md), ale nie dotyczą one tego polecenia. Są one używane przez polecenie [Std: Eksport](Std_Export/pl.md).

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby wyeksportować obiekty *(w tym obiekty siatkowe)* do formatu pliku siatkowego użyj metody `export` modułu *Mesh*.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D:/testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/pl
