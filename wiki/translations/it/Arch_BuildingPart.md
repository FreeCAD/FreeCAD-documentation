---
 GuiCommand:
   Name: Arch BuildingPart
   Name/it: Parte di edificio
   MenuLocation: Arch , Parte di edificio
   Workbenches: Arch_Workbench/it
   Shortcut: 
   Version: 0.18
   SeeAlso: Arch Building/it, Arch Site/it
---

# Arch BuildingPart/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Parti di edificio sostituisce i vecchi [Piano](Arch_Floor/it.md) e [Edificio](Arch_Building/it.md) di Arch con una versione più capace che può essere utilizzata non solo per creare Piani o Livelli, ma anche tutti i tipi di situazioni in cui è necessario raggruppare oggetti Arch o BIM diversi e quel gruppo può aver bisogno di essere gestito come un oggetto o replicato.


</div>



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Facoltativamente, selezionare uno o più oggetti da includere nella nuova Parte dell\'edificio.
2.  Premere il pulsante **<img src="images/Arch_BuildingPart.svg" width=16px> [Parte di edificio](Arch_BuildingPart/it.md)**.


</div>



### Note


<div class="mw-translate-fuzzy">

Parte di edificio incorpora implicitamente un [Piano di sezione](Arch_SectionPlane/it.md). {{Version/it|0.19}}


</div>

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

See also: [Property editor](Property_editor.md).

An Arch BuildingPart is derived from an [App GeoFeature](App_GeoFeature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Base}}

-    **Group|LinkList**: List of referenced objects.

-    **_ Group Touched|Bool|Hidden**
    


{{TitleProperty|Building Part}}

-    **Area|Area**: The computed floor area of this floor.

-    **Height|Length**: The height of this object, and of its children objects. The children objects could be, for example, [Arch Walls](Arch_Wall.md). Each wall\'s height must be set to `0` (zero), so the height property of the BuildingPart propagates to the objects inside of it.

-    **Level Offset|Length**: The level of the (0,0,0) point of this level. This value is added to the `Placement.Base.z` attribute of the BuildingPart, to indicate a vertical offset without actually moving the object. The resulting offset is displayed if **Show Level** is `True`.

-    **Materials Table|Map|Hidden**: A MaterialName:SolidIndexesList map that relates material names with solid indexes to be used when referencing this object from other files.

-    **Only Solids|Bool**: If true, only solids will be collected by this object when referenced from other files.

-    **Saved Inventor|FileIncluded|Hidden**: This property stores an inventor representation for this object.

-    **Shape|PartShape|Hidden**: The shape of this object.


{{TitleProperty|Children}}

-    **Height Propagate|Bool**: If true, the height value propagates to contained objects.


{{TitleProperty|IFC}}

-    **Ifc Data|Map|Hidden**: IFC data.

-    **Ifc Properties|Map|Hidden**: IFC properties of this object.

-    **Ifc Type|Enumeration**: The IFC type of this object.


{{TitleProperty|IFC Attributes}}

-    **Description|String**: An optional description for this component

-    **Global Id|String**
    

-    **Object Type|String**
    

-    **Overall Height|Length**
    

-    **Overall Width|Length**
    

-    **Partitioning Type|Enumeration**
    

-    **Predefined Type|Enumeration**
    

-    **Tag|String**: An optional tag for this component.

-    **User Defined Partitioning Type|String**
    

### View


{{TitleProperty|Auto Group}}

-    **Autogroup Autosize|Bool**: Automatically set the capture box size from the Building Part contents. <small>(v0.20)</small> 

-    **Autogroup Box|Bool**: Turns auto grouping (and the display of the capture box) on/off. <small>(v0.20)</small> 

-    **Autogroup Margin|Length**: A margin to use when autosize is turned on. <small>(v0.20)</small> 

-    **Autogroup Size|IntegerList**: The capture box for newly created objects expressed as \[XMin,YMin,ZMin,XMax,YMax,ZMax\]. <small>(v0.20)</small> 


{{TitleProperty|Building Part}}

-    **Diffuse Color|ColorList|Hidden**: The individual face colors.

-    **Display Offset|Placement**: A transformation to apply to the level mark.

-    **Font Name|Font**: The font to be used for texts.

-    **Font Size|Length**: The font size of texts.

-    **Line Width|Float**: The line width of this object.

-    **Origin Offset|Bool**: If true, when activated, Display offset will affect the origin mark too.

-    **Override Unit|String**: An optional unit to express levels.

-    **Show Label|Bool**: If true, when activated, the object\'s label is displayed.

-    **Show Level|Bool**: If true, show the level.

-    **Show Unit|Bool**: If true, show the unit on the level tag.


{{TitleProperty|Children}}

-    **Children Line Color|Color**: The line color to apply to the children of this Building Part.

-    **Children Line Width|Float**: The line width to apply to the children of this Building Part.

-    **Children Override|Bool**: If true, the objects contained in this Building Part will adopt these line, color and transparency settings.

-    **Children Shape Color|Color**: The shape color to apply to the children of this Building Part.

-    **Children Transparency|Percent**: The transparency to apply to the children of this Building Part.


{{TitleProperty|Clip}}

-    **Auto Cut View|Bool**: Turn cutting on when activating this level.

-    **Cut Margin|Length**: The distance between the level plane and the cut line.

-    **Cut View|Bool**: Cut the view above this level.


{{TitleProperty|Interactions}}

-    **Auto Working Plane|Bool**: If set to True, the working plane will be kept on Auto mode.

-    **Double Click Activates|Bool**: If True, double-clicking this object in the tree activates it.

-    **Restore View|Bool**: If set, the view stored in this object will be restored on double-click.

-    **Save Inventor|Bool**: If this is enabled, the inventor representation of this object will be saved in the FreeCAD file, allowing to reference it in other files in lightweight mode.

-    **Saved Inventor|FileIncluded|Hidden**: A slot to save the inventor representation of this object, if enabled.

-    **Set Working Plane|Bool**: If true, when activated, the working plane will automatically adapt to this Building Part.

-    **View Data|FloatList|Hidden**: Camera position data associated with this object.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Parte di edificio può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


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
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/it
