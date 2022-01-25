# FreeCAD API/pl
**''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Jest to główny *(root)* moduł programu FreeCAD. Może być również wywołany przez \"App\" z interpretera FreeCAD. Zawiera wszystko, co jest potrzebne do manipulowania dokumentami i ich zawartością *(obiektami)*.

Przykład: 
```python
import FreeCAD
print FreeCAD.listDocuments()
mydoc = FreeCAD.activeDocument()
```


{{APIFunction|ConfigDump| |Wydrukuje słownik z informacjami zawierający całą konfigurację środowiska FreeCAD}}

. {{APIFunction|ConfigGet|[string]| Zwraca wartość podanego klucza. Jeśli nie podano klucza, zwracana jest pełna konfiguracja - ciąg znaków.}} {{APIFunction|ConfigSet|string, string|Ustawia podany klucz (pierwszy ciąg) na podaną wartość (drugi ciąg).| }} {{APIFunction|Version| |Wydrukuje wersję FreeCAD.| }} {{APIFunction|activeDocument| |Zwraca aktywny dokument lub nic, jeśli nie ma aktywnego dokumentu.|Dokument FreeCAD.|}} {{APIFunction|addExportType|string, string|Dodaje nowy typ pliku eksportu do FreeCAD. Pierwszy ciąg znaków musi być sformatowany jak w tym przykładzie: "Dokument Word (*.doc)". Drugi łańcuch to nazwa skryptu/modułu Pythona zawierającego funkcję export().| }} {{APIFunction|addImportType|string, string|Dodaje nowy typ pliku importu do FreeCAD, działa tak samo jak addExportType, obsługujący moduł pythona musi zawierać funkcję open() i/lub import().| }} {{APIFunction|closeDocument|Nazwa dokumentu|Zamyka podany dokument| }} {{APIFunction|getDocument|Nazwa dokumentu|Zwraca dokument lub wywołuje wyjątek, jeśli nie ma dokumentu o podanej nazwie.| }} {{APIFunction|getExportType|string|Przywraca nazwę modułu, który może eksportować określony typ pliku.|string.}} {{APIFunction|getImportType|string|Przywraca nazwę modułu, który może importować określony typ pliku.|string.}} {{APIFunction|listDocuments| |Zwraca słownik nazw i wskaźników obiektów wszystkich dokumentów.|Słownik nazw i wskaźników obiektów.}} {{APIFunction|newDocument|[string], [hidden<nowiki>=</nowiki>False]|Tworzy i zwraca nowy dokument o podanej nazwie. Nazwa dokumentu musi być unikalna, co jest sprawdzane automatycznie. Jeśli nie zostanie podana nazwa, dokument będzie miał nazwę "Bez tytułu". Jeśli parametr <tt>hidden<nowiki>=</nowiki>{{True/pl}}</tt> zostanie przekazane, to FreeCAD w trybie GUI nie wyświetli dokumentu i nie pokaże zakładki dla dokumentu. Pozwala to na wykonywanie automatycznych operacji na tymczasowym dokumencie ''(lub utworzenie dokumentu i zapisanie go)'' bez zakłócania interfejsu użytkownika.|Nowo utworzony dokument.}} {{APIFunction|open|string|Patrz: openDocument| }} {{APIFunction|openDocument|filepath, [hidden]|Tworzy i zwraca dokument oraz wczytuje do niego plik projektu. Argument łańcuchowy musi wskazywać na istniejący plik. Jeśli plik nie istnieje lub nie można go załadować, zostanie wyrzucony wyjątek wejścia/wyjścia. W tym przypadku utworzony dokument zostanie zachowany, ale będzie pusty. Jeśli parametr <tt>hidden<nowiki>=</nowiki>{{True/pl}}</tt> zostanie przekazane, to FreeCAD w trybie GUI nie wyświetli dokumentu i nie pokaże zakładki dla dokumentu. Pozwala to na wykonywanie automatycznych operacji na dokumencie i zamknięcie go bez zakłócania interfejsu użytkownika.|Otwarty dokument FreeCAD.}} {{APIFunction|setActiveDocument|Nazwa dokumentu|Ustawia aktywny dokument po jego nazwie.| }}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > FreeCAD API/pl
