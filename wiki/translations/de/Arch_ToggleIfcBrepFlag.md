---
- GuiCommand   */de
   Name   *Arch ToggleIfcBrepFlag
   Name/de   *Arch UmschaltenIfcBrepMarkierung
   Workbenches   *[Arch](Arch_Workbench/de.md)
   MenuLocation   *Arch → Dienstprogramme → Umschalten Ifc Brep Markierung
   SeeAlso   *[Arch IfcExplorer](Arch_IfcExplorer/de.md), [Arch IFC](Arch_IFC/de.md)
---

# Arch ToggleIfcBrepFlag/de

## Beschreibung

Dieses Werkzeug schaltet die IfcBrep-Markierung eines ausgewählten [Arch](Arch_Workbench/de.md)-Objekts an/aus (die Voreinstellung ist immer aus). Wenn die Markierung an ist, wird das Objekt beim Export nach IFC als [IfcFacetedBrep](http   *//www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm) Objekt exportiert, auch wenn eine übergeordnete Exportart wie IfcExtrudedAreaSolid oder IfcBooleanResult möglich ist. Obwohl IfcFacetedBrep-Objekte schwerer und weniger bearbeitbar sind (sie verlieren einige Geometrieinformationen wie z.B. die Modellierungshistorie), sind sie oft weniger fehleranfällig. Das Setzen dieser Markierung ermöglicht es, einige Fälle von Objekten zu lösen, die nicht korrekt exportiert werden, wenn die Markierung nicht gesetzt ist.

## Anwendung

1.  Wähle ein Arch Objekt aus.
2.  Wähle die **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px>** Schaltfläche oder **Arch** → **Utilities** → **<img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> [Umschalten IfcBrepMarkierung](Arch_ToggleIfcBrepFlag.md)** aus dem oberen Menü.


<div class="mw-translate-fuzzy">





</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/de
