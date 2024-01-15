# Conda/pl
## Wprowadzenie




Ta strona ma na celu przedstawienie Conda jako menedżera pakietów, zależności i środowiska dla FreeCAD.

Obecnie ta strona głównie kataloguje linki do odpowiednich dyskusji na forum FreeCAD i innych miejsc w sieci, ale mamy nadzieję, że uda nam się udokumentować najważniejsze punkty z tych linków na tej stronie.

Zobacz także [samouczek wideo](https://www.youtube.com/watch?v=sCs8xlrw2nM) dotyczący zawartości tej strony.



## Motywacja

Motywacja do korzystania z Conda jest wieloraka, podobnie jak cel Conda.

Rozłóżmy to na czynniki pierwsze.



### Conda jako menedżer pakietów 

Po pierwsze, Conda jest menedżerem pakietów - podobnym do apt lub pip.

Oznacza to, że możemy zainstalować **pakiety** za pomocą prostego conda install z różnych \[<https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels>. kanałów\], takich jak [conda-forge](https://conda-forge.org/).

Conda Forge jest analogiczna do [Python Package Index (PyPI)](https://pypi.org/), kanału społecznościowego złożonego z tysięcy współtwórców, i obsługuje [freecad](https://anaconda.org/conda-forge/freecad) jako pakiet conda.



### Conda jako menedżer zależności 

Następnie, Conda jest menedżerem zależności - podobnym do apt lub pip.

Conda może zarządzać zależnościami i instalować zależności dla projektu takiego jak FreeCAD.

Dlaczego po prostu nie użyć pip? pip działa naprawdę dobrze do zarządzania zależnościami projektów, które „tylko" korzystają z Pythona.

Conda działa w wielu językach i dlatego lepiej nadaje się do zarządzania zależnościami projektów takich jak FreeCAD, które mają zależności w różnych językach, takich jak C / C++ i Python.



### Conda jako menedżer środowiska 

Conda ma koncepcję [środowiska](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html), które jest unikalną kombinacją pakietów i wersji potrzebnych do uruchomienia oprogramowania. Na przykład środowisko pracy FreeCAD.

Dzięki środowiskom można je łatwo \"aktywować\" i \"dezaktywować\" lub przełączać się między wersjami pakietów potrzebnych do poszczególnych elementów oprogramowania.

Jest to przydatne do testowania zachowania środowiska pracy z określonym zestawem pakietów. Na przykład, jak środowisko pracy zachowuje się w FreeCAD v18.4 w porównaniu do v19?

Środowiska Conda umożliwiają odtworzenie dokładnie tego samego \"otoczenia\" na różnych maszynach.

Na przykład wiele lokalnych maszyn deweloperskich lub zdalny serwer kompilacji hostowany przez Travis CI.



## Instalacja środowiska Conda 

1\. [Instalacja Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2\. Sprawdź, czy instalacja przebiegła pomyślnie i zapoznaj się z **CLI** dla 

## Instalacja FreeCAD przy użyciu Conda 

Najpierw musisz zdecydować, czy chcesz zainstalować *stabilną* wersję FreeCAD, czy eksperymentować z najnowszym *niestabilnym* kodem z FreeCAD master.

Stabilne, wydane wersje FreeCAD są dostępne na kanale conda-forge, natomiast najnowsze master FreeCAD są dostępne na kanale freecad/label/dev.

  kanał Conda           Stabilne?
   
  conda-forge         Yes ✔️
  freecad/label/dev   No ❌

Po drugie, ponieważ można łatwo tworzyć dedykowane środowiska w conda, zaleca się utworzenie jednego dla FreeCAD.

Komenda create umożliwia utworzenie środowiska z listy określonych pakietów. W naszym przypadku chcemy utworzyć środowisko o nazwie „fcenv" *(skrót od środowisko FreeCAD)* z pakietu freecad i powiedzieć Condzie, aby wyszukała pakiet freecad za pomocą metody kanał conda-forge. 
```python
conda create --name fcenv --channel conda-forge freecad
``` **Wskazówka:** Alternatywnie możesz powiedzieć conda, aby zawsze wyszukiwała conda-forge podczas instalowania pakietów za pomocą następującego polecenia: 
```python
conda config --add channels conda-forge
``` Cotygodniowe kompilacje można zainstalować z kanału freecad/label/dev w następujący sposób: 
```python
conda create --name fcenv-dev --channel freecad/label/dev freecad
```

## Dyskusja na forum FreeCAD 

-   [Porozmawiajmy o Conda](https://forum.freecadweb.org/viewtopic.php?t=39656)
-   [Rozwiązanie do pakowania: (ana)conda](https://forum.freecadweb.org/viewtopic.php?f=10&t=15197)
-   [Dystrybucja FreeCAD Conda](https://forum.freecadweb.org/viewtopic.php?f=8&t=45582)



## Zobacz również 

-   <https://docs.conda.io/en/latest/>
-   <https://conda-forge.org/docs/>
-   <https://docs.conda.io/projects/conda-build/en/latest/>
-   <https://anaconda.org/conda-forge/freecad>
-   <https://anaconda.org/freecad/freecad>
-   <https://github.com/FreeCAD/FreeCAD_Conda>
-   <https://github.com/FreeCAD/FreeCAD-AppImage>



---
⏵ [documentation index](../README.md) > [Developer_Documentation](Category_Developer_Documentation.md) > [Developer](Category_Developer.md) > Conda/pl
