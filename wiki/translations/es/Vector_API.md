# Vector API/es
<div class="mw-translate-fuzzy">

Los vectores se utilizan en todas partes en FreeCAD.


</div>

Vectors are used everywhere in FreeCAD.

Ejemplo: 
```python
v=FreeCAD.Vector()
v=FreeCAD.Vector(1,0,0)
v=FreeCAD.Base.Vector()
v2 = FreeCAD.Vector(3,2,-5)
v3 = v.add(v2)
print v3.Length
```


<div class="mw-translate-fuzzy">


{{APIProperty/es|Length|Devuelve la longitud del vector.}}


{{APIFunction/es|add|Vector|Añade otro vector a este|La suma de ambos vectores.}}


{{APIFunction/es|cross|Vector| |El producto vectorial de dos vectores.}}


{{APIFunction/es|distanceToLine|Vector1,Vector2| |La distancia entre el vector y una línea entre el Vector1 y Vector2.}}


{{APIFunction/es|distanceToPlane|Vector1,Vector2| |La distancia entre el vector y un plano definido por un punto y una normal.}}


{{APIFunction/es|dot|Vector| |El producto escalar de dos vectores.}}


{{APIFunction/es|getAngle|Vector| |El ángulo en radianes entre dos vectores.}}


{{APIFunction/es|multiply|Float|Multiplica (escala) un vector por el factor dado|Nada.}}


{{APIFunction/es|normalize| |Normaliza un vector (establece su longitud a 1.0).|Nada.}}


{{APIFunction/es|projectToLine|Vector1,Vector2|Proyecta el vector sobre una línea entre Vector1 y Vector2.|Nada.}}


{{APIFunction/es|projectToPlane|Vector1,Vector2|Proyecta el vector sobre un plano definido por un punto y una normal.|Nada.}}


{{APIFunction/es|scale|Float,Float,Float|Lo mismo que multiplicar pero permite especificar valores diferentes para las direcciones X, Y y Z.|Nada.}}


{{APIFunction/es|sub|Vector|Resta otro vector del primero.|El vector resultante.}}


{{APIProperty/es|x|La coordenada X de un vector.}}


{{APIProperty/es|y|La coordenada Y de un vector.}}


{{APIProperty/es|z|La coordenada Z de un vector.}}


</div>



---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > Vector API/es
