---
 GuiCommand:
   Name: Arch Pipe   Name/ro: Arch: Pipe/Țeavă
   MenuLocation: Arch , Pipe Tools , Pipe
   Workbenches: Arch_Workbench/ro
   Shortcut: **P** **I**
   Version: 0.17
   SeeAlso: Arch PipeConnector/ro, Arch Equipment/ro
---

# Arch Pipe/ro


</div>



## Descriere


<div class="mw-translate-fuzzy">


<small>(v0.17)</small> 

Acest instrument permite crearea de țevi/conducte de la zero, sau din obiectele selectate. Obiectele selectate trebui esă fie bzate pe Piese/Part-based (Draft, Sketch, etc..) și să conțină doar un filament deschis.


</div>




<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Optional, selectați o formă lineară [Part](Part_Workbench.md) ca de ex o [Draft Line](Draft_Line.md), un [Draft Wire](Draft_Wire.md) sau o [Sketch](Sketcher_NewSketch.md) deschisă
2.  Apăsați butonul **<img src="images/Arch_Pipe.png" width=16px> [Arch Pipe](Arch_Pipe.md)
**, sau apăsați în ordine tastele **P** apoi **I**


</div>



## Opțiuni


<div class="mw-translate-fuzzy">

-   Conductele partajează proprietățile și comportamentele comune tuturor [Arch Components](Arch_Component.md)


</div>



## Proprietăți

### Data


{{TitleProperty|Component}}

-    **Base|Link**: The base wire of this pipe, if any.

For the other properties in the group see [Arch Component](Arch_Component#Properties.md).


{{TitleProperty|Pipe}}


<div class="mw-translate-fuzzy">

-    **Length**: Setează lungimea acestei țevi,când nu se bazează pe un filament

-    **Diameter**: Diametrul acestei țevi, când nu se bazează pe un profil

-    **Base**: Filamentul de bază al acestei țevi, dacă există unul

-    **Profile**: Profilul de bază a acestei țevi. Dacă nu este specificat, țeava este cilindrică.


</div>



## Fluxul de lucru tipic 


<div class="mw-translate-fuzzy">

-   Începeți prin a plasa obiecte sanitare / hidraulice (mai jos este un fișier importat pas). Transformați aceste obiecte în Echipamente Arch, selectând-le și apăsând butonul [ Arbor Equipment](Arch_Equipment.md).


</div>

![](images/Arch_pipe_example_01.jpg )


<div class="mw-translate-fuzzy">

-   Echipamentele Arch au acum o proprietate nouă **SnapPoints**, care este o listă de vectori 3D. Acest lucru vă permite să adăugați puncte de fixare personalizate, pe care le puteți activa când noul buton [ Draft Special](Draft_Snap_Special.md) este activat. În prezent, această proprietate este disponibilă numai pentru Python. În cazul de mai sus am adăugat un nou punct de fixare la ieșirea aparatului de spălare. Vectorii din SnapPoints apar pe model ca puncte albe:


</div>

FreeCAD.ActiveDocument.Equipment.SnapPoints=[FreeCAD.Vector(0,0,100)]

![](images/Arch_pipe_example_02.jpg )


<div class="mw-translate-fuzzy">

-   Cu noul Snap Snap Special Snap Special, puteți acum să accesați aceste puncte personalizate:


</div>

![](images/Arch_pipe_example_03.jpg )

-   Acum, putem trage tuburile noastre folosind Linii de Proiectare, Proiectoare sau Schițe. Cea mai bună metodă, totuși, este utilizarea numai a liniilor de proiectare:

![](images/Arch_pipe_example_04.jpg )


<div class="mw-translate-fuzzy">

-   Acum există un nou instrument [Proiect Slope](Draft_Slope/ro.md) care permite modificarea pantei liniilor de proiectare, spre exemplu, 5% (0,05). Așadar, putem da rapid liniei noastre de deșeuri o pantă corectă. Numai coordonatele z sunt modificate de acest instrument, așa că trebuie doar să le înșurubăm unul în celălalt, proiecția de sus va rămâne neschimbată.


</div>

![](images/Arch_pipe_example_05.jpg )


<div class="mw-translate-fuzzy">

-   Trebuie doar să selectăm toate liniile noastre și să apăsăm butonul [Pipe Arch](Arch_Pipe.md). Arch Pipe funcționează cu orice obiect bazat pe componente care conține un singur fir deschis.


</div>

![](images/Arch_pipe_example_06.jpg )


<div class="mw-translate-fuzzy">

-   Acum putem crea conexiuni selectând 2 sau 3 tuburi coincidente și apăsați butonul [Arch PipeConnector](Arch_PipeConnector.md). Dacă sunt selectate 3 țevi, două dintre ele trebuie să fie aliniate pentru a crea un element (T):


</div>

![](images/Arch_pipe_example_07.jpg )

-   Schimbarea razei conectorilor nu modifică lungimea liniei de bază subiacente, numai tubul rezultat (prin schimbarea proprietății OffsetStart sau OffsetEnd). Deci, puteți să vă traseți linia doar cu linii drepte, fără a fi nevoie să vă îngrijiți de curbele și razele lor.

Este de asemenea posibil să se creeze Arch Pipes fără o linie de bază, în acest caz utilizați proprietatea \"Length\" pentru a defini lungimea sa.

## Scripting


<div class="mw-translate-fuzzy">

## Scrip-Programare 


</div>


<div class="mw-translate-fuzzy">

Instrumentul Pipe poate fi utilizat în [macros](macros.md) și de la consola python utilizând următoarele funcții:


</div>


```python
pipe = makePipe(baseobj=None, diameter=0, length=0, placement=None, name="Pipe")
```

-   Creates a `pipe` object from the given `baseobj` and `diameter`.
    -   
        `baseobj`
        
        is a [Draft Line](Draft_Line.md) or [Draft Wire](Draft_Wire.md).

    -   If `baseobj` is omitted, a straight pipe can be created with just the `diameter` and the `length` in the Z direction.
-   If a `placement` is given, it is used.


```python
import Draft, Arch

p1 = FreeCAD.Vector(1000, 0, 0)
p2 = FreeCAD.Vector(2500, 200, 0)
p3 = FreeCAD.Vector(3100, 1000, 0)
p4 = FreeCAD.Vector(3500, 500, 0)
line = Draft.make_wire([p1, p2, p3, p4])

pipe = Arch.makePipe(line, 200)
FreeCAD.ActiveDocument.recompute()

pipe2 = Arch.makePipe(diameter=120, length=3000)
FreeCAD.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">


{{docnav/ro|[Arch CompPipe](Arch_CompPipe.md)|[Pipe Connector](Arch_PipeConnector.md)|[Arch](Arch_Workbench.md)|IconL=Arch_CompPipe.png |IconC=Workbench_Arch.svg |IconR=Arch_PipeConnector.svg}}


</div>



---
⏵ [documentation index](../README.md) > [BIM](Category_BIM.md) > Arch Pipe/ro
