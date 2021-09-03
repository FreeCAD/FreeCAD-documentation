---
- GuiCommand:/it
   Name:Draft Point
   Name/it:Punto
   Workbenches:[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   MenuLocation:Draft →  Punto
   Shortcut:**P** **T**
   SeeAlso:[Aggiungi punto](Draft_AddPoint/it.md), [Linea](Draft_Line/it.md), [Polilinea](Draft_Wire/it.md)
   Version:0.7
---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Draft_Point.svg  style="width:16px;"> Punto crea un semplice punto nel [piano di lavoro](Draft_SelectPlane/it.md) corrente, utilizzabile come riferimento per posizionare successivamente delle linee, polilinee, o altri oggetti. Assume [il tipo di linea e il colore](Draft_Linestyle/it.md) impostati nella [barra di Draft](Draft_Tray/it.md).


</div>

<img alt="" src=images/Draft_point_example.jpg  style="width:400px;">

## Utilizzo

See also: [Draft Tray](Draft_Tray.md), [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_Point.svg" width=16px> Punto
**, o premere i tasti **P** e **T**
2.  Selezionare un punto nella vista 3D, oppure digitare le sue [coordinate ](Draft_Coordinates/it.md) e poi premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [aggiungi punto](Draft_AddPoint/it.md)**.


</div>

## Opzioni

The single character keyboard shortcuts available in the task panel can be changed. See [Draft Preferences](Draft_Preferences.md). The shortcuts mentioned here are the default shortcuts.


<div class="mw-translate-fuzzy">

-   Per inserire le coordinate manualmente, è sufficiente inserire i numeri, quindi premere **Invio** per ciascun componente X, Y e Z.. È possibile premere il pulsante **<img src="images/Draft_AddPoint.svg" width=16px> [Inserisci punto](Draft_AddPoint/it.md)** quando si hanno i valori desiderati per inserire il punto.
-   Premere il tasto **T** o fare clic sulla casella di controllo per attivare la modalità *continua*. Se la modalità continua è attiva, lo strumento punto viene riavviato dopo aver posizionato un punto, consentendo di posizionarne un altro senza premere nuovamente il pulsante dello strumento.
-   Premere il tasto **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.


</div>

## Notes

-   Use <img alt="" src=images/Draft_Snap_Near.svg  style="width:16px;"> [Draft Snap Near](Draft_Snap_Near.md) to snap to Draft points.

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Proprietà

See also: [Property editor](Property_editor.md).

A Draft Point object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{TitleProperty|Draft}}


<div class="mw-translate-fuzzy">

-    {{ProprietaDati|X}}: la coordinata X del punto.

-    {{ProprietaDati|Y}}: la coordonata Y del punto.

-    {{ProprietaDati|Z}}: la coordonata Z del punto.


</div>

### View


{{TitleProperty|Draft}}

-    **Pattern|Enumeration**: not used.

-    **Pattern Size|Float**: not used.

## Scripting


<div class="mw-translate-fuzzy">

## Script


**Vedere anche:**

[Draft API](Draft_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).


</div>


<div class="mw-translate-fuzzy">

Lo strumento Punto può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) utilizzando la seguente funzione:


</div>


```python
point = make_point(X=0, Y=0, Z=0, color=None, name="Point", point_size=5)
point = make_point(point, Y=0, Z=0, color=None, name="Point", point_size=5)
```


<div class="mw-translate-fuzzy">

-   Crea un oggetto `Point` con le coordinate specicate in `X`, `Y` e `Z`, con unità in millimetri. Se non vengono fornite coordinate, il punto viene creato all\'origine (0,0,0).
    -   Se `X` è un `point` definito da un `FreeCAD.Vector`, esso viene usato.

-    `color`è una tupla `(R, G, B)` che indica il colore del punto nella scala RGB; ogni valore nella tupla deve essere compreso nell\'intervallo tra `0` e `1`.

-    `name`è il nome dell\'oggetto.

-    `point_size`è la dimensione dell\'oggetto in pixel, se viene caricata l\'interfaccia utente grafica.


</div>

Esempio:


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

point1 = Draft.make_point(1600, 1400, 0)

p2 = App.Vector(-3200, 1800, 0)
point2 = Draft.make_point(p2, color=(0.5, 0.3, 0.6), point_size=10)

doc.recompute()
```

Esempio:


<div class="mw-translate-fuzzy">

Questo codice crea `N` punti casuali all\'interno di un quadrato di lato `2L`. Crea un anello creando `N` punti, che possono apparire ovunque da `-L` a `+ L` su X e Y; inoltre sceglie un colore e una dimensione casuali per ciascun punto. Cambiare `N` per cambiare il numero di punti e cambiare `L` per cambiare l\'area coperta dai punti.


</div>


```python
import random
import FreeCAD as App
import Draft

doc = App.newDocument()

L = 1000
centered = App.Placement(App.Vector(-L, -L, 0), App.Rotation())
rectangle = Draft.make_rectangle(2*L, 2*L, placement=centered)

N = 10
for i in range(N):
    x = 2*L*random.random() - L
    y = 2*L*random.random() - L
    z = 0
    r = random.random()
    g = random.random()
    b = random.random()
    size = 15*random.random() + 5
    Draft.make_point(x, y, z, color=(r, g, b), point_size=size)

doc.recompute()
```


<div class="mw-translate-fuzzy">





</div>


 
