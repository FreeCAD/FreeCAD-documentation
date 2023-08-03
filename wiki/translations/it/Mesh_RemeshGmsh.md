---
 GuiCommand:
   Name: Mesh_RemeshGmsh
   Name/it: Affinamento
   MenuLocation: Mesh , Affinamento...
   Workbenches: Mesh_Workbench/it
   Version: 0.19
   SeeAlso: Mesh_FromPartShape/it
---

# Mesh RemeshGmsh/it

## Descrizione

Il comando **Affinamento** rigenera un oggetto mesh utilizzando il mesher [Gmsh](https://gmsh.info/). La nuova mesh può essere più fine o più grossolana.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Selezionare un singolo oggetto mesh.
2.  Selezionare l\'opzione **Mesh → <img src="images/Mesh_RemeshGmsh.svg" width=16px> Affinamento...** dal menu.
3.  Si apre il pannello delle azioni **Rigenera con gmsh**.
4.  Specificare le impostazioni richieste. Vedere le [Impostazioni del mesher Gmsh](Mesh_FromPartShape/it#Mesher_Gmsh.md) del comando [Crea mesh da una forma](Mesh_FromPartShape/it.md).
5.  Premere il pulsante **Applica** per rimodellare l\'oggetto mesh.
6.  Facoltativamente, modificare una o più impostazioni e premere nuovamente il pulsante **Applica** fino a quando la nuova mesh non è di proprio gradimento.
7.  Premere il pulsante **Chiudi** per chiudere il pannello delle azioni e terminare il comando.


</div>

## Note

-   In alcuni casi questo comando produce una mesh con le normali capovolte. Per correggere questo problema si può utilizzare il comando [Inverti le normali](Mesh_FlipNormals/it.md).

## Proprietà

Vedere: [Mesh Feature](Mesh_Feature/it.md).


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh RemeshGmsh/it
