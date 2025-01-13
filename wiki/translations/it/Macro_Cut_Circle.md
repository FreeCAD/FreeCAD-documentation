# Macro Cut Circle/it
{{Macro/it
|Name=Macro Cut Circle
|Translate=Taglia Cerchio
|Description=Taglia cerchi o archi in più archi. Gli archi creati possono essere colorati alternativamente per distinguerli.<br/>{{ColoredText|(Riga di comando, incolla la macro completa nella console Python)}}.
|Author=mario52
|Version=00.03
|Date=2019-07-02
|Download=[https://wiki.freecad.org/images/9/93/Macro_Cut_Circle.png ToolBar Icon]
}}



## Descrizione

Questa macro taglia cerchi o archi in più archi. Gli archi creati possono essere colorati alternativamente per distinguerli.

<img alt="" src=images/Macro_CutCircle_00.png  style="width:400px;"> 
*CutCircle*



## Utilizzo

1.  Incollare la macro **cutCircle** nella [Console Python](Python_console/it.md).
2.  Premere **Enter** (il codice è ora in memoria).
3.  Selezionare uno o più cerchi o archi.
4.  Invocare la funzione {{Incode|cutCircle()}} con 1 o 2 argomenti dalla console Python:
    -   Esempio con 1 argomento: {{Incode|cutCircle(4)}}. Questo creerà 4 nuovi archi per ogni cerchio o arco selezionato e si fermerà lì (nessuna colorazione).
    -   Esempio con 2 argomenti: {{Incode|cutCircle(6, 1)}}. Questo creerà 6 nuovi archi per ciascun cerchio o arco selezionato, colorati alternativamente in rosso e bianco come mostrato nell\'immagine.
5.  L\'oggetto originale non viene eliminato.

## Script

Icona della barra degli strumenti ![](images/Macro_Cut_Circle.png )

**Macro_Cut_Circle.FCMacro**


{{MacroCode|code=

# selection circle(s) (circles and arcs)
# give number of cut, biColor 0/1
# cut the circle to x arcs
# if biColor is <> 0 the arcs are colored alternately Red White Red White ....
# 
 
__title__   = "cutCircle"
__author__  = "Mario52"
__date__    = "02/07/2019"
__version__ = "00.03"

import Draft
global biscolor ; biscolor = 0
def cutCircle(number = 2, biColor = 0):
    global biscolor
    def defbiColor(objet):
        global biscolor
        if biscolor == 0:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,0.0,0.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 1
        else:
            FreeCADGui.ActiveDocument.getObject(objet.Name).LineColor = (1.0,1.0,1.0) # 255 = 1 (10 = (1/255 * 10 ))
            biscolor = 0
    selection = FreeCADGui.Selection.getSelection()
    for piece in selection:
        nom = piece.Name
        if (nom[:6] == "Circle") or (nom[:8] == "Cylinder"):
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
 
            if (nom[:8] == "Cylinder"):
                pivot0 = float(piece.Angle/number)
                FreeCAD.Console.PrintMessage("Cylinder"+"\n")
            else:
                pivot0 = float(360/number)
                FreeCAD.Console.PrintMessage("Circle"+"\n")
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1),endangle=(pivot0+pivot1),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
        elif nom[:3] == "Arc":
            FreeCAD.Console.PrintMessage("Arc"+"\n")
            circonference = piece.Shape.Length
            rayon = piece.Radius
            placem = piece.Placement
            First = float(piece.FirstAngle)
            Last  = float(piece.LastAngle)
            pivot0 = abs((First - Last) / number)
            pivot1 = 0.0
            for i in range(number):
                cercle = Draft.makeCircle(radius=rayon,placement=placem,face=False,startangle=(pivot1+First),endangle=(pivot0+pivot1+First),support=None)
                if biColor != 0:
                    defbiColor(cercle)
                pivot1 += pivot0
    App.ActiveDocument.recompute()

#cutCircle(5, 1)  # here with 5 arcs and colored
#cutCircle(4)     #

}}



## Esempio


```python
cutCircle(5, 1)  # here with 5 arcs and colored
cutCircle(4)     #
```



## In progetto 

Tagliare il cerchio in cilindro



## Versione

ver 00.03 02/07/2019 : aggiunto \"App.ActiveDocument.recompute()\"

ver 00.02 03/09/2015 : aggiunta la creazione di archi colorati alternativamente Rosso Bianco Rosso Bianco \.... oppure no

ver 00.01 24/02/2015 :



---
⏵ [documentation index](../README.md) > Macro Cut Circle/it
