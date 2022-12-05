---
- GuiCommand:/it
   Name:Draft Ellipse
   Name/it:Ellisse
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft → Ellisse
   Shortcut:**E** **L**
   SeeAlso:[Circonferenza](Draft_Circle/it.md), [Arco](Draft_Arc/it.md)
   Version:0.7
---

# Draft Ellipse/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Crea nel corrente [piano di lavoro](Draft_SelectPlane/it.md) una ellisse inscritta in un rettangolo. Per definire il rettangolo di contenimento inserire due vertici opposti. L\'ellisse assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati in precedenza nella [barra di Draft](Draft_Tray/it.md).


</div>


<div class="mw-translate-fuzzy">

Questo strumento può essere utilizzato anche per creare archi ellittici specificando l\'angolo di inizio e di fine. Per creare cerchi e archi circolari usare gli strumenti [Cerchio](Draft_Circle/it.md) e [Arco](Draft_Arc/it.md). Si può anche approssimare un arco ellittico o circolare usando gli strumenti [B-spline](Draft_BSpline/it.md) e [Curva di Bezier](Draft_BezCurve/it.md).


</div>

<img alt="" src=images/Draft_ellipse_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">



*Ellisse definita dagli angoli del rettangolo*


</div>

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Ellipse.svg" width=16px> [Ellisse](Draft_Ellipse/it.md)**, o premere i tasti **E** e poi **L**.
2.  Selezionare un primo punto nella vista 3D, oppure digitare le sue coordinate poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.
3.  Selezionare un secondo punto nella vista 3D, oppure digitare le sue coordinate poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> aggiungi punto**.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> Inserisci punto** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **R** oppure fare clic sulla casella di controllo per attivare la modalità \"relativo\". Se la modalità relativo è attiva, le coordinate del punto successivo sono relative all\'ultimo; in caso contrario, sono assolute, prese dall\'origine (0,0,0).
-   Premere il tasto **T** oppure fare clic sulla casella di controllo per attivare la modalità \"continua\". Se la modalità continua è attiva, lo strumento Ellisse si riavvia dopo aver terminato la figura in costruzione, e consente di disegnare una nuova ellisse senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **L** oppure fare clic sulla casella di controllo per attivare la modalità *riempito*. Se la modalità di riempimento è attiva, l\'ellisse chiusa crea una faccia piena (**Make Face** `True`); in caso contrario, l\'ellisse chiusa non crea una faccia (**Make Face** `False`).
-   Tenere premuto **Ctrl** mentre si disegna per forzare [l\'aggancio](Draft_Snap.md) del proprio punto alla posizione di aggancio più vicina, indipendentemente dalla distanza.
-   Tenere premuto **Maiusc** mentre si disegna per [vincolare](Draft_Constrain.md) il prossimo punto in orizzontale o in verticale rispetto all\'ultimo.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes

-   A Draft Ellipse can be edited with the [Draft Edit](Draft_Edit.md) command.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.
-   To change the initial value of filled mode: **Edit → Preferences... → Draft → General settings → Draft tools options → Fill objects with faces whenever possible**. Changing the filled mode in a task panel will override this preference for the current FreeCAD session.
-   If the **Edit → Preferences... → Draft → General settings → Draft tools options → Use Part Primitives when available** option is checked, the command will create a [Part Ellipse](Part_Ellipse.md) instead of a Draft Ellipse.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Ellipse object is derived from a [Part Part2DObject](Part_Part2DObject.md) and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Dati

-    **First Angle**: specifica l\'angolo del primo punto dell\'ellisse; normalmente 0°.

-    **Last Angle**: specifica l\'angolo dell\'ultimo punto dell\'ellisse; normalmente 0°.

-    **Major Radius**: specifica il raggio maggiore dell\'ellisse.

-    **Minor Radius**: specifica il raggio minore dell\'ellisse.

:   Se entrambi i raggi hanno lo stesso valore, l\'ellisse ha lo stesso aspetto di un [Cerchio](Draft_Circle/it.md).

-    **Make Face**: specifica se l\'ellisse crea una faccia o no. Se è `True` viene creata una faccia, altrimenti solo il perimetro è considerato parte dell\'oggetto. Questa proprietà funziona solo se la forma è un\'ellisse completa.

:   Per avere un\'ellisse completa le proprietà **First Angle** e **Last Angle** devono avere lo stesso valore; in caso contrario, viene visualizzato un arco ellittico. I valori 0° e 360° sono considerati uguali.


</div>

### View


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

### Vista

-    **Pattern**: specifica un [Modello](Draft_Pattern/it.md) di disegno con cui riempire la faccia della forma. Questa proprietà funziona solo se **Make Face** è `True`, e se **Display Mode** è \"Flat Lines\".

-    **Pattern Size**: specifica la dimensione del [Modello](Draft_Pattern/it.md) di disegno.


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Ellisse può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
ellipse = make_ellipse(majradius, minradius, placement=None, face=True, support=None)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Ellipse` dai dati di (`majradius`) e (`minradius`) in millimetri.
    -   Il valore più grande viene utilizzato per il raggio maggiore (asse X) se non viene fornito nessun altro posizionamento.
-   Se viene dato un `placement`, esso viene utilizzato; altrimenti la forma viene creata all\'origine.
-   Se `face` è `True`, l\'ellisse crea una faccia, cioè appare riempita.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

ellipse1 = Draft.make_ellipse(3000, 200)
ellipse2 = Draft.make_ellipse(700, 1000)

zaxis = App.Vector(0, 0, 1)
p3 = App.Vector(1000, 1000, 0)
place3 = App.Placement(p3, App.Rotation(zaxis, 90))

ellipse3 = Draft.make_ellipse(700, 1000, placement=place3)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Ellipse/it
