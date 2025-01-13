# Macro FCInfo/it
<div class="mw-translate-fuzzy">


{{Macro
|Name=Macro FCInfo
|Icon=FCInfo.png
|Description=Fornisce una ampia serie di informazioni sulla forma selezionata quali lunghezza, angoli, superficie, inclinazione, volume e peso secondo la densità della forma selezionata, sia nelle unità del Sistema Internazionale che in quelle del Sistema Anglosassone.
<br />Versione francese [https://gist.githubusercontent.com/mario52a/6afc64081c4eb8be3b93/raw/57021aa2ac873bf5bdf0aad877cedaa59081dee1/FCInfo_fr_Ver_1-29b-rmu_Docked.FCMacro Version française]
|Author=Mario52
|Version=1.29b
|Date=2023/05/10
|FCVersion=All
|SeeAlso=[Arch: Ispeziona](Arch_Survey.md), [Macro SimpleProperties](Macro_SimpleProperties.md), [Macro FCInfoGlass](Macro_FCInfoGlass.md)
}}


</div>



## Descrizione

Fornisce una ampia serie di informazioni sulla forma selezionata quali lunghezza, angoli, superficie, inclinazione, volume e peso secondo la densità della forma selezionata, sia nelle unità del Sistema Internazionale che in quelle del Sistema Anglosassone.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/8d40ab6c018c2bde678f/raw/c6dd9eabe1ae67d0baf235d672faa75dfd927ad6/FCInfo_en_Ver_1-30-rmu_Docked.FCMacro}}

<img alt="FCInfo" src=images/Macro_FCInfo_00_en.png  style="width:480px;"> 
*FCInfo*



## Utilizzo

Selezionare un oggetto e avviare l\'applicazione oppure avviare prima l\'applicazione e quindi selezionare un oggetto. L\'oggetto viene analizzato e si apre una finestra di dialogo che mostra le informazioni raccolte. Ad ogni nuova selezione, l\'unità di lunghezza viene reimpostata su **mm** e l\'unità angolare su **gradi decimali**. <img alt="upper window" src=images/Macro_FCInfo_06.png  style="width:900px;">






### Settore 1: Documento 

![FCInfo Document](images/Macro_FCInfo_Document_00.png )

-   Nome del documento
-   Etichetta dell\'oggetto
-   Nome interno dell\'oggetto
-   Nome dei sottoelementi dell\'oggetto
-   Tipo di oggetto

*(puoi impostare a {{false}} la variabile **switch_setVisible_GBox_001_Document** per nascondere il box)*



### Settore 2: Coordinate del clic col mouse 

![FCInfo Coordinate](images/Macro_FCInfo_Coordinate_click_mouse_00.png )

-   Le coordinate X,Y e Z cliccate con il mouse
-   Il **bottone** crea un punto, un asse, un piano, copia l\'asse vettoriale da **FreeCAD.Vector(-24.0, 240.0, 7.0)**

*(puoi impostare a {{false}} la variabile **switch_setVisible_GBox_002_Coordinate_Mouse** per nascondere il Box)*



### Settore 3: Colore sul punto 

![FCInfo Color_on_point](images/Macro_FCInfo_Color_on_point_00.png )

-   Colore sul punto cliccato.
    -   valore da 0,0 a 1,0

