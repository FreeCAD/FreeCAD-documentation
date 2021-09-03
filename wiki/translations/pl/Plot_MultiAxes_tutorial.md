 {{TutorialInfo/pl
|Topic=środowisko pracy wykres
|Level=średniozaawansowany
|Time=dowolny
|Author= -
|FCVersion= -
|Files=brak
}}

Upewnij się, że odwiedziłeś [Poradnik: Podstawy dla środowiska pracy Wykres](Plot_Basic_tutorial/pl.md) przed rozpoczęciem tego poradnika. W tym poradniku nauczymy się jak tworzyć i edytować wykres wieloosiowy. Na stronie środowiska pracy[Wykres](Plot_Module/pl.md) możesz dowiedzieć się więcej o nim.

<img alt="Przykład wykresu wieloosiowego" src=images/Plot_MultiAxes_Example.png  style="width:600px;">


<center>

Przykład wykresu wieloosiowego.


</center>

Na poprzednim obrazku możesz zobaczyć rezultat, jaki w przybliżeniu uzyskamy. Dzięki temu poradnikowi dowiesz się:

-   Jak stworzyć wieloosiowy wykres z poziomu konsoli Pythona.
-   Jak edytować właściwości osi.
-   Jak kontrolować siatkę / legendę, gdy obecnych jest kilka osi.
-   Jak edytować etykiety, tytuły i pozycje legendy.

## Wykreślanie danych {#wykreślanie_danych}

Podobnie jak w [poprzednim poradniku](Plot_Basic_tutorial/pl.md) do wykreślania danych użyjemy konsoli Python lub [makrodefinicji](Macros.md), z tą różnicą, że w tym przypadku będziemy wykreślać dane na dwóch różnych osiach.

### Creating plot data {#creating_plot_data}

In this example we will plot 3 functions, the two ones used in [previous tutorial](Plot_Basic_tutorial.md), and another polynomial one. The fact is that the polynomial one will need new axes due to the variation range is different from all others. Next commands will create data arrays for us:


```python
import math
p = range(0,1001)
x = [2.0*xx/1000.0 for xx in p]
y = [xx**2.0 for xx in x]
t = [tt/1000.0 for tt in p]
s = [math.sin(math.pi*2.0*tt) for tt in t]
c = [math.cos(math.pi*2.0*tt) for tt in t]
```

As *x* moves from 0 to 2, *y* function has a maximum value of 4, so if we try to plot this function with trigonometrical ones, at least one function will be truncated or bad scaled, then we need a multiaxes plot. Multiaxes plot in FreeCAD is oriented to get a plot with multiple axes, not to get multiple plots in same document.

### Drawing functions, adding new axes {#drawing_functions_adding_new_axes}

We will draw polynomial function at main axes. If all your axes will have same size then is not relevant what function is ploted in what axes, but if your plot has axes with other size (as in this example), main axes must be the biggest one (because this axes have the white background). In order to do it we only need to launch a command


```python
import Plot
Plot.plot(x,y,r"$x^2$")
```

