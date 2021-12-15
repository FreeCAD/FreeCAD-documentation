# PartDesign AdditiveSphere/it
---
- GuiCommand:/it   Name:PartDesign AdditiveSphere   Name/it:Sfera additiva   Workbenches:[MenuLocation:Part Design → Crea una primitiva additiva → Sfera   Shortcut:None   Version:0.17   SeeAlso:[[PartDesign CompPrimitiveAdditive/it|Primitive additive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce una sfera primitiva nel corpo attivo come prima caratteristica o la fonde con le caratteristiche esistenti.

<img alt="" src=images/PartDesign_AdditiveSphere_example.png  style="width:200px;">

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_AdditiveSphere.png" width=24px> '''Sfera additiva'''**. **Nota**: La sfera additiva fa parte di un menu di icone etichettato *Crea una primitiva additiva*. Dopo l\'avvio, FreeCAD visualizza Cubo additivo nella barra degli strumenti. Per accedere alla sfera, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Sfera nel menu.
2.  Impostare i parametri della primitiva e [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Sfera.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione la sfera può essere modificata in due modi:

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite l\'[editor delle proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}: Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}: Etichetta data all\'oggetto Cono. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius}}: Raggio della sfera.

-    {{PropertyData/it|Angle1}}: (etichettato \'\' Parametro V \'\' nei parametri Primitive) Troncamento inferiore della sfera, parallelo alla sezione trasversale circolare (-90 gradi in una sfera piena)

-    {{PropertyData/it|Angle2}}: (non etichettato nei parametri primitivi) troncatura superiore dell\'ellissoide, parallelo alla sezione trasversale circolare (90 gradi in una sfera completa).

-    {{PropertyData/it|Angle3}}: (etichettato \'\' parametro U \'\' nei parametri primitivi) angolo di rotazione della sezione trasversale (360 gradi in una sfera piena).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign AdditiveSphere/it
