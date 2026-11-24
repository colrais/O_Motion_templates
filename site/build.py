#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成展示站 index.html（读 catalog.json + 固定文案/封面映射）

用法：python site/build.py     # 在仓库根目录产出 index.html、.nojekyll
"""
import json, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"

# 只有已上线的 9 支进卡片墙；slug 用于平台链接
META = {
    "0110010001-particle-arrow-illusion": dict(
        slug="0110010001-particle-arrow-illusion", cover="cover-particle.jpg", kind="完整模板",
        line="15 秒竖屏无缝循环。盯住一个方向，视线一移它就反向旋转；改字换色即时出片。"),
    "name-plaque-card": dict(
        slug="name-plaque-card", cover="cover-namecard.jpg", kind="动效片段",
        line="3 秒竖屏身份卡。双线长框双向描边、竖排姓名逐字落下，朱印收尾。"),
    "end-card-cta": dict(
        slug="end-card-cta", cover="cover-endcard.jpg", kind="动效片段",
        line="3 秒方形片尾。加号图标 + 一句订阅语 + 胶囊 CTA 回弹，图标文案配色都是参数。"),
    "0109010001-line-story": dict(
        slug="0109010001-line-story", cover="cover-linestory.jpg", kind="完整模板",
        line="一根金线画完整条故事，旁白驱动分幕；加一幕加一句旁白，片子就跟着变长。"),
    "ink-brush-title": dict(
        slug="ink-brush-title", cover="cover-inkbrush.jpg", kind="动效片段",
        line="3 秒水墨章节卡。墨笔横扫、书法大字遮罩渐显，朱砂线与印章收住版面。"),
    "cartoon-scribble-open": dict(
        slug="cartoon-scribble-open", cover="cover-cartoon.jpg", kind="动效片段",
        line="5 秒手绘片头。黄色笔刷写在屏幕上，标题逐字彩色弹入，配四件手绘装饰。"),
    "dotmatrix-portrait-v1": dict(
        slug="dotmatrix-portrait-v1", cover="cover-dotmatrix.jpg", kind="完整模板",
        line="三张人像化作双色网点，散开又重新聚拢拼出标题——一部 13 秒的横屏开场。"),
    "geek-dark-talk-v1": dict(
        slug="geek-dark-talk-v1", cover="cover-geekdark.jpg", kind="完整模板",
        line="暗色控制台 + 数据面板 + 逐条字幕，把硬知识讲成有节奏的口播画面。"),
    "particle-form-morph-v1": dict(
        slug="particle-form-morph-v1", cover="cover-morph.jpg", kind="完整模板",
        line="八个三维形状连续形变：球体、环面、双螺旋、立方体、黑洞漩涡……换形换色即时出片。"),
}

PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>O.motion · 模板合集</title>
<meta name="description" content="自制 MotionGit 模板合集：9 支已上线，封面一张图说清它长什么样、能改什么。">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="top">
  <a class="brand" href="./">O<span>.motion</span></a>
  <nav>
    <a href="https://github.com/colrais/O_Motion_templates" target="_blank" rel="noopener">GitHub ↗</a>
    <a href="https://motiongit.com/@fangcs" target="_blank" rel="noopener">作者页 ↗</a>
    <a href="README.md">README</a>
  </nav>
</header>

<main>
<section class="hero">
  <p class="eyebrow">MOTION TEMPLATES · @fangcs</p>
  <h1>模板做成一张图就能读懂</h1>
  <p class="lead">已上线 __PUB__ 支：横屏、竖屏、方形都在这里。每张封面都是重新设计的宣传页——先看它长什么样，再决定要不要换自己的素材。</p>
  <div class="stats">
    <span><b>__TOTAL__</b> 支在库</span>
    <span><b>__PUB__</b> 支已上线</span>
    <span><b>__FULL__</b> 完整模板 · <b>__FRAG__</b> 动效片段</span>
    <span>公开模板成片均可商用</span>
  </div>
</section>

<section class="toolbar">
  <div class="filters" id="kind-filters">
    <button data-kind="all" aria-pressed="true">全部</button>
    <button data-kind="完整模板" aria-pressed="false">完整模板</button>
    <button data-kind="动效片段" aria-pressed="false">动效片段</button>
  </div>
  <div class="filters" id="ratio-filters">
    <button data-ratio="all" aria-pressed="true">全部画幅</button>
    <button data-ratio="16:9" aria-pressed="false">16:9</button>
    <button data-ratio="9:16" aria-pressed="false">9:16</button>
    <button data-ratio="1:1" aria-pressed="false">1:1</button>
  </div>
  <div class="search-row">
    <input id="q" type="search" placeholder="搜标题、编号或关键词，如 粒子 / 水墨 / 0107">
    <span id="count"></span>
  </div>
</section>

<section class="grid" id="grid"></section>
<p id="empty" hidden>没有匹配的模板，换个关键词试试。</p>
</main>

<footer>
  <p>本仓库只承载索引、封面与文档，不分发模板二进制。模板本体通过 MotionGit 平台获取；成片可否商用按各模板声明（MIT / mg-commercial）。</p>
  <p><a href="https://github.com/colrais/O_Motion_templates" target="_blank" rel="noopener">colrais/O_Motion_templates</a>
     <a href="https://motiongit.com/@fangcs" target="_blank" rel="noopener">motiongit.com/@fangcs</a></p>
</footer>

<script>
const DATA = __DATA__;
const grid = document.getElementById("grid");
const q = document.getElementById("q");
const count = document.getElementById("count");
const empty = document.getElementById("empty");
let kind = "all", ratio = "all";

function card(t){
  const spec = [t.orientation, t.duration ? t.duration : "", t.fps ? t.fps + " FPS" : "", "v" + t.version]
    .filter(Boolean).join(" · ");
  return `<article class="card" data-kind="${t.kind}" data-ratio="${t.orientation}" data-q="${t.search}">
    <div class="media"><img src="docs/assets/${t.cover}" alt="${t.name} 封面" decoding="async"><span class="badge">已上线</span></div>
    <div class="body">
      <p class="meta"><span class="kind">${t.kind}</span><span class="code">${t.code}</span></p>
      <h2>${t.name}</h2>
      <p class="line">${t.line}</p>
      <p class="spec">${spec}</p>
      <div class="links">
        <a class="primary" href="https://motiongit.com/@fangcs/${t.slug}" target="_blank" rel="noopener">查看模板 ↗</a>
        ${t.doc ? `<a href="${t.doc}">说明文档</a>` : ""}
        <a href="docs/assets/${t.cover}" target="_blank" rel="noopener">封面原图</a>
      </div>
    </div>
  </article>`;
}

function render(){
  const kw = (q.value || "").trim().toLowerCase();
  const list = DATA.filter(t => (kind === "all" || t.kind === kind) &&
                                (ratio === "all" || t.orientation === ratio) &&
                                (!kw || t.search.includes(kw)));
  grid.innerHTML = list.map(card).join("");
  count.textContent = list.length + " / " + DATA.length;
  empty.hidden = list.length > 0;
}

document.querySelectorAll("#kind-filters button").forEach(b => b.onclick = () => {
  kind = b.dataset.kind;
  document.querySelectorAll("#kind-filters button").forEach(x => x.setAttribute("aria-pressed", x === b));
  render();
});
document.querySelectorAll("#ratio-filters button").forEach(b => b.onclick = () => {
  ratio = b.dataset.ratio;
  document.querySelectorAll("#ratio-filters button").forEach(x => x.setAttribute("aria-pressed", x === b));
  render();
});
q.addEventListener("input", render);
render();
</script>
</body>
</html>
"""


