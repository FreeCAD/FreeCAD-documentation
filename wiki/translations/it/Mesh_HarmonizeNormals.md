---
- GuiCommand:
   Name:Mesh_HarmonizeNormals
   Name/it:Armonizza le normali
   MenuLocation:Mesh - Armonizza le normali
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Inverti le normali](Mesh_FlipNormals/it.md)
---

# Mesh HarmonizeNormals/it



## Descrizione

Il comando **Armonizza le normali** armonizza le normali degli oggetti mesh.



## Utilizzo

1.  Selezionare uno o più oggetti mesh.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_HarmonizeNormals.svg" width=16px> [Armonizza le normali](Mesh_HarmonizeNormals/it.md)**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_HarmonizeNormals.svg" width=16px> Armonizza le normali** dal menu.



## Note

-   Questo comando può produrre una mesh con normali capovolte. Il comando [Inveri le normali](Mesh_FlipNormals/it.md) può essere utilizzato per correggere questo problema.
-   Per una chiara indicazione dell\'orientamento delle facce degli oggetti mesh, assicurarsi che la proprietà **Lighting** degli oggetti mesh sia impostata su {{Value|One side}}. Il colore della parte posteriore delle loro facce dipenderà quindi dalle impostazioni di retroilluminazione: **Modifica → Preferenze ... → Visualizzazione → Vista 3D → Colore retroilluminazione - Intensità**. Vedere nell\'[editor delle preferenze](Preferences_Editor/it#Vista_3D.md).





{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh HarmonizeNormals/it
