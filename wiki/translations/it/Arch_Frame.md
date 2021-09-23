---
- GuiCommand:/it
   Name:Arch Frame
   Name/it:Carpenteria
   MenuLocation:Arch → Carpenteria
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**F** **R**
   SeeAlso:[Parete](Arch_Wall/it.md), [Struttura](Arch_Structure/it.md)
---

# Arch Frame/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Arch_Frame.svg  style="width:16px;"> Carpenteria è utilizzato per costruire tutti i tipi di oggetti di carpenteria sulla base di un profilo e di un tracciato. Il profilo viene estruso lungo le linee del tracciato che può essere costituita da qualsiasi oggetto 2D, ad esempio, da uno [schizzo](Sketcher_Workbench/it.md), o da un [oggetto draft](Draft_Workbench/it.md). È particolarmente utile per creare ringhiere o pareti di carpenteria. Gli oggetti Carpenteria possono essere poi facilmente trasformati in oggetti [muri](Arch_Wall/it.md) o [strutture](Arch_Structure/it.md).


</div>

<img alt="" src=images/Arch_Frame_example.jpg  style="width:640px;">


<div class="mw-translate-fuzzy">


*Oggetto Carpenteria creato da una [schiera](Draft_Array/it.md) derivata da una [linea](Draft_Line/it.md), utilizzando un [cerchio](Draft_Circle/it.md) come profilo.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Creare un oggetto tracciato e un oggetto profilo, ad esempio con [Draft](Draft_Workbench/it.md) o con [Schizzo](Sketcher_Workbench/it.md).
2.  Selezionare l\'oggetto tracciato, poi, con **Ctrl** premuto, selezionare l\'oggetto profilo.
3.  Premere il pulsante **<img src="images/Arch_Frame.svg" width=16px> Carpenteria**, o premere i tasti **F** poi **R**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Gli elementi Carpenteria condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)
-   Impostando la sua proprietà Offset, l\'oggetto carpenteria può essere posizionato alla distanza voluta dall\'oggetto tracciato.
-   Il profilo viene copiato alla base di ciascun spigolo o linea dell\'oggetto tracciato, quindi estruso lungo esso. È possibile stabilire la posizione del profilo alla base di ogni linea del tracciato tramite le proprietà Align e Rotation.


</div>

### Proprietà

-    {{ProprietaDati|Base}}: Il tracciato su cui è basato l\'oggetto carpenteria.

-    {{ProprietaDati|Profile}}: Il profilo su cui è basato l\'oggetto carpenteria.

-    {{ProprietaDati|Align}}: Specifica se il profilo deve essere ruotato per posizionare il suo asse normale allineato con ciascuna linea del tracciato.

-    {{ProprietaDati|Offset}}: Una distanza opzionale tra l\'oggetto tracciato e l\'oggetto carpenteria.

-    {{ProprietaDati|Rotation}}: La rotazione del profilo attorno al suo asse di estrusione.


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Arch API](Arch_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Carpenteria può essere utilizzato nelle [macro](macros/it.md) e dalla [console di Python](FreeCAD_Scripting_Basics/it.md) tramite la seguente funzione:


</div>


```python
Frame = makeFrame(baseobj, profile)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Frame` da un dato `baseobj` e un `profile`.
    -   
        `baseobj`
        
        è qualsiasi oggetto che contenga dei contorni, come una [Polilinea](Draft_Wire/it.md) o una [Schiera](Draft_Array/it.md).

    -   
        `profile`
        
        è un oggetto 2D estrudibile contenente facce o contorni chiusi.


</div>

Esempio: 
```python
import Draft, Arch

Line = Draft.makeLine(FreeCAD.Vector(0, 0, 0), FreeCAD.Vector(0, 0, 2000))
baseobj = Draft.makeArray(Line, FreeCAD.Vector(1000, 0, 0), FreeCAD.Vector(0, 1, 0), 6, 1)

profile = Draft.makeCircle(200)
Frame = Arch.makeFrame(baseobj, profile)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/it
|[Nido](Arch_Nest/it.md)
|[Recinzione](Arch_Fence/it.md)
|[Arch](Arch_Workbench/it.md)
|IconL=Arch_Nest.svg
|IconC=Workbench_Arch.svg
|IconR=Arch_Fence.svg
}}


</div>

---
[documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Frame/it
