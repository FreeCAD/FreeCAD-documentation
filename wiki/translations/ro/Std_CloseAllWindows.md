---
- GuiCommand:   Name:Std_CloseAll   MenuLocation:[Workbenches:All   Shortcut:...   SeeAlso:[[Std_Close|Close](Std_File_Menu___File]]_→_Close_All.md), [Save As...](Std_SaveAs.md) e [Save](Std_Save.md)---


</div>

## Descriere

Comanda închide toate documentele proiectului, chiar și cele care nu sunt active. Cu această comandă nu ieșiți din FreeCAD.

The **Std CloseAllWindows** command closes all windows, thereby closing all documents.

## Utilizare

Alegeți ** File** → ** Close All** din meniul principal. Dacă în proiect există documente nesalvate sau modificate, se afișează un mesaj și sunteți întrebați dacă doriți să le salvați: ![](images/UnsavedDocument.png )

În cazul unui răspuns afirmativ,

-   dacă documentul a fost deja salvat, utilizați numele și setul de adrese,
-   dacă documentul nu a fost salvat niciodată, deschideți fereastra pentru a defini calea și a atribui un nume documentului:

![](images/FileSaveAs.png )  Comanda **Chiudi** în schimb, închide doar documentul activ și permite continuarea lucrului cu alte documente ale proiectului. 

### Link

[Comandi per categorie](ComandiPerCategorie/it.md)

1.  Select the **File → <img src="images/Std_CloseAllWindows.svg" width=16px> Close All** option from the menu.
2.  If there are unsaved documents a dialog box will prompt you to save them:
    -   Press the **Save** button to save the active document. If required enter a filename first.
    -   Press the **Discard** button to discard the active document and lose all changes.

## Options

-   When the dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.
-   If there are multiple unsaved documents: check the {{CheckBox|TRUE|Apply answer to all}} checkbox to avoid being prompted for each unsaved document separately.

## Notes

-   A document can also be closed by right-clicking it in the [Tree view](Tree_view.md) and selecting **Close document** from the context menu.

## Preferences

-   The last used file location is stored: **Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath**.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To close a document use the `closeDocument` method of the FreeCAD application. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}  
