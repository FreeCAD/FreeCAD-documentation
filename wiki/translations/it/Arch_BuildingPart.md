---
 GuiCommand:
   Name: Arch BuildingPart
   Name/it: Parte di edificio
   MenuLocation: Arch , Parte di edificio
   Workbenches: Arch_Workbench/it
   Version: 0.18
   SeeAlso: Arch_Building/it, Arch_Site/it
---

# Arch BuildingPart/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Parti di edificio sostituisce i vecchi [Piano](Arch_Floor/it.md) e [Edificio](Arch_Building/it.md) di Arch con una versione più capace che può essere utilizzata non solo per creare Piani o Livelli, ma anche tutti i tipi di situazioni in cui è necessario raggruppare oggetti Arch o BIM diversi e quel gruppo può aver bisogno di essere gestito come un oggetto o replicato.


</div>



## Utilizzo

1.  Facoltativamente, selezionare uno o più oggetti da includere nella nuova Parte dell\'edificio.
2.  Premere il pulsante **<img src="images/Arch_BuildingPart.svg" width=16px> [Parte di edificio](Arch_BuildingPart/it.md)**.



### Note

Parte di edificio incorpora implicitamente un [Piano di sezione](Arch_SectionPlane/it.md).

Questo piano di sezione è sempre parallelo al piano di base di Parte di edificio, ma è possibile specificare l\'offset tra di loro. Quindi tutti gli strumenti che funzionano con un piano di sezione, come [Vista profilo 2D](Draft_Shape2DView/it.md) di Draft e [Vista di Arch](TechDraw_ArchView/it.md) di TechDraw funzionano anche con Parte di edificio.



## Opzioni

-   Dopo aver creato una Parte di edificio, è possibile aggiungere più oggetti trascinandoli nella Vista ad albero o usando lo strumento **<img src="images/Arch_Add.svg" width=16px> [Aggiungi componente](Arch_Add/it.md)**.
-   Per rimuovere oggetti da una Parte di edificio trascinarli nella vista ad albero o usare lo strumento **<img src="images/Arch_Remove.svg" width=16px> [Rimuovi componente](Arch_Remove/it.md)**.
-   Facendo doppio clic sull\'oggetto Parte di edificio nella vista ad albero, il [Piano di lavoro](Draft_SelectPlane/it.md) viene impostato sulla sua posizione e la Parte di edificio diventa attiva, il che significa che i nuovi oggetti vengono aggiunti automaticamente ad esso. Facendo nuovamente doppio clic su Parte di edificio, essa si disattiva e si imposta il piano di lavoro nella posizione precedente (per essere disponibile questa opzione, deve essere impostata su true, nel pannello Visualizza combinata, la proprietà - Interaction - Double Click Activates).
-   Parte di edificio può visualizzare un marchio nella vista 3D con una etichetta e con l\'indicazione del livello.
-   Quando un oggetto Parte di edificio viene spostato o ruotato, tutti i suoi figli che non hanno alcuna proprietà **Move With Host** o che hanno questa proprietà attivata, si spostano o ruotano insieme.
-   Parte di edificio può essere [clonato](Draft_Clone/it.md)
-   Parte di edificio può assumere qualsiasi tipo di IFC. La sua proprietà **IFC Type** ne determina l\'utilizzo. Se la si imposta su **Building Storey** si comporta come livello. Se la si imposta su **Building** si comporta come un edificio e se la si imposta su **Element Assembly** si comporta come un assemblaggio. La sua icona cambia per riflettere questa impostazione, ma a parte questo non ha nessun altro impatto in FreeCAD. Tuttavia, l\'esportazione in IFC in un tipo o un altro tipo può avere un impatto in altre applicazioni BIM.
-   Le parti dell\'edificio consentono di definire una **Auto-group capture box**. I successivi oggetti Draft e Arch, o qualsiasi altra cosa che utilizzi Draft.autogroup(), verranno automaticamente aggiunti a quella parte di edificio se si trovano completamente all\'interno della casella di acquisizione. {{Version/it|0.20}}



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Una Parte di Edificio di Arch deriva da un oggetto [App GeoFeature](App_GeoFeature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Base}}

-    **Group|LinkList**: Elenco degli oggetti referenziati.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**: La superficie calcolata di questo piano.

-    **Height|Length**: L\'altezza di questo oggetto e dei suoi oggetti secondari. Gli oggetti figli potrebbero essere, ad esempio, [Muri di Arch](Arch_Wall/it.md). L\'altezza di ogni muro deve essere impostata su `0` (zero), quindi la proprietà altezza di BuildingPart si propaga agli oggetti al suo interno.

