# Rule

## HTML

### E01001. DOCTYPE must be decalred first (文档类型必须首先声明)

正确：

```html
<!DOCTYPE html>
<html>
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
<html>
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
<html>
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
<html>
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