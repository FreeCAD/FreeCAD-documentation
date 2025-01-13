---
 GuiCommand:
   Name: TechDraw ProjectionGroup
   Name/pl: Rysunek Techniczny: Wstaw grupę rzutów
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw grupę rzutów
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_View/pl
---

# TechDraw ProjectionGroup/pl



## Opis

Narzędzie Wstaw grupę rzutów tworzy [rzuty z wielu widoków](https://en.wikipedia.org/wiki/Multiview_projection) jednego lub więcej obiektów 3D, używając tradycyjnego [rzutowania metodą pierwszego kąta (europejskiego)](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) lub [rzutowania metodą trzeciego kąta (amerykańskiego)](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection). Można również dołączyć izometryczne widoki 4 przednich narożników.


{{Version/pl|1.0}}

: Narzędzie [Wstaw widok](TechDraw_View/pl.md) również może utworzyć grupę rzutów. Zalecane jest używanie tamtego narzędzia.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Trzy widoki ortogonalne i jeden izometryczny widok na obiekt bryły.*



## Użycie

Zobacz stronę [Wstaw widok](TechDraw_View/pl#Usage_Projection_Group_Item_and_Projection_Group.md), ale do wywołania narzędzia wybierz opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ProjectionGroup.svg" width=16px> Wstaw grupę rzutów** z menu.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Grupa rzutów, formalnie obiekt {{Incode|TechDraw::DrawProjGroup}} ma [właściwości](TechDraw_View/pl#Właściwości_-_Widok_części.md) wspólne dla wszystkich typów Widoków. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Podstawa}}

-    **Źródło|LinkList**: Łącza do obiektów rysunkowych, które mają zostać przedstawione.

-    **XSource|XLinkList**: Łącza do obiektów rysunkowych w pliku zewnętrznym.

-    **Kotwica|Link**: Główny widok w grupie. Zwykle jest to widok z przodu.

-    **Typ rzutowania|Enumeration**: {{Value|Kąt pierwszy}} lub {{Value|Kąt trzeci}}.


{{TitleProperty|Kolekcja}}

-    **Widoki|LinkList**: Łącza do widoków w tej Grupie rzutów.


{{TitleProperty|Rozmieść}}

-    **Rozmieszczenie automatyczne|Bool**: Jeśli opcja ma wartość {{TRUE/pl}}, poszczególne widoki będą rozmieszczane automatycznie. Użyj {{FALSE/pl}}, aby rozmieścić je samodzielnie.

-    **odstęp X|Length**: Poziomy odstęp między widokami przy automatycznym pozycjonowaniu. Należy pamiętać, że Skala i rozmiar innych widoków w grupie również wpływają na odstępy.

-    **odstęp Y|Length**: Pionowy odstęp między widokami przy automatycznym pozycjonowaniu.



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





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/pl
