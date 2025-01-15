# Localisation Sidebar/pt-br
[Localização](Localisation/pt-br.md) é o processo de fornecer software com uma interface de usuário em vários idiomas. O wiki de documentação também pode ser localizado, conforme descrito na seção [Traduzir o wiki do FreeCAD](Localisation/pt-br#Translate_the_FreeCAD_wiki.md).

A barra lateral é uma ferramenta de navegação importante no mundo wiki, consulte [Manual:Interface/Sidebar](http://www.mediawiki.org/wiki/Manual:Interface/Sidebar) para obter mais informações.



## Traduzir a barra lateral 

A barra lateral agora é totalmente traduzível com a [Translation extension](http://www.mediawiki.org/wiki/Help:Extension:Translate), que está disponível em todas as páginas do wiki.

No wiki do FreeCAD, a barra lateral é implementada por meio de modelos, que alteram o texto dependendo do idioma selecionado. Detalhes técnicos sobre como esse recurso foi implementado estão descritos no tópico do fórum [Wiki navigation/translation](http://forum.freecadweb.org/viewtopic.php?f=21&t=9687&start=10#p80441).



### Instruções

Você pode ir para a página especial [Special:Translate/wiki-sidebar](Special:Translate/wiki-sidebar.md) para iniciar a tradução.

Há um bug na página de download. Você não pode redirecionar o link para \"Download/fr\" ou \"Download/de\", etc. Em vez disso, o link apontará para a tradução real de \"Download\" no seu idioma. A melhor maneira de lidar com isso é criar esta nova página e redirecionar para a página certa. Mais sobre redirecionamento em [Help:Editing](Help_Editing.md).



## Notas importantes 

Na maioria das vezes, haverá duas strings para cada item na barra lateral.

** {{int:sidebar-faq-target}}|sidebar-faq

O esquerdo representa o destino do link e o direito representa o texto que será exibido na barra lateral.

Você pode ver a diferença entre os dois olhando na parte superior da caixa de tradução, onde o nome da variável é exibido. Quando o nome da variável termina com "-target", significa que você estará traduzindo um link de destino. É feito para permitir ao tradutor para redirecionar os itens para as páginas traduzidas, ou seja, adicionando um código de idioma no final do nome da página, por exemplo, \"/fr\" para uma tradução em francês.

Não adicione os códigos de idioma \"/fr\", \"/de\", \"/es\", \"/ru\", etc., se a página traduzida não existir nesse idioma, o link será quebrado. Neste caso, não escreva nada além do nome da página, ou o link será quebrado.

![Onde procurar](images/Translate-sidebar-instruction.png )



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > [Wiki](Category_Wiki.md) > Localisation Sidebar/pt-br
