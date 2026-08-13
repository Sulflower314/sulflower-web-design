# Output Guidelines

Apply only the section matching the requested artifact.

## Websites and product interfaces

- Use semantic structure and repository-native components.
- Design mobile, tablet, and desktop behavior when the artifact is responsive.
- Cover interaction states that the real flow can reach: default, hover, focus, active, disabled, loading, empty, and error as applicable.
- Do not add marketing sections, testimonials, metrics, or navigation destinations without content or product justification.
- Keep experimental controls out of production output.

## Interactive prototypes

- Show the product immediately instead of adding an unnecessary cover screen.
- Implement the key path rather than a collection of disconnected screens.
- Use device or browser frames when they improve realism.
- Build multiple variants only for genuine exploration; expose them through a design canvas or Tweaks panel when helpful.
- Make unavailable behavior explicit instead of implying unsupported functionality.

## HTML slide decks

- Use a 1920×1080, 16:9 canvas when no other format is specified.
- Fit the canvas to the viewport without distortion.
- Keep navigation controls usable outside the scaled canvas.
- Support left/right keys and Space for navigation.
- Persist the current slide when iterative review benefits from it.
- Number slides from 1 and add a stable `data-screen-label`.
- Let visuals lead; do not cram prose onto slides.

## Data visualization and dashboards

- Use Chart.js for straightforward charts and D3 for bespoke visual grammar, unless the repository already standardizes another library.
- Make chart containers responsive, commonly through `ResizeObserver`.
- Use semantic color encoding and accessible legends.
- Maximize data-ink ratio and remove decorative gridlines, depth effects, and shadows.
- Provide light/dark themes when required by the product rather than automatically.
- Never fabricate production metrics.

## Animation and demos

Choose the lightest layer that works:

1. CSS transition or animation.
2. Web Animations API or simple state plus `requestAnimationFrame`.
3. A shared timeline with easing and interpolation.
4. A specialized library only when the preceding layers cannot meet the requirement.

For timeline demos, provide play/pause and a scrubber when user control is useful. Reuse one easing vocabulary. Respect reduced motion. Skip title-card intros unless they are part of the requested narrative.

## Static comparisons

- Use a design canvas for typography, color, component, or layout comparisons.
- Use a clickable prototype for flows or multi-step interaction alternatives.
- Make differences explicit and comparable; avoid near-identical variants.

## Tweaks

Use a Tweaks panel only for meaningful live variables such as theme, density, spacing, type scale, animation, or component variant. Place it unobtrusively, hide it completely when closed, and remove it from production unless the user requests it as a feature.
