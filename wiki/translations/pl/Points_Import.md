---
- GuiCommand:/pl
   Name:Points Import
   Name/pl:Punkty: Import
   MenuLocation:Punkty → Import punktów ...
   Workbenches:[Punkty](Points_Workbench/pl.md)
   SeeAlso:[Import Eksport](Import_Export/pl.md)
---

# Points Import/pl

## Opis

Polecenie **Import punktów** importuje chmurę punktów z pliku.

## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Points_Import.svg" width=16px> '''Import punktów ...'''**.
    -   Wybierz z menu opcję **Punkty → <img src="images/Points_Import.svg" width=16px> Importuj punktów ...**.
2.  Wybierz plik chmury punktów.
3.  Naciśnij przycisk **Otwórz**.

## Właściwości

Zobacz stronę [Konwertuj na punkty](Points_Convert/pl.md).

## Format pliku chmury punktów 

-   Plik chmury punktów musi mieć rozszerzenie **.asc**, **.pcd** lub **.ply**.
-   Każda linia pliku musi zawierać współrzędne X, Y i Z punktu.
-   Współrzędne muszą być oddzielone spacjami.
-   We współrzędnych musi być użyty znak dziesiętny, a nie przecinek.

## Przykładowy plik chmury punktów 

0 0 0
1.4562 -7.2354 12.2367
5.9423 3.1728 -17.6439

Do testów możesz użyć [ten plik](https://raw.githubusercontent.com/FreeCAD/Examples/master/Point_cloud_ExampleFiles/PointCloud-Data_Stanford-Bunny.asc), który jest wersją low polygon [Stanford Bunny](http://graphics.stanford.edu/data/3Dscanrep/).





{{Points Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Points](Points_Workbench.md) > Points Import/pl
