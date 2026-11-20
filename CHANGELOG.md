# 变更记录

## 2026-11-21

- **登记 4 支动效片段（新增「动效片段」分组）**：`cartoon-scribble-open`（卡通涂鸦片头，v1.0.2）、`ink-brush-title`（水墨书法标题卡，v1.0.2）、`name-plaque-card`（竖排姓名身份卡，v1.0.0）、`end-card-cta`（片尾关注卡，v1.1.0）四条 `published` 条目，各带编号 `0107010001`–`0107040001`、`contentType: motion-fragment`、placement（opening/chapter/insert/ending）与独立说明页。本体在资产层私密仓，合集只登记能力与获取方式。
- **如实标注**：水墨书法标题卡的「font 为空时主标题退回小字号」缺陷写进条目 notes 与说明页；三支片段下载量未采集，不填估算值；片尾关注卡沿用 2026-11-20 回读的 22 次下载。
- counts：total 7→11，`published` 3→7，`publicDownloadable` 3→7；`generatedAt` 2026-11-21。
- **补登记资产层 2 支**：新增 `0106010001`（幼儿园日常宣传·综合叙事，`0106010001-kindergarten-daily` v0.1.0，自研 node-cdp 含 motiongit 适配，官方 inspect 7/7 已过，本期不上架）与 `0104010001`（化学课件·中学，`chemistry-middle-courseware-v1` v0 目录型）两支 `draft-private` 条目，仅作可发现性登记，不分发本体。
- **清理虚条**：删除 `board-writing-english-v2`（v2.0.0）——该 id/版本在全库无对应资产仓，属误登记；板书模板目前只在主项目工作区（`board-lecture-english-patterns-v1` v1.0.0），待独立成仓后再回到合集，`docs/board-writing-english.md` 暂保留。
- **加编号追溯列**：`catalog.json` 每条补 `code` 字段（10 位资产编号），README「模板一览 / 暂未公开发布」两表加「编号」列，与《项目配置指令》§三 子工程登记表、主项目 `模板库清单.md §一.5` 三处同源。
- counts：total 6→7，`draft-private` 0→2，`shelved` 3→2；`generatedAt` 2026-11-21。

## 2026-11-17

- **两支升级公告过审、粒子新身份过审**：点阵肖像 v1.5.0、暗场极客 v1.3.1、3D粒子形变（新身份首次发布）v1.3.1 均已通过审核并对其他用户可见
- 实抓作品页复核并回写数字：点阵肖像 v1.5.0 / 下载 **119**；暗场极客 v1.3.1 / 下载 **21**；3D粒子形变 v1.3.1 / 下载 **4**（三页 HTTP 200）
- `catalog.json`：三支 `version` 与 `publish.downloads` 更新，粒子 `status` 由 `in-review` 改为 `published`（counts：published 2→3、in-review 1→0、publicDownloadable 2→3、generatedAt 2026-11-17）；README 模板表与两份说明页同步
- **补充版本可见性口径**：平台上提交过的历史版本，只有**曾发布成功**的版本对其他用户可见，审核中或审核通过但未对外发布的版本仅作者本人可见，因此作品页版本号可能跳号（点阵页对外可见 v1.5.0 / v1.1.0 / v1.0.0，中间版本不对外）。已在 README「状态口径」下加注说明

## 2026-11-16

- **全仓术语与旧标识清理**：废弃"仿制"一词，来源性质统一为四档（原创 / 成片参照 / 契约参照 / 二次开发）；`catalog.json` 的 `source` 全部按四档重写，光带成字条目去掉旧标识前缀、名称去掉旧词后缀；README 增加四档说明表，展示页与说明页同步改写（历史条目保留当时措辞，不改写过去记录）
- 实抓三支公开作品页复核现状：点阵肖像 v1.1.0、下载 106；暗场极客 v1.0.1、下载 14；粒子新身份审核中暂不可访问（404），过审后再回写下载量
- 3D粒子以新身份 `particle-form-morph-v1` 重发并提交审核：原身份把旧来源词写进了平台固定地址，升版本无法修改，只能下架后换新身份；原身份已下架留档、号位不回收
- 补登 `catalog.json` 新条目（status `in-review`，counts total 5→6、in-review 0→1、generatedAt 2026-11-16），README 模板表同步加行
- 新身份来源按四档口径记为成片参照，许可 MIT

