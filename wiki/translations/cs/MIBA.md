

## Introduction


<div class="mw-translate-fuzzy">

## Úvod

Miba je způsob jak vložit informace o 3D prostoru do 2D obrázku. Často se to realizuje použitím 2D obrázků místo 3D prohlížeče. Pomocí Miba informací jste schopni vypočítat pozici 3D umístění ve 2D obrazu. To Vám umožňuje později doladit obraz libovolnými 3D informacemi. Můžete vzít obraz v ranném stádiu (plán) a použít jej později (např. výroba). Nemusíte znát druh 3D dat nebo pozici, když berete obraz. Takže obraz je kompletně oddělen od dat.


</div>

Detailnější specifikaci můžete nalézt zde: <http://miba.juergen-riegel.net/>

## Miba in FreeCAD {#miba_in_freecad}


<div class="mw-translate-fuzzy">

## Miba ve FreeCADu {#miba_ve_freecadu}

Jestliže si vyberete souborový formát, který umožňuje komentáře ( JPG and PNG), můžete do komentářových polí zapsat komentář nebo vložit MIBA informace (default):


</div>

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Vytváření Miba obrázků skriptem {#vytváření_miba_obrázků_skriptem}


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

[Category:User\_Documentation{{\#translation:}}](Category:User_Documentation.md)
