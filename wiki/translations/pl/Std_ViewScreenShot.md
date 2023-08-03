---
 GuiCommand:
   Name: Std ViewScreenShot
   Name/pl: Std: Zapisz zrzut ekranu
   MenuLocation: Przybory , Zapisz obrazek ...
   Workbenches: wszystkie
   SeeAlso: Std_Print/pl, Std_PrintPdf/pl, Macro_Copy3DViewToClipboard/pl, Macro_Screen_Wiki/pl, Macro_Snip/pl
---

# Std ViewScreenShot/pl



## Opis

Polecenie **Zapisz obrazek** otwiera okno dialogowe umożliwiające utworzenie pliku graficznego, zrzutu ekranu, z aktywnego okna [widoku 3D](3D_view/pl.md).

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*Okno dialogowe '''Zapisz obraz''' po naciśnięciu przycisku ''Rozszerz''.*



## Użycie

1.  Wybierz z menu opcję **Przybory → <img src="images/Std_ViewScreenShot.svg" width=16px> Zapisz obrazek...**.
2.  Zostanie otwarte okno dialogowe Zapisz obrazek.
3.  Opcjonalnie naciśnij przycisk **Rozszerz**, aby wyświetlić dodatkowy panel w oknie dialogowym. Więcej informacji znajdziesz w sekcji [Opcje](#Opcje.md).
4.  Ewentualnie przejdź do właściwego folderu.
5.  Wprowadź nazwę pliku i wybierz jego typ.
6.  Naciśnij przycisk **Zapisz**, aby utworzyć plik obrazu i zamknąć okno dialogowe.



## Opcje



### Rozmiar obrazu 

1.  Wybierz rozmiar standardowy z listy rozwijanej **Rozmiary standardowe**. Lub określ **Szerokość** i **Wysokość** dla rozmiaru niestandardowego.
2.  Opcjonalnie naciśnij przycisk **Proporcje obrazu**, aby ustawić stosunek szerokości do wysokości obrazu. Jeśli pole wejściowe **Szerokość** jest aktywne, wysokość obrazu zostanie zmieniona i na odwrót.



### Właściwości obrazu 

1.  Wybierz opcję z listy rozwijanej **Tło**:
    -   
        {{Value|Bieżące}}
        
        Ta opcja wykorzystuje tło widoku 3D.

    -   
        {{Value|Białe}}
        

    -   
        {{Value|Czarne}}
        

    -   
        {{Value|Przezroczyste}}
        
        Nie wszystkie formaty obrazów obsługują przezroczystość.
2.  Wybierz opcję z listy rozwijanej **Metoda tworzenia**:
    -   
        {{Value|Pozaekranowy (Nowy)}}
        
        Jest to metoda domyślna. Ta metoda obsługuje [antyaliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *\'Informacje techniczne: Najważniejszymi klasami dla tej metody są Qt\'s QOffscreenSurface i QOpenGLFramebufferObject.*

    -   
        {{Value|Pozaekranowy (Stary)}}
        
        Ta metoda nie działa w wielu nowoczesnych systemach Linux, ponieważ opiera się na sterowniku graficznym. Metoda ta nie obsługuje antyaliasingu. *Informacje techniczne: Jest to prawdziwa metoda renderowania poza ekranem, która wykorzystuje tylko funkcje z biblioteki Coin3d.*

    -   
        {{Value|Bufor ramki (standardowy)}}
        
        Ta metoda obsługuje antyaliasing. *Informacje techniczne: Jeśli antyaliasing jest wyłączony, metoda ta wczytuje obraz bezpośrednio z renderera grafiki, w przeciwnym razie renderuje do bufora ramki i stamtąd pobiera obraz. Kluczową częścią tej metody jest klasa QOpenGLFramebufferObject firmy Qt.*

    -   
        {{Value|Bufor ramki (jak jest)}}
        
        Metoda ta wykorzystuje te same techniki co **Bufor ramki (standardowy)**. Obsługuje ona również antyaliasing, ale ma pewne ograniczenia związane z niestandardowymi rozmiarami i zawsze używa bieżącego tła widoku 3D.



### Komentarz do obrazka 

1.  Wybierz opcję {{RadioButton|TRUE|Wstaw MIBA}}, aby dodać informacje [MIBA](MIBA.md) do pliku. Nie wszystkie formaty obrazów to obsługują.
2.  Lub wybierz opcję {{RadioButton|TRUE|Wstaw komentarz}} i wpisz komentarz w polu tekstowym, aby osadzić komentarz w pliku. Nie wszystkie formaty obrazów obsługują tę funkcję.
3.  Zaznacz pole wyboru {{CheckBox|TRUE|Dodaj znak wodny}}, aby dodać znak wodny. Znak wodny jest umieszczany w lewym dolnym rogu obrazu i zawiera logo i nazwę programu FreeCAD nad głównym adresem URL programu FreeCAD: [www.freecadweb.org](http://www.freecadweb.org).



## Uwagi

-   Liczba dostępnych formatów plików graficznych może się różnić w zależności od systemu operacyjnego.
-   Niektóre sterowniki OpenGL nie zezwalają na renderowanie obrazów powyżej pewnego maksymalnego rozmiaru.



## Ustawienia

-   Tło widoku 3D można zmienić w preferencjach: **Edycja → Preferencje ... → Wyświetlanie → Kolory → Kolor tła**. Zobacz także [Edytor ustawień](Preferences_Editor/pl#Kolory.md).
-   Aby zmienić antyaliasing widoku 3D: **Edycja → Preferencje ... → Wyświetlanie → Widok 3D → Renderowanie → Wygładzanie**. Zobacz także [Edytor ustawień](Preferences_Editor/pl#Widok_3D.md).



## Tworzenie skryptów 

Istnieje możliwość tworzenia zrzutów ekranu za pomocą kodu środowiska Python.


```python
Gui.ActiveDocument.ActiveView.saveImage('C:/temp/test.png',1656,783,'Current')
```

Ten skrypt zapisuje serię zrzutów ekranu o różnych rozmiarach i z różnych kierunków. Zmieniany jest także typ ujęcia widoku - ortograficzny lub perspektywiczny.


```python
import Part, PartGui
# Loading test part
Part.open('C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp')
OutDir = 'C:/temp/'
 
# Creating images with different Views, Cameras and sizes
for p in ['PerspectiveCamera','OrthographicCamera']:
    Gui.SendMsgToActiveView(p)
    for f in ['ViewAxo','ViewFront','ViewTop']:
        Gui.SendMsgToActiveView(f)
        for x,y in [[500,500],[1000,3000],[3000,1000],[3000,3000],[8000,8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.jpg',x,y,'White')
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.png',x,y,'Transparent')

# Close active document
App.closeDocument(App.ActiveDocument.Name)
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewScreenShot/pl
