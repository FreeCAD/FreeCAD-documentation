# Draft SVG/it







<div class="mw-translate-fuzzy">





</div>


{{TOCright}}

## Descrizione


<div class="mw-translate-fuzzy">

Draft SVG è un modulo software utilizzato dai comandi <img alt="" src=images/Std_Open.svg  style="width:24px;"> [Apri](Std_Open/it.md), [Importa](Std_Import/it.md) e [Esporta](Std_Export/it.md) per gestire il formato [SVG](SVG/it.md).


</div>

![](images/Screenshot_inkscape.jpg ) *Disegno di Inkscape esportato in SVG, e successivamente aperto in FreeCAD*

## Importazione

Si possono importare i seguenti oggetti SVG:

-   Oggetti PATH
-   Oggetti LINE
-   Oggetti RECT
-   Oggetti CIRCLE
-   Oggetti ELLIPSE
-   Oggetti POLYGON
-   Oggetti POLYLINE

## Limitazioni

FreeCAD non importerà oggetti tracciato che hanno un solo punto ([forum discussion](https://forum.freecadweb.org/viewtopic.php?f=3&t=43856)).

## Esportazione

È possibile esportare i seguenti oggetti FreeCAD:

-   Linee e spezzate (polilinee)
-   Archi e circonferenze
-   Facce
-   Testi
-   Dimensioni

### Limitazione

Ricordare che il formato SVG è un formato 2D, quindi si perdono tutte le informazioni sull\'asse Z (tutti gli oggetti risultano appiattiti).

## Gestione delle Unità 

Quando si esporta, una Unità utente (px) equivale a un millimetro.

Durante l\'importazione sono rispettati la larghezza, l\'altezza e gli attributi Viewbox. Tutti gli elementi vengono scalati alle loro dimensioni in millimetri, che è l\'unità interna di FreeCAD. Se il file SVG non contiene informazioni sulla dimensione fisica, si presuppone di avere una risoluzione di 90 DPI. L\'utilizzo di unità assolute negli attributi all\'interno del SVG è da evitare. Unità relative come em, ex e % non sono attualmente supportate.


<div class="mw-translate-fuzzy">

L\'editor di SVG [Inkscape](https://inkscape.org/) attualmente funziona solo con documenti con 90 DPI. Non importa quale unità è selezionata in Inkscape. In uscita, tutto deve essere considerato convertito in 90 DPI e **arrotondato** a 6 decimali.

Dato che FreeCAD (e lo standard SVG) è agnostico alla precisione di arrotondamento fatta in Inkscape questi valori non sono arrotondati in ingresso. And odd values in millimeter will remain.

Se è necessario importare l\'SVG senza arrotondamenti, lavorare in Unità utente (px) in Inkscape. La scalatura può essere eseguita dopo l\'importazione in FreeCAD o modificando la larghezza, l\'altezza e gli attributi Viewbox.


</div>

## Preferenze

Per ulteriori informazioni, consultare: [Preferenze di Importa/Esporta](Import_Export_Preferences/it.md).

## Script


<div class="mw-translate-fuzzy">


**Vedere anche:**

[API Draft](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>

Si possono esportare elementi in SVG usando la seguente funzione: 
```python
importSVG.export(exportList, filename)
```

Esempio: 
```python
import Draft, importSVG

Polygon1 = Draft.makePolygon(3, radius=500)
Polygon2 = Draft.makePolygon(5, radius=1500)

objects = [Polygon1, Polygon2]

importSVG.export(objects, "/home/user/Pictures/myfile.svg")
```


<div class="mw-translate-fuzzy">





</div>


 

[Category:File Formats](Category:File_Formats.md)
