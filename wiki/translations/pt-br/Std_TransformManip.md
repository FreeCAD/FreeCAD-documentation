---
 GuiCommand:
   Name: Transformar
   MenuLocation: Editar , Transformar
   Workbenches: Todos
   SeeAlso: Std_UserEditMode
---

# Std TransformManip/pt-br



## Descrição

O comando **Transformar** permite que você aplique incrementos de rotação e de translação a um objeto.

<img alt="" src=images/Std_TransformManip_Example.png  style="width:400px;">



## Utilização


<div class="mw-translate-fuzzy">

1.  Selecione um objeto com uma propriedade de **Posicionamento**. Consulte [Notas](#Notes.md).
2.  Existem várias maneiras de ativar o comando:
    -   Selecionando a opção **Editar → <img src="images/Std_TransformManip.svg" width=16px> Transformar** no menu.
    -   Selecione a opção **<img src="images/Std_TransformManip.svg" width=16px> Transformar** no menu de contexto da [visualização de árvore](Tree_view.md).
    -   Se o [modo de edição](Std_UserEditMode.md) estiver definido como **<img src="images/Std_UserEditModeTransform.svg" width=16px> Transformar**, você também pode clicar duas vezes no objeto na visualização de árvore.
3.  Quando o painel de **Incrementos** for aberto.
4.  Você também pode ajustar os parâmetros de incrementos.
5.  Faça um ou mais dos seguintes:
    -   Pressione e segure o botão esquerdo do mouse em uma seta do eixo e arraste para mover o objeto ao longo desse eixo.
    -   Pressione e segure o botão esquerdo do mouse em um plano e arraste para mover o objeto ao longo desse plano.
    -   Pressione e segure o botão esquerdo do mouse em uma esfera e arraste para girar o objeto em torno desse eixo.
6.  Faça um dos seguintes:
    -   Pressione o botão **OK** para confirmar e concluir o comando.
    -   Pressione o botão **Cancelar** para reverter as transformações aplicadas e concluir o comando. <small>(v0.22)</small> 


</div>



## Notas


<div class="mw-translate-fuzzy">

-   Assim que você girar/mover o objeto na [visualização 3D](3D_view.md), as alterações serão aplicadas.
-   Alguns objetos com uma propriedade **Posicionamento**, como esboços, não podem ser manipulados, assim como objetos que estão conectados a outros objetos.

Na {{VersionMinus|0.21}}, não há botão **Cancelar**, nessas versões você pode pressionar o botão **OK** e usar o comando <img alt="" src=images/Std_Undo.svg  style="width:20px;"> [Desfazer](Std_Undo.md) para reverter as alterações posteriormente.


</div>





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std TransformManip/pt-br
