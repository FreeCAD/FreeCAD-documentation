# PartDesign SubtractiveTorus/it
---
- GuiCommand:/it   Name:PartDesign SubtractiveTorus   Name/it:Toro sottrattivo   Workbenches:[MenuLocation:Part Design → Crea una primitiva sottrattiva → Toro   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce un toro sottrattivo nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractiveTorus_example.svg ) \'\' A sinistra il corpo attivo (A) mostrato in grigio e il toro sottrattivo (B) mostrato in rosso trasparente; a destra il risultato. \'\'

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractiveTorus.png" width=24px> '''Toro sottrattivo'''**. **Nota**: Il Toro sottrattivo fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere al Toro, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Toro nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Toro.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione il toro può essere modificato in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Toro. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius1}}: Raggio dell\'orbita immaginaria attorno alla quale ruota la sezione circolare. (La distanza tra il centro del toro e il centro della sezione trasversale)

-    {{PropertyData/it|Radius2}}: Raggio della sezione trasversale circolare che definisce la forma del toro.

-    {{PropertyData/it|Angle1}}: (etichettato \'\' Parametro V \'\' nei parametri primitivi) Troncamento inferiore del toro, parallelo alla sezione trasversale circolare (-180° in un toro pieno). Un bug nel codice causa risultati imprevisti quando si modifica Angle1.

-    {{PropertyData/it|Angle2}}: (non etichettato nei parametri primitivi) troncatura superiore dell\'ellissoide, parallela alla sezione trasversale circolare (180° in un toro pieno). Un bug nel codice causa risultati imprevisti quando si modifica Angle2.

-    {{PropertyData/it|Angle3}}: (etichettato \'\' parametro U \'\' nei parametri primitivi) angolo di rotazione della sezione trasversale circolare (360° in un toro pieno).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveTorus/it
