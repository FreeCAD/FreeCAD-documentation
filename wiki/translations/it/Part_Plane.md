# Part Plane/it
---
- GuiCommand:/it   Name:Part CreatePrimitives   Name/it:Primitive   Workbenches:[MenuLocation:Part → [[Part_CreatePrimitives/it|Crea primitive...](Part_Workbench/it___Part]].md) → Piano|
Shortcut=Nessuno   SeeAlso:[ Cono](Part_Cone/it_.md),[Cilindro](Part_Cylinder/it_.md),[ Sfera](Part_Sphere/it_.md),[ Toro](Part_Torus/it_.md), [ Crea primitive...](Part_CreatePrimitives/it_.md)---


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Crea un semplice Piano parametrico di 10 x 10 mm, con i parametri di [posizionamento](Tasks_Placement/it.md), lunghezza e larghezza.

Di default, il piano viene posizionato in corrispondenza dell\'origine (punto 0,0,0).


</div>

![](images/PartPlane.png )

## Utilizzo


<div class="mw-translate-fuzzy">

Il piano standard viene creato con l\'angolo inferiore sinistro nel punto di origine 0,0,0.
Per modificare questi parametri aprire la sezione **Posizione** e inserire i valori desiderati nei rispettivi campi di input, oppure cliccare su **Vista 3D** e selezionare un punto, le coordinate del punto vengono acquisite dai campi.
Nel menu **Direzione** si può inoltre definire un vettore standard (X,Y o Z) normale al piano, oppure cliccare su {{KEY/it|Definito dall'utente...}} per aprire il dialogo che consente di impostare un diverso vettore (ad esempio la direzione 1,0,-1 crea un piano inclinato di 45° rispetto a X e Z).


</div>


<div class="mw-translate-fuzzy">

Le proprietà possono essere modificate successivamente in **Vista combinata → Dati**, dopo aver selezionato l\'oggetto.


</div>

## Properties

### Data


{{TitleProperty|Base}}

-    **Label**: String name of the object, defaults to \'Plane\'. User may rename it.

-    **Placement**: Placement of feature is defined by below angle, axis and position.

-    **Angle**: Angle of rotation relative to the below axis.

-    **Axis**: Defines the axis of rotation plane: X, Y, or Z. Defaults to Z axis, Z = 1

-    **Position**: Position X, Y, Z, relative to the origin 0, 0, 0.


{{TitleProperty|Plane}}

-    **Length**: Length is the dimension along the X axis The default value is 10 mm

-    **Width**: Width is the size of the Y-axis The default value is 10 mm

### View

You have the standard properties view.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Plane/it
