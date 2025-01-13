# Mouse navigation/pt-br
## Visão Geral 

A navegação no FreeCAD consiste em uma combinação de comandos usados para navegar visualmente no seu espaço 3D e com isso interagir com os objetos exibidos. O FreeCAD suporta diversos estilos de navegação com o mouse. O estilo de navegação padrão é chamado de [Navegação CAD](#CAD_navigation.md), e ele é muito simples e prático, porém o FreeCAD também oferece outros estilos de navegação que podem ser usados com alternativa, caso você esteja habituado com algum outro programa. O estilo que escolher será usado para todos os bancadas de trabalho.

Para mais informações sobre a seleção de objetos, consulte [Métodos de seleção](Selection_methods/pt-br.md).

Para mais informações sobre manipulação de objetos, consulte o comando[ **Transformar**](Std_TransformManip/pt-br.md).



## Selecionando um estilo de navegação 

1.  **Selecionando um estilo de navegação:**
    -   Para acesso rápido clique no **[<img src=images/NavigationCAD_dark.svg style="width:16px">** botão de seleção na [Barra de status](Status_bar/pt-br.md).
    -   Clique com o botão direito do mouse em uma área vazia da [visualização 3D](3D_view.md) e selecione **Estilos de navegação** no Menu de Contexto.
2.  **Para definir seu estilo de navegação nas [Preferências](Preferences_Editor/pt-br#Navegação.md) do Freecad:**
    -   Vá na barra de menu, clique em **Editar → Preferências** e depois no icone **'''Tela''' → escolha a aba '''Navegação''' → Em '''Navegação 3D'''**. Então, clique na **seta para baixo** para abrir o menu de contexto e escolha a sua configuração preferida.![](images/Preferences_Display_Tab_Navigation.png )
3.  Se preferir, altere o **Estilo de órbita**: pressione o botão **[<img src=images/NavigationCAD_dark.svg style="width:16px">** na [barra de status](Status_bar.md) e depois escolha **Configurações → Estilo de órbita**. Consulte o [Editor de Preferências](Preferences_Editor#Navigation.md).
4.  Caso deseje, altere o **Modo de rotação**. Consulte o [Editor de Preferências](Preferences_Editor#Navigation.md).
5.  Se o estilo de navegação **CAD** estiver selecionado: caso e deseje, pode **Habilitar a animação** alterando a configuração. Consulte o [Editor de Preferências](Preferences_Editor#Navigation.md).



## Estilos de navegação disponíveis 

Com todos os estilos de navegação, exceto ao selecionar objetos de um esboço no modo de edição, é necessário pressionar **Ctrl** para selecionar vários objetos.

The following keyboard options are available for all styles:

-    **Ctrl**\+ {{ASCII|43}} and **Ctrl** + {{ASCII|22}} or **PgUp** and **PgDn** to zoom in and out, respectively.

-   The arrow keys, {{ASCII|17}}{{ASCII|16}}{{ASCII|30}}{{ASCII|31}}, to pan the view left/right and up/down.

-    **Shift**\+ {{ASCII|17}} and **Shift** + {{ASCII|16}} to rotate the view by 90 degrees.



### Navegação do Blender 

O estilo de navegação do Blender foi modelado com base no [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">


{{Blender Navigation
|Select_name=Selecionar
|Pan_name=Pan(Movimento lateral)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre o objeto que deseja selecionar.
|Pan_text=Pressione **Shift** e o botão do meio do mouse, depois mova o cursor.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the middle mouse button, then move the pointer.

|Pan_text=Hold **Shift** and the middle mouse button, then move the pointer.

Alternatively, hold both left and right mouse buttons, and then move the pointer.
}}



### Navegação CAD 

Este é o estilo de navegação padrão. Permite um controle simples da visualização e não requer o uso de teclas do teclado, exceto para fazer seleções múltiplas.


<div class="mw-translate-fuzzy">


{{CAD Navigation
|Select_name=Selecionar
|Pan_name=Pan(Movimento lateral)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar visão<br>Primeiro método
|Rotate_view_alt_name=Rotacionar visão<br>Método alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre o objeto que deseja selecionar.
|Pan_text=Mantenha pressionado o botão central do mouse e, em seguida, mova o cursor.
|Pan_mode_text=Movimentação panorâmica ou lateral: mantenha pressionada a tecla **Ctrl**, pressione o botão direito do mouse uma vez e, em seguida, mova o cursor.
|Zoom_text=Use a roda do mouse para aumentar e diminuir o zoom.
</div>

|Ctrl=**Ctrl**
|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.

|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

Se os botões forem soltos antes de você parar o movimento do mouse, a visualização continuará girando, se isso estiver habilitado.

<div class="mw-translate-fuzzy">
Um clique duplo com o botão central do mouse define um novo centro de rotação.
|Rotate_view_mode_text=Modo de rotação: mantenha pressionada a tecla **Shift**, pressione o botão direito do mouse uma vez e, em seguida, mova o cursor.
|Rotate_view_alt_text=Mantenha pressionado o botão central do mouse e, em seguida, pressione e segure o botão direito do mouse e mova o cursor.
</div>

|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Com este método, o botão central do mouse pode ser solto depois que o botão direito do mouse for pressionado.

<div class="mw-translate-fuzzy">
Os usuários que usam o mouse com a mão direita podem achar este método mais fácil do que o primeiro método.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.

\|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer.

\|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer.

\|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. }}



### Navegação por Gestos 

Este estilo foi adaptado para uso com tela sensível ao toque e caneta. No entanto, também pode ser utilizado com um mouse e é recomendado para uso em um Mac com trackpad.


<div class="mw-translate-fuzzy">


{{Gesture Navigation
|Select_name=Selecionar
|Pan_name=Pan (Movimento lateral)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar a visão
|Tilt_view_name=Inclinar a visão
|Select_text=Pressione o botão esquerdo do mouse sobre o objeto que deseja selecionar.
|Select_gesture_text=Toque para selecionar.
|Pan_text=Mantenha pressionado o botão direito do mouse e, em seguida, mova o cursor.
|Pan_gesture_text=Arraste com dois dedos.
</div>

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.

<div class="mw-translate-fuzzy">
Para definir o ponto de foco da câmera para rotação, clique em um ponto com o botão do meio do mouse. Como alternativa, aponte o cursor para um ponto e pressione **H** no teclado.
|Rotate_view_gesture_text=Arraste com um dedo para girar.
</div>

|Pan_text=Hold the right mouse button, then move the pointer.

|Tilt_view_text=Hold both left and right mouse buttons, then move the pointer sideways.

|Select_gesture_text=Tap to select.

|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.

|Rotate_view_gesture_text=Drag with one finger to rotate.

<div class="mw-translate-fuzzy">
Pressione **Alt** ao usar o [Ambiente de Esboço](Sketcher_Workbench.md).
|Tilt_view_text=Mantenha pressionados os botões esquerdo e direito do mouse, depois mova o ponteiro lateralmente.
|Tilt_view_gesture_text=Gire a linha imaginária formada por dois pontos de toque.
</div>

|Pan_gesture_text=Drag with two fingers.

<div class="mw-translate-fuzzy">
Alternatively, tap and hold, then drag. This simulates the pan with the right mouse button.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Zoom_gesture_text=Drag two fingers (pinch) closer or farther apart.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
In [Sketcher](Sketcher_Workbench.md) and other edit modes, this behavior is disabled. Hold **Alt** when pressing the mouse button to enter rotation mode.
</div>

|Tilt_view_gesture_text=Rotate the imaginary line formed by two touch points.

Este método está desabilitado por padrão. Para ativá-lo, vá para **Editar → Preferências → Exibição → Navegação**, e desmarque a caixa "Desativar gesto de inclinação na tela sensível ao toque".
}}



### Navegação por gestos no Maya 

Na Navegação por Gestos no Maya, o movimento panorâmico, o zoom e a rotação da visualização exigem a tecla **Alt** em conjunto com um botão do mouse; portanto, é necessário um mouse de três botões. Também é possível usar gestos, pois este estilo foi desenvolvido com base no estilo de [navegação por gestos](#Gesture_navigation.md).


<div class="mw-translate-fuzzy">

Na Navegação com o Maya-Gesture, o panorâmico, o zoom e a rotação da vista requerem a tecla **Alt** juntamente com um botão do mouse; portanto, é necessário um mouse de três botões. Também é possível usar gestos, pois este modo foi desenvolvido sobre o modo [Navegação por gestos](#Navegação_por_gestos.md). {{MayaGesture Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Alt=**Alt**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segurar **Alt** e o botão do meio do mouse, depois mover o ponteiro.
|Zoom_text=Segure **Alt** e o botão direito do mouse, depois mova o ponteiro.
</div>

|Alt=**Alt**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold **Alt** and the right mouse button, then move the pointer.

|Rotate_view_text=Hold **Alt** and the left mouse button, then move the pointer.

|Pan_text=Hold **Alt** and the middle mouse button, then move the pointer.

|Tilt_view_text=Hold **Alt** and both left and right mouse buttons, and then move the pointer sideways.
}}



### Navegação OpenCascade 

O estilo de navegação OpenCascade foi modelado com base no [OpenCascade](https://www.opencascade.com/).


<div class="mw-translate-fuzzy">


{{OpenCascade Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Ctrl=**Ctrl**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.
</div>

|Ctrl=**Ctrl**

|Select_text=Press the left mouse button over an object you want to select.

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
Como alternativa, mantenha pressionadas as teclas **Ctrl** e o botão esquerdo do mouse, depois mova o ponteiro.
|Rotate_view_text=Mantenha pressionadas as teclas **Ctrl** e o botão direito do mouse, depois mova o ponteiro.
}}


</div>

\|Rotate_view_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

Alternatively, hold **Ctrl** and the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. It is possible to hold **Ctrl**. }}



### Navegação OpenInventor 

A navegação do OpenInventor (anteriormente conhecido como Inventor) foi modelada com base no [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor). Para selecionar objetos, é necessário manter pressionada a tecla **Shift** ou **Ctrl**.

Este estilo não é baseado no Autodesk Inventor.


<div class="mw-translate-fuzzy">


{{OpenInventor Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Ctrl=**Ctrl**
|Select_text=Segure **Ctrl**, depois pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.
</div>

|Shift=**Shift**

|Select_text=Hold **Shift**, then press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
Mantenha pressionada a tecla **Ctrl** em vez disso para selecionar vários objetos.
|Pan_text=Mantenha pressionado o botão central do mouse e mova o ponteiro.
|Zoom_text=Use a roda do mouse para aumentar e diminuir o zoom.
</div>

|Zoom_text=Use the mouse wheel to zoom in and out.

<div class="mw-translate-fuzzy">
Como alternativa, mantenha pressionado o botão central do mouse, em seguida, pressione e segure o botão esquerdo do mouse, depois mova o ponteiro.
|Rotate_view_text=Mantenha pressionado o botão esquerdo do mouse, depois mova o ponteiro.
}}


</div>

\|Rotate_view_text=Hold the left mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Navegação OpenCascade 

O estilo de navegação do OpenSCAD foi modelado com base no [OpenSCAD](https://openscad.org/).


{{OpenSCAD_Navigation
|Select_name=Select
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Pan_name=Pan

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
Mantenha pressionadas as teclas **Ctrl** e **Shift** ao pressionar o botão do mouse para arrastar um objeto em um esboço no modo de edição.
|Pan_text=Mantenha pressionado o botão direito do mouse e mova o ponteiro.
|Zoom_text=Mantenha pressionado o botão central do mouse e mova o ponteiro.
Como alternativa, mantenha pressionadas as teclas **Shift** e o botão direito do mouse, depois mova o ponteiro.
|Rotate_view_text=Mantenha pressionado o botão esquerdo do mouse e mova o ponteiro.
}}


</div>

\|Zoom_text=Use the mouse wheel to zoom in and out.

Alternatively, hold the middle mouse button, then move the pointer.

Or hold **Shift** and the right mouse button, then move the pointer.

\|Rotate_view_text=Hold the left mouse button, then move the pointer.

Alternatively, and when a sketch is in edit mode, hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

\|Pan_text=Hold the right mouse button, then move the pointer. }}




<div class="mw-translate-fuzzy">

### Navegação do Revit 


</div>

O estilo de navegação do Revit foi modelado com base no [Revit](https://en.wikipedia.org/wiki/Autodesk_Revit).


<div class="mw-translate-fuzzy">


{{Revit Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
</div>

|Shift=**Shift**

|Select_text=Press the left mouse button over an object you want to select.

<div class="mw-translate-fuzzy">
|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.
|Rotate_view_text=Segure **Shift** e o botão central do mouse, depois mova o ponteiro.
</div>

|Rotate_view_text=Hold **Shift** and the middle mouse button, then move the pointer.

<div class="mw-translate-fuzzy">
Alternativamente, segure o botão central do mouse, depois pressione e segure o botão direito do mouse, depois mova o ponteiro.
}}


</div>

\|Pan_text=Hold the middle mouse button, then move the pointer.


<div class="mw-translate-fuzzy">

Alternativamente, segure os botões esquerdo e direito do mouse, depois mova o ponteiro.


</div>



### Navegação do TinkerCAD 

O estilo de navegação do TinkerCAD foi modelado com base no [TinkerCAD](https://en.wikipedia.org/wiki/Tinkercad).


<div class="mw-translate-fuzzy">


{{TinkerCAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.
|Rotate_view_text=Press the right mouse button, then move the pointer.
}}


</div>

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Use the mouse wheel to zoom in and out.

\|Rotate_view_text=Press the right mouse button, then move the pointer.

\|Pan_text=Hold the middle mouse button, then move the pointer. }}



### Navegação Touchpad 

Com o estilo de navegação do Touchpad, panorâmica, zoom e rotação da visualização exigem uma tecla modificadora junto com o touchpad. Este estilo também pode ser usado com um mouse.


<div class="mw-translate-fuzzy">

Na Navegação com touchpad, panorâmico, zoom e rotacionar vista requerem o pressionamento de tecla com o touchpad. {{Touchpad Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Shift=**Shift**
|Ctrl=**Ctrl**
|Alt=**Alt**
|PageUp=**PageUp**
|PageDown=**PageDown**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure **Shift**, depois mova o ponteiro.
|Zoom_text=Use **PageUp** e **PageDown** para aumentar e diminuir o zoom.
|Zoom_alt_text=Alternativamente, segure **Shift** e **Ctrl**, depois mova o ponteiro.
|Rotate_view_text=Segure **Alt**, depois mova o ponteiro.
|Rotate_view_alt_text=Alternativamente, segure **Shift** e o botão esquerdo, depois mova o ponteiro.
}}


</div>

\|Ctrl=**Ctrl** \|Shift=**Shift** \|Alt=**Alt**

\|Select_text=Press the left mouse button over an object you want to select.

\|Zoom_text=Hold **Ctrl** and **Shift**, then move the pointer.

\|Rotate_view_text=Hold **Alt**, then move the pointer.

Alternatively, hold **Shift** and the left button, then move the pointer.

\|Pan_text=Hold **Shift**, then move the pointer. }}



## Suporte de Hardware 

O FreeCAD também suporta alguns [dispositivos de entrada 3D](3D_input_devices/pt-br.md).



## Navegação recomendada para macOS 

Nos MacBooks com trackpad, a navegação por gestos funciona muito bem, mas os gestos têm um significado especial:

-   Zoom: arraste com dois dedos.
-   Girar: arraste com três dedos.
-   PAN (Panorâmica): **Ctrl** + três dedos.



---
⏵ [documentation index](../README.md) > Mouse navigation/pt-br
