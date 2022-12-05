---
- GuiCommand:/it
   Name:Ship New
   Name/it:Nuova‏‎
   MenuLocation:Ship design → Crea una nuova nave
   Workbenches:[Ship](Ship_Workbench/it.md)
   Shortcut:
   SeeAlso:
---

# Ship CreateShip/it


</div>

## Introduzione

Da fare

Create a New Ship or new Ship Instance.

Ship works over **Ship entities**, that must be created on top of provided geometry. Geometry must be a solid, or set of solids.The following criteria must be taken into account:

-   All hull geometry must be provided (including symmetric bodies).
-   Starboard geometry must be included at negatives *y* domain.
-   Origin (0,0,0) point is the **Midship section** (Midpoint between after and forward perpendicular) and **base line** intersection.

![](images/FreeCAD-Ship-SignCriteria.jpg ) 
*Ship sign criteria*

## Usage

In order to create a **Ship instance** (in other words, a New Ship), select the hull solid geometry and invoke **Ship design → <img src="images/Ship_CreateShip.svg" width=16px> Create a new ship**.

Appare il dialogo per la Creazione della barca e nella vista 3D viene mostrata la sua sagoma con alcune annotazioni. Non preoccupatevi delle annotazioni perché vengono rimosse quando si chiude lo strumento di creazione della nave.

Devono essere introdotti i dati principali della nave (FreeCAD-Ship utilizza un sistema di introduzione dei dati progressivo, in questo modo le operazioni di base possono essere eseguite utilizzando i dati di base della nave, e le ulteriori informazioni sono necessarie solo quando le operazioni diventano più complesse).

## Ship data 

### Dati della nave 

Le dimensioni principali che devono essere introdotte qui:

-   *Length*: lunghezza tra le perpendicolari, 25,5 m per questo scafo.
-   *Beam*: baglio, larghezza massima della barca, 3,389 m per questo scafo.
-   *Draft*: immersione, 1,0 m per questo scafo.

![](images/FreeCAD-Ship-S60ShipCreationFront.png ) ![Front view annotations](images/FreeCAD-Ship-S60ShipCreationFront.png )


<center>

Annotazioni di lunghezza nella vista frontale.


</center>

La distanza tra le perpendicolari dipende dall\'immersione, quindi se non si conosce la lunghezza tra le perpendicolari è possibile impostare l\'immersione e regolare la lunghezza in modo da ottenere l\'intersezione del dritto o ruota di prua (linea superiore della prua) con la [linea di galleggiamento](http://it.wikipedia.org/wiki/Linea_di_galleggiamento).

![](images/FreeCAD-Ship-S60ShipCreationSide.png ) ![Side view annotations](images/FreeCAD-Ship-S60ShipCreationSide.png )


<center>

Annotazioni sulla vista laterale.


</center>

Lo stesso procedimento è valido per il baglio. Si noti che viene richiesto il valore del [baglio maestro](http://it.wikipedia.org/wiki/Baglio_%28nautica%29) (larghezza massima) , ma l\'annotazione si riferisce solo alla metà di dritta della barca.

Quando si preme il pulsante **OK**, il programma crea la nuova istanza barca, questa nuova istanza è denominata **Ship** nell\'albero *Etichette e Attributi*. Ora la geometria originale non è più necessaria, quindi è possibile nasconderla.

## Tutorial

-   [/it\|Tutorial Ship s60, prima parte ](FreeCAD-Ship_s60_tutorial.md)
-   [Tutorial Ship s60, seconda parte](FreeCAD-Ship_s60_tutorial_(II)/it.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Ship](Category_Ship.md) > Ship CreateShip/it
