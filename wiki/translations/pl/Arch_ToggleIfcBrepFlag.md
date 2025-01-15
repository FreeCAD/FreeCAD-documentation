---
 GuiCommand:
   Name: Arch ToggleIfcBrepFlag
   Name/pl: BIM: Przełącz flagę Brep IFC
   MenuLocation: Narzędzia , Przełącz flagę Brep IFC
   Workbenches: BIM_Workbench/pl
   SeeAlso: Arch_IfcExplorer/pl, Arch_IFC/pl
---

# Arch ToggleIfcBrepFlag/pl



## Opis

Narzędzie **Przełącz flagę Brep IFC** włącza / wyłącza flagę IfcBrep wybranego obiektu [BIM](BIM_Workbench/pl.md) *(domyślnie jest ona zawsze wyłączona)*. Jeśli flaga jest włączona, podczas eksportu do IFC obiekt zostanie wyeksportowany jako obiekt [IfcFacetedBrep](http://www.buildingsmart-tech.org/ifc/IFC4/final/html/schema/ifcgeometricmodelresource/lexical/ifcfacetedbrep.htm), nawet jeśli możliwy jest eksport wyższego poziomu, taki jak IfcExtrudedAreaSolid lub IfcBooleanResult. Chociaż obiekty IfcFacetedBrep są cięższe i mniej edytowalne (tracą niektóre informacje o geometrii, takie jak historia modelowania), często są mniej podatne na błędy. Ustawienie tej flagi pozwala rozwiązać niektóre przypadki obiektów, które nie są eksportowane poprawnie, gdy flaga nie jest ustawiona.



## Użycie

1.  Wybierz obiekt Architektury.
2.  Wybierz przycisk z menu **Narzędzia → <img src="images/Arch_ToggleIfcBrepFlag.svg" width=16px> Przełącz flagę Brep IFC**.



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch ToggleIfcBrepFlag/pl
