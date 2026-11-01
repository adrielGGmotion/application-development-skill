# Roadmap

This project will grow through small, reviewable scopes. The research inventory is broad so that we can choose work deliberately. It is not a promise to implement every topic before the first usable version.

## Current stage

| Work | Status |
| --- | --- |
| Initial research and scope inventory | Drafted; available for review |
| Repository documentation and contribution templates | Drafted |
| Module format and evaluation approach | Proposed |
| Installable entry point | Not started |
| Application-development modules | Not started |
| Public release | Not scheduled |

The proposed next scope is the shared contract for components and user journeys: applicability, states, actions, interruption, recovery, and evidence. The proposed format is in [module-design.md](module-design.md).

## Development increments

| Order | Scope | Result to review |
| --- | --- | --- |
| 1 | Module format and routing | A small entry design, precise triggers, stable IDs, and a useful evaluation record |
| 2 | Component and journey completeness | Guidance for state, navigation, forms, focus, and recovery, exercised on representative tasks |
| 3 | Adaptation and interaction | Device variation, accessibility, themes, content, input, and purposeful motion |
| 4 | Data and interruption | Persistence, lifecycle, asynchronous work, networking, sync, and ambiguous outcomes |
| 5 | Engineering quality | Architecture, code health, security, privacy, dependencies, and performance |
| 6 | Platform modules | Web, Android, Apple, desktop, and shared-code guidance, reviewed independently |
| 7 | Delivery and maintenance | Device matrices, migrations, installation, releases, diagnostics, and support |
| 8 | Specialist modules | Selected features such as media, plugins, collaboration, or hardware integration |

Accessibility, security, and verification belong in each relevant increment. Later increments deepen that coverage; they do not postpone it.

## When a module is ready

A module needs a defined scope, reviewed rules, current sources where necessary, and evidence from representative tasks. Evaluation should also include a case where the module should stay out of the way.

Keep the status explicit:

- **Proposed:** scope and approach are open for review.
- **Accepted:** the scope has been agreed; implementation may still be incomplete.
- **Implemented:** the files and behavior exist.
- **Verified:** the recorded checks support the stated behavior and limits.
- **Deferred:** work is intentionally postponed, with a reason.
- **Deprecated:** guidance has been superseded and has a documented replacement or removal reason.

Revisit guidance when a platform changes, an evaluation fails, or a rule repeatedly causes unnecessary work. Measure token use before describing the skill as efficient.
