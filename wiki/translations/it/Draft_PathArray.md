---
- GuiCommand:
   Name: Draft_PathArray
   Name/it: Serie su tracciato
   MenuLocation: Modifiche - Strumenti serie - Serie su tracciato
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Version: 0.14
   SeeAlso: [Serie ortogonale](Draft_OrthoArray/it.md), [Serie polare](Draft_PolarArray/it.md), [Serie circolare](Draft_CircularArray/it.md), [Serie di link su tracciato](Draft_PathLinkArray/it.md), [Serie su punti](Draft_PointArray/it.md), [Serie di link su punti](Draft_PointLinkArray/it.md) 
---

# Draft PathArray/it



## Descrizione

Il comando <img alt="" src=images/Draft_PathArray.svg  style="width:24px;"> **Serie su tracciato** crea una serie (array) regolare da un oggetto selezionato posizionando copie lungo un percorso. Utilizzare invece il comando [Serie di link su tracciato](Draft_PathLinkArray/it.md) per creare una serie di [Link](App_Link/it.md) più efficiente. Fatta eccezione per il tipo di serie creato, Serie di link o Serie normale, il comando [Serie di link su tracciato](Draft_PathLinkArray/it.md) è identico a questo comando.

Entrambi i comandi possono essere utilizzati su oggetti 2D creati con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche su molti oggetti 3D come quelli creati con gli ambienti [Part](Part_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md) o [Arch](Arch_Workbench/it.md).

<img alt="" src=images/Draft_PathArray_Example.png  style="width:400px;"> 
*Serie su tracciato*



## Utilizzo

1.  Selezionare l\'oggetto che si desidera allineare.
2.  Aggiungere l\'oggetto tracciato alla selezione. È anche possibile selezionare invece dei bordi. I bordi devono appartenere allo stesso oggetto e devono essere collegati.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_PathArray.svg" width=16px> [Serie su tracciato](Draft_PathArray/it.md)**.
    -   Selezionare l\'opzione **Modifiche → Strumenti serie → <img src="images/Draft_PathArray.svg" width=16px> Serie su tracciato** dal menu.
