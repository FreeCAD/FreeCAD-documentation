---
 GuiCommand:
   Name: FCGear InvoluteGear
   Name/it: Ingranaggio ad evolvente
   MenuLocation: Gear , Involute Gear
   Workbenches: FCGear_Workbench/it
   Shortcut: None
   Version: v0.16
   SeeAlso: FCGear_CycloideGear/it
---

# FCGear InvoluteGear/it



## Descrizione

Grazie al rapporto di ingranamento favorevole e alla produzione relativamente semplice, la dentatura ad evolvente è la forma del dente più comune nell\'ingegneria meccanica. Le ruote dentate si trovano ovunque sia necessario trasferire movimento e forza da una parte all\'altra. Si trovano, ad esempio, nelle macchine, nelle automobili, negli orologi o negli elettrodomestici. Il movimento viene spesso trasferito direttamente da una ruota dentata all\'altra, ma talvolta anche tramite una catena. Inoltre è possibile modificare il senso di rotazione. È anche possibile trasformare un movimento radiale in uno lineare tramite una [cremagliera ad evolvente](FCGear_InvoluteRack/it.md).

![](images/Involute-Gear_example.png ) 
*Da sinistra a destra: ingranaggio cilindrico, ingranaggio elicoidale, ingranaggio elicoidale doppio*



## Utilizzo

