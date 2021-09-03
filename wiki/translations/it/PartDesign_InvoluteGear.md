---
- GuiCommand:/it
   Name:PartDesign InvoluteGear
   Name/it:DisegnoPezzo IngranaggioEvolvente
   MenuLocation:DisegnoPezzo → Ingranaggio Evolvente...
   Workbenches:[DisegnoPezzo](PartDesign_Workbench/it.md)
---


</div>

## Descrizione

Questo strumento consente di creare un profilo 2D dell\'evolvente di un ingranaggio. Questo profilo 2D è completamente parametrico, e può essere estruso con la funzione [DisegnoPezzo Pad](PartDesign_Pad/it.md) di PartDesign.
Per informazioni più dettagliate consultare le voci di Wikipedia per: [Gear](https://en.wikipedia.org/wiki/Gear) e [Involute Gear](https://en.wikipedia.org/wiki/Involute_gear)

![](images/PartDesign_Involute_Gear_01.png ) 

## Utilizzo

1.  Andare nel menu {{MenuCommand|Part Design → <img src=images/PartDesign_InternalExternalGear.svg style="width:24px"> Involute gear...}}.
2.  Impostare i parametri dell\'evolvente
3.  Cliccare su **OK**.
4.  L\'evolvente dell\'ingranaggio viene creato al di fuori del corpo attivo. Trascinalo e rilascialo in un corpo per applicarvi ulteriori funzioni, come il riempimento.

## Parametri

-   Numero di denti: Impostare il numero di denti.

-   Modulo: Diametro diviso per il numero di denti.

-   Angolo di pressione: Angolo acuto tra la retta di pressione e la normale alla congiungente i centri degli ingranaggi. Di default è 20 gradi. ([Altre info](http://en.wikipedia.org/wiki/Involute_gear))

-   Alta precisione: True o False

-   External gear: True o false

## Correlazioni

-   [Ambiente FCGear](FCGear_Workbench/it.md)


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
