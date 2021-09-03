---
- GuiCommand:/pl
   Name:Sketcher ConstrainPerpendicular
   Name/pl:Szkicownik: Wiązanie prostopadłości
   MenuLocation:Sketch → Wiązania Szkicownika → Wiązanie prostopadłości
   Workbenches:[Szkicownik](Sketcher_Workbench/pl.md)
   Shortcut:**N**
   SeeAlso:[Szkicownik: Wiązanie kąta](Sketcher_ConstrainAngle/pl.md)
---

## Opis

Wiązanie prostopadłości tworzy dwie linie, które są prostopadłe *(tzn. ortogonalne)* do siebie, lub dwie krzywe, które są prostopadłe na ich przecięciu. Linie są traktowane jako nieskończone, a łuki są traktowane jako pełne okręgi/elipsy. Wiązanie może również łączyć dwie krzywe, wymuszając ich prostopadłość w miejscu połączenia, podobnie jak w przypadku **<img src=images/Sketcher_ConstrainTangent.svg style="width:16px"> [Wiązanie styczności](Sketcher_ConstrainTangent/pl.md)**.

## Użycie

Istnieją cztery różne sposoby zastosowania tego wiązania:

1.  pomiędzy dwoma krzywymi *(dostępne nie dla wszystkich krzywych)*,
2.  pomiędzy dwoma punktami końcowymi krzywej,
3.  pomiędzy krzywą a punktem końcowym innej krzywej,
4.  pomiędzy dwoma krzywymi w punkcie zdefiniowanym przez użytkownika.

Aby zastosować wiązanie prostopadłości, należy wykonać następujące czynności:

-   Wybierz dwie lub trzy pozycje na szkicu.
-   Wywołaj wiązanie, klikając jego ikonę na pasku narzędzi, wybierając element menu lub używając skrótu klawiaturowego.

### Pomiędzy dwoma krzywymi *(prostopadłość bezpośrednia)* 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode1.png  style="width:600px;">

Dwie krzywe zostaną wykonane prostopadle w punkcie ich przecięcia *(rzeczywiste lub przedłużenia krzywych)*, a punkt przecięcia będzie domyślny. Tryb ten jest stosowany, jeśli zostały wybrane dwie krzywe.

**Zaakceptowany wybór:**

-   linia + linia, koło, łuk
-   okrąg, łuk + okrąg, łuk

Jeśli bezpośrednia prostopadłość między wybranymi łukami nie jest obsługiwana (np. między linią a elipsą), do szkicu zostanie automatycznie dodany punkt pomocniczy i zastosowany zostanie punkt prostopadły-przejściowy.

W przeciwieństwie do styczności, rekonstrukcja punktu prostopadłości przez utworzenie punktu i związanie jego położenia na obu łukach *(ograniczając w ten sposób punkt do punktu przecięcia)* jest całkowicie poprawna.

### Między dwoma punktami końcowymi *(prostopadłość między punktami)* 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode2.png  style="width:600px;">

W tym trybie zbierzne są punkty końcowe, a połączenie jest wykonane pod kątem prostym. Tryb ten jest stosowany, gdy wybrane zostały dwa punkty końcowe dwóch krzywych.

\"Zaakceptowany wybór:

-   punkt końcowy linii/łuku/łuku-ellipsy + punkt końcowy linii/łuku/łuku-ellipsy *(tj. dwa punkty końcowe dowolnych dwóch krzywych)*

### Między krzywą a punktem końcowym *(prostopadłość punktu do krzywej)* 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode3.png  style="width:600px;">

W tym trybie, punkt końcowy jednej krzywej jest związany z położeniem na drugiej, a krzywe są ustawione prostopadle do punktu. Tryb ten jest stosowany, gdy zostały wybrane krzywa i punkt końcowy innej krzywej.

**Zaakceptowany wybór:**

-   linia, okrąg, łuk, elipsa, łuk elipsy + punkt końcowy linii/łuku/łuku elipsy *(tzn. każda krzywa + punkt końcowy każdej krzywej)*.

### Pomiędzy dwoma krzywymi w punkcie *(prostopadłym do punktu) (v0.15)* 

<img alt="" src=images/Sketcher_ConsraintPerpendicular_mode4.png  style="width:600px;">

W tym trybie, dwie krzywe są wykonane prostopadle, a punkt prostopadłości znajduje się na trasie. Tryb ten jest stosowany w przypadku wybrania dwóch krzywych i punktu.

**Zaakceptowany wybór:**

-   każda linia/krzywizna + każda linia/krzywizna + każdy punkt

\"Każdy punkt\" może być samotnym punktem, albo punktem jakiegoś obiektu, np. środkiem okręgu, punktem końcowym łuku, albo początkiem.

Aby wiązanie działało prawidłowo, punkt musi znajdować się na obu krzywych. Tak więc, w miarę wywoływania wiązania, punkt będzie automatycznie związany z obiema krzywymi *([wiązanie pomocnicze](Sketcher_helper_constraint.md) zostanie dodane, jeśli jest to konieczne)*, a krzywe zostaną wymuszone w punkcie prostopadłym. Te [wiązania pomocnicze](Sketcher_helper_constraint.md) są zwykłymi regularnymi wiązaniami. Mogą być dodane ręcznie lub usunięte.

W porównaniu do trybu bezpośredniego prostopadłego, to wiązanie jest wolniejsze, ponieważ istnieją stopnie swobody, ale obsługuje elipsy.

Umieszczenie punktu przed zastosowaniem wiązania jest wskazówką dla rozwiązania, które określa, gdzie powinna znajdować się prostopadłość.

## Tworzenie skryptów 

Ograniczenie prostopadłe może być utworzone przez [makropolecenie](Macros/pl.md) i z konsoli Pyton za pomocą następujących narzędzi: 
```python
# direct perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,icurve2))

# point-to-point perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2,pointpos2))

# point-to-curve perpendicularity
Sketch.addConstraint(Sketcher.Constraint('Perpendicular',icurve1,pointpos1,icurve2))

# perpendicular-via-point (plain constraint, helpers are not added automatically)
Sketch.addConstraint(Sketcher.Constraint('PerpendicularViaPoint',icurve1,icurve2,geoidpoint,pointpos)) 
``` Gdzie:

:\* `Sketch` jest obiektem szkicu

:\* `icurve1`, `icurve2` są dwiema liczbami całkowitymi określającymi krzywe, które mają być wykonane prostopadle. Liczby całkowite są indeksami w szkicu *(wartość zwracana przez Sketch.addGeometry)*.

:\* `pointpos1`, `pointpos2` powinny mieć wartość `1` dla punktu początkowego i `2` dla końcowego.

:\* `geoid point` i `pointpos` w PerpendicularViaPoint są indeksami określającymi punkt prostopadłościanu.

Strona [skrypty szkicownika](Sketcher_scripting.md) wyjaśnia wartości, które mogą być użyte do `icurve1`, `icurve2`, `pointpos1`, `pointpos2` i `geoidpoint`, i zawiera dalsze przykłady, jak tworzyć wiązania ze skryptów Python.





{{Sketcher Tools navi

}}  
