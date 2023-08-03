---
 GuiCommand:
   Name: Part Helix
   Name/pl: Część: Helisa
   MenuLocation: Część , Utwórz geometrie pierwotne ... , Helisa
   Workbenches: Part_Workbench/pl, OpenSCAD_Workbench/pl
   SeeAlso: Part_Primitives/pl
---

# Part Helix/pl



## Opis

<img alt="" src=images/Part_Helix.svg  style="width:24px;"> **Helisa** środowiska praczy Część to parametryczna bryła, którą można utworzyć za pomocą polecenia <img alt="" src=images/Part_Primitives.svg  style="width:24px;"> [Utwórz geometrie pierwotne \...](Part_Primitives/pl.md). W układzie współrzędnych zdefiniowanym przez właściwość **Umiejscowienie**, oś helisy pokrywa się z osią Z, a jej dolny punkt, punkt początkowy, leży na osi X.

<img alt="" src=images/Part_Helix_Example.png  style="width:400px;">



## Użycie

Zobacz stronę [Geometrie pierwotne](Part_Primitives/pl#Użycie.md).



## Przykład

![Helisa środowiska pracy Część na przykładzie skryptu](images/Part_Helix_Scripting_Example.png )

Poniżej pokazano obiekt Halisy utworzony za pomocą [przykładowego skryptu](#Tworzenie_skryptów.md).



## Uwagi

-   Helisa środowiska Część może być używana do tworzenia gwintów śrubowych. Zobacz stronę [Tworzenie gwintów](Thread_for_Screw_Tutorial/pl.md).



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Obiekt Helisa wywodzi się z obiektu [Część: Cecha](Part_Feature/pl.md) i dziedziczy wszystkie jego właściwości. Posiada on również następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Dołączenie}}

Obiekt ten ma takie same właściwości dołączania jak [Part: Part2DObject](Part_Part2DObject/pl#Dane.md).


{{TitleProperty|Układ współrzędnych}}

-    **Koordynacja Lokalna|Enumeration**: [skrętność](https://en.wikipedia.org/wiki/Screw_thread), czyli kierunek spirali: {{Value|Prawoskrętny}} lub {{Value|Lewoskrętny}}. Domyślną wartością jest {{Value|Prawoskrętny}}, co oznacza, że spirala obraca się w kierunku przeciwnym do ruchu wskazówek zegara.


{{TitleProperty|Helisa}}

-    **Skok|Length**: Odległość między dwoma kolejnymi zwojami spirali mierzona wzdłuż jej osi Z. Domyślnie {{Value|1mm}}.

-    **Wysokość|Length**: Wysokość spirali. Domyślnie {{Value|2mm}}.

-    **Promień|Length**: Promień początkowy helisy. Spirala ma stały promień, jeśli **Kąt** ma wartość {{Value|0°}}.

-    **Długość segmentu|QuantityConstraint**: Liczba zwojów na każdy podział helisy. Domyślnie {{Value|1}}, co oznacza, że każdy pełny obrót helisy jest oddzielnym segmentem. Użyj wartości {{Value|0}}, aby pominąć podział.

-    **Kąt|Angle**: Kąt określający zewnętrzny kształt helisy. Prawidłowy zakres: {{Value|-90° &lt; wartość &lt; 90°}}. Wartością domyślną jest {{Value|0°}}. Jeśli {{Value|0°}}, helisa jest cylindryczna, w przeciwnym razie jest stożkowa.



## Tworzenie skryptów 

Zobacz również: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Skrypty w środowisku Część](Part_scripting/pl.md) i [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Helisa środowiska pracy Część jest tworzony za pomocą metody `addObject()`.


```python
helix = FreeCAD.ActiveDocument.addObject("Part::Helix", "myHelix")
```

-   Gdzie parametr {{Incode|"myHelix"}} jest etykietą dla obiektu.
-   Funkcja zwraca nowo utworzony obiekt.

Przykład:


```python
import FreeCAD as App

doc = App.activeDocument()

helix = doc.addObject("Part::Helix", "myHelix")
helix.Pitch = 2
helix.Height = 3
helix.Radius = 4
helix.SegmentLength = 21
helix.Angle = 45
helix.Placement = App.Placement(App.Vector(1, 2, 3), App.Rotation(75, 60, 30))

doc.recompute()
```





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Helix/pl
