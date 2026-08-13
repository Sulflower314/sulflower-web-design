# Workflow Modes

Use this reference after classifying the task as Create, Extend, Reconstruct, or Improve.

## Contents

1. Create
2. Extend
3. Reconstruct
4. Improve
5. Confirmation policy

## Create

Use when no established interface exists.

1. Establish audience, objective, artifact type, content, and technical delivery environment.
2. Gather brand material or a design anchor. If neither exists, use the Design Direction Advisor.
3. Produce a concise Design Read and declare the design system.
4. Make a v0 when direction risk or implementation cost is significant.
5. Build the approved direction using the least complex suitable stack.
6. Verify the relevant viewports, interactions, accessibility, and runtime.

Do not invent testimonials, metrics, partners, case studies, or claims. Use explicit placeholders for missing content.

## Extend

Use when adding to an existing interface.

1. Read repository instructions and inspect nearby components before editing.
2. Extract actual tokens: colors, typography, spacing, radii, borders, shadows, density, and motion.
3. Identify the component, routing, state, data, icon, and testing conventions already in use.
4. Declare the contracts that must not change.
5. Reuse existing components and patterns before introducing new primitives.
6. Implement the smallest coherent addition.
7. Compare the result with adjacent screens and run focused regression checks.

Success means the new work is visually and technically indistinguishable from the existing product.

## Reconstruct

Use for screenshots, Figma frames, mockups, or reference-page recreation.

1. Inventory available source material and identify missing fonts, assets, states, and responsive evidence.
2. Measure composition: canvas, grid, alignment, margins, type scale, line length, image ratios, and component density.
3. Separate observable facts from inference.
4. Reuse supplied assets and repository-native components where possible.
5. Recreate the highest-information structure first, then tune typography, spacing, and decoration.
6. Infer responsive behavior conservatively and state important assumptions.
7. Compare at the target viewport and correct the largest visual deltas first.

Do not copy protected source code or private assets from a reference website. Reconstruct only from materials the user is authorized to use.

## Improve

Use for redesigns, polish, audits, or visual fixes.

1. Diagnose the current interface before proposing a solution.
2. Identify what already works and must be preserved.
3. Separate visual, usability, content, accessibility, and implementation problems.
4. Rank issues by user impact and scope.
5. Distinguish three levels:
   - **Extension**: add missing behavior or content without changing the visual language.
   - **Preserve**: improve hierarchy and craft while maintaining identity and structure.
   - **Overhaul**: change the underlying visual or interaction system; require explicit authorization.
6. Implement the authorized level only.
7. Verify both the improvement and preserved behavior.

## Confirmation policy

Proceed without a formal checkpoint when the task is clear, bounded, reversible, and consistent with the existing system.

Pause for confirmation when:

- the brief is genuinely ambiguous;
- two or more directions would lead to materially different products;
- a brand identity or core interaction model would change;
- the work would discard substantial existing implementation;
- required assets or content cannot be obtained honestly;
- the request expands beyond its stated product or page scope.

Use a v0 for high-cost direction decisions. Do not force a v0 for small fixes or fully specified implementations.
