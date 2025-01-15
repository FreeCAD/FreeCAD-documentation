# Vector API/it
**(Ottobre 2019) Non modificare queste pagine. Le informazioni sono incomplete e obsolete. Per l'API più recente, consultare la [https://www.freecadweb.org/api documentazione API autogenerata] o generare la documentazione autonomamente. Vedere [Documentazione del codice sorgente](Source_documentation/it.md).**

In FreeCAD i vettori sono utilizzati ovunque.

Esempio: 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


{{APIProperty|Length|restituisce la lunghezza del vettore.}}


{{APIFunction|add|Vector|aggiunge un altro vettore a questo.|vector}}


{{APIFunction|cross|Vector|il prodotto vettoriale tra questo vettore e un altro.|vector}}


{{APIFunction|distanceToLine|Vector1,Vector2|la distanza tra il vettore e una linea tra Vettore1 e Vettore2 attraverso Vettore1 e in direzione di Vettore2.|float}}


{{APIFunction|distanceToPoint|Vector|la distanza tra questo vettore e un altro.|float}}


{{APIFunction|distanceToLineSegment|Vector1,Vector2|un vettore dal punto più vicino su un segmento di linea da Vettore1 a Vettore2.|Vector}}


{{APIFunction|distanceToPlane|Vector1,Vector2|la distanza tra il vettore e un piano definito da un punto e una normale.|float}}


{{APIFunction|dot|Vector|il prodotto scalare tra due vettori.|float}}


{{APIFunction|getAngle|Vector|l'angolo in radianti tra due vettori.|float}}


{{APIFunction|isEqual|Vector2,tolleranza|Controlla se la distanza tra i punti rappresentati da questo Vettore e Vettore2 è inferiore o uguale alla tolleranza data.|True/False}}


{{APIFunction|isNormal|Vector2,tolleranza|Controlla se questo vettore è normale al vettore2 entro la tolleranza.|True/False}}


{{APIFunction|isOnLineSegment|Vector1,Vector2|Verifica se questo vettore si trova sul segmento di linea generato da Vettore1 e Vettore2.|Vector}}


{{APIFunction|isParallel|Vector2,tolleranza|Controlla se questo vettore è parallelo al vettore2 entro la tolleranza.|True/False}}


{{APIFunction|multiply|Float|moltiplica (con scala uniforme) un vettore per il fattore indicato.|nothing}}


{{APIFunction|negative|Vector|Restituisce il negativo (opposto) di questo vettore.|Vector}}


{{APIFunction|normalize| |normalizza un vettore (imposta la sua lunghezza a 1,0).|nothing}}


{{APIFunction|projectToLine|Vector1,Vector2|proietta il vettore su una linea attraverso Vettore1 in direzione Vettore2.|nothing}}


{{APIFunction|projectToPlane|Vector1,Vector2|pproietta il vettore su un piano definito da un punto (Vettore1) e una normale (Vettore2).|nothing}}


{{APIFunction|scale|Float,Float,Float|Come per moltiplicare, ma consente di specificare valori diversi per le direzioni x, y e z (scala non uniforme).|nothing}}


{{APIFunction|sub|Vector|sottrae un altro vettore da questo.|vector}}


{{APIProperty|x|la coordinata x di un vettore.}}


{{APIProperty|y|la coordinata y di un vettore.}}


{{APIProperty|z|la coordinata z di un vettore.}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Vector API/it
