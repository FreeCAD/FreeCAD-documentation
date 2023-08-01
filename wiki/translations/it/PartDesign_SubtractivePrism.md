# PartDesign SubtractivePrism/it
---
- GuiCommand:   Name: PartDesign SubtractivePrism   Name/it: Prisma sottrattivo   Workbenches: [MenuLocation: Part Design - Crea una primitiva sottrattiva - Prisma   Version: 0.17   SeeAlso: [[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>



## Descrizione

Inserisce un prisma sottrattivo nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractivePrism_example.svg )

*A sinistra il corpo attivo (A) mostrato in grigio e il prisma sottrattivo (B) mostrato in rosso trasparente; a destra il risultato.*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractivePrism.png" width=24px> '''Prisma sottrattivo'''**. **Nota**: Il Prisma sottrattivo fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere al Prisma, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Prisma nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Prisma.


</div>



## Opzioni

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment.


<div class="mw-translate-fuzzy">

Dopo la sua creazione il Prisma può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>



## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Prisma. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Polygon}}: numero di lati nella sezione trasversale del poligono del prisma.

-    {{PropertyData/it|Circumradius}}: [raggio de cerchio circoscritto](https://en.wikipedia.org/wiki/Circumscribed_circle) della sezione trasversale del poligono del prisma.

-    {{PropertyData/it|Height}}: altezza del prisma.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractivePrism/it
