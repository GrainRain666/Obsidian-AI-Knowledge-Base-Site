---
tags:
  - type/moc
topic: Obsidian
---

# AI 捕获概览

运行命令“QuickAdd：AI捕获笔记”，输入内容和来源。新笔记保存在 07-Inbox/AI捕获，摘要、标签和关键词写入顶部属性。

以下清单读取每篇笔记的 summary 字段，新增笔记后自动更新。点击标题查看原文和来源；核对后把 ai_review 改为“已核对”。

```dataview
LIST WITHOUT ID link(file.path, title) + "：" + summary + "（" + ai_review + "）"
FROM "07-Inbox/AI捕获"
WHERE type = "ai-capture"
SORT file.ctime DESC
```

## 使用边界

- AI 只处理本次输入的内容，复用 Smart Composer 当前选中的模型和接口。
- 来源填写真实网址、书名或“本人输入”，原始内容保留在生成的笔记里。
- 标签、关键词和摘要是 AI 提取结果，默认标为“待核对”。
- 如果生成失败，笔记保留原文，核对状态显示“生成失败”。
- 原有“记录灵感”命令继续用于不调用 AI 的快速记录。
