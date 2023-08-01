---
- GuiCommand:/pl
   Name:Mesh Import
   Name/pl:Siatka: Import
   MenuLocation:Siatki → Importuj siatkę ...
   Workbenches:[Siatka](Mesh_Workbench/pl.md)
   SeeAlso:[Importuj](Std_Import/pl.md), [Otwórz](Std_Open/pl.md), [Import Eksport](Import_Export/pl.md)
---

# Mesh Import/pl

## Opis

Polecenie **Importuj siatkę** importuje geometrię z formatu pliku siatki do aktywnego dokumentu. Obsługiwanych jest kilka formatów plików. Polecenie tworzy nieparametryczny obiekt siatki, [cechę](Mesh_Feature/pl.md).

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_Import.svg" width=16px> [Importuj siatkę ...](Mesh_Import/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_Import.svg" width=16px> Importuj siatkę ...**.
    -   Wybierz opcję **<img src="images/Mesh_Import.svg" width=16px> Importuj siatkę ...** z menu podręcznego w oknie [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md). Ta opcja jest dostępna tylko wtedy, gdy został wybrany istniejący obiekt siatki. Zauważ, że wybrany obiekt nie jest w rzeczywistości używany ani modyfikowany przez polecenie.
2.  Opcjonalnie wybierz odpowiedni format pliku w oknie dialogowym.
3.  Wybierz plik.
4.  Naciśnij przycisk **Otwórz**.

## Obsługiwane formaty plików 

Polecenie obsługuje pliki: stl, ast, bms, obj, off, iv, ply, nas i bdf. Dla formatu plików NASTRAN *(nas/bdf)* obsługiwane są tylko karty GRID, CTRIA3 i CQUAD4.

## Ustawienia

-   Przechowywana jest ostatnio używana lokalizacja pliku: **Przybory → Edycja parametrów ... → BaseApp → Preferences → General → FileOpenSavePath**.

## Właściwości

Zapoznaj się z informacjami na stronie: [cecha siatki](Mesh_Feature/pl.md).

## Tworzenie skryptów 

Zobacz również: [FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Aby zaimportować plik siatki użyj metody `insert` modułu *Mesh*.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import/pl
