# Download/pl
{{TOCright}}

## Aktualne stabilne wersje 

Wydanie **0.20.1** *(29410)* programu FreeCAD zostało opublikowane 2022-08-10. Aby dowiedzieć się o nowościach, zobacz stronę [Informacje o wydaniu](Release_notes_0.20/pl.md).

Sumy kontrolne **SHA256** do weryfikacji wiarygodności pobranych plików znajdziesz na stronie [wydania 0.20.1](https   *//github.com/FreeCAD/FreeCAD/releases/tag/0.20.1).

Poprzednie wersje można pobrać ze strony [wydań](https   *//github.com/FreeCAD/FreeCAD/releases).

+   *   *+   *   *+   *   *+
| ![](images/Windows.png )                                                                                         | ![](images/Mac.png )                                                                                                             | ![](images/Linux_with_text.png )     |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [Install on Windows](Installing_on_Windows.md)                                                                 | [Install on Mac](Installing_on_Mac.md)                                                                                     | [Install on Linux](Installing_on_Linux.md) |
|                                                                                                                        |                                                                                                                                    |                                                    |
| [64-bit installer](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20.1/FreeCAD-0.20.1-WIN-x64-installer-1.exe) | [macOS 64-bit](https   *//github.com/FreeCAD/FreeCAD/releases/download/0.20.1/FreeCAD_0.20-1-2022-08-20-conda-macOS-x86_64-py310.dmg) | [AppImage 64-bit](AppImage.md)             |
++++

### Uwagi dla użytkowników systemu Windows 

-   Obsługiwane są następujące wersje systemu Windows   * 64-bitowy 7/8/10/11. 32-bitowy system Windows nie jest obsługiwany.
-   Wersja portable nie wymaga instalacji i jest dostępna na stronie [wydania](https   *//github.com/FreeCAD/FreeCAD/releases/).
-   Pakiet można również zainstalować za pomocą menedżera [Chocolatey](https   *//chocolatey.org/packages/freecad).

### Uwagi dla użytkowników systemu Mac OS X 

Mac OS X 10.12 **Sierra** jest wersją wymaganą jako minimalna.

### Uwagi dla użytkowników systemu GNU/Linux 

Większość dystrybucji nosi FreeCAD w swoich oficjalnych repozytoriach, jednak jeśli dystrybucja nie podąża za modelem kroczącego wydania, wersja, którą dostarczają, może być nieaktualna. Zamiast tego możesz pobrać powyższy AppImage, oznaczyć go jako wykonywalny i uruchomić go bez instalacji.

Proszę zobaczyć stronę [Kompilacja w systemie Linux](Installing_on_Linux/pl.md), aby uzyskać więcej opcji instalacji, w tym pakietów daily dla Ubuntu i jego pochodnych.

Wersja przenośna, która nie wymaga instalacji, może być osiągnięta przez uruchomienie programu FreeCAD następującymi poleceniami   *


{{Code|lang=text|code=
cd path/to/directory_containing_AppImage/
chmod +x ./name_of_AppImage_file.AppImage
HOME="$PWD/Settings" FREECAD_USER_HOME="$PWD/Settings" ./name_of_AppImage_file.AppImage
}}

Więcej informacji na temat zmiennych środowiskowych FreeCAD można znaleźć na stronie [uruchomienie i konfiguracja](Start_up_and_Configuration/pl#Zmienne_.C5.9Brodowiskowe/pl.md).

## Wersje rozwojowe 

FreeCAD jest aktywnie rozwijany.

-   Jeśli jesteś użytkownikiem Linuksa zapoznaj się z rozwojem [AppImage](AppImage.md).
-   Dla obserwowania rozwoju w MacOS i kompilacji Windows oraz kodu źródłowego, zobacz stronę [weekly builds](https   *//github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds).
-   Aby skompilować najnowszy kod źródłowy, proszę zobaczyć opis [kompilacji](Compiling/pl.md).

## Dodatkowe moduły i makra 

Społeczność FreeCAD dostarcza wiele dodatkowych modułów i makr. Od wersji *0.17* można je łatwo zainstalować z poziomu FreeCAD za pomocą narzędzia [menadżer dodatków](Std_AddonMgr/pl.md)<img alt="" src=images/Std_AddonMgr.svg  style="width   *22px;">.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Download/pl
