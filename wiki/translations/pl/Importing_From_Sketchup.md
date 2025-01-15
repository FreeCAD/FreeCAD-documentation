# Importing From Sketchup/pl
{{Fake heading|sub=4|< Powrót do [FreeCAD Jak importować, eksportować](FreeCAD_Howto_Import_Export.md)}}

## Najlepsza metoda 




Z doświadczenia wynika, że obecnie najlepszą metodą importu pliku ze Sketchup jest użycie formatu Collada *(\*.dae)*. FreeCAD nie obsługuje natywnie formatu Collada. Aby mieć tę funkcjonalność w FreeCAD, użytkownik musi zainstalować moduł Python do importowania i eksportowania tego formatu. Jest to stosunkowo łatwe zadanie do wykonania, a instrukcje można znaleźć na stronie [Dodatkowe moduły Python](Extra_python_modules/pl.md). Bezpośredni link do instrukcji to - [Extra python modules: pyCollada](http://www.freecadweb.org/wiki/index.php?title=Extra_python_modules#pyCollada).



## Import plików Collada (\*.dae) 

Po zainstalowaniu modułu pyCollada można otwierać lub importować pliki Collada tak jak wszystkie inne. Wybierz menu Plik, a następnie opcję Otwórz lub Importuj. Wybierz plik Collada i kliknij Otwórz. Możesz filtrować typ pliku, wybierając rozwijaną listę Pliki typu w oknie dialogowym Otwórz lub Importuj i wybierając Collada *(\*.dae)* z listy.



## Alternatywy

Korzystając z wtyczki eksportu Sketchup STL, można również wybrać format, który FreeCAD obsługuje natywnie. Istnieje wiele takich wtyczek dostępnych dla Sketchup, a niektóre z nich działają lepiej niż inne. Użytkownik może być zmuszony do sprawdzenia, która z nich najlepiej zaspokoi jego potrzeby.



## Uwagi

Zarówno Collada *(\*.dae)*, jak i STL są formatami siatki. Aby użyć tych plików w programie FreeCAD, który działa głównie z bryłami, w większości przypadków wymagana będzie dodatkowa praca z obiektami zaimportowanymi przy użyciu tych formatów.



## Powiązane

-   [FreeCAD Jak importować, eksportować](FreeCAD_Howto_Import_Export.md)
-   [Import Eksport](Import_Export/pl.md)
-   [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl.md)



---
⏵ [documentation index](../README.md) > [Common Questions](Category_Common%20Questions.md) > [File_Formats](Category_File_Formats.md) > Importing From Sketchup/pl
