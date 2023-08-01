---
- GuiCommand:
   Name:PartDesign Clone
   Name/pl:Projekt Części: Utwórz klona
   MenuLocation:Projekt części → Utwórz klona
   Workbenches:[Projekt części](PartDesign_Workbench/pl.md)
   Version:0.17
   Version:0.17
   SeeAlso:[Klon](Draft_Clone/pl.md)
---

# PartDesign Clone/pl



## Opis

Funkcja **Klon** środowiska Projekt Części tworzy połączoną kopię wybranego obiektu, która będzie podążać za wszelkimi przyszłymi edycjami oryginalnego obiektu *(z wyjątkiem umiejscowienia)*. Na przykład, jednym z przypadków użycia jest wykonanie [operacji logicznej](PartDesign_Boolean/pl.md) na obiekcie utworzonym w innym środowisku roboczym. Większość typów obiektów jest akceptowana, o ile są to pojedyncze bryły. Jeśli potrzebujesz sklonować wiele obiektów *(np. bryły)* lub [kontener](Std_Part/pl.md) środowiska Część, możesz użyć funkcji [klon](Draft_Clone/pl.md) ze środowiska Rysunek Roboczy. Jednym z zastrzeżeń jest to, że klon środowiska roboczego Projekt części ustawia bieżące położenie klonu jako zero *(zarówno translację kartezjańską, jak i orientację przestrzenną)*. Podczas gdy klon środowiska roboczego Rysunek Roboczy oblicza i ustawia wartości liczbowe bieżącego położenia i orientacji klonowanych obiektów w odniesieniu do pojemnika klonowanego obiektu.

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Klon wewnętrznego koła zębatego podczas przesuwania w przestrzeni 3D jako niezależny obiekt*



## Użycie

1.  W drzewie modelu wybierz obiekt, który ma zostać sklonowany.
2.  Naciśnij przycisk **[<img src=images/PartDesign_Clone.svg style="width:24px"> '''Utwórz klona'''**.



## Właściwości

-    **Cecha bazowa**: ustawia oryginalny obiekt, na którym bazuje klon. Aby zastąpić, naciśnij przycisk **...**, aby uzyskać listę dostępnych obiektów.

-    **Umiejscowninie**: określa orientację i pozycję klona w przestrzeni 3D. Zobacz stronę [Umiejscowienie](Placement/pl.md).

-    **Etykieta**: etykieta nadawana obiektowi Klon. Zmień ją zgodnie z własnymi potrzebami.



## Ograniczenia

-   Do klonowania w środowisku Projekt Części można użyć tylko jednego obiektu.
-   Obsługiwane są tylko obiekty składające się z pojedynczej bryły. Dlatego [złożenia](Glossary/pl#Compound.md) takie jak [Część: kontener](Std_Part/pl.md), [Część: Utwórz złożenie](Part_Compound/pl.md) lub [Rysunek Roboczy: Szyk ortogonalny](Draft_OrthoArray/pl.md) nie są obsługiwane.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/pl
