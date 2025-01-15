# FreeCAD and DWG Import/pl
{{Fake heading|sub=4|< Powrót do [FreeCAD Jak importować eksportować](FreeCAD_Howto_Import_Export.md)}}



## Dlaczego trudno jest obsługiwać pliki DWG w FreeCAD? 

Format DWG jest zamkniętym formatem plików binarnych, który nie jest bezpośrednio obsługiwany przez FreeCAD. Wymaga zewnętrznego konwertera plików do konwersji plików DWG na DXF i odwrotnie.



## Czego potrzebuję, aby móc importować pliki DWG? 

### LibreDWG

-   strona główna: <https://www.gnu.org/software/libredwg/> .
-   licencja: [GPLv3-or-later](https://savannah.gnu.org/projects/libredwg/).
-   funkcjonalność opcjonalna, używana do włączania importu i eksportu plików DWG.

GNU LibreDWG to darmowa biblioteka C do obsługi plików DWG. Ma ona być darmowym zamiennikiem bibliotek Open Design Alliance Drawings SDK. Należy pamiętać, że ponieważ libreDWG jest w trakcie opracowywania, nie obsługuje niektórych elementów DWG.



#### Instalacja Windows 

Pobierz i rozpakuj odpowiedni [prekompilowany plik binarny Windows](https://github.com/LibreDWG/libredwg/releases). Umieść plik wykonywalny w ścieżce wyszukiwania systemu operacyjnego, {{Incode|os.getenv("PATH")}}, w celu automatycznego wykrycia *({{Version/pl|0.21}})*, lub ustaw ścieżkę ręcznie. Zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md).



#### Instalacja w systemach Linux / Unix 


{{Code|lang=shell|code=
git clone --recurse-submodules https://github.com/LibreDWG/libredwg.git
cd libredwg
mkdir build
cd build
cmake ..
make
make install # lub użyj checkinstall, lub po prostu zlokalizuj i skopiuj dwg2dxf
             # do lokalizacji plików wykonywalnych, zostanie ono automatycznie wykryte przez FreeCAD
}}

Umieść plik wykonywalny w ścieżce wyszukiwania systemu operacyjnego, {{Incode|os.getenv("PATH")}}, w celu automatycznego wykrywania *({{Version/pl|0.21}})*, lub ustaw ścieżkę ręcznie. Zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md).



#### Instalacja openSUSE 

Aby uniknąć problemów, należy użyć pakietu LibreDWG skompilowanego dla zainstalowanej dystrybucji openSUSE OS. LibreDWG jest zwykle instalowany z **YAST** *(skrót od **Y**et **a**nother **S**etup **T**ool)*, narzędziem instalacyjnym i konfiguracyjnym systemu operacyjnego Linux.

Bardziej doświadczony użytkownik otrzymuje najpierw przegląd możliwych pakietów. **Uwaga:** openSUSE ma kilka opcji do wyboru podczas pobierania LibreDWG. Aby zobaczyć te opcje, przejdź na stronę [Survey of provided LibreDWG packages on openSUSE](https://software.opensuse.org/search?utf8=%E2%9C%93&baseproject=ALL&q=libredwg).

W przypadku np. 64-bitowych komputerów stacjonarnych, laptopów i serwerów Intel lub AMD należy wybrać wersję *(x86_64)*. Tak więc **libredwg0** i **libredwg-tools** są właściwym wyborem do zainstalowania.

Zaleca się, aby bezpośrednio pobrać pakiety binarne. Następnie wybierz właściwą dystrybucję dla zainstalowanego openSUSE OS.

W dowolnym terminalu / konsoli *(wymagane prawa roota)* instalacja zostanie przeprowadzona za pomocą:


```python
zypper install libredwg0 libredwg-tools
```

Umieść plik wykonywalny w ścieżce wyszukiwania systemu operacyjnego, {{Incode|os.getenv("PATH")}}, w celu automatycznego wykrywania *({{Version/pl|0.21}})*, lub ustaw ścieżkę ręcznie. Zobacz stronę [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md).



### Konwerter plików ODA 

-   strona główna: <https://www.opendesign.com/guestfiles/oda_file_converter>
-   licencja: freeware.
-   opcjonalny, używany do włączania importu i eksportu plików DWG.

Konwerter plików ODA to małe, swobodnie dostępne narzędzie, które umożliwia konwersję między kilkoma wersjami plików DWG i DXF. FreeCAD może go używać do oferowania importu i eksportu DWG, konwertując pliki DWG do formatu DXF w tle, a następnie używając standardowego importera DXF do importowania zawartości pliku. Obowiązują ograniczenia [importera DXF](Draft_DXF/pl.md).



#### Instalacja

Jeśli narzędzie nie zostanie znalezione automatycznie przez FreeCAD po instalacji, należy ręcznie ustawić ścieżkę do pliku wykonywalnego. Więcej informacji na ten temat można znaleźć na stronie [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md).



### QCAD Pro 


{{Version/pl|0.20}}

-   strona główna: <https://qcad.org/en/qcad-command-line-tools#dwg2dwg>
-   licencja: komercyjna.
-   opcjonalny, używany do włączania importu i eksportu plików DWG.

QCAD to dobrze znana platforma CAD 2D oparta na formacie DXF. Oferuje również płatną wersję pro, która jest w zasadzie wersją open-source plus wsparcie dla formatu DWG. Kupując wersję pro, QCAD zawiera również narzędzie do konwersji DWG na DXF, które może być używane przez FreeCAD.



#### Instalacja 

Jeśli narzędzie nie zostanie znalezione automatycznie przez FreeCAD po instalacji *({{Version/pl|0.21}})*, należy ręcznie ustawić ścieżkę do pliku bash *(Linux i macOS)* lub pliku wsadowego *(Windows)*. Więcej informacji na ten temat można znaleźć na stronie [Ustawienia Importu i Eksportu](Import_Export_Preferences/pl#DWG.md).



### Środowisko pracy CADExchanger 

Instalacja środowiska CADExchanger umożliwia pracę z plikami DWG poprzez integrację z płatnym komercyjnym produktem do konwersji plików [CADExchanger](https://cadexchanger.com/). Wystarczy postępować zgodnie z instrukcjami zawartymi w repozytorium [GitHub](https://github.com/yorikvanhavre/CADExchanger). Możesz omówić to środowisko pracy na [jego wątku na forum](https://forum.freecadweb.org/viewtopic.php?f=9&t=22227&p=462421).

W chwili obecnej CADExchanger jest jedynym programem, który pozwala na pracę z plikami 3D DWG, konwertując je do innych formatów 3D.



## Jakie są alternatywy? 

### DoubleCAD XT 

Dostępny jest również DoubleCAD XT *(https://www.turbocad.com/content/doublecad-xt-v5)*. Program jest darmowy do użytku osobistego i komercyjnego. Wymaga bezpłatnej rejestracji w celu otrzymania kodu aktywacyjnego pocztą elektroniczną. Ten program jest przeznaczony tylko dla systemu Windows. Uwaga: wydaje się, że nie był aktualizowany od lat.

### NanoCAD 5.0 

Dostępny jest również nanoCAD 5.0 *(https://nanocad.com/products/nanoCAD/download/)*. Program jest darmowy do użytku osobistego i komercyjnego. Wymaga bezpłatnej rejestracji w celu otrzymania kodu aktywacyjnego pocztą elektroniczną. Ten program jest przeznaczony tylko dla systemu Windows.



### Eksportuj pliki AutoCAD w przyjaznym formacie 

Eksportowanie plików AutoCAD w formacie bardziej przyjaznym dla FreeCAD, takim jak DXF R12 lub R14, SVG i IGES, jeśli wersja go obsługuje. Wszystkie są lepszą alternatywą dla formatu DWG podczas korzystania z FreeCAD.

Ważne jest, aby pamiętać, że nie ma różnicy między zawartością pliku zapisanego w formacie DWG lub DXF, pod warunkiem, że jest to ta sama wersja *(np. DWG 2014 vs. DXF 2014)*. Oba formaty są utrzymywane przez Autodesk i obsługują dokładnie te same funkcje. Różnica polega na tym, że DWG jest zamknięty *(kodowany maszynowo)*, podczas gdy DXF jest otwarty.



## Co mogę zrobić, aby pomóc? 



### Promowanie alternatywnych formatów 

Mówiąc najprościej, przestań akceptować pracę wykonaną w formacie DWG. W praktyce często łatwiej to powiedzieć niż zrobić. Mimo to nie byłoby złą praktyką dla użytkowników i zwolenników FreeCAD unikanie i odrzucanie formatu DWG, gdy tylko jest to możliwe.



### Korzystaj z biblioteki LibreDWG i zgłaszaj błędy 

W wersji rozwojowej, jak wspomniano powyżej, można przełączyć się z własnościowego konwertera ODA na darmową bibliotekę LibreDWG dla plików DWG *(i DXF)*. Prosimy o zrobienie tego i zgłaszanie wszelkich napotkanych problemów.



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Common Questions](Category_Common%20Questions.md) > [Draft](Category_Draft.md) > FreeCAD and DWG Import/pl
