# CompileOnWindows - Reducing Disk Footprint/pl
Oto techniki zmniejszania przestrzeni dyskowej wymaganej do budowania FreeCAD w systemie Windows. Poradnik ten może być przydatny dla tych, którzy mają ograniczoną przestrzeń dyskową *(na przykład z powodu dysku SSD)* oraz dla tych, którzy chcą uniknąć instalowania pełnego Visual Studio.

Zaleca się, aby przed podjęciem tej próby poznać w praktyce sposób [kompilacji w Windows](Compile_on_Windows/pl.md) z Qt Creator.



## Ustawianie kompilatora MSVC2013 bez instalowania Visual Studio 

Wymagania:

-   inny komputer, na którym jest / może być zainstalowane kompletne Visual Studio *(teoretycznie można to osiągnąć rozpakowując instalatory VS, ale nie ma tutaj wskazówek na ten temat)*.



### Pobieranie kompilatora 

0\. Aby uzyskać pliki kompilatora, należy przejść do innego komputera i zlokalizować rzeczywisty kompilator. Przykładowa ścieżka do kompilatora: drive:\\path\\to\\visual\\studio\\VC\\bin.

1\. Skopiuj pliki binarne kompilatora i standardowe biblioteki na inny komputer. To znaczy, skopiuj następujące foldery do C:\\Qt\\msvc12rip:

-   drive:\\path\\to\\visual\\studio\\VC\\*bin*
-   drive:\\path\\to\\visual\\studio\\VC\\*lib*
-   drive:\\path\\to\\visual\\studio\\VC\\*include*

2\. Zainstaluj [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/). Dla tych, którzy nie wiedzą, jest to zestaw nagłówków, bibliotek i narzędzi do kompilacji programów Windows. Zwróć uwagę, gdzie jest zainstalowany. Przykładowa ścieżka: C:\\Program Files (x86)\\Windows Kits\\8.1

3\. Zainstaluj CMake i Qt Creator *(tylko kreator, tj. środowisko, a nie rzeczywiste Qt, aby zaoszczędzić miejsce)*.

4\. Skonfiguruj niestandardowy kompilator w Qt Creator. Czytaj dalej, aby dowiedzieć się jak to zrobić.



### Kompilator w Qt Creator 

#### 32-bit

Ustawienie kompilatora na wersję 32-bitową jest dość proste.

4.1. Skonfiguruj kompilator w zakładce Kompilatory w ustawieniach: Dodaj **niestandardowy** kompilator:

-   Nazwa = msvcrip *(nazwa nie ma znaczenia, zależy od Ciebie)*,
-   Ścieżka kompilatora: C:\\Qt\\msvc12rip\\VC\\bin\\cl.exe
-   Ścieżka Make: C:\\Qt\\msvc12rip\\VC\\bin\\nmake.exe
-   ABI: x86-windows-msvc2013-pe-32bit
-   Ścieżki nagłówków - nic,
-   Parser błędów: MSVC.

![600px](images/Msvc-no-vs_compiler-setup-32.png)

4.2. W zakładce zestawy dodałem zestaw i skonfigurowałem go w następujący sposób:

-   Nazwa: FreeCAD32 *(znów do wyboru)*,
-   Typ urządzenia: Desktop,
-   Urządzenie: Lokalny PC,
-   Kompilator: msvcrip *(lub jakkolwiek go nazwałeś w kroku 1)*,
-   Środowisko: *(popraw ścieżki do swojej konfiguracji)*.


{{code|code=
INCLUDE=C:\Program Files (x86)\Windows Kits\8.1\Include\um\;C:\Qt\msvc12rip\VC\include\
LIB=C:\Qt\msvc12rip\VC\lib\;C:\Program Files (x86)\Windows Kits\8.1\Lib\winv6.3\um\x86\
LIBPATH=C:\Qt\msvc12rip\VC\lib\;C:\Program Files (x86)\Windows Kits\8.1\Lib\winv6.3\um\x86\
PATH=C:\Qt\msvc12rip\VC\bin\;C:\Program Files (x86)\Windows Kits\8.1\bin\x86\;C:\Qt\git\bin\}}

Zwróć uwagę na ścieżkę do git.exe w PATH. Jest to opcjonalne, ale jeśli nie zostanie określone, informacje o wersji będą niekompletne w \"O programie\" FreeCAD.

-   Debugger: *(opcjonalnie)* ustawiony na 32-bitowy (x86),
-   Wersja Qt: Brak.

![600px](images/Msvc-no-vs_kit-setup-32.png)

Najwięcej problemów sprawiła mi konfiguracja części środowiskowej ustawień.

#### 64-bit 

