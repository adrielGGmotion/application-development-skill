# Application Development Skill

Practical application-development guidance for AI agents, built one scope at a time.

Small omissions add up. A form loses its draft when the session expires. A dialog opens behind the keyboard. An animation jumps when someone reverses a gesture. An update breaks data from an older release.

This project collects those details and turns them into guidance an agent can apply and verify. It covers interface design, functional behavior, platform integration, reliability, and code health across web, mobile, and desktop applications.

## Project status

**Early development.** The repository currently contains the research inventory, contribution process, and templates for future modules. There is no installable skill or published release yet.

The [scope inventory](docs/scope-inventory.md) is the starting point. Its checkboxes identify candidate coverage; they do not mean the skill implements those requirements or that every app needs every feature.

## What belongs here

| Area | Examples |
| --- | --- |
| Interface details | Component states, navigation, forms, focus, motion, themes, responsive layouts |
| Complete behavior | Loading, cancellation, validation, interrupted work, recovery, permissions |
| Platform differences | Browser history, mobile lifecycle, desktop windows, native input and accessibility |
| Engineering | State ownership, persistence, synchronization, architecture, security, performance |
| Verification | Meaningful tests, device coverage, upgrades, diagnostics, evidence of completion |

Guidance should lead to something observable. “Handle errors well” is too vague. “Keep the entered values after a recoverable save failure and provide a safe retry” gives the agent a behavior to implement and check.

## How the skill will grow

Work starts with a concrete omission and a bounded scope. Each proposed module identifies when it applies, the behavior it requires, and how to verify the result. Platform-specific requirements stay with their platform.

The eventual entry file will select relevant modules. Long examples, research notes, and implementation references will be loaded only when needed. Token use will be measured alongside missed issues, false positives, and unnecessary work.

We will develop and evaluate modules before marking them ready. The [roadmap](docs/roadmap.md) records the current stage and proposed order.

## Repository guide

| Path | Purpose |
| --- | --- |
| [docs/scope-inventory.md](docs/scope-inventory.md) | Research and candidate coverage, with stable scope IDs |
| [docs/roadmap.md](docs/roadmap.md) | Current work and proposed development increments |
| [docs/module-design.md](docs/module-design.md) | Module boundaries, rule format, and evaluation expectations |
| [docs/publishing.md](docs/publishing.md) | Repository settings and preparation for a public release |
| [templates/](templates/) | Module proposals and evaluation records |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose, write, and review a change |
| [AGENTS.md](AGENTS.md) | Instructions for agents working on this repository |
| [scripts/check_docs.py](scripts/check_docs.py) | Local documentation checks used by CI |

## Contributing

Useful contributions start with a specific example: what was missed, when it happens, and what a correct result looks like. A focused correction or a well-supported removal is welcome too.

Read [CONTRIBUTING.md](CONTRIBUTING.md), then use a [module proposal](templates/module-proposal.md) for a new scope. Keep each change small enough to review on its own.

## Local checks

Python 3.10 or newer is sufficient. No packages need to be installed.

```sh
python3 scripts/check_docs.py
```

The checker validates document formatting, local inline-link targets, and duplicate checklist IDs. It does not check remote websites, Markdown fragments, or the technical correctness of the guidance. Those remain review tasks.

## License

Original project text and code are available under the [GNU General Public License v3.0](LICENSE). Referenced standards and third-party material retain their own terms; see [NOTICE.md](NOTICE.md).
