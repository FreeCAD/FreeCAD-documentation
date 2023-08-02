---
- GuiCommand:
   Name: PartDesign_Pad
   Name/cs: Návrh dílu Deska
   Workbenches: PartDesign Workbench/cs
   MenuLocation: Návrh dílu -> Deska
---

# PartDesign Pad/cs


</div>



## Úvod


<div class="mw-translate-fuzzy">

\'Vybraný náčrt do desky\' - Tento nástroj vezme vybraný náčrt (\'definující náčrt\') a vytvoří z něho \'desku\'. Pojem deska je zde obecně používán pro objekt vzniklý vysunutím náčrtu. Například, pokud je náčrt vytvořen ze dvou soustředných kružnic a následně je na ně aplikován nástroj Deska, bude výsledkem válec:


</div>

![](images/PartDesign_Pad_example.svg )

*Sketch (A) shown on the left; end result after pad operation (B) on the right.*

## Usage

1.  Select one sketch or face to be padded. <small>(v0.20)</small> : Alternatively you can select several sketches or faces.
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> [Pad](PartDesign_Pad.md)** button.
3.  Set the Pad parameters, see the [Options](#Options.md) below.
4.  Click **OK**.

When selecting a single sketch, it can have multiple enclosed profiles inside a larger one, for example a rectangle with two circles inside it. But the profiles may not intersect each other. <small>(v0.20)</small> 



## Volby


<div class="mw-translate-fuzzy">

Při vytváření desky nabízí dialogové okno \'parametrů desky\' pět různých způsobů zadání výšky do jaké bude deska vysunuta


</div>

![](images/Pad_parameters_cropped_cs.png )

### Type


<div class="mw-translate-fuzzy">

Typ nabízí pět různých způsobů určení délky, na kterou bude podložka protlačována.


</div>



#### Rozměr


<div class="mw-translate-fuzzy">

Zadání číselné hodnoty pro výšku desky. Defaultní směr vysunutí je ven z podkladu, ale může to být změněno zakliknutím volby **Opačně**. Vysunutí je ve směru [kolmém](http://en.wikipedia.org/wiki/Surface_normal) k definující rovině náčrtu. S volbou **Symetricky s rovinou** bude deska vysunuta z poloviny na jedné straně roviny a z poloviny na druhé straně roviny. Záporný rozměr není povolen. Místo toho použijte volbu **Opačně**.


</div>



### K poslední 

Deska se vysune až k poslední ploše tělesa ve směru vysunutí. Není-li v daném směru žádná plocha, zobrazí se chybové hlášení.



### K první 

Deska se vysune k první ploše tělesa ve směru vysunutí. Není-li v daném směru žádná plocha, zobrazí se chybové hlášení.



### Až k ploše 


<div class="mw-translate-fuzzy">

Deska se vysune až k ploše v objektu, která je vybrána kliknutím na ni. Není-li zde žádný objekt, nebude akceptován žádný výběr.


</div>



### Dva rozměry 


<div class="mw-translate-fuzzy">

Umožňuje zadat druhý rozměr. Pak se deska o tuto vzdálenost vysune na opačnou stranu (vzhledem k podkladové rovině). Opět lze využít volby **Opačně**.


</div>

### Length

Defines the length of the pad. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available when **Type** is either **Dimension** or **Two dimensions**.

### Offset to face 

Offset from face at which the pad will end. This option is only available when **Type** is either **To last**, **To first** or **Up to face**.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal:** The sketch or face is extruded along its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used. <small>(v0.20)</small> 
-   **Select reference\...:** The sketch is extruded along an edge of the 3D model. When this is method selected, you can click on any edge in the 3D model and it becomes the direction vector for the extrusion. <small>(v0.20)</small> 
-   **Custom direction:** The sketch is extruded along a direction that can be specified via vector values.

#### Show direction 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed. <small>(v0.20)</small> 

#### Length along sketch normal 

If checked, the pad length is measured along the sketch normal, otherwise along the custom direction. <small>(v0.20)</small> 

### Symmetric to plane 

Tick the checkbox to extrude half of the given length to either side of the sketch or plane.

### Reversed

Reverses the direction of the pad.

### Taper angle 


<small>(v0.20)</small> 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is either **Dimension** or **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

Limitations:

-   Sketches containing [B-Splines](B-Splines.md) often cannot be properly tapered. This is a limitation of the [OpenCASCADE](OpenCASCADE.md) kernel that FreeCAD uses.
-   For larger angles tapering will fail if the end face of the pad would have fewer edges than the start face/sketch.

### 2nd length 

Defines the length of the pad in the opposite extrusion direction. Multiple units can be used independently of the user\'s units preferences (m, cm, mm, nm, ft or \', in or \"). This option is only available if **Type** is **Two dimensions**.

### 2nd taper angle 


<small>(v0.20)</small> 

Tapers the pad in the opposite extrusion direction by the given angle. A positive angle means the outer pad border gets wider. This option is only available if **Type** is **Two dimensions**. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts.

## Properties

-    **Type**: Type of ways how the pad will be extruded, see [Options](#Options.md).

-    **Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2**: Second pad length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector**: If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction**: Vector of the pad direction if **Use Custom Vector** is used.

-    **Along Sketch Normal**: If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction. <small>(v0.20)</small> 

-    **Up To Face**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Refine**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part design → General → Model settings**). It can be manually changed afterwards. This property will be saved with the FreeCAD document.



## Omezení


<div class="mw-translate-fuzzy">

-   Stejně jako všechny funkce Návrh součástí, Pad také vytváří těleso, takže skica musí obsahovat uzavřený profil, jinak selže s chybou „Nepodařilo se ověřit zlomenou tvář". Uvnitř většího profilu může být více uzavřených profilů za předpokladu, že se žádné neprotínají (například obdélník se dvěma kruhy uvnitř).
-   Algoritmus používaný pro „To First" a „To Last" je:
    -   Vytvořte čáru přes těžiště náčrtu
    -   Najděte všechny plochy podpěry oříznuté touto čarou
    -   Vyberte plochu, kde je průsečík nejblíže / nejdále od náčrtu

:   To znamená, že nalezená tvář nemusí být vždy tím, co jste očekávali. Pokud se setkáte s tímto problémem, použijte místo toho typ „" „Nahoru do tváře" a vyberte požadovanou tvář.
:   Pro velmi zvláštní případ vytlačování na konkávní povrch, kde je náčrt větší než tento povrch, vytlačování selže. Toto je nevyřešená chyba.

-    v0.16 a nižší  Neexistuje žádné automatické čištění, např. sousedních rovinných povrchů do jednoho povrchu. Můžete to opravit ručně v pracovním stole součásti pomocí [ Zpřesnit tvar](Part_RefineShape/cs.md) (který vytvoří nepřipojený, neparametrický těleso) nebo pomocí [Zpřesnit tvarovou funkci](OpenSCAD_RefineShapeFeature/cs.md) z [OpenSCAD Workbench](OpenSCAD_Workbench/cs.md), který vytváří parametrickou funkci.


</div>


<div class="mw-translate-fuzzy">





</div>


{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Pad/cs
