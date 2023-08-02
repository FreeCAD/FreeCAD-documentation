---
- GuiCommand:
   Name: FEM MaterialEditor
   Name/it: Editor dei materiali
   MenuLocation: Modello -> Materiali -> Editor dei materiali
   Workbenches: FEM_Workbench/it
   Shortcut: 
   SeeAlso: FEM_tutorial/it
---

# FEM MaterialEditor/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

L\'editor dei materiali consente di modificare e salvare le informazioni contenute in un [materiale](Material.md) di FreeCAD. Attualmente tali materiali sono utilizzati dagli ambienti [FEM](FEM_Workbench/it.md) e [Arch](Arch_Workbench/it.md).


</div>


<div class="mw-translate-fuzzy">

![](images/Material_editor.jpg )


</div>

## Utilizzo

All\'editor dei materiale attualmente si può accedere da:


<div class="mw-translate-fuzzy">

-   Ambiente Arch:
    -   Dal pulsante **Edit material** del pannello di creazione dei [nuovi materiali](Arch_SetMaterial/it.md) del modulo [Arch](Arch_Workbench/it.md)
-   Ambiente FEM:
    -   Dal menu Modello → Materiali → Material editor
    -   Dall\'icona Material editor
-   Via python:


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
