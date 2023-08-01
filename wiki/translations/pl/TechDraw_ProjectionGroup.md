---
- GuiCommand:
   Name:TechDraw ProjectionGroup
   Name/pl:Rysunek Techniczny: Wstaw grupę rzutów
   MenuLocation:Rysunek Techniczny → Widoki → Wstaw grupę rzutów
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Wstaw widok](TechDraw_View/pl.md), [Wstaw widok przekroju](TechDraw_SectionView/pl.md)
---

# TechDraw ProjectionGroup/pl



## Opis

Narzędzie Wstaw grupę rzutów tworzy [rzuty z wielu widoków](https://en.wikipedia.org/wiki/Multiview_projection) jednego lub więcej obiektów 3D. Można również dołączyć izometryczne widoki 4 przednich narożników.

Jeśli chcesz stworzyć tylko jeden widok, nie będzie to korzystne przy użyciu **Grupy rzutów**. Zamiast tego powinieneś użyć narzędzia [Wstaw widok](TechDraw_View/pl.md). Jeśli nie chcesz używać tradycyjnego rzutowania [pierwszy-](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) / [trzeci-kąt Grupy rzutów](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection), powinieneś użyć wielokrotnie narzędzia *([Wstaw widok](TechDraw_View/pl.md))* zamiast **Grupy rzutów**.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Trzy widoki ortogonalne i jeden izometryczny widok na obiekt bryły.*



## Użycie

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). Kierunek ujęcia widoku w oknie [widok 3D](3D_view/pl.md) określa początkowa wartość **Kierunek pierwszy** grupy projekcji *(właściwość **Kierunek** widoku głównego)*.
2.  Wybierz jeden lub więcej obiektów w oknie [Widoku 3D](3D_view/pl.md) lub [Widoku drzewa](Tree_view/pl.md).
3.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w [Widoku drzewa](Tree_view/pl.md).
4.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij w menu przycisk **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> '''Wstaw grupę rzutów'''**.
    -   Wybierz opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ProjectionGroup.svg" width=16px> Wstaw grupę rzutów**.
5.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
6.  Otworzy się panel zadań **Grupa rzutów**.
7.  Wybierz widoki, które mają być wyświetlane w grupie projekcji, a także skalę i inne parametry grupy rzutów.
8.  Naciśnij przycisk **OK**.
9.  Opcjonalnie przesuń grupę rzutów, przeciągając jej środkowy widok.
10. Opcjonalnie przesuń inne widoki grupy projekcji względem widoku głównego, przeciągając je pojedynczo.

![](images/TaskProjGroup.png ) 
*[Panel zadań](Task_panel/pl.md) Grupa projekcji. Pole Rzutowanie wskazuje aktualny kierunek widoku.*



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Źródło|LinkList**: Łącza do obiektów rysunkowych, które mają zostać przedstawione.

-    **XSource|XLinkList**: Łącza do obiektów rysunkowych w pliku zewnętrznym.

-    **Kotwica|Link**: Główny widok w grupie. Zwykle jest to widok z przodu.

-    **Typ rzutowania|Enumeration**: {{Value|Kąt pierwszy}} lub {{Value|Kąt trzeci}}.

Pozostałe właściwości z tej grupy zostały opisane na stronie [Wstaw widok](TechDraw_View/pl#Właściwości.md).


{{TitleProperty|Kolekcja}}

-    **Widoki|LinkList**: Łącza do widoków w tej Grupie rzutów.


{{TitleProperty|Rozmieść}}

-    **Rozmieszczenie automatyczne|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, poszczególne widoki będą rozmieszczane automatycznie. Użyj {{FALSE/pl}}, aby rozmieścić je samodzielnie.

-    **odstęp X|Length**: Poziomy odstęp między widokami przy automatycznym pozycjonowaniu. Należy pamiętać, że Skala i rozmiar innych widoków w grupie również wpływają na odstępy.

-    **odstęp Y|Length**: Pionowy odstęp między widokami przy automatycznym pozycjonowaniu.



### Widok


{{TitleProperty|Podstawa}}

Zapoznaj się również informacjami na stronie [Wstaw widok](TechDraw_View/pl#Ustawienia.md) środowiska Rysunek Techniczny.



## Uwagi

Grupa Rzutów jako całość dziedziczy właściwości X, Y, Typ Skali, Skala i Obrót z widoku podstawowego.

Pojedyncze widoki w grupie dziedziczą wszystkie właściwości widoku części, ale obiekt **Grupa rzutów** kontroluje skalę wszystkich swoich prezentowanych widoków.

Właściwość **Wektor obrotu** poszczególnych widoków w grupie jest przestarzała od wersji **0.19**. Zamiast tego użyj **Kierunek X**.

Należy pamiętać, że w polu środkowym wyświetlany jest bieżący kierunek projekcji widoku głównego. Nie można go użyć do zmiany kierunku.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Nowa grupa rzutów może zostać utworzona za pomocą [makrodefinicji](Macros/pl.md) i z konsoli [Python](Python/pl.md) przy użyciu następujących funkcji:


```python
import FreeCAD as App

doc = App.ActiveDocument
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

group = doc.addObject("TechDraw::DrawProjGroup", "ProjGroup")
page.addView(group)
group.Source = [cyl]
group.ProjectionType = "Third Angle"

front_view = group.addProjection("Front") # First projection will become the Anchor.
group.Anchor.Direction = (0, 1, 0)
group.Anchor.RotationVector = (1, 0, 0)

left_view = group.addProjection("Left")
top_view = group.addProjection("Top")

group.X = page.PageWidth / 2
group.Y = page.PageHeight / 2

doc.recompute()
```

Uwaga: Przed dodaniem rzutów do grupy należy zawsze dodać **Grupę rzutów** do strony {{Incode|page.addView(group)}}. Dzięki temu Grupa rzutów może używać domyślnych wartości parametrów pochodzących ze strony nadrzędnej.





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/pl
