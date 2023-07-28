---
- GuiCommand:
   Name:TechDraw ToggleFrame
   Name/pl:Rysunek Techniczny: Włącz / wyłącz wyświetlanie ramek
   MenuLocation:Rysunek Techniczny → Widoki → Włącz / wyłącz wyświetlanie ramek
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Wstaw widok](TechDraw_View/pl.md), [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md)
---

# TechDraw ToggleFrame/pl



## Opis

Narzędzie **Włącz / wyłącz wyświetlanie ramek** włącza lub wyłącza wyświetlanie ramek w oknie widoku, etykiet oraz wierzchołków.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width:400px;"> 
*Widok rzutu bryły z włączonymi i wyłączonymi ramkami.*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w oknie [widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ToggleFrame.svg" width=16px> '''Włącz / wyłącz wyświetlanie ramek'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ToggleFrame.svg" width=16px> Włącz / wyłącz wyświetlanie ramek**.
    -   Jeśli strona jest wyświetlana w [głównym obszarze widoku](Main_view_area.md): kliknij prawym przyciskiem myszk na oknie strony i wybierz opcję **Włącz / wyłącz wyświetlanie ramek** z menu podręcznego.
3.  Jeśli w dokumencie znajduje się wiele stron rysunków, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Aktualnie widoczne ramki widoku znikną. Pojawią się aktualnie niewidoczne ramki widoku.
5.  Różne widoki mogą znajdować się w różnych trybach wyświetlania ramek. Jeśli tak się stanie, wywołaj to narzędzie raz lub dwa razy, aby ponownie zsynchronizować widoki.



## Kontekst

Kropkowana ramka widoku i punkty wierzchołków służą jedynie do celów poglądowych, nie są w rzeczywistości częścią rysunku, więc nie będą widoczne po wyeksportowaniu strony do formatu PDF lub SVG.

Sugerowany sposób działania to użycie narzędzia **<img src="images/TechDraw_ToggleFrame.svg" width=16px> '''Włącz / wyłącz wyświetlanie ramek'''**, aby ukryć widoczność ramki otaczającej widok, a także dodatkowych punktów. Przy użyciu punktów, użyj narzędzi pomiarowych, aby wybrać odpowiednie krawędzie do pomiaru, a następnie wyłącz widoczność ramek *(i wierzchołków)*, aby zobaczyć efekt końcowy. Nie jesteś zadowolony? Ponownie włącz widoczność ramki *(i wierzchołków)*, wybierz inne wierzchołki i utwórz nowe pomiary, a następnie ponownie wyłącz widoczność ramki.

Rozmiar punktów wierzchołków można dostosować w zakładce [skala](TechDraw_Preferences/pl#Skala.md). Nie należy ustawiać wartości ich rozmiaru na zero, a jedynie na tyle mały lub duży, aby wygodnie było je zaznaczać.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie te nie jest obecnie wyposażone w interfejs programistyczny.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/pl
