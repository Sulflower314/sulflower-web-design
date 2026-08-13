# Sulflower Web Design

一套面向 AI 编程代理的开源前端设计 Skill。它帮助 Agent 设计、构建、还原、改进和评审具有品牌识别度的浏览器界面，同时尊重已有代码库的框架、组件、设计变量和工程约束。

[English](README.en.md) · [贡献指南](CONTRIBUTING.md) · [安全政策](SECURITY.md) · [MIT License](LICENSE)

## 特性

- 支持从零创建、扩展现有产品、还原设计稿和渐进式改版四种工作模式。
- 保留克制的配色方法、品牌色优先、`oklch()` 色彩推导与语义化颜色体系。
- 保留排版、留白、视觉层级、动效和反 AI 模板审美规范。
- 内置 25 套按需加载的设计风格配方。
- 适配原生 HTML/CSS/JavaScript、React 原型及现有仓库的原生技术栈。
- 包含品牌素材、使用授权、响应式、无障碍、性能和视觉验收要求。
- 主文件负责决策与路由，详细规范按需加载，减少无关上下文占用。

## 适用场景

- Landing Page、品牌官网和产品页面
- Dashboard 和数据可视化
- 可点击原型和 UI Mockup
- 截图、Figma 或参考稿还原
- 现有产品新增页面、组件或流程
- 响应式改版和视觉质量提升
- HTML 演示文稿和时间轴动画
- 设计系统定义与界面评审

不适用于后端 API、CLI 工具、无视觉要求的数据处理或纯逻辑编程任务。

## 仓库结构

```text
sulflower-web-design/
├── README.md
├── README.en.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── skill/
    └── sulflower-web-design/
        ├── SKILL.md
        ├── manifest.json
        ├── agents/openai.yaml
        └── references/
```

`skill/sulflower-web-design/` 是可以直接安装的完整 Skill 目录。仓库根目录中的文件仅服务于 GitHub 项目介绍、协作和发布。

## 安装

将完整的 `skill/sulflower-web-design/` 目录复制到代理能够发现 Skill 的位置。

### Codex 用户级安装

macOS / Linux：

```bash
cp -R skill/sulflower-web-design ~/.codex/skills/sulflower-web-design
```

Windows PowerShell：

```powershell
Copy-Item -Recurse -Force .\skill\sulflower-web-design "$env:USERPROFILE\.codex\skills\sulflower-web-design"
```

### 项目级安装

对于支持项目级 Agent Skills 的工具，可复制到：

```text
your-project/.agents/skills/sulflower-web-design/
```

不同工具的 Skill 搜索路径可能不同，请以对应工具当前文档为准。

## 使用

显式调用：

```text
Use $sulflower-web-design to design a polished product landing page.
```

中文示例：

```text
使用 $sulflower-web-design 在现有 React 项目中新增一个与当前设计系统一致的数据分析页面。
```

```text
使用 $sulflower-web-design 将这张截图还原成响应式网页，先保留原始排版和配色。
```

```text
使用 $sulflower-web-design 评审这个页面的视觉层级、交互状态和无障碍问题。
```

## 核心工作流

```text
核验不稳定事实
→ 判断 Create / Extend / Reconstruct / Improve 模式
→ 阅读代码、素材和品牌上下文
→ 形成简短 Design Read
→ 声明设计系统与保留契约
→ 选择最匹配项目的技术路线
→ 按风险决定直接实现或先做 v0
→ 执行视觉、响应式、运行时和无障碍验收
```

## 设计风格库

配方库覆盖编辑极简、信息架构、现代工具、动态实验、粗野主义、温暖人文与特定年代风格。Agent 会先通过 `references/style-recipes/INDEX.md` 选择，再仅加载任务真正需要的配方，不会一次读入全部风格资料。

## 开发与验证

Skill 的主入口位于：

```text
skill/sulflower-web-design/SKILL.md
```

使用 OpenAI `skill-creator` 提供的 `quick_validate.py` 验证时，将 Skill 目录作为参数：

```bash
python -X utf8 quick_validate.py skill/sulflower-web-design
```

提交修改前，请同时检查：

- YAML frontmatter 和 Skill 名称有效。
- `agents/openai.yaml` 的调用名为 `$sulflower-web-design`。
- Markdown 内部引用均存在。
- 未包含密钥、个人路径、私人 URL 或未授权素材。
- 新规则不会破坏原有配色与前端设计原则。

## 来源与许可

本项目是一个独立维护的 MIT 开源改编版本。2.0 的任务模式、仓库适配、确认策略、无障碍、性能、素材授权、验收规范和开源项目结构由 Sulflower 整理与维护；原有视觉设计与配色思想继续保留。

详见 [NOTICE.md](NOTICE.md) 与 [LICENSE](LICENSE)。
