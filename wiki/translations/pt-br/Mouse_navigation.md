# Mouse navigation/pt-br
{{TOCright}}

## Overview


<div class="mw-translate-fuzzy">

## Visão geral 

O *Estilos de Navegação* do FreeCAD consiste nos comandos usados para navegar visualmente pelo espaço 3D e interagir com os objetos exibidos utilizando o mouse. O FreeCAD suporta múltiplos estilos de navegação. O estilo de navegação padrão é chamado de \"Navegação CAD\", e é muito simples e prático, mas o FreeCAD também oferece estilos alternativos de navegação que você pode escolher de acordo com suas preferências.


</div>

For more information about selecting objects see [Selection methods](Selection_methods.md).

For more information about manipulating objects see [Std TransformManip](Std_TransformManip.md).

## Selecting a navigation style 


<div class="mw-translate-fuzzy">

-   No menu [Editor de Preferências](Preferences_Editor/pt-br#Navegação.md); menu **Editar → Preferências → Tela → Navegação → Navegação 3D**.
-   Clicando com o botão direito do mouse no espaço vazio na Vista 3D e selecionando **Estilo de Navegação** no menu de contexto.


</div>

## Available navigation styles 


<div class="mw-translate-fuzzy">

### Blender Navigation 


</div>

The Blender navigation style was modeled after [Blender](https://www.blender.org).


<div class="mw-translate-fuzzy">

O estilo de navegação do Blender foi modelado após [Blender](https://www.blender.org). Anteriormente não havia como realizar movimento panorâmico usando apenas o mouse; sempre era necessário segurar a tecla **Shift**. Isto mudou em 2016, agora você pode segurar os botões esquerdo e direito do mouse para mover a janela de exibição. {{Blender Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure **Shift** e o botão central do mouse, depois mova o ponteiro.
</div>

Alternativamente, segure os botões esquerdo e direito do mouse, e então mova o ponteiro.
|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.
|Rotate_view_text=Segure o botão do meio do mouse, depois mova o ponteiro.
}}

### CAD navigation 


<div class="mw-translate-fuzzy">

### Navegação CAD 

Este é o estilo de navegação padrão. Ele permite ao usuário um controle simples da visualização, e não requer o uso de teclas de teclado, exceto para fazer seleções múltiplas.


</div>


{{CAD Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista<br>Primeiro método
|Rotate_view_alt_name=Rotacionar vista<br>Método alternativo
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.

<div class="mw-translate-fuzzy">
Manter pressionado **Ctrl** permite a seleção de múltiplos objetos.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
|Pan_mode_text=Pan mode: segure a tecla **Ctrl**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. <small>(v0.17)</small> 
|Zoom_text=Utilizar a roda do mouse para aumentar e diminuir o zoom.
</div>

<div class="mw-translate-fuzzy">
Clicando no botão do meio do mouse, a vista é centrada novamente na localização do cursor.
|Zoom_mode_text=Zoom mode: segure as teclas **Ctrl** e **Shift**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. 
<small>(v0.17)</small> 
|Rotate_view_text=Segure o botão central do mouse, depois pressione e segure o botão esquerdo do mouse, depois mova o ponteiro.
</div>

<div class="mw-translate-fuzzy">
A localização do cursor quando o botão central do mouse é pressionado determina o centro de rotação. A rotação funciona como girar uma bola que gira ao redor de seu centro. Se os botões forem soltos antes de você parar o movimento do mouse, a visualização continua [girando](Std_DemoMode/pt-br.md), se isto estiver habilitado.
</div>

<div class="mw-translate-fuzzy">
Um duplo clique com o botão do meio do mouse define um novo centro de rotação.
|Rotate_view_mode_text=Rotate mode: pressione a tecla **Shift**, pressione o botão direito do mouse uma vez, depois mova o ponteiro. <small>(v0.17)</small> 
|Rotate_view_alt_text=Segure o botão central do mouse, depois pressione e segure o botão direito do mouse, depois mova o ponteiro.
</div>

Com este método, o botão central do mouse pode ser solto depois que o botão direito do mouse for pressionado.

Os usuários que usam o mouse com a mão direita podem achar este método mais fácil do que o primeiro método.
}}


<div class="mw-translate-fuzzy">

### Navegação por gestos 


</div>

This style was tailored for use with a touchscreen and pen. Nevertheless, it can also be used with a mouse, and is recommended for use when using a Mac with a trackpad.


<div class="mw-translate-fuzzy">

Este estilo foi introduzido na versão 0.16, e foi adaptado para uso com uma tela sensível ao toque e uma caneta. No entanto, também pode ser usado com um mouse, recomendado para uso quando se usa um Mac com trackpad. {{Gesture Navigation \|Select\_name=Selecionar \|Pan\_name=Pan(movimento panorâmico) \|Zoom\_name=Zoom \|Rotate\_view\_name=Rotacionar vista \|Tilt\_view\_name=Vista inclinada \|Select\_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar. \|Select\_gesture\_text=Toque para selecionar. \|Pan\_text=Segure o botão direito do mouse, depois mova o ponteiro. \|Pan\_gesture\_text=Arrastar com dois dedos.


</div>

Você também pode clicar e segurar, depois arrastar. Isto simula o Pan(movimento panorâmico) com o botão direito do mouse. \|Zoom\_text=Use a rodinha do mouse para aumentar e diminuir o zoom. \|Zoom\_gesture\_text=Faça o movimento de pinça fechando os dedos para aproximar ou de abertura para afastar. \|Rotate\_view\_text=Mantenha o botão esquerdo do mouse pressionado, depois mova o ponteiro. Em [Sketcher](Sketcher_Workbench/pt-br.md) e outros modos de edição, este comportamento é desativado. Segure **Alt** ao pressionar o botão do mouse para entrar no modo de rotação.

Para definir o ponto de foco da câmera para rotação, clique em um ponto com o botão central do mouse. Alternativamente, aponte o cursor para um ponto e pressione **H** no teclado. \|Rotate\_view\_gesture\_text=Arraste com um dedo para girar.

Segure **Alt** quando no [Sketcher](Sketcher_Workbench/pt-br.md). \|Tilt\_view\_text=Segure os botões esquerdo e direito do mouse, depois mova o ponteiro para o lado. \|Tilt\_view\_gesture\_text=Gire a linha imaginária formada por dois pontos de contato.

Na v0.18 este método é desativado por padrão. Para ativar, vá para {**Editar → Preferências → Tela → Navegação → Navegação**, e desmarque a caixa de seleção "Desabilitar gesto de inclinação da tela sensível ao toque".
}}

<div class="mw-translate-fuzzy">
=== Maya-Gesture Navigation ===
</div>

In Maya-Gesture Navigation, panning, zooming, and rotating the view require the **Alt** key together with a mouse button; therefore, a three-button mouse is required. It's also possible to use gestures as this style was developed over the [Gesture navigation](#Gesture_navigation.md) style.

<div class="mw-translate-fuzzy">
Na Navegação com o Maya-Gesture, o panorâmico, o zoom e a rotação da vista requerem a tecla **Alt** juntamente com um botão do mouse; portanto, é necessário um mouse de três botões. Também é possível usar gestos, pois este modo foi desenvolvido sobre o modo [Navegação por gestos](#Navegação_por_gestos.md).
{{MayaGesture Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Alt=**Alt**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segurar **Alt** e o botão do meio do mouse, depois mover o ponteiro.
|Zoom_text=Segure **Alt** e o botão direito do mouse, depois mova o ponteiro.
</div>

Alternativamente, use a rodinha do mouse para aumentar e diminuir o zoom.
|Rotate_view_text=Segure **Alt** e o botão esquerdo do mouse, depois mova o ponteiro.
}}

<div class="mw-translate-fuzzy">
=== OpenCascade ===
</div>

The OpenCascade navigation style was modeled after [https://www.opencascade.com/ OpenCascade].

{{OpenCascade Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Ctrl=**Ctrl**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.
|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.

Alternativamente, segure **Ctrl** e o botão esquerdo do mouse, depois mova o ponteiro.
|Rotate_view_text=Segure **Ctrl** e o botão direito do mouse, depois mova o ponteiro.
}}

=== OpenInventor navigation ===

<div class="mw-translate-fuzzy">
=== Navegação OpenInventor ===
A navegação OpenInventor (antigo Inventor) foi modelada após [http://en.wikipedia.org/wiki/Open_Inventor Open Inventor]. Para selecionar objetos, você deve manter pressionada a tecla **Ctrl**.
</div>

<div class="mw-translate-fuzzy">
Este modo não é baseado no Autodesk Inventor.
</div>

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

Hold down **Ctrl** instead to select multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Zoom_text=Use the mouse wheel to zoom in and out.

Alternativamente, segure o botão central do mouse, depois pressione e segure o botão esquerdo do mouse, depois mova o ponteiro. |Rotate_view_text=Mantenha o botão esquerdo do mouse pressionado, depois mova o ponteiro.
}}

=== OpenSCAD navigation ===

The OpenSCAD navigation style was modeled after [https://openscad.org/ OpenSCAD].

<small>(v0.20)</small> 

{{OpenSCAD_Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.
|Pan_text=Hold the right mouse button, then move the pointer.
|Zoom_text=Hold the middle mouse button, then move the pointer.
Alternatively, hold **Shift** and the right mouse button, then move the pointer.
|Rotate_view_text=Hold the left mouse button, then move the pointer.
}}

<div class="mw-translate-fuzzy">
=== Navegação do Revit ===
</div>

The Revit navigation style was modeled after [https://en.wikipedia.org/wiki/Autodesk_Revit Revit].

{{Revit Navigation
|Select_name=Selecionar
|Pan_name=Pan(movimento panorâmico)
|Zoom_name=Zoom
|Rotate_view_name=Rotacionar vista
|Shift=**Shift**
|Select_text=Pressione o botão esquerdo do mouse sobre um objeto que você deseja selecionar.
|Pan_text=Segure o botão do meio do mouse, depois mova o ponteiro.

Alternativamente, segure os botões esquerdo e direito do mouse, depois mova o ponteiro.

|Zoom_text=Use a rodinha do mouse para aumentar e diminuir o zoom.
|Rotate_view_text=Segure **Shift** e o botão central do mouse, depois mova o ponteiro.

Alternativamente, segure o botão central do mouse, depois pressione e segure o botão direito do mouse, depois mova o ponteiro.
}}

=== TinkerCAD navigation ===

The TinkerCAD navigation style was modeled after [https://en.wikipedia.org/wiki/Tinkercad TinkerCAD].

<small>(v0.20)</small> 

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

<div class="mw-translate-fuzzy">
=== Navegação Touchpad ===
</div>

In Touchpad Navigation, panning, zooming, and rotating the view require a modifier key together with the touchpad.

<div class="mw-translate-fuzzy">
Na Navegação com touchpad, panorâmico, zoom e rotacionar vista requerem o pressionamento de tecla com o touchpad.
{{Touchpad Navigation
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

== Suporte de Hardware ==

<div class="mw-translate-fuzzy">
O FreeCAD também suporta alguns [dispositivos de entrada 3D](3D_input_devices/pt-br.md).
</div>

<div class="mw-translate-fuzzy">
== Problemas no Mac OS X ==
</div>

<div class="mw-translate-fuzzy">
Recentemente recebemos relatórios [http://forum.freecadweb.org/viewtopic.php?f=3&t=3592&start=0 no fórum] de usuários de Mac que esses botões do mouse e combinação de teclas não funcionam como esperado. Infelizmente, nenhum dos desenvolvedores possui um Mac, nem os outros colaboradores regulares. Precisamos de sua ajuda para determinar quais botões do mouse e combinação de teclas funcionam para que possamos atualizar este wiki.
</div>

== Developing a custom navigation == 

The tutorial [Adding a new mouse navigation option to FreeCAD](Adding_a_new_mouse_navigation_option_to_FreeCAD.md) orients developers who want to develop a custom mouse navigation option. Familiarity with the C++ syntax is required.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Mouse navigation/pt-br
