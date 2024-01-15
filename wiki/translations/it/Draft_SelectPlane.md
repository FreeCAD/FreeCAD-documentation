---
 GuiCommand:
   Name: Draft SelectPlane
   Name/it: Seleziona Piano
   MenuLocation: Utilità , Seleziona Piano
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   Shortcut: **W** **P**
   SeeAlso: Draft_WorkingPlaneProxy/it
---

# Draft SelectPlane/it



## Descrizione

Il comando <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft Seleziona Piano** definisce il piano di lavoro Draft corrente. Questo è il piano nella [Vista 3D](3D_view/it.md) dove vengono creati i nuovi oggetti [Draft](Draft_Workbench/it.md). Un nuovo piano di lavoro può essere basato su una delle diverse [preimpostazioni](#Utilizzo_con_preimpostazioni.md) o su una selezione. La selezione può essere creata prima ([pre-selezione](#Utilizzo_con_pre-selezion.md)) o dopo ([post-selezione](#Utilizzo_wcon_post-selezione.md)) l\'avvio del comando.


{{Version/it|0.22}}

: Per ogni vista 3D viene memorizzato un piano di lavoro separato.

Il pulsante ![](images/Draft_tray_button_plane.png ) nel [Vassoio di Draft](Draft_Tray/it.md) cambia a seconda del piano di lavoro corrente. {{Version/it|0.22}}: se il piano di lavoro non è impostato su **Auto** viene aggiunto un asterisco (*****) all\'etichetta del pulsante se l\'origine del piano di lavoro non corrisponde l\'origine globale.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Forme create su diversi piani di lavoro*



## Utilizzo con pre-selezione 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare un singolo oggetto. Sono supportati i seguenti oggetti:
        -   [Draft Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md): la **View Data** (la posizione della telecamera) e la **Visibility Map** (la visibilità salvata degli oggetti) del piano di lavoro proxy sono anche ripristinati.
        -   [Arch Assi](Arch_Axis/it.md) ({{Version/it|0.22}})
        -   [Arch Sistema di Assi](Arch_AxisSystem/it.md) ({{Version/it|0.22}})
        -   [Arch Parti di edificio](Arch_BuildingPart/it.md).
        -   [Arch Piani di sezione](Arch_SectionPlane/it.md).
        -   [Oggetti Part](Std_Part/it.md): per evitare di selezionare sottoelementi si consiglia di selezionarli nella [Vista ad albero](Tree_view/it.md).
        -   Oggetti non solidi che consistono in una singola faccia piana o un singolo bordo curvo o ({{Version/it|0.22}}) che hanno tre o più vertici.
        -   Oggetti solidi o oggetti senza forma che hanno una proprietà **Placement**. ({{Version/it|0.22}})
    -   Selezionare uno o più sottoelementi. E\' possibile selezionare:
        -   Una faccia piatta.
        -   Un bordo curvo.
        -   Tre vertici.
        -   Uno spigolo e un vertice, oppure due spigoli. I vertici combinati devono definire un piano. ({{Version/it|0.22}})
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante ![](images/Draft_tray_button_plane.png ) nella [Barra Draft](Draft_Tray/it.md).
    -   Seleziona l\'opzione **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona Piano** dal menu.
    -   Usare la scorciatoia da tastiera: **W** poi **P**.
3.  Il piano di lavoro e il pulsante nella [Barra Draft](Draft_Tray/it.md) vengono aggiornati.



## Utilizzo con post-selezione 

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante ![](images/Draft_tray_button_plane.png ) nella [Barra Draft](Draft_Tray/it.md).
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona Piano** dal menu.
    -   Usare la scorciatoia da tastiera: **W** poi **P**.
2.  Si apre il pannello attività **Impostazione piano di lavoro**. Vedi [Opzioni](#Opzioni.md) per maggiori informazioni.
3.  Effettuare una delle seguenti operazioni:
    -   Selezionare un singolo oggetto. Vedere il [paragrafo precedente](#Utilizzo_con_pre-selezione.md).
    -   Selezionare uno o più sottoelementi. Vedere il [paragrafo precedente](#Utilizzo_con_preselezione.md).
4.  Fare clic in un punto qualsiasi della [Vista 3D](3D_view/it.md) per confermare la selezione e terminare il comando.
5.  Il piano di lavoro e il pulsante nella [Barra Draft](Draft_Tray/it.md) vengono aggiornati.



## Utilizzo con preimpostazioni 

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante ![](images/Draft_tray_button_plane.png ) nella [Barra Draft](Draft_Tray/it.md).
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona Piano** dal menu.
    -   Usare la scorciatoia da tastiera: **W** poi **P**.
2.  Si apre il pannello attività **Impostazione piano di lavoro**. Vedere [Opzioni](#Opzioni.md) per maggiori informazioni.
3.  Premere uno qualsiasi dei pulsanti per terminare il comando.
4.  Il piano di lavoro e il pulsante nella [Barra Draft](Draft_Tray/it.md) vengono aggiornati.



## Opzioni

-   Premere il pulsante **<img src="images/View-top.svg" width=16px> Dall'alto (XY)** per allineare il piano di lavoro con il piano XY del sistema di coordinate globale.

-   Premere il pulsante **<img src="images/View-front.svg" width=16px> Frontale (XZ)** per allineare il piano di lavoro con il piano XZ del sistema di coordinate globale.

-   Premere il pulsante **<img src="images/View-right.svg" width=16px> Laterale (YZ)** per allineare il piano di lavoro con il piano YZ del sistema di coordinate globale.

-   Premere il pulsante **<img src="images/View-isometric.svg" width=16px> Allinea alla vista** per allineare il piano di lavoro con la [Vista 3D](3D_view/it.md) corrente. Se la casella di controllo **Centra piano sulla vista** non è selezionata, l\'origine del piano di lavoro corrisponderà all\'origine del sistema di coordinate globali, altrimenti corrisponderà al centro dell\'attuale [Vista 3D](3D_view/it.md).

-   Premere il pulsante **<img src="images/View-axonometric.svg" width=16px> Automatico** per impostare il piano di lavoro su **Auto**. Un piano di lavoro impostato su **Auto** si allineerà automaticamente con la [Vista 3D](3D_view/it.md) corrente ogni volta che viene avviato un comando Draft o [Arch](Arch_Workbench/it.md) che richiede l\'immissione di punti. Ciò equivale a premere il pulsante **<img src="images/View-isometric.svg" width=16px> Allinea alla vista** prima di utilizzare il comando. Inoltre, il piano di lavoro si allineerà alle facce planari selezionate prima di avviare il comando o quando vengono selezionati punti sulle facce planari durante il comando.

-    **Offset**definisce la distanza perpendicolare tra il piano calcolato e il piano di lavoro effettivo.

-   Selezionare la casella **Centra piano su vista corrente** per mettere l\'origine del piano di lavoro al centro della [Vista 3D](3D_view/it.md) corrente. Questa opzione può essere utile in combinazione con il pulsante **<img src="images/View-isometric.svg" width=16px> Allinea alla vista**.

-   Selezionare un vertice nella [Vista 3D](3D_view/it.md) e premere il pulsante **<img src="images/Draft_Move.svg" width=16px> Sposta piano di lavoro** per spostare il piano di lavoro in modo che la sua origine corrisponda alla posizione del vertice selezionato.

-    **Spaziatura della griglia**definisce la distanza tra le linee della griglia.

-   Il valore **Linea principale ogni** determina dove vengono disegnate le linee principali della griglia. Le linee della griglia principale sono leggermente più spesse delle normali linee della griglia. Ad esempio, se la spaziatura della griglia è {{Value|0.5 m}} e c\'è una linea principale ogni {{Value|10 linee}}, tale linea si verificherà ogni {{Value|5 m}}.

-   Il valore **Estensione griglia** determina il numero di linee della griglia nelle direzioni X e Y della griglia.

-   Il **Raggio di aggancio** è la distanza massima alla quale [Draft Snap Grid](Draft_Snap_Grid/it.md) rileva le intersezioni delle linee della griglia.

-   Premere il pulsante **<img src="images/view-fullscreen.svg" width=16px> Centra la vista** per allineare la [vista 3D](3D_view/it.md) con il piano di lavoro corrente.

-   Premere il pulsante **<img src="images/sel-back.svg" width=16px> Precedente** per reimpostare il piano di lavoro nella posizione precedente.

-   Premere il pulsante **Successivo <img src="images/sel-forward.svg" width=16px>** per reimpostare il piano di lavoro nella posizione successiva. {{Version/it|0.22}}

-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Può essere utile allineare la [Vista 3D](3D_view/it.md) con il piano di lavoro Draft selezionato. Ad esempio, dopo aver impostato il piano di lavoro su Frontale, si potrebbe voler passare anche alla [Vista frontale](Std_ViewFront/it.md).
-   La griglia può essere commutata con il comando [Draft Attiva Griglia](Draft_ToggleGrid/it.md).
-   Facendo doppio clic su [Draft Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md) nella [Vista ad albero](Tree_view/it.md) è possibile passare rapidamente da un piano di lavoro all\'altro.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Le impostazioni della griglia nel pannello delle attività così come molte altre impostazioni della griglia sono disponibili come preferenze: **Modifica → Preferenze... → Draft → Griglia e snap**.
-   Il raggio di Aggancio può anche essere modificato al volo (vedi [Draft Snap](Draft_Snap/it#Preferenze.md)) o modificando: **Strumenti → Modifica parametri... → BaseApp → Preferences → Mod → Draft → snapRange**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).


{{Version/it|0.22}}

Il modulo WorkingPlane offre due classi per creare oggetti del piano di lavoro: la classe `PlaneBase` e la classe `PlaneGui`. La seconda classe eredita dalla prima. Gli oggetti della classe `PlaneGui` interagiscono con la GUI (il pulsante [Draft Tray](Draft_Tray/it.md)), la [vista 3D](3D_view/it.md) e la [griglia](Draft_Snap_Grid/it.md). Gli oggetti `PlaneBase` no.

Utilizzare il metodo `get_working_plane()` del modulo WorkingPlane per ottenere un\'istanza della classe `PlaneGui` collegata alla vista 3D corrente. Il metodo restituisce il piano di lavoro esistente collegato alla vista o crea un nuovo piano di lavoro, se necessario.


```python
import FreeCAD as App
import WorkingPlane

wp = WorkingPlane.get_working_plane()

origin = App.Vector(0, 0, 0)
normal = App.Vector(1, 1, 1).normalize()
offset = 17
wp.align_to_point_and_axis(origin, normal, offset)

point = App.Vector(10, 15, 2)
projection = wp.project_point(point)
print(projection)
```

La classe `PlaneBase` può essere utilizzata per creare piani di lavoro indipendenti dalla GUI:


```python
import WorkingPlane

wp = WorkingPlane.PlaneBase()
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/it
