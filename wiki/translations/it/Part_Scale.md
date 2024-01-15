---
 GuiCommand:
   Name: Part Scale
   Name: Part Scala
   MenuLocation: Parte , Scala...
   Workbenches: Part_Workbench/it
   Version: 0.22
   SeeAlso: Draft_Clone/it, Draft_Scale
---

# Part Scale/it



## Descrizione

**Part Scala** ridimensiona le forme in base a un fattore specificato in tutte le direzioni o in base a fattori distinti in ciascuna direzione cardinale. Nel caso di fattori distinti, le forme potrebbero risultare distorte.

![400px](images/Part_Scale_demo.png) 
*Esempio di ridimensionamento*



## Utilizzo

1.  Selezionare una o più forme nella [Vista 3D](3D_view/it.md) o nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Part_Scale.svg" width=16px> [Scala...](Part_Scale/it.md)**.
    -   Selezionare l\'opzione **Parte → <img src="images/Part_Scale.svg" width=16px> Scala...** dal menu.
3.  Si apre un [pannello delle azioni](#Task_panel/it.md).
4.  Scegliere **Ridimensionamento uniforme** o **Ridimensionamento non uniforme**.
5.  Impostare i fattori di scala.
6.  Fare clic su **OK**.

In alternativa, la selezione può essere effettuata dopo aver lanciato il comando, selezionando una o più forme dalla lista nel [pannello delle Azioni](#Task_panel/it.md).

La Vista ad albero elencherà tanti oggetti Scala quante sono le forme selezionate. Ogni forma di input viene posizionata sotto il relativo oggetto Scala.



## Pannello Azioni 

![](images/Part_Scale_dialog.png )

-   Il pulsante **OK** crea l\'oggetto ridimensionato e chiude il pannello delle attività.
-   Il pulsante **Chiudi** chiude il pannello delle attività senza fare nulla.
-   Il pulsante **Applica** crea gli oggetti ridimensionati, ma non chiude il pannello delle attività. E\' possibile quindi selezionare un\'altra forma dall\'elenco in basso e creare più oggetti in scala.
-   Elenco **Forma**: qui è possibile selezionare quali forme ridimensionare. Se vengono selezionate più forme, vengono creati più oggetti Scala.



## Note

-   Il ridimensionamento non uniforme trasformerà tutti i bordi in curve B-spline e tutte le facce in superfici B-spline. Questi sono computazionalmente più pesanti.
-   I punti/vertici non possono essere ridimensionati poiché sono adimensionali.
-   È inoltre possibile ridimensionare gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno.
-   Il pannello delle Azioni non offre ancora un\'anteprima. **Applica** creerà un oggetto in scala ogni volta che si clicca su di esso, che può essere utile come anteprima. Tuttavia, l\'oggetto specchiato rimarrà e ne verrà creato uno ulteriore quando si farà clic su su **OK**. [Annulla](Std_Undo/it.md) può essere utile per ripulirli prima di fare clic su **OK**.



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un oggetto Part Specchio deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Scale}}

-    **Base|Link**: la forma di input (la forma su cui è stata applicata la scala della parte).

-    **Uniform|Bool**: controlla il ridimensionamento uniforme e non uniforme

-    **Uniform Scale|Float**: il fattore di scala per il ridimensionamento uniforme

-    **XScale|Float**: il fattore di scala X per il ridimensionamento non uniforme.

-    **YScale|Float**: il fattore di scala Y, idem.

-    **ZScale|Float**: il fattore di scala Z, idem.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Scale/it
