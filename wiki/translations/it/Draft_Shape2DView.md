---
- GuiCommand:/it
   Name:Draft Shape2DView
   Name/it:Vista forma 2D
   MenuLocation:Modifiche → Vista forma 2D
   Workbenches:[Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   SeeAlso:[TechDraw Proietta forma](TechDraw_ProjectShape/it.md)
---

# Draft Shape2DView/it



## Descrizione

Il comando <img alt="" src=images/Draft_Shape2DView.svg  style="width:24px;"> **Draft Vista forma 2D** crea proiezioni 2D da oggetti selezionati, solitamente solidi 3D o [Arch Piani di sezione](Arch_SectionPlane/it.md). Le proiezioni vengono posizionate nella [Vista 3D](3D_view/it.md).

Le proiezioni Draft Vista forma 2D possono essere visualizzate su una pagina [TechDraw](TechDraw_Workbench/it.md) utilizzando il comando [TechDraw DraftView](TechDraw_DraftView/it.md). In alternativa, [TechDraw](TechDraw_Workbench/it.md) offre i propri comandi di proiezione. Ma questi creano proiezioni che vengono visualizzate solo sulla pagina di disegno e non nella [Vista 3D](3D_view/it.md).

![](images/Draft_Shape2DView_example.jpg ) 
*Proiezione di forme solide sul piano XY*



## Utilizzo

1.  Facoltativamente, ruotare la [Vista 3D](3D_view/it.md). La direzione della telecamera nella [Vista 3D](3D_view/it.md) determina il vettore di proiezione. Ad esempio, una [vista dall\'alto](Std_ViewTop/it.md) verrà proiettata sul piano XY. Il vettore di proiezione viene ignorato per le proiezioni create da [Arch Piano sezione](Arch_SectionPlane/it.md).
2.  Opzionalmente selezionare uno o più oggetti.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_Shape2DView.svg" width=16px> [Draft Vista forma 2D](Draft_Shape2DView/it.md)**.
    -   Selezionare l\'opzione **Modifiche → <img src="images/Draft_Shape2DView.svg" width=16px> Vista forma 2D** dal menu.
4.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
5.  Gli oggetti proiettati vengono creati sul piano XY.



## Come produrre piante e sezioni con spessori di linea diversi 

<img alt="" src=images/Draft_shape2dview_example_plan.png  style="width:700px;">

I disegni con spessori di linea diversi per le linee visualizzate e tagliate possono essere facilmente prodotti utilizzando due oggetti VistaForma2D da uno stesso [Arch Piano Sezione](Arch_SectionPlane/it.md). Uno degli oggetti VistaForma2D ha la sua modalità di proiezione impostata su **Solid**, che esegue il rendering delle linee visualizzate, e un altro impostato su **Cut lines** o **Cut faces** per eseguire il rendering del taglio linee. Le due viste shape2D vengono quindi posizionate nella stessa posizione, una sopra l\'altra.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Draft Vista Forma 2D è derivato da un [Part Part2DObject](Part_Part2DObject/it.md) e ne eredita tutte le proprietà. Ha anche le seguenti proprietà aggiuntive:

### Data


{{TitleProperty|Draft}}

-    **Auto Update|Bool**: specifica se la proiezione deve essere ricalcolata automaticamente se l\'oggetto **Base** cambia. Selezionare {{False}} può essere utile se ci sono molte Draft VistaForma2D in un documento o se sono complesse. Se impostato su {{False}} il comando [Aggiorna](Std_Refresh/it.md) deve essere utilizzato per aggiornare la proiezione. {{Version/it|0.20}}

-    **Base|Link**: specifica l\'oggetto da proiettare.

-    **Face Numbers|IntegerList**: specifica gli indici delle facce da proiettare. Funziona solo se **Projection Mode** è {{Value|Individual Faces}}.

-    **Fuse Arch|Bool**: specifica se [Oggetti Arch](Arch_Workbench/it.md) dello stesso tipo e materiale sono fusi o meno.

-    **Hidden Lines|Bool**: specifica se le linee nascoste vengono visualizzate o meno.

-    **In Place|Bool**: funziona solo se l\'oggetto selezionato è un [Arch Piano Sezione](Arch_SectionPlane/it.md) e **Projection Mode** è {{Value|Cutlines}} o {{Value |Cutfaces}}, specifica se la proiezione apparirà complanare al piano di sezione.

-    **Projection|Vector**: specifica la direzione della proiezione. Ignorato se **Base** è un [Arch Piano Sezione](Arch_SectionPlane/it.md).

-    **Projection Mode|Enumeration**: specifica la modalità di proiezione. Sono disponibili le seguenti modalità:

    -   
        {{Value|Solid}}
        
        : proietta l\'intero oggetto selezionato.

    -   
        {{Value|Individual Faces}}
        
        : proietta solo i volti nell\'elenco **Face Numbers**.

    -   
        {{Value|Cutlines}}
        
        : funziona solo se l\'oggetto selezionato è un [Arch Piano Sezione](Arch_SectionPlane/it.md), proietta solo i bordi tagliati dal piano di sezione.

    -   
        {{Value|Cutfaces}}
        
        : funziona solo se l\'oggetto selezionato è un [Arch Piano Sezione](Arch_SectionPlane/it.md), proietta le aree tagliate attraverso i solidi dal piano di sezione come facce.

    -   
        {{Value|Facce solide}}
        
        : proietta l\'intero oggetto selezionato tagliando le facce una per una. Può essere utilizzato se la modalità {{Value|Solid}} dà risultati errati. {{Version/it|0.20}}

-    **Segment Length|Float**: specifica la dimensione in millimetri dei segmenti lineari se **Tessellation** è `True`.

-    **Tessellation|Bool**: specifica se deve essere eseguita la tassellazione. La tassellatura significa che le curve vengono sostituite da sequenze di segmenti di linea. Questo può essere computazionalmente intenso se **Segment Length** è troppo breve.

-    **Visible Only|Bool**: specifica se la proiezione deve essere ricalcolata solo se è visibile.

-    **Exclusion Points|Vector list**: un elenco di punti di esclusione. Qualsiasi bordo che passa attraverso uno di questi punti non verrà disegnato. {{Version/it|0.20}}

-    **Exclusion Names|String list**ː un elenco di nomi oggetto. Qualsiasi oggetto figlio visualizzato o tagliato con un nome in quell\'elenco non verrà disegnato. {{Version/it|0.21}}



### Vista


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Per creare una proiezione 2D usare il metodo `make_shape2dview` ({{Version/it|0.19}}) del modulo Draft. Questo metodo sostituisce il metodo deprecato `makeShape2DView`.


```python
shape2dview = make_shape2dview(baseobj, projectionVector=None, facenumbers=[])
```

-    `baseobj`è l\'oggetto da proiettare.

-    `projectionVector`è il vettore di proiezione. Se non fornito viene utilizzato l\'asse Z.

-    `facenumbers`è un elenco di numeri di facce (in base 0). Se fornite vengono considerate solo queste facce.

-    `shape2dview`viene restituito con la proiezione 2D creata.

Se necessario, modificare la proprietà `ProjectionMode` dell\'oggetto creato. Può essere: `"Solid"`, `"Individual Faces"`, `"Cutlines"`, `"Cutfaces"` o `" Facce solide"`.

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

box = doc.addObject("Part::Box", "Box")
box.Length = 2300
box.Width = 500
box.Height = 1000

shape1 = Draft.make_shape2dview(box)

shape2 = Draft.make_shape2dview(box, App.Vector(1, -1, 1))

shape3 = Draft.make_shape2dview(box, App.Vector(-1, 1, 1), [0, 5])
shape3.ProjectionMode = "Individual Faces"

doc.recompute()
```



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Shape2DView/it
