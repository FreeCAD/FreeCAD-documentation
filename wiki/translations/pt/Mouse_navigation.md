# Mouse navigation/pt
## Overview

Os **estilos de navegação** do FreeCAD consistem nos comandos usados para navegar visualmente no espaço 3D e interagir com os objetos mostrados. O FreeCAD suporta múltiplos estilos de navegação. O predefinido é o chamado [Navegação CAD](#CAD_navigation.md), e é muito simples e prático, mas o FreeCAD também disponibiliza estilos de navegação alternativos, que pode escolher de acordo com as suas preferências. O estilo escolhido fica activado para todas as Bancadas de trabalho.

Para mais informação sobre selecção de objectos ver [Métodos de selecção](Selection_methods/pt.md).

Para mais informação sobre manipulação de objectos ver [Std TransformManip](Std_TransformManip/pt.md).



## Seleccionar uma forma de navegação 

1.  Escolher de entre os seguintes passos:
    -   Clicar no **[<img src=images/NavigationCAD_dark.svg style="width:16px">** botão na [Barra de estado](Status_bar/pt.md).
    -   Clicar com o lado direito do rato numa zona vazia na [Vista 3D](3D_view/pt.md), e seleccionar **Navigation styles** a partir do Menu de contexto.
    -   Usar o [Editor de preferências](Preferences_Editor/pt#Navigation.md). No menu seleccione **Edit → Preferences** e depois **Display → Navigation → 3D Navigation**.
2.  Seleccione um dos estilos da lista.
3.  Opcionalmente mudar o **Orbit style**: clicar no **[<img src=images/NavigationCAD_dark.svg style="width:16px">** botão na [Barra de estado](Status_bar/pt.md) e depois escolher **Settings → Orbit style**. Ver [Editor de preferências](Preferences_Editor/pt#Navigation.md).
4.  Opcionalmente mudar o **Rotation mode**. Ver [Editor de preferências](Preferences_Editor/pt#Navigation.md).
5.  Se o **CAD** estilo de navegação está seleccionado: opcionalmente mudar a **Enable animation** definição. Ver [Editor de preferências](Preferences_Editor/pt#Navigation.md).



## Estilos de navegação disponíveis 

With all navigation styles, unless selecting objects from a sketch in edit mode, you must hold **Ctrl** to select multiple objects.

The following keyboard options are available for all styles:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.




<div class="mw-translate-fuzzy">

### Navegação Blender 


</div>

Este estilo de navegação foi adoptado depois do [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">


{{Blender Navigation
|Select_name=Seleccionar
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rodar vista
|Shift=**Shift**
|Select_text=Clique com o botão esquerdo do rato no objecto que quer seleccionar.
|Pan_text=Mantenha pressionado o **Shift** e o botão do meio do rato e mova o cursor.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the middle mouse button, then move the pointer.

|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer.
}}



### Navegação CAD 

Este é o estilo de navegação predefinido. Permite ao utilizador um controlo simples da visualização e não requer o uso do teclado excepto para fazer múltiplas seleções.


<div class="mw-translate-fuzzy">


{{CAD Navigation
|Select_name=Seleccionar
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rodar vista<br>primeiro método
|Rotate_view_alt_name=Rodar vista<br>Método alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Clique com o botão esquerdo do rato no objecto que quer seleccionar.
</div>

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

Se soltar os botões do rato antes de parar o movimento do mesmo a vista 3D continua a girar, caso essa função esteja activada.

<div class="mw-translate-fuzzy">
Um duplo clique com o botão do meio do rato define um novo centro de rotação.
|Rotate_view_mode_text=Modo de rotação: Mantenha pressionada a tecla **Shift**, clique o botão direito do rato uma vez e mova o cursor.
|Rotate_view_alt_text=Mantenha pressionado o botão do meio do rato, a seguir mantenha pressionado o botão direito do rato e mova o cursor.
</div>

|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Com este método o botão do meio do rato pode ser solto depois do botão direito estar pressionado.

<div class="mw-translate-fuzzy">
Utilizadores que usem o rato com a mão direita podem achar este método mais fácil que o primeiro.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.

\|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

\|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

\|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. }}



### Navegação por Gestos 

Este estilo foi adequado ao uso com um ecrã táctil e caneta. No entanto pode também ser usado com um rato, e é recomendado para usar num MAC com trackpad.


<div class="mw-translate-fuzzy">


{{Gesture Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rodar vista
|Tilt_view_name=Inclinar vista
|Select_text=Clique com o botão esquerdo do rato no objecto que quer seleccionar.
|Select_gesture_text=Toque para seleccionar.
|Pan_text=Mantenha pressionado o botão direito do rato e mova o cursor.
|Pan_gesture_text=Arraste com dois dedos.
</div>

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

<div class="mw-translate-fuzzy">
Para definir o ponto de foco da câmera para rotação, clique num ponto com o botão do meio do rato. Como alternativa, aponte o cursor para um ponto e pressione a tecla **H** do teclado.
|Rotate_view_gesture_text=Arraste com um dedo para girar.
</div>

|Pan_text=Hold the right mouse button, then move the pointer.

|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways.

|Select_gesture_text=Tap to select.

|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

|Rotate_view_gesture_text=Drag with one finger to rotate.

<div class="mw-translate-fuzzy">
Mantenha pressionada a tecla **Alt** se estiver na [Bancada de trabalho de Esboço](Sketcher_Workbench/pt.md).
|Tilt_view_text=Mantenha os botões esquerdo e direito do rato pressionados e mova o cursor para os lados. 
|Tilt_view_gesture_text=Rodar dois pontos de toque.
</div>

|Pan_gesture_text=Drag with two fingers.

<div class="mw-translate-fuzzy">
Como alternativa, toque e segure, depois arraste. Isto simula o Pan com o lado direito do rato.
|Zoom_text=Use a roda do rato para aproximar ou afastar (zoom in/out).
|Zoom_gesture_text=Arraste dois dedos juntando-os ou afastando-os.
|Rotate_view_text=Mantenha pressionado o botão esquerdo do rato e mova o cursor. 
Na [Bancada de trabalho de esboço](Sketcher_Workbench/pt.md) e outros modos de edição, este comportamento está desactivado. Mantenha premida a tecla **Alt** quando pressiona o botão do rato para entrar no modo de rotação.
</div>

|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

<div class="mw-translate-fuzzy">
Na versão v0.18 este método está desactivado por defeito. Para o activar vá ao **Edit → Preferences → Display**, e desmarque a caixa "Disable touchscreen tilt gesture".
}}


</div>



### Navegação por Gestos no Maya 

Na navegação por gestos no Maya, o Pan, o Zoom e rodação da vista requerem as teclas **Alt** em simultâneo com um botão do rato, como tal é preciso um rato com 3 botões. Também é possível usar gestos, que esta forma de navegar foi desenvolvida sobre o estilo [Navegação por Gestos](#Gesture_navigation/pt.md)


<div class="mw-translate-fuzzy">

In Maya-Gesture Navigation, all view movements are activated pressing **ALT** and a mouse button, so that it will be needed to have a 3 button mouse in order to correctly use this navigation mode. Alternately it\'s possible to use gestures as this mode was been developed over the normal Gesture Navigation mode. {{MayaGesture Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Alt=**Alt**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.
|Zoom_text=Hold **Alt** and the right mouse button, then move the pointer.

Alternatively, use the mouse wheel to zoom in and out.
|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.
}}


</div>

\|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Alt** and the right mouse button, then move the pointer.

\|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.

\|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.

\|Tilt_view_text=Hold **Alt** and both left and right mouse buttons, and then move the pointer sideways. }}

### OpenCascade navigation 

The OpenCascade navigation style was modeled after [OpenCascade](https://www.opencascade.com/).


{{OpenCascade Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Ctrl=**Ctrl**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Ctrl** and the left mouse button, then move the pointer.

|Rotate_view_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Alternatively, hold **Ctrl** and the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer. It is possible to hold **Ctrl**.
}}

### OpenInventor navigation 


<div class="mw-translate-fuzzy">

### Navegação Inventor 

Na Navegação Inventor, criada a partir do [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) (não confundir com Autodesk Inventor), não existe seleção apenas com o rato. Para poder selecionar objetos, é necessário pressionar a tecla **CTRL**. {{OpenInventor Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Ctrl=**Ctrl**
|Select_text=Hold **Ctrl**, then press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then press and hold the left mouse button, then move the pointer. 
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}


</div>

This style is not based on Autodesk Inventor.


{{OpenInventor Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

Hold **Ctrl** instead to select multiple objects.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

|Rotate_view_text=Hold the left mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.
}}

### OpenSCAD navigation 

The OpenSCAD navigation style was modeled after [OpenSCAD](https://openscad.org/).


{{OpenSCAD_Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

{{VersionMinus|0.21}} Hold **Ctrl** and **Shift** when pressing the mouse button to drag an object in a sketch in edit mode.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then move the pointer.

Or hold **Shift** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold the left mouse button, then move the pointer.

Alternatively, and when a sketch is in edit mode, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

|Pan_text=Hold the right mouse button, then move the pointer.
}}

### Revit navigation 

The Revit navigation style was modeled after [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


{{Revit Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, then move the pointer.
}}

### TinkerCAD navigation 

The TinkerCAD navigation style was modeled after [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


{{TinkerCAD Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Press the right mouse button, then move the pointer.

|Pan_text=Hold the middle mouse button, then move the pointer.
}}




<div class="mw-translate-fuzzy">

### Navegação Touchpad 


</div>

With the Touchpad navigation style, panning, zooming, and rotating the view require a modifier key together with the touchpad. This style can also be used with a mouse.


<div class="mw-translate-fuzzy">

Na Navegação Touchpad, não pode fazer \"pan\", nem zoom, nem rodar a vista, apenas com o rato (ou touchpad). {{Touchpad Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold **Shift**, then move the pointer.
|Zoom_text=Use **PageUp** and **PageDown** to zoom in and out.
|Zoom_alt_text=Alternatively, hold **Shift** and **Ctrl**, then move the pointer.
|Rotate_view_text=Hold **Alt**, then move the pointer.
|Rotate_view_alt_text=Alternatively, hold **Shift** and the left button, then move the pointer.
}}


</div>

\|Ctrl=**Ctrl** \|Shift=**Shift** \|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Hold **Ctrl** and **Shift**, then move the pointer.

\|Rotate_view_text=Hold **Alt**, then move the pointer.

Alternatively, hold **Shift** and the left button, then move the pointer.

\|Pan_text=Hold **Shift**, then move the pointer. }}



## Suporte de Hardware 


<div class="mw-translate-fuzzy">

O FreeCAD também suporta alguns [3D input devices](3D_input_devices.md).


</div>

## Recommended navigation for macOS 

On MacBooks with a trackpad the Gesture navigation works very well, but the gestures have a special meaning:

-   Zoom: drag with two fingers.
-   Rotate: drag with three fingers.
-   Pan: **Ctrl** + three fingers.



---
⏵ [documentation index](../README.md) > Mouse navigation/pt
