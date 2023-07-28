---
- GuiCommand:/pl
   Name:Std Group
   Name/pl:Std: Grupa
   MenuLocation:[Widok drzewa](Tree_view/pl.md) → Kliknij prawym przyciskiem myszki nazwę dokumentu → Utwórz grupę ...
   Workbenches:wszystkie
   Shortcut:
   Version:
   SeeAlso:[Część](Std_Part/pl.md), [Wybierz grupę](Draft_SelectGroup/pl.md), [Dodaj do grupy](Draft_AddToGroup/pl.md)
---

# Std Group/pl



## Opis

Obiekt **Std: Grupa** *(wewnętrznie nazywany [App DocumentObjectGroup](App_DocumentObjectGroup/pl.md))* jest kontenerem ogólnego przeznaczenia, który pozwala na grupowanie różnych typów obiektów w oknie [Widoku drzewa](Tree_view/pl.md), niezależnie od ich typu danych. Jest on używany jako prosty folder do kategoryzowania i organizowania obiektów w modelu w celu zachowania logicznej struktury. Obiekty Std: Grupa mogą być zagnieżdżone wewnątrz innych obiektów Std: Grupa.

Narzędzie Std: Grupa nie jest zdefiniowane przez konkretne środowisko pracy, lecz przez system bazowy, a więc znajduje się na **pasku narzędzi konstrukcji**, który jest dostępny we wszystkich [środowiskach pracy](Workbenches/pl.md).

Aby zgrupować obiekty 3D jako pojedynczą jednostkę, z zamiarem tworzenia złożeń, należy użyć obiektu [Std: Część](Std_Part/pl.md).

![](images/Std_Group_example.png )



*Różne elementy wewnątrz obiektu Std: Grupa w widoku drzewa.*



## Użycie

1.  Wykonaj jedną z następujących czynności:
    -   Kliknij prawym przyciskiem myszy nazwę dokumentu w [Widoku Drzewa](Tree_view/pl.md) i w menu kontekstowym wybierz pozycje **Utwórz grupę ...**.
    -   Naciśnij przycisk **<img src="images/Std_Group.svg" width=16px> [Utwórz grupę](Std_Group/pl.md)**.
2.  Utworzona zostanie pusta grupa.
3.  Aby dodać obiekty do grupy, wybierz je w oknie [Widoku drzewa](Tree_view/pl.md), a następnie przeciągnij i upuść na grupę.
4.  Aby usunąć obiekty z Grupy, przeciągnij je poza Grupę na etykietę dokumentu w górnej części okna [Widoku drzewa](Tree_view/pl.md).
5.  Obiekty mogą być również dodawane i usuwane poprzez edycję właściwości **Grupa**.



## Właściwości

Obiekt **Std: Grupa**, wewnętrznie nazywany [App DocumentObjectGroup](App_DocumentObjectGroup/pl.md) *(klasa `App::DocumentObjectGroup`)*, jest pochodną podstawowego obiektu [App DocumentObject](App_DocumentObject/pl.md) *(klasa `App::DocumentObject`)* i dziedziczy wszystkie jego właściwości.

Obiekt Std Grupa ma takie same właściwości jak [App: FeaturePython](App_FeaturePython/pl#Właściwości.md), który jest najbardziej podstawową instancją [App DocumentObject](App_DocumentObject/pl.md). Posiada on również następujące dodatkowe właściwości w [edytorze właściwości](Property_editor/pl.md). Ukryte właściwości można wyświetlić za pomocą polecenia **Wyświetl wszystko** w menu kontekstowym [edytora właściwości](Property_editor/pl.md).



### Dane


{{TitleProperty|Podstawa}}

-    **Grupa|LinkList**: lista obiektów, do których istnieją odniesienia. Domyślnie jest ona pusta {{value|[]}}.

-    **_ Group Touched|Bool|Hidden**: niezależnie od tego, czy grupa została zmodyfikowana, czy nie.



## Tworzenie skryptów 


**Zobacz również:**

[Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md), oraz [Obiekty skryptowe](Scripted_objects/pl.md).

Ogólne informacje na temat dodawania obiektów do dokumentu można znaleźć na stronie [Część: właściwość](Part_Feature/pl.md).

Element Std: Grupa *([App DocumentObjectGroup](App_DocumentObjectGroup/pl.md))* jest tworzony przy pomocy metody `addObject()` dokumentu. Gdy istnieje element Part, inne obiekty mogą być do niego dodane za pomocą metod `addObject()` lub `addObjects()` tej Części.


```python
import FreeCAD as App

doc = App.newDocument()
group = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Group")

obj1 = App.ActiveDocument.addObject("PartDesign::Body", "Body")
obj2 = App.ActiveDocument.addObject("Part::Box", "Box")

group.addObjects([obj1, obj2])
App.ActiveDocument.recompute()
```

Ten podstawowy obiekt `App::DocumentObjectGroup` nie posiada obiektu Proxy, więc nie może być w pełni wykorzystany do tworzenia klas podrzędnych.

Dlatego też, dla klasy podrzędnej [Python](Python/pl.md), powinieneś stworzyć obiekt `App::DocumentObjectGroupPython`.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "Name")
obj.Label = "Custom label"
```

Na przykład [Analiza MES](FEM_Analysis/pl.md) jest obiektem `App::DocumentObjectGroupPython` z niestandardową ikoną i dodatkowymi właściwościami.



## Odnośniki internetowe 

-   [Przypadek użycia w poradniku Architektury](Arch_tutorial/pl#Porządkowanie_modelu.md)
-   [Struktura dokumentu](Document_structure/pl.md)
-   [Porządkowanie modelu](http://www.freecadweb.org/wiki/index.php?title=Arch_tutorial#Organizing_your_model)





{{Std_Base_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std Group/pl
