---
 GuiCommand:
   Name: TechDraw ProjectShape
   Name: TechDraw Proietta forma
   MenuLocation: TechDraw , Viste TechDraw , Project shape...
   Workbenches: TechDraw_Workbench/it
   Shortcut: 
   Version: 0.20
   SeeAlso: Draft_Shape2DView/it
---

# TechDraw ProjectShape/it



## Descrizione

Lo strumento **TechDraw Proietta forma** crea proiezioni di forme. Le proiezioni vengono create nella [Vista 3D](3D_view/it.md) e non in una [Pagina TechDraw](TechDraw_PageDefault/it.md).

![](images/ProjectShape1_it.png )



## Utilizzo

1.  Facoltativamente ruotare la [vista 3D](3D_view/it.md). Gli oggetti verranno proiettati su un piano parallelo allo schermo, ovvero lungo la direzione della telecamera della vista 3D, che viene utilizzata come proprietà **Direction** predefinita.
2.  Selezionare uno o più oggetti. Per ogni oggetto verrà creata una proiezione separata.
3.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_ProjectShape.svg" width=16px> [Proietta forma...](TechDraw_ProjectShape/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_ProjectShape.svg" width=16px> Proietta forma...** dal menu.
4.  Si apre il pannello delle attività **Project Shapes**. Vedere [Proprietà](#Proprietà.md).
5.  Impostare le opzioni desiderate.
6.  Le opzioni selezionate non dovrebbero generare una proiezione vuota poiché ciò causerebbe un errore. Ad esempio, per un oggetto con solo spigoli vivi come un [Part Box](Part_Box/it.md), è necessario selezionare l\'opzione **Mostra gli spigoli vivi** e/o **Nascondi gli spigoli vivi**.
7.  Premere il pulsante **OK**.
8.  La proiezione è posizionata sul piano XY.
9.  Facoltativamente, modificare la proprietà **Placement** e/o la proprietà **Direction** della proiezione.



## Proprietà

Un oggetto Proiezione deriva da un oggetto [Funzione Part](Part_Feature/it.md) e ne eredita tutte le proprietà. Ha inoltre le seguenti proprietà aggiuntive:



### Dati


{{TitleProperty|Projection}}

-    **Source|Link**: La forma da proiettare.

-    **Direction|Vector**: La direzione della proiezione. Questo è il vettore normale del piano di proiezione.

-    **VCompound|Bool**: Se `True`, vengono mostrati gli spigoli vivi visibili. Esempio: tutti i bordi di un [Part Box](Part_Box/it.md).

-    **Rg1 Line VCompound|Bool**: Se `True`, vengono visualizzati i bordi smussati visibili. Esempio: i bordi tra un raccordo e le sue facce adiacenti.

-    **Rg NLine VCompound|Bool**: Se `True`, vengono mostrati i bordi cuciti (seme) visibili. Esempio: la cucitura di una faccia cilindrica a 360°.

-    **Out Line VCompound|Bool**: se `True`, vengono mostrati i bordi del contorno visibili (che non sono nitidi). Esempio: la vista laterale di un [Part Cilindro](Part_Cylinder/it.md) ha due di questi bordi.

-    **Iso Line VCompound|Bool**: Se `True`, vengono mostrati gli isoparametri visibili. Non funziona attualmente.

-    **HCompound|Bool**: Se `True`, vengono visualizzati gli spigoli vivi nascosti.

-    **Rg1 Line HCompound|Bool**: Se `True`, vengono visualizzati i bordi smussati nascosti

-    **Rg NLine HCompound|Bool**: Se `True`, vengono visualizzati i bordi cuciti nascosti.

-    **Out Line HCompound|Bool**: Se `True`, vengono visualizzati i bordi del contorno nascosti.

-    **Iso Line HCompound|Bool**: Se `True`, vengono visualizzati gli isoparametri nascosti. Non funziona attualmente.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectShape/it
