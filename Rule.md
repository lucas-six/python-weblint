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
