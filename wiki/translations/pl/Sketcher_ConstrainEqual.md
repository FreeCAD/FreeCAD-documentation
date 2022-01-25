---
- GuiCommand:/pl
   Name:Sketcher ConstrainEqual
   Name/pl:Skzkicownik: Wiązanie równości
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   MenuLocation:Szkicownik → Wiązania szkicownika → Wiązanie równości
   Shortcut:**E**
   SeeAlso:[Szkicownik: Wiązanie kąta](Sketcher_ConstrainRadius/pl.md)
---

# Sketcher ConstrainEqual/pl

## Opis

Wiązanie Równości wymusza, aby dwa lub więcej odcinki w linii, linii łamanej lub prostokącie miały jednakową długość. W przypadku zastosowania do łuków lub okręgów, promienie są wiązane tak, aby były równe. Wiązanie nie może być stosowane do elementów pierwotnych geometrii, które nie są tego samego typu *(np. odcinki linii i łuki)*.

## Użycie

Poniższy przykładowy rysunek zawiera szereg pierwotnych elementów szkicowych *(linia, linia łamana, prostokąt, łuk i okrąg)*.

![](images/EqualConstraint1.png )

Wybierz co najmniej dwa segmenty linii *(np. Linię i jeden bok prostokąta)*.

![](images/EqualConstraint2.png )

Kliknij na przycisk **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązanie równości](Sketcher_ConstrainEqual.md)** na pasku narzędzi Szkicownika *(w Środowiska pracy Szkicownik lub Projekt części)* lub wybierz pozycję menu Wiązanie równości z podmenu Wiązania Środowiska pracy Szkicownik lub lub Projekt części, zależnie od tego, które środowisko pracy zostanie wybrane, aby zastosować wiązanie do wybranych elementów.

![](images/EqualConstraint3.png )

Teraz wybierz łuk i okrąg na szkicu.

![](images/EqualConstraint4.png )

i zastosuj **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązanie równości](Sketcher_ConstrainEqual.md)** jak poprzednio.

![](images/EqualConstraint5.png )

Teraz wybierz odcinek linii, wszystkie segmenty linii łamanej i jeden z pozostałych niezwiązanych boków prostokąta

![](images/EqualConstraint6.png )

i zastosuj **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązanie równości](Sketcher_ConstrainEqual.md)** jak poprzednio.

![](images/EqualConstraint7.png )

Wybierz segment linii i łuk

![](images/EqualConstraint8.png )

i zastosuj **[<img src=images/Sketcher_ConstrainEqual.svg style="width:16px"> [Wiązanie równości](Sketcher_ConstrainEqual.md)** jak poprzednio. Wyskakujący komunikat wskazuje, że elementy podlegające wiązaniom muszą być tego samego typu geometrycznego *(linie o krzywiznach zerowych lub linie o krzywiznach niezerowych)*.

![](images/EqualConstraint9.png )

## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Equal', Edge1, Edge2))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Edge1` oraz `Edge2` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainEqual/pl
