# WebLint

The Web Code Quality Tool, including both front-end (HTML, CSS, JavaScript) and back-end (Python/Django).

一个Web代码质量评测工具，包括前端（HTML，CSS，JavaScript）和后端（基于Python/Django框架）

## Features（特性）

- Code Quality Verification
  - HTML
- Command Line Options
  - source

## Rules（代码规则）

### Global (全局)

- E00001. file or directory not exist (文件或目录不存在)

### HTML

- E01001. DOCTYPE must be decalred first (文档类型必须首先声明)
- E01002. DOCTYPE for HTML5 should be "&lt;DOCTYPE html&gt;" (HTML5的文档类型必须是"&lt;DOCTYPE html&gt;")
- E01003. invalid tag (不可使用非法标签)
- E01004. deprecated tag (不可使用废弃标签)
- E01005. tag must be paired (标签必须成对)
- E01006. invalid attribute (不可使用非法属性)
- E01007. deprecared attribute (不能使用废弃的属性)
- E01008. required element missing (必须包含特定标签)
- E01009. required attribute missing (必须包含特定属性)
- E01010. duplicated attribute (同一标签不可使用重复的属性)
- E01011. tag name must be in lowercase (标签名必须小写)
- E01012. attribute name must be in lowercase (属性名必须小写)
- E01013. "title" element must not be empty (title标签不可为空)
