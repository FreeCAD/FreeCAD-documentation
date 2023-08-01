---
- GuiCommand:
   Name: Draft SelectPlane
   Name/it: Seleziona Piano
   MenuLocation: Utilità - Seleziona Piano
   Workbenches: [Draft](Draft_Workbench/it.md), [Arch](Arch_Workbench/it.md)
   Shortcut: **W** **P**
   SeeAlso: [Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md)
---

# Draft SelectPlane/it



## Descrizione

Il comando <img alt="" src=images/Draft_SelectPlane.svg  style="width:24px;"> **Draft Seleziona Piano** seleziona il piano di lavoro Draft corrente. Questo è il piano nella [Vista 3D](3D_view/it.md) dove vengono creati i nuovi oggetti [Draft](Draft_Workbench/it.md). Un nuovo piano di lavoro può essere basato su una delle diverse [preimpostazioni](#Utilizzo_con_preimpostazioni.md) o su una selezione. La selezione può essere creata prima ([pre-selezione](#Utilizzo_con_pre-selezion.md)) o dopo ([post-selezione](#Utilizzo_wcon_post-selezione.md)) l\'avvio del comando.

<img alt="" src=images/WorkingPlane_example.png  style="width:400px;"> 
*Forme create su diversi piani di lavoro*



## Utilizzo con pre-selezione 

1.  Effettuare una delle seguenti operazioni:
    -   Selezionare un singolo oggetto. Sono supportati i seguenti oggetti:
        -   [Draft Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md): la **View Data** (la posizione della telecamera) e la **Visibility Map** (la visibilità salvata degli oggetti) del piano di lavoro proxy sono anche ripristinati.
        -   [Arch Parti di edificio](Arch_BuildingPart/it.md).
        -   [Arch Piani di sezione](Arch_SectionPlane/it.md).
        -   [Oggetti Part](Std_Part/it.md): per evitare di selezionare sottoelementi si consiglia di selezionarli nella [Vista ad albero](Tree_view/it.md).
        -   [Funzioni Part](Part_Feature/it.md) oggetti che hanno una sola faccia. [Part Piani](Part_Plane/it.md) ad esempio.
        -   Oggetti che non sono [Funzioni Part](Part_Feature/it.md) e hanno una proprietà **Placement**.
    -   Selezionare uno o più sottoelementi. E\' possibile selezionare:
        -   Una faccia piatta.
        -   Tre vertici.
        -   Un bordo circolare.
        -   Due spigoli diritti che sono co-planari ma non co-lineari.
        -   Un bordo dritto e un vertice che non giace sul bordo (esteso).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Seleziona Piano](Draft_SelectPlane/it.md)** nella [Barra Draft](Draft_Tray/it.md). A seconda del piano di lavoro corrente, questo pulsante può avere un aspetto diverso.
    -   Seleziona l\'opzione **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona Piano** dal menu.
    -   Usare la scorciatoia da tastiera: **W** poi **P**.
3.  Il piano di lavoro e il pulsante nella [Barra Draft](Draft_Tray/it.md) vengono aggiornati.



## Utilizzo con post-selezione 

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Seleziona Piano](Draft_SelectPlane/it.md)** nella [Barra Drft](Draft_Tray/it.md). A seconda del piano di lavoro corrente, questo pulsante può avere un aspetto diverso.
    -   Selezionare l\'opzione **Utilità → <img src="images/Draft_SelectPlane.svg" width=16px> Seleziona Piano** dal menu.
    -   Usare la scorciatoia da tastiera: **W** poi **P**.
