# Compile on MacOS/pl
**Istnieje eksperymentalny kontener FreeCAD Docker, który jest testowany pod kątem rozwoju FreeCAD. Przeczytaj więcej na ten temat na stronie [Kompilacja w Docker](Compile_on_Docker/pl.md)**






## Informacje ogólne 

Ta strona opisuje, jak kompilować kod źródłowy FreeCAD na macOS. Aby zapoznać się z kompilacją na innych platformach, zobacz [Kompilacja](Compiling/pl.md).

Te instrukcje były testowane na macOS Catalina ze standardowym Xcode 11.6. Ich działanie jest też potwierdzone na macOS Big Sur Beta z Xcode 12.0 beta. Jeśli planujesz używać wersji beta Xcode, upewnij się, że pobrałeś dodatek Command Line Tools przez pakiet dmg, aby obejść problemy z zależnościami libz.

Ta strona służy jako szybki przewodnik i nie jest przeznaczona do szczegółowego opisywania wszystkich dostępnych opcji kompilacji.

Jeśli chcesz tylko przetestować najnowszą wersję przed-wydaniową FreeCAD, możesz pobrać gotowe pliki wykonywalne [stąd](https://github.com/FreeCAD/FreeCAD/releases).



## Instalacja wymaganego oprogramowania 

Następujące oprogramowanie musi być zainstalowane aby umożliwić kompilację.

### Homebrew Package Manager 

Homebrew to menedżer pakietów oparty na wierszu poleceń dla macOS. [Strona główna Homebrew](https://brew.sh/) zawiera polecenie instalacyjne, które wystarczy wkleić do okna terminala.



### CMake

CMake to narzędzie do kompilacji, które generuje konfigurację kompilacji na podstawie określonych przez Ciebie zmiennych. Następnie wydajesz polecenie \make\, aby rzeczywiście zbudować tę konfigurację. Wersja wiersza poleceń CMake jest automatycznie instalowana jako część instalacji Homebrew powyżej. Jeśli wolisz używać wersji graficznej CMake, możesz pobrać ją [stąd](https://www.cmake.org/downloadDownload).



## Instalacja zależności 

FreeCAD utrzymuje \'cask\' Homebrew, który instaluje wymagane formuły i zależności. Wykonaj poniższe polecenia \brew\ w terminalu.


```python
brew tap freecad/freecad
brew install eigen
brew install --only-dependencies freecad
```


{{Incode|brew install}}

może potrwać dość długo, więc warto przygotować sobie napój. :-).

Alternatywnie możesz ręcznie zainstalować poszczególne zależności, instalując następujące pakiety za pomocą {{Incode|brew install ...}}:

-    `cmake`
    

-    `swig`
    

-    `boost`
    

-    `boost-python3`
    

-    `eigen`
    

-    `gts`
    

-    `vtk`
    

-    `xerces-c`
    

-    `qt@5`\- Obecnie obsługiwany jest tylko Qt5, wsparcie dla Qt6 jest w trakcie opracowywania

-    `opencascade`
    

-    `doxygen`
    

-    `pkgconfig`
    

-    `coin3d`\- Zauważ, że w momencie pisania (listopad 2022) ta wersja zainstaluje nieużywalną wersję pyside@2 jako zależność

Istnieje kilka pakietów, które są dostępne tylko po dodaniu tapu freecad cask: musisz to zrobić (`brew tap freecad/freecad`). Z powodu niektórych historycznych obejść błędów, w momencie pisania (listopad 2022) wersje PySide2 i Shiboken2 zainstalowane przez Homebrew są nieużywalne, ponieważ wymuszają użycie Py_Limited_API, którego FreeCAD nie obsługuje. Oczekuje się, że to obejście zostanie usunięte w nadchodzących miesiącach, ale w międzyczasie musisz używać wersji PySide i Shiboken z tapu FreeCAD. Użyj `brew install ...`, aby zainstalować następujące pakiety:

-    `freecad/freecad/pyside2@5.15.5`
    

-    `freecad/freecad/shiboken2@5.15.5`
    

-    `freecad/freecad/med-file`
    

-    `freecad/freecad/netgen`
    

Będziesz także musiał połączyć PySide i Shiboken:


```python
brew link freecad/freecad/pyside2@5.15.5 freecad/freecad/shiboken2@5.15.5
```

W niektórych przypadkach pakiety zainstalowane przez Homebrew mogą korzystać z różnych wersji Pythona: na przykład, w momencie pisania tego tekstu PySide2 używa Pythona 3.10, podczas gdy boost-python3 używa Pythona 3.11. Możliwe jest „cofnięcie" bardziej zaawansowanej wersji (aby boost-python3 używał Pythona 3.10), ale jest to zaawansowana operacja i w wielu przypadkach lepiej poczekać na aktualizację drugiego pakietu. Jeśli chcesz mimo wszystko spróbować tego rozwiązania, zapoznaj się z poleceniem \"brew extract\", które możesz wykorzystać do wyodrębnienia formuły do nowego casku (zazwyczaj freecad/freecad). Następnie możesz edytować tę formułę w razie potrzeby.

Będziesz musiał ustawić ścieżkę do Qt: obecnie wspierany jest Qt5, natomiast wsparcie dla Qt6 jest w trakcie prac. Ustaw \FREECAD_QT_VERSION\ na \"Auto\" lub \"5\", aby wybrać Qt5 (domyślnie). W wierszu poleceń użyj czegoś takiego jak:


```python
cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DQt5_DIR="/usr/local/Cellar/qt@5/5.15.7/lib/cmake/Qt5" \
  -DPySide2_DIR="/usr/local/Cellar/pyside2@5.15.5/5.15.5/lib/cmake/PySide2-5.15.5" \
  -DShiboken2_DIR="/usr/local/Cellar/shiboken2@5.15.5/5.15.5_1/lib/cmake/Shiboken2-5.15.5" \
  ../freecad-source
```



## Pobieranie kodu źródłowego 

W poniższych instrukcjach foldery źródłowy i kompilacji są tworzone obok siebie w folderze:


```python
/Users/username/FreeCAD
```

ale możesz użyć dowolnych folderów.


```python
mkdir ~/FreeCAD
cd ~/FreeCAD
```

Poniższe polecenie sklonuje repozytorium git FreeCAD do katalogu o nazwie FreeCAD-git.


```python
git clone --recurse-submodules https://github.com/FreeCAD/FreeCAD FreeCAD-git
```

Utwórz folder kompilacji.


```python
mkdir ~/FreeCAD/build
```



## Uruchom CMake 

Następnie uruchomimy CMake, aby wygenerować konfigurację budowy. Należy przekazać kilka opcji do CMake. Poniższa tabela opisuje opcje i dostarcza kilka informacji na ich temat.



### Opcje CMake 

  Nazwa               Wartość                                  Uwagi
    
  CMAKE_BUILD_TYPE    Release (STRING)                         Release lub Debug. Debug jest zazwyczaj używany do testowania na poziomie dewelopera, ale może być również wymagany do testowania i rozwiązywania problemów na poziomie użytkownika.
  CMAKE_PREFIX_PATH   \"/usr/local/opt/qt5152;\" \... (PATH)   Wymagane do budowy z Qt5. Zobacz uwagi poniżej. Należy również dodać ścieżkę do bibliotek VTK i pliku konfiguracyjnego cmake dla bibliotek NGLIB.

\|- \| FREECAD_CREATE_MAC_APP \|\| 1 (BOOL) \|\| Utwórz pakiet FreeCAD.app w lokalizacji określonej w CMAKE_INSTALL_PREFIX, gdy wydane zostanie polecenie \'make install\'. \|- \| CMAKE_INSTALL_PREFIX \|\| \"./..\" (PATH) \|\| Ścieżka, w której chcesz wygenerować pakiet FreeCAD.app. \|- \| FREECAD_USE_EXTERNAL_KDL \|\| 1 (BOOL) \|\| Wymagane. \|- \| BUILD_FEM_NETGEN \|\| 1 (BOOL) \|\| Wymagane, jeśli wybierasz kompilację narzędzi MES. \|}

Uwaga: Polecenie do wygenerowania CMAKE_PREFIX_PATH:

ls -d $(brew list -1 | grep qt | tail -1 | xargs brew --cellar)/*/lib/cmake



### GUI CMake 

Otwórz aplikację CMake i wypełnij pola dla folderu źródłowego i folderu kompilacji. W tym przykładzie będzie to **/Users/username/FreeCAD/FreeCAD-git** jako folder źródłowy i **/Users/username/FreeCAD/build** jako folder kompilacji.

Następnie kliknij przycisk **Configure**, aby wypełnić listę opcji konfiguracyjnych. Pojawi się okno dialogowe, w którym musisz określić, jaki generator ma być użyty. Pozostaw domyślną opcję **Unix Makefiles**. Konfiguracja nie powiedzie się za pierwszym razem, ponieważ niektóre opcje będą musiały zostać zmienione. Uwaga: Będziesz musiał zaznaczyć pole **Advanced**, aby zobaczyć wszystkie opcje.

Ustaw opcje zgodnie z tabelą powyżej, a następnie kliknij **Configure** ponownie, a potem **Generate**.



### Linia poleceń CMake 

Wprowadź poniższe w terminalu.


```python
export PREFIX_PATH="/usr/local/opt/qt5152;\
/usr/local/Cellar/nglib/v6.2.2007/Contents/Resources;\
/usr/local/Cellar/vtk@8.2/8.2.0_1/lib/cmake;"
```


```python
$cd ~/FreeCAD/build
$cmake \
  -DCMAKE_BUILD_TYPE="Release"   \
  -DBUILD_QT5=1                  \
  -DWITH_PYTHON3=1               \
  -DCMAKE_PREFIX_PATH="$PREFIX_PATH" \
  -DPYTHON_EXECUTABLE="/usr/local/bin/python3" \
  -DFREECAD_USE_EXTERNAL_KDL=1   \
  -DCMAKE_CXX_FLAGS='-std=c++14' \
  -DBUILD_FEM_NETGEN=1           \
  -DFREECAD_CREATE_MAC_APP=1     \
  -DCMAKE_INSTALL_PREFIX="./.."  \
  ../FreeCAD-git/

```



## Uruchom make 

Na koniec uruchom polecenie **make** w terminalu, aby skompilować i połączyć FreeCAD oraz wygenerować pakiet aplikacji.


```python
cd ~/FreeCAD/build
make -j5 install
```

Opcja -j określa, ile procesów make ma działać jednocześnie. Jedna więcej niż liczba rdzeni CPU jest zazwyczaj dobrym wyborem. Jednakże, jeśli kompilacja zakończy się niepowodzeniem, warto uruchomić make bez opcji -j, aby zobaczyć dokładnie, gdzie wystąpił błąd.

Zobacz też [Kompilacja (przyspieszamy)](Compiling_(Speeding_up)/pl.md)

Jeśli make zakończy się bez błędów, możesz teraz uruchomić FreeCAD, klikając dwukrotnie na plik wykonywalny w Finderze.



## Aktualizowanie z Github 

Rozwój FreeCAD postępuje szybko; codziennie pojawiają się poprawki błędów lub nowe funkcje. Aby uzyskać najnowsze zmiany, użyj gita, aby zaktualizować katalog źródłowy (zobacz [Zarządzanie kodem źródłowym](Source_code_management/pl.md)), a następnie ponownie uruchom kroki CMake i make opisane powyżej. Zazwyczaj nie ma potrzeby zaczynania od pustego katalogu build, a kolejne kompilacje będą zazwyczaj znacznie szybsze niż pierwsza.



## Kompilacja z Qt4 i Python 2.7 

FreeCAD przeszedł z Qt 4 do Qt 5 oraz do używania homebrew. Qt 4 nie jest już dostępne jako opcja dla nowych kompilacji na macOS po przejściu na Qt 5. Python 2.7 został wycofany w homebrew oraz nadchodzących wersjach macOS i również nie jest już wspierany w budowie FreeCAD na macOS.



## Rozwiązywanie problemów 



### Segfault przy uruchamianiu Qt5 

Jeśli Qt4 był wcześniej zainstalowany za pomocą brew, a następnie budujesz przy użyciu Qt5, możesz napotkać wyjątek EXC_BAD_ACCESS (SEGSEGV) podczas uruchamiania nowej kompilacji Qt5. Naprawą tego problemu jest ręczne odinstalowanie Qt4.


```python
brew uninstall --ignore-dependencies --force cartr/qt4/shiboken@1.2 cartr/qt4/pyside@1.2 cartr/qt4/pyside-tools@1.2 cartr/qt4/qt-legacy-formula
```

### Fortran

*\"No CMAKE_Fortran_COMPILER could be found.\"* podczas konfiguracji - Starsze wersje FreeCAD mogą wymagać zainstalowanego kompilatora Fortran. W przypadku Homebrew użyj polecenia \"brew install gcc\" i spróbuj ponownie skonfigurować, podając cmake ścieżkę do Fortrana, np. -DCMAKE_Fortran_COMPILER=/opt/local/bin/gfortran-mp-4.9. Lub, najlepiej, użyj nowszej wersji kodu źródłowego programu FreeCAD!

### FreeType

W przypadku używania wersji CMake starszych niż 3.1.0, konieczne jest ręczne ustawienie zmiennej CMake FREETYPE_INCLUDE_DIR_freetype2, np. /usr/local/include/freetype2.



### Dodatkowe instrukcje kompilacji 

FreeCAD można skompilować z najnowszego kodu źródłowego dostępnego na GitHubie, a następnie uruchomić z wiersza poleceń, korzystając z bibliotek dostarczanych przez homebrew-freeCAD tap. Pełną listę instrukcji dotyczących kompilacji można znaleźć [tutaj](https://github.com/ipatch/homebrew-us-05/tree/dev/freecad#building-freecad-for-macos-by-macos).



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compile on MacOS/pl
