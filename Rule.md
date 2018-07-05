# Rule

## HTML

### E01001. DOCTYPE must be decalred first (文档类型必须首先声明)

正确：

```html
<!DOCTYPE html>
<html lang="zh-Hans">
  <head>
    <title>文档的标题</title>
  </head>

  <body>
    文档的内容......
  </body>

</html>
```

错误

```html
<!-- <!DOCTYPE html> -->
<html lang="zh-Hans">
  <head>
    <title>文档的标题</title>
  </head>

  <body>
    文档的内容......
  </body>

</html>
```

### E01002. DOCTYPE for HTML5 should be "&lt;DOCTYPE html&gt;" (HTML5的文档类型必须是"&lt;DOCTYPE html&gt;")

正确：

```html
<!DOCTYPE html>
<html lang="zh-Hans">
  <head>
    <title>文档的标题</title>
  </head>

  <body>
    文档的内容......
  </body>

</html>
```

错误：

```html
<!DOCTYPE html6>
<html lang="zh-Hans">
  <head>
    <title>文档的标题</title>
  </head>

  <body>
    文档的内容......
  </body>

</html>
```

### E01003. invalid tag (不可使用非法标签)

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <p>AAA</p>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <invalidtag>AAA</invalidtag>
  </body>
</html>
```

### E01004. deprecated tag (不可使用废弃标签)

废弃标签包括

```html
<center>, <font>, <s>, <strike>, <b>, <i>, <tt>, <small>, <frame>, <acronym>, <big>, <u>, <isindex>, <basefont>, <dir>, <applet>, <style>
```

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <p>something</p>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <font>something</font>
  </body>
</html>
```

### E01005. non-selfclosed tag must be paired (双标签必须成对)

成对标签：

```html
<html>, <body>, <title>, <p>, <div>, <h1>~<h6>,<abbr>, <address>, <bdi>, <bdo>, <blockquote>, <cite>, <del>, <dfn>, <em>, <ins>, <kbd>, <meter>, <progress>, <rb>, <rtc>, <rp>, <rt>, <ruby>, <time>, <datalist>, <canvas>, <figcaption>, <figure>, <audio>, <source>, <video>, <nav>, <header>, <footer>, <section>, <article>, <aside>, <details>, <dialog>, <pre>, <q>, <samp>, <strong>, <sup>, <sub>, <var>, <form>, <textarea>, <button>, <select>, <option>, <optgroup>, <label>, <fieldset>, <legend>, <frameset>,<noframes>, <map>, <a>, <ul>, <ol>, <li>, <dl>, <dt>, <dd>, <menu>, <menuitem>, <span>, <head>, <script>, <noscript>, <object>, <table>, <th>, <td>, <tr>, <tbody>, <thead>, <tfoot>, <caption>, <col>, <colgroup>, <main>, <picture>, <template>, <data>, <code>
```

自闭合标签：

```html
<wbr>, <keygen>, <output>, <track>, <embed>, <input>, <iframe>, <img>, <area>, <link>, <meta>, <base>, <param>
```

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <p>段落</p><br>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <p>段落
  </body>
</html>
```

### E01006. invalid attribute (不可使用非法属性)

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title invalidattribute="oh">Page Title</title>
  </head>
  <body>
  </body>
</html>
```

### E01007. deprecared attribute (不能使用废弃的属性)

废弃属性包括

| 属性 | 所属的元素 |
| ---- | ---- |
| manifest | html |
| xmlns | html,title |
| align | caption, iframe, img, input, object, legend, table, hr, div, h1, h2, h3, h4, h5, h6, p, col, colgroup, tbody, td, tfoot, th, thead and tr |
| alink | body |
| link | body |
| vlink | body |
| text | body |
| background | body |
| bgcolor | table, tr, td, th and body |
| border | table and object, img|
| char | col, colgroup, tbody, td, tfoot, th, thead and tr |
| charoff | col, colgroup, tbody, td, tfoot, th, thead and tr |
| compact | dl , ol and ul |
| frame | table |
| frameborder | iframe |
| hspace | img and object |
| nowrap | td and th|
| rules | table |
| type | li, ol and ul |
| value | li |
| valign | col, colgroup, tbody, td, tfoot, th, thead and tr |
| width | hr, table, td, th, col, colgroup and pre |
| accept | form |
| vspace | img |
| charset | a, link |
| coords | a |
| name | a |
| rev | a, link |
| shape |
| target | link |
| height | th, td |

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title style="font-size: 1rem">Page Title</title>
  </head>
  <body>
  </body>
</html>
```

### E01008. required element missing (必须包含特定标签)

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>
  </body>
</html>
```

### E01009. required attribute missing (必须包含特定属性)

正确：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Page Title</title>
  </head>
  <body>
  </body>
</html>
```

错误：

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
  </body>
</html>
```