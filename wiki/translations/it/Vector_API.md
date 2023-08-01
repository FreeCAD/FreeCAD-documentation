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


{{APIFunction|add|Vector|aggiunge un altro vettore a questo | vettore.}}


{{APIFunction|cross|Vector| |il prodotto vettoriale tra questo vettore e u altro|vettore.}}


{{APIFunction|distanceToLine|Vector1,Vector2| |la distanza tra il vettore e una linea tra Vettore1 e Vettore2 attraverso Vettore1 e in direzione di Vettore2|float.}}


{{APIFunction|distanceToLineSegment|Vector1,Vector2|un vettore dal punto più vicino su un segmento di linea da Vettore1 a Vettore2.|vettore}}


{{APIFunction|distanceToPlane|Vector1,Vector2| |la distanza tra il vettore e un piano definito da un punto e una normale|float.}}


{{APIFunction|dot|Vector| |il prodotto scalare tra due vettori.}}


{{APIFunction|getAngle|Vector| |l'angolo in radianti tra 2 vettori|float.}}


{{APIFunction|multiply|Float|Moltiplica (scala uniforme) un vettore del fattore passato. | niente.}}


{{APIFunction|normalize| |normalizza un vettore (imposta la sua lunghezza a 1,0). | niente.}}


{{APIFunction|projectToLine|Vector1,Vector2|proietta il vettore su una linea attraverso Vettore1 in direzione Vettore2. | niente.}}


{{APIFunction|projectToPlane|Vector1,Vector2|proietta il vettore su un piano definito da un punto (Vettore1) e una normale (Vettore2). | nulla.}}


{{APIFunction|scale|Float,Float,Float|Uguale a moltiplicare, ma consente di specificare valori diversi per le direzioni x, y e z (scala non uniforme) .| Nulla.}}


{{APIFunction|sub|Vector|sottrae un altro vettore dal primo. | il vettore risultante.|vettore}}


{{APIProperty|x|la coordinata x di un vettore.}}


{{APIProperty|y|la coordinata y di un vettore.}}


{{APIProperty|z|la coordinata z di un vettore.}}



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > Vector API/it
