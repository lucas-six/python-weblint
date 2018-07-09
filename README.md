# WebLint

The Web Code Quality Tool, including both **front-end** (HTML, CSS, JavaScript) and **back-end** (Python/Django).

一个Web代码质量评测工具，包括**前端**（HTML，CSS，JavaScript）和**后端**（基于Python/Django框架）

## Features（特性）

- Code Quality Verification (代码质量验证)
  - HTML
- Command Line Options (命令行选项)
  - `source` (required)(必选项): source files (源文件)

## Code Rules（代码规则）

### Illustration (规则说明)

- `H`: Rule for **HTML**
- `C`: Rule for **CSS**
- `J`: Rules for **JavaScript**
- `G`: **Global** rules (全局)
- `S`: Rules for **Specification** (规范)
- `A`: Rules for **Accessibility** (可用性)

### Global (全局)

- **G00001**. file or directory not exist (文件或目录不存在)

### HTML

#### Specification (规范)

- **HS0001**. DOCTYPE must be decalred first (文档类型必须首先声明)
- **HS0002**. DOCTYPE for HTML5 should be `<DOCTYPE html>` (HTML5的文档类型必须是`<DOCTYPE html>`)
- **HS0003**. invalid tag must **NOT** be used (不可使用非法标签)
- **HS0004**. deprecated tag must **NOT** be used (不可使用废弃标签)
- **HS0005**. tag must be paired (双标签必须成对，自闭合标签必须闭合)
- **HS0006**. empty tag must be closed by self (空标签必须自闭合)
- **HS0007**. invalid attribute must **NOT** be used (不可使用非法属性)
- **HS0008**. deprecated attribute must **NOT** be used (不能使用废弃的属性)
- **HS0009**. attribute name must **NOT** be duplication in the same element (同一标签不可使用重复的属性)
- **HS0010**. tag name must be in lowercase (标签名必须小写)
- **HS0011**. attribute name must be in lowercase (属性名必须小写)
- **HS0012**. `<html>` element must have `lang` attribute (`<html>`元素必须包含`lang`属性)
- **HS0013**. `<html>` element must have one child of `head` element (`<html>`元素必须包含一个`<head>`子元素)
- **HS0014**. `<html>` element must have one child of `body` element (`<html>`元素必须包含一个`<body>`子元素)
- **HS0015**. `<head>` element must have one child of `<title>` element (`<head>`标签必须包含一个`<title>`子元素)
- **HS0016**. `<title>` element must **NOT** be empty (`<title>`元素不可为空)
- **HS0017**. `<p>` element must **NOT** be empty (`<p>`元素不可为空)
- **HS0018**. `<head>` element must have one child of `<meta>` element with `charset` attributee (`<head>`元素必须包含一个`charset`属性的`<meta>`元素)
- **HS0019**. `<ul>` element must have children of `<li>` elements (`<ul>`标签只能必须包含`<li>`子元素)
- **HS0020**. `<ol>` element must have children of `<li>` elements (`<ol>`标签只能必须包含`<li>`子元素)
- **HS0021**. `<select>` element must have children of `<option>` elements (`<select>`标签只能必须包含`<option>`子元素)
- **HS0022**. `<dl>` element must have children of `<dt>` elements (`<dl>`标签必须包含`<dt>`子元素)
- **HS0023**. `<dl>` element must have children of `<dd>` elements (`<dl>`标签必须包含`<dd>`子元素)
- **HS0024**. `<video>` element must have children of `<source>` elements (`<video>`标签必须包含`<source>`子元素)
- **HS0025**. `<source>` element must have `src` and `type` attributes (`<source>`元素必须包含`src`和`type`属性)
- **HS0026**. `<audio>` element must have children of `<source>` elements (`<audio>`标签必须包含`<source>`子元素)
- **HS0027**. `<video>` element must have `controls` atrribute (`<video>`标签必须包含`control`属性)
- **HS0028**. `<audio>` element must have `controls` atrribute (`<audio>`标签必须包含`control`属性)
- **HS0029**. `<details>` element must have child of `<summary>` element (`<details>`标签必须包含`<summary>`子元素)
- **HS0030**. `<summary>` element must **NOT** be empty (`<summary>`元素不可为空)
- **HS0031**. `<a>` element must have `href` atrribute (`<a>`标签必须包含`href`属性)
- **HS0032**. `<a>` element must **NOT** be empty (`<a>`元素不可为空)
- **HS0033**. `<img>` element must have `src` atrribute (`<img>`标签必须包含`src`属性)
- **HS0034**. non-boolean value of attribute must **NOT** be empty (非布尔值的属性值不能为空)
- **HS0035**. `<input>` element must have `type` atrribute (`<input>`标签必须包含`type`属性)
- **HS0036**. `<h1>`-`<h6>` element must **NOT** be empty (`<h1>`-`<h6>`元素不可为空)
- **HS0037**. `id` attribute value must be **unique** (`id`属性值必须**唯一**)
- **HS0038**. `<main>` element without `hidden` attribute must be present only **once** (不带`hidden`属性的`<main>`只能出现**一次**)
- **HS0039**. `<input>` element with `type` attribute's value is `image` must have `src` attribute (`type`属性为`image`的`<input>`必须包含`src`属性)
- **HS0040**. `<link>` element must have `href` and `rel` attributes (`<link>`元素必须包含`href`和`rel`属性)
- **HS0041**. `<link>` element must **NOT** have `type` attribute with value of `text/css` (`<link>`元素不可包含属性值为`text/css`的`type`属性)
- **HS0042**. `<script>` element must have `src` attribute (`<script>`元素必须包含`src`属性)
- **HS0043**. `<script>` element must **NOT** have `type` attribute with value of `text/javascript` (`<script>`元素不可包含属性值为`text/javascript`的`type`属性)
- **HS0044**. `<figure>` element must have child of `<figcaption>` element (`<figure>`元素必须包含`<figcaption>`子元素)
- **HS0045**. `<progress>` element must have `value` and `max` attributes (`<progress>`元素必须包含`value`和`max`属性)

#### Accessibility (可用性)

- **HA0001**. `<img>` element must have `alt` atrribute (`<img>`标签必须包含`alt`属性)
- **HA0002**. `<video>` element must **NOT** be empty (`<video>`元素不可为空)
- **HA0003**. `<audio>` element must **NOT** be empty (`<audio>`元素不可为空)
- **HA0004**. `<h1>` element must be present only **once** (`<h1>`元素只能出现**一次**)
- **HA0005**. `<input>` element with `type` attribute's value is `image` must have `alt` attribute (`type`属性为`image`的`<input>`必须包含`alt`属性)
- **HA0006**. `<aside>` element must **NOT** have child of `<main>` element (`<aside>`标签不可包含`<main>`子元素)

#### Performance (性能)

- **HP0001**. `<script>` element must **NOT** used in `<head>` element (`<script>元素不可用于<head>元素内`)
