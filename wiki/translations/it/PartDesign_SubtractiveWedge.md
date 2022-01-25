# PartDesign SubtractiveWedge/it
---
- GuiCommand:/it   Name:PartDesign SubtractiveWedge   Name/it:Cuneo sottrattivo   Workbenches:[MenuLocation:Part Design → Crea una primitiva sottrattiva → Cuneo   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce un cuneo sottrattivo nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractiveWedge_example.svg ) \'\' A sinistra il corpo attivo (A) mostrato in grigio e il cuneo sottrattivo (B) mostrato in rosso trasparente; a destra il risultato. \'\'

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractiveWedge.png" width=24px> '''Cuneo sottrattivo'''**. **Nota**: Il Cuneo sottrattivo fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere al Cuneo, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Cuneo nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Cuneo.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione il cuneo può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà

Usando il posizionamento predefinito, gli input sottostanti sono:

-    {{PropertyData/it|X min/max}}: Estensione sull\'asse X della faccia di base

-    {{PropertyData/it|Y min/max}}: Altezza del cuneo

-    {{PropertyData/it|Z min/max}}: Estensione sull\'asse Z della faccia di base

-    {{PropertyData/it|X2 min/max}}: Estensione sull\'asse X della faccia superiore

-    {{PropertyData/it|Z2 min/max}}: Estensione sull\'asse Z della faccia superiore

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveWedge/it
