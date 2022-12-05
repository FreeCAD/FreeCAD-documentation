---
- GuiCommand:/it
   Name:Mesh_PolyCut
   Name/it:Taglia la mesh
   MenuLocation:Mesh → Taglio → Taglia la mesh
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Rifila con un poligono](Mesh_PolyTrim/it.md), [Rifila con un piano](Mesh_TrimByPlane/it.md)
---

# Mesh PolyCut/it

## Descrizione

Il comando **Taglia la mesh** taglia intere facce da oggetti mesh.

## Utilizzo

1.  Durante il comando non è possibile modificare la [vista 3D](3D_view.md). Si consiglia di allineare correttamente prima la vista 3D.
2.  Selezionare uno o più oggetti mesh.
3.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Mesh_PolyCut.svg" width=16px> [Taglia la mesh](Mesh_PolyCut/it.md)**.
    -   Selezionare l\'opzione **Meshes → Taglio → <img src="images/Mesh_PolyCut.svg" width=16px> Taglia la mesh** dal menu.
4.  Definire un poligono selezionando dei punti nella vista 3D.
5.  Selezionare un\'opzione dal menu contestuale della vista 3D:
    -   
        **Interno**
        
        : rimuove le facce che sono (parzialmente) all\'interno del poligono.

    -   
        **Esterno**
        
        : rimuove le facce che sono completamente al di fuori del poligono.

    -   
        **Dividi**
        
        : rimuove le facce che sono completamente esterne al poligono e crea un nuovo oggetto mesh che le contiene.

    -   
        **Annulla**
        
        : annulla il comando.





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh PolyCut/it
