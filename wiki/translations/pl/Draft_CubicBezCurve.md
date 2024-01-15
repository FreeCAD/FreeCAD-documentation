---
 GuiCommand:
   Name: Draft CubicBezCurve
   Name/pl: Rysunek Roboczy: Sześcienna krzywa Bézier'a
   MenuLocation: Kreślenie , Narzędzia krzywych Bézier'a , Sześcienna krzywa Bézier'a
   Workbenches: Draft_Workbench/pl, Arch_Workbench/pl
   Version: 0.19
   SeeAlso: Draft_BezCurve/pl, Draft_BSpline/pl
---

# Draft CubicBezCurve/pl



## Opis

Polecenie <img alt="" src=images/Draft_CubicBezCurve.svg  style="width:24px;"> **Sześcienna krzywa Bézier\'a** tworzy [krzywą Béziera](http://en.wikipedia.org/wiki/Bezier_curve) trzeciego stopnia *(wymagane są cztery punkty)*.

Krzywa Béziera jest jedną z najczęściej używanych krzywych w grafice komputerowej. Polecenie to pozwala utworzyć ciągły splajn składający się z kilku segmentów Béziera trzeciego stopnia, w sposób podobny do narzędzia Bézier\'a w [Inkscape](https://inkscape.org/). Ogólną krzywą Béziera dowolnego stopnia można utworzyć za pomocą polecenia [Krzywa Bezier\'a](Draft_BezCurve/pl.md).

