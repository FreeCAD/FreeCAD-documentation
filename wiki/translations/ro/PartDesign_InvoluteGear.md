---
- GuiCommand:/ro
   Icon:PartDesign InternalExternalGear.svg
   Name:PartDesign InvoluteGear
   Name/ro:PartDesign: Angrenaj cilindric cu dinți drepți în evolventă
   MenuLocation:Part Design → Involute gear...
   Workbenches:[PartDesign](PartDesign_Workbench.md)
---


</div>


<div class="mw-translate-fuzzy">

## Descriere

Acest instrument vă permite să creați un profil 2D al unei roți dințate în evolventă. Acest profil 2D este complet parametric și poate fi extrudat cu funcția [PartDesign Pad](PartDesign_Pad.md).

Pentru a face un profil elicoidală, acesta trebuie extrudat cu ajutorul instrumentului Sweep folosind o elice ca traiectorie


</div>

![](images/PartDesign_Involute_Gear_01.png ) 


<div class="mw-translate-fuzzy">

## Cum se folosește {#cum_se_folosește}

1.  Go to the **Part Design → <img alt="" src=images/PartDesign_InvoluteGear.png  style="width:16px;"> Involute gear\...** menu.
2.  Set the Involute parameters.
3.  Click OK.
4.  Profilul în evolventă este creat în afara corpului activ. Trageți-l și plasați-l într-un corp pentru a aplica alte funcții, cum ar fi extrudarea.


</div>

## Parametrii

-   Număr de dinți: Definește numărul de dinți.


<div class="mw-translate-fuzzy">

-   Modulul:

Diametrul primitiv împărțit la numărul de dinți. Sau: Modulul X Numărul de dinți = Diametrul Primitiv (acestea sunt diametrele tangente într-o pereche de roți).

Acestea depind de distanța centrală a arborilor suport și de raportul de reducere a vitezei dintre cei doi arbori.


</div>


<div class="mw-translate-fuzzy">

-   Unghiul de presiune: Unghiul ascuțit între linia de acțiune (tracțiune) și o linie normală la linia care leagă centrele de angrenaje (tangentă la cercurile primitive).

Valoarea implicită este de 20 de grade. ([More info](http://en.wikipedia.org/wiki/Involute_gear))


</div>


<div class="mw-translate-fuzzy">

-   Precizie ridicată: True or false


</div>


<div class="mw-translate-fuzzy">

-   Angrenaj Extern: True or false


</div>

## Related

-   [FCGear Workbench](FCGear_Workbench.md)


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}} 
