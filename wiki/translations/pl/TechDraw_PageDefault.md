---
- GuiCommand:
   Name:TechDraw PageDefault
   Name/pl:Rysunek Techniczny: Wstaw nową domyślna stronę rysunku
   MenuLocation:Rysunek Techniczny → Wstaw nową domyślna stronę rysunku
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Wstaw nową domyślna stronę rysunku](TechDraw_PageTemplate/pl.md), [Szablony](TechDraw_Templates/pl.md)
---

# TechDraw PageDefault/pl

## Opis

Narzędzie **Wstaw nową domyślna stronę rysunku** tworzy nowy obiekt Strony używając pliku szablonu określonego w [Ustawieniach](TechDraw_Preferences/pl.md) dla środowiska pracy Rysunek Techniczny.

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Domyślny szablon dołączony do środowiska pracy Rysunek Techniczny: Strona A4 w orientacji poziomej, z edytowalnymi polami tekstowymi*

## Użycie

-   Naciśnij przycisk **<img src="images/TechDraw_PageDefault.svg" width=16px> [Wstaw nową domyślna stronę rysunku](TechDraw_PageDefault/pl.md)** *(Musi istnieć aktywny dokument)*.

## Uwagi

-   Jeśli strona jest oznaczona jako \"nie aktualizuj\" poprzez właściwość K*Utrzymuj aktualizację* lub ustawienie w Preferencjach, będzie ona ignorować zmiany w modelu 3D. Możesz zauważyć anomalie *(brakująca geometria, brakujące wartości wymiarów, itp.)* w wyglądzie strony. Poprawią się one po aktualizacji Strony za pomocą narzędzia [Przerysuj stronę](TechDraw_RedrawPage/pl.md). Strona będzie miała tę ikonę <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> w drzewie podczas zawieszenia aktualizacji. To ustawienie wpływa również na proces uruchamiania. Jeśli strona jest zaznaczona jako \"nie aktualizuj\" nie będzie rysowana przy starcie programu.

-   Jeśli domyślny szablon nie został określony w pliku konfiguracyjnym użytkownika `user.cfg`, narzędzie spróbuje:

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    

\" Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład:

:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    

## Właściwości

### Dane


{{TitleProperty|Podstawowe}}

-    **Typ projekcji**: Domyślny typ projekcji *(kąt pierwszy lub trzeci)* dla tej strony.


{{TitleProperty|Strona}}

-    **Utrzymuj aktualizację**: Jeśli opcja przyjmuje wartość {{false/pl}}, Strona nie jest aktualizowana o zmiany w modelu 3D. Przydatne dla skomplikowanych/wolnych rysunków. Zobacz uwagi.

-    **Szablon**: Link do obiektu [szablonu](TechDraw_Templates/pl.md) tej Strony.

-    **Widoki**: Lista linków do Widoków na tej Stronie.

-    **Skala**: Domyślna skala dla Widoków na tej Stronie.

-    **Następny numer dymka**: Autonumeracja dla dymków.

### Widok


{{TitleProperty|Siatka}}

-    **Pokaż siatkę**: Pokaż siatkę na Stronie. {{Version/pl|0.20}}

-    **Rozstaw siatki**: Odległość między liniami siatki w mm. {{Version/pl|0.20}}

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wstaw nową domyślna stronę rysunku może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji: 
```python
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Tworzy nową stronę w bieżącym dokumencie

### Pola tekstowe do edycji 


**Zobacz również:**

[Rysunek Techniczny: Szablony](TechDraw_Templates/pl.md) aby uzyskać więcej informacji na temat tworzenia szablonów.

Po utworzeniu nowej strony, jej atrybut `Template` przechowuje słownik `EditableTexts` zawierający nazwy edytowalnych pól *(klucze)* i ich wartości tekstowe. Skopiuj ten słownik do zmiennej, wprowadź zmiany, a następnie ponownie przypisz słownik do atrybutu `EditableTexts`, aby zobaczyć zmiany.


```python
page = FreeCAD.ActiveDocument.Page
texts = page.Template.EditableTexts

for key, value in texts.items():
    print("{0} = {1}".format(key, value))

texts["FC-Title"] = "The title of my page"
page.Template.EditableTexts = texts
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/pl
