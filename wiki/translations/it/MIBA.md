# MIBA/it


## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

MIBA è un modo per incorporare informazioni sullo spazio 3D in un\'immagine 2D. Sovente, ciò rende possibile utilizzare un\'immagine 2D invece di un visualizzazione 3D.

Con le informazioni MIBA è possibile calcolare la posizione di una collocazione 3D nell\'immagine 2D.

Questo consente di arricchire in un secondo tempo l\'immagine con l\'aggiunta di informazioni 3D arbitrarie (a piacere).

È possibile scattare una foto (salvare immagine) in uno stato di lavoro iniziale (in fase di disegno) e utilizzarla successivamente (ad esempio, in fase di produzione).

Per creare l\'immagine, non è necessario conoscere (o definire) il tipo di dati 3D o la posizione. L\'immagine (ad es. in formato .jpeg o .png) è quindi completamente separata dai dati 3D che sono invece contenuti in una sezione di commento come testo xml.


</div>

Una descrizione dettagliata delle informazioni Miba si può trovare in: <http://miba.juergen-riegel.net/>

## Miba in FreeCAD 


<div class="mw-translate-fuzzy">

## Miba in FreeCAD 

Quando si sceglie di salvare l\'immagine con un formato di file (JPG e PNG) che può contenere un commento è possibile decidere se scrivere un commento personale o inserire le informazioni MIBA nei Campi commento (default):


</div>

<img alt="" src=images/Save_picture.png  style="width:600px;">

## Produrre immagini Miba tramite script 


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

[Category:User\_Documentation](Category:User_Documentation.md)
