---
 GuiCommand:
   Name: Sketcher Switch virtual space
   Name/it: Cambia spazio virtuale
   Icon: Sketcher SwitchVirtualSpace.svg
   MenuLocation: Sketch , Spazio virtuale dello Sketcher , Cambia spazio virtuale
   Workbenches: Sketcher Workbench/it
   Version: 0.17
---

# Sketcher SwitchVirtualSpace/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

Sketcher ha due spazi virtuali su cui è possibile impostare i vincoli. Di solito tutti i vincoli vengono impostati su un solo spazio virtuale. È possibile spostare alcuni vincoli nello spazio virtuale due. Questo può aiutare a ispezionare solo su alcuni vincoli alla volta.


</div>

A sketch has two virtual spaces that can contain constraints. All constraints are created in the main virtual space, but they can be hidden which moves them to the other virtual space.



## Utilizzo

### (Un)hide constraints 


<div class="mw-translate-fuzzy">

Per spostare i vincoli sull\'altro spazio virtuale:

1.  Selezionare i vincoli che si vuole spostare.
2.  Premere il pulsante **<img src="images/Sketcher_SwitchVirtualSpace.svg" width=32px> Cambia spazio virtuale**.

Per cambiare lo spazio virtuale:

1.  Accertarsi di non aver selezionato nessun vincolo.
2.  Premere il pulsante **<img src="images/Sketcher_SwitchVirtualSpace.svg" width=32px> Cambia spazio virtuale**.


</div>

### Switch virtual space 

1.  Make sure no constraints have been selected.
2.  Invoke the tool as described above.
3.  Hidden constraints are made visible and unhidden constraints invisible, or vice versa.

## Notes

-   Constraints can also be (un)hidden from the [Sketcher Dialog](Sketcher_Dialog#Constraints.md).
-   The virtual space setting of a sketch is only used in the current session, it is not stored in the FreeCAD file.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher SwitchVirtualSpace/it
