---
- GuiCommand:/de
   Name:Part Revolve
   Name/de:Part Drehen
   MenuLocation:Formteil → Drehen
   Workbenches:[Part](Part_Workbench/de.md)
   SeeAlso:
---


</div>


<div class="mw-translate-fuzzy">

## Beschreibung

Dreht das ausgewählte Objekt um eine gegebene Achse. Die folgenden Formtypen sind erlaubt und führen zu den angegebenen Ausgabeformen ([Siehe Hinweise für Ausnahmen](#Notes.md)):


</div>

  Eingabeform   Ausgabeform
  ------------- ----------------------------------
  Knoten        Kante
  Kante         Fläche
  Draht         Hülle
  Fläche        Volumenkörper
  Hülle         Volumenkörperverbund (Compsolid)


<div class="mw-translate-fuzzy">

Volumenkörper oder CompSolids sind nicht als Eingabeform zulässig. Normale Verbünde sind derzeit ebenfalls nicht zulässig. Zukünftige Versionen werden den tatsächlichen Formtyp von Verbundobjekten prüfen.


</div>

![](images/Dialog-revolve.png )


<div class="mw-translate-fuzzy">

Das Winkelargument gibt an, wie weit das Objekt gedreht werden soll. Die Koordinaten verschieben den Ursprung der Rotationsachse relativ zum Urspung des Koordinatensystems.


</div>


<div class="mw-translate-fuzzy">

Wenn Du eine benutzerdefinierte Achse wählst, definieren die Zahlen die Richtung der Rotationsachse mit Bezug zum Koordinatensystem. Wenn die Z-Achse Null ist und die X- und Y-Koordinate nicht-Null sind, dann liegt die Achse in der X/Y-Ebene. Der Winkel ist der Tangens(?)/die Tangente des Verhältnisses der angegebenen X- und Y-Koordinaten.


</div>

### Anmerkungen

-   Wenn deine FreeCAD Version ein Kontrollkästchen für Volumenkörper im Dialogfeld Drehen hat, kannst du auch Volumenkörper aus geschlossenen Drähten und Kanten herstellen.
-   Wenn das Drehen mit einer Achse durchgeführt wird, die die zu drehende Fläche schneidet, und du einen Volumenkörper erzeugen möchtest, ist das Ergebnis möglicherweise ungültig. Dies kann aus verschiedenen Gründen geschehen, z.B. Selbstüberschneidung, Richtung usw.


<div class="mw-translate-fuzzy">





</div>


  
