---
- GuiCommand:
   Name:TechDraw GeometricHatch
   Name/it:Tratteggio geometrico
   MenuLocation:TechDraw - Tratteggio geometrico
   Workbenches:[TechDraw](TechDraw_Workbench/it.md)
   SeeAlso:[Tratteggio da modello](TechDraw_Hatch/it.md), [Tipi di tratteggio](TechDraw_Hatching/it.md)
---

# TechDraw GeometricHatch/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento Tratteggio geometrico riempie una regione chiusa in una vista con un modello basato su una specifica di tratteggio PAT AutoDesk. **In alternativa**, lo strumento [Tratteggio da modello](TechDraw_Hatch/it.md) utilizza un file [SVG](SVG/it.md) o [bitmap](bitmap/it.md) come modello di tratteggio, vedere i [tipi di tratteggio](TechDraw_Hatching/it.md) per i dettagli.


</div>

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Esempio di tratteggio geometrico su una faccia*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare una regione chiusa in una vista.
2.  Premere il pulsante **<img src="images/TechDraw_GeometricHatch.svg" width=16px> [Tratteggio geometrico](TechDraw_GeometricHatch/it.md)
**
3.  Si apre una finestra di dialogo in cui è possibile selezionare il motivo, una scala per il motivo, uno spessore di linea e il colore.


</div>



## Note


<div class="mw-translate-fuzzy">

-   Il tratteggio è vulnerabile al problema della \"[denominazione topologica](Topological_naming_problem/it.md)\". Per maggiori informazioni vedere lo strumento **<img src="images/TechDraw_LengthDimension.svg" width=16px> [Lunghezza](TechDraw_LengthDimension/it.md)**. Si consiglia che il tratteggio sia uno degli ultimi passaggi del processo di disegno.


</div>

Una piccola serie di modelli di tratteggio sono disponibili in:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```

dove `$INSTALL_DIR` è la directory in cui è stato installato FreeCAD, per esempio


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```



## Proprietà

-    **Source**: La vista e la faccia che devono ricevere il modello di tratteggio.

-    **File Pattern**: La posizione del file PAT da utilizzare.

-    **Name Pattern**: Il nome dello specifico PAT all\'interno di File Pattern.

-    **Scale Pattern**: La scala da applicare al modello (deve essere \> 0.0).

-    **Weight Pattern**: Lo spessore delle linee del modello.

-    **Color Pattern**: Il colore delle linee del modello.



## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento GeometricHatch può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawGeomHatch", "GeomHatch")
hatch.Source = (view1, ["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
page.addView(hatch)
```

It is also possible to use TechDraw\'s geometric hatch engine to produce a compound object in the 3D space. One must take care that the base face lies on the XY plane, as the algorithm is not tailored yet for other cases:


```python
import TechDraw
face = Part.makePlane(10, 10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/it
