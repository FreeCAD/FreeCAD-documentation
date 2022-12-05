# 3D view/it
## Introduzione


{{TOCright}}

La [Vista 3D](3D_view/it.md) di FreeCAD è un\'istanza di una [scena grafica](Scenegraph/it.md) di Coin3D che costituisce la finestra più importante dell\'[interfaccia](interface/it.md) . Coin3D è una libreria che implementa lo standard di descrizione della scena OpenInventor 2.1.

Alcune proprietà della vista, come il colore di sfondo, lo stile di [navigazione con il mouse](Mouse_navigation/it.md) e i passi dello zoom, possono essere configurate con l\'[editor delle preferenze](Preferences_Editor/it.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*La [vista 3D](3D_view/it.md) è un componente dell'[interfaccia](interface/it.md) di FreeCAD . Per impostazione predefinita, essa mostra un piccolo widget con gli assi delle coordinate e il cubo di navigazione anche esso con gli assi delle coordinate; la griglia può essere visualizzata e configurata caricando l'ambiente [Draft](Draft_Workbench/it.md).*

## Azioni


**Note:**

Azioni link {{Version/it|0.19}}.

Poiché la [vista ad albero](tree_view/it.md) elenca la maggior parte degli oggetti che sono visibili nella vista 3D, molte delle azioni sono uguali a quelle che possono essere eseguite dalla [vista ad albero](tree_view/it.md).

Quando è attivo l\'ambiente predefinito [Start](Start_Workbench/it.md), il clic destro sulla vista 3D mostra un solo comando:

-    **[Stile di navigazione](Mouse_navigation/it.md)**: permette di scegliere lo stile dei pulsanti da utilizzare con un mouse a 3 pulsanti o un trackpad per laptop.

Dopo aver caricato un [Ambiente di lavoro](Workbenches/it.md), sono disponibili comandi aggiuntivi:

-    **Azioni link**: [Crea un link](Std_LinkMake/it.md).

    -   
        **Crea un gruppo di link**
        
        : [Gruppo semplice](Std_LinkMakeGroup/it.md), [Gruppo con link](Std_LinkMakeGroup/it.md), [Gruppo con link di trasformazione](Std_LinkMakeGroup/it.md).

-    **[Visualizza tutto](Std_ViewFitAll/it.md)**: esegue una panoramica e ingrandisce la vista per adattarla a tutti gli oggetti nel documento sullo schermo.

-    **[Visualizza la selezione](Std_ViewFitSelection/it.md)**: effettua una panoramica e ingrandisce la vista per adattarla solo all\'oggetto attualmente selezionato sullo schermo.

-    **[Stile di disegno](Std_DrawStyle/it.md)**: come è, facce piene, ombreggiato, reticolo, punti, linee nascoste, nessuna ombreggiatura.

-    **[Viste standard](Std_View_Menu/it.md)**: [isometrica](Std_ViewIsometric/it.md), [di fronte](Std_ViewFront/it.md), [dall\'alto](Std_ViewTop/it.md), [da destra](Std_ViewRight/it.md), [da dietro](Std_ViewRear/it.md), [dal basso](Std_ViewBottom/it.md), [da sinistra](Std_ViewLeft/it.md), [ruota a sinistra](Std_ViewRotateLeft/it.md), [ruota a destra](Std_ViewRotateRight/it.md).

-    **Misure**: [attiva/disattiva le misure](View_Measure_Toggle_All/it.md), [cancella le misure](View_Measure_Clear_All/it.md).

-    **Finestra del documento**: [agganciata](Std_ViewDockUndockFullscreen/it.md), [non agganciata](Std_ViewDockUndockFullscreen/it.md), e [schermo intero](Std_ViewDockUndockFullscreen/it.md).

Inoltre, a seconda dell\'ambiente e dell\'oggetto attivo, possono essere disponibili altri comandi contestuali.

Ad esempio, con [Part](Part_Workbench.md) e un oggetto selezionato:

-    **[Aspetto](Std_SetAppearance/it.md)**: avvia la finestra di dialogo per modificare il colore e le dimensioni di linee e vertici e il colore delle facce.

-    **[Mostra/Nascondi](Std_ToggleVisibility/it.md)**: rende l\'oggetto visibile o invisibile nella vista 3D.

-    **[Attiva/disattiva selezionabilità](Std_ToggleSelectability/it.md)**: rende l\'oggetto non più selezionabile nella vista 3D; usare di nuovo questo comando per annullarne l\'effetto. Imposta l\'attributo `Selectable` dell\'oggetto su `True` o `False`. Modificare la proprietà attivando **Selectable** nell\'[editor delle proprietà](property_editor/it.md).

-    **[Vai alla selezione](Std_TreeSelection/it.md)**: espande la [vista ad albero](tree_view/it.md) per mostrare l\'oggetto selezionato nella gerarchia.

-    **[Colore casuale](Std_RandomColor/it.md)**: assegna un colore casuale all\'oggetto. Imposta l\'attributo `ShapeColor` dell\'oggetto su una tupla `(r,g,b)` con valore flottante casuale tra 0 e 1. Cambiare la proprietà modificando **Shape Color** nell\'[editor delle proprietà](property_editor/it.md).

-    **[Elimina](Std_Delete/it.md)**: rimuove l\'oggetto dal documento e dalla vista 3D chiamando il metodo `removeObject()` del documento.

Un altro esempio, con [Draft](Draft_Workbench/it.md) e un oggetto selezionato, mostra gli stessi comandi di [Part](Part_Workbench/it.md), ma anche:

-    **Draft**: comandi di creazione e modifica dell\'oggetto di [Draft](Draft_Workbench/it.md).

-    **Utilità**: comandi contestuali aggiuntivi forniti da [Draft](Draft_Workbench/it.md).

## Dettagli

FreeCAD usa la libreria Quarter per usare Coin3D in un ambiente Qt.

È possibile interagire direttamente con lo scena 3D dalla [console Python](Python_console/it.md) utilizzando la libreria Python Pivy.

Per ulteriori informazioni, consultare la documentazione per utenti esperti:

-   [Scena grafica](Scenegraph/it.md), descrizione di Coin3D.
-   [Pivy](Pivy/it.md), utilizzo di Coin3D dalla console Python.
-   [Librerie di terze parti](Third_Party_Libraries/it.md) usate da FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ documentation.


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > 3D view/it