-   La riga modificabile visualizza il valore del colore in diversi formati: {{LineEdit|"3435973887" , "#cccccc" , "0xcccccc" , "204,204,204" , "(0.8,0.8,0.8)"}}
    -   **3435973887** : Modalità RVBA Int unsigned (formato nelle preferenze di FreeCAD) Alpha = 255
    -   **#cccccc** : Modalità RVB Esadecimale (Qt: `setStyleSheet("color : #cccccc")`)
    -   **0xcccccc** : Modalità RVB Esadecimale (Python: `hex(0xcccccc`)
    -   \"**204,204,204** \" : RVB decim: Modalità RVB (Qt: `setStyleSheet(u"QLineEdit {" background-color: rgb(204, 204, 204)};")`)
    -   **(0.8,0.8,0.8)** : RVB float: Modalità formato RVB float da 0.0 a 1.0
    -   (Il numero di decimali dipende dall\'opzione *\"x (Decimals)\"*)

-    {{CheckBox|Sub.Objet}}: Cambia il colore dell\'oggetto o sotto-oggetto selezionato. Se questa casella è attivata {{CheckBox|TRUE|Sub.Objet}} la faccia o l\'oggetto secondario selezionato viene modificato o duplicato. Se non è attivato (default) l\'oggetto viene modificato (colore) o duplicato

-    **Coul. Obj**: Se cambiare il colore della forma o della faccia dipende dall\'opzione scelta. Nel caso dell\'oggetto Mesh o Punti viene colorato l\'oggetto completo.

-    **Dupl. Obj**: La duplicazione della faccia o dell\'oggetto dipende dall\'opzione scelta. Nel caso di un oggetto Mesh o di Punti l\'oggetto completo viene colorato. La duplicazione di un oggetto Mesh mantiene l\'originale e crea una forma solida. La duplicazione di un oggetto Points mantiene l\'originale e crea una copia.

-    {{SpinBox|0}}: Il grado di trasparenza della faccia o dell\'oggetto selezionato dipende dall\'opzione scelta **0 = opaco** , **100 = trasparente**

*(si può impostare a {{false}} la variabile **switch_setVisible_GBox_003_Color** per nascondere la casella)*



### Settore 4: Componenti Mesh 

![FCInfo Component Mesh](images/Componant_Mesh_v_1-28.png )

Se la selezione è un oggetto mesh viene visualizzata una nuova finestra ***\"Components\"*** che fornisce:

-   Edges : numero di bordi {{LineEdit|9561}}.
-   Faces : numero di facce {{LineEdit|6374}}.
-   Points : numero di punti {{LineEdit|3189}}.

*(si può impostare a {{false}} la variabile **switch_setVisible_GBox_004_Object_Mesh** per nascondere il Box)*


### Settore 5: Unità 

![FCInfo Units](images/Macro_FCInfo_Units_00.png )

-    {{ComboBox|mm}}: se l\'oggetto è il perimetro di una faccia, viene visualizzata la lunghezza dell\'oggetto. È possibile selezionare la dimensione dell\'unità:
    km, hm, decametri, m, dm, cm, **mm**, µm, nm, pm, fm, pollici, link, piede, iarda, pertica, catena, furlong, miglio, lega, nautica.

-   Length of the object: Lunghezza dell\'oggetto o perimetro della faccia {{LineEdit|10.0 mm}}.

-   Se l\'oggetto è un cerchio, viene mostrato un secondo campo **Radius :** che visualizza il raggio e il diametro del cerchio {{LineEdit|2.0 mm (dia. 4.0 mm)}}.

-   Perimeter of the shape (12). Perimetro dell\'oggetto e numero di sotto-oggetti (Bordi) contenuti nell\'oggetto {{LineEdit|120.0 mm}}.

*(si può impostare a {{false}} la variabile **switch_setVisible_GBox_005_Value_Unit** per nascondere la casella)*



### Settore 6: Inclinazione 

![FCInfo Inclination](images/Macro_FCInfo_Inclination_00.png )

-   **Inclination of the object** can be displayed in:
    -   decimal degree, ex: {{LineEdit|174.831872611°}}
    -   degree minute seconde, ex: {{LineEdit|174° 49' 54.741401''}}
    -   radian, ex: {{LineEdit|3.05139181449 rad}}
    -   grade, ex: {{LineEdit|194.257636235 gon}}
    -   percent, ex: 30° = {{LineEdit|57.74%}}
-   **Inclinations in planes XY, YZ, ZX** and their coordinates
-   **Direction object**, {{LineEdit|Vector (0.0, 0.0, -10.0)}} give the direction of object. The calculate is : coord_1 - coord_2 = direction (or reverse)
    -   
        **Direction**
        
        this button create a line in direction of the object.
-   **ValueAt(0)**, {{LineEdit|Vector (0.0, 0.0, 10.0)}} returns the 3D vector corresponding to a parameter value.
    -   
        **ValueAt(0)**
        
        this button create a line in ValueAt direction of the object.
-   **NormalAt(0,0)**, {{LineEdit|Vector (0.0, 0.0, 1.0)}} returns the 3D vector corresponding to a parameter value.
    -   
        **NormalAt(0,0)**
        
        this button create a line in NormalAt direction of the object.

*(you can checked to {{false}} the variable **switch_setVisible_GBox_006_Inclination** for hidden the Box)*



### Settore 7: Superficie e Volume 

![FCInfo Surface and Volume](images/Macro_FCInfo_Surface_and_Volume_00.png )

-   Surface of the form displayed, unit size can be selected. {{LineEdit|600.0 mm2}}
-   Surface of the face displayed, unit size can be selected. {{LineEdit|0.0 mm2}}
-   Volume of the form displayed, unit size can be selected. {{LineEdit|1000.0 mm3}}
-   Unit , choice your unit.
-   The {{ComboBox|gram}} unit mass can be chosen :
    ton,quintal, kg, hg, dag, **gram**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy),
    lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct.
-   Weight of the form displayed, unit mass can be selected. {{LineEdit|2.7 g}}
-   Density of the material in **kg by dm3** {{LineEdit|2.7000 kg (by dm3)}}
-   Material {{ComboBox|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   In beginning the macro search the file **FCInfo_material.txt**, if the file not exist, one file FCInfo_material.txt is created.
    -   The file is created with 10 types of material saved in this format.
        -   **Title of material , Density on dm3 , Price on dm3 , text info on choice**
        -   *(4 fields separate by coma)*
        -   Liquid Water (H2o),1,10.0,adapt Price
        -   Mater Beton,2.4,10.0,adapt Price
        -   Metal Aluminium (Al),2.7,10.0,adapt Price
        -   Metal Copper (Cu),8.96,10.0,adapt Price
        -   Metal Gold (Au),19.3,10.0,Gratis
        -   Metal Iron (Fe),7.87,10.0,adapt Price
        -   Metal Lead (Pb),11.35,10.0,adapt Price
        -   Metal Magnesium (Mg),1.43,10.0,adapt Price
        -   Metal Nickel (Ni),8.27,10.0,adapt Price
        -   Metal Pewter (Sn),7.29,10.0,adapt Price
        -   Metal Platinum (Pt),21.45,10.0,adapt Price
        -   Metal Silver (Ag),10.5,10.0,adapt Price
        -   Metal Sodium (Na),0.97,10.0,adapt Price
        -   Metal Titanium (Ti),4.4,10.0,adapt Price
        -   Metal Zinc (Zn),7.1,10.0,adapt Price
        -   Wood Beechwood,0.8,10.0,adapt Price
        -   Wood MDF,0.75,10.0,adapt Price
        -   Wood Mahogany,0.6,10.0,adapt Price
        -   Wood Oak,0.7,10.0,adapt Price
        -   Wood White pine,0.4,10.0,adapt Price
-   New material or editing {{LineEdit|Metal Nickel (Ni),8.27,10.0,adapt Price}}
    -   you can modify or edit one new material in this format:

    -   **Title, Density on dm3, Price on dm3, text info on choice**

    -   *(4 fields separate by coma)*

    -   *you can also edit the file in your favorite editor respecting the specific format*

    -   you can save the file in a path desired with the variable : **seTMaterialSavePathName**

    -   *by default the file is created in the macro path*

    -   
        **Delete 1/17**
        
        : delete the field displayed

    -   
        **Save**
        
        : save the modification or the new material

*(you can checked to {{false}} the variable **switch_setVisible_GBox_007_Surface_and_Volume** for hidden the Box)*



### Settore 8: Costo 

![FCInfo Cost](images/Macro_FCInfo_Cost_00.png )

-   Cost total : cost total of the object selected


{{LineEdit|0.027 Eu}}

-   Price (kg/dm3) : price of the material selected (*Metal Aluminium (Al),2.7,***10.0***,adapt Price*)


{{SpinBox|10,0000 Eu (by Kg)}}

*(you can checked to {{false}} the variable **switch_setVisible_GBox_008_Cost_And_Price** for hidden the Box)*



### Settore 9: BoundBox 

![FCInfo BoundBox](images/Macro_FCInfo_BoundBox_00.png )

-   BoundBox gives extreme dimensions of the shape.
    -   maximum X length : {{LineEdit|10.0 mm}}

    -   maximum Y length : {{LineEdit|10.0 mm}}

    -   maximum Z length : {{LineEdit|10.0 mm}}

    -   diagonal length : {{LineEdit|17.3205 mm}}

    -   
        **Tracing**
        
        : create 6 rectangles to dimensions of boundbox

    -   
        **Volume**
        
        : create volume to dimensions of boundbox

    -   
        {{CheckBox|Text Dim.}}
        
        : create the dimension of the triangle *(boundbox)*

    -   If the {{CheckBox|TRUE|Text Dim.}} is checked, the spinbox dimension of text {{SpinBox|3,000}} is operational for give your value *(3.0 by default)*

*(you can checked to {{false}} the variable **switch_setVisible_GBox_009_BoundBox** for hidden the Box)*



### Settore 10: Centro di: 

![FCInfo Center of\...](images/Macro_FCInfo_Center_of_00.png )

-   Center of the shape and these coordinates XYZ
-   Center of mass and these coordinates XYZ
-   The **buttons** creates on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(see Sector 13)*

*(you can checked to {{false}} the variable **switch_setVisible_GBox_010_Center_Mass** for hidden the Box)*



### Settore 11: Inerzia 

![FCInfo Inertia](images/Macro_FCInfo_Inertia_00.png )

-   Moment of inertia and these coordinates length and weigth
-   The button creates on point, axis, plane, copy vector axis form **FreeCAD.Vector(-24.0, 240.0, 7.0)** *(see Sector 13)*
    -   action line 1 : {{LineEdit|x1}}, {{LineEdit|y1}}, {{LineEdit|z1}}, {{LineEdit|0.0}}
    -   action line 2 : {{LineEdit|x2}}, {{LineEdit|y2}}, {{LineEdit|z2}}, {{LineEdit|0.0}}
    -   action line 3 : {{LineEdit|x3}}, {{LineEdit|y3}}, {{LineEdit|z3}}, {{LineEdit|0.0}}
    -   action 4 diagonal : {{LineEdit|x1}}, {{LineEdit|y2}}, {{LineEdit|z3}}

same for length and weigth

-   Determinant 1 : {{LineEdit|4629629629629.633}} computes the determinant of the matrix, in [scientific value](https://en.wikipedia.org/wiki/Scientific_notation)
-   Determinant 2 : {{LineEdit|4629629629629.6328125}} computes the determinant of the matrix, in decimal value

*(you can checked to {{false}} the variable **switch_setVisible_GBox_011_Inertia** for hidden the Box)*



### Settore 12: Foglio di calcolo 

![FCInfo Disabled](images/Macro_FCInfo_Disabled_module_00.png )

-    {{CheckBox|Disabled module}}CheckBox for search or not all details of the object. If it is not checked, only the principal value is displayed.

-   Vertexes and details of the shape (compt_Edge), (compt_Faces), (compt_Vector of the Face)

-   Max 200 lines in the table, if there are more than 200 lines it appears **(!+ 200)** and the number of lines

-   If the object is complicated with many objects, the time is long and the search is repeated with every mouse click. The write function in the spreadSheet included, decreases the display time for this it is disabled by default

-   Full details can save be the **Save** button in a file in CSV format and can be viewed the file in spreadsheet with the **Read** or by an external spreadsheet as [LibreOffice](https://www.libreoffice.org/) [OpenOffice](http://openoffice.apache.org/downloads.html) or other

*(you can checked to {{false}} the variable **switch_setVisible_GBox_012_SpreadSheet** for hidden the Box)*



### Settore 13: creazione del foglio di calcolo 

![FCInfo SpreedSheet](images/Macro_FCInfo_SpreedSheet_00.png )

-    **SpreadSheet**: create a new spreadsheet in a document

-    {{LineEdit|SpreadSheet}}: the current spreadsheet. if the spreadsheet does not exist one spreadsheet is created

-    **Refresh**: refresh the list of spreadsheet in document

-    {{ComboBox|-}}: the spreadsheet(s) present in document

-    **Read**: read the data in a spreadsheet saved **.FCInfo** or txt, asc, csv

-    **Save**: save the data in disk in the form selected below **.FCInfo** or txt, asc, csv

-    {{RadioButton|TRUE|Tabulation}}: the separator is Tabulation (by default)

-    {{RadioButton|Comma}}: the separator is Comma

-    {{RadioButton|Semicolon}}: the separator is Semicolon

-    {{RadioButton|Space}}: the separator is Space


<div class="mw-translate-fuzzy">

L\'opzione per salvare e leggere lo spreadsheet con differenti separatori, Tabulazioni, Virgola, Punto virgola, Spazzio
La Tabulazione e il separatore dello spreadsheet di FreeCAD
Il numero di separatori e calcolato per dare una potenziale informazione di chi sarebbe il separatore dentro il filo aperto.
La virgola e il separatore delle versione anteriore de FCInfo (01.16 e inferiore)
Adesso (versione 01.17 e più) il separatore per difetto e la tabulazione
Se volete convertire le vecchie fili di FCInfo, caricate il file con il separatore del file e salvatelo con la casella Tabulazione selezionata.


</div>



### Settore 14: Strumenti principali 

![FCInfo Main](images/Macro_FCInfo_Main_00.png )

-    {{CheckBox|Info}}: if this CheckBox is checked, the informations are displayed in the report view window

-    {{CheckBox|Point}}: if checked, one point is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Axis}}: if checked, one axis is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{CheckBox|Plane}}: if checked, one axis plane is created in the coordinate displayed form : **FreeCAD.Vector(-24.0, 240.0, 7.0)**

-    {{RadioButton|Clip-B0}}: None clipBoard

-    {{RadioButton|Clip-B1}}: If checked the coordinate are copy in the clipBoard Form : **FreeCAD.Vector(X.0, Y.0, Z.0)** FreeCAD model

-    {{RadioButton|Clip-B2}}: If checked the coordinate are copy in the clipBoard Form : **X, Y, Z** with Comma separator

-    {{RadioButton|Clip-B3}}: If checked the coordinate are copy in the clipBoard Form : **X Y Z** as is with Space separator

-    {{CheckBox|Left/Right}}: if this CheckBox is not checked, the window macro are displayed to right (default). If it is checked the window macro are displayed to left.
    If the option is 1 mode fly *(User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**seTPositionFlyRightLeft**)* this button is not visible .

-    {{SpinBox|4 (Decimales)}}: give the number of decimal displayed

-    {{SpinBox|12 (Dim. texte)}}: give the dimensionof text in the macro

-    **Forum**: direction FCInfo forum tread *(you must to be connected to internet)*

-    **Wiki**: direction Wiki FCInfo *(you must to be connected to internet)*

-    **Ref**: refresh the display of data in report view

-    **Exit**: exit properly the macro *(not use the red cross of the window)*

*(you can checked to {{false}} the variable **switch_setVisible_GBox_014_Main_Tools** for hidden the Box)*


<div class="mw-translate-fuzzy">

Una volta lanciata, la macro rimane attiva e la finestra rimane visibile. Per chiudere la macro si deve usare il pulsante **Exit**. Se si esce tramite il pulsante con la croce, la macro rimane in memoria ed i dati vengono visualizzati nel report di FreeCAD.


</div>


<div class="mw-translate-fuzzy">


<center>

Image:Macro_FCInfo_04.png\|La tabella dei dati può essere dislocata a destra, Image:Macro FCInfo 05.png\|o a sinistra con Vista combinata , o non dislocata, a piacere.


</center>





</div>



## Opzioni




<div class="mw-translate-fuzzy">

## Opzioni 

### Unità di misura utilizzate 

#### Lunghezza :

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.


</div>



#### Unità di lunghezza: 

km, hm, dam, m, dm, cm, **mm**, µm, nm, pm, fm, inch, link, foot, yard, perch, chain, furlong, mile, league, nautique.



#### Gradi angolari: 


<div class="mw-translate-fuzzy">

#### Angoli:

1.  **gradi sessadecimali**, esempio: 174.831872611°
2.  sessagesimali gradi primi secondi, es: 174° 49\' 54.741401\'\'
3.  radianti, es: 3.05139181449 rad
4.  centesimali, es: 194.257636235 gon
5.  pendenza %, es: 30° = 57.74%


</div>


<div class="mw-translate-fuzzy">

Visualizzazione degli angoli in FCInfo.


<center>

Image:Macro FCInfo 02.png\|Visualizzazione degli angoli in FCInfo. Image:Macro FCInfo 03.gif\|Visualizzazione della pendenza in FCInfo.
Clicca due volte sopra l\'immagine per vedere l\'animazione (l\'immagine deve essere in pieno schermo per vedere l\'animazione)


</center>





</div>


<center>

Image:Macro FCInfo 02.png\|Understanding of angles in FCInfo display Image:Macro FCInfo 03.gif\|Understanding of angles in percent in FCInfo display
click twice to see the animation (the image must be in full screen)


</center>






#### Unità di peso: 


<div class="mw-translate-fuzzy">

#### Peso:

tonne, quintal, kg, hg, dag, **grammo**, dg, cg, mg, µg, ng, pg, fg, gr (grain), dr (drachm), oz (once), oz t (once troy), lb t (livre troy), lb (livre av), st (stone), qtr (quarter), cwt (hundredweight), tonneau fr, ct
Il valore della massa volumica è preimpostato su **7,5** kg/dm3, che è la densità media dell\'acciaio. Per impostare un valore predefinito diverso, modificare il valore della densità nella riga 208:


</div>



#### Configurazione FCInfo 

-   Location : **Tools \> Edit parameter \> \*User parameter:BaseApp/Preferences/Macros/FCMmacros/FCInfo/**
-   **switchNotInfoOnBeginning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not this text information on run macro
        -   \[{{false}}\] = display this information

        -   
            {{true}}
            
            = this Information is Not displayed On Beginning
-   **switchVersionSearch** **\#** SetBool {{true}} or \[{{false}}\]
    -   Search if one new version exist on run macro
-   **switchWarning** **\#** SetBool {{true}} or \[{{false}}\]
    -   Display or not display the window warning in case not good selection
-   **switchCreatePoint** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create point checkBox
-   **switchCreateAxis** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create axis checkBox
-   **switchCreatePlane** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Create plane checkBox
-   **switchDisplayInfoObject** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the info checkBox
-   **switchClearDisplayReportView** **\#** SetBool {{true}} or \[{{false}}\]
    -   if switchClearDisplayReportView is {{true}} the ReportView is cleared
-   **seTWidgetPosition** **\#** SetBool {{true}} or \[{{false}}\]
    -   Check the Widget Position Left/Right checkBox
    -   if seTWidgetPosition \[{{false}}\] : if seTPositionFlyRightLeft = 2 = docked to Right
    -   if seTWidgetPosition {{true}} : if seTPositionFlyRightLeft = 3 = docked to Left
    -   if it is 1 the window macro is not docked
-   **switchBoundBoxCreateText** **\#** SetBool {{true}} or \[{{false}}\]
    -   Create the text dimension of the BoundBox
-   **seTBoundBoxTextHeigth** **\#** seTBoundBoxTextHeigth = 3.0
    -   Give the Heigth of the text dimension (independent of the seTTextHeigthValue)
-   **seTBoundBoxTextArround** **\#** seTBoundBoxTextArround = 3
    -   Give the arround of the text dimensions (independent of the seTDecimalValue)
-   **seTMemoClipBoard** **\#** SetInt \[0\], 1, 2, 3
    -   Give one value \[0\], 1, 2, 3 clipBoard
        -   \[0\] = desactivate the clipBoard
        -   1 = the data string is memorised to : FreeCAD.Vector( X, Y, Z )
        -   2 = the data string is memorised to : X, Y, Z
        -   3 = the data string is memorised to : X Y Z
-   **seTTextHeigthValue** **\#** SetInt 11
    -   Give one text heigth value of the macro
-   **seTDecimalValue** **\#** SetInt 4
    -   Give the number of decimal displayed
    -   If the number is -1 the total decimal value is displayed)
-   **seTMaterialCurrentIndex** **\#** SetInt 0
    -   Set the index of the ComboBox
-   **seTMaterialFileName** **\#** SetString FCInfo_material.txt
    -   Name of the material file
-   **seTMaterialSavePathName** **\#** SetString C:\\\...\\Macro\\FCInfo_material.txt
    -   Path name of the material file
-   **seTMaterialPrice** **\#** SetFloat
    -   Material price by Kg
-   **seTMaterialSuffixDevise** **\#** SetString
    -   Devise money
-   **seTMaterialSuffixCost** **\#** seTMaterialSuffixCost
    -   Suffix Devise cost
-   **seTMaterialCost** **\#** SetFloat
    -   Material cost
-   **seTDensiteValue** **\#** SetFloat 1.0
    -   Give the densite value
-   **seTDensiteDecimalNumber** **\#** SetInt 4
    -   Give the number of decimal for the densite value
-   **seTDensiteSingleStep** **\#** SetFloat 1.0
    -   Give the step for one click, by default 1.0 (possible 0.01 or \...)
-   **seTDensiteSuffixChain** **\#** SetString kg (by dm3)
    -   Choice your suffix string
-   **seTPositionFlyRightLeft** **\#** SetInt 2
    -   Choice your position, Fly, \[Right\], Left
        -   1 = the macro window is fly (not docked)
        -   \[2\] = the macro window is positioned to Right
        -   3 or other = the macro window is positioned to Left
-   **seTIndexUnitWeight** **\#** SetInt
    -   Set unit Weight index
-   **seTUnitSymbolMicro** **\#** U
    -   Set Symbol Micro
-   **seTUnitSymbolCube** **\#** 3
    -   Set Symbol Cube
-   **seTUnitSymbolCarre** **\#** 2
    -   Set Symbol Square
-   **seTIndexUnitLength** **\#** SetInt
    -   Set unit Length index
-   **setBSplineToByArcValue** **\#** SetFloat 0.00001
    -   Set unit for cut the BSpline for seack the radius on point given
-   **setMeshTopologyValue** **\#** SetFloat 0.1
    -   Set unit for create the Mesh to Shape
-   **switchBSplineCreateCircleConstructorAxis** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the axis of the circles (arcs) for create the BSpline
-   **switchBSplineCreateCircleConstructor** **\#**SetBool {{true}} or \[{{false}}\]
    -   Display the circles cretors for create the BSpline
-   **switchCreateLineDiVatNatOnClick** **\#**SetBool {{true}} or \[{{false}}\]
    -   Create the Line info on point (0,0,0) or on point mouse clicked (x,y,z) if it is {{true}}
    -   If it is {{true}} one \'\*\' is displayed in front of text. EX: \'\*Direction\'

This switch *(section GroupBox)* allows you to view only the desired section(s) (just visual) {{False}} or {{True}}.

All calculations are done without taking account of this option

-   section GroupBox begin
    -   **switch_setVisible_GBox_001_Document** = True (1)
    -   **switch_setVisible_GBox_002_Coordinate_Mouse** = True (1)
    -   **switch_setVisible_GBox_003_Color** = True (1)
    -   **switch_setVisible_GBox_004_Object_Mesh** = True (1)
    -   **switch_setVisible_GBox_005_Value_Unit** = True (1)
    -   **switch_setVisible_GBox_006_Inclination** = True (1)
    -   **switch_setVisible_GBox_007_Surface_and_Volume** = True (1)
    -   **switch_setVisible_GBox_008_Cost_And_Price** = True (1)
    -   **switch_setVisible_GBox_009_BoundBox** = True (1)
    -   **switch_setVisible_GBox_010_Center_Mass** = True (1)
    -   **switch_setVisible_GBox_011_Inertia** = True (1)
    -   **switch_setVisible_GBox_012_SpreadSheet** = True (1)
    -   **switch_setVisible_GBox_013_SpreadSheet_Creation** = True (1)
    -   **switch_setVisible_GBox_014_Main_Tools** = True (1)
-   section GroupBox end




<div class="mw-translate-fuzzy">

## Script

Copiare il contenuto della macro in un file chiamato \"FCInfo.FCMacro\"

-   Windows: di solito \"C:\\Utenti\\nome_utente\\AppData\\Roaming\\FreeCAD\\ \"

-   Ubuntu: di solito \"/home/nome_utente/.FreeCAD\".

Oppure, direttamente nell\'interfaccia di FreeCAD

L\'icona deve essere nella stessa directory della macro.

Scaricare l\'immagine posizionando il puntatore sull\'icona <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> e poi fare clic destro e selezionare \"Salva come\" (senza cambiare il nome).


</div>

Copy the contents of the macro in a file named \"FCInfo.FCMacro\"

-   Windows: the form is usually **\" drive:\\Users\\your_user_name\\AppData\\Roaming\\FreeCAD\\ \"**
-   Ubuntu: the form is usually **\" /home/your_user_name/.FreeCAD \"**.

Or, directly in the interface of FreeCAD
The icon must be in the same directory as the macro.
Download image positioning on the icon <img alt="" src=images/FCInfo.png  style="width:64px;"> <img alt="" src=images/FCInfoSpreadsheet.png  style="width:64px;"> and then drag the mouse right click \"save as\" (do not change the name)


<div class="mw-translate-fuzzy">

Dato che, per il momento, le pagine wiki accettano solo 64 KB e il file della macro è più grande, il suo codice è stato inserito nel forum.


</div>


<div class="mw-translate-fuzzy">

Scaricare il file **docked to right** [FCInfo_en_Ver_latest_Docked.FCMacro](https://gist.github.com/mario52a/8d40ab6c018c2bde678f). PySide


</div>


<div class="mw-translate-fuzzy">


{{CodeDownload|https://gist.github.com/mario52a/8d40ab6c018c2bde678f|Ultima versione di Macro_FCInfo}}


</div>


<div class="mw-translate-fuzzy">

Oppure scaricare **[Dal forum.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185&p=47748#p47748)**
**PS:** Questa macro utilizza il comando **getSelection()** e la lista degli oggetti comincia da 1 ex: per uno cubo **Edge1 to Edge12** e il codice dentro la console Python comincia da 0 ex: per uno cubo **Edge\[0\] fino Edge\[11\]**
Questo è normale il contatore della lista dentro OpenCascade comincia sempre da **1 e non da 0**


</div>



### Limitazioni


<div class="mw-translate-fuzzy">

### Limitazioni 

Uscire sempre dalla macro tramite il pulsante **Exit**, altrimenti il programma rimane in memoria e continua a funzionare fino a quando non si chiude FreeCAD.

La tabella riporta solo i primi 200 elementi dell\'oggetto, quando l\'oggetto contiene più di 200 elementi viene visualizzato l\'avviso **(! +200)**. In questo caso, l\'elenco completo dei dati è visibile nel file csv che può essere creato e salvato cliccando sul pulsante **Save**.


</div>


<div class="mw-translate-fuzzy">

Se dopo avere lanciato la macro la macro non e visibile, guardate a la base della finestra.


</div>

![](images/Macro_FCInfo_08.png )

![](images/FCInfo_begin_00.gif ) 


<div class="mw-translate-fuzzy">

**In progetto :**

~~leggere i dati direttamente in una tabella.~~ fatto

~~mappare dgli spigoli (\"Edges\") e le loro coordinate~~ fatto

associare una sostanza alla sua massa volumica

~~angoli di inclinazione riferiti all\'elemento piuttosto che all\'oggetto globale~~ fatto

~~alloggiamento a destra nell\'interfaccia di FreeCAD~~ fatto


</div>



## Versione

ver \"1.30\" 2025/01/02 : delette all reference to PySide PySide2 and QtWidgets modify the (Qt) Save file


```python
#
import PySide2
from PySide2 import QtGui , QtCore, QtWidgets
from PySide2.QtWidgets import QComboBox
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QTableWidget, QApplication
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

            OpenName, Filter = PySide2.QtWidgets.QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide2
