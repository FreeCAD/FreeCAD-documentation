# Tasks Placement/ro
## Descriere


<div class="mw-translate-fuzzy">

Comanda pentru a modifica **Placement**. Aceste opțiuni afectează numai poziția și orientarea obiectului în spațiu, ele nu afectează celelalte atribute ale formei. Plasarea este stocată intern sub formă de poziție și rotație (axa de rotație și unghiul transformat în quaternion.[1](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Deși există mai multe metode de specificare a unei rotații, de exemplu cu un centru de rotație, aceasta este utilizată doar pentru a calcula rotația și nu este stocată pentru operații ulterioare. Similar, dacă se specifică o axă de rotație de (1,1,1), aceasta poate fi normalizată atunci când este stocată în quaternion și apare ca (0.58, 0.58, 0.58) atunci când se navighează peste obiect mai târziu.


</div>

## Folosire


<div class="mw-translate-fuzzy">

Funcția **Placement** poate fi accesată în mai multe feluri:

-   via [script](Python_scripting_tutorial#Vecteurs_et_Positions.md) Python in the console and its [API](Placement_API.md).

![Scripting Placement as y/p/r and Matrix](images/PlacePyConv10.png )

-   sau, îm fereastra **Combo View → Properties → Data → Placement → **...****,

![Task_Placement](images/_Tache_Placement_fr_01.png )

-   sau prin meniul **Edit → Placement\...**.


</div>

### Activarea Placement în fereastra de afișare 


<div class="mw-translate-fuzzy">

-   Click pe o formă pentru a o selecta.
-   Click pe **Placement** (titlul, nu mica săgeată) și un buton cu trei puncte apare: ![ 256px \| Tache_Placement](images/_Tache_Placement_01_fr_00.png )
-   click pe acest buton, și este afișat **Placement Dialog** :


</div>


<div class="mw-translate-fuzzy">

![ left](images/_Tache_Placement_en_02.png )


</div>

### Options


{{TitleProperty|Translation}}


<div class="mw-translate-fuzzy">

### Opțiuni


{{TitleProperty | Translation:}}

-    {{TasksTag | X}}![ 150px \| Translation in X direction (Click to enlarge)](images/_Tache_Placement_Translation_X_fr.gif ) Moves the coordinate system of the object in the **X** direction in relation to the axis coordinates of origin 0, 0, 0.

-    {{TasksTag | Y}}![ 150px \| Translation in the Y direction (Click to enlarge)](images/_Tache_Placement_Translation_Y_fr.gif ) Moves the coordinate system of the object in the **Y** direction in relation to the axis coordinates of origin 0, 0, 0.

-    {{TasksTag | Z}}![ 150px \| Translation in the Z direction (Click to enlarge)](images/_Tache_Placement_Translation_Z_fr.gif )Mută sistemul de coordonate al obiectului în direcția **Z** față de axele de origine 0, 0, 0.


</div>


{{TitleProperty|Center}}


<div class="mw-translate-fuzzy">


{{TitleProperty | Center}}

-    {{TasksTag | X}}: Move the center of rotation in the direction **X**, from the coordinates of the selected object. (default: 0,0,0).

-    {{TasksTag | Y}}: Move the center of rotation in the direction **Y** from the coordinates of the selected object. (default: 0,0,0).

-    {{TasksTag | Z}}: Move the center of rotation in the direction **Z**, from the coordinates of the selected object. (default: 0,0,0).

-    {{TasksTag | User Defined ... }}: Allows you to change the three axes ( **X, Y, Z**) in a single operation ![ 96px \| User Defined](images/_Part_Revolve_fr_06.png ).


</div>


{{TitleProperty|Rotation}}


<div class="mw-translate-fuzzy">


{{TitleProperty | Rotation}}

Pentru a regla **rotation parameters** , avem două metode disponibile.


</div>


<div class="mw-translate-fuzzy">

-   Prima oțiune. Selectați **Rotation axis with angle**![ 256px \| Tache_Placement Option rotation axis and angle](images/_Tache_Placement_fr_05.png ) (Implicit).
    -   
        {{TasksTag | Axis: X}}
        
        : Rotație va fi pe axa **X**.

    -   
        {{TasksTag | Axis: Y}}
        
        : Rotația va fi pe axa **Y**.

    -   
        {{TasksTag | Axis: Z}}
        
        : Rotația va fi pe axa **Z**. (Axa implicită).

    -   
        {{TasksTag | Angle:}}
        
        Unghiul de rotație în grade de la **-360.00 °** la **360.00 °**. (Implicit: **0.00°**).


</div>


<div class="mw-translate-fuzzy">

-   A doua opțiune. Selectați **Euler Angles** ![ 256px \| Tache_Placement Option Euler angles](images/_Tache_Placement_fr_04.png ).


</div>


<div class="mw-translate-fuzzy">

Această opțiune poate fi mai ușor de utilizat, cu toate acestea, chiar și în acest mod, există lucruri importante de reținut: Rotațiile pozitive sunt în sensul **clockwise** , privind **din** origine de-a lungul axei pozitive. Sau pentru al pune în alt mod, rotațiile sunt pozitive în sensul **counterclockwise**, privind **spre** origine de-a lungul unei axe pozitive.


</div>


<div class="mw-translate-fuzzy">

  - **[Yaw](http://en.wikipedia.org/wiki/Flight_dynamics_%28fixed_wing_aircraft%29)** : este o mișcare de rotație orizontală a corpului în jurul axei Verticale. (Simbolul **ψ** este adesea utilizat pentru girație.)

  - **[Pitch](http://en.wikipedia.org/wiki/Flight_dynamics_%28fixed_wing_aircraft%29)** : este definit ca fiind o mișcare oscilatorie a navei înainte și înapoi.

  - **[Roll](http://en.wikipedia.org/wiki/Flight_dynamics_%28fixed_wing_aircraft%29)** : este o mișcare de rotație a unui corp în jurul axei sale longitudinale (axa de ruliu).


</div>


<div class="mw-translate-fuzzy">

Girația, tangajul și ruliu se referă la atitudinea unui obiect într-un spațiu 3D. Acești termeni sunt frecvent utilizați în aviație. The angles are the **Tait-Bryan angles.** If you want more information, try [Euler angles](http://en.wikipedia.org/wiki/Euler_angles).


</div>


<div class="mw-translate-fuzzy">

![ left \| Option Euler angles](images/_Tache_Placement_en_03.png ) 


</div>


<div class="mw-translate-fuzzy">

![ Left \| Yaw](images/_Tache_Placement_Lacet_fr_Mini.gif )

-    {{TasksTag | yaw axis}}**Girația este rotația față de axa Z**, adică o rație de la stanga la dreapta. (Unghiul de girație este **Psi ψ**). Valoarea fiind cuprinsă între **-360.00 °** și **360, 00 °**(Valorea Implicită este , **0.00 °**).


</div>


<div class="mw-translate-fuzzy">

![ Left \| Pitch](images/_Tache_Placement_Tangage_fr_Mini.gif )

-    {{TasksTag | pitch axis}}**Tangajul este rotația față de axa Y**, adică botul sus și botul jos. (Unghiul de tangaj este simbolizat prin **Phi φ**). Valoarea este cuprinsă între **-360.00 °** și **360, 00 °**(Valoarea Implicită este, **0.00 °**).


</div>


<div class="mw-translate-fuzzy">

![ Left \| Roll](images/_Tache_Placement_Roulis_fr_Mini.gif )

-    {{TasksTag | roll axis}}**Ruliu este rotația în jurul axei X**, ca și cum aripile oscilează când sus când jos. (Unghiul de ruliu este simbolizat prin **Thêta θ**). Valoarea este cuprinsă între**-360.00 °** și **360, 00 °**(Valoarea implicită este, **0.00 °**).


</div>


<div class="mw-translate-fuzzy">

-    {{TasksTag | Apply incremental changes to the placement of the object}}: Odată selectată, această opțiune **virtually** setează toți parametrii la zero, pentru a vă permite să introduceți valorile fără a fi nevoie să calculați parametrii formularului. După ce confirmați cu {{KEY | OK}}, valorile introduse vor fi adăugate la valorile din formular.


</div>


<div class="mw-translate-fuzzy">

-   Apăsarea tastei {{KEY | Reset}} aduce toate valorile la **0,0,0**.


</div>

## Legături și Exemple 


<div class="mw-translate-fuzzy">

Un exemplu practic de utilizare a acestei comenzi în tutorial [ Aeroplane](Aeroplane.md).


</div>


<div class="mw-translate-fuzzy">

Altă explicație este pe [Placement](Placement.md)


</div>



---
⏵ [documentation index](../README.md) > [Command_Reference](Category_Command_Reference.md) > Tasks Placement/ro
