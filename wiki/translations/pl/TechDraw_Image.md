---
 GuiCommand:
   Name: TechDraw Image
   Name/pl: Rysunek Techniczny: Wstaw obraz bitmapy
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw obraz bitmapy
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_Symbol/pl
---

# TechDraw Image/pl



## Opis

Narzędzie **Wstaw obraz bitmapy** wstawia z pliku do strony widok obrazu [bitmapy](Bitmap/pl.md) *(PNG, TIFF, JPEG itp.)*.

![](images/TechDraw_Image_example.png ) 
*Obraz wstawiony do strony rysunku.*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w [Widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_Image.svg" width=16px> '''Wstaw obraz bitmapy'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki → <img src="images/TechDraw_Image.svg" width=16px> Wstaw obraz bitmapowy**.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Zostanie otwarte okno dialogowe pliku.
5.  Wybierz lokalizację i nazwę pliku.
6.  Obraz zostanie wstawiony.
7.  Opcjonalnie można zmienić jego właściwość **Skala**, aby dostosować jego rozmiar.



## Właściwości

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Obraz}}

-    **Plik obrazu|File**: Plik zawierający tę bitmapę.

-    **Obraz dołączony|FileIncluded**: Wbudowany plik graficzny. Tylko do użytku systemowego.

-    **Szerokość|Float**: Szerokość wykadrowanego obrazu w mm. Używane tylko wtedy, gdy **Przytnij** ma wartość {{TRUE/pl}}.

-    **Wysokość|Float**: Wysokość wykadrowanego obrazu w mm. Analogicznie.



### Widok


{{TitleProperty|Obraz}}

-    **Przytnmij|Bool**: Przycina obraz do parametrów **Szerokość** x **Wysokość**.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Obraz może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dvi = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewImage','TestImage')
rc = page.addView(dvi)
dvi.ImageFile = "pathToMy/imageFile.png"
dvi.Height = 200
dvi.Width  = 200
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Image/pl
