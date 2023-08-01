# PartDesign SubtractiveCylinder/it
---
- GuiCommand:/it   Name:PartDesign SubtractiveCylinder   Name/it:Cilindro sottrattivo   Workbenches:[MenuLocation:Part Design → Crea una primitiva sottrattiva → Cilindro   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>



## Descrizione

Inserisce un cilindro sottrattivo nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractiveCylinder_example.svg )

*A sinistra il corpo attivo (A) mostrato in grigio e il cilindro sottrattivo (B) mostrato in rosso trasparente; a destra il risultato.*



## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractiveCylinder.png" width=24px> '''Cilindro sottrattivo'''**. **Nota**: Il Cilindro sottrattivo fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere al Cilindro, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Cilindro nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Cilindro.


</div>



## Opzioni

It is possible to create skewed cylinders by specifying angles in respect to the normal vector of the chosen attachment. <small>(v0.20)</small> 


<div class="mw-translate-fuzzy">

Dopo la sua creazione il cilindro può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>



## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Cilindro. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius}}: Il valore del raggio del cilindro.

-    {{PropertyData/it|Angle}}: Angolo di rotazione della sezione trasversale (360 gradi in un cilindro completo).

-    {{PropertyData/it|Height}}: L\'altezza del cilindro lungo il suo asse.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveCylinder/it
