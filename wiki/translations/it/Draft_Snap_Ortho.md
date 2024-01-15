---
 GuiCommand:
   Name: Draft Snap Ortho
   Name/it: Aggancia Ortogonale
   Workbenches: Draft_Workbench/it, Arch_Workbench/it
   SeeAlso: Draft Snap/it, Draft_Snap_Lock/it
---

# Draft Snap Ortho/it



## Descrizione

L\'opzione <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:24px;"> **Draft Aggancia Ortogonale** esegue l\'aggancio alle linee immaginarie che attraversano il punto precedente a multipli di 45°. Le linee e gli angoli sono relativi al piano XY del sistema di coordinate del [piano di lavoro](Draft_SelectPlane/it.md).

![](images/Draft_Snap_Ortho_example.png ) 
*Aggancio del secondo punto di una linea a una linea immaginaria che ha un angolo di 45° con l'asse X. I piccoli cerchi magenta indicano tutte le possibili direzioni.*



## Utilizzo

Per informazioni generali riguardo gli agganci vedere [Draft Aggancio](Draft_Snap/it.md).

1.  Assicurarsi che l\'aggancio sia abilitato. Vedere <img alt="" src=images/Draft_Snap_Lock.svg  style="width:16px;"> [Draft Blocca aggancio](Draft_Snap_Lock/it.md).
2.  Se **Draft Aggancia Ortogonale** non è attivo, eseguire una delle seguenti operazioni:
    -   Premere il pulsante **<img src="images/Draft_Snap_Ortho.svg" width=16px>** nella barra degli strumenti di aggancio di Draft.
    -   Premere il pulsante **<img src="images/Draft_Snap_Ortho.svg" width=16px>** nel [Draft snap widget](Draft_snap_widget/it.md).
3.  Scegliere un comando [Draft](Draft_Workbench/it.md) o [Arch](Arch_Workbench/it.md) per creare la propria geometria.
4.  Tenere presente che si può anche modificare le opzioni di aggancio mentre un comando è attivo.
5.  Scegliere un primo punto. Questa opzione di aggancio richiede un punto precedente.
6.  Se si muove il cursore attorno al punto precedente si nota un effetto \"magnetico\" quando il cursore si trova su una linea infinita immaginaria che attraversa quel punto con un angolo di 0°, 45°, 90° o 135°.
7.  Il punto viene contrassegnato e l\'icona <img alt="" src=images/Draft_Snap_Ortho.svg  style="width:16px;"> viene visualizzata vicino al cursore.
8.  Fare clic per confermare il punto.



## Preferenze

Vedere [Draft Aggancio](Draft_Snap/it#Preferenze.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Snap Ortho/it
