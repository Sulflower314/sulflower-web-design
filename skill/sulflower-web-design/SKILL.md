---
name: sulflower-web-design
description: "Design, build, improve, reconstruct, or critique polished browser-based interfaces using HTML, CSS, JavaScript, and repository-native frontend frameworks. Use for landing pages, product sites, dashboards, interactive prototypes, responsive redesigns, screenshot or Figma reconstruction, HTML presentations, motion, design systems, UI mockups, and data visualization. Preserve existing brand and code conventions when working in an established product. Not for back-end, CLI, or non-visual programming tasks."
---

# Sulflower Web Design

Create refined, brand-aware frontend work whose visual quality is intentional rather than merely functional. Preserve the original design philosophy, color system, anti-cliché rules, typography standards, motion language, and anchored recipe library while adapting the implementation process to the actual project.

## Scope

Use this skill for visual frontend deliverables: websites, product pages, dashboards, UI flows, prototypes, redesigns, screenshot or Figma reconstruction, HTML slide decks, animations, data visualization, and design-system work.

Do not use it for back-end APIs, CLI tools, non-visual data processing, pure logic work, or performance tuning without a visual interface objective.

## Core Standard

Aim for a coherent, recognizable, polished result. Every major visual decision must trace to the brief, brand, content, or chosen design direction. Do not fill gaps with generic AI defaults, fabricated content, or ornamental UI.

Preserve these original design principles:

- Build hierarchy through proportion, typography, spacing, color, and composition.
- Use brand assets and existing visual vocabulary before inventing a new system.
- Prefer real assets or honest placeholders over weak imitations.
- Avoid default AI-web clichés unless the brand or requested direction explicitly uses them.
- Use color semantically and derive supporting colors from the declared palette.
- Treat whitespace as an active design material; solve emptiness with composition, not filler.
- Add motion only when it clarifies state, guides attention, or strengthens the narrative.

Read `references/design-foundations.md` before declaring or changing a visual system. It contains the preserved color, typography, layout, anti-cliché, placeholder, scale, and content rules.

## Workflow

### 1. Verify unstable facts

When the task names a current product, brand, SDK, library, event, release, or specification that may have changed, verify it with authoritative sources before relying on it. If verification remains ambiguous and the ambiguity materially affects the design, ask the user instead of guessing.

### 2. Classify the work mode

Choose the closest mode before editing:

| Mode | Use when | Primary obligation |
|---|---|---|
| **Create** | Starting a page, prototype, presentation, dashboard, or visual system from scratch | Establish a deliberate design direction and system |
| **Extend** | Adding a screen, component, or flow to an existing product | Make the addition indistinguishable from the existing product |
| **Reconstruct** | Recreating a screenshot, Figma frame, reference page, or supplied mockup | Reproduce structure, proportion, typography, spacing, assets, and behavior faithfully |
| **Improve** | Redesigning, polishing, reviewing, or fixing an existing interface | Diagnose first; preserve protected contracts and change only the authorized scope |

Read `references/workflow-modes.md` for the mode-specific procedure and preservation rules.

### 3. Inspect context

Read user-provided code, screenshots, Figma exports, UI kits, content, and brand material before designing. When both code and screenshots exist, treat the code and existing design tokens as the structural source of truth and screenshots as visual evidence.

For existing projects:

- Inspect repository instructions, framework, build tooling, routing, dependencies, component library, tokens, icon system, state patterns, and test commands.
- Reuse the current stack and conventions. Do not replace the framework or add a parallel design system for convenience.
- Preserve public component APIs, routes, data contracts, analytics hooks, localization, and accessibility behavior unless the request authorizes changes.

For branded work, follow `references/brand-assets.md` before implementation.

### 4. Produce a concise Design Read

State or infer the following before choosing tokens:

- Narrative role: hero, transition, data, workflow, detail, comparison, closing, or another clear role.
- Viewing distance: phone, desktop, installation, or projector.
- Visual temperature: quiet, energized, authoritative, warm, somber, playful, or another deliberate quality.
- Density and capacity: how much content the layout must hold without overflow or dead space.
- Preservation mode: what must remain visually and technically unchanged.

If the request is genuinely vague and has no design anchor, use the Design Direction Advisor in `references/design-directions.md`: offer three visibly different directions from different schools. After selection, use `references/style-recipes/INDEX.md` to identify suitable recipes, then load only the selected recipe files.

### 5. Declare the design system

Before substantial implementation, make the system explicit:

```markdown
Design Decisions:
- Mode: [Create / Extend / Reconstruct / Improve]
- Anchor / recipe: [named recipe or custom]
- Color palette: [primary / secondary / neutral / accent]
- Typography: [heading / body / code]
- Spacing system: [base unit and scale]
- Radius strategy: [large / small / sharp / hierarchical]
- Shadow hierarchy: [levels and use]
- Motion style: [easing / duration / triggers]
- Preserved contracts: [visual and technical invariants]
```

For a small or already well-specified task, keep this declaration brief and proceed. Pause for confirmation only when direction is genuinely ambiguous, the work is a brand-level redesign, multiple choices would materially change the outcome, or implementation would discard substantial existing work.

