---
- GuiCommand:/it   Name:PartDesign AdditivePrism   Name/it:Prisma additivo   Workbenches:[MenuLocation:Part Design → Crea una primitiva additiva → Prisma   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveAdditive/it|Primitive additive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce un prisma primitivo nel corpo attivo come prima caratteristica o lo fonde con le caratteristiche esistenti.

<img alt="" src=images/PartDesign_AdditivePrism_example.png  style="width:200px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_AdditivePrism.png" width=24px> '''Prisma additivo'''**. **Nota**: Il Prisma additivo fa parte di un menu di icone etichettato *Crea una primitiva additiva*. Dopo l\'avvio, FreeCAD visualizza Cubo additivo nella barra degli strumenti. Per accedere al Prisma, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Prisma nel menu.
2.  Impostare i parametri della primitiva e [Attachment](Part_Attachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Prisma.


</div>

## Opzioni

It is possible to create skewed prisms by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">

Dopo la sua creazione il Prisma può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_Attachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Prisma. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Polygon}}: numero di lati nella sezione trasversale del poligono del prisma.

-    {{PropertyData/it|Circumradius}}: [raggio de cerchio circoscritto](https://en.wikipedia.org/wiki/Circumscribed_circle) della sezione trasversale del poligono del prisma.

-    {{PropertyData/it|Height}}: altezza del prisma.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}  
