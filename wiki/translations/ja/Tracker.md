





{{TOCright}}

![](images/Mantis_logo_262x90.png )


<div class="mw-translate-fuzzy">

もし、バグを発見したかもと思ったら、そこにバグを報告することは歓迎されます。しかし、バグを報告する前に、以下の項目をチェックしてください。:

-   あなたの見つけたバグが本当にバグかどうか、つまり動くべき機能が動かないことを確認してください。

　あなたがわからない場合は、ためらわずに [フォーラム](http://forum.freecadweb.org/) にこの問題を説明し、何をすればよいか訪ねてください。

-   投稿する前に、[frequently asked questions](FAQ.md) を読み、[フォーラム](http://forum.freecadweb.org/) 内を検索し、バグトラッカーを検索して、同じバグがまだ投稿されてないことを確認してください。
-   できるだけ詳しく、問題や再現方法について説明してください。バグを確認できない場合、修正できなことがあります。
-   あなたが使用しているオペレーティングシステムが32bitか64bitか、　あなたが使っているFreeCADのバージョンについての情報を付け加えてください。
-   バグ毎に個別のレポートを投稿してください。
-   FreeCADをinux上で利用し、バグが原因でクラッシュした場合は、デバッグトレースを実行することもできます。端末からgdb freecadを実行（gdbパッケージがインストールされていることを仮定）し、gdbの中でrunを実行します。　FreeCADは実行されます。クラッシュが発生したら、btと入力するとバックトレースを取得できます。投稿するバグレポートの中にバックトレースを含めてください。


</div>

## フローチャート

![](images/Bugreport-workflow.png )

上記のフローチャートに示されているように、チケットを作成する前にまずフォーラムとバグトラッカーを検索して、問題が既知の問題で あるかどうかを確認してください。 これにより、開発者やボランティアにとって、FreeCADをさらにすばらしいものにする時間を節約できます。

## バグ

もし、バグを発見したかもと思ったら、そこにバグを報告することは歓迎されます。しかし、バグを報告する前に、以下の項目をチェックしてください。:

もしバグを発見したかもしれないと思う場合は、トラッカーの [Bugs Section](http://sourceforge.net/tracker/?atid=455298&group_id=49159&func=browse) に行き、statusをanyにして、これまでに申請されたバグを確認してください。キーワード検索を利用すると、似ている問題のバグトラッカーのエントリを見つけることができます。もし、あなたの問題が過去の項目になかったときは、同じページに新たな項目として投稿すべきです。

### 機能追加要求

あなたがFreeCADを世界で一番のCADソフトウェアにするために絶対に必要と思う機能がないことに気づいたら、[Feature Request](http://sourceforge.net/tracker/?atid=455301&group_id=49159&func=browse) 機能追加要望のセクションが役に立つかもしれません。

### サポート要求

あなたがFreeCADをコンパイルするのにどうすることもできず、 [Compile On Windows](CompileOnWindows/jp.md) や [Compile On Unix](CompileOnUnix/jp.md) にヒントとなるものが書かれていない場合や、他の新しい環境への移植を試す場合や、FreeCADの新しいモジュールや拡張機能を作る場合に、補助が必要な場合は、[Support Requests](http://sourceforge.net/tracker/?atid=455299&group_id=49159&func=browse) セクションがあなたの行くべき場所になります。

### 新しいパッチ

バグの修正や、拡張機能、一般公開できるFreeCADの何らかを作成したときは、Subversioを使ってパッチを作成し、 [patches section](https://sourceforge.net/tracker/?group_id=49159&atid=455300) セクションにファイルを投稿してください。

## 機能追加要望

実装されていない機能をFreeCADで使いたいと思ったら、それはバグではなく、機能追加要望です。これは同じトラッカー（バグではなく機能要望として申請する）に投稿できますが、あなたの機能追加要望が実現される保証が無いことを心に留めておいてください。

-   あなたの見つけたバグが本当にバグかどうか、つまり動くべき機能が動かないことを確認してください。

　あなたがわからない場合は、ためらわずに [フォーラム](http://forum.freecadweb.org/) にこの問題を説明し、何をすればよいか訪ねてください。

-   投稿する前に、[frequently asked questions](FAQ.md) を読み、[フォーラム](http://forum.freecadweb.org/) 内を検索し、バグトラッカーを検索して、同じバグがまだ投稿されてないことを確認してください。
-   できるだけ詳しく、問題や再現方法について説明してください。バグを確認できない場合、修正できなことがあります。
-   あなたが使用しているオペレーティングシステムが32bitか64bitか、　あなたが使っているFreeCADのバージョンについての情報を付け加えてください。
-   バグ毎に個別のレポートを投稿してください。
-   FreeCADをinux上で利用し、バグが原因でクラッシュした場合は、デバッグトレースを実行することもできます。端末からgdb freecadを実行（gdbパッケージがインストールされていることを仮定）し、gdbの中でrunを実行します。　FreeCADは実行されます。クラッシュが発生したら、btと入力するとバックトレースを取得できます。投稿するバグレポートの中にバックトレースを含めてください。

## パッチの投稿　

In case you have programmed a bug fix, an extension or something else that can be of public use in FreeCAD, create a patch using the Git diff tool and submit it on the same tracker (file it as *patch*).

Addendumː FreeCAD development has switched to the [GitHub](https://github.com/FreeCAD/FreeCAD) development model so the workflow for submitting patches has been greatly enhanced/streamlined by submitting Pull Requests.

1.  Open a forum thread in the [Developer subforum](https://forum.freecadweb.org/viewforum.php?f=10) to announce and discuss your patch.
2.  Submit your Pull Request (PR) to the [FreeCAD GitHub repo](http://github.com/FreeCAD/FreeCAD). Be sure to link to the forum thread in the git commit summary. If you haven\'t worked with `git` before or are unfamiliar with submitting a PR to github, please read our introduction to [github](Source_code_management.md) wiki page.
3.  Paste the PR link in to the forum thread for the devs/testers to test.
4.  Be present for the discussion so that your code can potentially be merged more effectively.

**NOTEː** the FreeCAD community recommends to first discuss any large revision to the source code in advance to save everyone time.

## \"古い\"sourceforgeのトラッカー(廃止)

注意：バグを報告するために、新しいMantisバグトラッカーを利用してください。この方法は現在廃止予定です。

### どこで見つけるか？

FreeCADには独自の [トラッカー要約ページ](https://sourceforge.net/tracker/?group_id=49159) があります。そこではトラッカーの個々のセクションの概要を見ることができます。

### いつ使用するか？

![The FreeCAD Bug Tracker](images/Bugtracker_Screenshot_annotated.png )

(Same guidelines as [Submiting patches](https://www.freecadweb.org/wiki/Tracker#Submitting_patches))

If you have created a git branch containing changes that you would like to see merged into the FreeCAD code, you can ask there to have your branch reviewed and merged if the FreeCAD developers are OK with it. You must first publish your branch to a public git repository (github, gitlab, bitbucket, sourceforge etc\...) and then give the URL of your branch in your merge request.

## MantisBT Tips and Tricks 

近年、sourceforgeプラットフォームにより、プロジェクトのバグトラッカーアプリケーション[mantis bug tracker](http://www.mantisbt.org/) が作られ、FreeCADは、古いビルトインのバグトラッカーの代わりに、現在このバグトラッカーを使っています。

### MantisBT BBCode 

In addition to the above [MantisBT Markup](Tracker#MantisBT_Markup.md) one also has the possibility to use BBCode format. For a comprehensive list see the [BBCode plus plugin page](https://github.com/mantisbt-plugins/BBCodePlus#supported-bbcode-tags). Here is a list of supported BBCode tagsː 
[img][/img] - Images
[url][/url] - Links
[email][/email] - Email addresses
[color=red][/color] - Colored text
[highlight=yellow][/highlight] - Highlighted text
[size][/size] - Font size
[list][/list] - Lists
[list=1][/list] - Numbered lists (number is starting number)
[*] - List items
[b][/b] - Bold
[u][/u] - underline
[i][/i] - Italic
[s][/s] - Strikethrough
[left][/left] - Left align
[center][/center] - Center
[right][/right] - Right align
[justify][/justify] - Justify
[hr] - Horizontal rule
[sub][/sub] - Subscript
[sup][/sup] - Superscript
[table][/table] - Table
[table=1][/table] - Table with border of specified width
[tr][/tr] - Table row
[td][/td] - Table column
[code][/code] - Code block
[code=sql][/code] - Code block with language definition
[code start=3][/code] - Code block with line numbers starting at number
[quote][/quote] - Quote by *someone* (no name)
[quote=name][/quote] - Quote by *name*


=== MantisBT \<=\> GitHub Markup === Below are special MantisBT Source-Integration plugin keywords which will link to the FreeCAD GitHub repo. See [GitHub and MantisBT](Tracker#GitHub_and_MantisBT.md).

-   **c:FreeCAD:git commit hash:** - **c** stands for \'commit\'. FreeCAD stands for the FreeCAD GitHub repo. \'git commit hash\' is the specific git commit hash to reference. Note: the trailing colon is necessary. Exampleː cːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **d:FreeCAD:git commit hash:** - similar to the above, **d** stands for \'diff\' which will provide a Diff view of the commit. Exampleː dːFreeCADː709d2f325db0490016807b8fa6f49d1c867b6bd8ː
-   **p:FreeCAD:pullrequest:** - similar to the above, **p** stands for Pull Request. Exampleː pːFreeCADː498ː

<img alt="" src=images/mantisbt-source-integration-markup.jpg  style="width:600px;"> 

## GitHub and MantisBT 

The FreeCAD bugtracker has a plug-in called [Source Integration](https://github.com/mantisbt-plugins/source-integration) which essentially ties both the FreeCAD GitHub repo to our MantisBT tracker. It makes it easier to track and associate git commits with their respective MantisBT tickets. **The Source Integration plugin scans the git commit messages for specific keywords in order to execute the following actions:**

**Note** The below keywords need to be added in the git commit message and not the PR subject

### Remotely referencing a ticket 

Using this pattern will automagically associate a git commit to a ticket (**Note:** this will not close the ticket.) The format MantisBT will recognize:

-   bug \#1234
-   bugs \#1234, \#5678
-   issue \#1234
-   issues \#1234, \#5678
-   report \#1234
-   reports \#1234, \#5678

For the inquisitive here is the regex MantisBT uses for this operation:


### Remotely resolving a ticket 

The format MantisBT will recognize:

-   fix \#1234
-   fixed \#1234
-   fixes \#1234
-   fixed \#1234, \#5678
-   fixes \#1234, \#5678
-   resolve \#1234
-   resolved \#1234
-   resolves \#1234
-   resolved \#1234, \#5678
-   resolves \#1234, \#5678

For the inquisitive here is the regex MantisBT uses for this operation:


## Related

-   [Bug Triage](Bug_Triage.md)
-   [Source Code Management](Source_Code_Management.md)


<div class="mw-translate-fuzzy">


{{docnav|Licence|Bug Triage}}


</div>




[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Administration{{\#translation:}}](Category:Administration.md)
