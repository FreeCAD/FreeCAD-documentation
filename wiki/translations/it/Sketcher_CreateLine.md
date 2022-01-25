---
- GuiCommand:/it
   Name:Sketcher CreateLine
   Name/it:Linea
   Workbenches:[Sketcher](Sketcher_Workbench/it.md)
   MenuLocation:Sketch → Geometrie → Linea
   Shortcut:L
   SeeAlso:[Polilinea](Sketcher_CreatePolyline/it.md)
---

# Sketcher CreateLine/it


</div>

## Descrizione

Disegna una segmento tra due punti selezionati nella vista 3D. Quando lo strumento è attivo, il puntatore del mouse assume la forma di croce bianca con l\'icona linea rossa.

Accanto al puntatore sono visualizzate, in blu, le coordinate della sua posizione, aggiornate in tempo reale.

![](images/Sketcher_LineExample1.png‎ )


<div class="mw-translate-fuzzy">

L\'oggetto linea creato inizia e finisce nei punti specificati, ma rispetto ai vincoli [Tangente](Sketcher_ConstrainTangent/it.md), [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) e [Angolo](Sketcher_ConstrainAngle/it.md) la linea è infinita. Ciò significa ad esempio che un punto con il vincolo [Punto su oggetto](Sketcher_ConstrainPointOnObject/it.md) può non essere posizionato tra i due punti dati ma può trovarsi al di fuori dei due punti sull\'estensione della linea disegnata.


</div>

## Utilizzo

-   Selezionare i punti su un\'area vuota della vista 3D, o su un oggetto esistente. I vincoli automatici (auto constraints) si attivano nella scheda **Azioni → Modifica controlli → Autovincoli** del pannello **Vista combinata**.
-   Premere il tasto {{KEY/it|Esc}}, o cliccare sul tasto destro del mouse, per annullare l\'operazione.


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/it
