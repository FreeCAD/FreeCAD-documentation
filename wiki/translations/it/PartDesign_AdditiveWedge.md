# PartDesign AdditiveWedge/it
---
- GuiCommand   */it   Name   *PartDesign AdditiveWedge   Name/it   *Cuneo additivo   Workbenches   *[MenuLocation   *Part Design → Crea una primitiva additiva → Cuneo   Version   *0.17   SeeAlso   *[[PartDesign CompPrimitiveAdditive/it|Primitive additive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce un cuneo primitivo nel corpo attivo come prima caratteristica o lo fonde con le caratteristiche esistenti.

<img alt="" src=images/PartDesign_AdditiveWedge_example.png  style="width   *200px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_AdditiveWedge.png" width=24px> '''Cuneo additivo'''**. **Nota**   * Il Cuneo additivo fa parte di un menu di icone etichettato *Crea una primitiva additiva*. Dopo l\'avvio, FreeCAD visualizza Cubo additivo nella barra degli strumenti. Per accedere al Cuneo, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Cuneo nel menu.
2.  Impostare i parametri della primitiva e [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Cuneo.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione il cuneo può essere modificato in due modi   *

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà

Usando il posizionamento predefinito, gli input sottostanti sono   *

-    {{PropertyData/it|X min/max}}   * Estensione sull\'asse X della faccia di base

-    {{PropertyData/it|Y min/max}}   * Altezza del cuneo

-    {{PropertyData/it|Z min/max}}   * Estensione sull\'asse Z della faccia di base

-    {{PropertyData/it|X2 min/max}}   * Estensione sull\'asse X della faccia superiore

-    {{PropertyData/it|Z2 min/max}}   * Estensione sull\'asse Z della faccia superiore

## Pyramids

Wedges can be used to create pyramids by setting **X2 min/max** and **Z2 min/max** each so that min = max.


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveWedge/it