In this example we pass directly the series label for the legend. Note that the label string has the *r* prefix in order to avoid Python try to interpret special characters (*\\* symbol is used frecuently in [LaTeX](http://www.latex-project.org) syntax).

Now we can plot trigonometrical functions, creating new axes before. In [FreeCAD Plot module](Plot_Module.md) when you create new axes this axes are selected as active ones, so new plots will be associated to this axes.


```python
Plot.addNewAxes()
Plot.plot(t,s,r"$\sin\left( 2 \pi t \right)$")
Plot.plot(t,c,r"$\cos\left( 2 \pi t \right)$")
```

As you can see you plot has gone crazy, with axes ticks overlaped, curves of same color, etc. Now we needs to use [FreeCAD Plot module](Plot_Module.md) to fix this graph.

## Konfiguracja wykresu {#konfiguracja_wykresu}

### Konfigurowanie osi {#konfigurowanie_osi}

Moduł [Wykres FreeCAD](Plot_Module/pl.md) dostarcza narzędzia do modyfikacji właściwości każdej z osi.

![Ikonka narzędzia konfiguracji osi](images/Plot_Axes.svg‎ )


<center>

Ikonka narzędzia konfiguracji osi.


</center>

Pierwszą rzeczą, którą można znaleźć w narzędziu osi jest selektor aktywnych osi. Ponieważ osie aktywne są ostatnimi, aktywne osie są umieszczone na pierwszej pozycji. Narzędzie Osie, podobnie jak narzędzie Etykiety, pozwala ustawić aktywne osie, umożliwiając wykreślanie większej ilości danych na osiach, których potrzebujemy *(w tym dodawanie / usuwanie osi)*. Na razie będziemy pracować nad wybranymi osiami, które są związane z funkcjami trygonometrycznymi.

W suwakach wymiarów przesuniemy suwaki lewy poziomy i dolny pionowy *(starając się naśladować przykład)*, aby zmniejszyć rozmiar osi. Następnie możemy ustawić wyrównanie osi, zmieniając je na górne i prawe, oraz ustawiając niewielkie przesunięcie o dwie jednostki.

### Konfiguracja serii {#konfiguracja_serii}

Ustaw właściwości serii tak jak to robiliśmy w [poprzednim poradniku](Plot_Basic_tutorial/pl.md).

### Wyświetlenie siatki i legendy {#wyświetlenie_siatki_i_legendy}

Siatka i legenda jest pokazywana i ukrywana za pomocą tych samych narzędzi, które były używane w [poprzednim poradniku](Plot_Basic_tutorial/pl.md), ale w tym przypadku zachowanie jest trochę inne z powodu obecności dwóch różnych osi.

Regarding grid lines, you can show lines for each axes set, for example, if you try to show grid now you will show only the grid of the trigonometrical functions, so in order to show the grid of polynomial function plot you needs to change active axes to 0 (using axes configuration tool) before using grid tool another time (Is possible that you need to press two times the tool).

Regarding legend, the legend will be the same for both axes, so you can choose the axes that you want in order to show the legend, but is strongly recommended to use the biggest ones (0 in this example) because position will be refered to this axes coordinates. If you show the legend you can see that is really bad placed, we will fix this problem later.

### Setting axes labels {#setting_axes_labels}

You can set axes labels with same tool used in [previous tutorial](Plot_Basic_tutorial.md), with the difference that now you have more axes. Since axes labels is ussually set as one per axis, is not a significant difference, but [FreeCAD Plot module](Plot_Module.md) allow you to set a title by axes too. In this case we only wants to set title to main axes, so set:

**Axes 0:**

-   Title = Multiaxes example
-   X Label = \$x\$
-   Y Label = \$\\mathrm{f} \\left( x \\right)\$

**Axes 1:**

-   X Label = \$t\$
-   Y Label = \$\\mathrm{f} \\left( t \\right)\$

Set also 20 to fontsize for all but title, that uses a fontsize of 24. As happens with legend, title is bad placed, interseting with second axes set, so we need to solve both problems.

### Setting elements position {#setting_elements_position}

[FreeCAD Plot module](Plot_Module.md) provides a tool in order to set the position of several plot elements, as titles, labels or legend.

![Position editor icon](images/Plot_Positions.svg‎ )


<center>

Position editor icon.


</center>

When you run the tool you see a list with all the editable elements. Title elements, as well as legend, can be moved in both directions, since axes labels can be moved only on the axes direction. Select title of axes 0 and move it to (0.24,1.01), then select legend and move it to a better position. You can increase legend labels fontsize too.

## Zapisanie wykresu {#zapisanie_wykresu}

Teraz możesz zapisać swoją pracę. Zobacz [poprzedni poradnik](Plot_Basic_tutorial/pl.md) jeśli nie pamiętasz jak to zrobić. {{Tutorials navi}} {{Plot Tools navi}} 
