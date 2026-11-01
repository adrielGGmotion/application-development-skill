# Contributing

Start with something specific that an application or an agent got wrong. Describe the trigger, the effect on the user, and the result you expected. That gives a proposed rule something concrete to address.

## Choose a focused change

- Correct an inaccurate requirement or outdated source.
- Add a missing case to an existing scope.
- Propose a module for a bounded part of application development.
- Improve an example, evaluation, or repository check.
- Remove duplicated guidance or a rule that creates unnecessary work.

Use the existing [scope IDs](docs/scope-inventory.md) where possible. A new feature does not automatically need a new module.

Small corrections can go straight into a pull request. For a new module, use [templates/module-proposal.md](templates/module-proposal.md). Discuss changes that alter the project's overall structure before spreading them across several scopes.

## Write useful guidance

State when a rule applies, the behavior it requires, and how someone can verify it. Include an exception when a reader could reasonably apply it too broadly.

Write in plain English. Prefer “restore the previous selection” to “ensure seamless continuity.” Keep technical terms when they make the rule more precise. Avoid promotional claims, generic introductions, and examples that imply tests or experience that did not happen.

Separate these kinds of statements:

| Kind | What to record |
| --- | --- |
| Standard or platform requirement | Primary source, applicable version, and date checked |
| Project recommendation | Reasoning, tradeoffs, and when it does not apply |
| Observed failure | Reproduction steps and available evidence |
| Unverified hypothesis | What remains uncertain and how to investigate it |

Use primary sources for API behavior and platform requirements. Record changing details in their module rather than adding them to every checklist. Keep external material under its original terms; see [NOTICE.md](NOTICE.md).

## Preserve the project boundaries

The repository is currently in the planning stage. Proposals and research do not become working skill modules merely because they have been merged.

Keep the entry point small when implementation begins. Share common rules, then load feature and platform detail only when needed. Do not add a framework, service, account requirement, or dependency without a concrete reason.

Keep stable IDs when changing wording or moving a requirement. Do not reuse retired IDs for unrelated rules. Record substantial scope changes in the roadmap or the relevant proposal.

## Verify the change

Run from the repository root:

```sh
python3 scripts/check_docs.py
```

Review the rendered Markdown and follow any links you changed. The script checks local file targets, formatting, and duplicate inventory IDs. It does not verify external links, heading fragments, source accuracy, or whether an agent follows the guidance correctly.

Changes to executable checks need a passing case and a case that should fail. Use temporary fixtures when a permanent test suite would add little value.

For an implemented module, include an [evaluation record](templates/evaluation-record.md). Report what ran, what it showed, and what remains untested. Compare with the same task without the module when assessing its benefit or token cost.

## Open a pull request

Explain the problem, the changed behavior or guidance, and the checks you performed. Include relevant scope IDs and sources. Keep unrelated cleanup separate.

AI assistance is welcome. Review the result, verify claims and references, and do not submit invented evidence or copied material you cannot license. The same review expectations apply regardless of how a contribution was written.

## Working together

Discuss the work directly and treat contributors with respect. Explain disagreements with examples or evidence. Harassment, personal attacks, and publishing someone else's private information are not acceptable. Maintainers may close or remove disruptive contributions.

Keep credentials, personal records, and sensitive reports out of public issues and evaluation fixtures. A private reporting contact must be configured before the project starts accepting reports that need confidentiality; this draft does not invent one.

## Licensing contributions

Submit original contributions under the repository's [GNU General Public License v3.0](LICENSE), unless the change explicitly identifies compatible third-party material and its notices. Do not remove an existing attribution or license notice.
