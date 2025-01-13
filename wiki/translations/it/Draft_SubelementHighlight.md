---
 GuiCommand:
   Name: Draft SubelementHighlight
   Name/it: Draft Evidenzia sottoelemento
   MenuLocation: Draft , Evidenzia sottoelemento
   Workbenches: Draft_Workbench/it
   Shortcut: **H** **S**
   Version: 0.19
   SeeAlso: Draft_Move/it, Draft_Rotate/it, Draft_Scale/it
---

# Draft SubelementHighlight/it



## Descrizione

Il comando <img alt="" src=images/Draft_SubelementHighlight.svg  style="width:24px;"> **Draft Evidenzia sottoelemento** evidenzia temporaneamente gli oggetti selezionati o gli oggetti di base degli oggetti selezionati. È concepito per essere utilizzato in combinazione con la modalità del sottoelemento del comando [Draft Muovi](Draft_Move/it.md), il comando [Draft Ruota](Draft_Rotate.md) o il comando [Draft Scala](Draft_Scale.md). Attualmente la modalità sottoelemento funziona correttamente solo per [Draft Linee](Draft_Line/it.md) e [Draft Polilinee](Draft_Wire/it.md).

![](images/Draft_SubelementHighlight_example.png ) 
*Un muro ad arco la cui base, una polilinea, è stata evidenziata*



## Utilizzo

1.  Facoltativamente, selezionare una o più [Linee](Draft_Line/it.md) o [Draft Polilinee](Draft_Wire/it.md), o oggetti i cui oggetti **Base** sono [Draft Linee](Draft_Line/it.md) o [Draft Polilinee](Draft_Wire/it.md).
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Draft_SubelementHighlight.svg" width=16px> [Evidenzia sottoelemento](Draft_SubelementHighlight/it.md)**.
    -   Seleziona l\'opzione **Modifiche → <img src="images/Draft_SubelementHighlight.svg" width=16px> Evidenzia sottoelemento** dal menu.
    -   Usare la scorciatoia da tastiera: **H** poi **S**.
3.  Se non si ha ancora selezionato un oggetto: selezionare un oggetto nella [Vista 3D](3D_view/it.md).
4.  Gli oggetti selezionati vengono resi visibili (se richiesto), il loro **Line Color** e **Point Color** vengono modificati in rosso e il loro **Point Size** viene modificato in {{ Value\|10}}.
5.  È consigliabile ora deselezionare la selezione esistente, ad esempio facendo clic su un punto casuale nella [Vista 3D](3D_view/it.md).
6.  Selezionare uno o più sottoelementi, spigoli o punti, degli oggetti che sono stati contrassegnati in rosso.
7.  Richiamare [Draft Muovi](Draft_Move/it.md), [Draft Ruota](Draft_Rotate/it.md) o [Draft Scala](Draft_Scale/it.md).
8.  Attivare/disattivare la modalità dei sottoelementi nel pannello delle attività di quel comando selezionando la casella di controllo **Modifica sottoelementi**.
9.  Modificare i sottoelementi selezionati e completare il comando Draft Modifica.
10. Premere **Esc** per ripristinare i cambiamenti visivi temporanei degli oggetti.



## Note

-   Se gli oggetti sono stati evidenziati con questo comando, le modifiche visive temporanee devono essere annullate prima di salvare e riaprire il file.
-   Gli oggetti evidenziati non devono essere copiati se la modalità sottoelemento è disattivata. Le modifiche visive temporanee non possono essere ripristinate per le copie create in questo modo.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft SubelementHighlight/it
