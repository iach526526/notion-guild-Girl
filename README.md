# Notion Guild Girl

![cover](./img/cover.png)

[![](https://img.shields.io/badge/翻譯-繁體中文-blue)](./README_zh.md)
<!-- credit: pixai.art -->
## Introduction
### What is this?

This program will automatically select a task from my task list randomly and assign it to me for today's tasks. You can set it to automatically execute once a day to draw a task card. You just need to input unfinished tasks in the Notion database and mark them as random. As long as these tasks are not completed within a day, they have a chance to come up and remind you that today is a good day to do this task.

## Setup
- Create an operable table and automation connection (Integrations) in Notion. This is the database my program uses [click me](https://grave-milk-49d.notion.site/327582f4f57245dba861699bcef48139?pvs=4).

- Make sure you have Python installed.
- Change the environment variables in `.env.example` to your use case, including your Notion token and the table to operate on, and rename it to `.env`.
- Find a machine to run `main.py` regularly.

## [Step-by-Step Guide](./stepBystep/how-to-do.md)
