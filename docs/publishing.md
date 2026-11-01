# Publishing the repository

Repository: [adrielGGmotion/application-development-skill](https://github.com/adrielGGmotion/application-development-skill).

Suggested description: “Application-development guidance for AI agents, developed by scope across design, behavior, reliability, and code health.”

The repository is private and uses the GNU General Public License v3.0 for original code and documentation. Keep the full license and existing notices when publishing. Referenced material retains its own terms.

## Repository settings

The owner, repository name, visibility, and license are set. Before a public release, establish a maintainer contact and a private route for reports that need confidentiality. Review visibility separately when a public release is requested.

Use `main` as the default branch. The issue templates and pull-request template are ready for that branch. Keep the README's early-development status until there is an installable, evaluated skill.

## Checks and maintenance

The included workflow runs `python3 scripts/check_docs.py` on pushes and pull requests. It uses a read-only token and an immutable checkout action reference, with stored checkout credentials disabled. The action reference was resolved from the official `actions/checkout` repository's `v6` ref on 31 October 2026.

After the first hosted run passes, make `Documentation checks` a required check if the repository's settings support it. For a collaborative repository, consider requiring review and disallowing force pushes to the default branch.

Before accepting community reports, publish the actual reporting route and add security/conduct policies that use it. Do not add placeholder email addresses or promise response times nobody has agreed to maintain.

There is no automatic publishing, release, installation, or external-write workflow in this draft. Add release automation only after the package and its verification process exist.

## References

- [GitHub repository practices](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [Issue and pull-request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- [Adding a license](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
- [Pinned checkout action](https://github.com/actions/checkout/commit/d23441a48e516b6c34aea4fa41551a30e30af803)
