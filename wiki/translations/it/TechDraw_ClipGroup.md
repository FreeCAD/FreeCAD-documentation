---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/it: TechDraw Gruppo di ritaglio
   MenuLocation: TechDraw , Viste TechDraw , Gruppo di ritaglio
   Workbenches: TechDraw_Workbench/it
   SeeAlso: 
---

# TechDraw ClipGroup/it



## Descrizione

Lo strumento **TechDraw Gruppo di ritaglio** crea una finestra di ritaglio (clip) che può contenere Viste.

![](images/TechDraw_Clipview.png ) 
*Finestra di ritaglio di diverse viste esistenti*



## Utilizzo

1.  Se nel documento sono presenti più pagine di disegno: facoltativamente attivare la pagina desiderata selezionandola nella [Vista ad albero](Tree_view/it.md).
2.  Esistono diversi modi per richiamare lo strumento:
    -   Premere il pulsante **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Inserisci Gruppo di ritaglio](TechDraw_ClipGroup/it.md)**.
    -   Selezionare l\'opzione **TechDraw → Viste TechDraw → <img src="images/TechDraw_ClipGroup.svg" width=16px> Inserisci Gruppo di ritaglio** dal menu.
3.  Se nel documento sono presenti più pagine di disegno e non si ha ancora attivato una pagina, si apre la finestra di dialogo **Scelta pagina**:
    1.  Selezionare la pagina desiderata.
    2.  Premere il pulsante **OK**.
4.  Le viste possono essere trascinate e rilasciate da e verso il Gruppo di ritaglio (Clip) nella vista ad albero. {{Version/it|1.0}}



## Proprietà

Vedere anche: [Editor delle proprietà](Property_editor/it.md).

Un Ggruppo di ritaglio, formalmente un oggetto {{Incode|TechDraw::DrawViewClip}}, ha le [proprietà](TechDraw_View/it#Properties_Part_View.md) comuni a tutti i tipi di visualizzazione. Ha anche le seguenti proprietà aggiuntive.



### Dati


{{TitleProperty|Clip Group}}

-    **Width|Length**: La larghezza della finestra di ritaglio in unità

-    **Height|Length**: L\'altezza della finestra di ritaglio in unità

-    **ShowFrame|Bool**: Quando è vero, mostra una cornice attorno alla finestra di ritaglio

-    **Views|LinkList**: Le Viste contenute nella finestra di ritaglio





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/it
