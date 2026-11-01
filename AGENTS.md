# Working on this repository

This repository develops application-development guidance for AI agents. It is currently a research and repository draft. Work on the scope the user requests; do not turn the whole inventory into a skill in one pass.

## Read only what the task needs

- Start with `README.md` and `docs/roadmap.md`.
- Use the index in `docs/scope-inventory.md` to locate affected IDs. Avoid loading the entire inventory for a small edit.
- Read `docs/module-design.md` before proposing or implementing a module.
- Use `CONTRIBUTING.md` for sources, writing, and review expectations.

## Make changes carefully

- Keep existing scope IDs stable and distinguish proposed, accepted, implemented, and verified work.
- Write concrete requirements with applicability and observable verification.
- Preserve useful platform differences. Avoid universal stack or architecture prescriptions.
- Keep shared rules in one place and detailed references outside the future entry file.
- Verify changing API claims against primary sources and retain the date and version.
- Do not fabricate measurements, successful tests, maintainers, release history, or compatibility claims.
- Preserve attribution and license notices. Keep secrets and private user data out of files and fixtures.
- Add a directory when it has a real purpose and content. Do not create empty module scaffolding.

## Finish the requested scope

Run `python3 scripts/check_docs.py`. Review changed links and Markdown rendering. Exercise changed scripts with relevant successful and failing inputs.

Report the changes, checks performed, and material limits. Do not mark a module verified from document checks alone. Publication, installation, and changes to external repositories follow the user's instructions for the task.
