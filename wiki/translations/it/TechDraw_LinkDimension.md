---
 GuiCommand:
   Name: TechDraw LinkDimension
   Name/it: TechDraw Link alla geometria 3D
   MenuLocation: TechDraw , Quotatura , Link alla geometria 3D
   Workbenches: TechDraw_Workbench/it
   SeeAlso: TechDraw_View/it, TechDraw_ProjectionGroup/it
---

# TechDraw LinkDimension/it



## Descrizione

Lo strumento **TechDraw Link alla geometria 3D** crea un collegamento tra la geometria 3D e una o più quote proiettate esistenti su una Pagina. Questo collegamento consente alla Quota di utilizzare valori 3D effettivi anziché valori proiettati 2D.

L\'uso più comune dello strumento Link alla geometria 3D è nella quotatura delle viste isometriche in un gruppo di proiezione. La lunghezza proiettata di un Bordo in una vista isometrica, ovviamente, non sarà necessariamente uguale alla lunghezza effettiva del bordo. In una vista ortogonale le lunghezze proiettate e quelle effettive saranno uguali.

Il link alla geometria 3D indica alla Quota di calcolare il valore direttamente dalla geometria 3D.



## Utilizzo

1.  Creare una quota appropriata nella Pagina di disegno utilizzando uno qualsiasi tra [TechDraw Quota allineata](TechDraw_LengthDimension/it.md), [TechDraw Quota orizzontale](TechDraw_HorizontalDimension/it.md), ecc. Questa quota sarà nel posto giusto sulla Pagina, ma mostrerà un valore proiettato.
2.  Selezionare la geometria nella vista 3D, ad esempio un bordo, che corrisponde alla geometria proiettata della propria quota.
3.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_LinkDimension.svg" width=16px> [Collega dimensione alla geometria 3D](TechDraw_LinkDimension/it.md)**.
    -   Seleziona l\'opzione **TechDraw → Quotatura → <img src="images/TechDraw_LinkDimension.svg" width=16px> Link alla geometria 3D** dal menu.
4.  Si apre un pannello delle azioni.
5.  Selezionare una o più quote da collegare alla geometria 3D selezionata.
6.  Premere **OK**.

L\'operazione di collegamento modifica la proprietà **MeasureType** della quota da `Projected` a `True`.



## Limitazioni

Gli oggetti Quota sono vulnerabili al \"[problema di denominazione topologica](Topological_naming_problem/it.md)\". Per ulteriori informazioni, vedere [TechDraw Quota allineata](TechDraw_LengthDimension/it.md). Si consiglia di collegare le quote come uno degli ultimi passaggi del processo di disegno.

Lo strumento Link alla dimensione non impedisce di creare collegamenti errati, quindi bisogna scegliere il bordo corretto dalla vista 3D quando si crea il collegamento.

Al momento non c\'è modo di interrompere un link; si può però ripristinare la proprietà **MeasureType** in `Projected` in modo che la dimensione utilizzi il valore proiettato invece del valore collegato.

Notare che se la dimensione da collegare si basa su due vertici, si devono selezionare due vertici nella vista 3D. Allo stesso modo se la dimensione si basa su un bordo, è necessario selezionare un bordo nella vista 3D.



## Script


**Vedere anche:**

[API TechDraw](TechDraw_API/it.md) e [Nozioni di base sugli script di FreeCAD](FreeCAD_Scripting_Basics/it.md).

Lo strumento TechDraw Link alla geometria 3D non è utilizzabile direttamente nelle macro, ma la modifica della proprietà **References 3D** può ottenere lo stesso risultato.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LinkDimension/it
