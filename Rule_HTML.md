# Rules for HTML

## Sepecification (规范)

### `HS0001`. DOCTYPE must be decalred first (文档类型必须首先声明)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!-- <!DOCTYPE html> -->
<html lang="en">
  ...
</html>
```

### `HS0002`. DOCTYPE for HTML5 should be "&lt;DOCTYPE html&gt;" (HTML5的文档类型必须是"&lt;DOCTYPE html&gt;")

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html6>
<html lang="zh-Hans">
  ...
</html>
```

### `HS0003`. invalid tag must NOT be used (不可使用非法标签)

Right(正确)：

```html
<!DOCTYPE html>
<html2 lang="en">
  ...
</html2>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html2 lang="en">
  ...
</html2>
```

### `HS0004`. deprecated tag must NOT be used (不可使用废弃标签)

Deprecated tags  (废弃标签):

```html
<center>, <font>, <s>, <strike>, <b>, <i>, <tt>, <small>, <frame>, <acronym>, <big>, <u>, <isindex>, <basefont>, <dir>, <applet>, <style>
```

### `HS005`. tag must be paired (双标签必须成对)

Paired Tags (成对标签)：

```html
<html>, <body>, <title>, <p>, <div>, <h1>~<h6>, <abbr>, <address>, <bdi>, <bdo>, <blockquote>, <cite>, <del>, <dfn>, <em>, <ins>, <kbd>, <meter>, <progress>, <rb>, <rtc>, <rp>, <rt>, <ruby>, <time>, <datalist>, <canvas>, <figcaption>, <figure>, <audio>, <source>, <video>, <nav>, <header>, <footer>, <section>, <article>, <aside>, <details>, <dialog>, <pre>, <q>, <samp>, <strong>, <sup>, <sub>, <var>, <form>, <textarea>, <button>, <select>, <option>, <optgroup>, <label>, <fieldset>, <legend>, <frameset>, <noframes>, <map>, <a>, <ul>, <ol>, <li>, <dl>, <dt>, <dd>, <menu>, <menuitem>, <span>, <head>, <script>, <noscript>, <object>, <table>, <th>, <td>, <tr>, <tbody>, <thead>, <tfoot>, <caption>, <col>, <colgroup>, <main>, <picture>, <template>, <data>, <code>, <summary>
```

Right(正确)：

```html
<p>段落</p>
```

Wrong(错误)：

```html
<p>段落
```

### `HS0006`. empty tag must be closed by self (空标签必须自闭合)

Empty tags (空标签)：

```html
<wbr>, <keygen>, <output>, <track>, <embed>, <input>, <iframe>, <img>, <area>, <link>, <meta>, <base>, <param>
```

Right(正确)：

```html
<br/>
```

Wrong(错误)：

```html
<br>
```

### `HS0007`. invalid attribute must NOT be used (不可使用非法属性)

Right(正确)：

```html
<title>Page Title</title>
```

Wrong(错误)：

```html
<title invalidattribute="oh">Page Title</title>
```

### `HS0008`. deprecated attribute must NOT be used (不能使用废弃的属性)

Deprecated attributes (废弃属性包括):

| Attribute (属性) | Element (所属的元素) |
| ---- | ---- |
| style | ALL |
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

Right(正确)：

```html
<body>
  ...
</body>
```

Wrong(错误)：

```html
<body bgcolor="black">
  ...
</body>
```

### `HS0009`. attribute name must NOT be duplication in the same element (同一标签不可使用重复的属性)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html lang="en" lang="zh-Hans">
  ...
</html>
```

### `HS0010`. tag name must be in lowercase (标签名必须小写)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<HTML lang="en">
  ...
</html>
```

### `HS0011`. attribute name must be in lowercase (属性名必须小写)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html LANG="en">
  ...
</html>
```

### `HS0012`. `<html>` element must have `lang` attribute (`<html>`元素必须包含`lang`属性)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  ...
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html>
  ...
</html>
```

### `HS0013`. `<html>` element must have child of `head` element (`<html>`元素必须包含`<head>`子元素)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    ...
  </head>
  <body>
    ...
  </body>
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html>
  <body>
    ...
  </body>
</html>
```

### `HS0014`. `<html>` element must have child of `body` element (`<html>`元素必须包含`<body>`子元素)

Right(正确)：

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    ...
  </head>
  <body>
    ...
  </body>
</html>
```

Wrong(错误)：

```html
<!DOCTYPE html>
<html>
  <head>
    ...
  </head>
</html>
```

### `HS0015`. `<head>` element must have child of `<title>` element (`<head>`标签必须包含`<title>`子元素)

### `HS0016`. `<title>` element must **NOT** be empty (`<title>`元素不可为空)

Right (正确):

```html
<title>Page Title</title>
```

Wrong (错误):

```html
<title></title>
```

### `HS0017`. `<p>` element must **NOT** be empty (`<p>`元素不可为空)

Right (正确):

```html
<p>Paragraph...</p>
```

Wrong (错误):

```html
<p></p>
```

### `HS0018`. `<head>` element must have child of `<meta>` element with `charset` attributee (`<head>`元素必须包含`charset`属性的`<meta>`元素)

Example as below (示例如下)：

```html
<meta charset="utf-8"/>
```

### `HS0019`. `<ul>` element must have children of `<li>` element (`<ul>`标签只能必须包含`<li>`子元素)

### `HS0020`. `<ol>` element must have children of `<li>` element (`<ol>`标签只能必须包含`<li>`子元素)

### `HS0021`. `<select>` element must have children of `<option>` element (`<select>`标签只能必须包含`<option>`子元素)

### `HS0022`. `<dl>` element must have children of `<dt>` element (`<dl>`标签必须包含`<dt>`子元素)

