# Navigation Cube/de
{{TOCright}}



## Einleitung


<div class="mw-translate-fuzzy">

Die Navigationswürfelsteuerung, oder **Navigationswürfel**, ist eine grafische Hilfe der Benutzeroberfläche zur Neuausrichtung der 3D Ansicht. Standardmäßig ist es sichtbar und befindet sich in der oberen rechten Ecke der 3D Anzeige. Wenn Du dir die Standard 3D Ansicht ansiehst, sieht es wie folgt aus:


</div>

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

Der Navigationswürfel besteht aus einer Anzahl mehrerer Teile:

-   Richtungspfeile
-   Hauptnavigationswürfel
-   Mini-Würfel Menü


</div>

All parts, except the axis indicators, can be clicked.



## Anwendung

### Main cube 

The main cube has 26 faces: 6 main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.




<div class="mw-translate-fuzzy">

## Richtungspfeile


</div>


<div class="mw-translate-fuzzy">

Es gibt sechs Richtungspfeile: vier dreieckige Pfeilspitzen, eine oben, unten, links und rechts; und zwei gebogene Pfeile, eine auf beiden Seiten des oberen Pfeils.


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.




<div class="mw-translate-fuzzy">

## Miniwürfelmenü


</div>


<div class="mw-translate-fuzzy">

In unteren rechten Ecke des Navigationswürfels befindet sich ein kleiner Würfel. Der Typ der Ansicht (orthographic, perspektivisch oder isometrisch) kann in einem Menü geändert werden, wenn man auf diesen Würfel klickt. Damit wird auch die Ansicht auf die Fenstergröße angepasst.


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## Verschieben der Navigationswürfeldarstellung 

Du kannst die gesamte Navigationswürfelkontrollstruktur an eine andere Stelle in der 3D Darstellung verschieben, indem du die Maus an einer beliebigen Stelle im Hauptnavigationswürfels drückst und ziehst. Die Struktur beginnt sich erst dann zu bewegen, wenn der Mauszeiger den Rand des Hauptnavigationswürfels hinter sich gelassen hat.


</div>



### Einstellungen


<div class="mw-translate-fuzzy">

Der Navigationswürfel ist konfigurierbar, einschließlich der Anpassung seiner Größe: **Bearbeiten → Einstellungen... → Anzeige → Navigation → Navigationswürfel** {{Version/de|0.19}}.


</div>

### Advanced parameters 

Some advanced Navigation Cube parameters cannot be changed in the [Preferences Editor](Preferences_Editor#Navigation.md). These parameters can be set manually in the [Parameter editor](Std_DlgParameter.md) or via the [CubeMenu external workbench](Interface_Customization#CubeMenu.md). Changes will become visible when a new 3D view is created (with [Std New](Std_New.md), [Std Open](Std_Open.md) or [Std ViewCreate](Std_ViewCreate.md)).

To manually set colors:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New unsigned item** from the context menu.
4.  Enter the name of one of these colors:
    -   
        **BorderColor**
        
        : the lines separating the cube faces, default is {{Value|4281479730}} (hex: {{Value|ff323232}}).

    -   
        **ButtonColor**
        
        : all elements around the cube, default is {{Value|2162354671}} (hex: {{Value|80e2e9ef}}).

    -   
        **FrontColor**
        
        : all cube faces, default is {{Value|3236096495}} (hex: {{Value|c0e2e9ef}}).

    -   
        **HiliteColor**
        
        : the cube or arrow face that is currently highlighted, default is {{Value|4289389311}} (hex: {{Value|ffaae2ff}}).

    -   
        **TextColor**
        
        : the text on the cube faces, default is {{Value|4278190080}} (hex: {{Value|ff000000}}).
5.  The color value must be entered as a 32-bit unsigned integer. Translated to the hexadecimal format this integer has the form {{Value|AARRGGBB}}. Where {{Value|AA}} stands for the alpha channel (a measure for the transparency), and the other three digit pairs stand for red, green and blue. To convert a hexadecimal value to an unsigned integer you can use the [Python console](Python_console.md), enter for example {{Incode|int("ff323232", 16)}}, or an online service such as [this one](https://cryptii.com/pipes/integer-encoder).
6.  Optionally set more colors.
7.  Press the **Close** button.

To manually set the border width:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New float item** from the context menu.
4.  Enter the name **BorderWidth**, {{Value|default is 1.1}}.
5.  Enter the width.
6.  Press the **Close** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/de
