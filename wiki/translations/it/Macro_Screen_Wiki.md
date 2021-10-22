# Macro Screen Wiki/it
{{Macro/it
|Name=Macro Screen Wiki
|Icon=Macro_Screen_Wiki.png
|Description=Macro speciale per Wiki Worker. Questa macro consente di salvare la vista 3D nel formato desiderato. La vista 3D o la finestra 3D completa di FreeCAD assume le dimensioni desiderate. Una rotazione dell'oggetto selezionato o della vista 3D è possibile dare un angolo di rotazione il numero di immagini viene calcolato automaticamente è possibile dare un angolo di partenza e un angolo di arrivo. È necessario utilizzare un altro programma di esempio Gimp per assemblare le immagini e creare il file animato.
|Author=Mario52
|Version=00.05
|Date=2021/05/21
|FCVersion=0.19
|Download=Telecarica l'icon [https://wiki.freecadweb.org/images/f/f5/Macro_Screen_Wiki.png Macro_Screen_Wiki.png] e copia il file dentro lo stesso repertorio delle macro
|SeeAlso= <img src="images/Macro_Copy3DViewToClipboard.png" width=24px>[Macro_Copy3DViewToClipboard](Macro_Copy3DViewToClipboard.md)<br/><img src="images/Snip.png" width=24px> [Macro_Snip](Macro_Snip.md)
}}

## Descrizione

Macro speciale per Wiki Worker. Questa macro consente di salvare la vista 3D nel formato desiderato. La [vista 3D](3D_view/it.md) o la finestra 3D completa di FreeCAD assume le dimensioni desiderate. Una rotazione dell\'oggetto selezionato o della vista 3D è possibile dare un angolo di rotazione il numero di immagini viene calcolato automaticamente è possibile dare un angolo di partenza e un angolo di arrivo. È necessario utilizzare un altro programma di esempio Gimp per assemblare le immagini e creare il file animato.


