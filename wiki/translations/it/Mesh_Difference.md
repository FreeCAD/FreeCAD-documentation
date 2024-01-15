# Mesh Difference/it
---
 GuiCommand:
   Name: Mesh_Difference
   Name/it: Differenza
   MenuLocation: Mesh , Operazione booleana , Differenza
   Workbenches: Mesh Workbench/it---



## Descrizione

Il comando **Differenza** crea un nuovo oggetto mesh non parametrico, un [Mesh Feature](Mesh_Feature/it.md), che è la differenza di due oggetti mesh: un oggetto mesh viene tagliato (sottratto) dall\'altro.

Per utilizzare questo comando bisogna che [OpenSCAD](http://www.openscad.org/) sia installato e il percorso del suo eseguibile sia impostato nelle [preferenze di OpenSCAD](OpenSCAD_Preferences/it.md).

![](images/Mesh_Difference_example.png ) 
*A sinistra due oggetti mesh, a destra l'oggetto mesh che è la differenza di quegli oggetti se il cubo è selezionato come oggetto principale*



## Utilizzo

1.  Selezionare l\'oggetto mesh principale.
2.  Aggiungere alla selezione l\'oggetto mesh che si desidera tagliare dall\'oggetto principale. Gli oggetti mesh devono sovrapporsi.
3.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_Difference.svg" width=16px> [ Differenza](Mesh_Difference/it.md)**.
    -   Selezionare l\'opzione **Mesh → Operazione booleana → <img src="images/Mesh_Difference.svg" width=16px> Differenza** dal menu.



## Proprietà

Vedere [Mesh Feature](Mesh_Feature/it.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Difference/it
