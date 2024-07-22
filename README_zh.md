# notion 任務接待員
![cover](./img/cover.png)
![English](./README.md)
<!-- creadit :pixai.art-->
## 簡介
### 這是什麼？

這個程式會自動從我的任務清單隨機選擇一件事放到今天任務指派給我做，你可以設定排成每天自動執行他一次抽取任務卡。只需要預先在 notion 資料庫中輸入未完成的任務並標記為 random ，只要這些任務一天沒做完，它就有機會浮上來提醒今天是做這件事的良辰吉日

## setup
- 在 notion 建立可以被操作的表格和自動化連接(Integrations)，這是我的程式使用的資料庫 [click me](https://grave-milk-49d.notion.site/327582f4f57245dba861699bcef48139?pvs=4)

- 確定你安裝了 python
- 把 .env.example 的環境變數更改為你的使用情境，包括你的 notion token 、要操作的表格並重新命名為 .env
- 找個機器定期執行 main.py

## [分解步驟](./stepBystep/how-to-do.md)