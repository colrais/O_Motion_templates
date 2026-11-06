# 使用与渲染说明

适用于合集内所有 `.motion` 模板。

## 环境

| 组件 | 要求 |
|---|---|
| Node.js | 22+（v24 已验证） |
| Chromium | Playwright 管理，headless 可用 |
| FFmpeg / ffprobe | 需含 `libx264`，抽帧用 `-frames:v 1` 编号序列（`pattern_type glob` 在部分构建上不可用） |
| 输出规格 | 由模板 `motion.json` 的 `output` 声明决定（分辨率 / 帧率 / 时长） |

## 参数替换

1. 读模板内 `params.schema.json`：每个可改字段都有 `type` / `minimum` / `maximum` / `maxLength`，按契约填值
2. 图片类参数传图片路径；颜色类传 `#RRGGBB`
3. 时间点参数（如 `tP1End`）是**绝对时间**，改总时长时必须同步改时间点
4. 文本参数注意：`maxLength` 只是上限提示，实现侧通常另有字号自适应，超长仍可能变小或溢出——以实际出片为准

## 渲染

- 命令行链路：`omotion` 子命令一律用**位置参数**（`validate` / `doctor` / `probe` / `audit` 传 `--template` 会报错）
- `doctor` 认**模板目录**，`validate` 认 **`.motion` 文件（ZIP）**，两者口径相反
- 打包成 `.motion` 后若静态检查失败，不会有产物输出——先看检查报告再重试

## 常见坑

- **视口不等于窗口**：`--window-size=1920,1080` 的实际视口约 1898×982，按画布尺寸直接截图会裁掉右侧与底部；必须用 `Emulation.setDeviceMetricsOverride` 强制视口
- **自动循环**：模板默认不应自动 rAF 循环，否则与逐帧截图抢时钟导致抖动；只允许显式开启（如 `?play=1`）
- **确定性校验**：同一参数 + 同一时间点应得到同帧哈希；不稳定先查随机种子
- **Chrome 调试端口**：不要写死或纯随机，可能撞上常驻进程，表现为 CDP 超时

## 许可

各模板许可以其 `motion.json` / MotionGit 页面为准；本仓库文档为 MIT。