Jest to nieco bardziej skomplikowane niż w przypadku kompilatora 32-bitowego. Głównym problemem było to, że nie ma pliku wykonywalnego nmake w C:\\Qt\\msvc12rip\\VC\\bin\\*x86_amd64*, a nmake ciągle używa 32-bitowego kompilatora. Aby przeciwdziałać temu problemowi, należy utworzyć specjalny folder \"C:\\Qt\\msvc12rip\\VC\\bin\\*x86_amd64_sa*\", w którym połączone są mnake i 64-bitowy cl. Czytaj dalej, aby uzyskać instrukcje krok po kroku.

4.1. w C:\\Qt\\msvc12rip\\VC\\bin, utwórz folder o nazwie **x86_amd64_sa** *(sa oznacza Stand-Alone, użyj dowolnej nazwy)*.

4.2. skopiuj zawartość folderu C:\\Qt\\msvc12rip\\VC\\bin do folderu x86_amd64_sa *(teraz masz tam 32-bitowy kompilator)*.

4.3. Skopiuj zawartość folderu x86_amd64 do x86_amd64_sa, zastępując przy tym pliki. Teraz masz 64-bitowy kompilator z nmake.

4.4. Skonfiguruj kompilator w zakładce Kompilatory w ustawieniach: Dodaj **niestandardowy** kompilator:

-   Nazwa = msvcrip*\'64* *(nazwa nie ma znaczenia, zależy od Ciebie)*,
-   Ścieżka kompilatora: C:\\Qt\\msvc12rip\\VC\\bin\\x86_amd64_sa\\cl.exe
-   Ścieżka Make: C:\\Qt\\msvc12rip\\VC\\bin\\x86_amd64_sa\\nmake.exe
-   ABI: x86-windows-msvc2013-pe-**64bit**,
-   Ścieżki nagłówka - nic,
-   Parser błędów: MSVC.

4.5. W zakładce zestawy dodaj zestaw i skonfiguruj go w następujący sposób:

-   Nazwa: FreeCAD*\'64* *(ponownie, zależy od Ciebie)*,
-   Typ urządzenia: Desktop,
-   Urządzenie: Lokalny PC,
-   Kompilator: msvcrip*\'64* *(lub jakkolwiek go nazwałeś w kroku 4.4)*,
-   Środowisko: *(popraw ścieżki do swojej konfiguracji)* *(w porównaniu do 32-bitowego, amd64/x64 pojawiło się lub zastąpiło x86 w kilku miejscach)*.


{{code|code=
INCLUDE=C:\Program Files (x86)\Windows Kits\8.1\include\shared\;C:\Program Files (x86)\Windows Kits\8.1\include\um\;C:\Qt\msvc12rip\VC\include
LIB=C:\Program Files (x86)\Windows Kits\8.1\lib\winv6.3\um\x64\;C:\Qt\msvc12rip\VC\lib\amd64\
LIBPATH=C:\Program Files (x86)\Windows Kits\8.1\References\CommonConfiguration\Neutral\
PATH=C:\Qt\msvc12rip\VC\bin\x86_amd64_sa\;C:\Program Files (x86)\Windows Kits\8.1\bin\x64\;C:\Qt\git\bin\}}

Zwróć uwagę na ścieżkę do git.exe w PATH. Jest to opcjonalne, ale jeśli nie zostanie określone, informacje o wersji będą niekompletne w \"O programie\" FreeCAD.

-   Debugger: *(opcjonalnie)* ustawiony na **64**-bit (x64),
-   Wersja Qt: Brak.

Wskazówka: skonfiguruj inną parę zestaw+kompilator do używania jom zamiast nmake, aby umożliwić kompilację wielordzeniową. Konfiguracja jest identyczna z 64-bitową z nmake, z wyjątkiem tego, że Make w zakładce kompilatora powinien wskazywać na jom.exe. Przykładowa ścieżka do jom: C:\\Qt\\Qt542\\Tools\\QtCreator\\bin\\jom.exe *(powinieneś być w stanie znaleźć jom w lokalizacji, w którym zainstalowany jest twój Qt creator)*.

Cała reszta jest identyczna z normalnym sposobem kompilacji FreeCAD.



### Testowanie kompilatora i kompilacja FreeCAD 

Wymagania:

