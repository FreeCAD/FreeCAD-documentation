# Part Mirror/ro
---
 GuiCommand:   Name: Part Mirror   MenuLocation: Part -> Mirror   Workbenches: Part Workbench   Part|SeeAlso: 


</div>

## Description


<div class="mw-translate-fuzzy">

## Introducere

\'Mirror Object\' - Acest instrument creează un nou obiect (imagine) care este o refelctare a unui obiect original(sursa). Obiectul imagine este creat în spatele planului/suprafeței oglinzii. Planul oglinzii poate fi un plan standard (**XY**, **YZ**, or **XZ**), sau orice plan paralel la planele standarde.


</div>

Un exemplu:

![](images/PARTMirrorBeforev11.png )



*Before*

![](images/PARTMirrorAfterv11.png )



*After mirrored through YZ plane*



## Utilizare

![](images/PartMirroring_Scr1.png )


<div class="mw-translate-fuzzy">

Selectați obiectul sursă dion listă. Selectați un **Mirror plane** standard din dropbox. Apăsați **OK** pentru a crea obiectul imagine.


</div>

When the select button label says **Selecting** you are in reference selection mode and there is a selection gate in effect, which disallows the selection of unsupported reference objects. Click the button to toggle the selection gate off, the button label then changes to **Select reference**.

The mirror plane is defined by a **Normal** (direction) and a **Base** (position). When the **Mirror Plane** property contains a reference object these properties are made read-only as they are then computed based on that object. The plane is infinite even if the reference object is not.

A reference object can be a planar face, such as the face of a [Part Box](Part_Box.md), a circular edge, a [Datum Plane](PartDesign_Plane.md), an [origin plane](App_OriginGroupExtension.md) of a [Std Part](Std_Part.md) container, or any object with a single planar face or single circular edge. There is also support for [Links](App_Link.md). Note, however, that B-spline surfaces, such as [ruled surfaces](Part_RuledSurface.md) or [loft faces](Part_Loft.md) are not supported.

## Options


<div class="mw-translate-fuzzy">

## Opțiuni

Casetele **Base point** pot fi utilizate pentru a mișca planul oglinzii paralel cu planul oglinzii standard. Numia una dintre casetele **X**, **Y**, or **Z** este efectivă pentru planul satndard.


</div>


<div class="mw-translate-fuzzy">

  Standard Plane   Base Point Box   Effect
    
  **XY**           **Z**            Move mirror plane along **Z** axis.
  **XY**           **X**, **Y**     No effect.
  **XZ**           **Y**            Move mirror plane along **Y** axis.
  **XZ**           **X**, **Z**     No effect.
  **YZ**           **X**            Move mirror plane along **X** axis.
  **YZ**           **Y**, **Z**     No effect.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Limitări

-   Planurile de oglindă arbitrare (adică nu sunt paralele cu planul standard) nu sunt acceptate (începând de la versiunea FC 0.13).


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/ro