```

replaced and change command by


```python
#
import PySide
try:
    from PySide import QtWidgets
    from PySide.QtWidgets import *
except Exception:
    None
from PySide import QtGui , QtCore
from PySide.QtGui import *
from PySide.QtCore import *

            OpenName, Filter = QFileDialog.getOpenFileName(None, u"Read a txt file", setPathLatestDirectory, "*.FCInfo *.csv *.asc *.txt;;FCInfo (*.FCInfo);;Cvs (*.csv);;Ascii (*.asc);;TXT (*.txt);;(*.*);;(*)")#PySide

```

ver \"1.29b\" 2024/05/10 **PySide2** modify Inertia \" MatrixX1\*uniteM to (MatrixX1\*uniteM) \" and adding spinBox inertia

-   [Moment of inertias calculation](https://forum.freecad.org/viewtopic.php?p=713935#p713935)
-   [Momentof Interia - FCInfo macro](https://forum.freecad.org/viewtopic.php?t=64653)

ver 1.29 2024/05/06 **french** version **fr PySide6** by sylvainbx <https://gist.github.com/sylvainbx/af09a30be3e1427de56305825331fb29> merci sylvainbx

ver 1.28b 1.28c 2023/10/30 orthographe

ver 1.28 01/09/2023 modify variable name, possibility hidden each sector, save data spreadSheet in document, surface radius, add button webWiki and webForum

ver 1.27 2023/06/30 optimize the styleSheet, correct the left/right position and restore view after edition sketcher 
```python
            self.PB_00_Decrement.setStyleSheet("background-color: white; border:2px solid rgb(215, 10, 22);")      # bord white and red
