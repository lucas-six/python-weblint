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