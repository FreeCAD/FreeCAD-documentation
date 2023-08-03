---
 GuiCommand:
   Name: Part Revolve
   Name/de: Part Drehen
   MenuLocation: Formteil , Drehen
   Workbenches: Part_Workbench/de
---

# Part Revolve/de

## Beschreibung

Dreht das ausgewählte Objekt um eine gegebene Achse. Die folgenden Formtypen sind erlaubt und führen zu den angegebenen Ausgabeformen:

  Eingabeform   Ausgabeform
   
  Knoten        Kante
  Kante         Fläche
  Draht         Hülle
  Fläche        Volumenkörper
  Hülle         Volumenkörperverbund (Compsolid)

Eine [Skizze](Sketcher_Workbench/de.md) kann auch verwendet werden. Volumenkörper oder Verbundkörper sind nicht als Eingabeformen zulässig. Normale Verbünde sind derzeit ebenfalls nicht zulässig.

![](images/Dialog-revolve.png )

Das Winkelargument gibt an, wie weit das Objekt gedreht werden soll. Die Koordinaten verschieben den Ursprung der Rotationsachse relativ zum Urspung des Koordinatensystems.

Wenn Du eine benutzerdefinierte Achse wählst, definieren die Zahlen die Richtung der Rotationsachse mit Bezug zum Koordinatensystem. Wenn die Z-Achse Null ist und die X- und Y-Koordinate nicht-Null sind, dann liegt die Achse in der X/Y-Ebene. Der Tangens des Winkels ist das Verhältnis der angegebenen X- und Y-Koordinaten.

## Hinweise

-   [App-Link](App_Link/de.md)-Objekte, die mit geeigneten Objektarten verknüpft sind, können auch als Formen und zum Festlegen der Achse verwendet werden. <small>(v0.20)</small> 
-   Wenn das zu drehende Objekt die Drehachse schneidet, wird die Ausführung in den meisten Fällen scheitern.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/de
