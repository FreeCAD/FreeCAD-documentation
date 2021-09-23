---
- GuiCommand:/it
   Name:Sketcher ToggleConstraint   Name/it:Vincoli guida o definitivi
   Workbenches:[Sketcher](Sketcher_Workbench/it.md), [PartDesign](PartDesign_Workbench/it.md)
   MenuLocation:Sketch → Vincoli → Vincoli guida o definitivi
   SeeAlso:[Geometrie di costruzione](Sketcher_ToggleConstruction/it.md)
   Version:0.16
---

# Sketcher ToggleDrivingConstraint/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Lo strumento <img alt="" src=images/Sketcher_ToggleConstraint.svg  style="width:24px;"> **Toggle Constraint** commuta i vincoli dimensionali (blocco, distanza orizzontale o verticale, lunghezza, raggio e angolo) in modalità di riferimento e viceversa. Le icone nella barra degli strumenti diventano blu e, al posto dei vincoli dimensionali, vengono create delle quote di riferimento. Le quote di riferimento non vincolano lo schizzo. Può essere utile creare quote di riferimento in uno schizzo come modo per verificare le misurazioni; quando gli viene assegnato un nome, possono essere utilizzate anche per guidare i vincoli in un altro schizzo attraverso le [espressioni](Expressions/it.md).


</div>

![](images/Sketcher_Constraint_Toolbar_ReferenceMode.png ) *La barra degli strumenti Vincolo di Sketcher con i vincoli dimensionali nella modalità quote di riferimento (blu).*

![](images/Sketcher_ToggleConstraint_example.png ) *Per definire il profilo sono stati impostati un vincolo di distanza orizzontale (50 mm), un vincolo verticale (30 mm) e un vincolo di angolo (75°); poi al segmento inclinato è stata aggiunta una quota di riferimento per conoscerne la sua lunghezza (31,0583 mm).*

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src=images/Sketcher_ToggleConstraint.svg style="width:24px"> '''Vincoli guida o definitivi'''**. Le icone di vincoli dimensionali nella barra degli strumenti Vincoli di Sketcher passano da rosso a blu.
2.  Funziona come la creazione di vincoli dimensionali, sempre nello stesso modo, ma ora viene invece aggiunta una quota di riferimento di colore blu.
3.  Per riportare la barra degli strumenti Vincoli dello Sketcher alla modalità vincolo (rosso), premere nuovamente il pulsante Vincoli guida o definitivi.
4.  Per trasformare un vincolo dimensionale in una quota di riferimento, o il contrario, selezionarlo e premere il pulsante Vincoli guida o definitivi.


</div>


<div class="mw-translate-fuzzy">





</div>


{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ToggleDrivingConstraint/it