### 6. Choose the implementation path

Use the least complex approach that meets the task:

| Context | Default path |
|---|---|
| Existing repository | Use its framework, component system, styling approach, package manager, and pinned versions |
| Portable single-file artifact | Semantic HTML + hand-written CSS + minimal JavaScript |
| Portable React prototype | Pinned React + ReactDOM + Babel CDN pattern from `references/advanced-patterns.md` |
| New maintainable multi-screen app | A suitable modern project setup, preferably TypeScript, only when the requested deliverable warrants it |
| Simple charts | Existing chart library or Chart.js |
| Complex bespoke visualization | D3 or the repository's established visualization stack |
| Micro-interactions | CSS transitions/animations or Web Animations API |
| Timeline-driven motion | React state/RAF or the timeline pattern in `references/advanced-patterns.md` |

Do not introduce a dependency when existing code or browser primitives solve the problem cleanly. Do not upgrade unrelated dependencies or rewrite the build system.

For portable React + Babel prototypes only:

- Load React, ReactDOM, Babel, then component scripts in that order.
- Do not use `type="module"` with the inline Babel pipeline.
- Namespace global style objects; never declare a generic global `const styles` across files.
- Export cross-file components explicitly through `window` because separate Babel script blocks do not share local scope.
- Avoid `scrollIntoView` in iframe previews; update the intended scroll container directly.

### 7. Build at the right fidelity

Use an early v0 when the layout direction needs validation or the work is large enough that rework would be expensive. A v0 should show structure, tokens, representative modules, assumptions, and honest placeholders—not full content, every state, or final motion.

For clear, bounded tasks, implement directly without forcing a v0 checkpoint.

Build variants only when the user requests exploration or the brief has unresolved directional choices. Explore layout, visual treatment, interaction, and creative metaphor—not trivial recolors. Use a Tweaks panel only when live comparison or parameter exploration materially helps; keep it hidden or remove it from final production UI.

Read `references/output-guidelines.md` for prototypes, websites, slide decks, dashboards, animation, and comparison artifacts.

### 8. Verify proportionately

Run the repository's relevant checks and visually inspect the result in the target environment. Scale verification to risk, but do not deliver a visual artifact without checking it.

Required baseline:

- No relevant runtime or browser-console errors.
- No text overflow, accidental clipping, broken assets, or layout collapse.
- Correct behavior at the target viewport(s).
- Interactive states are present where the scenario needs them.
- Colors come from the declared system; no unexplained hue drift.
- No fabricated data, testimonials, logos, or claims.
- Existing routes, contracts, and nearby UI remain intact.

For production-facing work also check semantic structure, keyboard access, visible focus, contrast, reduced motion, media sizing, loading behavior, and avoidable layout shift. Follow `references/quality-assurance.md`.

### 9. Critique when requested

For review, scoring, or self-check, evaluate philosophy alignment, visual hierarchy, craft quality, functionality, and originality. Read `references/critique-guide.md` for the complete rubric. Critique the artifact, not the designer, and prioritize fixes by impact.

## Brand and Asset Rules

- Use a real logo for branded work. If it cannot be sourced after a reasonable attempt, ask for it or use an explicit pending state rather than inventing one.
- Use real product imagery for physical products and representative real UI captures for digital products whenever available and authorized.
- Do not redraw recognizable product imagery as a CSS silhouette or improvised illustration.
- Record asset paths, sources, usage rights, colors, and fonts in `brand-spec.md` or equivalent project documentation when the task warrants it.
- Copy permitted assets locally instead of hotlinking user-provided private resources.
- Do not treat public availability as permission to redistribute.

Read `references/brand-assets.md` for the sourcing order, licensing fields, and fallback policy.

## File Management

- Use descriptive filenames and follow repository naming conventions.
- Split large standalone prototypes into meaningful component files when that improves maintainability.
- Preserve older standalone artifact versions for major visual revisions unless the user asks to replace them.
- Prefer one artifact with controlled variants over duplicated near-identical files.
- Keep temporary controls, mocks, and debug panels out of production deliverables.
- Never embed credentials, private tokens, personal filesystem paths, or unpublished private URLs.

## Reference Routing

Read only what the task needs:

| Need | Read |
|---|---|
| Preserved visual design, color, typography, layout, motion, anti-cliché, placeholders | `references/design-foundations.md` |
| Create / Extend / Reconstruct / Improve procedures | `references/workflow-modes.md` |
| Brand assets, sourcing, rights, and `brand-spec.md` | `references/brand-assets.md` |
| Device frames, slide engine, timeline, Tweaks, dark mode, data viz, color and font patterns | `references/advanced-patterns.md` |
| Websites, prototypes, slides, dashboards, animation, comparisons | `references/output-guidelines.md` |
| Responsive, runtime, accessibility, performance, and visual QA | `references/quality-assurance.md` |
| Vague request and three-direction recommendation | `references/design-directions.md` |
| Named style anchor | Only the matching `references/style-recipes/<anchor>.md` |
| Recipe discovery | `references/style-recipes/INDEX.md`, then the selected recipe files |
| Design review and scoring | `references/critique-guide.md` |
