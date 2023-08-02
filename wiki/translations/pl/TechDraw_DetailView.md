---
- GuiCommand:
   Name: TechDraw DetailView
   Name/pl: Rysunek Techniczny: Wstaw widok szczegółu
   MenuLocation: Rysunek Techniczny -> Wstaw widok szczegółu
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_View/pl, TechDraw_ProjectionGroup/pl
---

# TechDraw DetailView/pl



## Opis

Narzędzie **Wstaw widok szczegółu** tworzy widok małego obszaru istniejącego widoku.

![](images/ViewDetail.png ) 
*Widok szczegółu z okrągłym polem widoku istniejącego widoku*



## Użycie

-   Wybierz widok na stronie lub w drzewie.
-   Naciśnij przycisk **<img src="images/TechDraw_DetailView.svg" width=16px> '''Wstaw widok szczegółu'''**, aby utworzyć widok szczegółu.
-   W pojawiającym się oknie dialogowym zadania można zdefiniować promień pola widoku, skalę i pozycję widoku. W przypadku tego ostatniego można to zrobić
    -   zmieniając współrzędne
    -   lub naciskając przycisk **Podświetlenie szczegółu**. W tym przypadku granica początku szczegółu jest podświetlona pogrubioną czcionką i etykietą \"przeciągnij\". Kliknij granicę lub etykietę, przytrzymaj przycisk myszy i przeciągnij ją do żądanej pozycji. Na koniec zwolnij przycisk myszy, aby zaakceptować zmianę.

Widok szczegółów może być wyświetlany w okrągłym lub kwadratowym polu widoku. Jest to kontrolowane przez ustawienie [ustawienie](TechDraw_Preferences/pl#Adnotacje.md) **Kształt konturu widoku szczegółu**.



## Właściwości widoku szczegółu 

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Szczegół}}

-    **Widok podstawowy|Link**: Widok, na którym opiera się ten widok szczegółu.

-    **Punkt kotwiczenia|Vector**: Środek widoku szczegółowego w obrębie **Widoku podstawowego**.

-    **Promień|Float**: Rozmiar obszaru w **Widoku podstawowym**, który jest wyświetlany w widoku szczegółów.

-    **Odniesienie|String**: Identyfikator widoku szczegółowego w **Widoku podstawowym**.



## Właściwości widoku bazowego 

Obiekt **Widok szczegółu** dziedziczy wszystkie odpowiednie właściwości widoku określonego jako **Widok bazowy**. We właściwościach tego widoku można zmienić wygląd linii przekroju:

-    **Podświetlenie szczegółu**: Kąt obrotu widoku szczegółowego zgodnie z ruchem wskazówek zegara.

-    **Kolor linii podświetlenia**: Kolor linii dla kształtu konturu. Domyślnym ustawieniem jest ustawienie **Podświetlenie szczegółu** w [TechDraw preferences](TechDraw_Preferences.md).

-    **Styl linii podświetlenia**: Styl linii dla kształtu konturu. Wartość domyślna to **Styl podświetlenia szczegółu** w [ustawieniach](TechDraw_Preferences/pl.md).



## Uwagi

-   [Dobra dyskusja na temat ustawiania kotwicy](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Widok szczegółu** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/pl
