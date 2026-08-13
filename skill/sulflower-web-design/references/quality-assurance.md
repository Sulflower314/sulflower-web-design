# Quality Assurance

Use this checklist proportionately to the artifact's risk and intended audience.

## Runtime

- Run the project's relevant build, typecheck, lint, and focused tests.
- Check the browser console for relevant errors and warnings.
- Verify assets resolve and network failures have a usable state where applicable.
- Confirm routes, links, controls, and key flows work.

## Responsive and visual

- Inspect the target viewport exactly.
- For responsive work, inspect representative mobile, tablet, and desktop widths.
- Check overflow, clipping, wrapping, sticky/fixed elements, safe areas, and zoom.
- Confirm type scale, spacing rhythm, alignment, image ratios, and hierarchy.
- Confirm all colors originate from the declared system.
- Check loading, empty, error, disabled, hover, focus, and active states when applicable.

## Accessibility

- Use semantic HTML before adding ARIA.
- Provide accessible names for controls and labels for form inputs.
- Make the key flow operable with a keyboard.
- Keep focus visible and logically ordered.
- Do not communicate meaning with color alone.
- Provide appropriate image alternatives.
- Keep text and interactive control contrast suitable for WCAG 2.2 AA when the artifact is production-facing.
- Respect reduced-motion preferences and avoid trapping users in automatic animation.
- Keep touch targets approximately 44×44px where practical.

## Performance

- Size media for its rendered use and prefer modern formats when compatible.
- Lazy-load non-critical media.
- Control font families, weights, and external requests.
- Avoid adding a large dependency for a small visual effect.
- Avoid unnecessary continuous animation, large-area blur, and filter-heavy scrolling.
- Reserve space for media and dynamic content to reduce layout shift.
- Preserve the existing project's performance strategy and budgets.

## Content and publishing safety

- Do not fabricate metrics, testimonials, brands, claims, or affiliations.
- Do not publish credentials, tokens, private URLs, personal paths, or non-public data.
- Confirm redistributed assets and fonts have appropriate permission.
- Label placeholders, simulated data, and AI-generated material honestly.

## Delivery evidence

Report the checks actually performed, important assumptions, known asset or content gaps, and any check that could not run. Do not claim verification that did not occur.
