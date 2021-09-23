# Path SetupSheet/it
{{TOCright}}

## Descrizione

L\'utilizzo di una Tabella delle impostazioni (SetupSheet) consente all\'utente di personalizzare il modo in cui sono calcolati i vari valori delle proprietà per le operazioni. L\'utente ha sempre la possibilità di sovrascrivere i valori del SetupSheet con un valore esplicito o modificare il modo in cui vengono calcolati i valori di SetupSheet.

Poiché i SetupSheet fanno parte di una Lavorazione Path, i valori non cambiano il comportamento predefinito di Path. Piuttosto, cambiano solo il comportamento all\'interno del contesto del lavoro corrente.

Le tabelle delle impostazioni sono particolarmente utili se salvate con un [Modello di lavorazione](Path_ExportTemplate/it.md).

## Proprietà

-    **VertRapid**: Imposta la velocità rapida verticale nei nuovi controller degli utensili. (Utilizzato nei post processori che supportano velocità rapide personalizzabili)

-    **HorizRapid**: Imposta la velocità rapida orizzontale nei nuovi controller degli utensili. (Utilizzato nei post processori che supportano velocità rapide personalizzabili)

-    **SafeHeightOffset**: L\'utilizzo di questo campo dipende da SafeHeightExpression (vedere sotto)

-    ** SafeHeightExpression**: Il risultato di questa espressione viene utilizzato per impostare l\'altezza di sicurezza delle operazioni.

-    **ClearanceHeightOffset**: L\'utilizzo di questo campo dipende da ClearanceHeightExpression (vedere sotto)

-    **ClearanceHeightExpression**: Il risultato di questa espressione viene utilizzato per impostare l\'altezza di sorvolo delle operazioni.

-    **StartDepthExpression**: Il risultato di questa espressione viene utilizzato per impostare la proprietà StartDepth delle operazioni.

-    ** FinalDepthExpression**: Il risultato di questa espressione viene utilizzato per impostare la proprietà FinalDepth delle operazioni.

-    **StepDownExpression**: Il risultato di questa espressione viene utilizzato per impostare la proprietà StepDown delle operazioni.


<div class="mw-translate-fuzzy">

1.  1.  Parametri dell\'operazione


</div>

The following are pulled from:

-   OpFinalDepth - The value of the FinalDepth property
-   OpStartDepth - The value of the FinalDepth property
-   OpToolDiameter - The value of the Tool Diameter property of the Tool Controller referenced by the operation.

## SetupSheet Values 

Other values in the SetupSheet can be referenced directly:

-   SetupSheet.ClearanceHeightOffset
-   SetupSheet.SafeHeightOffset

-   StartDepth
-   SafeHeightOffset
-   SafeHeightExpression
-   ClearanceHeightOffset
-   ClearanceHeightExpression
-   StartDepthExpression
-   FinalDepthExpression
-   StepDownExpression





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path SetupSheet/it
