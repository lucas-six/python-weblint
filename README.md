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

- **G0001**. file or directory not exist (文件或目录不存在)

### HTML

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
- **HS0013**. `<html>` element must have children of `head` and `body` element (`<html>`元素必须包含`<head>`和`<body>`子元素)
- **HS0014**. `<head>` element must have child of `<title>` element (`<head>`标签必须包含`<title>`子元素)
- **HS0015**. `<title>` element must **NOT** be empty (`<title>`元素不可为空)
- **HS0016**. `<p>` element must **NOT** be empty (`<p>`元素不可为空)
- **HS0017**. `<head>` element must have child of `<meta>` element with `charset` attributee (`<head>`元素必须包含`charset`属性的`<meta>`元素)
- E01015. (`id`只能是唯一)
- E01016. (`<h1>`只能出现一次)
- E01017. (不能包含特定标签)
- E01018. (`<main>`不带`hidden`只能出现一次)
- E01019. (`<script>`不能有`type="text/javascript"`属性)
- E01020. (`<link>`不能有`type="text/css"`属性)