def main():
    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    all_items = cat["templates"]
    pub = [t for t in all_items if t.get("status") == "published"]

    rows = []
    for t in pub:
        m = META.get(t["id"])
        if not m:
            continue
        dur = t.get("durationSec")
        dur_s = ""
        if dur:
            dur_s = f"{int(dur)}s" if dur < 60 else f"{int(dur) // 60}m{int(round(dur % 60)):02d}s"
        rows.append(dict(
            code=t["code"], name=t["name"].split("（")[0], version=t["version"],
            orientation=t["orientation"], duration=dur_s, fps=t.get("fps"),
            kind=m["kind"], slug=m["slug"], cover=m["cover"], line=m["line"],
            doc=t.get("doc") or "",
            search=" ".join([t["name"], t["code"], m["line"], m["kind"]]).lower(),
        ))

    full = sum(1 for r in rows if r["kind"] == "完整模板")
    frag = len(rows) - full
    body = (PAGE.replace("__PUB__", str(len(rows)))
                .replace("__TOTAL__", str(len(all_items)))
                .replace("__FULL__", str(full))
                .replace("__FRAG__", str(frag))
                .replace("__DATA__", json.dumps(rows, ensure_ascii=False)))
    (ROOT / "index.html").write_text(body, encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"index.html written: {len(rows)} cards, {len(all_items)} in catalog")


if __name__ == "__main__":
    main()

