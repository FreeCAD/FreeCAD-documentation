# Source documentation/pl
## Przegląd

Kod źródłowy FreeCAD jest komentowany, aby umożliwić automatyczne generowanie dokumentacji programistycznej przy użyciu narzędzia [Doxygen](Doxygen/pl.md), popularnego systemu dokumentacji kodu źródłowego. Doxygen może udokumentować zarówno C++ jak i Python będącego nieodzowną częścią FreeCAD, czego wynikiem są strony HTML z hiperłączami do każdej udokumentowanej funkcji i klasy.

Dokumentacja jest przechowywana online na stronie [FreeCAD API](https://freecad.github.io/SourceDoc/). Proszę zauważyć, że ta dokumentacja może nie zawsze być aktualna. Jeśli potrzebujesz więcej szczegółów, pobierz najnowszy kod źródłowy FreeCAD i skompiluj dokumentację samodzielnie. Jeśli masz pilne pytania dotyczące kodu, zapytaj w sekcji dla deweloperów na [forum FreeCAD](https://forum.freecadweb.org/index.php).

Kompilacja dokumentacji API przebiega tak samo jak kompilacja pliku wykonywalnego programu FreeCAD, jak wskazano na stronie [Kompilacja w Linux OS](Compile_on_Linux/pl.md).

<img alt="" src=images/FreeCAD_documentation_compilation_workflow.svg  style="width:800px;">



*Ogólny przepływ pracy w celu skompilowania dokumentacji programistycznej programu FreeCAD. W systemie muszą znajdować się pakiety Doxygen i Graphviz, a także sam kod źródłowy FreeCAD. CMake konfiguruje system tak, aby za pomocą jednej instrukcji make dokumentacja całego projektu została skompilowana do wielu plików HTML z diagramami.*



## Zbuduj dokumentację źródłową 



### Pełna dokumentacja 

Jeśli masz zainstalowany Doxygen, bardzo łatwo jest zbudować dokumentację. Zainstaluj również [Graphviz](https://www.graphviz.org/), aby móc tworzyć diagramy pokazujące zależności pomiędzy różnymi klasami i bibliotekami w kodzie FreeCAD. Graphviz jest również używany przez [wykres zależności](Std_DependencyGraph/pl.md) programu FreeCAD do pokazywania zależności pomiędzy różnymi obiektami. 
```python
sudo apt install doxygen graphviz
```

Następnie wykonaj te same kroki, które wykonałbyś, aby skompilować FreeCAD, jak opisano na stronie [kompilacja dla Linux](Compile_on_Linux/pl.md) i podsumowano tutaj dla wygody.

-   Pobierz kod źródłowy FreeCAD i umieść go we własnym katalogu `freecad-source`.
-   Utwórz kolejny katalog `freecad-build`, w którym skompilujesz FreeCAD i jego dokumentację.
-   Skonfiguruj źródła za pomocą `cmake`, upewniając się, że wskazujesz katalog źródłowy i określasz wymagane opcje kompilacji.
-   Wyzwól tworzenie dokumentacji za pomocą `make`.


```python
git clone https://github.com/FreeCAD/FreeCAD.git freecad-source
mkdir freecad-build
cd freecad-build
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ../freecad-source
```

Gdy znajdujesz się w katalogu kompilacji, wydaj następującą instrukcję, aby utworzyć tylko dokumentację. 
```python
make -j$(nproc --ignore=2) DevDoc
``` Jak wspomniano na stronie [Kompilacja (przyspieszamy)](Compiling_(Speeding_up)/pl.md), opcja `-j` ustawia liczbę rdzeni procesora używanych do kompilacji. Wynikowe pliki dokumentacji pojawią się w katalogu 
```python
freecad-build/doc/SourceDocu/html/
```

Punktem startowym dokumentacji jest plik `index.html`, który można otworzyć za pomocą przeglądarki internetowej: 
```python
xdg-open freecad-build/doc/SourceDocu/html/index.html
```


`DevDoc`

wygeneruje znaczną ilość danych, około 5 GB nowych plików, w szczególności ze względu na diagramy utworzone przez Graphviz.



### Zredukowana dokumentacja 

Kompletna dokumentacja zajmuje około 3 GB miejsca na dysku. Alternatywna, mniejsza wersja dokumentacji, która zajmuje tylko około 600 MB, może być wygenerowana dla innych celów. Jest to wersja wyświetlana na stronie [FreeCAD API](https://freecad.github.io/SourceDoc/). 
```python
make -j$(nproc --ignore=2) WebDoc
```

Dokumentacja na stronie [FreeCAD API](https://freecad.github.io/SourceDoc/) jest tworzona automatycznie z <https://github.com/FreeCAD/SourceDoc> . Każdy może ją przebudować i przesłać żądanie ściągnięcia *(pull request)*:

-   wykonaj Fork repozytorium dla <https://github.com/FreeCAD/SourceDoc>
-   na swoim komputerze: sklonuj kod FreeCAD (jeśli jeszcze tego nie zrobiłeś), utwórz katalog kompilacji dla dokumentu i sklonuj w nim powyższe repozytorium SourceDoc. Ten SourceDoc zostanie zaktualizowany po przebudowaniu dokumentu, a następnie będziesz mógł zatwierdzić i wypchnąć wyniki:


```python
git clone https://github.com/FreeCAD/FreeCAD
cd FreeCAD
mkdir build
cd build
mkdir -p doc/SourceDocu/html
cd doc/SourceDocu/html
git clone your-fork-url
cd ../../..
cmake -DBUILD_QT5=ON -DPYTHON_EXECUTABLE=/usr/bin/python3 ..
make WebDoc
cd doc/SourceDocu/html
git commit
git push
```

-   Przejdź do swojego forka online i utwórz żądanie ściągnięcia.

## Inne wersje 

[FreeCAD 0.19 development](https://iesensor.com/FreeCADDoc/0.19/) dokumentacja stworzona przez [qingfeng.xia](http://forum.freecadweb.org/viewtopic.php?t=12613).



## Integracja dokumentacji Coin3D 

W systemach Unix możliwe jest połączenie dokumentacji źródłowej Coin3D z dokumentacją FreeCAD. Pozwala to na łatwiejszą nawigację i kompletne diagramy dziedziczenia dla klas pochodnych Coin.

-   Zainstaluj pakiet `libcoin-doc`, `libcoin80-doc` lub pakiet o podobnej nazwie.
-   Rozpakuj archiwum `coin.tar.gz` znajdujące się w `/usr/share/doc/libcoin-doc/html`, pliki mogą być już rozpakowane w twoim systemie.
-   Wygeneruj ponownie dokumentację źródłową.

Jeśli nie zainstalujesz pakietu dokumentacji dla Coin, zostaną wygenerowane linki umożliwiające dostęp do dokumentacji online na stronie [BitBucket](https://coin3d.bitbucket.io/Coin/). Stanie się tak, jeśli plik znacznika Doxygen można pobrać w czasie konfiguracji za pomocą `wget`.



## Wykorzystanie Doxygen 

Zobacz stronę [Doxygen](Doxygen/pl.md), aby uzyskać obszerne wyjaśnienie, jak komentować kod źródłowy C++ i Python, aby mógł być przetwarzany przez Doxygen w celu automatycznego tworzenia dokumentacji.

Zasadniczo, blok komentarza, zaczynający się od `/**` lub `///` dla C++, lub `##` dla Pythona, musi pojawić się przed każdą definicją klasy lub funkcji, tak aby został wychwycony przez Doxygen. Wiele [specjalnych poleceń](Doxygen/pl#Znaczniki_Doxygen.md), które zaczynają się od `\` lub `@`, może być użytych do zdefiniowania części kodu i sformatowania wyjścia. [Składnia Markdown](Doxygen/pl#Obsługa_znaczników_Markdown.md) jest również rozumiana w bloku komentarza, co sprawia, że wygodnie jest podkreślić pewne części dokumentacji. 
```python
/**
 * Returns the name of the workbench object.
 */
std::string name() const;

/**
 * Set the name to the workbench object.
 */
void setName(const std::string&);

/// remove the added TaskWatcher
void removeTaskWatcher(void);
```



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Source documentation/pl
