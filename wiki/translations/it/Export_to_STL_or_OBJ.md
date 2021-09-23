# Export to STL or OBJ/it
<div class="mw-translate-fuzzy">


{{TutorialInfo/it
|Topic= Esportare in STL o OBJ
|Level= Base
|Time= 20 minuti
|Author=r-frank
|FCVersion=0.16.6703
|Files=
}}


</div>

## Introduction


<div class="mw-translate-fuzzy">

## Introduzione

In questo tutorial ci occuperemo di come esportare file STL / OBJ da FreeCAD. Dato che il formato mesh STL / OBJ è adimensionale, nelle esportazioni FreeCAD assume che l\'unità utilizzata nel modello è il mm. Se non è così bisogna scalare il modello. Un modo per farlo è usare <img alt="" src=images/Draft_Scale.svg  style="width:24px;"> [Scala](Draft_Scale/it.md) di Draft.


</div>

## Sample part 


<div class="mw-translate-fuzzy">

## La parte modello 

È possibile utilizzare un file di FreeCAD, ma si può anche creare velocemente un file di test con queste azioni:

-   Avviare FreeCAD
-   Creare un nuovo documento
-   Passare nell\'ambiente Part
-   Inserire un cubo cliccando su <img alt="" src=images/Part_Box.svg  style="width:32px;"> [Cubo](Part_Box/it.md)
-   Inserire un cono cliccando su <img alt="" src=images/Part_Cone.svg  style="width:32px;"> [Cono](Part_Cone/it.md)
-   Selezionare entrambi gli oggetti nella vista ad albero
-   Applicare una fusione cliccando su <img alt="" src=images/Part_Fuse.svg  style="width:32px;"> [Fusione](Part_Union/it.md)
-   Salvare il file


</div>

## Export Method 1: Using \"File → Export\" 


<div class="mw-translate-fuzzy">

## Esportazione metodo 1: Usando \"File → Esporta\" 

-   Selezionare il solido da esportare nella vista ad albero.
-   Scegliere ** File** → ** Export...** e impostare il tipo di file su \"STL mesh (\*.stl \*.ast)\".
-   Inserire il nome del file. L\'estensione di default è \".stl\". È necessario includere l\'estensione \".ast\" nel nome del file per produrre un file .ast. Scegliere **Salva**.


</div>

## Export Method 2: Using the Mesh Workbench in FreeCAD 


<div class="mw-translate-fuzzy">

## Esportazione metodo 2: Usando l\'ambiente Mesh di FreeCAD 

-   Passare all\'ambiente [Mesh](Mesh_Workbench/it.md).
-   Selezionare il solido da rendere mesh, in vista ad albero
-   Scegliere ** Mesh** → **<img src="images/Mesh_FromPartShape.svg" width=32px> Crea Mesh da forma...** dal menu principale.
-   Selezionare una dei mesher disponibili e specificare le opzioni disponibili, per maggiori informazioni fare riferimento alla pagina [Mesh da Forma](Mesh_FromPartShape/it.md).
-   Scegliere ** OK**. Nella vista ad albero viene creato l\'oggetto mesh (con l\'icona verde di mesh <img alt="" src=images/Workbench_Mesh.svg  style="width:16px;">).
-   Fare clic con il tasto destro del mouse sull\'oggetto mesh nella vista ad albero e scegliere **<img src="images/Mesh_Export.svg" width=32px> Esporta mesh...**.
-   Compilare il nome del file; l\'estensione non è necessaria. L\'estensione viene impostata in base al tipo di file. Se si include un\'estensione che non corrisponde al tipo di file selezionato, viene aggiunta un\'estensione per il tipo selezionato quando il file viene salvato. Se si include un\'estensione che corrisponde al tipo di file, non viene aggiunta alcuna estensione addizionale.
-   Il tipo di file predefinito è \"Binary STL (\*.stl)\". Cambiare il tipo se lo si desidera.
-   Scegliere **Salva** per eseguire l\'esportazione.


</div>

## Which Method to choose ? 


<div class="mw-translate-fuzzy">

## Quale metodo scegliere? 

-   Il metodo 2 deve essere quello preferito. Tra i motivi:
-   Quando si vuole convertire più di un Corpo si possono usare gli strumenti di [Mesh](Mesh_Workbench/it.md). Ad esempio, è possibile fondere le mesh prima dell\'esportazione.
-   Le superfici curve sono rappresentate in STL come una serie di segmenti lineari, generati tramite tessellatura. Ciò si traduce in dimensioni interne leggermente sottodimensionate per le superfici curve. Se si sta esportando per l\'utilizzo nella stampa 3D, questo può comportare, ad esempio, un buco sottodimensionato. In questi casi potrebbe essere necessario usare un valore di tessellazione più fine. Quando si esporta da un altro ambiente usando **File** → **Esporta ...**, la tessellatura è controllata dal set generale di visualizzazione della tassellatura in **Modifica** → **Preferenze ...** → Part Design → Visualizzazione della figura. Tuttavia, poiché questi parametri controllano la tassellatura utilizzata per il rendering delle forme sul display, la loro diminuzione rallenta il rendering della visualizzazione, spesso in modo significativo. Inoltre, l\'esportazione immediatamente dopo aver modificato il valore della preferenza per la tessellizzazione della visualizzazione non ha l\'effetto desiderato perché la tessellatura della visualizzazione non viene aggiornata immediatamente. Per far ricalcolare la tessellatura si deve forzare una modifica nel modello sottostante, ad esempio modificando un parametro dello schizzo (l\'impostazione sul suo valore originale è sufficiente).


</div>

## Links


<div class="mw-translate-fuzzy">

## Link

-   [Importare da STL o OBJ](Import_from_STL_or_OBJ/it.md)
-   [Importazione e esportazione](Import_Export/it.md)


</div>




[Category:File\_Formats](Category:File_Formats.md)

---
[documentation index](../README.md) > [File_Formats](Category:File_Formats.md) > Export to STL or OBJ/it
