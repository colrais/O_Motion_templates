# 暗场极客知识口播（geek-dark-talk-v1）

暗场科技风的知识口播模板：只给结构化脚本 `sections`，语义层自动把内容映射到匹配镜头，原生无署名、无时码、无第三方品牌标，时长按内容与口播伸缩。

| 项 | 值 |
|---|---|
| 模板 id | `geek-dark-talk-v1` |
| 版本 | v1.0.1 |
| 来源性质 | 成片参照 |
| 运行时 | `html-canvas/1` |
| 画幅 / 帧率 / 时长 | 1920×1080 / 60 fps / 4 min 29 s（默认样例；时长按内容伸缩） |
| 许可 | MIT（第三方字体与素材遵循包内各自许可） |
| 网络依赖 | 无（离线可渲染） |
| 状态 | 已发布（MotionGit，[作品页](https://motiongit.com/@fangcs/geek-dark-talk-v1)，下载量 14，2026-11-16 实抓复核） |
| 确定性 | 固定随机种子，同一参数 + 同一时间点多次渲染哈希一致 |

---

## 画面结构

14 个成品级场景：开场 → 预览 → 分层介绍 → 总览 → 规则 → 8 招正文 → 收口。画面全部由代码程序化生成（颗粒 / 网格 / 辉光内置），无外部图片随包；字体缺省回退系统字体。

语义层按 12 类角色自动选镜头：

| 角色 | 含义 |
|---|---|
| `hook` | 开场钩子 |
| `statement` | 观点陈述 |
| `overview` | 全局总览 |
| `list` | 要点列举 |
| `spatial` | 空间 / 布局关系 |
| `parameter` | 参数 / 数值面板 |
| `path` | 路径 / 走向 |
| `compare` | 双项对比 |
| `focus` | 强调聚焦 |
| `process` | 流程 / 时间线 |
| `transition` | 段落过渡 |
| `closing` | 收口 |

## 可改参数

参数契约文件：`params.schema.json`（打包在模板内）。最小输入只需 `sections`：

```json
{
  "sections": [
    { "id": "open", "title": "标题", "lines": ["第一句", "第二句"] }
  ]
}
```

| 参数 | 类型 | 约束 | 说明 |
|---|---|---|---|
| `sections` | array | 必填 | 结构化脚本；作者只给标题 / 句子 / 要点 / 可选 role，不逐槽填字 |
| `meta` | object | — | 元信息 |
| `media` | object | — | slot 到素材路径的绑定；未绑定的 slot 自动落占位符 |
| `audio` | object | — | 可选；原始音轨给路径，渲染器自动裁 / 补到精确时钟并做响度归一 |
| `srt` | string | — | 可选；SRT 路径，渲染器内置解析为字幕 |
| `timing` | object | — | 时间节奏 |
| `durationSeconds` | number | 4 – 600 | 目标总时长；缺省按 sections 与口播 / SRT 自动决定 |

## 渲染

```bash
node _render/render.mjs --data <json> --out <mp4>
```

可选 `--srt / --voice / --music / --sfx`，可选 `--width / --height / --fps`（默认 1920×1080@60）。ffmpeg 经 `FFMPEG_DIR` 注入，不写死本机路径。

## 使用建议

- **脚本写法**：`sections` 里每条 `lines` 对齐一句口播；语义层按句意与时长挑镜头，写得太碎会频繁切镜，写得太长会拖节奏
- **素材替换**：不提供素材也能完整出片（程序化占位）；要给真实画面时按 slot 绑定到对应素材位
- **口播对齐**：给 `audio` 或 `srt` 后以音轨时长为锚，画面逐句对齐；不给则按内容自动估时长
- **响度**：渲染器自带总轨母带响度（目标 −14 LUFS，真峰值不削波），外部 BGM 建议单独给 `music`

## 已知限制

- v1.0.1 修复了 720p / 高分辨率输出时字幕被视口裁切、大部分时间不显示的问题（渲染器强制页面视口精确等于目标分辨率，字幕在 `renderAt` 内与画面同帧渲染）
- 缺素材时落程序化占位标记，可正常出片但不是成品效果
- 只支持横屏 16:9
- 平台标注 Beta：模板库按日更新，使用前建议让助手先检查更新

## 获取

MotionGit 模板页（已发布开放，免费 MIT）：

- 作品页：[geek-dark-talk-v1](https://motiongit.com/@fangcs/geek-dark-talk-v1)
- 作者主页：[@fangcs](https://motiongit.com/fangcs)

> 下载得到的 `.motion` 内含**个人 API key**，请勿公开分享包体；分享模板链接即可。
