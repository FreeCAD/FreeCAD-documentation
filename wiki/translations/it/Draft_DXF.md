





<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Draft DXF è un modulo software utilizzato dai comandi <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Apri](Std_Open/it.md), [Importa](Std_Import/it.md) and [Esporta](Std_Export/it.md) per gestire il formato DXF.


</div>

![](images/Screenshot_qcad.jpg ) *Disegno fatto con Qcad esportato in DXF, e successivamente aperto in FreeCAD*

## Importazione


<div class="mw-translate-fuzzy">

Sono supportate le versioni DXF R12 - 2007.


</div>

3D objects inside a DXF file are stored under a binary ACIS/SAT blob, which at the moment cannot be read by FreeCAD. Simpler entities like 3DFACEs, though, are supported.


<div class="mw-translate-fuzzy">

Possono essere importati i seguenti tipi di oggetti DXF:

-   linee
-   polilinee e polilinee alleggerite
-   circonferenze
-   archi
-   layers (i layers contenenti gli oggetti vengono convertiti in gruppi FreeCAD)
-   testi e testi multipli (mtexts)
-   dimensioni
-   blocchi (solo la geometria; i testi, le dimensioni e gli attributi all\'interno di blocchi sono ignorati)
-   punti
-   linee guida
-   \... e altro


</div>

## Esportazione


<div class="mw-translate-fuzzy">

I file vengono esportati nel formato DXF R12 che può essere gestito da molte applicazioni.


</div>


<div class="mw-translate-fuzzy">

Possono essere esportati i seguenti oggetti FreeCAD:

-   linee e spezzate (polilinee)
-   archi e circonferenze
-   testi
-   i colori sono mappati dai colori RGB degli oggetti secondo l\'indice dei colori di autocad (ACI). Il nero è sempre \"da layer\"
-   i layers sono mappati dai nomi dei gruppi. Quando i gruppi sono nidificati, il gruppo più interno attribuisce il nome al livello (layer)
-   le dimensioni, che vengono esportate con dimstyle \"Standard\"
-   \... e altro


</div>

## Installazione


<div class="mw-translate-fuzzy">

Per motivi di licenza, le librerie di importazione e di esportazione [DXF](DXF/it.md) richieste non fanno parte del codice sorgente di FreeCAD.

Per ulteriori informazioni, consultare: [Importare i file DXF in FreeCAD](FreeCAD_and_DXF_Import/it.md).


</div>

## Preferenze

Per ulteriori informazioni, consultare: [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md).

## Script


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Si possono esportare elementi in DXF usando la seguente funzione: 
```python
importDXF.export(objectslist, filename, nospline=False, lwPoly=False)
```

Esempio: 
```python
import Draft, importDXF

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importDXF.export(objects, "/home/user/Pictures/myfile.dxf")
```


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats{{\#translation:}}](Category:File_Formats.md)
