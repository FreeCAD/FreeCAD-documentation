---
- GuiCommand   */it
   Name   *Mesh_PolyTrim
   Name/it   *Rifila con un poligono
   MenuLocation   *Mesh → Taglio → Rifila con un poligono
   Workbenches   *[Mesh](Mesh_Workbench/it.md)
   SeeAlso   *[Taglia la mesh](Mesh_PolyCut/it.md), [Rifila con un piano](Mesh_TrimByPlane/it.md)
---

# Mesh PolyTrim/it

## Descrizione

Il comando **Rifila con un poligono** taglia facce e parti di facce da oggetti mesh.

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Durante il comando non è possibile modificare la [vista 3D](3D_view.md). Si consiglia di allineare correttamente prima la vista 3D.
2.  Selezionare uno o più oggetti mesh.
3.  Selezionare l\'opzione **Mesh → Taglio → <img src="images/Mesh_PolyTrim.svg" width=16px> Rifila con un poligono** dal menu.
4.  Definire un poligono selezionando dei punti nella vista 3D.
5.  Selezionare un\'opzione dal menu contestuale della vista 3D   *
    -   
        **Interno**
        
           * rimuove le facce che sono (parzialmente) all\'interno del poligono.

    -   
        **Esterno**
        
           * rimuove le facce che sono completamente al di fuori del poligono.

    -   
        **Dividi**
        
           * rimuove le facce che sono completamente esterne al poligono e crea un nuovo oggetto mesh che le contiene.

    -   
        **Annulla**
        
           * annulla il comando.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyTrim/it
