---
- GuiCommand:
   Name: Arch_Rebar
   Name/it: Armatura
   MenuLocation: Arch - Strumenti armatura o 3D/BIM - Strumenti armatura
   Workbenches: [Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   Shortcut: **R** **B**
   SeeAlso: [Struttura](Arch_Structure/it.md), [Ambiente Reinforcement](Reinforcement_Workbench/it.md)
---

# Arch Rebar/it


</div>



## Descrizione

Lo strumento Armatura permette di posizionare delle [barre di rinforzo](http://en.wikipedia.org/wiki/Rebar) negli oggetti [Struttura](Arch_Structure/it.md).

Lo strumento **Armatura** è anche integrato in [BIM](BIM_Workbench/it.md).

Gli oggetti Armature sono basati su profili 2D come gli [schizzi](Sketcher_Workbench/it.md) o gli [oggetti draft](Draft_Workbench/it.md), che devono essere disegnati su una faccia di un oggetto struttura. Dopo la creazione è possibile modificare la configurazione delle armature, come il numero e il diametro delle barre, o la distanza tra le estremità dell\'elemento strutturale.

<img alt="" src=images/Arch_Rebar_example.jpg  style="width:400px;"> 
*Oggetto strutturale con due schizzi disegnati sulle sue facce, che vengono poi trasformati in due serie di oggetti armature*



## Estensione disponibile 


<div class="mw-translate-fuzzy">

Lo strumento Armatura è potenziato dall\'ambiente [Reinforcement](Reinforcement_Workbench/it.md), che viene installato dal [Addon Manager](Std_AddonMgr/it.md). I tipi di barre di armatura aggiuntivi disponibili con l\'addon sono:

-   <img alt="" src=images/Arch_Rebar_Straight.svg  style="width:32px;"> [Armatura dritta](Arch_Rebar_Straight/it.md)
-   <img alt="" src=images/Arch_Rebar_UShape.svg  style="width:32px;"> [Armatura ad U](Arch_Rebar_UShape/it.md)
-   <img alt="" src=images/Arch_Rebar_LShape.svg  style="width:32px;"> [Armatura ad L](Arch_Rebar_LShape/it.md)
-   <img alt="" src=images/Arch_Rebar_BentShape.svg  style="width:32px;"> [Armatura sagomata](Arch_Rebar_BentShape/it.md)
-   <img alt="" src=images/Arch_Rebar_Stirrup.svg  style="width:32px;"> [Staffe](Arch_Rebar_Stirrup/it.md)
-   <img alt="" src=images/Arch_Rebar_Helical.svg  style="width:32px;"> [Armatura elicoidale](Arch_Rebar_Helical/it.md)


</div>



## Utilizzo

1.  Passare nell\'ambiente <img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Arch](Arch_Workbench/it.md)
2.  Creare un elemento **<img src="images/Arch_Structure.svg" width=16px> [Struttura](Arch_Structure/it.md)**.
3.  Passare nell\'ambiente <img alt="" src=images/Workbench_Sketcher.svg  style="width:16px;"> [Sketcher](Sketcher_Workbench/it.md).
4.  Selezionare una faccia dell\'elemento strutturale.
5.  Premere il pulsante **<img src="images/Sketcher_NewSketch.svg" width=16px> [Crea uno schizzo](Sketcher_NewSketch/it.md)** per iniziare un nuovo schizzo sulla faccia selezionata.
6.  Disegnare la sagoma dell\'armatura.
7.  Premere il pulsante **<img src="images/Sketcher_LeaveSketch.svg" width=16px> [Esci](Sketcher_LeaveSketch/it.md)** per terminare lo schizzo.
8.  Tornare nell\'ambiente <img alt="" src=images/Workbench_Arch.svg  style="width:16px;"> [Arch](Arch_Workbench/it.md).
9.  Selezionare lo schizzo appena disegnato.
10. Premere il pulsante **<img src="images/Arch_Rebar.svg" width=16px> [Armatura](Arch_Rebar/it.md)**, o i tasti **R** poi **B**.
11. Regolare le proprietà desiderate. Se qualcuna delle proprietà crea una situazione impossibile, l\'armatura potrebbe non apparire immediatamente, ad esempio, se il diametro del tondino è 0, o se la lunghezza offset è maggiore della lunghezza dell\'elemento struttura.

Anche se normalmente all\'interno di una struttura di Arch viene utilizzata una barra d\'armatura, da FreeCAD 0.19 l\'armatura può essere creata al di fuori di qualsiasi oggetto ospite. Per ospitare una barra di armatura all\'interno di un oggetto, basta impostare la sua proprietà **Host**.



## Opzioni

-   Gli elementi Armatura condividono le proprietà e i comportamenti comuni di tutti i [Componenti Arch](Arch_Component/it.md)
-   Il valore del raggio di piega viene espresso in n volte il diametro. Se la barra ha un diametro di 5 mm, un valore del raggio di piega 3 crea una curva con il raggio di 15 mm.
-   I valori di default per le nuove armature possono essere impostati nelle preferenze di Arch.
-   Se non è specificato un vettore di direzione, la direzione e la distanza lungo la quale le barre si propagano vengono calcolate automaticamente dall\'oggetto strutturale ospitante, utilizzando la direzione normale al disegno di base, e incassandolo nell\'oggetto struttura. Se si specifica un vettore di direzione, viene anche presa in considerazione la lunghezza di questo vettore.
-   La distanza viene calcolata secondo la quantità corrente di barre, e rappresenta la distanza tra gli assi delle barre. Quindi, per avere la dimensione dello spazio libero tra le barre è necessario sottrarre il diametro della barra.



## Proprietà

-    {{ProprietaDati|Amount}}: La quantità di barre.

-    {{ProprietaDati|Diameter}}: Il diametro delle barre.

-    {{ProprietaDati|Direction}}: La direzione (e lunghezza) lungo la quale le barre devono essere distribuite. Se il valore è (0,0,0), la direzione viene calcolata derivandola automaticamente dall\'oggetto strutturale ospitante.

-    {{ProprietaDati|Offset Start}}: La distanza di offset tra il bordo dell\'oggetto strutturale e la prima barra.

-    {{ProprietaDati|Offset End}}: La distanza di offset tra il bordo dell\'oggetto strutturale e l\'ultima barra.

-    {{ProprietaDati|Rounding}}: Un valore piega da applicare agli angoli delle barre, espresso in volte il diametro.

-    {{ProprietaDati|Spacing}}: La distanza tra gli assi di ogni barra.




<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[API Arch](Arch_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


**See also:**

[Arch API](Arch_API.md) and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).


<div class="mw-translate-fuzzy">

Lo strumento Armatura può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


</div>


```python
Rebar = makeRebar(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name="Rebar")
```

-   Crea un oggetto `Rebar` dal `baseobj` dato, che è una [Struttura](Arch_Structure/it.md), e da uno `sketch` come profilo.
    -   
        `diameter`
        
        , `amount`, e `offset` sono usati per definire le caratteristiche delle barre.

    -   Se non viene fornito nessun valore per `diameter`, `amount`, o `offset`, sono utilizzati i valori di default definiti nelle [Preferenze](Arch_Preferences/it.md) di Arch.

Esempio:


```python
import FreeCAD, Arch, Part

Structure = Arch.makeStructure(None, length=1000, width=1000, height=3000)
Structure.ViewObject.Transparency = 80
FreeCAD.ActiveDocument.recompute()

p1 = FreeCAD.Vector(-400, 400, 0)
p2 = FreeCAD.Vector(400, 400, 0)
Sketch = FreeCAD.ActiveDocument.addObject('Sketcher::SketchObject', 'Sketch')
Sketch.MapMode = "FlatFace"
Sketch.Support = [(Structure, "Face6")]
Sketch.addGeometry(Part.LineSegment(p1, p2))
FreeCAD.ActiveDocument.recompute()

Rebar = Arch.makeRebar(Structure, Sketch, diameter=80, amount=7, offset=50)
Rebar.OffsetStart = 100
Rebar.OffsetEnd = 100
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > [External Command Reference](Category_External Command Reference.md) > [Reinforcement](Category_Reinforcement.md) > [Arch](Arch_Workbench.md) > Arch Rebar/it