4.  La serie viene creata.
5.  Facoltativamente, modificare le [proprietà](#Proprietà.md) della serie nell\'[Editor delle proprietà](property_editor/it.md).



## Allineamento

L\'allineamento degli elementi in una Serie su tracciato dipende dalle proprietà della serie e dall\'orientamento dell\'oggetto sorgente. La posizione dell\'oggetto sorgente viene ignorata: ai fini della serie {{Value|x}}, {{Value|y}} e {{Value|z}} sono impostati su {{Value|0}}. Se la proprietà **Align** della serie è impostata su `False` l\'orientamento degli elementi della serie è identico a quello dell\'oggetto sorgente. Se è impostata su `True`, l\'asse X del sistema di coordinate locale di ciascun posizionamento dell\'elemento è tangente al percorso. Gli assi Y e Z dei sistemi di coordinate locali dipendono dalla proprietà **Align Mode** della serie. Altre proprietà della serie coinvolte nell\'allineamento includono **Tangent Vector**, **Force Vertical** e **Vertical Vector**.

<img alt="" src=images/Draft_PathArray_example2.png  style="width:600px;"> 
*3 serie basate sullo stesso percorso non planare. Da sinistra a destra: Align è falso, Align è vero con Align Mode Original e Align è vero con Align Mode Frenet*.



### Modalità allineamento 

Sono disponibili tre modalità:



#### Originale

Questa modalità si avvicina di più alla singola **Align Mode** disponibile nella versione 0.18. Si basa su un vettore normale fisso. Se il percorso è planare questo vettore è perpendicolare al piano del percorso, altrimenti viene utilizzato un vettore predefinito, l\'asse Z positivo. Da questo vettore normale e dal vettore tangente locale (l\'asse X locale) viene calcolato un [cross product](https://en.wikipedia.org/wiki/Cross_product). Questo nuovo vettore viene utilizzato come asse Z locale. L\'orientamento dell\'asse Y locale è determinato dagli assi X e Z locali.

#### Frenet

Questa modalità utilizza il vettore normale locale derivato dal percorso in corrispondenza di ciascun posizionamento dell\'elemento. Se questo vettore non può essere determinato (ad esempio nel caso di un segmento retto) viene utilizzato un vettore predefinito, sempre l\'asse Z positivo. Con questo vettore e il vettore tangente locale si determina il sistema di coordinate locale utilizzando la stessa procedura del paragrafo precedente.



#### Tangente

Questa modalità è simile a **Align Mode** {{Value|Original}} ma include la possibilità di pre-ruotare l\'oggetto sorgente specificando un **Tangent Vector**.



### Forza Verticale e Vettore Verticale 

Queste proprietà sono disponibili solo se **Align Mode** è {{Value|Original}} o {{Value|Tangent}}. Se **Force Vertical** è impostato su `True` il sistema di coordinate locale viene calcolato in modo diverso. Il **Vertical Vector** viene utilizzato come vettore normale fisso. Da questo vettore normale e dal vettore tangente locale (l\'asse X locale) viene nuovamente calcolato un prodotto incrociato. Ma ora questo vettore è usato come asse Y locale. L\'orientamento dell\'asse Z locale è determinato dagli assi X e Y locali.

L\'utilizzo di queste proprietà può essere richiesto se uno degli spigoli del percorso è (quasi) parallelo alla normale predefinita del percorso.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Serie su tracciato è derivato da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà (ad eccezione di alcune proprietà View che non sono ereditate da Serie di Link). Le seguenti proprietà sono aggiuntive se non diversamente specificato:

### Data


{{TitleProperty|Link}}

Le proprietà in questo gruppo sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Scale|Float**
    

-    **Scale Vector|Vector|Hidden**
    

-    **Scale List|VectorList**
    

-    **Visibility List|BoolList|Hidden**
    

-    **Placement List|PlacementList|Hidden**
    

-    **Element List|LinkList|Hidden**
    

-    **_ Link Touched|Bool|Hidden**
    

-    **_ Child Cache|LinkList|Hidden**
    

-    **Colored Elements|LinkSubHidden|Hidden**
    

-    **Link Transform|Bool**
    


{{TitleProperty|Alignment}}

-    **Align|Bool**: specifica se gli elementi nella serie sono allineati o meno lungo il percorso. Se è `False` tutte le altre proprietà in questo gruppo, eccetto **Extra Translation**, non si applicano e sono nascoste.

-    **Align Mode|Enumeration**: specifica la modalità di allineamento, che può essere {{Value|Original}}, {{Value|Frenet}} o {{Value|Tangent}}.

-    **End Offset|Length**: specifica la lunghezza dalla fine del percorso all\'ultima copia. Deve essere inferiore alla lunghezza del percorso meno **Start Offset**. {{Version/it|0.21}}

-    **Extra Translation|VectorDistance**: specifica uno spostamento aggiuntivo per ogni elemento lungo il percorso.

-    **Force Vertical|Bool**: specifica se sovrascrivere la direzione normale predefinita con il valore di **Vertical Vector**. Utilizzato solo se **Align Mode** è {{Value|Original}} o {{Value|Tangent}}.

-    **Start Offset|Length**: specifica la lunghezza dall\'inizio del percorso alla prima copia. Deve essere inferiore alla lunghezza del percorso. {{Version/it|0.21}}

-    **Tangent Vector|Vector**: specifica il vettore di allineamento. Utilizzato solo se **Align Mode** è {{Value|Tangent}}.

-    **Vertical Vector|Vector**: specifica l\'override per la direzione normale predefinita. Utilizzato solo se **Vertical Vector** è `True`.


{{TitleProperty|Objects}}

-    **Base|LinkGlobal**: specifica l\'oggetto da duplicare nella serie.

-    **Count|Integer**: specifica il numero di elementi nella serie.

-    **Expand Array|Bool**: specifica se espandere la serie nella [Vista ad albero](Tree_view/it.md) per abilitare la selezione dei suoi singoli elementi. Disponibile solo per le serie di Link.

-    **Path Object|LinkGlobal**: specifica l\'oggetto da utilizzare per il percorso. Deve contenere {{Value|Edges}} nella sua [Part TopoShape](Part_TopoShape/it.md).

-    **Path Subelements|LinkSubListGlobal**: specifica un elenco di spigoli dell\'**Path Object**. Se forniti solo questi bordi vengono utilizzati per il percorso.

### View


{{TitleProperty|Link}}

Le proprietà in questo gruppo, ad eccezione della proprietà ereditata, sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Draw Style|Enumeration**
    

-    **Line Width|FloatConstraint**
    

-    **Override Material|Bool**
    

-    **Point Size|FloatConstraint**
    

-    **Selectable|Bool**: questa è una proprietà ereditata che appare nel gruppo Selezione per altre serie

-    **Shape Material|Material**
    


{{TitleProperty|Base}}

Le proprietà in questo gruppo, ad eccezione della proprietà ereditata, sono disponibili solo per le serie di link. Vedere [Crea link](Std_LinkMake/it#Proprietà.md) per ulteriori informazioni.

-    **Child View Provider|PersistentObject|Hidden**
    

-    **Material List|MaterialList|Hidden**
    

-    **Override Color List|ColorList|Hidden**
    

-    **Override Material List|BoolList|Hidden**
    

-    **Proxy|PythonObject|Hidden**: questa è una proprietà ereditata.


{{TitleProperty|Display Options}}

Le proprietà in questo gruppo sono proprietà ereditate. Vedere [Part Feature](Part_Feature#Properties.md) per ulteriori informazioni.

-    **Bounding Box|Bool**: questa proprietà non è ereditata dalle serie di link.

-    **Display Mode|Enumeration**: per le serie di link può essere {{value|Link}} o {{value|ChildView}}. Per altre serie può essere: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} o {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

Le proprietà in questo gruppo non vengono ereditate dalle serie di link.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una serie su tracciato utilizzare il metodo `make_path_array` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makePathArray`.


```python
path_array = make_path_array(base_object, path_object,
                             count=4, extra=App.Vector(0, 0, 0), subelements=None,
                             align=False, align_mode="Original", tan_vector=App.Vector(1, 0, 0),
                             force_vertical=False, vertical_vector=App.Vector(0, 0, 1),
                             use_link=True)
```

-    `base_object`è l\'oggetto da disporre in serie. Può anche essere la `Label` (string) di un oggetto nel documento corrente.

-    `path_object`è l\'oggetto percorso. Può anche essere la `Label` (string) di un oggetto nel documento corrente.

-    `count`è il numero di elementi nella serie.

-    `extra`è un vettore che sposta ogni elemento.

-    `subelements`è un elenco di bordi di `path_object`, ad esempio `["Edge1", "Edge2"]`. Se forniti solo questi bordi vengono utilizzati per il percorso.

-   Se `align` è `True` gli elementi sono allineati lungo il percorso a seconda del valore di `align_mode`, che può essere `"Original"`, `"Frenet"` o `"Tangent"`.

-    `tan_vector`è un vettore unitario che definisce la direzione tangente locale degli elementi lungo il percorso. Viene utilizzato quando `align_mode` è `"Tangent"`.

-   Se `force_vertical` è `True` `vertical_vector` viene utilizzato per la direzione Z locale degli elementi lungo il percorso. Viene utilizzato quando `align_mode` è `"Original"` o `"Tangent"`.

-   Se `use_link` è `True` gli elementi creati sono [App Links](App_Link/it.md) invece di normali copie.

-    `path_array`viene restituito con l\'oggetto serie creato.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

p1 = App.Vector(500, -1000, 0)
p2 = App.Vector(1500, 1000, 0)
p3 = App.Vector(3000, 500, 0)
p4 = App.Vector(4500, 100, 0)
spline = Draft.make_bspline([p1, p2, p3, p4])
obj = Draft.make_polygon(3, 500)

path_array = Draft.make_path_array(obj, spline, 6)
doc.recompute()

wire = Draft.make_wire([p1, -p2, -p3, -p4])
path_array2 = Draft.make_path_array(obj, wire, count=3, extra=App.Vector(0, -500, 0), subelements=["Edge2", "Edge3"], align=True, force_vertical=True)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PathArray/it
