# MIBA/pl
## Wprowadzenie

Miba to sposób na osadzenie informacji o przestrzeni 3D w obrazie 2D. Dzięki temu często możliwe jest użycie obrazu 2D zamiast przeglądarki 3D. Dzięki informacji Miba jesteś w stanie obliczyć pozycję miejsca 3D w obrazie 2D. To pozwala na późniejsze ozdobienie obrazu dowolnymi informacjami 3D. Możesz zrobić obraz we wczesnym stanie *(projekt)* i użyć go później *(np. produkcja)*. Nie musisz znać rodzaju danych 3D ani ich pozycji w momencie wykonywania zdjęcia. Zdjęcie jest więc całkowicie oddzielone od danych 3D.

Szczegółową specyfikację można znaleźć na stronie: <http://miba.juergen-riegel.net/>

## Miba w programie FreeCAD 

Jeśli wybierzesz format pliku, który ma możliwość komentowania *(JPG i PNG)* możesz wybrać opcję napisania komentarza lub wstawienia informacji MIBA w pola komentarza *(domyślnie)*:

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Tworzenie obrazów Miba za pomocą skryptu 


```python
import Part,PartGui

# loading test part
Part.open("C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp")

OutDir = "c:/temp/"
Gui.ActiveDocument.ActiveView.setAnimationEnabled(False)

# creating images with different Views, Cameras and sizes
for p in ["PerspectiveCamera", "OrthographicCamera"]:
    Gui.SendMsgToActiveView(p)
    for f in ["ViewAxo", "ViewFront", "ViewTop"]:
        Gui.SendMsgToActiveView(f)
        for x, y in [[500, 500], [1000, 3000], [3000, 1000], [3000, 3000], [8000, 8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".jpg", x, y, "White")
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + "Blade_" + p + "_" + f + "_" + str(x) + "_" + str(y) + ".png", x, y, "Transparent")

# close active document
App.closeDocument(App.ActiveDocument.Name)
```



---
![](images/Button_right.svg) [documentation index](../README.md) > [User_Documentation](Category_User_Documentation.md) > MIBA/pl
