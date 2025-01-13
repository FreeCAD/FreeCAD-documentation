---
 GuiCommand:
   Name: PartDesign_Pad
   Name/cs: Návrh dílu Deska
   Workbenches: PartDesign Workbench/cs
   MenuLocation: Návrh dílu , Deska
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

1.  Select a single sketch or one or more faces from the Body.
2.  Press the **<img src="images/PartDesign_Pad.svg" width=16px> [Pad](PartDesign_Pad.md)** button.
3.  Set the Pad parameters, see [Options](#Options.md) below.
4.  Press the **OK** button.



## Volby


<div class="mw-translate-fuzzy">

Při vytváření desky nabízí dialogové okno \'parametrů desky\' pět různých způsobů zadání výšky do jaké bude deska vysunuta


</div>


<div class="mw-translate-fuzzy">

![](images/Pad_parameters_cropped_cs.png )


</div>

### Type


<div class="mw-translate-fuzzy">

Typ nabízí pět různých způsobů určení délky, na kterou bude podložka protlačována.


</div>



#### Rozměr


<div class="mw-translate-fuzzy">

Zadání číselné hodnoty pro výšku desky. Defaultní směr vysunutí je ven z podkladu, ale může to být změněno zakliknutím volby **Opačně**. Vysunutí je ve směru [kolmém](http://en.wikipedia.org/wiki/Surface_normal) k definující rovině náčrtu. S volbou **Symetricky s rovinou** bude deska vysunuta z poloviny na jedné straně roviny a z poloviny na druhé straně roviny. Záporný rozměr není povolen. Místo toho použijte volbu **Opačně**.


</div>



### K poslední 


<div class="mw-translate-fuzzy">

Deska se vysune až k poslední ploše tělesa ve směru vysunutí. Není-li v daném směru žádná plocha, zobrazí se chybové hlášení.


</div>



### K první 


<div class="mw-translate-fuzzy">

Deska se vysune k první ploše tělesa ve směru vysunutí. Není-li v daném směru žádná plocha, zobrazí se chybové hlášení.


</div>



### Až k ploše 


<div class="mw-translate-fuzzy">

Deska se vysune až k ploše v objektu, která je vybrána kliknutím na ni. Není-li zde žádný objekt, nebude akceptován žádný výběr.


</div>



### Dva rozměry 


<div class="mw-translate-fuzzy">

Umožňuje zadat druhý rozměr. Pak se deska o tuto vzdálenost vysune na opačnou stranu (vzhledem k podkladové rovině). Opět lze využít volby **Opačně**.


</div>

#### Up to shape 


<small>(v1.0)</small> 

: The pad will extend up to the selected shape. Optionally press the **Select shape** button and select a shape. Leave the **Select all faces** checkbox enabled or disable it, press the **Select faces** button and select the faces up to which the pad should be created.

### Offset to face 

Offset from face at which the pad will end. This option is only available if **Type** is **To last**, **To first** or **Up to face**.

### Length

Defines the length of the pad. This option is only available if **Type** is **Dimension** or **Two dimensions**. The length is measured along the direction vector, or along the normal of the sketch or face. Negative values are not possible. Use the **Reversed** option instead.

### 2nd length 

Defines the length of the pad in the opposite direction. This option is only available if **Type** is **Two dimensions**.

### Symmetric to plane 

Check this option to extrude half the given length to either side of the sketch or face. This option is only available if **Type** is **Dimension**.

### Reversed

Reverses the direction of the pad.

### Direction

#### Direction/edge

You can select the direction of the extrusion:

-   **Sketch normal** or **Face normal:** The sketch or face is extruded in the direction of its normal. If you have selected several sketches or faces to be extruded, the normal of the first one will be used.
-   **Select reference\...:** The sketch or face is extruded in the direction of a straight edge or a [datum line](PartDesign_Line.md) selected from the Body.
-   **Custom direction:** The sketch or face is extruded in the direction of the specified vector.

#### Show direction 

If checked, the pad direction will be shown. In case the pad uses a **Custom direction**, it can be changed.

#### Length along sketch normal 

If checked, the pad length is measured along the sketch or face normal, otherwise along the custom direction.

### Taper angle 

Tapers the pad in the extrusion direction by the given angle. A positive angle means the outer pad border gets wider. Note that inner structures receive the opposite taper angle. This is done to facilitate the design of molds and molded parts. This option is only available if **Type** is **Dimension** or **Two dimensions**.

### 2nd taper angle 

Tapers the pad in the opposite extrusion direction by the given angle. See **Taper angle**. This option is only available if **Type** is **Two dimensions**.

## Properties

### Data


{{TitleProperty|Pad}}

-    **Type|Enumeration**: Defines how the pad will be extruded, see [Options](#Options.md).

-    **Length|Length**: Defines the length of the pad, see [Options](#Options.md).

-    **Length2|Length**: Second pad length in case the **Type** is **TwoLengths**, see [Options](#Options.md).

-    **Use Custom Vector|Bool**: If checked, the pad direction will not be the normal vector of the sketch but the given vector, see [Options](#Options.md).

-    **Direction|Vector**: Vector of the pad direction if **Use Custom Vector** is used.

-    **Reference Axis|LinkSub**
    

-    **Along Sketch Normal|Bool**: If *true*, the pad length is measured along the sketch normal. Otherwise and if **Use Custom Vector** is used, it is measured along the custom direction.

-    **Up To Face|LinkSub**: A face the pad will extrude up to, see [Options](#Options.md).

-    **Offset|Length**: Offset from face in which the pad will end. This is only taken into account if the **Type** option **UpToLast**, **UpToFirst** or **UpToFace** is used.

-    **Taper Angle|Angle**
    

-    **Taper Angle2|Angle**
    


{{TitleProperty|Part Design}}

-    **Refine|Bool**: True or false. Cleans up residual edges left after the operation. This property is initially set according to the user\'s settings (found in **Preferences → Part Design → General → Model settings**).


{{TitleProperty|Sketch Based}}

-    **Profile|LinkSub**
    

-    **Midplane|Bool**
    

-    **Reversed|Bool**
    

-    **Allow Multi Face|Bool**
    



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