2.  Si apre il pannello attività **Impostazione piano di lavoro**. Vedi [Opzioni](#Opzioni.md) per maggiori informazioni.
3.  Effettuare una delle seguenti operazioni:
    -   Selezionare un singolo oggetto. Vedere il [paragrafo precedente](#Utilizzo_con_pre-selezione.md) per gli oggetti supportati.
    -   Selezionare uno o più sottoelementi. E\' possibile selezionare:
        -   Una faccia piatta.
        -   Tre vertici.
4.  Fare clic in un punto qualsiasi della [Vista 3D](3D_view/it.md) per confermare la selezione e terminare il comando.
5.  Il piano di lavoro e il pulsante nella [Barra Draft](Draft_Tray/it.md) vengono aggiornati.



## Utilizzo con preimpostazioni 

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_SelectPlane.svg" width=16px> [Draft Seleziona Piano](Draft_SelectPlane/it.md)** nella [Barra Draft](Draft_Tray.md). A seconda del piano di lavoro corrente, questo pulsante può avere un aspetto diverso.
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

-   Premere il pulsante **<img src="images/View-axonometric.svg" width=16px> Automatica** per allineare automaticamente il piano di lavoro con la [Vista 3D](3D_view/it.md) corrente ogni volta che un comando Draft o [Arch](Arch_Workbench/it.md) richiede l\'inserimento di un punto. Ciò equivale a premere il pulsante **<img src="images/View-isometric.svg" width=16px> Allinea alla vista** prima di utilizzare il comando.

-    **Offset**definisce la distanza perpendicolare tra il piano calcolato e il piano di lavoro effettivo.

-   Selezionare la casella **Centra piano su vista corrente** per mettere l\'origine del piano di lavoro al centro della [Vista 3D](3D_view/it.md) corrente. Questa opzione ha davvero senso solo se viene utilizzato il pulsante **<img src="images/View-isometric.svg" width=16px> Allinea alla vista**.

-   Selezionare un vertice nella [Vista 3D](3D_view/it.md) e premere il pulsante **<img src="images/Draft_Move.svg" width=16px> Sposta piano di lavoro** per spostare il piano di lavoro in modo che la sua origine corrisponda alla posizione del vertice selezionato.

-    **Spaziatura della griglia**definisce la distanza tra le linee della griglia.

-   Il valore **Linea principale ogni** determina dove vengono disegnate le linee principali della griglia. Le linee della griglia principale sono leggermente più spesse delle normali linee della griglia. Ad esempio, se la spaziatura della griglia è {{Value|0.5 m}} e c\'è una linea principale ogni {{Value|10 linee}}, tale linea si verificherà ogni {{Value|5 m}}.

-   Il valore **Estensione griglia** determina il numero di linee della griglia nelle direzioni X e Y della griglia.

-   Il **Raggio di aggancio** è la distanza massima alla quale [Draft Snap Grid](Draft_Snap_Grid/it.md) rileva le intersezioni delle linee della griglia.

-   Premere il pulsante **<img src="images/view-fullscreen.svg" width=16px> Centra la vista** per utilizzare l\'origine del piano di lavoro corrente come centro della [Vista 3D](3D_view/it.md).

-   Premere il pulsante **<img src="images/edit-undo.svg" width=16px> Precedente** per reimpostare il piano di lavoro nella posizione precedente.

-   Premere **Esc** o il pulsante **Chiudi** per interrompere il comando.



## Note

-   Può essere utile allineare la [Vista 3D](3D_view/it.md) con il piano di lavoro Draft selezionato. Ad esempio, dopo aver impostato il piano di lavoro su Frontale, si potrebbe voler passare anche alla [Vista frontale](Std_ViewFront/it.md).
-   La griglia può essere commutata con il comando [Draft Attiva Griglia](Draft_ToggleGrid/it.md).
-   Facendo doppio clic su [Draft Piano di lavoro proxy](Draft_WorkingPlaneProxy/it.md) nella [Vista ad albero](Tree_view/it.md) è possibile passare rapidamente da un piano di lavoro all\'altro.



## Preferenze

Vedere anche: [Impostare le preferenze](Preferences_Editor/it.md) e [Preferenze per l\'ambiente Draft](Draft_Preferences/it.md).

-   Le impostazioni della griglia nel pannello delle attività così come molte altre impostazioni della griglia sono disponibili come preferenze: **Modifica → Preferenze... → Draft → Griglia e snap → Griglia**.
-   Per utilizzare la griglia è necessario selezionare l\'opzione **Modifica → Preferenze... → Draft → Griglia e snap → Griglia → Usa griglia**. Dopo aver modificato questa preferenza è necessario riavviare FreeCAD.
-   Il raggio di Aggancio può anche essere modificato al volo (vedi [Draft Snap](Draft_Snap/it#Preferenze.md)) o modificando: **Strumenti → Modifica parametri... → BaseApp → Preferences → Mod → Draft → snapRange**.



## Script

Vedere anche: [Autogenerated API documentation](https://freecad.github.io/SourceDoc/) e [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md).

Se ,\'ambiente [Draft](Draft_Workbench/it.md) è attivo, l\'oggetto dell\'applicazione FreeCAD ha una proprietà `DraftWorkingPlane` che memorizza il piano di lavoro Draft corrente. E\' possibile accedere a questa proprietà e applicarvi delle trasformazioni:


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

È anche possibile creare piani indipendentemente dal piano di lavoro Draft. Questo può essere utile per calcoli e proiezioni:


```python
import WorkingPlane

my_plane = WorkingPlane.plane()

v1 = App.Vector(0, 0, 0)
v2 = App.Vector(1, 1, 1).normalize()
my_plane.alignToPointAndAxis(v1, v2, 17)

projection = my_plane.projectPoint(App.Vector(10, 15, 2))
print(projection)
```



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SelectPlane/it
