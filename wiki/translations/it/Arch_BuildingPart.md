---
- GuiCommand:/it
   Name:Arch BuildingPart
   Name/it:Parte di edificio
   MenuLocation:Arch → Parte di edificio
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:
   Version:0.18
   SeeAlso:[Edificio](Arch_Building/it.md), [Sito](Arch_Site/it.md)
---

# Arch BuildingPart/it


</div>

## Descrizione

Parti di edificio sostituisce i vecchi [Piano](Arch_Floor/it.md) e [Edificio](Arch_Building/it.md) di Arch con una versione più capace che può essere utilizzata non solo per creare Piani o Livelli, ma anche tutti i tipi di situazioni in cui è necessario raggruppare oggetti Arch o BIM diversi e quel gruppo può aver bisogno di essere gestito come un oggetto o replicato.

## Utilizzo

1.  Facoltativamente, selezionare uno o più oggetti da includere nella nuova Parte dell\'edificio.
2.  Premere il pulsante **<img src="images/Arch_BuildingPart.svg" width=16px> [Parte di edificio](Arch_BuildingPart/it.md)**.

### Note

Parte di edificio incorpora implicitamente un [Piano di sezione](Arch_SectionPlane/it.md). {{Version/it|0.19}}

Questo piano di sezione è sempre parallelo al piano di base di Parte di edificio, ma è possibile specificare l\'offset tra di loro. Quindi tutti gli strumenti che funzionano con un piano di sezione, come [Vista profilo 2D](Draft_Shape2DView/it.md) di Draft e [Vista di Arch](TechDraw_ArchView/it.md) di TechDraw funzionano anche con Parte di edificio.

## Opzioni


<div class="mw-translate-fuzzy">

-   Dopo aver creato una Parte di edificio, è possibile aggiungere più oggetti trascinandoli nella Vista ad albero o usando lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi componente](Arch_Add/it.md)**.
-   Per rimuovere oggetti da una Parte di edificio trascinarli nella vista ad albero o usare lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)**.
-   Facendo doppio clic sull\'oggetto Parte di edificio nella vista ad albero, il [Piano di lavoro](Draft_SelectPlane/it.md) viene impostato sulla sua posizione e la Parte di edificio diventa attiva, il che significa che i nuovi oggetti vengono aggiunti automaticamente ad esso. Facendo nuovamente doppio clic su Parte di edificio, essa si disattiva e si imposta il piano di lavoro nella posizione precedente.
-   Parte di edificio può visualizzare un segno nella vista 3D con una etichetta e l\'indicazione del livello.
-   Quando un oggetto Parte di edificio viene spostato o ruotato, tutti i suoi figli che non hanno alcuna proprietà **Move With Host** o che hanno questa proprietà attivata, si spostano o ruotano insieme.
-   Parte di edificio può essere [clonato](Draft_Clone/it.md)
-   Parte di edificio può assumere qualsiasi tipo di IFC. La sua proprietà **IFC Type** ne determina l\'utilizzo. Se la si imposta su **Building Storey** si comporta come livello. Se la si imposta su **Building** si comporta come un edificio e se la si imposta su **Element Assembly** si comporta come un assemblaggio. La sua icona cambia per riflettere questa impostazione, ma a parte questo non ha nessun altro impatto in FreeCAD. Tuttavia, l\'esportazione in IFC in un tipo o un altro tipo può avere un impatto in altre applicazioni BIM.


</div>

## Proprietà

### Dati

-    **Height**: l\'altezza di questo oggetto, e dei suoi oggetti figli. Gli oggetti figli possono essere, per esempio, dei [muri](Arch_Wall/it.md). L\'altezza di ogni muro deve essere impostata su `0` (zero), quindi la proprietà altezza della Parte di edificio si propaga agli oggetti al suo interno.

-    **LevelOffset**: il livello del punto (0,0,0) di questo livello. Questo valore viene aggiunto all\'attributo `Placement.Base.z` di BuildingPart, per indicare un offset verticale senza spostare effettivamente l\'oggetto. L\'offset risultante viene visualizzato se **Show Level** è `True`.

-    **Area**: l\'area del pavimento calcolata di questo piano.

-    **IfcType**: il tipo di questo oggetto.

-    **Description**: una descrizione facoltativa per questo componente.

-    **Tag**: un tag opzionale per questo componente.

-    **IfcAttributes**: proprietà e attributi IFC personalizzati.

### Vista

-    **LineWidth**: lo spessore di linea di questo oggetto

-    **OverrideUnit**: un\'unità opzionale per esprimere i livelli

-    **DisplayOffset**: una trasformazione da applicare al segno di livello

-    **ShowLevel**: se è vero, mostra il livello

-    **ShowUnit**: se è vero, mostra l\'unità sul tag di livello

-    **SetWorkingPlane**: se è vero, quando attivato, il piano di lavoro si adatta automaticamente a questa Parte di edificio

-    **OriginOffset**: se è vero, quando attivato, l\'Offset della visualizzazione influisce anche sul segno di origine

-    **ShowLabel**: se true, quando attivato, viene visualizzata l\'etichetta dell\'oggetto

-    **FontName**: il carattere da utilizzare per i testi

-    **FontSize**: la dimensione del carattere dei testi

-    **RestoreView**: se impostato, la vista memorizzata in questo oggetto viene ripristinata con un doppio clic

-    **DiffuseColor**: i singoli colori delle facce


{{Version/it|0.19}}

-    **ChildrenOverride**: Se impostato, le impostazioni seguenti influenzno i figli di questa Parte di edificio.

-    **ChildrenLineWidth**: La larghezza di linea da applicare ai figli di questa Parte di edificio.

-    **ChildrenLineColor**: Il colore della linea da applicare ai figli di questa Parte di edificio.

-    **ChildrenShapeColor**: Il colore della forma da applicare ai figli di questa Parte di edificio.

-    **ChildrenTransparency**: La trasparenza da applicare ai figli di questa Parte di edificio.

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Parte di edificio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Crea un oggetto `BuildingPart` da una `objectslist`, che è una lista di oggetti.

Esempio: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/it
