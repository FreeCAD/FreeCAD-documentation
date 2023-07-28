# Sketcher helper constraint/pl
## Przegląd

<img alt="Przykład wiązania pomocniczego *(Constraint5 - punkt na okręgu)* dla wiązania stycznego *(Constraint6 w trybie styczna-przez-punkt)*. W tym przypadku używane jest tylko jedno wiązanie pomocnicze, ponieważ punkt styczności jest punktem końcowym głównej średnicy elipsy, która z natury leży na elipsie." src=images/Sketcher_helper_constraint_example1.png  style="width:500px;">

Wiązanie pomocnicze jest zwykłym wiązaniem szkicownika, które jest potrzebne jako część bardziej złożonego wiązania, ale jest widoczne w interfejsie użytkownika, aby pomóc w radzeniu sobie z redundancją. Na przykład, dla [prawo Snell\'a](Sketcher_ConstrainSnellsLaw/pl.md), dwie linie reprezentujące promienie światła muszą być połączone ([zbieżnością punktów](Sketcher_ConstrainCoincident/pl.md)), a złącze musi leżeć na interfejsie ([Zwiąż punkt na obiekcie](Sketcher_ConstrainPointOnObject/pl.md)).

Wiązania pomocnicze są dodawane automatycznie, gdy są potrzebne. Decyzja o tym, czy są one potrzebne, jest obecnie podejmowana przez ocenę błędu wiązania pomocniczego dla bieżącego stanu geometrii *(może to się zmienić w przyszłych wersjach)*. Jeśli błąd jest wystarczająco mały, wiązanie jest uważane za niepotrzebne i nie jest dodawane. W niektórych przypadkach ta logika może prowadzić do błędów *(wiązanie może zostać spełnione przez przypadek, co może się łatwo zdarzyć, gdy włączona jest funkcja przyciągania siatki szkicownika)*.

Jeśli tak się stanie *(brakuje jakiegoś wiązania pomocniczego, a wymagane warunki nie są spełnione w inny sposób)*, wiązanie złożone zostanie uszkodzone. Wykona ono coś, ale rzeczywiste zachowanie jest niezdefiniowane. Takie uszkodzone wiązanie może być naprawione przez ręczne dodanie brakującego wiązania pomocniczego.

Wiązania pomocnicze są obecnie wymagane dla:

-   [wiązań styczności](Sketcher_ConstrainTangent/pl.md) *(w trybie styczna-przez-punkt, potrzebne są dwa wiązania w punkcie)*,
-   [wiązań prostopadłości](Sketcher_ConstrainPerpendicular/pl.md) *(w trybie prostopadle-przez-punkt, potrzebne są dwa wiązania w punkcie)*,
-   [wiązań kąta](Sketcher_ConstrainAngle/pl.md) *(w trybie kątowym, potrzebne są dwa wiązania w punkcie)*,
-   [wiązań prawa Snell\'a](Sketcher_ConstrainSnellsLaw/pl.md) *(potrzebne są wiązania zbieżności i w punkcie)*.

## Tworzenie skryptów 

Gdy wiązania wymagające elementów pomocniczych są dodawane z poziomu środowiska Python, żadne wiązania pomocnicze nie są dodawane automatycznie. Można odtworzyć automatyczne podejmowanie decyzji przez polecenia UI w skrypcie, testując funkcje, specjalnie dodane w tym celu i używane w procedurach UI: 
```python
Sketch.isPointOnCurve(icurve,x,y)
``` isPointOnCurve sprawdza, czy punkt wirtualny określony przez współrzędne szkicu x,y *(wartości zmiennoprzecinkowe)* spełnia wymogi wirtualnego punktu na obiekcie - tj. leży na krzywej określonej przez indeks krzywej icurve. Zwraca wartość {{True/pl}}, jeśli punkt jest na krzywej, i {{False/pl}}, jeśli tak nie jest.


```python
Sketch.calculateConstraintError(iconstr)
```

CalcConstraintError ocenia funkcję błędu wiązania określonego przez jego indeks iconstr w szkicu. Jeśli w wiązaniu występuje tylko jedna funkcja błędu, zwracaną wartością jest podpisana wartość zwracana przez funkcję błędu. Jeśli z więzem związana jest więcej niż jedna funkcja błędu *(tj. wiązanie usuwa więcej niż jeden stopień swobody)*, zwracaną wartością jest RMS wszystkich funkcji błędu *(zawsze dodatnia)*.



## Wersja

Wiązania pomocnicze zostały wprowadzone w wersji 0.15.4387


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher helper constraint/pl
