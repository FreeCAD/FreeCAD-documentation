---
- GuiCommand:   Name:Std Close   MenuLocation:[|Workbenches:All   Shortcut:Ctrl+W   SeeAlso:[[Std CloseAll|CloseAll](Std_File_Menu___File]]_→_Close.md)---


</div>

Închide documentul curent {{GuiCommand/it|Name=Std_Close|Name/it=Chiudi|MenuLocation=[File](Std_File_Menu/it.md) → Chiudi|Workbenches=Tutti|Shortcut=Crtl+W|SeeAlso=[Chiudi tutto](Std_CloseAll/it.md), [Salva con nome...](Std_SaveAs/it.md) e [Salva](Std_Save/it.md)}}

### Descriere

Comanda închide numai documentul activ și vă permite să continuați să lucrați la alte documente ale proiectului.

Dacă documentul nu a fost salvat sau a fost modificat, afișează un mesaj și întreabă dacă doriți să îl salvați:

![](images/UnsavedDocument.png )

În cazul unui răspuns afirmativ,

-   dacă documentul a fost deja salvat, utilizați numele și setul de adrese,
-   dacă documentul nu a fost salvat niciodată, deschideți fereastra pentru a defini calea și a atribui un nume documentului:

![](images/FileSaveAs.png ) 

Comanda {{KEY/it|Chiudi tutto}} închide toate documentele proiectului .

Cu această comandaă nu se iese din FreeCAD.

### Link

[Comandi per categorie](ComandiPerCategorie/it.md)

The **Std CloseActiveWindow** command closes the active window. To close a document all its windows must be closed.

## Usage

1.  There are several ways to invoke the command:
    -   Select the {{MenuCommand|File → <img src="images/Std_CloseActiveWindow.svg" width=16px> Close}} option from the menu.
    -   Use the keyboard shortcut: **Ctrl**+**F4**.
2.  To close a document: repeat this for all windows belonging to it.
3.  When closing the last window of a document that has not been saved, a dialog box will prompt you to save it:
    -   Press the **Save** button to save the document. If required enter a filename first.
    -   Press the **Discard** button to discard the document and lose all changes.

## Options

-   When the dialog box is displayed: press **Esc** or the **Cancel** button to abort the command.

## Notes

-   The command can only close [docked](Std_ViewDockUndockFullscreen.md) windows.
-   A document can also be closed by right-clicking it in the [Tree view](Tree_view.md) and selecting {{MenuCommand|Close document}} from the context menu.

## Preferences

-   The last used file location is stored: {{MenuCommand|Tools → Edit parameters... → BaseApp → Preferences → General → FileOpenSavePath}}.

## Scripting


**See also:**

[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

To close a document use the `closeDocument` method of the FreeCAD application. For a scripting example see [Std New](Std_New.md).





{{Std Base navi

}}  