-   Kod źródłowy FreeCAD *(patrz [Kompilacja w Windows](Compile_on_Windows/pl.md))*.
-   Poprawny libpack, wyodrębniony. *(\"poprawny\" oznacza, że musi pasować do kompilatora i bit-ness)* *(patrz [Kompilacja w Windows](Compile_on_Windows/pl.md))*.

Utuchom FreeCAD (CMakeLists.txt) za pomocą Qt creatora, a on zaprosi Cię do uruchomienia cmake. Uruchom go. **CMake zbuduje program testowy, aby sprawdzić, czy kompilator działa**. Jeśli kompilator nie działa, zostanie wyświetlony błąd informujący o tym i zawierający listę danych wyjściowych kompilacji. Dane wyjściowe kompilacji powinny pomóc zidentyfikować, co idzie nie tak. Oto mała lista typowych błędów:

-   *Can\'t open Kernel32.lib* - coś jest nie tak ze zmiennymi środowiskowymi LIB lub LIBPATH (uwaga: ustawia się je w zakładce kits w Qt, nie w Windowsie!).
-   *Can\'t resolve external symbol* - coś jest nie tak z LIB lub LIBPATH *(prawdopodobnie wskazują na .lib-s o niewłaściwej bitowości)*.
-   *Manifest-related error* - PATH nie wskazuje na lokalizację, w której znajduje się kompilator zasobów (rc.exe) o odpowiedniej bitowości.
-   *Can\'t locate include* - lista lokalizacji include powinna zawierać ścieżkę do standardowych nagłówków *(C:\\Qt\\msvc12rip\\VC\\include na moim komputerze)*.

Aby uruchomić FreeCAD skompilowany z typem \"Debug\", debugowane wersje redystrybucyjnych bibliotek MSVC2013 *(msvcp120d.dll, msvcr120d.dll)* muszą być obecne gdzieś, gdzie można uzyskać dostęp za pośrednictwem PATH *(tym razem w całym systemie*).

Możesz uzyskać te pliki dll z drugiego komputera, na którym znajduje się Visual Studio, z którego pobrałeś kompilator. Alternatywnie, te pliki dll można wyodrębnić bezpośrednio z instalatora Visual Studio, co jest bardzo proste:

-   zamontować pobrany obraz .iso jako dysk (dysk D: w moim systemie)
-   zlokalizować pliki:
    -   D:\\packages\\vc_librarycore86\\cab3.cab/F_REDIST_DLL_APPLOCAL\_**msvcp120d_x64** *(← lub x86, jeśli budujesz 32-bit)*
    -   D:\\packages\\vc_librarycore86\\cab3.cab/F_REDIST_DLL_APPLOCAL\_*msvcr120d_x64*
-   rozpakuj pliki i nazwij je \"msvcp120d.dll\", \"msvcr120d.dll\"
-   skopiuj pliki do folderu libpack, do bin



## Unikanie kopiowania jakichkolwiek plików libpack w celu uruchomienia FreeCAD 

Wymagania:

-   Windows Vista i nowsze.
-   System plików NTFS *(? może nie\...)*.

Idea jest bardzo prosta: zamiast kopiować pliki - utwórz linki. W systemie Windows dostępne są do tego celu dowiązania symboliczne. Dowiązanie sprawia, że linkowany plik wydaje się być tam, gdzie jest dowiązanie, ale plik jest faktycznie przechowywany gdzie indziej. Linki można tworzyć za pomocą polecenia wsadowego **\[<https://technet.microsoft.com/en-us/library/cc753194(v=ws.10>).aspx mklink\]**.

Ponieważ istnieje zbyt wiele plików, aby tworzyć linki ręcznie, należy użyć skryptu wsadowego. Oto przykład takiego skryptu:

links_libpack.bat:


{{code|code=
@set libpackpath=C:\_vt\dev\PC\Qt\FreeCAD\libpack\active
@set builddir=%1
pushd %libpackpath%\bin
for %%i in (*) do mklink "%builddir%\bin\%%i" "%libpackpath%\bin\%%i"
for /D %%s in (*) do mklink /d "%builddir%\bin\%%s" "%libpackpath%\bin\%%s"
popd
pause
}}

Pierwsza pętla for tworzy linki do plików, druga pętla - linki do folderów.
Będziesz musiał zmodyfikować ścieżkę do libpack, aby pasowała do twojej. Używaj ścieżek bezwzględnych. Następnie podaj ścieżkę folderu kompilacji FreeCAD *(pełną ścieżkę!)* do skryptu jako argument.

Ta partia musi być uruchomiona z uprawnieniami administratora *(lub można ustawić zezwolenie użytkownikom na korzystanie z mklink w lokalnych ustawieniach zasad bezpieczeństwa w systemie Windows)*. Partia może się nie powieść, jeśli w ścieżkach znajdują się spacje *(może działać, ale nie zostało to przetestowane)*. Wskazówka: utwórz skrót do pliku links_libpack.bat, skonfiguruj go do uruchamiania jako administrator *(we właściwościach skrótu)* i przeciągnij folder kompilacji na skrót.



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > CompileOnWindows - Reducing Disk Footprint/pl
