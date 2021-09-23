# Material editor/it
---
- GuiCommand:/it   Name:Material_editor   Name/it:Editor dei materiali   Icon:Arch_Material_Group.svg   MenuLocation:Modello → Materiali → Editor dei materiali   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/it|Tutorial FEM](FEM_Workbench/it___FEM]].md)---


</div>

## Descrizione


<div class="mw-translate-fuzzy">

L\'editor dei materiali consente di modificare e salvare le informazioni contenute in un [materiale](Material/it.md) di FreeCAD. Attualmente tali materiali sono utilizzati dagli ambienti [FEM](FEM_Workbench/it.md) e [Arch](Arch_Workbench/it.md).


</div>

![](images/Material_editor.jpg )


<div class="mw-translate-fuzzy">

## Utilizzo


</div>


<div class="mw-translate-fuzzy">

All\'editor dei materiale attualmente si può accedere da:


</div>


<div class="mw-translate-fuzzy">

-   Ambiente Arch:
    -   Dal pulsante **Edit material** del pannello di creazione dei [nuovi materiali](Arch_SetMaterial/it.md) del modulo [Arch](Arch_Workbench/it.md)
-   Ambiente FEM:
    -   Dal menu Modello → Materiali → Material editor
    -   Dall\'icona Material editor
-   Via python:


</div>

## Opzioni


<div class="mw-translate-fuzzy">

-   **Browser button**: Apre il contenuto della proprietà URL in un browser
-   **Material card**: Permette di scegliere un preset per riempire i campi
-   **Open**: Apre un file .FCMat
-   **Save as**: Salva il contenuto dell\'editor come un nuovo file .FCMat
-   **Preview**: Nn ancora implementato
-   **Properties editor**: Permette di modificare il contenuto delle proprietà del materiale
-   **Add property**: Permette di aggiungere una nuova proprietà personalizzata
-   **Delete property**: Elimina una proprietà selezionata. Possono essere eliminate solo le proprietà personalizzate


</div>

Note:


<div class="mw-translate-fuzzy">

-   I pulsanti **OK** e **Cancel** hanno e lo stesso effetto quando l\'editor del materiale non viene utilizzato per modificare direttamente la proprietà materiale di un oggetto esistente.


</div>

## Script


```python
import MaterialEditor
MaterialEditor.openEditor()
```


<div class="mw-translate-fuzzy">





</div>


{{FEM Tools navi

}}

---
[documentation index](../README.md) > [Material](Material_Workbench.md) > Material editor/it