### `HS0023`. `<dl>` element must have children of `<dd>` element (`<dl>`标签必须包含`<dd>`子元素)

### `HS0024`. `<video>` element must have children of `<source>` element (`<video>`标签必须包含`<source>`子元素)

### `HS0025`. `<source>` element must have `src` and `type` attributes (`<source>`元素必须包含`src`和`type`属性)

### `HS0026`. `<audio>` element must have children of `<source>` element (`<audio>`标签必须包含`<source>`子元素)

### `HS0027`. `<video>` element must have `controls` attribute (`<video>`元素必须包含`controls`属性)

### `HS0028`. `<audio>` element must have `controls` attribute (`<audio>`元素必须包含`controls`属性)

### `HS0029`. `<details>` element must have child of `<summary>` element (`<details>`标签必须包含`<summary>`子元素)

### `HS0030`. `<summary>` element must **NOT** be empty (`<summary>`元素不可为空)

### `HS0031`. `<a>` element must have `href` atrribute (`<a>`标签必须包含`href`属性)

### `HS0032`. `<a>` element must **NOT** be empty (`<a>`元素不可为空)

### `HS0033`. `<img>` element must have `src` atrribute (`<img>`标签必须包含`src`属性)

### `HS0034`. non-boolean value of attribute must **NOT** be empty (非布尔值的属性值不能为空)

### `HS0035`. `<input>` element must have `type` atrribute (`<input>`标签必须包含`type`属性)

### `HS0036`. `<h1>`~`<h6>` element must **NOT** be empty (`<h1>`~`<h6>`元素不可为空)

### `HS0037`. `id` attribute value must be unique (`id`属性值必须唯一)

正确：

```html
<body>
  <p id="index">文档内容</p>
  <p id="home">文档内容</p>
</body>
```

错误：

```html
<body>
  <p id="index">文档内容</p>
  <p id="index">文档内容</p>
</body>
```

### `HS0038`. `<main>` element without `hidden` attribute must be present only **once** (不带`hidden`属性的`<main>`只能出现**一次**)

正确：

```html
<body>
  <main>主体内容</main>
  <main hidden>主体内容</main>
</body>
```

或

```html
<body>
  <main>主体内容</main>
</body>
```

错误：

```html
<body>
  <main>主体内容</main>
  <main>主体内容</main>
</body>
```

### `HS0039`. `<input>` element with `type` attribute's value is `image` must have `src` attribute (`type`属性为`image`的`<input>`必须包含`src`属性)

### `HS0040`. `<link>` element must have `src` and `rel` attributes (`<link>`元素必须包含`src`和`rel`属性)

### `HS0041`. `<link>` element must **NOT** have `type` attribute with value of `text/css` (`<link>`元素不可包含属性值为`text/css`的`type`属性)

正确：

```html
<link href="css/style.css" rel="stylesheet"/>
```

错误：

```html
<link href="css/style.css" rel="stylesheet" type="text/css"/>
```

### `HS0042`. `<script>` element must have `src` attribute (`<script>`元素必须包含`src`属性)

### `HS0043`. `<script>` element must **NOT** have `type` attribute with value of `text/javascript` (`<script>`元素不可包含属性值为`text/javascript`的`type`属性)

正确：

```html
<script src="js/js.js"></script>
```

错误：

```html
<script src="js/js.js" type="text/javascript"></script>
```

## Accessibility (可用性)

### `HA0001`. `<img>` element must have `alt` atrribute (`<img>`标签必须包含`alt`属性)

### `HA0002`. `<video>` element must **NOT** be empty (`<video>`元素不可为空)

```html
<video controls>
  <source src="example.ogg" type="video/ogg"/>
  Your browser does not support the &lt;video&gt; element.
</video>
```

### `HA0003`. `<audio>` element must **NOT** be empty (`<audio>`元素不可为空)

```html
<audio controls>
  <source src="example.ogg" type="audio/ogg"/>
  Your browser does not support the &lt;audio&gt; element.
</audio>
```

### `HA0004`. `<h1>` element must be present only **once** (`<h1>`元素只能出现**一次**)

Right (正确)：

```html
<body>
  <h1>一级标题</h1>
  <h2>二级标题</h2>
</body>
```

Wrong (错误)：

```html
<body>
  <h1>一级标题1</h1>
  <h1>一级标题2</h1>
</body>
```

### `HA0005`. `<input>` element with `type` attribute's value is `image` must have `alt` attribute (`type`属性为`image`的`<input>`必须包含`alt`属性)

### `HA0006`. `<aside>` element must **NOT** have child of `<main>` element (`<aside>`标签不可包含`<main>`子元素)

正确：

```html
<html lang="zh-Hans">
  <head>
    <meta charset="utf-8">
    <title>文档标题</title>
  </head>
  <body>
    <aside>侧边栏内容</aside>
    <main>主体内容</main>
  </body>
</html>
```

错误：

```html
<html lang="zh-Hans">
  <head>
    <meta charset="utf-8">
    <title>文档标题</title>
  </head>
  <body>
    <aside>
      侧边栏内容
      <main>主体内容</main>
    </aside>
  </body>
</html>
```

## Performance (性能)

### `HP0001`. `<script>` element must **NOT** used in `<head>` element (`<script>元素不可用于<head>元素内`)

---

### E01009. required attribute missing (必须包含特定属性)

- `<iframe>`必须包含属性`src`
- `<embed>`必须包含属性`src`
- `<input>`的`type`的属性值为`radio`的时候必须包含`name`属性
- `<output>`必须包含属性`name`、`for`
- `<meter>`必须包含属性`value`
- `<progress>`必须包含属性`value`