``` replaced by 
```python
            self.PB_00_Decrement.setStyleSheet("QPushButton {background-color: white; border:2px solid rgb(215, 10, 22)};")      # bord white and red
```


<div class="mw-translate-fuzzy">

-   ver 1.22 , 12/11/2020 : adesso la macro si disinstallare totalmente utilizzo :


</div>

-   ver 1.26b 20/02/2022 upgrade for detect BSpline in SubObject

-   ver 1.26 06/02/2022 add info on Mesh and Points objects, decode colours, duplicate object or subObject, memorize the latest path and other preferences options

-   ver 1.25e 18/12/2021 add info detailed to BSpline (ToByArcs) and info \"sel\[0\].TypeId\"
-   ver 1.25d 12/12/2021 \-\--
-   ver 1.25c 12/12/2021 correct \"strAround((\" by \"str(Around(\" and other little \...
-   ver 1.25b 11/12/2021 correction error in change/modify new material and reorganization
-   ver 1.25 10/12/2021 PySide2 and add comboBox materials
-   ver 1.24 02/12/2021 add [adjustedGlobalPlacement](https://forum.freecadweb.org/viewtopic.php?f=22&t=59852) modified by edwilliams16 for placement with Body, boundbox tracing
-   ver 1.23cb 25/11/2021 delete **\"import Sketcher \* \"** create conflict with \"**open(OpenName, \"r\")**\" ??

Adding 
```python
FreeCAD.ActiveDocument.openTransaction(u"FCInfo")    # memorise les actions (avec annuler restore)
FreeCAD.ActiveDocument.commitTransaction()           # restore les actions  (avec annuler restore)
#FreeCAD.ActiveDocument.abortTransaction()            # abandonne les actions(avec annuler restore)
```

-   ver 1.25d, 13/12/2021 little correction material field uncomment the \"\'try\...Except\" !!!
-   ver 1.25c, 12/12/2021 little correction new material
-   ver 1.23b, 20/11/2021 little correction, add text info in beginning run macro, and ordinal the text code
-   ver 1.23 , 19/11/2021 include icon in macro, number decimal displayed, text height, configure options in the Preference FC, correct info for elements of sketch in edit mode.
-   ver 1.22 , 12/11/2020 : now the macro is totally uninstalled i use :


```python
try:
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)    # destroy
        self.window.deleteLater()                                     # destroy
        self.window.destroy()                                         # destroy
