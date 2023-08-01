---
- GuiCommand:
   Name:Sketcher ConstrainParallel
   Name/pl:Szkicownik: Wiązanie równoległości
   MenuLocation:Szkic → Wiązania szkicownika → Wiązanie równoległości
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**P**
   SeeAlso:[Zwiąż w pionie](Sketcher_ConstrainVertical/pl.md), [Zwiąż w poziomie](Sketcher_ConstrainHorizontal/pl.md)
---

# Sketcher ConstrainParallel/pl



## Opis

Wiązanie równoległości narzuca, aby dwie wybrane proste lub krawędzie były równoległe do siebie.



## Użycie

Szkic zawiera dwie linie o przypadkowej lokalizacji.

<img alt="" src=images/ConstrainParallel1.png  style="width:500px;">



*Zaznacz obie linie, klikając kolejno na każdą z nich..*

<img alt="" src=images/ConstrainParallel2.png  style="width:500px;">

Zastosuj wiązanie równoległości poprzez:

-   Naciśnięcie przycisku **[<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> [Wiązanie równoległości](Sketcher_ConstrainParallel/pl.md)** z paska narzędzi wiązania Szkicownika.
-   Używając klawiszy **P** skrót klawiszowy.
-   Używając pozycji **Szkic → Wiązania Szkicownika → [<img src=images/Sketcher_ConstrainParallel.svg style="width:16px"> Wiązanie równoległości** z menu głównego.

<img alt="" src=images/ConstrainParallel3.png  style="width:500px;">



*Result: Wybrane linie zostają ustawione równolegle do siebie. Zmiana orientacji jednej linii spowoduje zmianę orientacji drugiej, tak aby zachować tę samą orientację.*



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Parallel', Line1, Line2))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Line1` oraz `Line2` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainParallel/pl
