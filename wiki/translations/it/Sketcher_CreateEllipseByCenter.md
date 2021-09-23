---
- GuiCommand:/it
   Name:Sketcher CreateEllipse
   Name/it:Ellisse da centro
   Icon:Sketcher_CreateEllipse.svg
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Geometrie → Ellisse da centro
   Version:0.15
   SeeAlso:[Ellisse da 3 punti](Sketcher_CreateEllipseBy3Points/it.md), [Cerchio](Sketcher_CreateCircle/it.md), [Arco di ellisse](Sketcher_CreateArcOfEllipse/it.md)
---

# Sketcher CreateEllipseByCenter/it


</div>

## Descrizione

Questo strumento disegna un ellisse selezionando tre punti: il centro, la fine del raggio maggiore, il raggio minore. Quando si avvia lo strumento, il puntatore del mouse si trasforma in una croce bianca con un\'icona a forma di ellisse rossa. Le coordinate sono indicate in tempo reale.


<div class="mw-translate-fuzzy">

<img alt="La sequenza della selezione è indicata dalle frecce gialle con i numeri. C è il centro, a è il diametro maggiore, b è il diametro minore, F1 e F2 sono i fuochi." src=images/Sketcher_EllipseExample1.png‎  style="width:500px;">


</div>


*The sequence of clicks is indicated by yellow arrows with numbers. C is the center, a - major diameter, b - minor diameter, F1, F2 are foci.*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Richiamare il comando facendo clic sul pulsante nella barra degli strumenti, scegliendo la voce nel menu, oppure usando la scorciatoia da tastiera che però deve essere assegnata prima in [Personalizza l\'interfaccia](Interface_Customization/it.md).
-   Il primo clic nella vista 3D imposta il centro dell\'ellisse. Il secondo clic imposta il primo raggio e l\'orientamento dell\'ellisse. Il terzo clic imposta l\'altro raggio (il secondo raggio è la distanza dalla linea definita dai primi due clic).
-   Dopo il terzo clic, viene creata l\'ellisse, insieme ad una serie di geometrie di costruzione allineate ad essa (diametro maggiore, diametro minore, due fuochi). La geometria di costruzione può essere cancellata manualmente se non è necessaria, e ricreata in seguito. Vedere [Vincoli di allineamento interni](Sketcher_ConstrainInternalAlignment/it.md) e [Mostra/Nascondi la geometria interna](Sketcher_RestoreInternalAlignmentGeometry/it.md).
-   Premere **Esc** o cliccare sul tasto destro del mouse per annullare la funzione.


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
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateEllipseByCenter/it
