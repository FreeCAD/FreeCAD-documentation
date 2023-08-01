---
- GuiCommand:/de
   Name:Assembly3 CreateAssembly
   Name/de:Assembly3 BaugruppeAnlegen
   Icon:Assembly_New_Assembly.svg
   MenuLocation:Assembly3 → Create assembly
   Workbenches:[Assembly3](Assembly3_Workbench/de.md)
   Shortcut:**A** **N**
---

# Assembly3 CreateAssembly/de

## Beschreibung

Der Befehl **Assembly3 Baugruppe anlegen** fügt dem Konstruktionsbaum ein neues **Assembly**-Astobjekt hinzu.

Jedes Astobjekt ist ein <img alt="" src=images/Assembly_Assembly_Tree.svg  style="width:24px;"> **Assembly** -Container und enthält vier Gruppencontainer:

:   \- Einen für die <img alt="" src=images/Assembly_Assembly_Constraints_Tree.svg  style="width:24px;"> **Bedingungen** (welcher ausgeblendet ist, solange er leer ist)
:   \- Einen für die <img alt="" src=images/Assembly_Assembly_Element_Tree.svg  style="width:24px;"> 
**Elemente**
:   \- Einen für die <img alt="" src=images/Assembly_Assembly_Part_Tree.svg  style="width:24px;"> 
**Part-Objekte**
:   \- Einen für die <img alt="" src=images/Assembly_Assembly_Relation_Tree.svg  style="width:24px;"> **Beziehungen** (welcher standardmäßig ausgeblendet ist und der eingeblendet wird, sobald der Befehl <img alt="" src=images/Assembly_GotoRelation.svg  style="width:16px;"> [Zur Beziehung gehen](Assembly3_GoToRelation/de.md) verwendet wurde)

Das hinzugefügte **Assembly**-Objekt mit allen sichtbaren Containern sieht so aus (0.20.pre and Link Branch):

<img alt="" src=images/Assembly3_Example-Tree-07.png  style="width:190px;"> <img alt="" src=images/Assembly3_Example-Tree-08.png  style="width:190px;">

## Anwendung

1.  Durch drücken der Schaltfläche **<img src="images/Assembly_New_Assembly.svg‎‎" width=16px> [Baugruppe anlegen](Assembly3_CreateAssembly/de.md)** oder
    durch die Verwendung des Tastenkürzels **A** dann **N**, wird ein leerer Assembly-Container erzeugt



---
![](images/Button_right.svg) [documentation index](../README.md) > Assembly3 CreateAssembly/de
