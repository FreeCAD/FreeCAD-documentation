# Plot MultiAxes tutorial/pl



{{TutorialInfo/pl
|Topic=środowisko pracy wykres
|Level=średniozaawansowany
|Time=dowolny
|Author=
|FCVersion= -
|Files=
}}

Upewnij się, że odwiedziłeś [Poradnik: Podstawy dla środowiska pracy Wykres](Plot_Basic_tutorial/pl.md) przed rozpoczęciem tego poradnika. W tym poradniku nauczymy się jak tworzyć i edytować wykres wieloosiowy. Na stronie środowiska pracy[Wykres](Plot_Module/pl.md) możesz dowiedzieć się więcej o nim.

<img alt="" src=images/Plot_MultiAxes_Example.png  style="width:600px;"> 
*Przykład wykresu wieloosiowego*

Na poprzednim obrazku możesz zobaczyć rezultat, jaki w przybliżeniu uzyskamy. Dzięki temu poradnikowi dowiesz się:

-   Jak stworzyć wieloosiowy wykres z poziomu konsoli [Pythona](Python_console/pl.md).
-   Jak edytować właściwości osi.
-   Jak kontrolować siatkę / legendę, gdy obecnych jest kilka osi.
-   Jak edytować etykiety, tytuły i pozycje legendy.

## Wykreślanie danych 

Podobnie jak w [poprzednim poradniku](Plot_Basic_tutorial/pl.md) do wykreślania danych użyjemy [konsoli Python](Python_console/pl.md) lub [makrodefinicji](Macros.md), z tą różnicą, że w tym przypadku będziemy wykreślać dane na dwóch różnych osiach.

### Tworzenie danych wykresu 

W tym przykładzie wykreślimy 3 funkcje, dwie użyte w [poprzednim poradniku](Plot_Basic_tutorial/pl.md), oraz jeszcze jedną wielomianową. Faktem jest, że wielomian będzie potrzebował nowych osi z powodu zakresu zmienności innego niż wszystkie pozostałe. Kolejne polecenia utworzą nam tablice z danymi:


```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```

Gdy *x* zmienia się od 0 do 2, funkcja *y* ma maksymalną wartość 4, więc jeśli spróbujemy wykreślić tę funkcję za pomocą funkcji trygonometrycznych, przynajmniej jedna funkcja będzie obcięta lub źle przeskalowana, więc potrzebujemy wykresu wieloosiowego. Funkcja Multiaxes plot w FreeCAD jest zorientowana na uzyskanie wykresu z wieloma osiami, a nie na uzyskanie wielu wykresów w tym samym dokumencie.

### Rysowanie funkcji, dodawanie nowych osi 

Będziemy rysować funkcje wielomianowe na osiach głównych. Jeśli wszystkie osie będą miały ten sam rozmiar to nie jest istotne jaka funkcja jest narysowana w której osi, ale jeśli Twój wykres ma osie o innych rozmiarach *(jak w tym przykładzie)* to oś główna musi być największa *(ponieważ ta oś ma białe tło)*. Aby to zrobić wystarczy uruchomić komendę


```python
try:
    from FreeCAD.Plot import Plot
except ImportError:
    from freecad.plot import Plot

Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```

W tym przykładzie przekazujemy bezpośrednio etykiety serii dla legendy. Zwróć uwagę, że łańcuchy etykiet mają przedrostek *r*, aby zapobiec próbom interpretacji znaków specjalnych przez środowisko [Python](Python/pl.md) \'\'(symbol *r* jest często używany w składni [LaTeX](http://www.latex-project.org))\'\'.

Zanim będziemy mogli wykreślić funkcję wielomianową, musimy utworzyć nowe osie. W środowisku pracy [Wykres](Plot_Module/pl.md) nowe osie są automatycznie wybierane jako aktywne, a nowe wykresy będą powiązane z tymi osiami.


```python
Plot.addNewAxes()
Plot.plot(x,y,r"$x^2$")
```

Jak widzisz, wykres oszalał, znaczniki osi nałożyły się na siebie, krzywe mają ten sam kolor itd. Teraz musimy użyć [Modułu Wykres FreeCAD](Plot_Module/pl.md), aby naprawić ten wykres.