-    **Level Offset|Length**: Il livello del punto (0,0,0) di questo livello. Questo valore viene aggiunto all\'attributo `Placement.Base.z` di BuildingPart, per indicare un offset verticale senza spostare effettivamente l\'oggetto. L\'offset risultante viene visualizzato se **Show Level** è `True`.

-    **Materials Table|Map|Hidden**: Una mappa MaterialName:SolidIndexesList che mette in relazione i nomi dei materiali con gli indici solidi da utilizzare quando si fa riferimento a questo oggetto da altri file.

-    **Only Solids|Bool**: Se vero, solo i solidi verranno raccolti da questo oggetto quando è referenziato da altri file.

-    **Saved Inventor|FileIncluded|Hidden**: Questa proprietà memorizza una rappresentazione dell\'inventore per questo oggetto.

-    **Shape|PartShape|Hidden**: La forma di questo oggetto.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**: Se vero, il valore dell\'altezza si propaga agli oggetti contenuti. Vedere la proprietà **Height** per ulteriori informazioni.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**: dati IFC.

-    **Ifc Properties|Map|Hidden**: Proprietà IFC di questo oggetto.

-    **Ifc Type|Enumeration**: Il tipo IFC di questo oggetto.


{{TitleProperty|IFC Attributes}}

-    **Description|String**: Una descrizione facoltativa per questo componente

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**: Un tag facoltativo per questo componente.

-    **User Defined Partitioning Type|String**
    



### Vista


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**: Imposta automaticamente la dimensione della casella di acquisizione dal contenuto della parte di edificio. {{Version/it|0.20}}

-    **Autogroup Box|Bool**: Attiva/disattiva il raggruppamento automatico (e la visualizzazione della casella di acquisizione). {{Version/it|0.20}}

-    **Autogroup Margin|Length**: Un margine da utilizzare quando il ridimensionamento automatico è attivato. {{Version/it|0.20}}

-    **Autogroup Size|IntegerList**: La casella di acquisizione per gli oggetti appena creati espressi come \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. {{Version/it|0.20}}


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**: I colori individuali della faccia.

-    **Display Offset|Placement**: Una trasformazione da applicare al segno di livello.

-    **Font Name|Font**: Il carattere da utilizzare per i testi.

-    **Font Size|Length**: La dimensione del carattere dei testi.

-    **Line Width|Float**: Lo spessore della linea di questo oggetto.

-    **Origin Offset|Bool**: Se vero, quando attivato, l\'offset del display influenzerà anche il segno di origine.

-    **Override Unit|String**: Un\'unità opzionale per esprimere i livelli.

-    **Show Label|Bool**: Se vero, quando attivato, viene visualizzata l\'etichetta dell\'oggetto.

-    **Show Level|Bool**: Se vero, mostra il livello.

-    **Show Unit|Bool**: Se vero, mostra l\'unità sull\'etichetta del livello.


{{TitleProperty|Children}}

-    **Children Line Color|Color**: Il colore della linea da applicare agli elementi figlio di questa parte dell\'edificio.

-    **Children Line Width|Float**: Lo spessore della linea da applicare agli elementi figlio di questa parte dell\'edificio.

-    **Children Override|Bool**: Se vero, gli oggetti contenuti in questa parte di edificio adotteranno queste impostazioni di linea, colore e trasparenza.

-    **Children Shape Color|Color**: Il colore della forma da applicare agli elementi figlio di questa parte dell\'edificio.

-    **Children Transparency|Percent**: La trasparenza da applicare ai figli di questa Parte Edile.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**: Attivare il taglio quando si attiva questo livello.

-    **Cut Margin|Length**: La distanza tra il piano del livello e la linea di taglio.

-    **Cut View|Bool**: Taglia la vista sopra questo livello.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**: Se impostato su True, il piano di lavoro verrà mantenuto in modalità Auto.

-    **Double Click Activates|Bool**: Se True, facendo doppio clic su questo oggetto nell\'albero lo si attiva.

-    **Restore View|Bool**: Se impostata, la vista memorizzata in questo oggetto verrà ripristinata con un doppio clic.

-    **Save Inventor|Bool**: Se è abilitato, la rappresentazione dell\'inventore di questo oggetto verrà salvata nel file di FreeCAD, consentendo di farvi riferimento in altri file in modalità leggera.

-    **Saved Inventor|FileIncluded|Hidden**: Uno slot per salvare la rappresentazione dell\'inventore di questo oggetto, se abilitato.

-    **Set Working Plane|Bool**: Se vero, una volta attivato, il piano di lavoro si adatterà automaticamente a questa parte dell\'edificio.

-    **View Data|FloatList|Hidden**: Dati sulla posizione della telecamera associati a questo oggetto.



## Script


**Vedere anche:**

[API di Arch](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento Parte di edificio può essere utilizzato nelle [macro](Macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


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


{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch BuildingPart/it
