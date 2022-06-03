---
- GuiCommand   */pl
   Name   *Sketcher ConstrainTangent
   Name/pl   *Szkicownik   * Wiązanie styczności
   MenuLocation   *Sketch → Wiązania szkicownika → Wiązanie styczności
   Workbenches   *[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut   ***T**
   SeeAlso   *[Wiązanie punktu na obiekcie](Sketcher_ConstrainPointOnObject/pl.md)
---

# Sketcher ConstrainTangent/pl

## Opis

Wiązanie styczności tworzy dwie krzywe, które dotykają się wzajemnie *(są styczne)*. Linie są traktowane jako nieskończone, a łuki są traktowane jako pełne koła/elipsy. Wiązanie jest również w stanie połączyć dwie krzywe, zmuszając je do zetknięcia się ze sobą po stycznej, co sprawia, że połączenie jest gładkie.

Wiązanie styczności może być również użyte z dwiema liniami, aby uczynić je współliniowymi.

## Użycie

Istnieje pięć różnych sposobów zastosowania tego wiązania   *

1.  pomiędzy dwoma krzywymi *(dostępne nie dla wszystkich krzywych)*,
2.  pomiędzy dwoma punktami końcowymi krzywej, tworząc gładkie połączenie
3.  pomiędzy krzywą a punktem końcowym innej krzywej,
4.  pomiędzy dwoma krzywymi w punkcie zdefiniowanym przez użytkownika.
5.  pomiędzy dwiema liniami, aby stworzyć warunki współliniowe.

Aby zastosować wiązanie styczności, należy wykonać następujące czynności   *

-   Wybierz dwie lub trzy pozycje na szkicu.
-   Wywołaj wiązanie, klikając jego ikonę na pasku narzędzi, wybierając element menu lub używając skrótu klawiaturowego.

### Pomiędzy dwoma krzywymi *(bezpośrednia styczność)* 

<img alt="" src=images/Sketcher_ConsraintTangent_mode1.png  style="width   *600px;">

Dwie krzywe staną się styczne, a punkt styczności będzie ukryty. Tryb ten jest stosowany w przypadku wybrania dwóch krzywych.

**Zaakceptowany wybór**   *

-   linia + linia, okrąg, łuk, elipsa, łuk elipsy
-   okrąg, łuk + okrąg, łuk

Jeżeli bezpośrednia styczność pomiędzy wybranymi krzywymi nie jest obsługiwana *(np. pomiędzy okręgiem a elipsą)*, do szkicu zostanie automatycznie dodany punkt pomocniczy i zastosowany zostanie punkt styczności.

Nie zaleca się rekonstrukcji punktu styczności poprzez tworzenie punktu i wiązanie go z ułożeniem na obu krzywych. Będzie to działać, ale zbieżność będzie znacznie wolniejsza, bardziej skokowa i będzie wymagała około dwa razy więcej iteracji do zbieżności niż normalnie. Użyj innych trybów tego wiązania, jeśli punkt styczności jest potrzebny.

### Między dwoma punktami końcowymi (styczność punkt-punkt) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode2.png  style="width   *600px;">

W tym trybie punkty końcowe są zbieżne, a połączenie jest styczne *(C1 - gładkie lub \"ostre\", w zależności od położenia krzywych przed nałożeniem wiązania)*. Tryb ten jest stosowany w przypadku wybrania dwóch punktów końcowych dla dwóch krzywych. Jeśli chcesz uzyskać ten rodzaj styczności, nie możesz używać zbieżności plus styczności między krzywymi / liniami. Solver nie może utworzyć stabilnych rozwiązań dla tej kombinacji i odpowiednio zastępuje ograniczenia.

\"Zaakceptowany wybór   *

-   punkt końcowy linii / łuku / łuku-ellipsy + punkt końcowy linii / łuku/ łuku-ellipsy *(tj. dwa punkty końcowe dowolnych dwóch krzywych)*

### Pomiędzy krzywą a punktem końcowym (styczność punkt - krzywa) 

<img alt="" src=images/Sketcher_ConsraintTangent_mode3.png  style="width   *600px;">

W tym trybie, punkt końcowy jednej krzywej jest związany z położeniem na drugiej krzywej, a krzywe stają się w tym punkcie stycznymi. Tryb ten jest stosowany, gdy krzywa i punkt końcowy innej krzywej zostały wybrane.

**Zaakceptowany wybór   ***

-   linia, okrąg, łuk, elipsa, łuk elipsy + punkt końcowy linii / łuku / łuku elipsy *(tzn. każda krzywa + punkt końcowy każdej krzywej)*.

### Między dwiema krzywymi w punkcie *(styczna do punktu) (v0.15)* 

<img alt="" src=images/Sketcher_ConsraintTangent_mode4.png  style="width   *600px;">

W tym trybie dwie krzywe są styczne, a punkt styczności jest śledzony. Ten tryb jest stosowany, gdy wybrano dwie krzywe i punkt.

**Zaakceptowany wybór   ***

-   każda linia / krzywizna + każda linia / krzywizna + każdy punkt

\"Każdy punkt\" może być samotnym punktem, albo punktem jakiegoś obiektu, np. środkiem okręgu, punktem końcowym łuku, albo początkiem.

Aby wiązanie działało prawidłowo, punkt musi znajdować się na obu krzywych. Tak więc, w miarę wywoływania wiązania, punkt będzie automatycznie związany z obiema krzywymi *([wiązanie pomocnicze](Sketcher_helper_constraint/pl.md) zostanie dodane, jeśli jest to konieczne)*, a krzywe zostaną związane w punkcie styczności. Te [wiązania pomocnicze](Sketcher_helper_constraint/pl.md) są zwykłymi regularnymi wiązaniami. Mogą być dodane ręcznie lub usunięte.

W porównaniu z bezpośrednią stycznością, wiązanie to jest wolniejsze, ponieważ istnieje więcej stopni swobody, ale jeśli punkt styczności jest potrzebny, jest to tryb zalecany, ponieważ oferuje lepszą zbieżność w porównaniu z bezpośrednią stycznością + punkt na dwóch krzywych.

Umiejscowienie punktu przed zastosowaniem wiązania jest wskazówką dla solwera, gdzie powinna znajdować się styczność. Z tym wiązaniem można związać dwie elipsy w dwóch miejscach, aby stykały się ze sobą.

### Pomiędzy dwoma liniami *(współliniowe)* 

<img alt="" src=images/Sketcher_ConstraintTangent_mode5.png  style="width   *600px;">

**Akceptowany wybór   ***

-   dowolna linia / wierzchołek + dowolna linia / wierzchołek

## Tworzenie skryptów 

Wiązanie styczności może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następującej funkcji   * 
```python
# direct tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,icurve2))

# point-to-point tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve tangency
Sketch.addConstraint(Sketcher.Constraint('Tangent',icurve1,pointpos1,icurve2))

# tangent-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('TangentViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` gdzie   *

   ** `Sketch` jest obiektem typu szkic

   ** `icurve1`, `icurve2` są dwiema liczbami całkowitymi określającymi krzywe, które mają być styczne. Liczby całkowite to indeksy w szkicu *(wartość zwracana przez`Sketch.addGeometry`)*.

   ** `pointpos1`, `pointpos2` powinny wynosić 1 dla punktu początkowego i 2 dla punktu końcowego.

   ** `geoidpoint` oraz `pointpos` w `TangentViaPoint` są indeksami określającymi punkt styczności.

Strona [Skrypty szkicownika](Sketcher_scripting/pl.md) wyjaśnia wartości, które mogą być używane dla `incurve1`, `incurve2`, `pointpos1`, `pointpos2`, `geoidpoint` i `pointpos`, a także zawiera kolejne przykłady tworzenia wiązań za pomocą skryptów języka Python.





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ConstrainTangent/pl
