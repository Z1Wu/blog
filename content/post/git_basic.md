---
title: "Git_basic"
date: 2018-09-20T17:40:31+08:00
draft: true
tags: ["git"]
categories: ["git_basic"]
---

# 粒度
git 的修改粒度是行, 也就是存储和修改冲突的最小单位是行，而不是文件

# 优点

如果git的修改粒度不是行，而是文件的话，那么每一个commit所形成的新版本都会占据大量的空间，而且该版本和旧版本之间，存在有大量的相同的内容。

# .git 文件


## 文件结构
![](/images/git_basic/git_file_structure.png)
## 具体作用
- index
    - 这个文件是我们在使用 ` git add ` 修改的

