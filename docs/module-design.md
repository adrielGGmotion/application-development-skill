# Module design

Status: proposed. This document describes how future modules should be written and evaluated. It does not define an installable skill.

## Boundaries

One module should cover a coherent problem an agent can recognize from the task: forms, media playback, offline synchronization, or a specific platform's lifecycle, for example.

Start with its applicability. State what triggers it, what it excludes, and which shared rules it depends on. Keep requirements in the module that owns them; refer to their IDs from elsewhere.

The [scope inventory](scope-inventory.md) supplies candidate IDs. Some scopes will become modules; others may be combined or split after evaluation. Preserve the mapping when that happens.

## Reading paths

The eventual package should let an agent move from a short entry file to the relevant material without reading the whole project.

| Layer | Contents |
| --- | --- |
| Entry | Task classification, scope selection, essential invariants, completion report |
| Shared contracts | Common behavior for state, interaction, recovery, and verification |
| Feature modules | Rules for the feature being changed |
| Platform modules | Native behavior, capabilities, and version-specific details |
| References | Detailed examples, primary sources, and troubleshooting |

Repository documentation, contribution policy, and the research backlog should remain outside the installable package. A future package can live under `skills/` once its first usable scope exists. Do not create that directory just to hold empty placeholders.

## Rule format

A useful rule contains:

| Field | Question it answers |
| --- | --- |
| ID | Which requirement does this implement or refine? |
| Applies when | What feature, platform, state, or risk makes it relevant? |
| Behavior | What should the application do? |
| Verification | What action and observation would demonstrate that behavior? |
| Exceptions | When would applying this rule be unnecessary or incorrect? |
| Evidence | Is this a sourced requirement, an observation, or a project recommendation? |

Add reasoning or an example when it prevents a likely mistake. A routine rule does not need a paragraph explaining familiar programming concepts.

The [module proposal template](../templates/module-proposal.md) captures the scope before implementation. Use primary sources for changing platform facts and identify the applicable versions and date checked.

## Evaluation

Choose tasks that expose the rule's purpose: a normal case, a likely failure, and a case where the rule should not activate. Include other environments when claiming portability.

Compare the same task with and without the module under comparable conditions. Record the model/runtime, available tools, task input, module revision, observed behavior, checks, and token/tool cost when measurable. Keep expected answers separate from the task given to an evaluating agent.

Use held-out cases when evaluating whether the guidance generalizes. Success on the example used to write a rule is useful evidence, but it is not enough to establish broad reliability.

An [evaluation record](../templates/evaluation-record.md) should make failed checks and unavailable environments visible. Document checks establish repository consistency; they do not establish application correctness or skill effectiveness.
