---
- GuiCommand   */it
   Name   *Draft SelectPlane
   Name/it   *Seleziona il piano
   MenuLocation   *Draft → Utilità → Seleziona il piano
   Workbenches   *[Draft](Draft_Workbench/it.md), [Architettura](Arch_Workbench/it.md)
   Shortcut   ***W** **P**
   SeeAlso   *[Piano proxy](Draft_SetWorkingPlaneProxy/it.md), [Mostra la griglia](Draft_ToggleGrid/it.md)
---

# Draft SelectPlane/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Il modulo Draft dispone di un sistema di Piani di lavoro, questo consente di specificare un piano personalizzato nello spazio 3D nel quale viene eseguito il comando successivo di Draft.

Esistono diversi metodi per definire il piano di lavoro   *

-   Da una faccia selezionata
-   Da tre vertici selezionati
-   Dalla vista corrente.
-   Da una preimpostazione   * dall\'altoe, anteriore o laterale.
-   Nessuna, nel qual caso il piano di lavoro viene adattato automaticamente alla vista corrente quando si avvia un comando o a una faccia se si inizia a disegnare su una faccia esistente.


</div>

<img alt="" src=images/WorkingPlane_example.png  style="width   *400px;">


<div class="mw-translate-fuzzy">



*È possibile impostare diversi piani di lavoro su cui disegnare forme*


</div>

## Usage with pre-selection 


<div class="mw-translate-fuzzy">

1.  Selezionare una faccia di un oggetto esistente nella vista 3D o tenere premuto **Ctrl** e selezionare tre vertici di qualsiasi oggetto. {{Version/it|0.17}}
2.  Premere il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona il piano](Draft_SelectPlane/it.md)**, oppure fare clic con il tasto destro e selezionare **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona il piano](Draft_SelectPlane/it.md)**.


</div>

## Usage with post-selection 

1.  There are several ways to invoke the command   *
    -   Press the **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft SelectPlane](Draft_SelectPlane.md)** button in the [Draft Tray](Draft_Tray.md). Depending on the current working plane this button can look different.
    -   Select the **Utilities → <img src="images/Draft_SelectPlane.svg" width=16px> Select Plane** option from the menu.
    -   Use the keyboard shortcut   * **W** then **P**.
