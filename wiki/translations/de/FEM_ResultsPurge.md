---
 GuiCommand:
   Name: FEM ResultsPurge
   Name/de: FEM ErgebnisseLöschen
   MenuLocation: Ergebnisse , Ergebnisse löschen
   Workbenches: FEM_Workbench/de
   Shortcut: **R** **P**
   SeeAlso: FEM_tutorial/de
---

# FEM ResultsPurge/de



## Beschreibung

**Ergebnisse löschen** löscht alle [Ergebnisobjekte](FEM_ResultShow/de.md) und alle Ergebnisnetze aus dem aktiven Analysecontainer in der [Baumansicht](Tree_view/de.md).


{{VersionPlus/de|1.1}}

: Löscht alle Ausgabeobjekte aller Gleichungslöser (CalculiX-Ergebnisse, Objekte, Pipelines, Filter und Textmeldungen).

Wenn nur das Ergebnisobjekt gelöscht werden soll, das Ergebnisnetz aber beibehalten werden soll, ist eine Kopie des Ergebnisnetzes zu erstellen, dann das Ergebnisobjekt in der Baumansicht auswählen und durch Drücken von **Del** löschen. Auf diese Weise bleibt die erstellte Kopie des Netzes erhalten. (Die Verwendung von FEM ResultsPurge würde die Kopie ebenfalls löschen).



## Anwendung

Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:

-   Die Schaltfläche **<img src="images/FEM_ResultsPurge.svg" width=16px> [Ergebnisse bereinigen](FEM_ResultsPurge/de.md)** drücken.
-   Den Menüeintrag **Ergebnisse → <img src="images/FEM_ResultsPurge.svg" width=16px> Ergebnisse bereinigen** auswählen.
-   Das Tastaturkürzel **R** dann **P**.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultsPurge/de
