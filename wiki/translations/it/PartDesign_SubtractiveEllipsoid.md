# PartDesign SubtractiveEllipsoid/it
---
- GuiCommand   */it   Name   *PartDesign SubtractiveEllipsoid   Name/it   *Ellissoide sottrattivo   Workbenches   *[MenuLocation   *Part Design → Crea una primitiva sottrattiva → Ellissoide   Version   *0.17   SeeAlso   *[[PartDesign CompPrimitiveSubtractive/it|Primitive sottrattive](PartDesign_Workbench/it___PartDesign]].md)---


</div>

## Descrizione

Inserisce un ellissoide sottrattivo nel corpo attivo. La sua forma viene sottratta dal solido esistente.

![](images/PartDesign_SubtractiveEllipsoid_example.svg )

\'\' A sinistra il corpo attivo (A) mostrato in grigio e l\'ellissoide sottrattivo (B) mostrato in rosso trasparente; a destra il risultato. \'\'

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/PartDesign_SubtractiveEllipsoid.png" width=24px> '''Ellissoide sottrattivo'''**. **Nota**   * Ellissoide sottrattivo fa parte di un menu di icone etichettato *Crea una primitiva sottrattiva*. Dopo l\'avvio, FreeCAD visualizza Cubo sottrattivo nella barra degli strumenti. Per accedere all\'ellissoide, fare clic sulla freccia verso il basso accanto all\'icona visibile e selezionare Ellissoide nel menu.
2.  Impostare i parametri della primitiva e il modo di [Associazione](Part_EditAttachment/it.md).
3.  Cliccare **OK**.
4.  Nel corpo attivo viene visualizzata una funzione Ellissoide.


</div>

## Opzioni


<div class="mw-translate-fuzzy">

Dopo la sua creazione l\'ellissoide può essere modificato in due modi   *

-   Fare doppio clic nella struttura del modello, oppure fare clic con il tasto destro e selezionare **Modifica primitiva** nel menu contestuale; questo richiama i parametri primitivi.
-   Tramite le [Proprietà](Property_editor/it.md).


</div>

## Proprietà


<div class="mw-translate-fuzzy">

-    {{PropertyData/it|Attachment}}   * Definisce la modalità e l\'offset di associazione. Vedere [Associazione](Part_EditAttachment/it.md).

-    {{PropertyData/it|Label}}   * Etichetta data all\'oggetto ellissoide. Modificabile secondo le proprie esigenze.

-    {{PropertyData/it|Radius1}}   * il valore del raggio lungo l\'asse verticale dell\'ellissoide; di default, parallelo all\'asse Z.

-    {{PropertyData/it|Radius2}}   * il valore del raggio lungo la lunghezza dell\'ellissoide; di default, parallelo all\'asse X.

-    {{PropertyData/it|Radius3}}   * il valore del raggio lungo la larghezza dell\'ellissoide; di default, parallelo all\'asse Y. Al valore predefinito di zero, l\'ellissoide forma un [oblate spheroid](http   *//en.wikipedia.org/wiki/Oblate_spheroid).

-    {{PropertyData/it|Angle1}}   * (etichettato \"Parametro V\" nei parametri primitivi) Troncamento inferiore dell\'ellissoide, parallelo alla sezione trasversale circolare (-90 gradi in uno sferoide completo)

-    {{PropertyData/it|Angle2}}   * (non etichettato nei parametri primitivi) troncatura superiore dell\'ellissoide, parallelo alla sezione trasversale circolare (90 gradi in uno sferoide completo).

-    {{PropertyData/it|Angle3}}   * (etichettato \'\' parametro U \'\' nei parametri primitivi) angolo di rotazione della sezione trasversale ellittica (360 gradi in uno sferoide completo).


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign SubtractiveEllipsoid/it
