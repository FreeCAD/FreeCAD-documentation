---
- GuiCommand:/it
   Name:Mesh_Import
   Name/it:Importa mesh
   MenuLocation:Mesh → Importa mesh...
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Importa](Std_Import/it.md), [Apri](Std_Open/it.md), [Importazione e Esportazione](Import_Export/it.md)
---

# Mesh Import/it

## Descrizione

Il comando **Importa mesh** importa la geometria da un formato file mesh nel documento attivo. Sono supportati diversi formati di file. Il comando crea un oggetto mesh non parametrico, una [Mesh Feature](Mesh_Feature/it.md).

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_Import.svg" width=16px> Importa mesh**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_Import.svg" width=16px> Importa mesh...** dal menu.
    -   Selezionare l\'opzione **<img src="images/Mesh_Import.svg" width=16px> Importa mesh...** dal menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md). Questa opzione è disponibile solo se è stato selezionato un oggetto mesh esistente. Notare che l\'oggetto selezionato non viene effettivamente utilizzato o modificato dal comando.
2.  Facoltativamente, selezionare il formato file corretto nella finestra di dialogo.
3.  Selezionare un file.
4.  Premere il pulsante **Apri**.

## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.

## Proprietà

Vedere: [Mesh Feature](Mesh_Feature/it.md).

## Script

Vedere anche: [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per importare un file mesh utilizzare il metodo `insert` del modulo Mesh.


```python
import Mesh
Mesh.insert('D:/testfiles/cylinder.stl')
```


<div class="mw-translate-fuzzy">





</div>


{{Mesh Tools navi

}}

---
[documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Import/it
