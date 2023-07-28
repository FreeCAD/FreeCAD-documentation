# Compiling (Speeding up)/pl
{{TOCright}}



## Informacje ogólne 

FreeCAD jest dużą aplikacją, której całkowita kompilacja ze źródła może zająć od 10 minut do godziny. Zależy to głównie od wydajności Twojego procesora i liczby rdzeni, które są wykorzystywane w procesie kompilacji. Oto kilka wskazówek, jak przyspieszyć ten proces i skrócić czas kompilacji.



## CCache

Zainstaluj `ccache`, aby buforować kompilacje.

[Ccache](https://ccache.dev/) przyspiesza rekompilację poprzez buforowanie poprzednich kompilacji i wykrywanie, kiedy ta sama kompilacja jest wykonywana ponownie. Ccache jest wolnym oprogramowaniem, wydanym na licencji GPLv3 lub nowszej.

W większości systemów ccache zostanie automatycznie wykryty i włączony, można użyć opcji `FREECAD_USE_CCACHE` `cmake` by kontrolować to zachowanie.



## Wyłączanie modułów 

Używając `cmake` do konfiguracji kompilacji, można wyłączyć kompilację niektórych środowisk roboczych, które mogą nie być potrzebne w danej chwili. Jest to przydatne, jeśli chcesz przetestować tylko kilka środowisk roboczych.

Na przykład, aby uniknąć budowy środowisk pracy MES i Siatka:


```python
cmake -DBUILD_FEM=OFF -DBUILD_MESH=OFF ../freecad-source
```

Użyj `cmake-gui`, `cmake-curses-gui` lub `cmake-qt-gui`, aby wyświetlić wszystkie możliwe zmienne, które można edytować w konfiguracji. Za pomocą tych interfejsów można łatwo włączać i wyłączać różne środowiska pracy.



## Liczba zadań wykonywanych równolegle 

Po skonfigurowaniu za pomocą `cmake`, program `make` uruchamia rzeczywisty kompilator C++ do pracy nad plikami kodu źródłowego. Kompilację można przyspieszyć, pracując nad różnymi plikami w tym samym czasie. Można to osiągnąć za pomocą opcji `-j` programu `make`, która określa liczbę \"zadań\" lub poleceń kompilacji uruchamianych jednocześnie. Opcja ta jest liczbą całkowitą.

Uruchomienie równolegle czterech poleceń kompilacji:


```python
make -j4
```

Kompiluje równolegle tyle plików, ile rdzeni procesora w systemie. Jest to przydatne, jeśli masz wiele rdzeni i chcesz użyć ich wszystkich do kompilacji oprogramowania.


{{code|code=
make -j$(nproc)
}}

Kompilowanie tylu plików równolegle, ile rdzeni procesora w systemie, minus dwa. Użyj tego, aby system nadal reagował na wykonywanie innych zadań. Na przykład dwa rdzenie pozwolą ci korzystać z przeglądarki, podczas gdy pozostałe rdzenie będą kompilować oprogramowanie w tle.


{{code|code=
make -j$(nproc --ignore=2)
}}



## distcc

Program `distcc` może być używany do wykonywania rozproszonej kompilacji kodu C i C++ na kilku maszynach w sieci.

[Distcc](https://www.distcc.org/) powinien zawsze generować takie same wyniki jak lokalna kompilacja. Jest darmowy, prosty w instalacji i użyciu, a często dwa lub więcej razy szybszy niż lokalna kompilacja.

Deweloper FreeCAD \"etrombly\" opublikował krótkie wyjaśnienie na stronie \[<https://forum.freecadweb.org/viewtopic.php?f=4&t=50810&p=459142#p458614>, jak zainstalować distcc, aby skompilować FreeCAD w sieci komputerów przy użyciu Dockera\].



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Compiling (Speeding up)/pl
