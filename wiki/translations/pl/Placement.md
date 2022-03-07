# Placement/pl
## Przegląd

**Umiejscowienie** to sposób w jaki FreeCAD określa położenie i pozycję *(orientację)* obiektu w przestrzeni. Umiejscowienie może być określone w wielu formach i manipulowane poprzez [skrypty](Python_scripting_tutorial#Vectors_and_placements.md), [Edytor właściwości](Property_editor/pl.md) lub wybierając **Edycja → Umiejscowienie...** aby otworzyć [Panel zadań umiejscowienie](Std_Placement/pl.md).

### Dostęp do atrybutu Umiejscowienie 

Atrybuty Umiejscowienia obiektu mogą być dostępne i modyfikowane na 3 sposoby:

![Umiejscowienie w edytorze właściwości](images/PlacementPropertiesv10-800x800.png ) 

![Umiejscowienie w skrypcie jako y/p/r i Macierz i jej [API](images/Placement_API/pl.md).](PlacePyConv10.png ) 

![Panel zadań umiejscowienia](images/PlacementDialogv10.png ) 

## Formy umiejscowienia 

Umiejscowienie jest przechowywane wewnętrznie jako pozycja i obrót (oś obrotu i kąt przekształcone w [quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)). Chociaż istnieje kilka form określania obrotu, na przykład środek obrotu, jest on używany tylko do wpływania na obliczanie obrotu i nie jest przechowywany do późniejszych operacji. Podobnie, jeśli określona jest oś obrotu o wartości (1,1,1), może ona zostać znormalizowana podczas przechowywania w kwaternionie i pojawić się jako (0.58, 0.58, 0.58) podczas późniejszego przeglądania obiektu.

### Kąt, oś i pozycja 

**Umiejscowienie = \[Kąt, Oś i Pozycja\]**

Pierwsza forma **Umiejscowienia** ustala położenie obiektu w przestrzeni za pomocą Pozycji i opisuje jego orientację jako pojedynczy obrót wokół osi.

**Kąt = r** jest skalarem wskazującym wielkość obrotu obiektu wokół **Osi**. Wprowadzany jako stopnie, ale przechowywany wewnętrznie jako radiany.

**Oś = (ax,ay,az)** jest wektorem opisującym oś obrotu *(patrz uwaga o osi obrotu)*. Przykładami są:

   *(1,0,0)* ==> wokół osi **X**,
   *(0,1,0)* ==> wokół osi **Y**,
   *(0,0,1)* ==> wokół **osi Z**,
   *(0,71,0,71,0)* ==> wokół prostej **y=x**.

Zauważ, że możliwe jest również translacja *(przemieszczanie)* obiektu wzdłuż tej osi obrotu (ruch osiowy) poprzez wpisanie odległości do przemieszczenia w polu {{SpinBox|Osiowo: 0.0mm}} i kliknięcie **Zastosuj osiowo**. \'\'(Jednym ze sposobów wyobrażenia sobie ruchu osiowego jest samolot ze śmigłem obracającym się na dziobie - śmigło obraca się *wokół* osi obrotu, podczas gdy samolot porusza się *wzdłuż* tej samej osi)\'\'. Wartości w wektorze można traktować jako względną wielkość ruchu, który zostanie wykonany w danym kierunku. Na przykład w przypadku y=x *(0,71,0,71,0)* wartość zawarta w polu wyboru osi zostanie zastosowana w równej mierze w kierunkach X i Y, ale w kierunku Z nie nastąpi żaden ruch.

**Pozycja = (x,y,z)** to wektor opisujący punkt, od którego będzie obliczana geometria obiektu *(w efekcie jest to \"lokalny początek\" obiektu)*. Należy zauważyć, że w skryptach do oznaczenia składowej położenia obiektu Placement.Base jest używana wartość Placement.Base. Edytor właściwości nazywa tę wartość **pozycją**, a panel zadań umieszczania - przesunięciem.

### Pozycja i odchylenie, pochylenie oraz obrót 

![Panel zadań umiejscowienia: {{ComboBox|Kąty Eulera}} zaznaczone](images/PlacementDialogv10b.png )  **Umiejscowienie = \[Pozycja, odchylenie, pochylenie, obrót\]**.

Druga forma **Umiejscowienia** określa położenie obiektu w przestrzeni za pomocą **Pozycji** *(tak jak w pierwszej formie)*, ale opisuje jego orientację za pomocą [Kątów odchylenia, pochylenia i obrotu](http://en.wikipedia.org/wiki/Yaw,_pitch,_and_roll). Kąty te są czasem określane jako [kąty Eulera](http://en.wikipedia.org/wiki/Euler_angles) lub kąty Tait-Bryana. Odchylenie, Pochylenie i Obrót to powszechnie używane w lotnictwie określenia orientacji *(lub położenia)* ciała.

**Położenie = (x,y,z)** to wektor opisujący punkt, od którego będzie obliczana geometria obiektu *(w efekcie \"lokalne odniesienie położenia\" obiektu)*.

**Odchylenie-Pochylenie-Obrót = (y,p,r)** to krotka określająca położenie obiektu. Wartości dla y,p,r określają stopnie obrotu wokół każdej z osi z,y,x *(patrz uwaga)*.  
```python
>>> App.getDocument("Sans_nom").Cylinder.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(10,20,30), App.Vector(0,0,0))
```

App.Rotation(10,20,30) = Kąt Eulera

**Odchylenie** = 10° *(**Z**)*

**Pochylenie** = 20° *(**Y**)*

**Obrót** = 30° *(**X**)*

![](images/Tache_Placement_Lacet_fr_Mini.gif )**Odchylenie** to obrót wokół **osi Z**, czyli obrót z lewej strony na prawą.
*(Kąt odchylenia jest równy **Psi ψ**)*. 

![](images/Tache_Placement_Tangage_fr_Mini.gif )**Pochylenie** to obrót wokół **osi Y**, czyli do góry i do dołu.
*(Kąt nachylenia jest wartością **Phi φ**)*. 

![](images/Tache_Placement_Roulis_fr_Mini.gif )**Obrót** to obrót wokół osi X, czyli w górę i w dół skrzydła.
*(Kąt obrotu to **Thêta θ**)*. 

### Macierz

**Umiejscowienie = Macierz**

Trzecia forma **Umiejscowienia** opisuje położenie i orientację obiektu za pomocą macierzy transformacji afinicznej 4x4 *([Affine Transformation](http://en.wikipedia.org/wiki/Affine_transformation))*.

**Macierz** =

  ((r11,r12,r13,t1),
   (r21,r22,r23,t2),
   (r31,r32,r33,t3),
   (0,0,0,1)) , gdzie r*ij* określa obrót, a t*i* - przesunięcie. 




## Okno dialogowe umiejscowienia 

Okno dialogowe Umiejscowienia jest wywoływane z menu **Edycja**. Służy ono do precyzyjnego obracania / przesuwania obiektów. Jest ono również używane, gdy chcemy utworzyć szkic na \"niestandardowej\" płaszczyźnie lub zmienić orientację szkicu na nową płaszczyznę.

Sekcja **Przesunięcie** dostosowuje położenie obiektu w przestrzeni. Sekcja **Środek** dostosowuje oś obrotu do takiej, która nie przechodzi przez punkt odniesienia obiektu. W sekcji **Obrót** dostosowuje się kąt*(y)* obrotu oraz metodę określania tych kątów.

Chociaż elementy w każdej sekcji mają zasadniczo zastosowanie do celów danej sekcji, niektóre elementy w jednej sekcji mogą mieć wpływ na elementy w innej sekcji. Na przykład kliknięcie przycisku Wybrane punkty w sekcji **Środek** z zaznaczonymi dwoma punktami w oknie widoku 3D powoduje nie tylko wypełnienie pól wyboru współrzędnych **Środek** współrzędnymi punktu środkowego między tymi dwoma zaznaczonymi punktami, ale także utworzenie niestandardowej osi wzdłuż linii zdefiniowanej przez te dwa zaznaczone punkty w sekcji **Obrót**. W innym przykładzie umieszczenie wartości w polu wyboru osi i kliknięcie przycisku Zastosuj oś w sekcji **Przesunięcie** powoduje translację *(przesunięcie)* obiektu wzdłuż osi zdefiniowanej w sekcji **Obrót**.

Pole wyboru **Zastosuj zmiany przyrostowe** jest przydatne, gdy translacje / obroty mają być wykonywane względem aktualnego położenia / pochylenia obiektu, a nie względem pierwotnego położenia / pochylenia. Zaznaczenie tego pola resetuje pola dialogowe do zera, ale nie zmienia orientacji ani położenia obiektu. Kolejne wpisy zmieniają orientację / położenie, ale są stosowane od aktualnej pozycji obiektu. Włączenie tego pola wyboru jest również przydatne podczas korzystania z przycisku Wybrane punkty, ponieważ może ono czasami zapobiegać niepożądanym zmianom położenia.

PS: od wersji 0.17 wprowadzono nowy obiekt Część, obiekt ten posiada swoje umiejscowienie, a obiekt Umiejscowienie utworzony w obiekcie Część jest inkrementowany o Umiejscowienie części. {{Version/pl|0.17}} Aby uzyskać Umiejscowienie środowiska Część użyj następującego kodu: 
```python
import Draft, Part
sel = FreeCADGui.Selection.getSelection()
print sel[0].Placement
print sel[0].getGlobalPlacement()   # return the GlobalPlacement
print sel[0].getParentGeoFeatureGroup() # return the GeoFeatureGroup, ex:  Body or a Part.
print  "____________________"
```

Przycisk **Wybrane punkty** służy do wypełniania współrzędnych w polach współrzędnych **Środek** oraz *(po wybraniu 2 lub 3 punktów)* dodatkowo do tworzenia własnej (zdefiniowanej przez użytkownika) osi obrotu w sekcji **Obrót**. Punktem może być wierzchołek, ale może to być także dowolny punkt wzdłuż krawędzi lub na powierzchni. Gdy zaznaczasz krawędź lub ścianę, zaznaczana jest cała krawędź lub ściana, ale FreeCAD zapamiętuje również, na który punkt na tej ścianie lub krawędzi najeżdżał kursor myszki, gdy ta krawędź lub ściana była zaznaczona. To właśnie współrzędne tego punktu są używane w oknie dialogowym Umiejscowienie, gdy zostanie kliknięty przycisk **Wybrane punkty**. Być może uważasz, że nie jest to zbyt precyzyjny sposób zaznaczania punktu, i masz rację, ale w wielu przypadkach wystarczy, że wybrany punkt będzie znajdował się na tej krawędzi lub ścianie. W przypadkach, gdy trzeba precyzyjnie wyznaczyć punkt, który ma zostać użyty, należy wybrać wierzchołek. Jeśli w żądanym miejscu nie ma żadnego wierzchołka, można go utworzyć, np. w tymczasowym szkicu dołączonym do tej ściany lub krawędzi, lub za pomocą obiektu środowiska Rysunek Roboczy, takiego jak linia lub punkt itp.

Rozważmy najpierw prosty przypadek wybrania jednego punktu. W tym celu należy najpierw zaznaczyć żądany punkt, a następnie kliknąć przycisk **Wybrane punkty**. Współrzędne wybranego punktu zostaną użyte do wypełnienia pól obrotowych X, Y i Z w sekcji **Środek**. Teraz każdy obrót wykonywany na obiekcie będzie się odbywał wokół tego środka obrotu.

Now consider the case of selecting 2 points. You would select the 2 desired points, and then click the **Selected points** button. The coordinates of the midpoint between the 2 selected points get placed into the X, Y, and Z spinboxes within the **Center** section. Now any rotation done on the object will be about this center of rotation. But in addition to setting up the **Center** section coordinates a custom (user-defined) axis is also added to the **Axis** element within the **Rotation** section. (Note: if you were in Euler rotation mode, the mode gets switched to Rotation with an axis mode and the new custom axis is selected as the current axis of rotation.) Now any rotation done using the new custom axis will be about this axis of rotation. As an added bonus, the distance is measured between the 2 selected points, and this information is given in the Report View. (Note: Hold down the Shift key while clicking the **Selected points** button to copy the distance measurement to the clipboard.) By entering this distance into the Axial spinbox in the **Translation** section and clicking the **Apply axial** button you can translate (move) the object so that the first selected point now occupies the coordinates occupied by the second selected point (at the time the **Selected points** button was clicked).

Now consider the case of selecting 3 points. You would select the 3 desired points, and then click the **Selected points** button. The coordinates of the first selected point (order of selection is very important here) get placed into the X, Y, and Z spinboxes within the **Center** section. Since 3 points define a plane FreeCAD is able to take advantage of that and use those 3 points to create a new custom (user-defined) axis of rotation that is normal (perpendicular) to that defined plane. As with 2 selected points, the distance between points is also shown in the Report View, but this time it is the distance between the 2nd and 3rd selected points. (Note: Hold down the Shift key while clicking **Selected points** button \-- Shift + Click \-- to copy the angle measurement to the clipboard.) Additionally, the angle between the 2nd and 3rd points is also measured and displayed in the Report View. By entering this angle into the **Angle** spinbox within the **Rotation** section we can very precisely rotate the object such that now the 2nd selected point is in alignment with the coordinates occupied by the 3rd selected point. (Note: you might want to increase the number of digits used within the Edit menu -\> Preferences -\> General -\> Units -\> Number of decimals spinbox if you desire more precision.)

## Przykłady

Obroty wokół jednej osi:

<img alt="Before Rotation" src=images/RotationAboutZBefore.png  style="width:600px;"> Before Rotation (top view) 

<img alt="After Rotation about Z" src=images/RotationAboutZAfter.png  style="width:600px;"> After Rotation about Z (top view) 

<img alt="After Rotation about y=x" src=images/RotationAboutYXAfter.png  style="width:600px;"> After Rotation about y=x (right view) 

Rotation with offset centre point:

<img alt="Before Rotation" src=images/RotationOffsetBefore.png  style="width:600px;"> Before Rotation (top view) 

<img alt="After Rotation about Z" src=images/RotationOffsetAfter.png  style="width:600px;"> After Rotation about Z (top view) 

Rotation using Euler angles:

<img alt="Before Rotation" src=images/RotationEulerBefore.png  style="width:600px;"> Before Rotation 

<img alt="After Rotation" src=images/RotationEulerAfter.png  style="width:600px;"> After Rotation 

## Placement.Base vs Shape Definition 

Placement is not the only way to position a shape in space. Note the Python console in this image:

![2 Shapes with Same Placement](images/2Placements800.png )

Both cubes have the same value for Placement, but are in different locations! This is because the 2 shapes are defined by different vertices (curves in more complex shapes). For the 2 shapes in the above illustration:

 >>> ev = App.ActiveDocument.Extrude.Shape.Vertexes
 >>> for v in ev: print v.X,",",v.Y,",",v.Z
 ... 
 30.0,30.0,0.0
 30.0,30.0,10.0
 40.0,30.0,0.0
 40.0,30.0,10.0
 40.0,40.0,0.0
 40.0,40.0,10.0
 30.0,40.0,0.0
 30.0,40.0,10.0
 >>> e1v = App.ActiveDocument.Extrude001.Shape.Vertexes
 >>> for v in e1v: print v.X,",",v.Y,",",v.Z
 ... 
 0.0,10.0,0.0
 0.0,10.0,10.0
 10.0,10.0,0.0
 10.0,10.0,10.0
 10.0,0.0,0.0
 10.0,0.0,10.0
 0.0,0.0,0.0
 0.0,0.0,10.0
 >>> 
 

The Vertices (or Vectors) that define the shape use the Placement.Base attribute as their origin. So if you want to move a shape 10 units along the **X** axis, you could add 10 to the **X** coordinates of all the Vertices or you could set Placement.Base to (10,0,0).

## Using \"Center\" to Control Axis of Rotation 

By default, the axis of rotation isn\'t really the x/y/z axis. It is a line parallel to the selected axis, but passing through the reference point (Placement.Base) of the object to be rotated. This can be changed by using the Center fields in the Placement dialog or, in scripts, by using the Center parameter of the FreeCAD.Placement constructor.

For example, suppose we have a box (below) positioned at (20,20,10). ![Before Rotation](images/LocalZBefore2.png ) We wish to spin the box around it\'s own vertical centre line (ie local Z), while keeping it the same position. We can easily achieve this by specifying a Center value equal to the coordinates of the box\'s central point (25,25,15). ![After Rotation](images/LocalZAfter2.png )

In a script, we would do: 
```python
import FreeCAD
obj = App.ActiveDocument.Box                       # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)   # 45° about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)   # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                   # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,15)                  # central point of box 
pos = obj.Placement.Base                           # position point of box
newplace = FreeCAD.Placement(pos,rot,centre)       # make a new Placement object
obj.Placement = newplace                           # spin the box
``` Same script with the file example [RotateCoG2.fcstd](http://forum.freecadweb.org/download/file.php?id=1651) (discussion on the [forum](http://forum.freecadweb.org/viewtopic.php?f=3&t=3950#p31052)) 
```python
import FreeCAD
obj = App.ActiveDocument.Extrude                    # our box
rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),45)    # 45 about Z
#rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,1),45)    # 45° about X and 45° about Z
#rot = FreeCAD.Rotation(10,20,30)                    # here example with Euler angle Yaw = 10 degrees (Z), Pitch = 20 degrees (Y), Roll = 30 degrees (X) 
centre = FreeCAD.Vector(25,25,0)                    # "centre" of rotation (where local Z cuts XY)
pos = obj.Placement.Base                            # original placement of obj
newplace = FreeCAD.Placement(pos,rot,centre)        # make a new Placement object
obj.Placement = newplace                            # spin the box
```

## Using Placement in expressions 

In expressions it is possible to use the components of the placement for example to access the x-component of the object labeled \"Cube\": 
```python
<<Cube>>.Placement.Base.x
```

Dostęp do kąta obrotu można uzyskać przez 
```python
<<Cube>>.Placement.Rotation.Angle
```

Dostęp do osi obrotu można uzyskać za pomocą 
```python
<<Cube>>.Placement.Rotation.Axis.x
<<Cube>>.Placement.Rotation.Axis.y
<<Cube>>.Placement.Rotation.Axis.z
``` gdzie często jedną z tych wartości jest {{Value|1}}, a pozostałe są równe {{Value|0}}.

You can also use the whole Placement in a single expression: Right click on Placement property in the property editor, select \"show all\" then extra properties will show. If you then right click on Placement again the context menu will include Expression, select Expression then the Expression dialogue will open and whatever you type will go into the Placement property rather than its child properties.

To make the placement of \"Sketch\" equal to that of \"Cylinder\", you would enter in that way for Sketch the expression 
```python
<<Cube>>.Placement
``` ![Setting the whole Placement in one expression](images/PlacementInExpression.png )

**NOTE:** It\'s also possible to *create* Placement objects in expressions. See the [Expressions](Expressions#Placement.md) page for details.

## Uwagi

-   The Placement properties in the Data tab are disabled for objects which are attached to some other object. The Attachment Offset has to be edited instead.
-   Axis and Angle can also be expressed as a [quaternion](http://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation).
-   The reference point of an object varies depending on the object. Some examples for common objects:

  Object                           Reference Point
   
  Part.Box                         left (minx), front (miny), bottom (minz) vertex
  Part.Sphere                      center of the sphere (ie centre of bounding box)
  Part.Cylinder                    center of the bottom face
  Part.Cone                        center of bottom face (or apex if bottom radius is 0)
  Part.Torus                       center of the torus
  Features derived from Sketches   the Feature inherits the Position of the underlying Sketch. Sketches always start with Position = (0,0,0). This position corresponds to the origin in the sketch.

## Problemy

-   Względne rozmieszczanie obiektów będzie docelowo obsługiwane w środowisku pracy Złożenie.

## Więcej

-   Ten poradnik: [Aeroplan](Aeroplane/pl.md) obszernie omawia mechanikę zmiany położenia obiektu.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Placement/pl
