---
 GuiCommand:
   Name: FEM MaterialEditor
   Name/it: Editor dei materiali
   MenuLocation: Modello , Materiali , Editor dei materiali
   Workbenches: FEM_Workbench/it, Arch_Workbench/it
   Version: 0.18
   SeeAlso: Arch_SetMaterial/it, FEM_tutorial/it
---

# FEM MaterialEditor/it


</div>



## Descrizione


<div class="mw-translate-fuzzy">

L**\'Editor dei materiali** consente di modificare e salvare le informazioni contenute in un [Materiale di FreeCAD](Material/it.md). Attualmente tali materiali sono utilizzati dai banchi da lavoro <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/it.md) e <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md).


</div>

![](images/Material_editor.png )



## Utilizzo

All\'editor dei materiale attualmente si può accedere da:


<div class="mw-translate-fuzzy">

1.  <img alt="" src=images/Workbench_Arch.svg  style="width:24px;"> [Arch](Arch_Workbench/it.md):
    -   Il pulsante **<img src="images/Arch_SetMaterial.svg" width=16px> [Materiale](Arch_SetMaterial/it.md)**.
    -   La voce di menu **Arch → Strumenti di materiali → <img src="images/Arch_SetMaterial.svg" width=16px> Materiale**.
2.  <img alt="" src=images/Workbench_FEM.svg  style="width:24px;"> [FEM](FEM_Workbench/it.md):
    -   Il pulsante **<img src="images/FEM_MaterialEditor.svg" width=16px> [Materiale](FEM_MaterialEditor/it.md)**.
    -   La voce di menu **Model → Materiali → <img src="images/FEM_MaterialEditor.svg" width=16px> Editor dei Materiali**.


</div>



## Opzioni

-   **Browser button**: Apre il contenuto della proprietà URL in un browser
-   **Material card**: Permette di scegliere un preset per riempire i campi
-   **Open**: Apre un file .FCMat
-   **Save as**: Salva il contenuto dell\'editor come un nuovo file .FCMat
-   **Preview**: Nn ancora implementato
-   **Properties editor**: Permette di modificare il contenuto delle proprietà del materiale
-   **Add property**: Permette di aggiungere una nuova proprietà personalizzata
-   **Delete property**: Elimina una proprietà selezionata. Possono essere eliminate solo le proprietà personalizzate

 {{Arch Tools navi/it}}

-   I pulsanti **OK** e **Cancel** hanno e lo stesso effetto quando l\'editor del materiale non viene utilizzato per modificare direttamente la proprietà materiale di un oggetto esistente.

!!FUZZY!!


{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [Arch](Category_Arch.md) > [FEM](Category_FEM.md) > FEM MaterialEditor/it
