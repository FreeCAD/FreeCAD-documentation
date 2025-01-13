---
 GuiCommand:
   Name: Arch Roof
   Name/pl: BIM: Dach
   MenuLocation: 3D / BIM , Dach
   Workbenches: BIM_Workbench/pl
   Shortcut: **R** **F**
   SeeAlso: 
---

# Arch Roof/pl



## Opis

Narzędzie **Dach** pozwala na utworzenie pochyłego dachu z wybranej linii. Utworzony obiekt dachu jest parametryczny, zachowując relację z obiektem bazowym. Zasada jest taka, że każdej krawędzi przypisany jest profil dachu *(nachylenie, szerokość, okap, grubość)*.

**Uwaga:** Narzędzie to jest wciąż w fazie rozwoju i może zawieść w przypadku bardzo złożonych kształtów.

<img alt="" src=images/RoofExample.png  style="width:600px;"> 
*Widok z góry modelu budynku przedstawiający dach z pewną przezroczystością.*



## Użycie(polilinia bazowa) 

1.  Stwórz zamkniętą polilinię, idąc w kierunku przeciwnym do ruchu wskazówek zegara, i zaznacz ją.

2.  Naciśnij przycisk **<img src="images/Arch_Roof.svg" width=16px> '''Dach'''**, lub użyj skrótu klawiszowego **R**, a następnie **F**.

3.  Domyślny obiekt dachu może mieć dziwny kształt, ponieważ narzędzie brakuje niezbędnych informacji.

4.  Po utworzeniu domyślnego dachu, kliknij dwukrotnie na obiekt w widoku drzewa, aby uzyskać dostęp i edytować wszystkie właściwości. Kąt musi mieć wartość pomiędzy 0° a 90°.

5.  Każda linia odpowiada jednej płycie dachowej. Możesz więc ustawić właściwości dla każdej z nich.

6.  Aby ułatwić sobie zadanie, możesz ustawić wartość `Angle` lub `Run` na `0` i zdefiniować `Relative Id`, co spowoduje automatyczne obliczenie danych względem `Relative Id`.

7.  Działa to następująco:
    1.  Jeśli `Angle &#61; 0` i `Run &#61; 0`, to profil jest identyczny jak względny profil.
    2.  Jeśli `Angle &#61; 0`, to `Angle` jest obliczany tak, aby wysokość była taka sama jak w względnym profilu.
    3.  Jeśli `Run &#61; 0`, to `Run` jest obliczany tak, aby wysokość była taka sama jak w względnym profilu.

8.  W końcu, ustaw kąt na 90°, aby uzyskać szczyt.

9.  
    **Uwaga**: dla lepszego zrozumienia, zapoznaj się z [prezentacją na YouTube](https://www.youtube.com/watch?v=4Urwru71dVk).



## Użycie (bryła bazowa) 

Jeśli dach ma skomplikowany kształt *(np. zawiera skośne okna lub inne niestandardowe elementy)*, można utworzyć niestandardowy obiekt bryłowy za pomocą różnych innych narzędzi FreeCAD *([Część](Part_Workbench/pl.md), [Szkicownmik](Sketcher_Workbench.md) itp.)* A następnie użyć tej bryły jako obiektu **bazowego** dla dachu:

1.  Wybierz obiekt bazowy.
2.  Naciśnij przycisk **<img src="images/Arch_Roof.svg" width=16px> '''Dach'''** lub naciśnij **R**, a następnie **F**.



## Odjęcie nad dachem 

Dachy mają automatycznie generowaną objętość odejmowania *({{Version/pl|1.0}} dla dachów z podstawą z bryły)*. Gdy dach jest [usuwany](Arch_Remove/pl.md) ze ścian budynku, zarówno sam dach, jak i wszystko nad nim jest odejmowane od ścian.


{{Version/pl|1.0}}

: Możliwe jest zastąpienie automatycznego odejmowania objętości poprzez ustawienie właściwości **Subvolume** dachu na niestandardowy obiekt bryłowy.

<img alt="" src=images/Arch_Roof_Subtract_Default.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subtract_Subvolume.png  style="width:" height="150px;"> <img alt="" src=images/Arch_Roof_Subvolume_Example.png  style="width:" height="150px;"> 
*Dach oparty na bryle przed ''(obrazek 1.)'' i po ''(obrazek 2.)'' [usunięciu](Arch_Remove/pl.md) go ze ścian.<br>
Trzeci obraz przedstawia wygenerowaną objętość odejmowania.*



## Opcje

-   Dachy dzielą wspólne właściwości i zachowania wszystkich [komponentów](Arch_Component/pl.md).



## Właściwości



### Dane


{{TitleProperty|Dach}}

-    **Kąty|FloatList**: Lista kątów połaci dachu.

-    **Długość obramowania|Length**: Całkowita długość granic dachu.

-    **Ściana|Integer**: Numer ściany obiektu bazowego użytej do budowy dachu (nie używane).

-    **Odwrócony|Bool**: Określa, czy kierunek dachu powinien być odwrócony.

-    **Wysokości|FloatList**: Lista obliczonych wysokości segmentów dachu.

-    **Id Rel|IntegerList**: Lista identyfikatorów profilów względnych segmentów dachu.

-    **Overhang|FloatList**: Lista wysięgników segmentów dachu.

-    **Długość kalenic|Length**: Całkowita długość grzbietów i szczytów dachu.

-    **Przebiegi|FloatList**: Lista rzutów poziomych długości segmentów dachu.

-    **ObjętośćPodrzędna|Link**: Objętość do odjęcia. Jeśli określone, jest używana zamiast automatycznie wygenerowanej objętości podrzędnej. {{Version/pl|1.0}}

-    **Grobość|FloatList**: Lista grubości segmentów dachu.



## Tworzenie skryptów 


**Zobacz również:**

[API: Architektura](Arch_API/pl.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Dach** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji:


```python
Roof = makeRoof(baseobj=None, facenr=0, angles=[45.,], run=[], idrel=[0,], thickness=[50.,], overhang=[100.,], name="Roof")
```

-   Tworzy obiekt `Roof` z podanego `baseobj`, który może być zamkniętą linią lub obiektem stałym.
    -   Jeśli `baseobj` jest linią, można podać listy dla `angles`, `run`, `idrel`, `thickness` i `overhang`, dla każdej krawędzi w linii, aby zdefiniować kształt dachu.
    -   Listy są automatycznie uzupełniane w celu dopasowania do liczby krawędzi w polilinii.

Przykład:


```python
import FreeCAD as App
import Arch, Draft

doc = App.newDocument()

rect = Draft.makeRectangle(3000, 4000)
doc.recompute()

roof = Arch.makeRoof(rect, angles=[30.,])

p1 = App.Vector(0, 0, 0)
p2 = App.Vector(1000, 1000, 0)
p3 = App.Vector(0, 2000, 0)

wire = Draft.make_wire([p1, p2, p3], closed=True)
doc.recompute()

roof1 = Arch.makeRoof(wire)

doc.recompute()
```





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch Roof/pl
