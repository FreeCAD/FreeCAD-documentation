---
- GuiCommand:
   Name: Std Placement
   Name/pl: Std: Umiejscowienie
   MenuLocation: Edycja -> Umiejscowienie ...
   Workbenches: wszystkie
   SeeAlso: Std_Alignment/pl, Placement/pl
---

# Std Placement/pl

## Opis

Polecenie **Std: Umiejscowienie** wyświetla [panel zadań](Task_panel/pl.md) Umiejscowienia dla wybranego obiektu.

![](images/Std_Placement_taskpanel.png ) 
*Panel zadań funkcji umiejscowienie*

## Użycie

1.  Zaznacz pojedynczy obiekt, który ma właściwość **Umiejscowienie** w [edytorze właściwości](Property_editor/pl.md).
2.  Wybierz z menu opcję **Edycja → Umiejscowienie ...**.
3.  Zmień jeden lub więcej parametrów przesunięcia i obrotu.
4.  Wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk **OK**, aby zastosować zmiany i zamknąć panel zadań.
    -   Naciśnij przycisk **Zastosuj**, aby zastosować zmiany, ale zachować panel zadań otwarty dla dalszych zmian.
5.  Naciśnij klawisz **Esc** lub przycisk **Anuluj**, aby przerwać operację. Spowoduje to cofnięcie wszystkich zmian, które nie zostały zastosowane.

Okno dialogowe można również uruchomić, klikając przycisk z wielokropkiem **...**, który pojawia się w [edytorze właściwości](Property_editor/pl.md) po kliknięciu właściwości **Umiejscowienie**.

## Uwagi

-   Więcej informacji na temat parametrów rozmieszczenia można znaleźć na stronie [Umiejscowienie](Placement/pl.md) oraz w poradniku [Samolot](Aeroplane/pl.md).

## Tworzenie skryptów 


**Zobacz również:**

[FreeCAD podstawy tworzenia skryptów](FreeCAD_Scripting_Basics/pl.md).

Zobacz również stronę [Tworzenie skryptów Python](Python_scripting_tutorial/pl#Wektory_i_umiejscowienia.md).

Umiejscowienie jest wewnętrznie zdefiniowane przez macierz. W wielu przypadkach prościej jest przedstawić je za pomocą dwóch składników, punktu *(wektora)* `Baza` i wartości `Obrót`. Sam `Obrót` ma różne reprezentacje. Może być całkowicie zdefiniowany przez wartość \"[quaternion](https://en.wikipedia.org/wiki/Quaternion)\" `(xi + yj + zk + w)`, ale może być również opisana przez rotację `Oś` *(wektor jednostkowy)* oraz rotację `Kąt` *(radiany)*.


```python
import FreeCAD as App

doc = App.newDocument()
obj = doc.addObject("Part::Cylinder", "Cylinder")

print(obj.Placement)
# Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
print(obj.Placement.Base)
# Vector (0.0, 0.0, 0.0)
print(obj.Placement.Rotation)
# Rotation (0.0, 0.0, 0.0, 1.0)

print(obj.Placement.Rotation.Angle)
# 0.0
print(obj.Placement.Rotation.Axis)
# Vector (0.0, 0.0, 1.0)
print(obj.Placement.Rotation.Q)
# (0.0, 0.0, 0.0, 1.0)
```

Przesuń punkt bazowy obiektu, a następnie obróć obiekt o 45° wokół osi X. 
```python
import math

obj.Placement.Base = App.Vector(5, 3, 1)
obj.Placement.Rotation.Axis = App.Vector(1, 0, 0)
obj.Placement.Rotation.Angle = math.radians(45)

print(obj.Placement)
# Placement [Pos=(5,3,1), Yaw-Pitch-Roll=(0,0,45)]
print(obj.Placement.Rotation.Q)
# (0.3826834323650898, 0.0, 0.0, 0.9238795325112867)
print(obj.Placement.Matrix)
# Matrix ((1,0,0,5),(0,0.707107,-0.707107,3),(0,0.707107,0.707107,1),(0,0,0,1))
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Placement/pl
