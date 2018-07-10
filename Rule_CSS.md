# Rules for CSS

## Possible Errors (潜在错误)

### `box-model`

This rule is aimed at eliminating unwanted box model sizing issues. As such, the rule warns when it finds:

- `width` being used with `border`, `border-left`, `border-right`, `padding`, `padding-left`, or `padding-right`
- `height` being used with `border`, `border-top`, `border-bottom`, `padding`, `padding-top`, or `padding-bottom`

If the `box-sizing` property is specified, then the rule does not emit any warnings for the above conditions as it assumes you know what you're doing.

设置`width`或`height`的同时，还设置`border*`或`padding*`，则必须设置`box-sizing`.

Right (正确):

```css
/* width and border with box-sizing */
.mybox {
    box-sizing: border-box;
    border: 1px solid black;
    width: 100px;
}

/* width and border-top */
.mybox {
    border-top: 1px solid black;
    width: 100px;
}

/* height and border-top of none */
.mybox {
    border-top: none;
    height: 100px;
}
```

Wrong (错误):

```css
/* width and border */
.mybox {
    border: 1px solid black;
    width: 100px;
}

/* height and padding */
.mybox {
    height: 100px;
    padding: 10px;
}
```

### `display-property-grouping`

This rule is aimed at flagging properties that don't work based with the `display` property being used. The ultimate goal is to produce a smaller, clearer CSS file without unnecessary code. As such, the rule warns when it finds:

- `display: inline` used with `width`, `height`, `margin`, `margin-top`, `margin-bottom`, and `float`.
- `display: inline-block` used with `float`.
- `display: block` used with `vertical-align`.
- `display: table-*` used with `margin` (and all variants) or `float`.

设置`display`属性时，不能包含其他不必要的代码，如

- 设置`display:inline`，又设置`width`, `height`, `margin`, `margin-top`, `margin-bottom`, 和 `float`值
- 设置`display:inline-block`，又设置`float`值
- 设置`display:block`，又设置`vertical-align`值
- 设置`display:table-*`，又设置`margin-*`和`float`值

Right (正确):

```css
/* inline with margin-left */
.mybox {
    display: inline;
    margin-left: 10px;
}

/* table and margin */
.mybox {
    display: table;
    margin-bottom: 10px;
}
```

Wrong (错误):

```css
/* inline with height */
.mybox {
    display: inline;
    height: 25px;
}

/* inline-block with float */
.mybox {
    display: inline-block;
    float: left;
}

/* table-cell and margin */
.mybox {
    display: table-cell;
    margin: 10px;
}
```

### `duplicate-properties`

不允许包含重复的样式属性

### `empty-rules`

不允许包含空样式规则

### `known-properties`

不允许使用不识别的样式属性

## Compatibility (兼容性)

### `adjoining-classes`

不要使用相邻选择器，如`.a.b{}`

### `box-sizing`

`box-sizing`不要与相关属性同用

### `compatible-vendor-prefixes`

需要兼容第三方前缀

### ~~`gradients`~~

~~需要所有的渐变定义~~

### `text-indent`

不能使用负值

### `vendor-prefix`

第三方前缀和标准属性一起使用

### ~~`fallback-colors`~~

~~需要指定备用颜色~~

### `star-property-hack`

不能使用`*`hack

### `underscore-property-hack`

不能使用`_`hack

### `bulletproof-font-face`

需要使用备用字体

## Performance (性能)

### `font-faces`

不能使用超过5个web字体

### `import`

禁止使用`@import`

### `regex-selectors`

禁止使用属性选择器中的正则表达式选择器

### `universal-selector`

禁止使用通用选择器`*`

### `unqualified-attributes`

禁止使用不规范的属性选择器

### `zero-units`

`0`后面不要加单位

### `overqualified-elements`

使用相邻选择器时，不要使用不必要的选择器

### `shorthand`

简写样式属性

### `duplicate-background-images`

相同的url在样式表中不超过一次

## Maintainability & Duplication (可维护性)

### `floats`

不使用超过10次的浮动

### `font-sizes`

不使用超过10次的`font-size`

### `ids`

不使用`id`选择器

### `important`

不使用`!important`

## Accessibility (可访问性)

### `outline-none`

禁用`outline:none`

## OOCSS

### `qualified-headings`

<h1-h6>应该被设置为顶级样式，所以`.box h3{}`会提示警告；而`h3{}`则不会

### `unique-headings`

当多个规则定义针对同一标题的属性时，会出现警告