## Konfiguracja wykresu 

### Konfigurowanie osi 

Moduł [Wykres FreeCAD](Plot_Module/pl.md) dostarcza narzędzia do modyfikacji właściwości każdej z osi.

![](images/Plot_Axes.svg‎ ) *Ikonka narzędzia konfiguracji osi*

Za pomocą narzędzia [Konfiguruj osie](Plot_Axes/pl.md) możesz dodawać i usuwać osie oraz ustawiać aktywne osie, które są następnie używane, gdy wykreślasz więcej danych.

Aby zmienić rozmiar pierwszego zestawu osi, związanego z funkcjami trygonometrycznymi, należy go najpierw uaktywnić, zmieniając aktywną oś z {{Value|1}} na {{Value|0}}. Następnie możemy przesuwać suwaki wymiarów poziomych i pionowych, aby zmniejszyć jego rozmiar *(spróbuj odtworzyć przykład)*. Musimy również zmienić wyrównanie osi: wybieramy odpowiednio górę i prawo.

### Konfiguracja serii 

Ustaw właściwości serii tak jak to robiliśmy w [poprzednim poradniku](Plot_Basic_tutorial/pl.md).

### Wyświetlenie siatki i legendy 

może być pokazywana i ukrywana za pomocą narzędzi opisanych w [poprzednim poradniku](Plot_Basic_tutorial.md), ale w tym przypadku zachowanie jest nieco inne, ponieważ istnieją dwa zestawy osi.

Linie siatki są dodawane do aktywnego zestawu osi. Aby dodać linie do drugiego zestawu osi w naszym przykładzie, musi on być najpierw aktywowany poprzez zmianę aktywnych osi z {{Value|0}} na {{Value|1}} w [Konfiguruj osie](Plot_Axes/pl.md).

Jak już wspomnieliśmy, legenda zostanie umieszczona względem ostatniej ustawionej osi. Jeśli pokażesz teraz legendę, zobaczysz, że jest ona naprawdę źle umieszczona, ale naprawimy to później.

### Ustawianie etykiet osi 

Kiedy przychodzi do ustawiania [etykiet](Plot_Labels/pl.md) dla osi, znów mamy do czynienia z naszymi dwoma zestawami osi. Ale ponieważ etykiety są zazwyczaj ustawiane dla wszystkich osi, procedura jest taka sama jak opisana w [poprzednim poradniku](Plot_Basic_tutorial/pl.md). Moduł [Wykres](Plot_Module/pl.md) pozwala na ustawienie tytułu dla każdego zestawu osi. W tym przypadku chcemy ustawić tytuł tylko dla ostatniego, największego zestawu osi.

**Oś 0:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$

**Axes 1:**

-   Title = Przykład, wykres wieloosiowy
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

Zmień rozmiar czcionki wszystkich etykiet na {{Value|20}} oraz rozmiar czcionki tytułu do {{Value|24}}. Znów pojawia się element, tytuł, który jest źle umiejscowiony.

## Ustawianie pozycji elementów 

=

Moduł FreeCAD [Wykres](Plot_Module/pl.md) udostępnia narzędzie do ustawiania pozycji kilku elementów wykresu, takich jak tytuły, etykiety czy legenda.

![](images/Plot_Positions.svg ) *Ikona edytora pozycji*

Gdy uruchomisz narzędzie, zobaczysz listę wszystkich edytowalnych elementów. Tytuły i legendy mogą być przesuwane w obu kierunkach, ale etykiety osi mogą być przesuwane tylko wzdłuż osi, do której należą. Wybierz tytuł osi 1 i przesuń go na pozycję (0.24,1.01), następnie wybierz legendę i przesuń ją na lepszą pozycję. Możesz również zwiększyć rozmiar czcionki etykiet legendy.

## Zapisanie wykresu 

Teraz możesz zapisać swoją pracę. Zobacz [poprzedni poradnik](Plot_Basic_tutorial/pl.md) jeśli nie pamiętasz jak to zrobić.


{{Tutorials_navi

}} {{Plot_Tools_navi}} 

[Category:External\_Workbenches](Category:External_Workbenches.md) [Category:Addons](Category:Addons.md)