except Exception:
        None
```

[How do i exit from FreeCAD instead of Python?](https://forum.freecadweb.org/viewtopic.php?f=22&t=48013#p411508)

instead: 
```python
self.window.hide()
``` e aggiungendo la possibilità di visualizzare o meno la finestra \"Error Message\" \"Falso\" per impostazione predefinita, se si attiva la finestra di avviso vai a 
```python
FreeCAD >Menu >Tools >Edit parameters... >BaseApp/Preferences/Macros/FCMmacros/FCInfo > switchWarning
```


<div class="mw-translate-fuzzy">

-   ver 1.21-3.01 , 07/11/2019 \# 07/11/2019 ver \"01.21-3-rmu\" replace character micro = \"U\", square = \"2\", cube = \"3\", degrees = \" deg\" see \"<https://forum.freecadweb.org/viewtopic.php?f=3&t=6005&start=70#p345819>\"

-   ver 1.21-2.01 (1.21-rmu) 11/06/2019 rmu replace all characters over 127 in ex: \"°\" in chr(176)) #degree

ver 1.21.01 (1.21-rmu) 30/05/2019 rmu change fixed positions to qt layouts grid.addWidget() by rmu75 see the rmu75 fork \"<https://gist.github.com/rmu75/b165147bd1c2f2659c014103793ae1d8>\"

ver 1.21 , 16/04/2019 optimization for Py 3\... Qt 5\... FreeCAD 0.15 to 0.19 release

ver 1.20 , 29/01/2018 optimization

ver 1.19 , 20/01/2018 create checkBox for use detection all elements of the object if wanted or not , the macro is faster. Optimisation

ver 1.18 , 19/12/2017 \...

ver 1.17c , 14/12/2017 create plane with coordinate give in one project in other project and replace \"FCInfo\" by \"\_\_title\_\_\"

ver 1.17b , 13/12/2017 little correction replace FCTreeView to FCInfo

ver 1.17 , 12/12/2017 add upgrade Moment of inertia mm and kg by pinq [FCMacro and moment of inertia of assembly](https://forum.freecadweb.org/viewtopic.php?t=23888), and create plane, axis, point, and add options separator for spreadsheet

ver 1.16 , 21/06/2017 aggiunto controllo della altezza della pollice (qui PointSize 8), casella di posizione della finestra della macro sinistra o destra e nuovo sistema di ricerca del imposta mento delle macro
ver 1.15 , 19/12/2015 soppressione PyQt4 option [see](http://forum.freecadweb.org/viewtopic.php?f=12&t=13541) , add checkBox for editing infos in report view
ver 1.14 , 04/08/2014 PyQt4 and PySide, corretto tooltip che non funzionava con PySide, aggiunto \"fg\"

ver 1.13 , 27/07/2014 sostituzione FCInfo_en_Ver_1-12_Docked.FCMacro con FCInfo_en_Ver_1-13_Docked.FCMacro accetta PyQt4 and PySide

ver 1.12 , 10/03/2014 aggiunto tooltip sopra i pulsanti

ver 1.11 , 04/03/2014 aggiunto µm, nm, pm, fm, µg, ng, pg, percento, correzione dell\'errore carat ~~\"cd\"~~ con **\"ct\"**, visualizzazione dell\'etichetta e del nome interno, correzione del calcolo degli angoli XY YZ ZX, funzionava bene su un oggetto semplice, ma ha dato un valore sbagliato su un pezzo composto (ha preso altre coordinate ! scoperto confrontando la tabella e le coordinate visualizzate nella sezione inclinazioni), finestra mobile o ancorabile in qualsiasi parte della GUI di FreeCAD
ver 1.10b, 19/11/2013 pulsanti esterni alla scrollbar e bloccaggio delle dimensioni della finestra

ver 1.10 , 18/11/2013 agggiunto una scrollbar per diminuire la dimensione della finestra

ver 1.08b 10/10/2013 correzione dell\'errore di superficie delle facce elencati nella tabella e sostituzione di \"**print**\" con \"**App.Console.PrintMessage**\"

~~ver 1.09 , 04/11/2013 funziona perfettamente su Windows e Linux (causa dell\'errore i caratteri : ² ³ ° \" ordinal not in range (128)\")~~

ver 1.08 , 24/10/2013 correzione della mappa dei titoli \"Faces\" e \"Edges\" sopra 100 objeti

ver 1.07 , 11/10/2013 mappare gli spigoli (\"Faces\") e le loro coordinate.

ver 1.06 , 22/09/2013 mappare gli spigoli (\"Edges\") e le loro coordinate, angoli di inclinazione riferiti all\'elemento piuttosto che all\'oggetto globale

ver 1.05 , 17/09/2013 aggiunto un\'icona per il foglio di calcolo, conversione in tonneau fr, dà le dimensioni fuori tutto invece di dare le coordinate.

ver 1.04 , 11/09/2013: leggere i dati direttamente in una tabella.

ver 1.03 , 09/09/2013: visualizzazione più chiara nella \"vista report\" e sostituzione di \"typeObject = sel\[0\].Shape.ShapeType\"

ver 1.02 , 7/09/2013 : piccole modifiche

ver 1.0 , 6/09/2013


</div>



## Link

Vedere anche: <img alt="Arch Survey" src=images/Arch_Survey.svg  style="width:36px;"> [Arch: Ispeziona](Arch_Survey/it.md)

Si può commentare questa macro nel forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)
Qui uno altro post ché parla di [FCInfo Macro](http://forum.freecadweb.org/viewtopic.php?f=8&t=6005)



---
⏵ [documentation index](../README.md) > Macro FCInfo/it
