---
- GuiCommand   *
   Name   *TechDraw ToggleFrame
   Name/pl   *Rysunek Techniczny   * Włącz / wyłącz wyświetlanie ramek
   MenuLocation   *Rysunek Techniczny → Włącz / wyłącz wyświetlanie ramek
   Workbenches   *[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso   *[Widok](TechDraw_View/pl.md), [Grupa rzutów](TechDraw_ProjectionGroup/pl.md)
---

# TechDraw ToggleFrame/pl

## Opis

Narzędzie **Włącz / wyłącz wyświetlanie ramek** włącza lub wyłącza wyświetlanie ramek w oknie widoku, etykiet oraz wierzchołków.

<img alt="" src=images/TechDraw_ToggleFrame.png  style="width   *400px;"> 
*Widok rzutu bryły z włączonymi i wyłączonymi ramkami.*

## Użycie

1.  Jeśli masz wiele stron rysunków w swoim dokumencie, będziesz musiał wybrać odpowiednią stronę w drzewie.
2.  Naciśnij przycisk **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md)**.
3.  Jeśli ramki widoku są aktualnie wyświetlane, znikną. Jeśli ramki widoku są ukryte, zostaną wyświetlone.
4.  Możliwe jest, aby różne widoki były wyświetlane w różnych trybach. Jeśli tak się stanie, naciśnij przycisk **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md)** raz lub dwa razy, aby zsynchronizować widoki.

## Kontekst

Kropkowana ramka widoku i punkty wierzchołków służą jedynie do celów poglądowych, nie są w rzeczywistości częścią rysunku, więc nie będą widoczne po wyeksportowaniu strony do formatu PDF lub SVG.

Sugerowany sposób działania to użycie narzędzia **<img src="images/TechDraw_ToggleFrame.svg" width=16px> [Włącz / wyłącz wyświetlanie ramek](TechDraw_ToggleFrame/pl.md)**, aby ukryć widoczność ramki otaczającej widok, a także dodatkowych punktów. Przy użyciu punktów, użyj narzędzi pomiarowych, aby wybrać odpowiednie krawędzie do pomiaru, a następnie wyłącz widoczność ramek *(i wierzchołków)*, aby zobaczyć efekt końcowy. Nie jesteś zadowolony? Ponownie włącz widoczność ramki *(i wierzchołków)*, wybierz inne wierzchołki i utwórz nowe pomiary, a następnie ponownie wyłącz widoczność ramki.

Rozmiar punktów wierzchołków można dostosować w zakładce [skala](TechDraw_Preferences/pl#Skala.md). Nie należy ustawiać wartości ich rozmiaru na zero, a jedynie na tyle mały lub duży, aby wygodnie było je zaznaczać.

## Tworzenie skryptów 


**Zobacz również   ***

[TechDraw API](TechDraw_API.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie te nie jest obecnie wyposażone w interfejs programistyczny.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ToggleFrame/pl
