---
 TutorialInfo:t
   Topic:  Esportare in STL o OBJ
   Level:  Base
   Time:  20 minuti
   Author: r-frank
   FCVersion: 0.16.6703
---

# Export to STL or OBJ/it







## Introduzione

In questo tutorial tratteremo come esportare file STL/OBJ da FreeCAD. Il formato mesh STL/OBJ è adimensionale; FreeCAD assumerà durante l\'esportazione che le unità utilizzate nel modello siano in mm. Se questo non è il caso si deve ridimensionare il proprio modello. Un modo per farlo è utilizzare <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Draft Scala](Draft_Scale/it.md).



## La parte modello 

E\' possibile utilizzare il proprio file FreeCAD, ma è possibile anche creare un file di test rapido:

1.  Aprire FreeCAD.
2.  Creare un nuovo documento.
3.  Passare all\'<img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Ambiente Part](Part_Workbench/it.md).
4.  Inserire un cubo facendo clic su <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cubo](Part_Box/it.md).
5.  Inserire un cono facendo clic su <img alt="" src=images/Part_Cone.svg  style="width:24px;"> [Part Cono](Part_Cone/it.md).
6.  Selezionare entrambi gli oggetti nella [vista ad albero](Tree_view/it.md).
7.  Applicare una fusione facendo clic su <img alt="" src=images/Part_Fuse.svg  style="width:24px;"> [Part Unisci](Part_Fuse/it.md).
8.  Salvare il file.



## Metodo di esportazione 1: utilizzando \"File → Esporta\" 

1.  Con le impostazioni predefinite, questo metodo crea una mesh con curve notevolmente frastagliate. Per ottenere una finitura più liscia quando ad es. per la Stampa 3D, la risoluzione della mesh deve essere configurata:
    1.  Assicurarsi che l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Ambiente Mesh](Mesh_Workbench/it.md) sia stato caricato (non è caricato per impostazione predefinita).
    2.  Andare in **Modifica → Preferenze... → Importa-Esporta → Formati mesh**.
    3.  Cambiare **Deviazione massima della mesh**. Un valore più basso produrrà una mesh con una risoluzione più alta.
2.  Selezionarere il solido da esportare nella vista ad albero.
3.  Scegliere **File → Esporta...** e impostare il tipo di file su **STL mesh (*.stl *.ast)**.
4.  Inserire il nome del file. L\'estensione predefinita è **.stl**. È necessario includere l\'estensione **.ast** per produrre un file **.ast**.
5.  Scegliere **Salva**.



## Metodo di esportazione 2: utilizzo dell\'ambiente Mesh in FreeCAD 

1.  Passare all\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [Ambiente Mesh](Mesh_Workbench.md).
2.  Selezionare il solido da convertire in mesh nella vista ad albero.
3.  Scegliere **Meshes → <img src="images/Mesh_FromPartShape.svg" width=24px> Crea mesh dalla forma...** dal menu principale (in alto).
4.  Selezionare uno dei mesher disponibili e specificare le opzioni disponibili. Per ulteriori informazioni fare riferimento a [Mesh da forma](Mesh_FromPartShape/it.md).
5.  Scegliere **OK**. L\'oggetto mesh verrà creato nella vista ad albero (con un\'icona mesh verde <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">).
6.  Fare clic con il pulsante destro del mouse sull\'oggetto mesh nella vista ad albero e scegliere **<img src="images/Mesh_Export.svg" width=24px> Esporta mesh...**.
7.  Inserire il nome del file, l\'estensione non è necessaria. L\'estensione verrà impostata in base al tipo di file. Se si include un\'estensione che non corrisponde al tipo di file selezionato, quando il file verrà salvato verrà aggiunta un\'estensione per il tipo selezionato.
8.  Il tipo di file predefinito è **Binary STL (*.stl)**. Cambiare il tipo se lo si desidera.
9.  Scegliere **Salva**.



## Quale metodo scegliere? 

-   Il metodo 1 può essere utilizzato per la maggior parte delle situazioni in cui è necessario un file mesh.
-   Con il metodo 2 è possibile verificare la mesh in FreeCAD. E se si ha più di un solido da convertire si possono utilizzare gli Strumenti dell\'[Ambiente Mesh](Mesh_Workbench/it.md). Ad esempio, è possibile fondere le mesh prima dell\'esportazione.



## Collegamenti

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Importazione e esportazione](Import_Export/it.md)



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Export to STL or OBJ/it
