---
- GuiCommand:
   Name: TechDraw ExportPageDXF
   Name/pl: Rysunek Techniczny: Wyeksportuj stronę do formatu DXF
   MenuLocation: Rysunek Techniczny - Strona - Wyeksportuj stronę do formatu DXF
   Workbenches: [Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version: 0.18
   SeeAlso: [Wyeksportuj stronę do formatu SVG](TechDraw_ExportPageSVG/pl.md), [DXF](Draft_DXF/pl.md)
---

# TechDraw ExportPageDXF/pl



## Opis

Narzędzie **Wyeksportuj stronę do formatu DXF** zapisuje stronę rysunku jako plik [DXF](DXF/pl.md).



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w oknie [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ExportPageDXF.svg" width=16px> Wyeksportuj stronę do formatu DXF**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Strona → <img src="images/TechDraw_ExportPageDXF.svg" width=16px> Wyeksportuj stronę do formatu DXF**.
    -   Jeśli strona jest wyświetlana w [głównym obszarze widoku](Main_view_area/pl.md): kliknij prawym przyciskiem myszy okno strony i wybierz opcję **Eksportuj do formatu DXF** z menu kontekstowego.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Zostanie otwarte okno dialogowe **Eksportuj stronę do formatu DXF**.
5.  Wybierz lokalizację i nazwę pliku.



## Ograniczenia

-   Wymiary promieniowe i średnicowe będą eksportowane poprawnie tylko wtedy, gdy znajdują się \"wewnątrz\" łuku.
-   Skalowanie nie jest obsługiwane. Plik DXF zostanie narysowany w rzeczywistym rozmiarze tak jak na stronie Rysunku Technicznego.
-   Jednostki nie są obsługiwane. Plik DXF zostanie narysowany w milimetrach *(mm)*. Tekst wymiarów będzie wyświetlany dokładnie tak, jak jest wyświetlany na stronie Rysunku Technicznego.
-   Środowisko Rysunek Techniczny nie może eksportować [obiektów środowiska Rysunek Roboczy](TechDraw_DraftView/pl.md) lub [Architektury](TechDraw_ArchView/pl.md) do DXF. Widoki te są elementami [SVG](SVG/pl.md) generowanymi wewnętrznie przez środowisko pracy [Rysunek Roboczy](Draft_Workbench/pl.md), więc nie ma geometrycznego kształtu do wyeksportowania. Aby wyeksportować widok jako DXF, musi on zostać utworzony za pomocą narzędzia [Wstaw widok](TechDraw_View/pl.md) lub [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md). Na przykład wybierz narzędzie [Płaszczyzna przekroju](Arch_SectionPlane/pl.md) środowiska Architektura, następnie użyj [Widok 2D kształtu](Draft_Shape2DView/pl.md) ze środowiska Rysunek Roboczy, aby utworzyć płaski kształt rzutowania, a następnie użyj [Wstaw widok](TechDraw_View/pl.md) na tym obiekcie. Alternatywnie, wybierz obiekty z widoku drzewa lub widoku 3D i wyeksportuj do DXF za pomocą opcji **Plik → [Eksport](Std_Export/pl.md)**.
-   Blok tytułowy strony jest również szablonem [SVG](SVG/pl.md), więc również nie zostanie wyeksportowany do DXF.
-   Ogólnie rzecz biorąc, Rysunek Techniczny może eksportować do DXF tylko te obiekty, które są obsługiwane przez klasę {{Incode|Import::ImpExpDxfWrite}} modułu [Import Module](Draft_DXF/pl.md).



## Uwagi

-   Ta funkcja eksportuje wersje R12 *(AC1009)* i R14 *(AC1014)* [DXF](DXF/pl.md).
    -   R12 jest starszą, prostszą wersją standardu, ale powinna być czytelna dla większości innych programów.
    -   R14 jest wersją domyślną. Zawiera między innymi obsługę splajnów i elips.
-   Te parametry wpływają na dane wyjściowe:
    -   
        **Przybory → Edycja parametrów → BaseApp/Preferencje/Mod/Import → DxfVersionOut**
        
        . Jest to wartość całkowita. Prawidłowe wpisy to 12 lub 14. Domyślną wartością jest 14.

    -   
        **Przybory → Edycja parametrów → BaseApp/Preferencje/Mod/Import → DiscretizeEllipses**
        
        . Jest to wartość logiczna. Jeśli jest to wartość {{TRUE/pl}}, splajny i elipsy są konwertowane na polilinie. Jeśli jest to wartość {{FALSE/pl}}, splajny i elipsy są zapisywane jako obiekty splajnów i elips. Wartością domyślną jest {{FALSE/pl}}. Jeśli parametr DxfVersionOut ma wartość 12, splajny i elipsy są zawsze konwertowane na polilinie.

    -   
        **Przybory → Edycja parametrów → BaseApp/Preferencje/Mod/Import → maxsegmentlength**
        
        . Jest to wartość zmiennoprzecinkowa. Jeśli splajny i elipsy są konwertowane na polilinie, parametr ten określa długość segmentu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wyeksportuj stronę do formatu DXF** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
TechDraw.writeDXFPage(page,filename)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ExportPageDXF/pl
