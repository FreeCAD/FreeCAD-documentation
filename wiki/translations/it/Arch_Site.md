---
- GuiCommand:/it
   Name:Arch Site
   Name/it:Sito
   Workbenches:[Architettura](Arch_Workbench/it.md)
   MenuLocation:Arch → Sito
   Shortcut:**S** **I**
   SeeAlso:[Piano](Arch_Floor/it.md), [Edificio](Arch_Building/it.md)
---

# Arch Site/it


</div>



## Descrizione

Il Sito di Arch è un oggetto speciale che unisce le proprietà di un oggetto gruppo standard di FreeCAD con quelle degli oggetti Arch. Esso è particolarmente adatto per rappresentare un intero sito del progetto o un terreno. Nei lavori di architettura basati su IFC, serve soprattutto per organizzare il modello, racchiudendo in esso gli oggetti [edificio](Arch_Building/it.md). Il sito è utilizzato anche per gestire e visualizzare un terreno fisico, e può calcolare i volumi di terra che devono essere aggiunti o rimossi.



## Utilizzo

1.  Selezionare uno o più oggetti da includere nel nuovo sito
2.  Premere il pulsante **<img src="images/Arch_Site.svg" width=16px> [Sito](Arch_Site/it.md)
**, oppure premere i tasti **S** e **I**



## Opzioni

-   Dopo aver creato un sito, è possibile aggiungere ad esso altri oggetti con il drag-and-drop nella struttura ad albero o utilizzando lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi](Arch_Add/it.md)**. Ciò determina solo quale oggetto fa parte di un dato sito, e non ha effetto sul terreno stesso.
-   È possibile rimuovere gli oggetti da un sito trascinandoli fuori con il drag-and-drop nella vista ad albero o utilizzando lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi](Arch_Remove/it.md)
**
-   È possibile aggiungere un oggetto terreno modificando la proprietà **Terrain** del Sito. Il terreno deve essere un guscio aperto (shell) o una superficie.
-   È possibile aggiungere volumi da sommare o da sottrarre dal terreno di base, facendo doppio clic sul Sito, e aggiungendo gli oggetti ai suoi gruppi Sottrazioni o Aggiunte. Gli oggetti devono essere dei solidi.
-   La proprietà **Extrusion Vector** può essere utilizzata per risolvere alcuni problemi che possono presentarsi quando si lavora con le sottrazioni e le aggiunte. Per svolgere tali addizioni o sottrazioni, la superficie del terreno viene estrusa in un solido, che viene poi opportunamente aggiunto o sottratto. A seconda della topologia del terreno, questa estrusione potrebbe non riuscire con il vettore di default di estrusione. Può darsi che sia possibile risolvere il problema assegnando al vettore a un valore diverso.



## Proprietà

### Data


<div class="mw-translate-fuzzy">

### Dati

-    {{PropertyData/it|Terrain}}: Il terreno di base del sito

-    {{PropertyData/it|Address}}: La via e il numero civico di questo sito

-    {{PropertyData/it|Postal Code}}: Il codice postale o zip di questo sito

-    {{PropertyData/it|City}}: La città di questo sito

-    {{PropertyData/it|Country}}: Il paese di questo sito

-    {{PropertyData/it|Latitude}}: La latitudine di questo sito

-    {{PropertyData/it|Longitude}}: La longitudine di questo sito

-    {{PropertyData/it|Url}}: Un URL che mostra questo sito in un sito web mapping

-    {{PropertyData/it|Projected Area}}: L\'area della proiezione di questo oggetto sul piano XY

-    {{PropertyData/it|Perimeter}}: La lunghezza del perimetro di questo terreno

-    {{PropertyData/it|Addition Volume}}: Il volume di terra da aggiungere a questi terreni

-    {{PropertyData/it|Subtraction Volume}}: Il volume di terra da rimuovere da questi terreni

-    {{PropertyData/it|Extrusion Vector}}: Un vettore di estrusione da utilizzare durante l\'esecuzione di operazioni booleane

-    {{PropertyData/it|Remove Splitter}}: Rimuovere gli scarti dalla forma risultante

-    **Declination**: l\'angolo tra la direzione Nord reale e quella Nord in questo documento, ovvero l\'asse Y.<small>(v0.18)</small>  Ciò significa che per impostazione predefinita l\'asse Y punta a Nord e l\'asse X punta a Est; l\'angolo aumenta in senso antiorario. Questa proprietà era precedentemente nota come**North Deviation**.

