---
 GuiCommand:
   Name: Assembly CreateAssembly
   Name/de: Assembly BaugruppeErstellen
   MenuLocation: Assembly , Baugruppe erstellen
   Workbenches: Assembly_Workbench/de
   Shortcut: **A**
   Version: 1.0
   SeeAlso: 
---

# Assembly CreateAssembly/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Assembly_CreateAssembly.svg  style="width:24px;"> [Assembly BaugruppeErstellen](Assembly_CreateAssembly/de.md) erstellt eine Hauptbaugruppe (Assembly-Objekt) im aktuellen Dokument oder eine Unterbaugruppe in einer schon vorhandenen aktiven Baugruppe. Ein Dokument kann nur eine Hauptbaugruppe enthalten.

Jedes Assembly-Objekt wird standardmäßig mit einem [Ursprung](App_OriginGroupExtension/de.md) (Origin-Objekt) und einem leeren Behälter zur Aufnahme der Verbindungen (Joints container) erstellt.



## Anwendung

1.  Wenn das Dokument schon eine oder mehrere Baugruppen enthält: Eine Baugruppe aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/Assembly_CreateAssembly.svg" width=16px> [Baugruppe erstellen](Assembly_CreateAssembly/de.md)** drücken.
    -   Den Menüeintrag **Assembly → <img src="images/Assembly_CreateAssembly.svg" width=16px> Baugruppe erstellen** auswählen.
    -   Das Tastaturkürzel **A**.
3.  Ein neues Assembly-Objekt wird erstellt, entweder im Dokument oder in der aktivierten Baugruppe.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein **Assembly**-Objekt, oder formal ein {{Incode|Assembly::AssemblyObject}} besitzt die folgenden Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Type|String}}:

-    {{PropertyData/de|Material|Link}}:

-    {{PropertyData/de|Meta|Map|Hidden}}:

-    {{PropertyData/de|Id|String}}:

-    {{PropertyData/de|Uid|UUID|Hidden}}:

-    {{PropertyData/de|License|String}}:

-    {{PropertyData/de|License URL|String}}:

-    {{PropertyData/de|Color|Color}}:

-    {{PropertyData/de|Placement|Placement}}:

-    {{PropertyData/de|Label|String}}:

-    {{PropertyData/de|Label2|String|Hidden}}:

-    {{PropertyData/de|Expression Engine|ExpressionEngine|Hidden}}:

-    {{PropertyData/de|Visibility|Bool|Hidden}}:

-    {{PropertyData/de|Origin|Link|Hidden}}:

-    {{PropertyData/de|Group|LinkList}}:

-    {{PropertyData/de|_ Group Touched|Bool|Hidden}}:



### Ansicht


{{TitleProperty|Display Options}}

-    {{PropertyView/de|Display Mode|Enumeration}}: {{value|Group}} (bisher die einzige Option).

-    {{PropertyView/de|Show In Tree|Bool}}: Standardwert {{value|true}}.

-    {{PropertyView/de|Visibility|Bool}}: Standardwert {{value|true}}.


{{TitleProperty|Selection}}

-    {{PropertyView/de|On Top When Selected|Enumeration}}:

-    {{PropertyView/de|Selection Style|Enumeration}}:





{{Assembly_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Assembly](Assembly_Workbench.md) > Assembly CreateAssembly/de