{{Codeextralink|https://gist.githubusercontent.com/mario52a/61571ce0bd41af0471995df7c3ea855f/raw/4fdc5b2db7ed3ed062a2575637e035f728b2e40d/Macro_Screen_Wiki.FCMacro}}

![](images/Macro_Screen_Wiki_00.png )



*Macro Screen Wiki Immagine e finestra di configurazione*

![](images/Macro_Screen_Wiki_01.png )



*Finestra Rotazione Wiki schermo macro*

## Uso

### Images options 

#### Definition

1.  
    {{RadioButton|400x200}}
    

2.  
    {{RadioButton|TRUE|600x400}}(Default)

3.  
    {{RadioButton|1024x768}}
    

4.  
    {{RadioButton|320x240 (QVGA)}}
    

5.  
    {{RadioButton|320x480 (HVGA)}}
    

6.  
    {{RadioButton|400x300}}
    

7.  
    {{RadioButton|480x360}}
    

8.  
    {{RadioButton|640x480 (VGA)}}
    

9.  
    {{RadioButton|768x576 (PAL)}}
    

10. 
    {{RadioButton|800x600 (SVGA)}}
    

11. 
    {{RadioButton|960x720}}
    

12. 
    {{RadioButton|1024x768 (XGA)}}
    

#### Format image 

1.  
    {{SpinBox|600 px}}Length (Impostato: 600 px)

2.  
    {{SpinBox|400 px}}Height (Impostato: 400 px)

#### Window

1.  
    {{RadioButton|Window FC}}: Il completo FreeCAD window

2.  
    {{RadioButton|TRUE|Screen 3D}}: La vista 3D di FreeCAD

#### BackGround Color 

1.  
    {{RadioButton|TRUE|Current}}(Default)

2.  
    {{RadioButton|Color}}
    

3.  
    {{RadioButton|Transparent}}
    

4.  
    **Restore**
    

#### Commando

1.  
    **Set Screen**: Docked finestra

2.  
    **Tile Screen**: Finestra volante

3.  
    **Save Image**: Salva l\'immagine ex: {{FileName|imageBox_000.png}} (il \_000 e sempre aggiunto)

4.  
    **Follow**: Dopo aver salvato la prima immagine, premere questo pulsante se si desidera salvare l\'immagine successiva con lo stesso nome. Le immagini salvate vengono incrementate ex: {{FileName|imageBox_001.png}}, {{FileName|imageBox_002.png}}, {{FileName|imageBox_003.png}}, etc. ..

5.  
    **New image**: Salva una nuova immagine senza modificare il contatore

6.  
    **Rotation**: Accesso al menu di rotazione (il titolo della sezione

\"Image options\" cambia in \"Rotation options\")

1.  
    **Quit**: \_\_\_Screen\_Wiki end\_\_\_\_\_\_\_\_\_\_

2.  
    **ToolBar**: Riduci la finestra dell\'immagine in una barra degli strumenti, l\'opzione **Rotation** non è disponibile in questa modalità

    1.  ![](images/Macro_Screen_Wiki_ToolBar_01.png )![](images/Macro_Screen_Wiki_ToolBar_02.png )![](images/Macro_Screen_Wiki_ToolBar_03.png )![](images/Macro_Screen_Wiki_ToolBar_04.png )
    2.  The button **[[Image:Macro_Screen_Wiki_ToolBar_04_6.png]]** Flip/Flop S/N la mini barra degli strumenti ![](images/Macro_Screen_Wiki_ToolBar_Mini.png )

### Rotation options 

#### Rotation on 

1.  
    {{RadioButton|3D View}}: La vista completa viene ruotata

2.  
    {{RadioButton|TRUE|Object}}: L\'oggetto selezionato viene ruotato

#### Axis

:   
    {{RadioButton|TRUE| {{ColoredText||red|'''X'''}}}}: Rotation on X axis

:   
    {{RadioButton| {{ColoredText||Green|'''Y'''}}}}: Rotation on Y axis

:   
    {{RadioButton| {{ColoredText||Blue|'''Z'''}}}}: Rotation on Z axis

:   
    {{RadioButton| {{ColoredText||#995500|'''D'''}}}}: Rotazione su una direzione, per utilizzare questa opzione, selezionare prima l\'oggetto, secondo: la linea guida del filo. Se {{RadioButton|TRUE|{{ColoredText||#995500|'''D'''}}}} è selezionato e nessun filo è selezionato, la direzione è `Vector(0, 0, 0)`

#### Point Rotation BoundBox 

1.  Object : Rotazione sul centro BoundBox dell\'oggetto selezionato
2.  Sub Object : Rotazione sul centro BoundBox dell\' secondo oggetto selezionato

#### Angles

-   Angle Rotation

1.  
    **-**: Ridurre il valore di 10 gradi

2.  
    {{SpinBox|0 Degrees}}: Valore

3.  
    **+**: Aumenta il valore di 10 gradi

-   Number images : Viene calcolata l\'immagine numerica salvata con i valori indicati (approssimazione + 1)
-   Angle Begin Rotation

1.  
    **-**: Ridurre il valore di 10 gradi

2.  
    {{SpinBox|0 Degrees}}: Valore : Angolo della rotazione iniziale

3.  
    **+**: Aumenta il valore di 10 gradi

-   Angle End Rotation

1.  
    **-**: Ridurre il valore di 10 gradi

2.  
    {{SpinBox|360 Degrees}}: Valore : Angolo della rotazione finale

3.  
    **+**: Aumenta il valore di 10 gradi

#### Command

-   Delay between 2 images

1.  
    {{SpinBox|0,00|Delay second}}: Se hai problemi con il salvataggio dell\'immagine (computer troppo veloce) dai un valore \...

2.  
    {{CheckBox|Reverse}}: Checked, questa opzione inverte la vista 3D o l\'oggetto di rotazione

3.  
    {{CheckBox|TRUE|Original position}}: Questa opzione ripristina la posizione originale della vista 3D o dell\'oggetto ruotato. In caso contrario, la vista 3D o l\'oggetto rimangono nell\'ultima posizione della rotazione

4.  
    **Save the animation**: Salva l\'animazione

## Esempio immagini 

![](images/Macro_Screen_Wiki_03_Set_Screen.png )



*Mode Set Screen 640 px x 400 px*

![](images/Macro_Screen_Wiki_04_Tile_Screen.png )



*Mode Tile Screen 640 px x 400 px ad esempio: sposta la finestra. L'immagine viene salvata nello stesso modo ché Set Screen qui sopra*

![](images/Macro_Screen_Wiki_Object_Direction_Object.gif )



*Modalità animazione Oggetto selezionato e direzione BoundBox center Object. <br/> Le immagini devono essere assemblate con un altro programma per creare un GIF animato<br/>Esempio [https://www.gimp.org/downloads/ Gimp] o [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_Object_Direction_SUBObject.gif )



*Oggetto di animazione Direzione oggetto selezionato. <br/> Le immagini devono essere assemblate con un altro programma per creare un'animazione GIF<br/>Example [https://www.gimp.org/downloads/ Gimp] or [https://www.screentogif.com ScreenToGif]*

![](images/Macro_Screen_Wiki_07.png )



*La finestra di FreeCAD ridimensionata. La dimensione può essere diversa dalla definizione (dipende dal Widget, dalla barra del titolo ... utilizzata)*

## Versione

Version=00.05: 2021/05/21 : adding code in Save file section for Linux Mint QFileDialog ignore the extension. Only the Path+name is displayed


```python
global switchQFileDialogMint
                ####  mint
                if switchQFileDialogMint == True:   #
                    Filter = Filter[Filter.find("."):Filter.find(")")]
                    SaveName = SaveName + Filter
                ####  mint
```

Version=00.04: 2021/01/13 : adding mini ToolBar

Version=0.03: 2020/10/30 : create a tool bar for the image and new button for unique image

Version=0.02: 2020/05/04 : correct bug color button (self.PB\_01\_Color obsolete)

Versione=0.01 : 2020/03/21 :

---
[documentation index](../README.md) > Macro Screen Wiki/it
