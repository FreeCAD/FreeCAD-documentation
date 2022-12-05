---
- GuiCommand:/ro
   Name:Part Offset2D
   Name/ro:Part:Decalj 2D
   MenuLocation:Componentă → 2D Offset
   Workbenches:[Part](Part_Workbench/ro.md)
   Version:0.17
   SeeAlso:[Part Offset 3D](Part_Offset/ro.md), [Part Thickness](Part_Thickness/ro.md), [Draft Offset](Draft_Offset/ro.md)
---

# Part Offset2D/ro


</div>

## Description


<div class="mw-translate-fuzzy">

## Descriere

Part 2D Offset construiește un filament/contur, paralel cu firul original, la o anumită distanță de acesta. Sau mărește/micșorează o fațetă plană, în mod similar.


</div>

Filamentul/Fațete trebuie să fie în același plan.Pot exista mai multe filamente într-un singur obiect, nu neapărat coplanar.

![600px](images/Part_Offset2D_Demo.png)

## Usage


<div class="mw-translate-fuzzy">

## Cum se folosește 

1.  Selectați un obiect pentru decalaj/offset
2.  Apăsați butonul **[<img src=images/Part_Offset2D.svg style="width:24px">** **Offset2D**.
3.  Definiți offset în Task Panel.
4.  Apăsați **OK**.


</div>

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be used as source objects. <small>(v0.20)</small> 

## Probleme cunoscute 

-   Majoritatea modurilor non-implicite vor funcționa numai cu OCC 7.0.0 sau o versiune ulterioară.


<div class="mw-translate-fuzzy">

-   Utilizarea instrumentului poate provoca caderea FreeCAD (vezi punctul următor). Pe Windows, aceste accidente sunt convertite în excepții și, în general, nu determină închiderea FreeCAD; pe alte sisteme de operare nu este cazul. Deci, este recomandat să salvați proiectul înainte de a încerca să utilizați instrumentul.


</div>

-   Lărgirea fețelor cu găuri circulare cu o cantitate suficient de mare pentru a provoca gauri de închidere, apare un accident (OCC 7.0.0). Problema pare să fie specifică cercurilor; alte forme par să se închidă în mod corespunzător.


<div class="mw-translate-fuzzy">

-   când se compensează cercuri care au poziționare diferită de zero, rezultatul este plasat greșit. (OCC 7.0.0)


</div>


<div class="mw-translate-fuzzy">

-   când se compensează cercurile, uneori sunt compensate în direcție neașteptată (de exemplu spre interior în loc de exterior). (OCC 7.0.0)


</div>

-   Fill=\"true\" nu funcționează când compensați colectiv filamentele deschise în modul \"Skin\"

-   \"Tangent\" modul de conectare nu funcționează (OCC 7.0.0)

-   Filamentele decalajul/Offset din segmentul cu o singură linie nu sunt acceptate (deoarece segmentul de linie nu definește un plan). Segmentele de linie unice nu pot participa la decalajul/offset colectivă.

## Proprietăți

-    **Source**: Link to original shape


<div class="mw-translate-fuzzy">

-    **Value**The distance to enlarge the wire/face by. If negative, the wire/face is shrunk instead.


</div>

-    **Mode**(\"Pipe\" or \"Skin\"): sets how non-closed wires are processed. If \"Pipe\", the wire is outlined as if it was an extremely thin closed contour. If \"Skin\", an open wire is created.

:   ![600px](images/Part_Offset2D_Mode.png)

-    **Join**(\"Arc\", \"Tangent\", \"Intersection\"): sets the behavior around kinks. If \"Arc\", offset segments are connected with an arc of circle, centered at the vertex. \"Tangent\" is unsupported on OCC7.0.0. \"Intersection\": offset segments are extended till they intersect.

:   ![600px](images/Part_Offset2D_Join.png)

-    **Intersection**(\"false\", \"true\"): sets if multiple wires are treated collectively or independently. If \"false\", wires are offset independently, intersections between resulting wires are ignored. If \"true\", the wires are offset in collective manner.

:   ![600px](images/Part_Offset2D_Intersection.png)





:   Numai firele din cadrul unui compus sunt cuplate. De exemplu, dacă structura este asemănătoare compusului (wire1, wire2, compound (wire3, wire4)), wire1 și wire2 vor fi tratate colectiv, dar independent de wire3 și wire4. De asemenea, firele 3 și firele 4 sunt tratate colectiv, dar independent de fir1 + fir2.





:   De asemenea, în modul colectiv, direcțiile firelor sunt importante și influențează direcția de decalaj. Acest lucru este în strânsă legătură cu modul în care sunt tratate găurile în fațete.





:   Filamentele tratate colectiv trebuie să fie coplanare. Filamentele fiind decalate/offset independent nu trebuie să fie coplanare.

-    **Fill**(\"false\", \"true\"): dacă este \"true\", spațiul dintre filament/fațetă original(ă) și offset este umplut cu o fațetă.

:   ![600px](images/Part_Offset2D_Fill.png)

## Scrip-Programare 


<div class="mw-translate-fuzzy">

Instrumentul poate fi utilizat în [macros](macros.md) și din consola python utilizând următoarea funcție:


</div>


{{code|code=
f = App.ActiveDocument.addObject("Part::Offset2D", "Offset2D")
f.Source =  #some object
f.Value = 10.0
}}

2D offset este, de asemenea, disponibil ca o metodă de Part.Shape. Exemplu: {{code|code=
import Part
circle = Part.Circle().toShape()
enlarged_circle = circle.makeOffset2D(10.0)
Part.show(circle)
Part.show(enlarged_circle)
# makeOffset2D(offset, join = 0, fill = False, openResult = false, intersection = false)
# 
# * offset: distance to expand the shape by. 
# 
# * join: method of offsetting non-tangent joints. 0 = arcs, 1 = tangent, 2 =
# intersection
# 
# * fill: if true, the output is a face filling the space covered by offset. If
# false, the output is a wire/face.
# 
# * openResult: True for "Skin" mode; False for Pipe mode. 
# 
# * intersection: collective offset
# 
# Returns: result of offsetting (wire or face or compound of those). Compounding
# structure follows that of source shape.
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Offset2D/ro
