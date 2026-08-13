# Design Foundations

Use this reference whenever defining or changing the visual system. These rules preserve the original skill's frontend design and color philosophy.

## Contents

1. Position the artifact
2. Declare the system
3. Color
4. Typography and scale
5. Layout and depth
6. Motion
7. Anti-cliché rules
8. Placeholders and content

## Position the artifact

Before selecting tokens, answer four questions:

- **Narrative role**: Is this a hero, transition, data view, workflow, pull quote, comparison, or closing moment?
- **Viewing distance**: Will it be read at phone distance, laptop distance, or across a room?
- **Visual temperature**: Should it feel quiet, energized, authoritative, warm, somber, playful, or another deliberate quality?
- **Capacity**: Does the content fit the intended composition without overflow or dead space?

Do not pick aesthetics in a vacuum. The system must serve these answers.

## Declare the system

Make the following explicit before substantial implementation:

```markdown
Design Decisions:
- Anchor / recipe: [named recipe or custom]
- Color palette: [primary / secondary / neutral / accent]
- Typography: [heading / body / code]
- Spacing system: [base unit and multiples]
- Border-radius strategy: [large / small / sharp / hierarchical]
- Shadow hierarchy: [levels and use]
- Motion style: [easing / duration / triggers]
```

When using a recipe, take its concrete palette, typography, spacing, radius, shadow, and motion values from the selected file. Load only the recipe being used.

## Color

- Prefer the brand's established palette.
- When supporting colors are needed, derive harmonious variants with `oklch()` instead of inventing unrelated hues.
- Manage colors as CSS custom properties or the repository's existing design tokens.
- Give color a structural or semantic job: hierarchy, action, category, time, success, warning, or error.
- Keep accent colors scarce enough to remain meaningful.
- Do not introduce rogue hues during component implementation.
- Design light and dark themes intentionally; do not mechanically invert colors.
- For data visualization, encode meaning rather than decoration. Remove needless gridlines, 3D effects, and ornamental shadows.

Example token roles:

```css
:root {
  --color-canvas: ...;
  --color-surface: ...;
  --color-surface-raised: ...;
  --color-text: ...;
  --color-text-muted: ...;
  --color-border: ...;
  --color-primary: ...;
  --color-primary-hover: ...;
  --color-focus: ...;
  --color-success: ...;
  --color-warning: ...;
  --color-danger: ...;
}
```

Do not treat color hex values alone as a brand. Recognition depends more heavily on real logos, product imagery, interface captures, typography, and composition.

## Typography and scale

- Use type-scale contrast to create hierarchy; a 4–6× ratio between a hero heading and body copy can be appropriate.
- Keep font families controlled, normally no more than two unless the concept has a clear reason.
- Avoid defaulting to Inter, Roboto, Arial, Fraunces, or `system-ui` as display faces. Use them when the brand, existing product, or chosen recipe calls for them.
- Use `clamp()` for fluid type where appropriate.
- Use `text-wrap: pretty` when supported and verify the fallback.
- Start web body text around 16–18px unless the established system requires otherwise.
- Keep presentation text at least 24px on a 1920×1080 canvas, preferably larger.
- Keep print-oriented text at least 12pt.
- Keep mobile touch targets at least 44px in both dimensions when practical.

## Layout and depth

- Prefer CSS Grid and Flexbox for layout.
- Use proportion and whitespace to create rhythm.
- If a composition feels empty, solve the layout, scale, or pacing instead of adding filler.
- Choose a coherent radius strategy rather than applying the same large radius everywhere.
- Use shadows as a hierarchy, not a decoration applied to every container.
- Use fills, texture, layering, blend modes, masks, filters, and backdrop effects when they support the concept and remain performant.
- Let every element earn its place. Remove anything whose absence does not weaken the design or comprehension.

## Motion

- Prefer CSS transitions and animations for micro-interactions.
- Use state-driven JavaScript or the Web Animations API for behavior that CSS cannot express cleanly.
- Use timeline-driven animation only when the artifact actually has scenes or choreography.
- Define a consistent easing vocabulary and duration scale.
- Use motion for feedback, orientation, hierarchy, or narrative—not as ambient noise.
- Respect `prefers-reduced-motion` and provide a usable reduced-motion state.

## Avoid AI-style clichés

Anti-cliché rules protect brand recognition. AI defaults average many brands into a generic visual identity. The exception is always the same: if the brand or selected direction genuinely uses the pattern, preserve it deliberately.

| Pattern | Why it usually fails | When it is appropriate |
|---|---|---|
| Aggressive purple–pink–blue gradient | Generic technology shorthand used across unrelated products | The brand uses it or the task intentionally explores that aesthetic |
| Rounded cards with colored left borders | Repetitive dashboard filler that weakens hierarchy | The established product system preserves it |
| Emoji used as icon substitutes | Signals missing visual craft rather than intentional friendliness | The brand uses emoji or the audience is explicitly casual |
| Improvised SVG people, faces, or scenes | Often looks cheap and distracts from the product | Prefer real imagery, generated raster art, or honest placeholders |
| CSS silhouettes replacing real products | Removes brand recognition from physical products | Do not use for branded product imagery |
| Default display typography | Makes polished work read like a framework demo | Use when specified by the brand or product system |
| Cyber-neon on generic dark gray | Produces interchangeable developer-tool styling | Use when it is an authentic brand or genre choice |
| Fabricated metrics, logo walls, or testimonials | Damages credibility | Never fabricate; mark real-data requirements explicitly |

Do not use emoji by default. If the target system uses it, match its density, scale, and context precisely.

## Placeholders and content

Use honest placeholders when assets are unavailable:

- Missing icon: a labeled placeholder such as `[icon]`.
- Missing avatar: an initial-letter circle using an existing token.
- Missing image: a card labeled with the required aspect ratio.
- Missing data: a clear real-data-needed state.
- Missing logo: stop or mark it pending; do not invent a substitute logo.

Do not fabricate content to make a layout feel complete. Do not add sections or pages beyond the requested scope without a product reason or user authorization. Use composition, whitespace, hierarchy, and type rhythm to make sparse content feel intentional.

## Originality

Aim for at least one decision that is unexpected but right: an unusual proportion, typographic move, interaction metaphor, spatial transition, or visual framing that remains coherent with the system. Originality must strengthen the artifact rather than compete with usability.
