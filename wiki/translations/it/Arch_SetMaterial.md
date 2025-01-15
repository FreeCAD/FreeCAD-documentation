---
 GuiCommand:
   Name: Arch SetMaterial
   Name/it: Arch Materiale
   MenuLocation: Arch , Strumenti di materiali , Materiale
   Workbenches: Arch_Workbench/it, BIM_Workbench/it
   Shortcut: **M** **T**
   SeeAlso: Arch_MultiMaterial/it
---

# Arch SetMaterial/it



## Descrizione

Questo strumento permette di aggiungere dei [materiali](Material/it.md) al documento attivo, e di attribuire un materiale ad un oggetto di [Arch](Arch_Workbench/it.md). Un Materiale possiede tutte le proprietà di un determinato materiale, e controlla il colore dell\'oggetto a cui è collegato. I materiali vengono memorizzati in una cartella **Materials** nel documento attivo.

![](images/Arch_materials_01.jpg )



## Utilizzo

1.  Facoltativamente, selezionare uno o più oggetti a cui si desidera attribuire un nuovo materiale.
2.  Esistono diversi modi per richiamare il comando:
    -   Premere il pulsante **<img src="images/Arch_SetMaterial.svg" width=16px> [Imposta materiale](Arch_SetMaterial/it.md)** nella barra degli strumenti.
    -   Usare la scorciatoia **M** e poi **T** da tastiera.
    -   Usare il comando **Arch → Strumenti materiali → Materiale** dal menu principale.
3.  Caricare un materiale predefinito, o crearne uno nuovo riempiendo i campi.
4.  Premere **OK**.



## Opzioni

-   Al momento della creazione di un nuovo materiale, un pannello consente di impostare le diverse opzioni:

![](images/Arch_materials_02.jpg )

-   **Choose preset**: Scegliere uno dei materiali preimpostati, da utilizzare come è, o per adattarlo modificando i campi sottostanti
-   **Name**: Scegliere un nome per il materiale
-   **Edit button**: Questo apre il materiale corrente nel [Editor dei materiali](FEM_MaterialEditor/it.md) di FreeCAD, che permette di modificare molte proprietà aggiuntive e di aggiungere le proprie personalizzate
-   **Description**: Una descrizione più dettagliata del materiale
-   **Color**: Il colore di visualizzazione per il materiale, che sarà applicato a tutti gli oggetti che utilizzano tale materiale
-   **Section Color**: un colore di visualizzazione per il materiale, che verrà applicato sulle pagine TechDraw, quando un oggetto con questo materiale viene sezionato e la proprietà \"Display materials\" del piano di sezione contenente è impostata su True .
-   **Code**: Un nome e numero di riferimento di un sistema di specificazione, come [Masterformat](https://en.wikipedia.org/wiki/MasterFormat) o [Omniclass](http://www.omniclass.org/).
-   **Code browser button**: Non ancora implementato - permetterà di aprire il riferimento in un browser web
-   **URL**: Un URL in cui si possono trovare ulteriori informazioni sul materiale
-   **URL button**: Apre l\'URL in un browser Web



## Relazione con IFC 

Questo corrisponde approssimativamente a [IfcMaterial](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/link/ifcmaterial.htm).



---
⏵ [documentation index](../README.md) > Arch SetMaterial/it
