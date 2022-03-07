---
- GuiCommand:/it
   Name:Arch_SetMaterial
   Name/it:Imposta Materiale
   MenuLocation:Arch → Strumenti materiali → Materiale
   Workbenches:[Arch](Arch_Workbench/it.md), [BIM](BIM_Workbench/it.md)
   Shortcut:**M** **T**
   SeeAlso:[Materiali](Arch_CompSetMaterial/it.md), [Multimateriali](Arch_MultiMaterial/it.md)
---

# Arch SetMaterial/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento materiale permette di aggiungere dei [materiali](Material.md) al documento attivo, e di attribuire un materiale ad un oggetto [Arch](Arch_Workbench/it.md). I Materiali possiedono tutte le proprietà di un determinato materiale, e controllano il colore dell\'oggetto a cui sono allegati. I materiali vengono memorizzati in una cartella **Materials** nel documento attivo.


</div>

![](images/Arch_materials_01.jpg )

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Facoltativamente, selezionare uno o più oggetti a cui si desidera attribuire un nuovo materiale.
2.  Richiamare il comando in uno di questi modi:
    -   Premere il pulsante **<img src="images/Arch_SetMaterial.svg" width=16px> [Imposta materiale](Arch_SetMaterial/it.md)** nella barra degli strumenti.
    -   Usare la scorciatoia **M** e poi **T** da tastiera.
    -   Usare il comando **Arch → Strumenti materiali → Materiale** dal menu principale.
3.  Caricare un materiale predefinito, o crearne uno nuovo riempiendo i campi.
4.  Premere **OK**.


</div>

## Opzioni

-   Al momento della creazione di un nuovo materiale, un pannello consente di impostare le diverse opzioni:

![](images/Arch_materials_02.jpg )


<div class="mw-translate-fuzzy">

-   **Choose preset**: Scegliere uno dei materiali preimpostati, da utilizzare come è, o per adattarlo modificando i campi sottostanti
-   **Name**: Scegliere un nome per il materiale
-   **Edit button**: Questo apre il materiale corrente nel [Editor dei materiali](Material_editor/it.md) di FreeCAD, che permette di modificare molte proprietà aggiuntive e di aggiungere le proprie personalizzate
-   **Description**: Una descrizione più dettagliata del materiale
-   **Color**: Il colore di visualizzazione per il materiale, che sarà applicato a tutti gli oggetti che utilizzano tale materiale
-   **Code**: Un nome e numero di riferimento di un sistema di specificazione, come [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) o [Omniclass](http://www.omniclass.org/).
-   **Code browser button**: Non ancora implementato - permetterà di aprire il riferimento in un browser web
-   **URL**: Un URL in si possono trovare ulteriori informazioni sul materiale
-   **URL button**:Apre l\'URL in un browser Web


</div>

## Relazione con IFC 

Questo corrisponde approssimativamente a [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SetMaterial/it