2.  The **Working plane setup** task panel opens. See [Options](#Options.md) for more information.
3.  Do one of the following   *
    -   Select a single object. See the [previous paragraph](#Usage_with_pre-selection.md) for the supported objects.
    -   Select one or more subelements. You can select   *
        -   A flat face.
        -   Three vertices.
4.  Click anywhere in the [3D view](3D_view.md) to confirm the selection and finish the command.
5.  The working plane and the button in the [Draft Tray](Draft_Tray.md) are updated.

## Usage with presets 


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona il piano](Draft_SelectPlane/it.md)**, o usare **Draft** → **Utilità** → **<img src="images/Draft_SelectPlane.svg" width=16px> [Seleziona il piano](Draft_SelectPlane/it.md)** dal menu principale, o la scorciatoia **W** **P**.
2.  Selezionare l\'offset, la spaziatura della griglia e delle linee principali
3.  Selezionare uno dei preset   * **<img src="images/View-top.svg" width=16px> XY (dall'alto)**, **<img src="images/View-front.svg" width=16px> XZ (frontale)**, **<img src="images/View-right.svg" width=16px> YZ (laterale)**, **<img src="images/View-isometric.svg" width=16px> Vista**, o **<img src="images/View-axonometric.svg" width=16px> Auto**.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   Premere il pulsante **<img src="images/View-top.svg" width=16px> XY (dall'alto)** per impostare il piano di lavoro sul piano XY. Per disegnare facilmente su questo piano, è necessario impostare la vista dall\'alto o dal basso (la normale è nella direzione Z positiva o negativa). Premere **2** o **5** per passare rapidamente a queste viste.
-   Premere il pulsante **<img src="images/View-front.svg" width=16px> XZ (frontale)** per impostare il piano di lavoro sul piano XZ. Per disegnare facilmente su questo piano, è necessario impostare la vista anteriore o posteriore (la normale è nella direzione Y negativa o positiva). Premere **1** o **4** per passare rapidamente a queste viste.
-   Premere il pulsante **<img src="images/View-right.svg" width=16px> YZ (laterale)** per impostare il piano di lavoro sul piano YZ. Per disegnare facilmente su questo piano, è necessario impostare la vista sul lato sinistro o destro (la normale è nella direzione X positiva o negativa). Premere **3** o **6** per passare rapidamente a queste viste.
-   Premere il pulsante **<img src="images/View-isometric.svg" width=16px> Vista** per impostare il piano di lavoro sulla vista 3D corrente, perpendicolare all\'asse della telecamera e passante attraverso l\'origine (0,0,0).
-   Premere il pulsante **<img src="images/View-axonometric.svg" width=16px> Auto** per annullare l\'impostazione di qualsiasi piano di lavoro corrente e impostare automaticamente un piano di lavoro quando viene utilizzato uno strumento. Quando viene selezionato uno strumento di disegno, la griglia verrà automaticamente aggiornata alla vista corrente; quindi, se la vista viene ruotata e viene selezionato un altro strumento, la griglia viene ridisegnata nella nuova vista. Questo equivale a premere automaticamente **<img src="images/View-isometric.svg" width=16px> Vista** prima di usare uno strumento.
-   Impostare il valore \"Offset\" per impostare il piano di lavoro a una certa distanza perpendicolare dal piano selezionato.
-   Impostare il valore \"Spaziatura griglia\" per definire lo spazio tra ciascuna linea nella griglia.
-   Impostare il valore \"Linea principale ogni\" per tracciare una linea leggermente più spessa nella griglia al valore impostato. Ad esempio, se la spaziatura della griglia è di 0,5 m, e c\'è una linea principale ogni 20 linee, ci sarà una linea leggermente più spessa ogni 10 m.
-   Fare clic sulla casella di controllo \"Centra il piano nella vista\" per disegnare il piano e la griglia più vicino alla vista della telecamera nella vista 3D.
-   Premere **Esc** o il pulsante {{button|Chiudi}} per interrompere il comando corrente.
-   \* La griglia visualizza un bordo aggiuntivo con la spaziatura delle linee principali indicata nell\'angolo in basso a sinistra {{Version/it|0.19}}. Questo può essere disabilitato tramite Modifica-\> Preferenze-\> Draft-\> Griglia e snap-\> Mostra il bordo della griglia


</div>

## Notes

-   It can be useful to align the [3D view](3D_view.md) with the selected Draft working plane. For example after switching the working plane to Front you may want to switch to the [Front view](Std_ViewFront.md) as well.
-   The grid can be toggled with the [Draft ToggleGrid](Draft_ToggleGrid.md) command.
-   By double-clicking [Draft WorkingPlaneProxies](Draft_WorkingPlaneProxy.md) in the [Tree view](Tree_view.md) you can quickly switch between working planes.

## Preferences

See also   * [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   The grid settings in the task panel as well as several other grid settings are available as preferences   * **Edit → Preferences... → Draft → Grid and snapping → Grid**.
-   To use the grid the **Edit → Preferences... → Draft → Grid and snapping → Grid → Use grid** option must be selected. After changing this preference you must restart FreeCAD.
-   The Snapping radius can also be changed on-the-fly (see [Draft Snap](Draft_Snap#Preferences.md)) or by changing   * **Tools → Edit parameters... → BaseApp → Preferences → Mod → Draft → snapRange**.

## Scripting


<div class="mw-translate-fuzzy">

## Script


{{emphasis|Vedere anche   *}}

[Draft API](Draft_API/it.md) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md). Vedere le [WorkingPlane API](http   *//www.freecadweb.org/api/DraftWorkingPlane.html).


</div>


<div class="mw-translate-fuzzy">

È possibile accedere al corrente piano di lavoro di Draft e applicare delle trasformazioni   *


</div>


```python
# This code only works if the Draft Workbench is active!

import FreeCAD as App
import FreeCADGui as Gui

workplane = App.DraftWorkingPlane

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
Gui.Snapper.toggleGrid()
Gui.Snapper.toggleGrid()
```


<div class="mw-translate-fuzzy">

È possibile creare un proprio piano e utilizzarlo indipendentemente dal piano di lavoro corrente di Draft. Ciò è utile se è necessario eseguire calcoli o proiezioni in questi altri piani.


</div>


```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/it
