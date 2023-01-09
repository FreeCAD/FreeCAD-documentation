---
- GuiCommand:/it
   Name:Mesh_Export
   Name/it:Esporta mesh
   MenuLocation:Mesh → Esporta mesh...
   Workbenches:[Mesh](Mesh_Workbench/it.md)
   SeeAlso:[Esporta](Std_Export/it.md), [Importazione e Esportazione](Import_Export/it.md)
---

# Mesh Export/it

## Descrizione

Il comando **Esporta mesh** esporta un oggetto mesh in un formato file mesh. Sono supportati diversi formati di file.

## Utilizzo

1.  Selezionare un singolo oggetto mesh.
2.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Mesh_Export.svg" width=16px> Esporta mesh**.
    -   Selezionare l\'opzione **Mesh → <img src="images/Mesh_Export.svg" width=16px> Esporta mesh...** dal menu.
    -   Selezionare l\'opzione **<img src="images/Mesh_Export.svg" width=16px> Esporta mesh...** dal menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md).
3.  Selezionare il formato file corretto nella finestra di dialogo.
4.  Inserisci un nome file. Se nel passaggio precedente è stata selezionata l\'opzione {{Value|Tutti i file (*.*)}} e non si specifica un\'estensione di file, viene utilizzata l\'estensione **.stl**.
5.  Premere il pulsante **Salva**.

## Note

-   Esistono alcune preferenze di esportazione correlate ai [Formati mesh](Import_Export_Preferences/it#Formati_mesh.md) ma queste non si applicano a questo comando. Sono utilizzati dal comando [Esporta](Std_Export/it.md).

## Preferenze

-   L\'ultima posizione del file utilizzato viene memorizzata in: **Strumenti → Modifica parametri... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script

Vedere anche: [Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per esportare oggetti (inclusi gli oggetti mesh) in un formato file mesh, utilizzare il metodo `export` del modulo Mesh.


```python
import FreeCAD
import Mesh

doc = FreeCAD.ActiveDocument

Mesh.export([doc.Cone, doc.Cylinder], 'D:/testfiles/mymodel.stl')
```





{{Mesh Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Export/it