1.  Passare a <img alt="" src=images/FCGear_workbench_icon.svg  style="width:16px;"> [FCGear](FCGear_Workbench/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **[<img src=images/FCGear_InvoluteGear.svg style="width:16px"> [Involute Gear](FCGear_InvoluteGear/it.md)** nella barra degli strumenti.
    -   Selezionare l\'opzione **Gear → [<img src=images/FCGear_InvoluteGear.svg style="width:16px"> Involute Gear** dal menu.
3.  Modificare ogni parametro dell\'ingranaggio alle condizioni richieste (vedere [Proprietà](#Proprietà.md)).



## Proprietà

Un oggetto FCGear InvoluteGear deriva da un oggetto [Part Feature](Part_Feature/it.md) ed eredita tutte le sue proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{Properties_Title|accuracy}}


<div class="mw-translate-fuzzy">

-    **numpoints|Integer**: L\'impostazione predefinita è {{Value|6}}. Modifica del profilo dell\'evolvente. La variazione di questo valore può portare a risultati imprevisti.

-    **simple|Bool**: Il valore predefinito è {{False}}, {{True}} genera una visualizzazione semplificata (senza denti e solo un cilindro col diametro primitivo).


</div>


{{Properties_Title|base}}


<div class="mw-translate-fuzzy">

-    **height|Length**: Il valore predefinito è {{Value|5 mm}}. Valore della larghezza dell\'ingranaggio.

-    **module|Length**: L\'impostazione predefinita è {{Value|1 mm}}. Il modulo è il rapporto tra il diametro di riferimento dell\'ingranaggio diviso per il numero di denti (vedere [Note](#Note.md)).

-    **teeth|Integer**: L\'impostazione predefinita è {{Value|15}}. Numero di denti (vedere [Note](#Note.md)).


</div>


{{Properties_Title|computed}}


<div class="mw-translate-fuzzy">

-    **angular_backlash|Angle**: (sola lettura)

-    **da|Length**: (sola lettura) Diametro esterno, misurato all\'addendum (la testa dei denti).

-    **df|Length**: (sola lettura) Diametro di fondo, misurato ai piedi dei denti.

-    **dw|Length**: (sola lettura) Diametro primitivo di lavoro.

-    **transverse_pitch|Length**: (sola lettura) Passo nel piano di rotazione.


</div>


{{Properties_Title|fillets}}


<div class="mw-translate-fuzzy">

-    **head_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.

-    **root_fillet|Float**: L\'impostazione predefinita è {{Value|0 mm}}.

-    **undercut|Bool**: L\'impostazione predefinita è {{False}}, {{True}} cambia il profilo del dente sul fondo (vedere [Note](#Note.md)).


</div>


{{Properties_Title|helical}}


<div class="mw-translate-fuzzy">

-    **beta|Angle**: L\'impostazione predefinita è {{Value|0 °}}. Con l\'angolo dell\'elica β viene creato un ingranaggio elicoidale -- valore positivo → senso di rotazione destra, valore negativo → senso di rotazione sinistra (vedere [Note](#Note.md)).

-    **double_helix|Bool**: L\'impostazione predefinita è {{False}}, {{True}} crea un ingranaggio a doppia elica (vedere [Note](#Note.md)).

-    **properties_from_tool|Bool**: L\'impostazione predefinita è {{False}}. Se {{True}} e **beta** non è zero, i parametri dell\'ingranaggio vengono ricalcolati internamente per l\'ingranaggio ruotato.


</div>


{{Properties_Title|hole}}

-    **Axle_hole|Bool**: Default is {{False}}. {{True}} enables a central hole for an axle.

-    **Axle_holesize|Length**: Default is {{Value|10 mm}}. Diameter of the hole for an axle.

-    **offset_hole|Bool**: Default is {{False}}, {{True}} enables an offset hole.

-    **offset_holeoffset|Length**: Default is {{Value|10 mm}}. The offset of the offset hole.

-    **offset_holesize|Length**: Default is {{Value|10 mm}}. The diameter of the offset hole.


{{Properties_Title|involute}}

-    **pressure_angle|Angle**: Il valore predefinito è {{Value|20 °}} (vedere [Note](#Note.md)).

-    **shift|Float**: Il valore predefinito è {{Value|0}}. Genera uno spostamento del profilo positivo o negativo (vedere [Note](#Note.md)).


{{Properties_Title|tolerance}}

-    **backlash|Length**: L\'impostazione predefinita è {{Value|0}}. Il gioco, chiamato anche aria o spaziatura, è la distanza tra i denti di una coppia di ingranaggi.

-    **clearance|Float**: L\'impostazione predefinita è {{Value|0.25}} (vedere [Note](#Note.md)).

-    **head|Float**: L\'impostazione predefinita {{Value|0}}. Questo valore viene utilizzato per modificare l\'altezza del dente.

-    **reversed_backlash|Bool**: {{True}} diminuzione del gioco o {{False}} (predefinito) aumento del gioco vedere [Note](#Note.md)).


{{Properties_Title|version}}

-    **version|String**:



## Note

-    **beta**: Quando viene modificato **beta**, cambia anche **diametro primitivo**. La seguente formula illustra come interagiscono i parametri: d = m \* Z / cos beta (Z = numero di denti, d = diametro primitivo, m = modulo). Ciò significa che per la ruota dentata cilindrica: cos beta = 0 e per la ruota elicoidale: cos beta \> 0. Tuttavia un angolo dell\'elica inferiore a 10° non presenta quasi alcun vantaggio rispetto ai denti diritti.

-    **clearance**: In una coppia di ingranaggi, il gioco è la distanza tra la testa del dente del primo ingranaggio e il piede del dente del secondo ingranaggio.

-    **double_gear**: Per utilizzare la doppia dentatura elicoidale è necessario prima inserire l\'angolo dell\'elica β (**beta**) per la dentatura elicoidale.

-    **module**: Utilizzando le linee guida ISO (Organizzazione internazionale per la standardizzazione), la dimensione del modulo è designata come l\'unità che rappresenta le dimensioni dei denti degli ingranaggi. Modulo (m): m = 1 (p = 3.1416), m = 2 (p = 6.2832), m = 4 (p = 12.566). Se si moltiplica il modulo per pigreco, si può ottenere il passo (p). Il passo è la distanza tra i punti corrispondenti dei denti adiacenti.

-    **shift**: Lo spostamento del profilo non viene utilizzato semplicemente per prevenire il sottosquadro. Può essere utilizzato per regolare la distanza centrale tra due ingranaggi. Se viene applicata una correzione positiva, tale da prevenire il sottosquadro in un pignone, lo spessore del dente nella parte superiore è più sottile.

-    **teeth**: Se si cambia il numero di denti, cambia anche il diametro primitivo (**dw**).

-    **undercut**: Il sottosquadro viene utilizzato quando il numero di denti di un ingranaggio è troppo piccolo. Altrimenti l\'ingranaggio di accoppiamento taglia il piede del dente. Il sottosquadro non solo indebolisce il dente come un vitino di vespa, ma rimuove anche parte dell\'evolvente utile adiacente al cerchio di base.

-    **pressure_angle**: 20° è un valore standard in questo caso. L\'angolo di pressione è definito come l\'angolo tra la linea d\'azione (tangente comune ai cerchi di base) e una perpendicolare alla linea dei centri. Pertanto, per gli ingranaggi standard, gli ingranaggi con angolo di pressione di 14,5° hanno i cerchi di base molto più vicini ai piedi dei denti rispetto agli ingranaggi da 20°. È per questo motivo che gli ingranaggi da 14,5° incontrano maggiori problemi di sottosquadro rispetto agli ingranaggi da 20°. Importante. l\'angolo di pressione cambia con uno spostamento del profilo. Modificare il parametro solo se si dispone di una conoscenza sufficiente della geometria dell\'ingranaggio.

-    **reversed_backlash**: Se sono presenti più ingranaggi, prestare attenzione per quale ingranaggio viene impostato il parametro.



## Limitazioni

Un profilo del dente 2D, ottenuto impostando **height** su zero, non può essere utilizzato con funzionalità che richiedono una forma 2D. Ad esempio, le funzioni [PartDesign: Estrusione](PartDesign_Pad/it.md) e [PartDesign: Elica additiva](PartDesign_AdditiveHelix/it.md) non accettano tale profilo come base. Per i dettagli tecnici, fare riferimento al relativo [issue su GitHub](https://github.com/looooo/freecad.gears/issues/97).



## Formule utili 



### Ingranaggi cilindrici standard 

Qui "standard" si riferisce a quegli ingranaggi cilindrici senza coefficiente di spostamento del profilo ($x$).

+++++
| Simbolo  | Termine                                          | Formula                          | Parametro FCGear                        |
+==========+==================================================+==================================+=========================================+
| $m$      | *Modulo*                                         | \-                               | $\texttt{module}$                       |
+++++
| $z$      | *Numero di denti*                                | \-                               | $\texttt{teeth}$                        |
+++++
| $\alpha$ | *Pressure Angle*                                 | Tipicamente, $\alpha = 20^\circ$ | $\texttt{pressure} {\_} \texttt{angle}$ |
+++++
| $d$      | *Diametro di riferimento* o *Diametro primitivo* | $z \cdot m$                      | $\texttt{dw}$                           |
+++++
| $h^*_a$  | *Coefficiente di Addendum*                       | Tipicamente, $h^*_a = 1$         | $h^*_a = 1 + \texttt{ head}$            |
+++++
| $h^*_f$  | *Coefficiente di Dedendum*                       | Tipicamente, $h^*_f = 1.25$      | $h^*_f = 1 + \texttt{ clearance}$       |
+++++
| $h_a$    | *Addendum*                                       | $h_a = h^*_a \cdot m$            | \-                                      |
+++++
| $h_f$    | *Dedendum*                                       | $h_f = h^*_f \cdot m$            | \-                                      |
+++++
| $h$      | *Altezza dente* o *Profondità dente*             | $h = h_a + h_f$                  | \-                                      |
|          |                                                  | Tipicamente, $h = 2.25 \cdot m$  |                                         |
+++++
| $x$      | *Coefficiente di spostamento del profilo*        | Per ingranaggi standard, $x = 0$ | $\texttt{shift}$                        |
+++++

: style=\"text-align: left;\" \| Formule base comuni agli ingranaggi cilindrici standard interni ed esterni

++++
| Simbolo | Termine             | Formula                                |
+=========+=====================+========================================+
| $d_a$   | *Diametro di testa* | $d_a = d + 2 \cdot h_a$                |
|         |                     | Tipicamente, $d_a = (z + 2) \cdot m$   |
++++
| $d_f$   | *Diametro di piede* | $d_f = d - 2 \cdot h_f$                |
|         |                     | Tipicamente, $d_f = (z - 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Formule di base specifiche per ingranaggi cilindrici standard esterni

++++
| Simbolo | Termine             | Formula                                |
+=========+=====================+========================================+
| $d_a$   | *Diametro di testa* | $d_a = d - 2 \cdot h_a$                |
|         |                     | Tipicamente, $d_a = (z - 2) \cdot m$   |
++++
| $d_f$   | *Diametro di piede* | $d_f = d + 2 \cdot h_f$                |
|         |                     | Tipicamente, $d_f = (z + 2.5) \cdot m$ |
++++

: style=\"text-align: left;\" \| Formule di base specifiche per ingranaggi cilindrici standard interni

++++
| Simbolo | Termine                   | Formula                         |
+=========+===========================+=================================+
| $a$     | *Distanza tra i centri*   | $a = \frac{d_1 + d_2}{2}$       |
++++
| $c$     | *Giogo tra testa e piede* | $c_1 = h_{f2} - h_{a1}$         |
|         |                           | $c_2 = h_{f1} - h_{a2}$         |
|         |                           | Tipicamente, $c = 0.25 \cdot m$ |
++++

: style=\"text-align: left;\" \| Formule di base specifiche per una coppia di ingranaggi cilindrici esterni standard

-   **Ingranaggi elicoidali e a doppia elica**
    -   
        **diametro primitivo (dw)**
        
        = **module** \* **teeth** : **cos beta**

    -   
        **interasse**
        
        = **(diametro primitivo (dw) 1 + diametro primitivo (dw) 2)** : 2

    -   
        **diametro addendum**
        
        = **diametro primitivo (dw)** + 2 \* **modulo**

    -   
        **module**
        
        = **diametro primitivo (dw)** \* **cos beta** : **denti**



## Script

Utilizzare la potenza di Python per automatizzare la modellazione degli ingranaggi: 
```python
import FreeCAD as App
import freecad.gears.commands
gear = freecad.gears.commands.CreateInvoluteGear.create()
gear.teeth = 20
gear.beta = 20
gear.height = 10
gear.double_helix = True
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
```



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [FCGear](Category_FCGear.md) > [External Command Reference](Category_External%20Command%20Reference.md) > FCGear InvoluteGear/it
