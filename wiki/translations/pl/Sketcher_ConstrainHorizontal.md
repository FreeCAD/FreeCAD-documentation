---
- GuiCommand:/pl
   Icon:Constraint Horizontal.svg
   Name:Sketcher ConstrainHorizontal
   Name/pl:Szkicownik: Zwiąż w poziomie
   MenuLocation:Szkic → Wiązania szkicownika → Zwiąż w poziomie
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**H**
   SeeAlso:[Wiązanie pionowe](Sketcher_ConstrainVertical/pl.md)
---

# Sketcher ConstrainHorizontal/pl



## Opis

Wiązanie poziome wymusza, aby wybrana linia lub linie na szkicu były równoległe do osi poziomej szkicu.



## Użycie

<img alt="" src=images/HorizontalConstraint1.png  style="width:500px;"> 
*Wybierz linię na szkicu, klikając na nią.*

<img alt="" src=images/HorizontalConstraint2.png  style="width:500px;"> 
*Linia staje się ciemnozielona.*

<img alt="" src=images/HorizontalConstraint3.png  style="width:500px;"> 
*Zastosuj Wiązanie poziome klikając na ikonę **[<img src=images/Sketcher_ConstrainHorizontal.svg style="width:16px"> '''Zwiąż w poziomie'''* na pasku narzędzi '''Wiązania szkicownika''' lub wybierając pozycję menu '''Zwiąż w poziomie''' w podmenu '''Wiązania szkicownika''' w pozycji menu Szkic w środowisku pracy Szkicownik ''(lub w pozycji menu Projekt Części w środowisku pracy Projekt Części)''. Wybrana linia jest związana z osią poziomą szkicu, która powinna być równoległa do osi poziomej.**

<img alt="" src=images/HorizontalConstraint4.png  style="width:500px;"> 
*Można wybrać wiele linii.*

<img alt="" src=images/HorizontalConstraint5.png  style="width:500px;"> 
*a następnie stosując opisane powyżej wiązanie, są one powiązane równolegle do osi poziomej szkicu.*



## Tworzenie skryptów 


```pythonSketch.addConstraint(Sketcher.Constraint('Horizontal', Line))```

Strona [skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, których można użyć dla `Line` oraz zawiera dalsze przykłady tworzenia wiązań przy użyciu skryptów języka Python.





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainHorizontal/pl
