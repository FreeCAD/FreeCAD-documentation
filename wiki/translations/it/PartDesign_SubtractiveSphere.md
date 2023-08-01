# PartDesign SubtractiveSphere/it
---
- GuiCommand:/it   Name:PartDesign SubtractiveSphere   Name/it:Sfera sottrattiva   Workbenches:[MenuLocation:Part Design → Crea una primitiva sottrattiva → Sfera   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce una sfera sottrattiva nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractiveSphere_example.svg ) *A sinistra il corpo attivo (A) mostrato in grigio e la sfera sottrattiva (B) mostrata in rosso trasparente; a destra il risultato.*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractiveSphere.png" width=24px> '''Sfera sottrattiva'''**. **Nota**: La sfera sottrattiva fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere alla sfera, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Sfera nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Sfera.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione la sfera può essere modificata in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite le [Proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto sfera. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius}}: Raggio della sfera.

-    {{PropertyData/it|Angle1}}: (etichettato *Parametro V* nei parametri Primitive) Troncamento inferiore della sfera, parallelo alla sezione trasversale circolare (-90 gradi in una sfera piena)

-    {{PropertyData/it|Angle2}}: (non etichettato nei parametri primitivi) troncatura superiore dell\'ellissoide, parallelo alla sezione trasversale circolare (90 gradi in una sfera piena).

-    {{PropertyData/it|Angle3}}: (etichettato *parametro U* nei parametri primitivi) angolo di rotazione della sezione trasversale (360 gradi in una sfera completa).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveSphere/it
