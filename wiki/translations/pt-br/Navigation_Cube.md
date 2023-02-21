# Navigation Cube/pt-br
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

O controle do cubo de navegação, ou *\'cubo de navegação*, é uma ajuda gráfica de interface com o usuário para reorientar a visualização 3D. Por padrão, ele é visível e reside no canto superior direito da tela 3D. Se você estiver olhando para a vista 3D padrão, ela se parece com o seguinte:


</div>

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

O cubo de navegação é composto de várias partes:

-   Setas direcionais
-   Cubo de navegação principal
-   Menu mini-cubo


</div>

All parts, except the axis indicators, can be clicked.

## Usage

### Main cube 

The main cube has 26 faces: 6 main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.




<div class="mw-translate-fuzzy">

## Setas direcionais 


</div>


<div class="mw-translate-fuzzy">

Há seis setas direcionais: quatro setas triangulares, na parte superior, inferior, esquerda e direita; e duas setas curvas, uma de cada lado da seta superior.


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.




<div class="mw-translate-fuzzy">

## Menu mini-cubo 


</div>


<div class="mw-translate-fuzzy">

No canto inferior direito do cubo de navegação está um pequeno cubo. Clicando neste cubo, aparecerá um menu que você pode usar para mudar o tipo de vista (Ortográfica, Perspectiva, Isométrica) e para \"Zoom to Fit\".


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## Movendo a exibição do cubo de navegação 

Você pode mover toda a estrutura de controle do cubo de navegação para outro local na tela 3D, pressionando o mouse em qualquer lugar no cubo de navegação principal e arrastando. A estrutura não começará a se mover até que o ponteiro do mouse tenha passado a borda do cubo de navegação principal.


</div>

### Preferences


<div class="mw-translate-fuzzy">

O cubo de navegação é configurável, incluindo o ajuste de seu tamanho: **Editar → Preferências... → Tela → Navegação → Cubo de Navegação ** <small>(v0.19)</small> .


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
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/pt-br
