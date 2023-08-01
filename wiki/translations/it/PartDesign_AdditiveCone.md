---
- GuiCommand:
   Name:PartDesign AdditiveCone
   Name/it:Cono additivo
   Workbenches:[PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Part Design - Crea una primitiva additiva - Cono
   Version:0.17
   SeeAlso:[Primitive additive](PartDesign_CompPrimitiveAdditive/it.md)
---

# PartDesign AdditiveCone/it


</div>

## Descrizione

Inserisce un cono primitivo nel corpo attivo come prima caratteristica o lo fonde con le caratteristiche esistenti.

<img alt="" src=images/PartDesign_AdditiveCone_example.png  style="width:200px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_AdditiveCone.png" width=24px> '''Cono additivo'''**. **Nota**: Il Cono additivo fa parte di un menu di icone etichettato *Crea una primitiva additiva*. Dopo l\'avvio, FreeCAD visualizza Cubo additivo nella barra degli strumenti. Per accedere al Cono, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Cono nel menu.
2.  Impostare i parametri della primitiva e [Attachment](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Cono.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione il cono può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Cono. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius1}}: Il valore del raggio alla base del cono.

-    {{PropertyData/it|Radius2}}: Il valore del raggio nella parte superiore del cono. Un valore diverso da zero crea un tronco di cono.

-    {{PropertyData/it|Height}}: L\'altezza del cono lungo il suo asse.

-    {{PropertyData/it|Angle}}: Angolo di rotazione della sezione trasversale (360 gradi in un cono completo).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveCone/it
