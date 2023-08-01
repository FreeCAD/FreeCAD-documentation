# FreeCAD and DXF Import/pl
## Kontekst

DXF jest zastrzeżonym formatem danych CAD dla rysunków 2D, który wywodzi się z programu AutoCAD. Więcej szczegółów można znaleźć na stronie Wiki [DXF](DXF/pl.md).



## Wprowadzenie

Od wersji 0.18 FreeCAD posiada nowy importer C++ DXF, a od wersji 0.19 również nowy eksporter C++ DXF. Te nowe komponenty są instalowane z programem FreeCAD.

Aby używać starszego importera i eksportera DXF, musisz zainstalować kilka plików. Te pliki nie mogą być dołączone do programu FreeCAD, ponieważ używają bibliotek opublikowanych na licencji, która nie jest kompatybilna z programem FreeCAD.



## Jak zainstalować starszy importer i eksporter DXF 



### Automatycznie

Jeśli pliki nie są jeszcze zainstalowane, przejdź do menu **Edycja → Preferencje ... → Import-Export → DXF** i włącz opcję **Pozwól programowi FreeCAD na automatyczne pobieranie i aktualizacje bibliotek DXF**, aby program FreeCAD automatycznie pobierał i instalował te pliki.

W przypadku programu FreeCAD 0.14 lub starszego należy zainstalować go ręcznie:



### Samodzielnie

1.  Wejdź na stronę [Yorik\'s Github account](https://github.com/yorikvanhavre/Draft-dxf-importer) i pobierz te pliki *(po prawej stronie możesz wybrać \"pobierz jako ZIP\")*.
2.  Umieść pliki w swoim folderze z makrodefinicjami.
3.  Jeśli nie jesteś pewien, gdzie znajduje się ten folder, przejdź do **Edycja → Preferencje ... → Ogólne → Makrodefinicje** i sprawdź pole o nazwie **Ścieżka do pliku makrodefinicji**.

-   W Ubuntu folder z makrami znajduje się w standardowej lokalizacji *(folder jest ukryty, może być konieczne jego celowe wyświetlenie)*:

/home/your_user_name/.FreeCAD 

-   W systemie Windows folder z makrami znajduje się w standardowej lokalizacji:

C:\Użytkownicy \AppData\Roaming\FreeCAD

Zobacz również: [Instalacja importera Dxf](Dxf_Importer_Install/pl.md)



## Porady i sztuczki 

Czasami pliki DXF nie importują się, mimo że otwierają się bez problemów w innych programach CAD.

Możesz spróbować:

1.  Przejdź do menu **Edycja → Preferencje ... → Import-Export → DXF** i usuń zaznaczenie opcji **Łącz geometrie** i spróbuj ponownie.
2.  Pamiętaj, że być może teraz nie będziesz miał zbieżnych punktów końcowych. Możesz sprawić, że będą one zbieżne dzięki funkcji [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md).

Możesz również spróbować:

1.  Przejdź do **Edycja → Preferencje ... → Rysunek Roboczy → Ustawienia ogólne** i dostosuj wartość **Tolerancja** *(domyślnie: 0,05)* i spróbuj ponownie.

Aby uzyskać przegląd wszystkich preferencji związanych z DXF, zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DXF.md).



---
⏵ [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > [File_Formats](Category_File_Formats.md) > FreeCAD and DXF Import/pl
