# Installing Helpfile/pl
### Moduł Pomocy 

**Uwaga:** Pliki pomocy offline programu FreeCAD, opisane poniżej, są wycofywane z użycia. System pomocy FreeCAD jest teraz zarządzany przez [Dodatek Pomocy](https://github.com/yorikvanhavre/FreeCAD-Help), który można zainstalować poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Dodatek Pomoc umożliwia dostęp do dokumentacji online, bez potrzeby pobierania czegokolwiek, lub do kopii offline dokumentacji do pobrania, którą również można zainstalować za pomocą Menedżera dodatków.

## Dokumentacja pomocy FreeCAD 

Dokumentacja FreeCAD offline jest budowana z wiki FreeCAD przy użyciu skryptów. Rozrosła się do rozmiaru pliku przekraczającego 220 MB. Te duże pliki nie są częścią instalatorów i plików wykonywalnych FreeCAD, ale mogą być instalowane oddzielnie, tak jak zostało to tutaj przedstawione.

Zachęca się do pracy nad tłumaczeniami społeczności, dzięki czemu dokumentacja offline jest teraz dostępna również w języku francuskim i włoskim. Dla innych języków mogą istnieć różne etapy zaawansowania.

## Pobierz pliki pomocy 

Dokumentacja działająca w trybie offline składa się z co najmniej dwóch plików: **freecad.qhc** konfiguracja pliku Qt-helpfile i **freecad.qch** skompresowany plik Qt-helpfile. Są one umieszczone razem w archiwum ZIP.

Pliki pomocy można pobrać tutaj: <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z>

W przyszłości będzie można je zainstalować z poziomu FreeCAD za pomocą [Menadżera Dodatków](Std_AddonMgr/pl.md).

Pliki pomocy mają zawsze te same nazwy: **freecad.qhc** i **freecad.qch**. Aby mieć różne wersje plików pomocy, pliki te muszą być zainstalowane w różnych katalogach. W przypadku ręcznego pobierania, wystarczy zapisać plik zip lokalnie i rozpakować archiwum do wybranego katalogu.

## Zarejestrowanie dokumentacji 

System dokumentacji FreeCAD wykorzystuje Qt Assistant. Powinieneś najpierw zainstalować ten program, jeśli go nie posiadasz.

Obecna organizacja pomocy offline pozwala, aby aktywny był tylko jeden plik pomocy. Dlatego nie jest możliwe posiadanie plików pomocy w różnych językach dostępnych jednocześnie z FreeCAD.

Aby aktywować kolejną dokumentację FreeCAD, należy wykonać następujące kroki:

-   Kliknij na liście menu w FreeCAD **Pomoc → Pomoc**. Program Qt-assistant powinien się otworzyć.
-   W programie Qt-assistant kliknij w menu **Edit → preferencje**.
-   W oknie dialogowym preferencji kliknij zakładkę **Documentation**.
-   Na liście zarejestrowanych dokumentów wybierz `org.freecad.usermanual` i kliknij przycisk **Remove**.
-   Zamknij okno dialogowe za pomocą **OK**, ale nie zamykaj okna programu Qt-assistant. Jest to ważne, ponieważ w przeciwnym razie inny plik pomocy nie zostanie zarejestrowany.
-   Otwórz ponownie okno dialogowe preferencji poprzez menu **Edit → preferencje**.
-   Wybierz zakładkę dokumentacja i kliknij przycisk **Dodaj...**.
-   W oknie dialogowym przejdź do nowego pliku pomocy i wybierz **freecad.qch**.
-   Zamknij okno dialogowe, potwierdzając wybór. W zakładce **Documentation** w preferencjach powinna teraz znajdować się linia z `org.freecad.usermanual`.
-   Zamknij **Preferences** za pomocą **OK**.
-   Powinieneś teraz mieć nową dokumentację dostępną w Qt-assistant, która jest dostępna z poziomu FreeCAD.

## Uwaga o Ubuntu 

Podczas próby instalacji pakietów dokumentacji na Ubuntu mogą pojawić się trudności *(na przykład, `freecad-doc` lub `freecad-daily-doc`)*. Jeśli okaże się, że tak jest, to wykonanie następujących kroków umożliwi Ci posiadanie dokumentacji offline.

-   Pobierz pliki pomocy **freecad.qch** help files from <https://github.com/FreeCAD/FreeCAD/releases/download/0.19.2/FreeCAD.0_19.Offline.Doc.7z> i rozpakuj je przy użyciu 7zip.
-   Alternatywnie, możesz zamiast tego pobrać rozwojowe wersje plików pomocy **freecad.qhc** oraz **freecad.qch** z [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Doc). Będziesz musiał scalić wszystkie pliki **.part** [concatenate](http://man7.org/linux/man-pages/man1/cat.1.html) w całość: `cat freecad.qch.part00 freecad.qch.part01 freecad.qch.part02 freecad.qch.part03 > freecad.qch`.



---
⏵ [documentation index](../README.md) > Installing Helpfile/pl
