# Download/pl
## Aktualne stabilne wersje 

Wydanie **1.0** programu FreeCAD zostało opublikowane 2024-11-18. Aby dowiedzieć się o nowościach, zobacz stronę [Informacje o wydaniu](Release_notes_1.0/pl.md).

Sumy kontrolne **SHA256** do weryfikacji wiarygodności pobranych plików znajdziesz na stronie [wydania 1.0](https://github.com/FreeCAD/FreeCAD/releases/tag/1.0).

Poprzednie wersje można pobrać ze strony [wydań](https://github.com/FreeCAD/FreeCAD/releases).

+::+::+::+
| ![](images/Windows.png )                                                                                                          | ![](images/Mac.png )                                                                                                            | ![](images/Linux_with_text.png )                                                                                  |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [Install instructions](Installing_on_Windows.md)                                                                                | [Install instructions](Installing_on_Mac.md)                                                                              | [Install instructions](Installing_on_Linux.md)                                                                          |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit installer](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-installer-1.exe)       | [ARM (M-series) disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-arm64-py311.dmg) | [x86_64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)   |
|                                                                                                                                         |                                                                                                                                   |                                                                                                                                 |
| [64-bit portable version (.7z)](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Windows-x86_64-py311.7z) | [Intel disk image](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-macOS-x86_64-py311.dmg)         | [aarch64 AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-aarch64-py311.AppImage) |
++++



### Uwagi dla użytkowników systemu Windows 

-   Obsługiwane są następujące wersje systemu Windows: 64-bitowy 8/10/11.
-   Pakiet można również zainstalować za pomocą menedżera [Chocolatey](https://chocolatey.org/packages/freecad). Chocolatey nie jest obecnie aktualny.



### Uwagi dla użytkowników systemu Mac OS 

Mac OS X 10.12 **Sierra** jest wersją wymaganą jako minimalna.



### Uwagi dla użytkowników systemu GNU/Linux 

Większość dystrybucji nosi FreeCAD w swoich oficjalnych repozytoriach, jednak jeśli dystrybucja nie podąża za modelem kroczącego wydania, wersja, którą dostarczają, może być nieaktualna. Zamiast tego możesz pobrać powyższy AppImage, oznaczyć go jako wykonywalny i uruchomić go bez instalacji.

Proszę zobaczyć stronę [Kompilacja w systemie Linux](Installing_on_Linux/pl.md), aby uzyskać więcej opcji instalacji, w tym pakietów daily dla Ubuntu i jego pochodnych.

Wersja przenośna, która nie wymaga instalacji, może być osiągnięta przez uruchomienie programu FreeCAD następującymi poleceniami:


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Więcej informacji na temat zmiennych środowiskowych FreeCAD można znaleźć na stronie [uruchomienie i konfiguracja](Start_up_and_Configuration/pl#Zmienne_.C5.9Brodowiskowe/pl.md).



## Wersje rozwojowe 

FreeCAD jest aktywnie rozwijany.

-   Aby uzyskać kompilacje rozwojowe i kod źródłowy, zobacz stronę [weekly builds](https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds). Cotygodniowe kompilacje są dostępne dla systemów Linux, MacOS i Windows. Dla Linuksa dostępne są również codzienne kompilacje: użyj kanału edge [pakiet snap](Ubuntu_Snap/pl.md) lub [FreeCAD daily PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily) *(ten ostatni tylko dla dystrybucji opartych na Debianie)*.
-   Aby skompilować najnowszy kod źródłowy, proszę zobaczyć opis [kompilacji](Compiling/pl.md).



## Dodatkowe moduły i makra 

Społeczność FreeCAD dostarcza wiele dodatkowych modułów i makr. Można je łatwo zainstalować z poziomu FreeCAD za pomocą narzędzia <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżer dodatków](Std_AddonMgr/pl.md).



---
⏵ [documentation index](../README.md) > Download/pl
