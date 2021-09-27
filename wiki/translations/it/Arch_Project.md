---
- GuiCommand:/it
   Name:Arch Project
   Name/it:Progetto
   MenuLocation:Arch → Progetto
   Workbenches:[Arch](Arch_Workbench/it.md)
   Shortcut:**P** **O**
   SeeAlso:[Sito](Arch_Site/it.md), [Edificio](Arch_Building/it.md)
---

# Arch Project/it


</div>

## Descrizione


<div class="mw-translate-fuzzy">

Progetto di Arch è un oggetto speciale ch epermette di migliorare la compatibilità con i file [IFC](Arch_IFC/it.md). Ogni file IFC deve contenere un\'entità [IfcProject](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifckernel/lexical/ifcproject.htm). IfcProject viene utilizzato principalmente per definire le impostazioni generali del progetto come i sistemi di proiezione, la compatibilità GIS o i sistemi di unità di misura.


</div>

Quando si esporta un modello FreeCAD nel formato file IFC, se il modello non contiene alcun oggetto Project, ne viene automaticamente creato uno predefinito, che nella maggior parte dei casi è sufficiente. Tuttavia, si potrebbe voler mettere a punto le impostazioni del progetto, nel qual caso può essere utile aggiungere un oggetto Project. Quando si importa un file IFC, viene sempre creato un oggetto Project. Tuttavia, se non lo si usa, si può semplicemente eliminarlo dopo l\'importazione.


<div class="mw-translate-fuzzy">

Notare che, sebbene a un Progetto possa essere aggiunto qualsiasi altro oggetto BIM, cosa che lo standard IFC non proibisce, il modo comune di operare è quello di avere sempre solo dei [siti](Arch_Site/it.md) o degli [edifici](Arch_Building/it.md) come figli diretti di un progetto. Tutti gli altri oggetti BIM devono trovarsi all\'interno di questi siti o edifici. Il Progetto dovrebbe essere sempre nella parte superiore della struttura del modello, ovvero non dovrebbe essere incluso in nessun altro oggetto.


</div>

## Utilizzo


<div class="mw-translate-fuzzy">

1.  Premere il pulsante **<img src="images/Arch_Project.svg" width=16px> [Progetto](Arch_Project/it.md)**, o premere i tasti **P** e poi **O**.
2.  Aggiungere qualsiasi oggetto al progetto trascinandoli sul progetto nella vista ad albero.


</div>


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch Project/it
