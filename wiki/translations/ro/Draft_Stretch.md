---
- GuiCommand:
   Name:Draft Stretch
   Name/ro:Draft Stretch
   MenuLocation:Draft → Stretch
   Workbenches:[Draft](Draft_Workbench/ro.md), [Arch](Arch_Workbench/ro.md)
   Shortcut:**S** **H**
   SeeAlso:[Draft Offset](Draft_Offset/ro.md)
---

# Draft Stretch/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument permite întinderea unui obiect prin mutarea unora dintre vârfurile acestuia.


</div>

<img alt="" src=images/Draft_Stretch_Example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

![](images/Draft_Stretch_Example.jpg )


</div>

## Usage

See also: [Draft Snap](Draft_Snap.md) and [Draft Constrain](Draft_Constrain.md).


<div class="mw-translate-fuzzy">

## Cum se utilizează 

1.  Selectați obiectele pe care doriți să le întindeți
2.  Apăsați tasta **<img src="images/Draft_Stretch.png" width=16px> [[Draft Stretch]]
**
3.  Alegeți primul colț al unui dreptunghi de selecție
4.  Alegeți colțul opus al dreptunghiului de selecție. Vitezele selectate sunt evidențiate
5.  Alegeți primul punct al deplasării pe care doriți să o dați acestor vârfuri
6.  Alegeți punctul final al deplasării


</div>

## Options

The single character keyboard shortcuts mentioned here can be changed. See [Draft Preferences](Draft_Preferences.md).


<div class="mw-translate-fuzzy">

## Opțiuni

-   Dacă nu este selectat niciun obiect la pornirea comenzii, veți fi invitat să alegeți unul. Dar pentru a lucra pe mai multe obiecte, trebuie să le selectați înainte de a porni comanda.
-   Până în prezent, numai obiectele [Draft Wire](Draft_Wire.md), [Draft Line](Draft_Line.md), [Draft BSpline](Draft_BSpline.md), [Draft BezCurve](Draft_BezCurve.md) și [Draft Rectangle](Draft_Rectangle.md) obiecte vor fi supuse la întindere. Toate celelalte obiecte vor avea punctul lor de origine mutat dacă se află în interiorul dreptunghiului de selecție.


</div>

## Preferences

See also: [Preferences Editor](Preferences_Editor.md) and [Draft Preferences](Draft_Preferences.md).

-   To change the number of decimals used for the input of coordinates: **Edit → Preferences... → General → Units → Units settings → Number of decimals**.

## Scripting


<div class="mw-translate-fuzzy">

## Script

Instrumentul Stretch nu are nicio funcție directă de tip python deoarece tot ceea ce face este să modifice proprietățile obiectelor selectate, cum ar fi proprietățile de plasare sau puncte ale obiectelor de proiect. Privind la ieșirea python atunci când utilizați instrumentul stretch, este ușor să reproduceți lucrul manual.


</div>

There is no Python method to stretch objects. To emulate the results of the Draft Stretch command geometric properties of objects have to be modified.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft Stretch/ro