-    **EPW File**: Consente di allegare un file EPW dal [sito web di dati EPW Ladybug](https://www.ladybug.tools/epwmap/) a questo sito. Ciò è necessario per visualizzare i diagrammi della rosa dei venti {{version/it|0.19}}


</div>

### View


<div class="mw-translate-fuzzy">

### Vista

-    **Solar Diagram**: Mostra o nasconde il diagramma solare

-    **Solar Diagram Color**: Il colore del diagramma solare

-    **Solar Diagram Position**: La posizione del diagramma solare

-    **Solar Diagram Scale**: La scala del diagramma solare

-    **Wind Rose**: Mostra o nasconde il diagramma della rosa dei venti (richiede che la proprietà dati **File EPW** sia riempita e il modulo Ladybug Python sia installato (vedere sotto)


</div>



## Tipico flusso di lavoro 

Iniziare creando un oggetto che rappresenta il terreno. Deve essere una superficie aperta, non un solido. Per esempio, è facile per importare dati mesh, che possono essere trasformati in una Part Shape dal menu **Part → Crea Forma da Mesh**. Poi, creare un oggetto Sito, e impostare la sua proprietà **Terrain** dalla Parte appena creata:

![](images/Arch_site_example_01.jpg )

Creare alcuni volumi (devono essere dei solidi) che rappresentano le aree che si desidera scavare o riempire. Fare doppio clic sull\'oggetto Sito nella struttura ad albero, e aggiungere questi volumi ai gruppi Aggiunte o Sottrazioni. Fare clic su OK.

![](images/Arch_site_example_02.jpg )

La geometria sito sarà ricalcolata e le proprietà aree, il perimetro e i volumi rivalutati.

![](images/Arch_site_example_03.jpg )



## Diagrammi solari e del vento 


<div class="mw-translate-fuzzy">

Se nel proprio sistema è installato [Ladybug](https://www.ladybug.tools/ladybug.html), i [Siti](Arch_Site/it.md) di Arch possono visualizzare un diagramma solare o del vento. Per questo, le proprietà **Longitude**, **Latitude** e **Declination** (precedentemente era **North Deviation**) devono essere impostate correttamente, e la proprietà **Solar Diagram** o **Wind Rose** impostata su `True`. {{Version/it|0.17}} e {{Version/it|0.19}}


</div>

**Nota**: Se non avete Ladybug, [pysolar](http://pysolar.org/) è ancora supportato per generare diagrammi solari, ma non rose dei venti. E\' richiesto Pysolar 0.7 o superiore; questa versione funziona solo con Python 3. Se serve questa funzione con Python 2, si deve avere Pysolar 0.6 in quanto questa è l\'ultima versione che funziona con Python 2. Tuttavia, Ladybug è uno strumento molto più potente che probabilmente verrà utilizzato di più in futuro, quindi si consiglia di utilizzarlo al posto di pysolar. Ladybug può essere installato semplicemente tramite [pip](https://github.com/ladybug-tools/ladybug).

![](images/Freecad-solar-diagram.jpg )

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Sito può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
Site = makeSite(objectslist=None, baseobj=None, name="Site")
```

-   Crea un oggetto `Site` da `objectslist`, che è una lista di oggetti, o da un `baseobj`, che è una `Shape` o un `Terrain`.

Esempio: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
Wall = Arch.makeWall(baseline, length=None, width=150, height=2000)
FreeCAD.ActiveDocument.recompute()

Building = Arch.makeBuilding([Wall])
Site = Arch.makeSite([Building])

FreeCAD.ActiveDocument.recompute()
FreeCAD.Gui.ActiveDocument.ActiveView.viewIsometric()
```



### Diagramma solare 

Se il modulo `pysolar` è presente, è possibile aggiungere al sito un diagramma solare. Impostare gli angoli di longitudine, latitudine e declinazione in modo appropriato, nonché una scala adeguata per le dimensioni del modello.

Notare che è richiesto Pysolar 0.7 o superiore, e questa versione funziona solo con Python 3.


```python
Site.Longitude = -46.38
Site.Latitude = -23.33
Site.Declination = 30
#Site.Compass = True

Site.ViewObject.SolarDiagram = True
Site.ViewObject.SolarDiagramScale = 10000
FreeCAD.ActiveDocument.recompute()
```



### Diagramma solare indipendente dal sito 

Un diagramma solare può essere creato con la seguente funzione, indipendentemente da qualsiasi sito: 
```python
Node = makeSolarDiagram(longitude, latitude, scale=1, complete=False)
```

-   Crea un diagramma solare come nodo Pivy, usando `longitude` e `latitude`, con una {{incode | scale}} opzionale.
-   Se `complete` è `True`, disegna i 12 mesi, che mostra l\'intero [analemma](https://en.wikipedia.org/wiki/Analemma) solare.


```python
import FreeCADGui, Arch

Node = Arch.makeSolarDiagram(-46.38, -23.33, scale=10000, complete=True)
FreeCAD.Gui.ActiveDocument.ActiveView.getSceneGraph().addChild(Node)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Site/it