## 2026-11-15（巡检二次复核）

- 巡检实测两支已发布作品页可访问；下载量按新判据回写：点阵肖像 87 → **91**，暗场极客 33 → **4**
- **修正计数判据**：作品页下载量节点为 `<span class="exact-count" title="N">N<span class="exact-count-tip">N</span></span>`，悬浮提示会重复同一个数字；对整段文本做抓取会出现 "9191"/"44" 这类拼接假象，早期记录里的 "33" 即 "3" 与提示 "3" 拼接所致
- 新判据：以 `.exact-count` 节点的 `title` / `aria-label` 属性值为准（服务端 HTML 与真实浏览器 DOM 两处交叉验证）；不再直接取文本节点数字
- 同步 `catalog.json`（downloads 91 / 4、generatedAt 2026-11-15）、README 模板表与两份说明页

## 2026-11-15

- 暗场极客 `geek-dark-talk-v1` 审核通过并公开，实抓作品页复核（HTTP 200，v1.0.1，下载 **33**，更新于 12 小时前），按 11-14 约定补登本仓
- 新增 `docs/geek-dark-talk.md`；`catalog.json` 增条目并更新 counts（total 4→5、published 1→2、publicDownloadable 1→2、generatedAt 2026-11-15）
- README 模板表与仓库结构同步补行

## 2026-11-14

- 巡检实测作品页可访问，下载量 57 → **87**（页面"关于"区现抓，更新于 7 天前）
- 同步 `catalog.json`（downloads 87 / generatedAt 2026-11-14）、README 模板表与 `docs/dotmatrix-portrait.md`
- 暗场极客 `geek-dark-talk-v1` 已在 MotionGit 提交 v1.0.1 审核（templateId 1002 / releaseId 1230）；**审核通过前不登记本仓**，通过后再补条目并更新 counts

## 2026-11-11

- 巡检实测作品页 `https://motiongit.com/@fangcs/dotmatrix-portrait-v1` 可访问，下载量 45 → **57**
- 修正一处判据：`motiongit.com/fangcs` 个人页的模板列表由前端 JS 渲染，静态抓取显示「0 templates」属假象，**不能作为发布状态判据**；判据以作品页可访问 + 页面下载数 + 重载版本为准
- 同步 `catalog.json`（downloads 57 / generatedAt 2026-11-11）、README 模板表与 `docs/dotmatrix-portrait.md`

## 2026-11-10

- 巡检确认 `dotmatrix-portrait-v1` 在 MotionGit 已公开发布，作品页 `https://motiongit.com/@fangcs/dotmatrix-portrait-v1` 实测 HTTP 200
- 补齐 `publish.url`（此前为 null）；下载量按当日实测 23 → 45；`counts.publicDownloadable` 0 → 1
- 同步 README 模板表状态列、`docs/dotmatrix-portrait.md` 状态与获取链接

## 2026-11-08

- `dotmatrix-portrait-v1` 点阵肖像在 MotionGit 审核通过，状态由 `in-review` 改为 `published`，下载量 23；`publish.url` 暂缺（未取得具体链接），保持 null
- 同步更新 `catalog.json`（counts：published 1 / in-review 0）、README 模板表与 `docs/dotmatrix-portrait.md`

## 2026-11-07

- 新增 `docs/assets/preview-title.jpg`（1600×824，280 KB）：点阵肖像 v1.0.0 成片结尾标题帧，作为 README 与说明页预览
  - 该帧已裁掉原片底部/右侧渲染视口残留（画布 1920×1080 实际只有 1899×982 有内容）
  - 人像帧涉及示例人物肖像，不放入公开仓
- 合集仓库建立，收录 4 条自有模板登记：
  - `dotmatrix-portrait-v1` 点阵肖像 — 审核中（MotionGit）
  - 光带成字（当时的标识带旧来源词前缀）— 本地留存
  - `seaside-portrait-vertical` 海边电影感·竖屏 — 本地留存
  - `board-writing-english-v2` 板书讲解·英语句式 — 本地留存
  - 注：本条记录当时使用的旧术语与旧标识，已于 2026-11-16 统一为四档来源性质，历史记录不改写
- 明确口径：仓库只承载索引与文档，不分发模板二进制；不含凭据与本机路径
