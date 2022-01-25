---
- GuiCommand:/it
   Name:Sketcher CreateEllipseBy3Points
   Name/it:Ellisse da tre punti
   Icon:Sketcher_CreateEllipse_3points.png
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Geometrie → Ellisse da 3 punti
   Version:0.15
   SeeAlso:[Ellisse da centro ...](Sketcher_CreateEllipseByCenter/it.md), [Cerchio](Sketcher_CreateCircle/it.md), [Arco di ellisse ...](Sketcher_CreateArcOfEllipse/it.md)
---

# Sketcher CreateEllipseBy3Points/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Questo strumento disegna un\'ellisse selezionando tre punti: (1) Periasse (Primo incrocio del diametro maggiore con l\'ellisse), (2) apoasse (Secondo incrocio del diametro maggiore con l\'ellisse), (3) un punto su un lato del diametro più lungo (a) che definisce il raggio minore (b). (c) è il centro risultante e (f) sono i punti focali.


</div>

Quando si avvia lo strumento, il puntatore del mouse si trasforma in una croce bianca con un\'icona a forma di ellisse rossa.

![](images/Ellipse_3Point.png‎ )


<div class="mw-translate-fuzzy">

*La sequenza di clic è indicata da frecce gialle con numeri. 1 è il periasse, 2 è l\'apoasse, 3 è il punto di definizione per il diametro minore, le linee verdi sono i diametri maggiori e minori. Le linee blu sono linee di costruzione casuali fatte solo a scopo illustrativo.*


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

Premere il pulsante **[<img src=images/Sketcher_CreateEllipse_3points.png style="width:24px"> '''Ellisse da 3 punti'''**.

-   Il pr\* imo clic nella vista 3D imposta un punto che definisce l\'incrocio del diametro maggiore con l\'ellisse (periasse). Il secondo clic nella vista 3D imposta un punto che definisce l\'incrocio del diametro maggiore con l\'ellisse opposta al punto centrale (apoasse). Il terzo clic imposta un punto sull\'ellisse che definisce il raggio minore.


</div>


<div class="mw-translate-fuzzy">

-   Dopo il terzo clic, viene creata l\'ellisse, insieme ad un gruppo di geometrie costruttive allineate ad esso (diametro maggiore, diametro minore, due fuochi). La geometria della costruzione può essere cancellata manualmente se non è necessaria e ricreata in seguito. Vedere il vincolo [Allineamento interno](Sketcher_ConstrainInternalAlignment/it.md) e come [Mostrare o nascondere la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md).
-   Premere **Esc** o fare clic con il tasto destro del mouse per annullare la funzione.


</div>

## Peculiarities


<div class="mw-translate-fuzzy">

## Peculiarità

-   Gli assi maggiore e minore dell\'ellisse sono tassativi e non possono essere scambiati ridimensionando l\'ellisse. Questo a causa della solutozione parametrica utilizzata (centro (x,y), fuoco1 (x,y), lunghezza del raggio minore (b)) e lo stesso comportamento fiscale di OpenCascade. Per scambiare gli assi l\'ellisse deve essere ruotata.
-   Ellisse può funzionare come un cerchio quando le sue linee diametro maggiore e minore vengono eliminate e uno dei fuochi è vincolato a coincidere con il centro. Ma su tale cerchio il vincolo raggio non funziona.
-   Spostare l\'ellisse dal bordo equivale a spostare il suo centro.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseBy3Points/it