Polecenia [Krzywa Bézier\'a](Draft_BezCurve/pl.md) i Sześcienna krzywa Bézier\'a używają **punktów kontrolnych** do zdefiniowania położenia i krzywizny odcinka krzywej. Z kolei polecenie [Krzywa złożona](Draft_BSpline/pl.md) określa **dokładne punkty**, przez które będzie przechodzić krzywa.

<img alt="" src=images/Draft_CubicBezCurve_example.png  style="width:500px;"> 
*Krzywa Spline składająca się z trzech sześciennych segmentów Béziera. Pierwszy segment jest zdefiniowany przez cztery punkty. Kolejne segmenty wykorzystują ponownie dwa punkty z poprzedniego segmentu, a zatem wymagają tylko dwóch dodatkowych punktów.*



## Użycie

Zapoznaj się również z informacjami na stronie: [Tacka narzędziowa](Draft_Tray/pl.md), [Przyciąganie](Draft_Snap/pl.md) oraz [Wiązania](Draft_Constrain/pl.md).

1.  Polecenie można wywołać na kilka sposobów:
    -   Naciśnij przycisk **<img src="images/Draft_CubicBezCurve.svg" width=16px> '''Sześcienna krzywa Béziera'''**.
    -   Wybierz z menu **Kreślenie → Narzędzia krzywych Bézier'a → <img src="images/Draft_CubicBezCurve.svg" width=16px> Sześcienna krzywa Béziera** .
2.  Otworzy się panel zadań **Sześcienna krzywa Béziera**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Nie jest możliwe wprowadzanie punktów za pomocą panelu zadań.
4.  W przypadku następujących modeli [Profil nawigacji myszką](Mouse_navigation/pl.md) należy przytrzymać klawisz klawiatury:
    -   W przypadku korzystania z profilu [OpenInventor](Mouse_navigation/pl#OpenInventor.md) klawisz **Ctrl** musi być wciśnięty przez cały czas trwania polecenia.
    -   Jeśli korzystasz z profilu [Gesture](Mouse_navigation/pl#Gesture.md), klawisz **Alt** musi być wciśnięty dla każdej sekwencji kliknięcia i przytrzymania, ale możliwe jest również trzymanie tego klawisza wciśniętego przez cały czas trwania polecenia.
5.  Wybierz pierwszy punkt w oknie [widoku 3D](3D_view/pl.md) i przytrzymaj przycisk myszki *(1)*, jest to pierwszy punkt końcowy.
6.  Przeciągnij kursor do innego punktu w oknie [widoku 3D](3D_view/pl.md) i zwolnij przycisk myszki *(2)*, jest to pierwszy punkt kontrolny.
7.  Przesuń kursor do innego punktu w oknie [widoku 3D](3D_view/pl.md), wybierz ten punkt i przytrzymaj przycisk myszki *(3)*, jest to drugi punkt końcowy.
8.  Przesuń kursor do innego punktu w oknie [widoku 3D](3D_view/pl.md), aby dostosować końcową krzywiznę segmentu i zwolnij przycisk myszki *(4)*, jest to drugi punkt kontrolny.
9.  Masz teraz jedną krzywą Béziera 3 stopnia.
10. Opcjonalnie można powtórzyć proces klikania i przytrzymywania *(5)* oraz przeciągania i zwalniania *(6)*, aby dodać więcej segmentów.
11. Każdy kolejny segment użyje drugiego punktu końcowego i drugiego punktu kontrolnego poprzedniego segmentu jako odpowiednio pierwszego punktu końcowego i pierwszego punktu kontrolnego.
12. Naciśnij **Esc** lub przycisk **Zamknij**, aby zakończyć polecenie.



## Opcje

Zapoznaj się z informacjami na stronie [Krzywa Bezier\'a](Draft_BezCurve/pl#Options.md).



## Uwagi

-   Sześcienną krzywą Béziera środowiska Rysunek Roboczy można edytować za pomocą polecenia [Edycja](Draft_Edit/pl.md).



## Właściwości

Zapoznaj się z informacjami na stronie [Krzywa Bézier\'a](Draft_BezCurve/pl#Właściwości.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby uzyskać ogólne informacje, zobacz stronę [Krzywa Bézier\'a](Draft_BezCurve/pl.md). Poprzez przekazanie opcji tworzony jest sześcienna krzywa Bézier\'a degree=3 to `makeBezCurve()`.

Dla każdego segmentu krzywej sześciennej Béziera należy użyć czterech punktów, z których dwa skrajne wskazują miejsce, przez które przechodzi krzywizna, a dwa punkty pośrednie są punktami kontrolnymi.

-   Jeżeli podane są tylko trzy punkty, zamiast tego tworzona jest kwadratowa krzywa Béziera z tylko jednym punktem kontrolnym.
-   Jeżeli podane są tylko 2 punkty, tworzona jest liniowa krzywa Béziera, czyli linia prosta.
-   Jeśli podano 5 punktów, pierwsze 4 tworzą sześcienny segment krzywej Béziera, 4. i 5. punkt są używane do utworzenia linii prostej.
-   Jeśli podano 6 punktów, pierwsze 4 tworzą sześcienny odcinek krzywej Béziera, 4. i pozostałe dwa punkty są używane do utworzenia kwadratowego odcinka Béziera.
-   Jeśli podano 7 punktów, pierwsze 4 tworzą sześcienny odcinek krzywej Béziera, czwarty i pozostałe trzy punkty są używane do utworzenia drugiego sześciennego odcinka krzywej Béziera.
-   Ogólnie rzecz biorąc, ostatni punkt w grupie czterech jest dzielony z następującymi maksymalnie trzema punktami, aby utworzyć kolejny segment krzywej Béziera.
-   Aby uzyskać gładkie krzywe, bez prostych segmentów, liczba punktów powinna wynosić `3n + 1` lub `3n`, gdzie `n` jest liczbą segmentów, dla n >= 1.

<img alt="" src=images/Draft_CubicBezCurve_API_example.png  style="width:600px;">



*Przykłady krzywych Béziera utworzonych przy użyciu 2, 3, 4, 5, 6, 7 i 8 punktów. Linie ciągłe oznaczają sześcienne segmenty Béziera. Pozostałe linie są kwadratowe lub proste.*

Przykład:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(-3500, 0, 0)
p2 = App.Vector(-3000, 2000, 0)
p3 = App.Vector(-1100, 2000, 0)
p4 = App.Vector(0, 0, 0)

p5 = App.Vector(1500, -2000, 0)
p6 = App.Vector(3000, -1500, 0)
p7 = App.Vector(5000, 0, 0)
p8 = App.Vector(6000, 1500, 0)
rot = App.Rotation()

c1 = Draft.make_circle(100, placement=App.Placement(p1, rot), face=False)
c1.Label = "B1_E1"
c2 = Draft.make_circle(50, placement=App.Placement(p2, rot), face=True)
c2.Label = "B1_c1"
c3 = Draft.make_circle(50, placement=App.Placement(p3, rot), face=True)
c3.Label = "B1_c2"
c4 = Draft.make_circle(100, placement=App.Placement(p4, rot), face=False)
c4.Label = "B1_E2"
c5 = Draft.make_circle(50, placement=App.Placement(p5, rot), face=True)
c5.Label = "B2_c3"
c6 = Draft.make_circle(50, placement=App.Placement(p6, rot), face=True)
c6.Label = "B2_c4"
c7 = Draft.make_circle(100, placement=App.Placement(p7, rot), face=False)
c7.Label = "B2_E3"
c8 = Draft.make_circle(50, placement=App.Placement(p8, rot), face=True)
c8.Label = "B3_c5"

doc.recompute()

B1 = Draft.make_bezcurve([p1, p2], degree=3)
B1.Label = "B_lin"
B1.ViewObject.DrawStyle = "Dashed"

B2 = Draft.make_bezcurve([p1, p2, p3], degree=3)
B2.Label = "B_quad"
B2.ViewObject.DrawStyle = "Dotted"

B3 = Draft.make_bezcurve([p1, p2, p3, p4], degree=3)
B3.Label = "B_cub"
B3.ViewObject.LineWidth = 4

B4 = Draft.make_bezcurve([p1, p2, p3, p4, p5], degree=3)
B4.Label = "B_cub+lin"
B4.ViewObject.DrawStyle = "Dashed"

B5 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6], degree=3)
B5.Label = "B_cub+quad"
B5.ViewObject.DrawStyle = "Dotted"

B6 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7], degree=3)
B6.Label = "B_cub+cub"
B6.ViewObject.LineWidth = 2

B7 = Draft.make_bezcurve([p1, p2, p3, p4, p5, p6, p7, p8], degree=3)
B7.Label = "B_cub+cub+lin"
B7.ViewObject.DrawStyle = "Dashed"

doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft CubicBezCurve/pl
