---
- GuiCommand:
   Name: Draft_PointArray
   Name/it: Serie su punti
   MenuLocation: Modifiche -> Strumenti serie ->  Serie su punti
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Version: 0.18
   SeeAlso: Draft_OrthoArray/it, Draft_PolarArray/it, Draft_CircularArray/it, Draft_PathArray/it, Draft_PathLinkArray/it, Draft_PointLinkArray/it
---

# Draft PointArray/it



## Descrizione

Il comando <img alt="" src=images/Draft_PointArray.svg  style="width:24px;"> **Serie su punti** crea una serie (array) regolare da un oggetto base selezionato posizionando copie nei punti da un oggetto punto. Utilizzare invece il comando [Serie di link su punti](Draft_PointLinkArray/it.md) per creare una serie [Link](App_Link/it.md) più efficiente. Fatta eccezione per il tipo di matrice creata, Serie di link o Serie normale, il comando [Serie di link su punti](Draft_PointLinkArray/it.md) è identico a questo comando.

L\'oggetto di base può essere un oggetto 2D creato con [Draft](Draft_Workbench/it.md) o [Sketcher](Sketcher_Workbench/it.md), ma anche un oggetto 3D come quelli creati con [Part](Part_Workbench/it.md), \[ \[PartDesign_Workbench/it\|PartDesign\]\] o [Arch](Arch_Workbench/it.md).

L\'oggetto punto può essere qualsiasi oggetto con una forma e vertici (inclusa una [Parte](Std_Part/it.md) contenente uno o più di tali oggetti), così come un [mesh](Mesh_Workbench/it.md) e un [nuvola di punti](Points_Workbench/it.md). I punti duplicati nell\'oggetto punto vengono filtrati. {{Version/it|0.21}}

In {{VersionMinus/it|0.20}} sono supportati solo tre tipi di oggetto punto, vedere [Oggetto punto versione 0.20 e precedenti](#Oggetto_punto_versione_0.20_e_precedenti.md).

<img alt="" src=images/Draft_PointArray_Example.png  style="width:400px;"> 
*Serie su punti*



## Utilizzo

1.  Selezionare l\'oggetto che si desidera allineare.
2.  Aggiungere l\'oggetto [composto di punti](#Point_compound/it.md) alla selezione.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_PointArray.svg" width=16px> [Serie su punti](Draft_PointArray/it.md)**.
    -   Selezionare l\'opzione **Modifiche → Strumenti serie→ <img src="images/Draft_PointArray.svg" width=16px> Serie su punti** dal menu.
4.  La serie viene creata.
5.  Facoltativamente, modificare le [proprietà](#Proprietà.md) della serie nell\'[Editor delle proprietà](property_editor/it.md).



## Oggetto punto versione 0.20 e precedenti 

Questi sono gli oggetti punto supportati in {{VersionMinus/it|0.20}} e come possono essere creati:

-   [Part Composto](Part_Compound/it.md): creare uno o più [Punti Draft](Draft_Point/it.md) o [Punti Part](Part_Point/it.md), selezionarli e richiamarli con il comando [Part Composto](Part_Compound/it.md).
-   Blocco di Draft: creare uno o più [Punti Draft](Draft_Point/it.md) o [Punti Part](Part_Point/it.md), selezionarli e invocare il comando [Draft Promuovi](Draft_Upgrade/it.md).
-   [Sketch](Sketcher_NewSketch/it.md): Creare uno [Sketch](Sketcher_NewSketch/it.md) e aggiungere uno o più [Punti Sketch](Sketcher_CreatePoint/it.md) allo sketch.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Serie su punti è derivato da un oggetto [Part Feature](Part_Feature/it.md) e ne eredita tutte le proprietà (ad eccezione di alcune proprietà View che non sono ereditate da Serie di Link). Le seguenti proprietà sono aggiuntive se non diversamente specificato:

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
    


{{TitleProperty|Objects}}

-    **Base|Link**: specifica l\'oggetto da duplicare nella serie.

-    **Count|Integer**: (sola lettura) specifica il numero di elementi nella serie. Questo numero è determinato dal numero di punti nel **Point Object**.

-    **Expand Array|Bool**: specifica se espandere la serie nella [Vista ad albero](Tree_view/it.md) per abilitare la selezione dei suoi singoli elementi. Disponibile solo per le serie di Link.

-    **Extra Placement|Placement**: : specifica un ulteriore [posizionamento](Placement/it.md), traslazione e rotazione, per ogni elemento nella serie.

-    **Point Object|Link**: specifica l\'oggetto composto i cui punti vengono utilizzati per posizionare gli elementi nella serie. L\'oggetto deve avere una proprietà **Links**, **Components** o **Geometry** e contenere almeno un elemento con **X**, **Y ** e le proprietà **Z**.

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
    

-    **Proxy|PythonObject|Hidden**: this is an inherited property.


{{TitleProperty|Display Options}}

Le proprietà in questo gruppo sono proprietà ereditate. Vedere [Part Feature](Part_Feature#Properties.md) per ulteriori informazioni.

-    **Bounding Box|Bool**: questa proprietà non è ereditata dalle serie di link.

-    **Modalità di visualizzazione|Enumeration**: per le serie di link può essere {{value|Link}} o {{value|ChildView}}. Per altre serie può essere: {{value|Flat Lines}}, {{value|Shaded}}, {{value|Wireframe}} o {{value|Points}}

-    **Show In Tree|Bool**
    

-    **Visibility|Bool**
    


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.


{{TitleProperty|Object style}}

Le proprietà in questo gruppo non vengono ereditate dalle serie di link.

## Scripting

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una serie di punti usare il metodo `make_point_array` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makePointArray`.


```python
point_array = make_point_array(base_object, point_object, extra=None, use_link=True)
```

-    `base_object`è l\'oggetto da disporre in serie. Può anche essere la `Label` (string) di un oggetto nel documento corrente.

-    `point_object`è l\'oggetto che contiene i punti. Può anche essere la `Label` (string) di un oggetto nel documento corrente. Dovrebbe avere una proprietà `Geometry`, `Links` o `Components` contenente punti.

-    `extra`è un `App.Placement`, un `App.Vector` o un `App.Rotation` che sposta ogni elemento.

-   Se `use_link` è `True` gli elementi creati sono [App Links](App_Link/it.md) invece di normali copie.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

polygon = Draft.make_polygon(3, radius=500.0)

p1 = Draft.make_point(App.Vector(1500, 0, 0))
p2 = Draft.make_point(App.Vector(2500, 0, 0))
p3 = Draft.make_point(App.Vector(2000, 1000, 0))

compound = doc.addObject("Part::Compound", "Compound")
compound.Links = [p1, p2, p3]

point_array = Draft.make_point_array(polygon, compound)
doc.recompute()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft PointArray/it
