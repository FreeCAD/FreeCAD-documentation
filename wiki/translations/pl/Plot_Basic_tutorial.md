# Plot Basic tutorial/pl
{{TutorialInfo/pl
|Topic=Poradnik: Podstawy środowiska pracy Wykres
|Level=Początkujący
|Time=
|Author=
|FCVersion=-
|Files=
}}

W tym poradniku dowiemy się, jak wykonać podstawowy wykres przy użyciu środowiska pracy [Wykres](Plot_Workbench/pl.md) i konsoli [Python](Python_console/pl.md).

<img alt="" src=images/Plot_Trigonometric_Example.png  style="width:600px;"> 
*Przykład prostego wykresu*

Na poprzednim obrazku możesz zobaczyć rezultat, jaki w przybliżeniu uzyskamy. Po tym poradniku nauczysz się:

-   Jak utworzyć wykres w konsoli [Python](Python_console/pl.md).
-   Jak wykreślić kilka danych w konsoli [Python](Python_console/pl.md).
-   Jak wyświetlić <img alt="" src=images/Plot_Grid.svg  style="width:24px;"> [linie siatki](Plot_Grid/pl.md).
-   Jak wyświetlić <img alt="" src=images/Plot_Legend.svg  style="width:24px;"> [legendę](Plot_Legend/pl.md).
-   Jak edytować <img alt="" src=images/Plot_Series.svg  style="width:24px;"> [etykiety serii](Plot_Series/pl.md), wprowadzając tekst w [LaTeX](http://www.latex-project.org).
-   Jak edytować <img alt="" src=images/Plot_Labels.svg  style="width:24px;"> [etykiety osi](Plot_Labels/pl.md), wprowadzając tekst w edytorze [LaTeX](http://www.latex-project.org).
-   Jak edytować style serii.
-   Jak zapisać swój wykres.

## Wykreślanie danych 

Aby wykreślić dane nie musisz tworzyć nowego dokumentu FreeCAD, wystarczy, że uruchomisz konsolę [Python](Python_console/pl.md) i zaczniesz wysyłać komendy, lub użyjesz [makrodefinicji](Macros/pl.md).

### Tworzenie dokumentu wykresu 

Wykresy są specjalnymi dokumentami, które można utworzyć ręcznie w celu późniejszego dodania danych, lub pozwolić, aby moduł utworzył je automatycznie w momencie rozpoczęcia wykreślania danych. Tworzenie własnych dokumentów wykresów ma dwie zalety:

-   Możesz ustawić etykietę okna dokumentu.
-   Możesz łatwo kontrolować, na którym dokumencie wykreślać dane.

Aby utworzyć nowy dokument działki wystarczy uruchomić następujące komendy:


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.figure("TrigonometricTest")
```

W wersji FreeCAD 0.19 wymagane jest zainstalowanie środowiska pracy <img alt="" src=images/Workbench_Plot.svg  style="width:24px;"> [Wykres](Plot_Workbench/pl.md) za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md), natomiast od wersji 0.20 FreeCAD nie wymaga już zewnętrznego dodatku do wykonywania wykresów. Powyższe polecenia utworzą nową zakładkę w [głównym oknie](Main_view_area/pl.md) o nazwie **TrigonometricTest**. Nowo utworzony dokument posiada już zestaw osi. Każdy dokument wykresu posiada co najmniej jeden zestaw osi.

### Funkcje rysowania 

Można również rozpocząć pracę od tego miejsca, ponieważ, jak już wyjaśniono, polecenie plot utworzy w razie potrzeby nowy dokument. Następną rzeczą, którą musimy zrobić, jest utworzenie danych dla funkcji sinus i cosinus, które chcemy wykreślić:


```python
import math
t = range(0,101)
t = [tt/100.0 for tt in t]
s = [math.sin(2.0*math.pi*tt) for tt in t]
c = [math.cos(2.0*math.pi*tt) for tt in t]
```

Spowoduje to utworzenie 3 tablic danych *(ze 101 punktami)*:

-   *t* = Czas w sekundach.
-   *s* = Funkcja sinus.
-   *c* = funkcja cosinus.

W celu wykreślenia obu funkcji wystarczy uruchomić kolejne komendy:


```python
Plot.plot(t,s)
Plot.plot(t,c)
```

Spowoduje to wykreślenie naszych funkcji. Polecenie **plot**\' dopuszcza jako argument etykietę serii, ale ponieważ będziemy ją później edytować za pomocą narzędzi modułu Plot, nie przekazujemy jeszcze tych danych.

## Konfiguracja wykresu 

### Wyświetlanie siatki i legendy 

Zmień środowisko pracy FreeCAD na [Wykres](Plot_Module/pl.md) w menu **Widok → Środowiska pracy**. Po załadowaniu modułu użyj narzędzia [siatki](Plot_Grid/pl.md), aby ją wyświetlić.

![](images/Plot_Grid.svg‎ ) *Ikonka narzędzia Pokaż / ukryj siatkę*

Możesz powtórzyć tę czynność, aby ukryć siatkę. Możesz również wyświetlić [legendę](Plot_Legend/pl.md) za pomocą dostarczonego narzędzia.

![](images/Plot_Legend.svg ) *Ikonka narzędzia Pokaż / ukryj legendę*

Jak widzisz, legenda jest pusta, ponieważ nie ustawiliśmy jeszcze żadnej etykiety serii. W środowisku pracy [Wykres](Plot_Module/pl.md) serie bez etykiety nie są wyświetlane w legendzie.

### Ustawianie etykiet serii 

Za pomocą narzędzia [serii](Plot_Series/pl.md) możesz edytować niektóre parametry serii.

![](images/Plot_Series.svg‎ ) *Ikonka narzędzia konfiguracji serii*

Najpierw wybierz serię, którą chcesz edytować, na przykład zaczniemy od pierwszej. Odznacz opcje {{CheckBox|Brak etykiety}} i ustaw tę etykietę:


```python
$y = \sin \left( 2 \pi t \right)$
```

Ponieważ [matplotlib](http://matplotlib.org/) obsługuje [LaTeX](http://www.latex-project.org), możesz ustawić wszystkie etykiety i tytuły, które chcesz, za jego pomocą. Ustaw następującą etykietę na drugą serię:


```python
$y = \cos \left( 2 \pi t \right)$
```

### Ustawianie stylu serii 

Seria pozwala na ustawienie wielu różnych właściwości. Spróbuj ustawić właściwości pokazane na przykładowym obrazku, zmieniając kolory serii i styl rysowania drugiej serii.

### Ustawianie etykiet osi 

Za pomocą narzędzia [Etykiety](Plot_Labels/pl.md) można ustawić etykiety przypisane do wszystkich utworzonych osi.

![](images/Plot_Labels.svg‎ ) *Ikonka narzędzia Ustaw etykiety*

Ustaw te dane:

-   Title = Przykład funkcji trygonometrycznych
-   X Label = \$t\$
-   Y Label = \$y = \\mathrm{f} \\left( t \\right)\$

Zmień również rozmiar czcionki w tytule i wszystkich etykietach na {{Value|20}}.

## Zapisywanie wykresu 

Za pomocą narzędzia do [zapisywania](Plot_Save/pl.md) wykresu możesz zapisać swój wykres jako plik graficzny w kilku formatach.

![](images/Plot_Save.svg ) *Ikonka narzędzia Zapisz wykres*

Najpierw należy wybrać ścieżkę dostępu do pliku wyjściowego.

Możesz ustawić rozmiar obrazu wyjściowego w calach, na przykład możemy ustawić 11.7x8.3, który jest rozmiarem papieru **DIN A4**. DPI *(Dots per inch)* będzie kontrolować rozdzielczość obrazu, na przykład 100 dpi. W połączeniu z podanymi wymiarami da to obraz o wymiarach 1170x830 pikseli.


{{Tutorials_navi

}} {{Plot_Tools_navi}} 

_ _

---
[documentation index](../README.md) > [External_Workbenches](Category_External_Workbenches.md) > Plot Basic tutorial/pl
