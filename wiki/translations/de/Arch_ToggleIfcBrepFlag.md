---
 GuiCommand:
   Name: Arch ToggleIfcBrepFlag
   Name/de: Arch IfcBrepKennzeichnungUmschalten
   MenuLocation: Dienstprogramme , IFC-B-rep-Kennzeichnung Umschalten
   Workbenches: BIM_Workbench/de
   SeeAlso: Arch_IfcExplorer/de, Arch_IFC/de
---

# Arch ToggleIfcBrepFlag/de



## Beschreibung

Das Werkzeug **Arch IfcBrepKennzeichnungUmschalten** schaltet die IfcBrep-Markierung eines ausgewählten [BIM](BIM_Workbench.md)-Objekts an/aus (die Voreinstellung ist immer aus). Wenn die Markierung an ist, wird das Objekt beim Export nach IFC als [IfcFacetedBrep](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm)-Objekt exportiert, auch wenn eine übergeordnete Exportart wie IfcExtrudedAreaSolid oder IfcBooleanResult möglich ist. Obwohl IfcFacetedBrep-Objekte schwerer und weniger bearbeitbar sind (sie verlieren einige Geometrieinformationen wie z.B. die Modellierungshistorie), sind sie oft weniger fehleranfällig. Das Setzen dieser Markierung ermöglicht es, einige Fälle von Objekten zu lösen, die nicht korrekt exportiert werden, wenn die Markierung nicht gesetzt ist.



## Anwendung

1.  Ein Arch Objekt auswählen.
2.  Den Menüeintrag **Dienstprogramme → <img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> IFC-B-rep-Kennzeichnung Umschalten** auswählen.





{{BIM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > Arch ToggleIfcBrepFlag/de
