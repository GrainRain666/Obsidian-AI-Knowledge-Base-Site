---
type: concept
topic: Obsidian
created: 2026-11-16
tags:
  - type/concept
  - 研读中
---

# {{Obsidian 核心模板与 Templater 的区别}}

## 一句话定义
Obsidian 核心模板能填写日期、时间、标题等内置变量；Templater 还能执行函数和脚本，完成更灵活的自动填写。

## 核心机制
两个插件识别的模板语法不同。

核心模板识别它支持的变量，例如 {{date}}。Templater 的日期函数写成 <% tp.date.now("YYYY-MM-DD") %>。

如果用核心模板的“插入模板”命令插入 Templater 代码，这段代码会被当作文字留下，不会自动变成日期。

手动插入 Templater 模板时，应使用：
Templater: Open insert template modal

如果已经插入了代码，可以在实际笔记中运行：
Templater: Replace templates in the active filegua

## 应用场景

- 场景1：
- 场景2：

## 与其他概念的链接

- [[相关概念1]] —— 关系说明

## 来源笔记

> 「原句引用」——《来源》

## 理解演变

- {{date}}：初次记录
