# Scenegraph/ro
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

Geometria care apare în vizualizările 3D ale FreeCAD este redată de biblioteca Coin3D. Coin3D este o implementare satandard a [OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor).Software-ul openCascade oferă, de asemenea, aceeași funcționalitate, dar s-a hotărât, încă de la începuturile FreeCAD, să nu se folosească de vizualizatorul openCascade încorporat ci mai degrabă să se treacă la software-ul coin3D mai performant. O modalitate bună de a învăța despre această bibliotecă este cartea [Open Inventor Mentor](http://www-evasion.imag.fr/Membres/Francois.Faure/doc/inventorMentor/sgi_html/).


</div>

## Description


<div class="mw-translate-fuzzy">

[OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor) este de fapt un limbaj de descriere a scenei 3D. Scena descrisă în openInventor este apoi redată în OpenGL pe ecran. Coin3D are grijă să facă acest lucru, astfel încât programatorul nu are nevoie să se ocupe de apelurile complexe openGL, ci doar să-l furnizeze cu un cod OpenInventor valabil. Marele avantaj este că OpenInventor este un standard foarte bine cunoscut și bine documentat.


</div>


<div class="mw-translate-fuzzy">

Una din marile servicii pe care FreeCAD le face pentru dvs. este de a traduce în mod deschis informația geometriei OpenCascade în limbajul openInventor.


</div>


<div class="mw-translate-fuzzy">

OpenInventor descrie o scenă 3D sub formă de a[scenegraph](http://en.wikipedia.org/wiki/Scene_graph), like the one below:


</div>

![](images/Scenegraph.gif )


<div class="mw-translate-fuzzy">

![](images/Scenegraph.gif ) image from [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html)


</div>


<div class="mw-translate-fuzzy">

Un scenograf openInventor descrie tot ce face parte dintr-o scenă 3D, cum ar fi geometria, culorile, materialele, luminile etc., și organizează toate datele într-o structură convenabilă și clară. Totul poate fi grupat în sub-structuri, permițându-vă să vă organizați conținutul scenei cât de mult vă place. Iată un exemplu de fișier openInventor:


</div>


{{Code|lang=bash|code=
#Inventor V2.0 ascii
 
Separator { 
    RotationXYZ {   
       axis Z
       angle 0
    }
    Transform {
       translation 0 0 0.5
    }
    Separator { 
       Material {
          diffuseColor 0.05 0.05 0.05
       }
       Transform {
          rotation 1 0 0 1.5708
          scaleFactor 0.2 0.5 0.2
       }
       Cylinder {
       }
    }
}
}}


<div class="mw-translate-fuzzy">

După cum puteți vedea, structura este foarte simplă. Utilizați separatoare pentru a vă organiza datele în blocuri, un pic asemănător cu modul cum ați organiza fișierele în foldere. Fiecare afirmație afectează ce urmează, de exemplu primele două elemente ale separatorului rădăcină sunt o rotație și o translație, ambele afectează următorul element, care este un separator. În acest separator se definește un material și o altă transformare. Cilindrul nostru va fi astfel afectat de ambele transformări, cel care a fost aplicat direct la acesta și cel aplicat separatorului părinte.


</div>


<div class="mw-translate-fuzzy">

De asemenea, avem multe alte tipuri de elemente pentru organizarea scenei noastre, cum ar fi grupuri, switch-uri sau adnotări. Putem defini materiale foarte complexe pentru obiectele noastre, cu culori, texturi, moduri de umbrire și transparență. De asemenea, putem defini lumini, camere de luat vederi și chiar mișcări. Este posibil chiar să încorporați fragmente de script-uri în fișierele openInventor, pentru a defini comportamente mai complexe.


</div>


<div class="mw-translate-fuzzy">

Dacă sunteți interesat să aflați mai multe despre openInventor, mergeți direct la cele mai faimoase referințe ale sale [Inventor mentor](http://www-evasion.imag.fr/~Francois.Faure/doc/inventorMentor/sgi_html/index.html).


</div>


<div class="mw-translate-fuzzy">

În FreeCAD, în mod normal, nu trebuie să interacționăm direct cu scenograful openInventor. Fiecare obiect dintr-un document FreeCAD, fiind o plasă, o formă a unei piese sau orice altceva, devine automat convertit în codul openInventor și inserat în descrierea grafică a scenei principală pe care îl vedeți într-o vizualizare 3D. Această descriere grafică este actualizat continuu când faceți modificări, adăugați sau eliminați obiecte în document. De fapt, fiecare obiect (în spațiul App) are un furnizor de vizualizare (un obiect corespunzător în spațiul Gui), responsabil pentru emiterea codului openInventor.


</div>


<div class="mw-translate-fuzzy">

Dar există multe avantaje pentru a putea accesa scenegraful direct. De exemplu, putem schimba temporar aspectul unui obiect sau putem adăuga obiecte în scenă care nu au o existență reală în documentul FreeCAD, cum ar fi geometria construcției, ajutoarele, sugestii grafice sau unelte cum ar fi manipulatorii sau informații pe ecran .


</div>

FreeCAD dispune de mai multe instrumente pentru a vedea sau a modifica codul openInventor. De exemplu, următorul cod python va afișa reprezentarea openInventor a unui obiect selectat:


```python
obj = FreeCAD.ActiveDocument.ActiveObject
viewprovider = obj.ViewObject
print viewprovider.toString()

```


<div class="mw-translate-fuzzy">

Dar avem, de asemenea, un modul python care permite accesul complet la tot ceea ce gestionează Coin3D, cum ar fi descrierea grafică a scenei FreeCAD. Deci, citiți mai departe [Pivy](Pivy.md).


</div>

## Coding examples 

See [Coin3d snippets](Coin3d_snippets.md) courtesy of MariwanJ\'s research for the [Design456 Workbench](Design456_Workbench.md). The code repository of said examples can be found at <https://github.com/MariwanJ/COIN3D_Examples>. {{Top}}


<div class="mw-translate-fuzzy">


{{docnav/ro|Mesh to Part/ro|Pivy/ro}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Scenegraph/ro
