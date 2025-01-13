# FreeCAD and Mesh Import/pl
## Po imporcie 

Po zaimportowaniu model jest *(dla FreeCAD)* tylko zbiorem ścian. Możesz chcieć przekonwertować model na kształt, który FreeCAD może rozpoznać i który można później edytować w programie FreeCAD.

Aby to zrobić:

1.  Przełącz się do środowiska pracy <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md)
2.  Wybierz siatkę i przejdź do **Część → [Utwórz kształt z siatki](Part_ShapeFromMesh/pl.md)** lub naciśnij przycisk <img alt="" src=images/Part_ShapeFromMesh.svg  style="width:24px;"> [Utwórz kształt z siatki](Part_ShapeFromMesh/pl.md).
3.  Kliknij **OK** w oknie dialogowym
4.  Wybierz nowo utworzony kształt
5.  Przejdź do **Część → [Przekształć na bryłę](Part_MakeSolid/pl.md)**.
6.  Wybierz nowo utworzoną bryłę
7.  Przejdź do **Część → Utwórz kopię → [Udoskonal kształt](Part_RefineShape/pl.md)** lub naciśnij przycisk <img alt="" src=images/Part_RefineShape.svg  style="width:24px;"> [Udoskonal kształt](Part_RefineShape/pl.md).

**Uwaga:** Ostatni krok nie jest konieczny, ale oczyści bryłę z większości krawędzi na powierzchniach płaskich i cylindrycznych.



## Błędy



### \"nie można przekonwertować, ponieważ kształt nie jest powłoką\" 

Cóż, twoja powłoka wydaje się mieć błędy, być może nie jest zamknięta *(ma dziury)*. Ponieważ możliwości środowiska pracy Siatka w FreeCAD są obecnie nieco ograniczone, możesz spróbować sprawdzić i naprawić swój model za pomocą oprogramowania zewnętrznego. Następnie możesz spróbować ponownie zaimportować i przekonwertować model.



## Programy zewnętrzne 

-   [MeshLab](https://www.meshlab.net/),
    -   Licencja: Open Source *(GPL V2)*,
    -   Działa w systemach Windows 32/64 bit, Linux i macOS.
-   [Meshmixer](https://meshmixer.com/),
    -   Licencja: Freeware,
    -   Działa na Windows 64-bit.



## Poradniki

-   [Importowanie plików STL lub OBJ](Import_from_STL_or_OBJ/pl.md)
-   [Eksport do formatu STL lub OBJ](Export_to_STL_or_OBJ.md)



## Powiązane

-   [FreeCAD Jak importować eksportować](FreeCAD_Howto_Import_Export.md)



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and Mesh Import/pl
