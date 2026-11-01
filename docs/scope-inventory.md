# Application development skill — research and scope inventory

Version: 0.1 · Research date: 31 October 2026 · Status: proposed inventory for discussion

This document defines what a future, incrementally developed AI-agent skill should cover. It is not the skill, an implementation plan for a particular application, or a claim that every listed feature belongs in every application.

The intended scope is application development across web, mobile and desktop, with separate extensions for other devices and specialist domains. It includes client behavior, supporting services, engineering practices, verification, distribution and maintenance. Design and engineering are considered together: a polished screen is incomplete if its actions lose work, report false success or cannot be completed with another input method.

## Research findings that shape the inventory

- Quality needs to be specified and evaluated across a product's lifecycle. ISO/IEC 25010 provides a quality-model frame; its public abstract was consulted, not the full paid standard. This inventory is an original synthesis, not a reproduction or conformance checklist. [S01]
- Platform guidance covers interactions and operating conditions as well as appearance. Android, Apple, Windows, GNOME and KDE provide different conventions; a shared skill needs platform-specific branches. [S02–S07]
- Accessibility needs testable outcomes and complete user journeys. WCAG, WAI component guidance and evaluation methodology provide useful references, while native applications additionally require their platform accessibility APIs and testing. [S08–S10]
- Data ownership, interruption and synchronization are major quality concerns. Offline behavior and database upgrades need explicit contracts rather than incidental implementation. [S11–S12]
- Security belongs throughout development. OWASP and NIST provide reference frameworks to select according to the application and its risks. [S13–S15]
- Code review, runtime measurement and supply-chain evidence address different questions. A clean build alone does not establish a complete, usable or reliable product. [S16–S19]

The numbered items below are proposed coverage requirements for our skill. Their wording, examples, grouping, prioritization and module structure are our synthesis. Sources establish reference points; they do not individually mandate every proposed item.

## Scope index

| Scope | Contents |
| --- | --- |
| A01–A04 | Product definition, domain workflows, research/information architecture, surface inventory |
| B01–B13 | Design system, components, behavior contracts, navigation, input, forms, content, state, motion, adaptation, themes, accessibility, localization |
| C01–C07 | Onboarding, accounts, authorization/permissions, settings, search/collections, notifications, files/sharing |
| D01–D07 | Data models, persistence, APIs, asynchronous work, offline sync, lifecycle, recovery |
| E01–E07 | Architecture, code health, security, privacy, dependencies/builds, performance, services |
| F01–F06 | Web, Android, Apple, desktop, shared-code/hybrid and additional device adapters |
| G01–G16 | Specialist feature packs selected only when needed |
| H01–H06 | Automated/manual verification, device matrix, releases, operations, documentation, completion evidence |
| I01–I02 | Token efficiency, module routing, iterative development and evaluation of the skill |
| J–L | Omission scenarios, suggested development increments and scope acceptance criteria |

## How to use this inventory

**Core:** consider for every application, with effort proportional to scope. **Conditional:** load only when its feature or risk exists. **Adapter:** load for a supported platform. **Specialist:** add a dedicated module when the product requires it.

Checkboxes mean “candidate content to develop into the skill.” They do not mean a product is missing all these features. For a future project, record each applicable requirement as **unassessed, planned, implemented, verified, deferred, blocked, or not applicable**. A checked code task and a verified user outcome are different statuses.

Use stable identifiers so we can develop one scope without rewriting the entire document. Each future rule should carry: applicability trigger; requirement; consequence if missed; concise implementation guidance; observable acceptance criterion; verification method; source and last-review date where relevant. Add examples only when they clarify a likely failure.

## A. Product definition and completeness

### A01. Product purpose, users and constraints — Core

- [ ] A01.01 Define the actual user outcomes, the problem solved and the main reasons people return.
- [ ] A01.02 Identify user groups, roles, skill levels, access needs and situational limitations without inventing research.
- [ ] A01.03 Separate confirmed requirements, assumptions, open questions and intentionally excluded functionality.
- [ ] A01.04 Specify supported platforms, minimum OS/browser versions, hardware classes and distribution channels.
- [ ] A01.05 Identify real constraints: budget, development time, connectivity, storage, battery, backend availability and team capacity.
- [ ] A01.06 Define product-specific success and failure measures, including task completion and lost-work incidents.
- [ ] A01.07 Establish data sensitivity, consequence of mistakes and appropriate review depth.
- [ ] A01.08 Identify ownership and dependencies for design, client, service, content, release and support decisions.
- [ ] A01.09 Distinguish prototype, internal tool, public release and maintained product expectations.
- [ ] A01.10 Define a workable minimum product without presenting unfinished flows as completed functionality.

### A02. Domain rules and complete workflows — Core

- [ ] A02.01 Describe the main entities, terminology, relationships and business invariants before choosing UI representations.
- [ ] A02.02 Map each journey from entry through completion, cancellation, failure and recovery.
- [ ] A02.03 Include secondary operations such as edit, duplicate, archive, restore, export and delete when the domain calls for them.
- [ ] A02.04 Define rules for boundaries, quotas, ordering, eligibility, expiration, rounding and conflicting actions.
- [ ] A02.05 Identify destructive or consequential operations and decide whether undo, review or explicit confirmation fits the risk.
- [ ] A02.06 Define what “saved,” “sent,” “complete,” “available” and similar status words actually guarantee.
- [ ] A02.07 Cover interrupted workflows, partially completed work and resuming at a meaningful step.
- [ ] A02.08 Specify role and ownership changes during a workflow, not only at initial entry.
- [ ] A02.09 Model dependencies between features so removing or disabling one does not strand another.
- [ ] A02.10 Map every visible action to implemented behavior and a discoverable destination or result.
- [ ] A02.11 Record what can happen concurrently and what must remain atomic or ordered.
- [ ] A02.12 Define domain-specific acceptance examples with realistic input and expected durable results.

### A03. Research, information architecture and discoverability — Core

- [ ] A03.01 Identify the evidence used: user observation, support reports, existing behavior, analytics or explicit stakeholder requirements.
- [ ] A03.02 Group content and functions using language users understand; validate ambiguous labels.
- [ ] A03.03 Define navigation hierarchy, primary destinations, contextual actions and advanced-function discovery.
- [ ] A03.04 Make frequent tasks reachable without forcing every feature into the primary interface.
- [ ] A03.05 Identify first-use, occasional-use and expert workflows and provide suitable guidance or shortcuts.
- [ ] A03.06 Define search, browse, filter and recent-item approaches according to the actual information volume.
- [ ] A03.07 Validate findability and task completion with representative scenarios instead of visual preference alone.
- [ ] A03.08 Plan help, terminology explanations and support entry points near likely confusion.
- [ ] A03.09 Establish how changes to navigation preserve existing users' orientation.
- [ ] A03.10 Record deliberate tradeoffs and unresolved product decisions without treating guesses as established needs.

### A04. Surface and entry-point inventory — Core

- [ ] A04.01 List screens, routes, windows, panels, dialogs, sheets, menus and important embedded views.
- [ ] A04.02 List external entries: URLs, app links, files, share targets, notifications, shortcuts and widgets when supported.
- [ ] A04.03 Define initial state for direct entry, cold launch, warm launch and restored sessions.
- [ ] A04.04 Include onboarding, settings, account, help, diagnostics and update surfaces only where applicable.
- [ ] A04.05 Cover unknown routes, missing objects, expired invitations and unavailable destinations.
- [ ] A04.06 Identify shared components and record intentional per-platform differences.
- [ ] A04.07 Map each surface to user goals, data sources, permissions and supported actions.
- [ ] A04.08 Include alternate presentations: compact/expanded, read/edit, single/multi-select and restricted access.
- [ ] A04.09 Track completion by surface and journey, including the connections between them.
- [ ] A04.10 Make demo-only content, placeholders and incomplete integration visible in development status.

## B. Interface system and interaction details

### B01. Design system and visual foundations — Core

- [ ] B01.01 Establish product identity, visual hierarchy, density and the intended relationship with platform conventions.
- [ ] B01.02 Define semantic color roles for content, surfaces, actions, state, borders and emphasis.
- [ ] B01.03 Define typography roles, font fallbacks, size/weight relationships, line height and reading width.
- [ ] B01.04 Define spacing, alignment, layout grids, container widths and content grouping.
- [ ] B01.05 Define icon meaning, optical sizing, stroke/fill consistency and when text labels are necessary.
- [ ] B01.06 Define shape, elevation, layering, scrims and surface separation without relying solely on shadows.
- [ ] B01.07 Define image cropping, aspect ratios, focal points, transparency and failure placeholders.
- [ ] B01.08 Define component variants through reusable tokens and APIs rather than scattered overrides.
- [ ] B01.09 Document exceptions and avoid forcing unlike platform interactions into identical components.
- [ ] B01.10 Maintain a representative component preview/gallery for states and themes when its maintenance cost is justified.
- [ ] B01.11 Check real content, long labels and mixed image sizes rather than only ideal sample data.
- [ ] B01.12 Distinguish visual consistency from unnecessary sameness across different tasks.

### B02. Component catalogue — Conditional by actual interface

The skill should have concise contracts for these families. It should not require every application to implement the catalogue.

| Family | Components/patterns to cover | Frequently missed behavior |
| --- | --- | --- |
| Actions | Buttons, icon buttons, split buttons, links, floating actions | Busy state, repeat activation, accessible name, real destination |
| Binary and exclusive choice | Checkboxes, switches, radio groups | Indeterminate state, immediate versus deferred save, label activation |
| Multiple choice | Chips, tags, multiselects, segmented controls | Removal, overflow, selection count, keyboard operation |
| Text entry | Single-line fields, text areas, password fields, search fields | Composition input, autofill, selection, paste, clear and error states |
| Structured entry | Number fields, steppers, sliders, range inputs | Precision, bounds, units, non-drag alternative, locale parsing |
| Selection and lookup | Selects, comboboxes, autocomplete, pickers | Empty suggestions, loading, stale requests, focus versus selection |
| Time and dates | Date/time pickers, calendars, duration and recurrence editors | Time zones, invalid ranges, daylight-saving changes |
| Navigation | Tabs, rails, sidebars, drawers, breadcrumbs, pagination | History, direct entry, selection persistence, compact-layout changes |
| Collections | Lists, grids, cards, trees, tables, data grids | Stable identity, focus after deletion, virtualization, partial loading |
| Collection actions | Sorting, filtering, selection bars, bulk actions, reordering | Selection scope, partial failure, stable ordering, undo |
| Containment | Panels, sections, accordions, split views, inspectors | Hidden focus, resizing, expansion persistence, reading order |
| Commands | Menus, context menus, toolbars, command palettes | Keyboard discovery, disabled explanation, unavailable commands |
| Overlays | Dialogs, sheets, popovers, drawers | Dismissal, focus return, nested layers, keyboard overlap |
| Contextual help | Tooltips, descriptions, inline help | Essential information remains available without hover |
| Sequential flows | Multistep forms, wizards, guided setup | Progress, backtracking, retained answers, skipped steps |
| Rotating content | Carousels, paged galleries, auto-advancing panels | Pause, manual control, focus, announcements, reduced motion |
| Feedback | Inline messages, banners, toasts, snackbars, badges | Announcement timing, persistence, action availability |
| Waiting | Spinners, skeletons, progress bars, transfer queues | Honest progress, cancellation, delayed feedback, no endless limbo |
| Status surfaces | Empty, error, offline, restricted and unavailable views | Correct reason, recovery, next useful action |
| Rich content | Images, galleries, audio/video players, previews | Fallbacks, controls, captions, interruption and loading |
| Data visualization | Charts, legends, maps, timelines | Text equivalents, units, missing data, non-color encoding |
| Files | Pickers, uploads, downloads, attachments, export dialogs | Permission, names, overwrite, progress, saved-file location |
| Identity | Avatars, account menus, profile panels, organization switchers | Missing images, identity clarity, stale access |
| Editors | Rich text, code, canvas and document editors | Undo, selection, dirty state, composition, autosave |
| Desktop chrome | Windows, title bars, menu bars, tool windows, status areas | Close versus quit, window restoration, shortcuts |
| Device-specific controls | Remote focus, crown input, stylus tools, spatial targets | Input parity, reachability, unavailable hardware |

### B03. Shared component contract — Core, applied only to relevant states

- [ ] B03.01 Define purpose, semantics and when to use an existing native/framework component.
- [ ] B03.02 Cover enabled, disabled, focused, hovered, pressed, selected, expanded, busy, invalid and read-only states where meaningful.
- [ ] B03.03 Specify pointer, touch, keyboard and assistive-technology activation behavior.
- [ ] B03.04 Specify accessible name, role, value, state, description and relationships.
- [ ] B03.05 Distinguish focus from selection and disabled from read-only.
- [ ] B03.06 Define hit target, spacing, hit testing and behavior when nearby interactive regions overlap.
- [ ] B03.07 Handle long text, no text, missing icons, dynamic content and large text sizes.
- [ ] B03.08 Specify how asynchronous actions affect interaction, feedback and repeat activation.
- [ ] B03.09 Define dismissal, cancellation, undo and focus restoration where applicable.
- [ ] B03.10 Cover layout direction, theme and available-space changes during use.
- [ ] B03.11 Define composition rules, event ownership and predictable controlled/uncontrolled state behavior where relevant.
- [ ] B03.12 Include minimal behavioral checks and visual examples for meaningful variants.
- [ ] B03.13 Define modal initial focus, contained focus, inert background, explicit dismissal rules and focus return; preserve nonmodal behavior for nonmodal surfaces.

### B04. Navigation, history and context — Core

- [ ] B04.01 Specify back, up, forward, close, cancel and dismiss separately; they do not always mean the same thing.
- [ ] B04.02 Preserve meaningful scroll, selection, filters, tab state and drafts when returning.
- [ ] B04.03 Define route/deep-link behavior before and after authentication or permission requests.
- [ ] B04.04 Prevent duplicate destinations, accidental navigation loops and unexpected history entries.
- [ ] B04.05 Define what happens when the current object is deleted or access is revoked.
- [ ] B04.06 Keep navigation destinations understandable when compact layouts become multipane layouts.
- [ ] B04.07 Restore or deliberately reset focus after navigation, with an understandable destination announcement.
- [ ] B04.08 Handle unsaved work and in-flight operations when leaving a surface.
- [ ] B04.09 Support direct entry to a valid nested destination without assuming the user visited its parent.
- [ ] B04.10 Respect platform navigation gestures, browser history and keyboard conventions.
- [ ] B04.11 Define external-link, external-app and return-to-app behavior.
- [ ] B04.12 Ensure hidden or unavailable destinations cannot be reached through stale shortcuts without a useful explanation.

### B05. Input, focus and selection — Core

- [ ] B05.01 Establish logical focus order, visible focus and reliable activation with supported inputs.
- [ ] B05.02 Specify initial focus and focus return for overlays, newly inserted content and removed elements.
- [ ] B05.03 Avoid focus theft during background refresh, validation or notification arrival.
- [ ] B05.04 Handle software keyboards, input-method composition, hardware keyboards and keyboard dismissal.
- [ ] B05.05 Support text selection, copying, pasting and familiar editing shortcuts where appropriate.
- [ ] B05.06 Define gesture thresholds, cancellation and coexistence with scrolling or system gestures.
- [ ] B05.07 Provide discoverable alternatives to swipe, hover, drag, long-press and precise multitouch actions.
- [ ] B05.08 Define drag feedback, valid drop targets, auto-scroll, cancellation and reorder persistence.
- [ ] B05.09 Account for different pointer precision, touch targets, stylus behavior and button mappings.
- [ ] B05.10 Resolve shortcut collisions with OS, browser, assistive technology and text editing.
- [ ] B05.11 Distinguish single selection, multi-selection, range selection and keyboard navigation.
- [ ] B05.12 Keep selection and focus stable through sorting, filtering, refresh and virtualization.
- [ ] B05.13 Follow compound-widget keyboard conventions: Tab between widgets, appropriate internal navigation and preserved standard text-editing keys. [S09]

### B06. Forms, validation and editing — Conditional: user input

- [ ] B06.01 Define labels, help, required/optional indication, field grouping and sensible defaults.
- [ ] B06.02 Select suitable keyboard/input types, autocomplete hints and submit actions.
- [ ] B06.03 Specify validation timing: while entering, on blur, on submit or after server confirmation.
- [ ] B06.04 Separate local format checks, domain rules, server rejection and connectivity failures.
- [ ] B06.05 Preserve non-sensitive entered work after recoverable failure, navigation and reauthentication.
- [ ] B06.06 Never include passwords, one-time codes or other restricted secrets in general draft recovery.
- [ ] B06.07 Keep error messages associated with fields and provide a usable route to every error.
- [ ] B06.08 Define dirty state, autosave timing, explicit save, discard and undo behavior.
- [ ] B06.09 Handle asynchronous validation races so an old response cannot reject a newer value.
- [ ] B06.10 Prevent unintended duplicate submissions without trapping the user in permanent disabled state.
- [ ] B06.11 Cover paste, autofill, password managers, international names, address variation and long input.
- [ ] B06.12 Define dependent fields, hidden fields and whether their values remain valid or are cleared.
- [ ] B06.13 Handle edits from another device/user and report conflicts before silently losing work.
- [ ] B06.14 Verify both the presented values and the durable values actually written.
- [ ] B06.15 Define multistep progress, earlier-answer review, optional-step skipping and retention of valid answers during backtracking.
- [ ] B06.16 Warn about meaningful time limits and provide extension or recoverable restart where the domain permits it.

### B07. Content, wording and information presentation — Core

- [ ] B07.01 Use consistent domain terminology and concrete action labels.
- [ ] B07.02 Provide useful empty states for first use, no search results, cleared filters and no access.
- [ ] B07.03 Explain failures with a next step and preserve useful technical identifiers outside primary copy.
- [ ] B07.04 Define truncation, wrapping, full-value access, selectable text and overflow handling.
- [ ] B07.05 Use accurate counts, units, timestamps, percentages and status labels.
- [ ] B07.06 Distinguish unknown, unavailable, zero, null, redacted and not-yet-loaded information.
- [ ] B07.07 Provide media alternatives, meaningful link labels and understandable icon labels.
- [ ] B07.08 Review real microcopy for confirmation, deletion, retry, permission, sync and logout flows.
- [ ] B07.09 Ensure user-generated text cannot impersonate trusted interface instructions or status.
- [ ] B07.10 Handle missing translations, missing assets, broken links and stale help content.
- [ ] B07.11 Define content ownership, revision and removal when application correctness depends on maintained content.
- [ ] B07.12 Avoid misleading urgency, hidden consequences and confirmation text that conceals the action.

### B08. State presentation and feedback — Core

- [ ] B08.01 Separate content state, request state, mutation state and presentation state.
- [ ] B08.02 Cover initial, loading, ready, empty, refreshing, partial, failed and unavailable states as applicable.
- [ ] B08.03 Represent cached, stale, optimistic, queued, syncing, conflicted and local-only data honestly.
- [ ] B08.04 Distinguish “failed” from “outcome unknown” after a request may already have reached the server.
- [ ] B08.05 Choose local versus page-level feedback according to the scope of the operation.
- [ ] B08.06 Preserve useful content during refresh instead of repeatedly replacing the screen.
- [ ] B08.07 Avoid premature empty states and success messages before the relevant guarantee is met.
- [ ] B08.08 Define loading feedback delay, long-wait explanation, timeout and recovery behavior.
- [ ] B08.09 Use determinate progress only when a meaningful fraction is known.
- [ ] B08.10 Make important status perceivable without relying only on color, motion, sound or a brief toast.
- [ ] B08.11 Define notification priority and avoid overwhelming users with simultaneous messages.
- [ ] B08.12 Keep actions discoverable after transient feedback disappears.

### B09. Motion, transitions, haptics and sound — Core consideration; conditional implementation

- [ ] B09.01 Inventory transitions: navigation, overlays, expanding content, insertion/removal, reordering, loading and state changes.
- [ ] B09.02 Specify what each animation communicates: location, hierarchy, continuity, progress or action confirmation.
- [ ] B09.03 Define duration, easing, spring behavior and coordinated sequencing using platform/product conventions.
- [ ] B09.04 Make transitions interruptible and reversible when users reverse or repeat an action.
- [ ] B09.05 Handle rapid taps, cancelled gestures, asynchronous completion and changing targets mid-animation.
- [ ] B09.06 Avoid flicker, layout jumps, clipping and objects appearing in the wrong layer during transitions.
- [ ] B09.07 Preserve focus, semantics and operability while visual elements move or disappear.
- [ ] B09.08 Provide reduced-motion behavior that preserves meaning without problematic movement. [S22]
- [ ] B09.09 Avoid gating routine interaction on decorative animation completion.
- [ ] B09.10 Define progress animation, looping motion and when users can pause it.
- [ ] B09.11 Use haptic/audio feedback only where appropriate, respect preferences and provide another channel for essential information.
- [ ] B09.12 Verify frame pacing and transition continuity on representative slower hardware.

### B10. Adaptive layout, device variation and windows — Core

- [ ] B10.01 Adapt to available window space and capabilities, not only device model names.
- [ ] B10.02 Define meaningful compact, intermediate and expanded compositions based on content needs.
- [ ] B10.03 Handle portrait, landscape, split-screen, free resizing and fold/unfold while preserving state.
- [ ] B10.04 Account for safe areas, cutouts, system bars, hinges, window chrome and onscreen keyboards.
- [ ] B10.05 Specify navigation transformations and single-pane/multipane behavior.
- [ ] B10.06 Prevent unusable stretched forms, excessive line lengths and unexplained empty space on wide screens.
- [ ] B10.07 Define scrolling ownership, nested scrolling, sticky content and reaching the final item.
- [ ] B10.08 Test text scaling, display scaling, browser zoom and unusual aspect ratios.
- [ ] B10.09 Handle density/DPI changes and moving windows between displays.
- [ ] B10.10 Restore window bounds safely when a saved monitor is disconnected.
- [ ] B10.11 Test runtime changes while dialogs, keyboards, menus or animations are active.
- [ ] B10.12 Define minimum usable size and a graceful response when less space is available.
- [ ] B10.13 Test constrained height independently of width, including wide, short windows with an open keyboard or overlay.

### B11. Appearance, themes and system preferences — Core

- [ ] B11.01 Support the product's declared light, dark and system-following modes consistently.
- [ ] B11.02 Use semantic roles so error, selection, disabled and focus styling remain meaningful across themes.
- [ ] B11.03 Handle system theme changes while the application is open.
- [ ] B11.04 Define support for high contrast, forced colors, increased contrast and reduced transparency where available.
- [ ] B11.05 Check images, icons, charts, embedded content and external surfaces in every supported theme.
- [ ] B11.06 Verify contrast for text, controls, focus indicators and boundaries in actual backgrounds.
- [ ] B11.07 Handle accent/dynamic colors without making semantic colors ambiguous.
- [ ] B11.08 Prevent incorrect-theme flashes at launch or during navigation.
- [ ] B11.09 Respect user overrides and define their precedence over system defaults.
- [ ] B11.10 Check screenshots and visual regressions with stable system settings and realistic content.

### B12. Accessibility and inclusive completion — Core

- [ ] B12.01 Declare the target accessibility requirements and applicable platforms; distinguish targets from verified conformance.
- [ ] B12.02 Use semantic structure and platform accessibility APIs for headings, groups, controls and relationships.
- [ ] B12.03 Provide meaningful names, roles, values and state changes for custom and standard components.
- [ ] B12.04 Ensure important journeys work with keyboard, screen reader and relevant alternative inputs.
- [ ] B12.05 Keep focus visible, unobscured and predictable across overlays, navigation and content changes.
- [ ] B12.06 Support large text, zoom and reflow without losing controls or task completion.
- [ ] B12.07 Supply alternatives to color-only distinctions, complex gestures and drag-only interaction.
- [ ] B12.08 Make errors identifiable and correctable, including with assistive technology.
- [ ] B12.09 Handle announcements, live updates and progress without repeated or excessive interruptions.
- [ ] B12.10 Cover captions, transcripts, audio description and media controls as the content requires.
- [ ] B12.11 Consider timing limits, cognitive load, flashing content, motion sensitivity and authentication barriers.
- [ ] B12.12 Test reading order and semantics after responsive rearrangement and list virtualization.
- [ ] B12.13 Include accessible third-party content and embedded flows in the journey boundary.
- [ ] B12.14 Combine automated checks, manual operation and representative user feedback; track each method's coverage limits.
- [ ] B12.15 Exclude decorative content from announcements and group semantic children without repeating labels or hiding meaningful controls.

### B13. Internationalization, locale and global data — Core consideration

- [ ] B13.01 Externalize translatable content and avoid assembling sentences from separately translated fragments.
- [ ] B13.02 Handle plural forms, grammatical context, interpolation and translated accessibility labels.
- [ ] B13.03 Test text expansion, pseudolocalization, non-Latin scripts and font fallback.
- [ ] B13.04 Support RTL layout and mixed-direction text; mirror only elements whose meaning requires it.
- [ ] B13.05 Format numbers, currency, units, dates and times according to context and user preference.
- [ ] B13.06 Distinguish instants, local dates, durations and recurring wall-clock times in the data model.
- [ ] B13.07 Handle time-zone changes, daylight-saving transitions and invalid/ambiguous local times.
- [ ] B13.08 Avoid assuming a universal address, phone, personal-name or postal-code structure.
- [ ] B13.09 Define collation, searching, case handling, Unicode normalization and grapheme-aware editing where relevant.
- [ ] B13.10 Support locale changes without corrupting stored values or confusing partially entered input.
- [ ] B13.11 Define fallback behavior for unavailable translations and unsupported locale features.
- [ ] B13.12 Separate locale adaptation from domain-specific regional policy or legal requirements.

## C. Common application capabilities

### C01. Onboarding, help and progressive discovery — Conditional

- [ ] C01.01 Let users reach value quickly, with skippable or resumable explanation where appropriate.
- [ ] C01.02 Request setup information and permissions when the related feature needs them.
- [ ] C01.03 Distinguish first installation, first account use, returning use and migrated users.
- [ ] C01.04 Handle interrupted onboarding without duplicating accounts, setup work or consent prompts.
- [ ] C01.05 Make permissions and optional features understandable before asking for them.
- [ ] C01.06 Provide contextual examples, empty-state guidance and useful recovery links.
- [ ] C01.07 Let users revisit essential tutorials and discover keyboard/gesture alternatives.
- [ ] C01.08 Ensure help remains usable when the service or network is unavailable, where needed.
- [ ] C01.09 Keep feature announcements dismissible and avoid repeating them after every launch.
- [ ] C01.10 Verify that onboarding ends in a functioning product state rather than a decorative completion screen.

### C02. Accounts, authentication and sessions — Conditional

- [ ] C02.01 Decide whether accounts are necessary; define guest/local use if supported.
- [ ] C02.02 Cover registration, sign-in, verification, recovery, logout and account deletion as applicable.
- [ ] C02.03 Support chosen identity methods, password managers, autofill and accessible authentication.
- [ ] C02.04 Handle expired links/codes, repeated submissions and cancelled external authentication.
- [ ] C02.05 Preserve permitted user work through session expiry and reauthentication.
- [ ] C02.06 Coalesce token refresh within the same session/credential family and prevent retry loops or accidental logout storms.
- [ ] C02.07 Define logout effects on protected storage, cached data, downloads, notifications and background work.
- [ ] C02.08 Isolate account/organization data and prevent old asynchronous results entering the new session.
- [ ] C02.09 Define revoked sessions, remote logout, changed credentials and lost second-factor recovery.
- [ ] C02.10 Handle guest-to-account migration and account linking without silent data replacement.
- [ ] C02.11 Show which account or organization owns consequential actions and pending work.
- [ ] C02.12 Make deletion and export status truthful, including retention exceptions supplied by the product's policy.

### C03. Authorization and device permissions — Conditional

- [ ] C03.01 Distinguish application roles/authorization from OS permissions and consent preferences.
- [ ] C03.02 Enforce protected actions and object ownership at a trusted boundary, not only in visible controls.
- [ ] C03.03 Cover not-requested, granted, limited, denied, permanently denied and revoked permission states where supported.
- [ ] C03.04 Explain the feature impact and provide useful fallback behavior.
- [ ] C03.05 Recheck capabilities after returning from settings or an external picker.
- [ ] C03.06 Handle revocation while a camera, file, location or other resource is already in use.
- [ ] C03.07 Request the narrowest access that meets the feature's actual need.
- [ ] C03.08 Preserve work and navigation context across permission prompts.
- [ ] C03.09 Avoid repeated prompting or implying optional access is required for unrelated functionality.
- [ ] C03.10 Test role changes, organization switches and resource access loss during an operation.

### C04. Settings, preferences and user control — Conditional

- [ ] C04.01 Define scope of each preference: device, installation, account, organization or session.
- [ ] C04.02 Define defaults and precedence among user, system, organization and remote configuration.
- [ ] C04.03 Specify immediate apply versus save/cancel behavior and whether restart is necessary.
- [ ] C04.04 Persist settings reliably and migrate renamed or removed preferences.
- [ ] C04.05 Explain unavailable settings and dependencies without silently ignoring changes.
- [ ] C04.06 Provide reset behavior with an explicit scope and appropriate recovery.
- [ ] C04.07 Keep privacy, notification, accessibility and data-use controls discoverable.
- [ ] C04.08 Handle settings synchronization conflicts and offline changes where supported.
- [ ] C04.09 Ensure the displayed preference matches effective runtime behavior.
- [ ] C04.10 Preserve an escape route from configuration that makes the app unusable.

### C05. Search, collections and bulk operations — Conditional

- [ ] C05.01 Define search scope, searchable fields, ranking expectations and supported matching behavior.
- [ ] C05.02 Handle query debouncing, cancellation and out-of-order results.
- [ ] C05.03 Preserve query, filters, sorting and scroll through navigation.
- [ ] C05.04 Distinguish empty collection, zero matches, unavailable search and incomplete results.
- [ ] C05.05 Define pagination/cursor behavior, stable ordering and deduplication during live changes.
- [ ] C05.06 Handle selection across pages, filters and unloaded results explicitly.
- [ ] C05.07 Explain bulk-action scope before applying consequential changes.
- [ ] C05.08 Report partial success and offer retry for only the failed portion when safe.
- [ ] C05.09 Keep row identity, focus and selection stable after edits or refresh.
- [ ] C05.10 Define export, sorting and filtering behavior for large datasets without blocking interaction.

### C06. Notifications and background communication — Conditional

- [ ] C06.01 Define which events deserve interruption, an inbox entry or quiet status only.
- [ ] C06.02 Cover opt-in, categories/channels, preferences and unavailable delivery.
- [ ] C06.03 Make notification actions and deep links work from cold, warm and signed-out states.
- [ ] C06.04 Handle duplicate, delayed, stale and out-of-order messages.
- [ ] C06.05 Keep notification identity/account binding correct after logout or account switching.
- [ ] C06.06 Define lock-screen privacy and content redaction.
- [ ] C06.07 Synchronize read/unread counts and badge semantics where supported.
- [ ] C06.08 Handle revoked permission, token changes and expired registrations.
- [ ] C06.09 Avoid treating push delivery as guaranteed data synchronization.
- [ ] C06.10 Define scheduling, time zones, quiet periods, rescheduling and cancellation for reminders.

### C07. Files, import, export and sharing — Conditional

- [ ] C07.01 Define supported formats, schema versions, encodings and size limits.
- [ ] C07.02 Use appropriate platform pickers, permissions and resource handles.
- [ ] C07.03 Handle missing, renamed, moved, externally modified or temporarily unavailable files.
- [ ] C07.04 Validate content, not only extensions; handle malformed input without partial corruption.
- [ ] C07.05 Define import preview, duplicate handling, partial results and rollback where warranted.
- [ ] C07.06 Define filename, destination, overwrite and collision behavior for exports.
- [ ] C07.07 Write durable outputs safely and verify the result rather than reporting success after generation starts.
- [ ] C07.08 Handle cancellation, low storage, permission loss and interrupted transfers.
- [ ] C07.09 Preserve expected metadata while removing sensitive metadata according to the feature's policy.
- [ ] C07.10 Define sharing lifetime, access grants, temporary-file cleanup and revoked access.
- [ ] C07.11 Keep user work separate from disposable caches and temporary artifacts.
- [ ] C07.12 Provide a usable way to find or reopen a completed export/download.

## D. Data, execution and reliability

### D01. Data models and integrity — Core

- [ ] D01.01 Define entity identity, relationships, ownership and invariants independently of screens.
- [ ] D01.02 Distinguish unknown, absent, zero, default, pending and deleted values.
- [ ] D01.03 Define validation at trusted boundaries and enforce constraints where data is committed.
- [ ] D01.04 Use suitable types for money, timestamps, measurements, identifiers and bounded values.
- [ ] D01.05 Define transaction boundaries and behavior after partial failure.
- [ ] D01.06 Specify uniqueness, duplicate handling, ordering and referential integrity.
- [ ] D01.07 Define serialization, versioning and compatibility with older clients or stored records, including unknown fields/enums when mixed versions are supported.
- [ ] D01.08 Define deletion, archival, tombstones and recovery according to domain needs.
- [ ] D01.09 Handle concurrent writes, conflict detection and ownership changes.
- [ ] D01.10 Test invariants against realistic and malformed boundary data.

### D02. Storage, caching and persistence — Conditional: stored data

- [ ] D02.01 Classify authoritative data, derived data, cache, user files, drafts and secrets.
- [ ] D02.02 Specify the correct persistence location and lifetime for each class.
- [ ] D02.03 Define cache keys, identity partitioning, invalidation, expiration and size limits.
- [ ] D02.04 Keep important user data safe when caches are cleared or storage is evicted.
- [ ] D02.05 Handle disk-full, quota, read-only, corrupted and unavailable-storage conditions.
- [ ] D02.06 Define atomic writes, crash recovery and consistency after interrupted commits.
- [ ] D02.07 Establish consistent backup/restore mechanisms, exclusions and key availability; verify restoration and avoid unsafe ordinary copies of active databases. [S24]
- [ ] D02.08 Define database query/index needs using actual access patterns and expected scale.
- [ ] D02.09 Manage connections, handles and resource cleanup across lifecycle changes.
- [ ] D02.10 Test retained data through restart, upgrade, account change and supported restore paths.
- [ ] D02.11 Define retention and cleanup for abandoned drafts, exports, media and background queues.
- [ ] D02.12 Avoid putting security credentials into ordinary preferences, logs or general-purpose state serialization.

### D03. API contracts and networking — Conditional: remote communication

- [ ] D03.01 Specify request/response schemas, error categories and compatibility expectations.
- [ ] D03.02 Define deadlines, cancellation, timeout classification and user-visible recovery.
- [ ] D03.03 Distinguish connectivity hints from proof that the required service is reachable.
- [ ] D03.04 Handle malformed responses, partial payloads, redirects and unexpected content types.
- [ ] D03.05 Define pagination, filtering, sorting, conditional fetch and consistency contracts.
- [ ] D03.06 Establish which layer owns retries, with bounded attempts, backoff and jitter where appropriate.
- [ ] D03.07 Respect rate limits and overload signals; avoid retry amplification.
- [ ] D03.08 Define idempotency/deduplication for consequential retried writes, including key scope and lifetime.
- [ ] D03.09 Handle expired authentication, permission changes and version incompatibility distinctly.
- [ ] D03.10 Test slow, dropped, repeated and reordered traffic as relevant to the transport.
- [ ] D03.11 Define upload/download resumability, checksums, range support and failure cleanup when needed.
- [ ] D03.12 Avoid exposing sensitive request or response data through diagnostics.

Protocol-level retry and idempotency semantics should be checked against the transport's authoritative specification; for HTTP, use RFC 9110. [S23]

### D04. Concurrency, asynchronous work and background tasks — Conditional

- [ ] D04.01 Assign ownership and lifetime to each asynchronous task or subscription.
- [ ] D04.02 Separate work that should stop with a screen from work that must survive it.
- [ ] D04.03 Handle cancellation cooperatively and do not misreport it as an ordinary failure.
- [ ] D04.04 Prevent stale results from replacing newer data or entering a different account/session.
- [ ] D04.05 Define serialization, locking, atomic operations or immutable snapshots where shared state requires them.
- [ ] D04.06 Bound concurrency, queues, buffering and memory use; define backpressure.
- [ ] D04.07 Keep blocking work off latency-sensitive/UI execution paths.
- [ ] D04.08 Prevent duplicate scheduled work, listeners, timers and subscriptions.
- [ ] D04.09 Handle worker termination, retries, reboot and OS scheduling restrictions.
- [ ] D04.10 Make long-running work observable and cancellable when supported by the underlying operation.
- [ ] D04.11 Release resources after success, failure and cancellation.
- [ ] D04.12 Test interleavings rather than assuming a fast local run rules out races.

### D05. Offline operation and synchronization — Conditional

- [ ] D05.01 Decide which reads and writes work offline; do not promise unsupported offline functionality.
- [ ] D05.02 Identify the source of truth for each entity and the UI's freshness guarantees.
- [ ] D05.03 Define durable queued work, ordering, prerequisites and retry ownership.
- [ ] D05.04 Bind queued work to immutable account/tenant identity and never replay it under a different identity.
- [ ] D05.05 Handle multiple devices, simultaneous edits and explicit conflict resolution.
- [ ] D05.06 Define delete propagation and prevent old replicas from resurrecting deleted data.
- [ ] D05.07 Distinguish local save, queued upload, server acceptance and completed synchronization.
- [ ] D05.08 Handle reconnect bursts, duplicate events, lost acknowledgements and pagination during reconciliation.
- [ ] D05.09 Define stale-read behavior and whether an action may use stale information safely.
- [ ] D05.10 Expose blocked work and let users retry, discard or resolve it where appropriate.
- [ ] D05.11 Define what happens to pending work on logout, uninstall, account deletion and schema upgrade.
- [ ] D05.12 Select conflict policy according to data semantics; do not universally apply last-write-wins.

### D06. Lifecycle, interruption and restoration — Core

- [ ] D06.01 Define cold start, warm resume, backgrounding, suspension and termination behavior per platform.
- [ ] D06.02 Preserve the right non-sensitive state: drafts, position, selection, navigation and active task identity.
- [ ] D06.03 Distinguish configuration recreation from a genuinely new application session.
- [ ] D06.04 Handle lock/unlock, sleep/wake, calls, audio interruptions and external-app round trips as applicable.
- [ ] D06.05 Restore state only for the correct account and currently valid resources.
- [ ] D06.06 Reconcile pending remote operations before allowing actions that might duplicate them.
- [ ] D06.07 Refresh stale credentials, permissions and time-sensitive content on return.
- [ ] D06.08 Release or reacquire camera, microphone, location and other exclusive resources correctly.
- [ ] D06.09 Handle multiple windows, tabs or instances sharing local state.
- [ ] D06.10 Define crash-loop recovery and a safe startup path for invalid stored configuration.
- [ ] D06.11 Test interruption at meaningful boundaries such as before dispatch, after dispatch and during persistence.
- [ ] D06.12 Ensure restoration includes usability details, not just reconstructing a data object.

### D07. Failure handling, recovery and consequential operations — Core

- [ ] D07.01 Classify recoverable, permanent, authentication, authorization, validation and unknown-outcome failures.
- [ ] D07.02 Define recovery ownership and avoid every layer independently retrying the same work.
- [ ] D07.03 Keep user work intact through recoverable errors and state the limits of recovery.
- [ ] D07.04 Resolve ambiguous mutation outcomes through authoritative lookup or safe deduplicated replay.
- [ ] D07.05 Distinguish cancelling local waiting from cancelling the remote action itself.
- [ ] D07.06 Design rollback or compensating actions when one atomic transaction cannot cover the operation.
- [ ] D07.07 Report partial success and define which parts remain actionable.
- [ ] D07.08 Provide a bounded recovery path instead of an endless spinner or retry loop.
- [ ] D07.09 Handle unavailable dependencies with appropriate degradation or an honest blocked state.
- [ ] D07.10 Preserve diagnostic context while keeping internal errors and secrets out of ordinary UI.
- [ ] D07.11 Make destructive recovery options explicit about data loss.
- [ ] D07.12 Verify that undo and rollback actually restore the promised state.

## E. Engineering quality

### E01. Architecture, boundaries and changeability — Core

- [ ] E01.01 Understand the existing repository, conventions and ownership before selecting a new pattern.
- [ ] E01.02 Separate responsibilities sufficiently to reason about UI, domain behavior, data and platform access.
- [ ] E01.03 Choose architecture proportional to current complexity; do not mandate microservices or a particular named pattern.
- [ ] E01.04 Define dependency direction and prevent circular or hidden cross-feature coupling.
- [ ] E01.05 Centralize business invariants without forcing unrelated features into a shared abstraction.
- [ ] E01.06 Make state ownership and side effects explicit and testable.
- [ ] E01.07 Isolate platform-specific behavior behind suitable boundaries when sharing code.
- [ ] E01.08 Design public module APIs, compatibility expectations and error contracts.
- [ ] E01.09 Use dependency injection or equivalent substitution where it meaningfully improves testing and ownership.
- [ ] E01.10 Record significant decisions and tradeoffs in short, maintained architecture notes.
- [ ] E01.11 Design extensibility only for a concrete need; keep migration and removal paths understandable.
- [ ] E01.12 Review changes for effects across UI, persistence, background work and services.

### E02. Code health and review — Core

- [ ] E02.01 Prefer readable names, explicit intent and manageable function/module responsibilities.
- [ ] E02.02 Use types, nullability, exhaustiveness and invariants to prevent invalid states where practical.
- [ ] E02.03 Handle errors explicitly; avoid swallowed failures and success-shaped fallback data.
- [ ] E02.04 Remove dead code, obsolete flags, unused dependencies and misleading comments as scope allows.
- [ ] E02.05 Reduce harmful duplication while avoiding premature generalization.
- [ ] E02.06 Review resource ownership, cleanup, concurrency and cancellation paths.
- [ ] E02.07 Use formatting, lint, compiler diagnostics and static analysis with documented exceptions.
- [ ] E02.08 Keep logging deliberate, useful and free of unnecessary sensitive values.
- [ ] E02.09 Review generated code and dependencies with the same behavioral expectations as hand-written code.
- [ ] E02.10 Keep changes reviewable and separate unrelated refactors from feature work.
- [ ] E02.11 Maintain useful comments about reasons, constraints and non-obvious contracts.
- [ ] E02.12 Prefer tests that catch broken behavior over assertions that merely mirror implementation.

### E03. Security and trust boundaries — Core, depth based on risk

- [ ] E03.01 Identify assets, actors, entry points and trust boundaries with a proportionate threat model.
- [ ] E03.02 Apply least privilege to users, processes, services, plugins and build credentials.
- [ ] E03.03 Validate untrusted input and use appropriate output encoding and safe parsing.
- [ ] E03.04 Enforce authentication, authorization and tenant/object isolation at trusted boundaries.
- [ ] E03.05 Use platform-supported secret storage and reviewed cryptographic primitives with explicit key lifecycle.
- [ ] E03.06 Protect transport and validate endpoint identity; document any exceptional trust configuration.
- [ ] E03.07 Address web-specific injection, cross-site request, content security and origin boundaries where relevant.
- [ ] E03.08 Address native IPC, exported components, WebViews, deep links and local file boundaries where relevant.
- [ ] E03.09 Validate uploaded files, archives, URLs and imported data before privileged processing.
- [ ] E03.10 Define abuse limits and resource bounds for expensive or public operations.
- [ ] E03.11 Keep secrets and sensitive content out of source, crash reports, logs and unintended backups.
- [ ] E03.12 Select applicable OWASP or platform verification requirements and record concrete evidence.
- [ ] E03.13 Plan vulnerability reporting, dependency fixes, key rotation and incident remediation.
- [ ] E03.14 If used, treat obfuscation and client-side checks as supplemental measures rather than authorization boundaries.

### E04. Privacy, data lifecycle and user agency — Core

- [ ] E04.01 Inventory collected, inferred, transmitted and retained data, including SDK behavior.
- [ ] E04.02 Collect the minimum data necessary for specified product purposes.
- [ ] E04.03 Define local versus remote processing and user-visible implications where meaningful.
- [ ] E04.04 Define retention, deletion, export, correction and backup treatment for each data class.
- [ ] E04.05 Make optional telemetry and permissions controllable where the product's requirements call for it.
- [ ] E04.06 Prevent accidental leakage through screenshots, clipboard, recent-app previews, files and notifications as applicable.
- [ ] E04.07 Isolate private/account data in caches, search indexes, temporary files and offline work.
- [ ] E04.08 Prefer redacted diagnostics and explicit inclusion of sensitive support attachments.
- [ ] E04.09 Verify SDK and service disclosures against actual implementation behavior.
- [ ] E04.10 Define shared-device and signed-out behavior, including residual access to user content.
- [ ] E04.11 Route jurisdiction-specific or regulated requirements to current authoritative sources and qualified review.
- [ ] E04.12 Treat privacy as application behavior, not just the presence of a policy page.

### E05. Dependencies, builds and software supply chain — Core

- [ ] E05.01 Evaluate dependency purpose, maintenance, compatibility, footprint, license and replacement options.
- [ ] E05.02 Record toolchain versions, dependency resolution and required environment configuration.
- [ ] E05.03 Use lockfiles or platform equivalents and verify integrity where supported.
- [ ] E05.04 Track direct and transitive vulnerabilities with an actionable update policy.
- [ ] E05.05 Control build-script and CI privileges, untrusted pull-request execution and secret access.
- [ ] E05.06 Define artifact provenance, signing and verification appropriate to distribution risk.
- [ ] E05.07 Separate development, test and production configuration without shipping private credentials.
- [ ] E05.08 Verify clean-checkout builds and detect reliance on untracked local files.
- [ ] E05.09 Manage license notices, source obligations and third-party asset attribution.
- [ ] E05.10 Track dependency removal and end-of-support plans rather than accumulating abandoned packages.
- [ ] E05.11 Measure build time and resource usage on realistic developer hardware.
- [ ] E05.12 Use caches, parallelism and incremental builds without sacrificing correctness or exhausting host resources.

### E06. Runtime performance and resource efficiency — Core

- [ ] E06.01 Set budgets for important operations based on user expectations and target devices.
- [ ] E06.02 Measure startup, time to usable content, interaction latency and sustained workload behavior.
- [ ] E06.03 Measure frame pacing and scrolling/animation performance in realistic content states.
- [ ] E06.04 Bound memory, cache growth, object retention and long-session leaks.
- [ ] E06.05 Profile CPU, disk, network and battery consumption where supported.
- [ ] E06.06 Handle large datasets, expensive images, repeated navigation and background workloads.
- [ ] E06.07 Avoid unnecessary rendering, recomputation, duplicate fetching and unbounded observers.
- [ ] E06.08 Use lazy loading, pagination, virtualization and prefetch only with correct semantics and bounded costs.
- [ ] E06.09 Test constrained networks, low memory, thermal throttling and energy-saving modes where relevant.
- [ ] E06.10 Distinguish cold/warm caches and debug/release builds in performance evidence.
- [ ] E06.11 Track regressions with repeatable representative measurements instead of one fast run.
- [ ] E06.12 Include accessibility, input responsiveness and data correctness in performance tradeoffs.

### E07. Supporting services and infrastructure — Conditional

- [ ] E07.01 Specify service ownership, client contracts, capacity assumptions and reliability objectives.
- [ ] E07.02 Define transactional operations, background jobs, event ordering and duplicate delivery behavior.
- [ ] E07.03 Bound requests, queues, payloads and expensive computations.
- [ ] E07.04 Design overload protection and dependency isolation proportionate to service scale.
- [ ] E07.05 Define database indexing, query limits, connection management and schema rollout.
- [ ] E07.06 Protect secrets, service identities, administration interfaces and tenant boundaries.
- [ ] E07.07 Maintain backup, restore and disaster-recovery procedures with evidence that restoration works.
- [ ] E07.08 Cover old-client/new-server and new-client/old-server compatibility during rollout.
- [ ] E07.09 Track operational cost and prevent accidental unbounded resource consumption.
- [ ] E07.10 Provide meaningful health signals, alert ownership and safe configuration changes.
- [ ] E07.11 Where persistent queues exist, define poison-job handling, dead-letter inspection, safe replay and bounded retention.

## F. Platform adapters

Platform modules should add concrete conventions and current API requirements to the shared contracts. They should not duplicate the entire core or assume one vendor's guideline applies everywhere.

### F01. Web applications and PWAs — Adapter

- [ ] F01.01 Semantic HTML, native form behavior and deliberate custom-widget accessibility.
- [ ] F01.02 URL structure, direct navigation, refresh, history, open-in-new-tab and browser back/forward.
- [ ] F01.03 Responsive layout, zoom, touch/pointer combinations and software-keyboard viewport changes.
- [ ] F01.04 Supported browsers, feature detection and appropriate progressive enhancement.
- [ ] F01.05 Rendering/hydration correctness and recovery from failed script chunks or stale deployments.
- [ ] F01.06 Storage quotas/eviction, private modes and cross-tab state coordination.
- [ ] F01.07 Service-worker scope, cache separation, offline behavior and safe activation of updates. [S20]
- [ ] F01.08 Cookie/session/origin boundaries, cross-site protections and embedded-content restrictions.
- [ ] F01.09 Downloads, uploads, printing, clipboard and permission differences across browsers.
- [ ] F01.10 Performance measures appropriate to web journeys, including field conditions. [S17]
- [ ] F01.11 Installation, launch display, icon/manifest quality and fallback when PWA capabilities are unavailable.
- [ ] F01.12 Public-page metadata, indexing, canonical URLs and sharing previews when discovery is a product requirement.

### F02. Android — Adapter

- [ ] F02.01 Lifecycle recreation, process death, saved state and task/back-stack behavior.
- [ ] F02.02 System back, predictive-back integration where applicable and gesture navigation.
- [ ] F02.03 Insets, edge-to-edge content, keyboard changes and system bar readability.
- [ ] F02.04 Adaptive windows, tablets, foldables, desktop modes and external input.
- [ ] F02.05 Runtime permissions, limited grants, revocation and platform-approved pickers.
- [ ] F02.06 Background work, foreground-service applicability, power restrictions and scheduling.
- [ ] F02.07 App links, intents, share targets, notifications, shortcuts and widgets when supported.
- [ ] F02.08 TalkBack, accessibility semantics, text/display scaling and alternative input.
- [ ] F02.09 Scoped storage, protected credential storage, backup and migration behavior.
- [ ] F02.10 Device/API/OEM variation, unavailable hardware and capability detection.
- [ ] F02.11 App bundle/APK packaging, signing, native ABI support and release-build behavior.
- [ ] F02.12 Current target-SDK behavior changes and chosen distribution-channel requirements.

### F03. Apple platforms — Adapter

- [ ] F03.01 iOS/iPadOS/macOS lifecycle and scene/window behavior as applicable.
- [ ] F03.02 Navigation, presentation, dismissal and platform gesture expectations.
- [ ] F03.03 Safe areas, Dynamic Type, multitasking layouts and external display behavior.
- [ ] F03.04 VoiceOver, keyboard/full-keyboard access, contrast and motion preferences.
- [ ] F03.05 Permission, entitlement and privacy-description requirements for actual capabilities used.
- [ ] F03.06 Protected storage, file access and document ownership/lifecycle.
- [ ] F03.07 Universal links, sharing, widgets, notifications and other supported extensions.
- [ ] F03.08 Background execution, interruption, resource contention and state restoration.
- [ ] F03.09 Native menus, commands, pointer interactions and multiwindow patterns on supported devices.
- [ ] F03.10 Signing, packaging, update compatibility and chosen distribution requirements.
- [ ] F03.11 Runtime availability checks and supported OS/framework combinations.
- [ ] F03.12 Platform-specific asset, icon, theme and visual material behavior without assuming every Apple device uses identical UI.

### F04. Desktop: Windows, Linux and macOS-specific integration — Adapter

- [ ] F04.01 Window sizing, snapping, multiple displays, scaling and safe position restoration.
- [ ] F04.02 Menus, keyboard shortcuts, context menus, toolbars and command discovery.
- [ ] F04.03 Close/minimize/quit semantics, multiple instances and unsaved-document handling.
- [ ] F04.04 Open-with, file associations, drag/drop, clipboard and native pickers.
- [ ] F04.05 Background/tray behavior, startup registration and user control where supported.
- [ ] F04.06 Sandboxes, filesystem permissions, OS credential stores and interprocess communication.
- [ ] F04.07 Linux desktop integration, portals, themes, launcher/file registration and GNOME/KDE conventions as applicable. [S25]
- [ ] F04.08 Windows activation, notifications, accessibility and packaging choices as applicable.
- [ ] F04.09 Installer/uninstaller/update behavior and handling of retained user data.
- [ ] F04.10 Native toolkit versus web-runtime tradeoffs, including memory, input and platform integration.
- [ ] F04.11 Resume from sleep, disconnected devices, mounted volumes and session restoration.
- [ ] F04.12 Keyboard-only and assistive-technology completion of all critical desktop workflows.

### F05. Shared-code and hybrid applications — Adapter

- [ ] F05.01 Define what is shared: business rules, data, networking, UI or all of them.
- [ ] F05.02 Maintain a feature/capability matrix across targets and explicit behavior for unavailable capabilities.
- [ ] F05.03 Preserve native lifecycle, input and accessibility semantics through abstraction boundaries.
- [ ] F05.04 Define thread, memory, serialization and error contracts across native/runtime bridges.
- [ ] F05.05 Test platform-specific code and integrations separately from shared unit tests.
- [ ] F05.06 Review embedded web content, JavaScript bridges and plugin trust boundaries where present.
- [ ] F05.07 Handle platform-specific persistence, package size, startup and rendering costs.
- [ ] F05.08 Keep parity goals explicit without forcing identical appearance or unsupported features.

### F06. Additional device families — Specialist adapters

- [ ] F06.01 TV: directional focus, remote input, viewing distance, overscan considerations and playback interruption.
- [ ] F06.02 Wearables: brief tasks, small/round displays, crown/buttons, haptics, connectivity and energy limits.
- [ ] F06.03 Automotive: platform-approved tasks, driver distraction constraints and current platform safety requirements.
- [ ] F06.04 Spatial/XR: spatial layout, focus/targeting, physical comfort, tracking loss and safe transitions.
- [ ] F06.05 Kiosks/shared terminals: session clearing, physical access, idle behavior and recoverability.
- [ ] F06.06 Embedded/IoT companions: pairing, reconnect, firmware compatibility and offline device state.
- [ ] F06.07 CLI/TUI applications: terminal sizing, key handling, pipes, exit codes, cancellation, accessible output and configuration.
- [ ] F06.08 Games and highly interactive graphics: dedicated performance, input, simulation and accessibility modules beyond this general core.

## G. Specialist feature packs

These are future module candidates. Each needs its own research and acceptance criteria when selected; the inventory does not establish specialist readiness.

| ID | Trigger | Coverage to develop |
| --- | --- | --- |
| G01 | Audio/video playback | Buffering, seeking, queues, track changes, audio focus, route changes, background controls, captions, downloads, codec/capability fallback, accurate duration and position |
| G02 | Camera/recording/media editing | Permission, preview orientation, capture lifecycle, interruption, device selection, encoded output, applied effects, EXIF/privacy, storage failure and saved-media verification |
| G03 | Location/maps/navigation | Accuracy, approximate grants, stale positions, unavailable sensors, offline maps, route changes, battery, geographic conventions and location privacy |
| G04 | Real-time communication | Connection state, reconnect, ordering, duplication, acknowledgements, delivery/read semantics, presence, blocking, retention and call-device changes |
| G05 | Collaboration/documents | Concurrent edits, merge/conflict policy, autosave, undo boundaries, presence, permissions, version history, large documents and offline collaboration |
| G06 | Commerce/subscriptions | Pricing authority, currency, inventory, repeated checkout, pending outcomes, entitlements, restoration, refunds, cancellation and receipt validation; domain review when needed |
| G07 | Social/user-generated content | Uploads, moderation, reporting, blocking, visibility, content removal, appeals, abuse controls, media privacy and age-related product requirements |
| G08 | AI-powered features | Task-specific evaluations, uncertainty, streaming, cancellation, retry cost, model/version changes, prompt injection boundaries, tool authority, private data, fallback and human correction |
| G09 | Plugins/extensions | Capability model, permissions, isolation, API versions, resource limits, signing/trust policy, updates, revocation, failure containment and discoverability |
| G10 | Analytics/dashboards | Data provenance/freshness, missingness, units, aggregation, filtering, drilldown, exports, accessible alternatives and avoiding misleading scales |
| G11 | Calendar/scheduling | Recurrence, time zones, daylight-saving boundaries, reminders, exceptions, conflict resolution, invitations and cancellation |
| G12 | Hardware/Bluetooth/USB | Discovery, pairing, permissions, reconnect, device ownership, firmware/protocol versions, dropped transfers and unavailable hardware |
| G13 | Enterprise/multi-tenant tools | Role matrices, organization switching, auditability, policy controls, SSO lifecycle, delegated administration, bulk work and tenant isolation |
| G14 | Educational/children's apps | Age-appropriate interaction, guardian roles where relevant, accessibility, progress integrity, privacy and specialist policy review |
| G15 | Health/financial/safety-critical workflows | Domain-specific standards, hazard analysis, specialist review, data integrity, auditability and validated recovery; general app guidance alone is insufficient |
| G16 | Scientific/creative/professional tools | Numerical precision, units, reproducibility, color/format fidelity, large projects, specialized input, undo, export integrity and long-running work |

## H. Verification, delivery and maintenance

### H01. Test strategy and automated verification — Core

- [ ] H01.01 Derive tests from user outcomes, invariants and likely failure modes.
- [ ] H01.02 Select unit, integration, contract, component and end-to-end tests according to what each can prove.
- [ ] H01.03 Cover critical journeys with real integration boundaries rather than exclusively mocked success paths.
- [ ] H01.04 Test boundary data, invalid input, missing data and realistic scale.
- [ ] H01.05 Test asynchronous ordering, cancellation, duplicates and interruption where applicable.
- [ ] H01.06 Test storage migrations and preserved data values, not only the resulting schema.
- [ ] H01.07 Test access control, identity changes and protected-data isolation.
- [ ] H01.08 Add visual regression coverage for representative components/states when useful and review baselines intentionally.
- [ ] H01.09 Run accessibility automation while tracking what still requires manual verification.
- [ ] H01.10 Make tests deterministic using controlled clocks, randomness, data and network conditions where practical.
- [ ] H01.11 Track flaky tests, cleanup, isolation and useful failure diagnostics.
- [ ] H01.12 Verify the released configuration and artifact, including any enabled optimization, obfuscation and feature flags.
- [ ] H01.13 Use property/state-machine/fuzz/load tests when their specific risk warrants the cost.
- [ ] H01.14 Treat coverage numbers as supporting information, not proof that the important behaviors were tested.

Tool-specific testing modules should preserve user-visible assertions and isolated state rather than bind checks unnecessarily to implementation details. Playwright provides one primary-source example for web automation. [S26]

### H02. Manual review and environment matrix — Core

- [ ] H02.01 Exercise complete critical journeys rather than reviewing only isolated screenshots.
- [ ] H02.02 Inspect spacing, alignment, typography, clipping, stacking and touch/focus targets with real content.
- [ ] H02.03 Review transitions, interruption and rapid repeated input in the running application.
- [ ] H02.04 Verify keyboard, screen reader and relevant alternative-input completion.
- [ ] H02.05 Cover representative minimum, common and demanding device configurations.
- [ ] H02.06 Test compact/expanded windows, orientation, keyboard visibility and runtime resizing.
- [ ] H02.07 Test supported themes, contrast settings, text scales, locales and RTL.
- [ ] H02.08 Test offline, slow, unstable and service-unavailable conditions appropriate to the app.
- [ ] H02.09 Test empty, small, large, malformed and externally changed data sets.
- [ ] H02.10 Test session expiry, account switching, permission changes and role revocation.
- [ ] H02.11 Test cold start, resume, process termination, crash recovery and multiple instances where supported.
- [ ] H02.12 Select combinations by consequence and likely interaction; do not require an impractical full Cartesian product.
- [ ] H02.13 Record what used physical hardware, emulation, simulation or static inspection.
- [ ] H02.14 Mark untested environments and blocked checks explicitly.

### H03. Installation, releases, updates and migrations — Core for distributed apps

- [ ] H03.01 Verify fresh installation, first launch, update and uninstall through supported channels.
- [ ] H03.02 Test upgrades from each supported starting version, including users who skipped releases.
- [ ] H03.03 Migrate databases, preferences, caches, documents and queued work where their formats changed.
- [ ] H03.04 Preserve user data and verify value-level correctness after migration.
- [ ] H03.05 Define behavior for interrupted or failed migration, insufficient space and incompatible data.
- [ ] H03.06 Establish rollback feasibility; do not assume an older binary can read newer data.
- [ ] H03.07 Coordinate clients, services, feature flags and schema changes during mixed-version operation.
- [ ] H03.08 Verify signing, entitlements, permissions, icons, metadata and release configuration.
- [ ] H03.09 Define staged rollout, stop conditions and recovery where the distribution channel supports them.
- [ ] H03.10 Keep release notes, known limitations, migration guidance and support information accurate.
- [ ] H03.11 Verify update prompts preserve ongoing work and provide a usable path when an update is mandatory.
- [ ] H03.12 Test actual published/packaged artifacts rather than only development builds.

### H04. Observability, support and incidents — Core consideration; implementation proportional to deployment

- [ ] H04.01 Define useful signals for failures, latency, lost work, blocked journeys and background-work health.
- [ ] H04.02 Correlate events across a logical operation without unnecessarily collecting personal information.
- [ ] H04.03 Capture enough diagnostic context to reproduce failures, including version and relevant environment.
- [ ] H04.04 Keep logs, metrics, traces and crash reporting bounded and appropriately redacted.
- [ ] H04.05 Distinguish user cancellation, expected errors and product defects in reporting.
- [ ] H04.06 Monitor success of important workflows rather than server availability alone.
- [ ] H04.07 Define actionable alerts and ownership for services that require operations support.
- [ ] H04.08 Provide user-facing diagnostics/export and issue-report guidance when appropriate.
- [ ] H04.09 Maintain incident response, rollback, communication and recovery procedures appropriate to the product.
- [ ] H04.10 Turn confirmed recurring failures into regression cases and improved guidance.
- [ ] H04.11 Avoid making optional remote telemetry a prerequisite for local application quality.
- [ ] H04.12 Define retention and access controls for diagnostic data.
- [ ] H04.13 Retain release-matched symbols/source maps where applicable and verify that shipping-build failures can actually be diagnosed.

### H05. Documentation, developer experience and maintenance — Core

- [ ] H05.01 Provide a reproducible setup path with required tools, configuration and build/test commands.
- [ ] H05.02 Explain repository structure, important boundaries and how to add a feature in the established style.
- [ ] H05.03 Document supported platforms, known limitations and capability differences.
- [ ] H05.04 Maintain contract/API documentation and examples where other modules or developers rely on them.
- [ ] H05.05 Record architecture decisions, migrations and non-obvious operational constraints.
- [ ] H05.06 Keep contributing, review and issue-reproduction instructions useful for new contributors.
- [ ] H05.07 Track technical debt by consequence and planned action rather than accumulating vague TODOs.
- [ ] H05.08 Maintain dependency, platform and toolchain upgrade procedures.
- [ ] H05.09 Remove or deprecate obsolete features with explicit compatibility and data treatment.
- [ ] H05.10 Monitor build/test cost and developer resource usage as the project grows.
- [ ] H05.11 Keep product documentation consistent with the implemented behavior.
- [ ] H05.12 Establish ownership for ongoing maintenance and eventual service/product retirement.

### H06. Completion evidence and review discipline — Core

- [ ] H06.01 Link each selected requirement to implementation and a verification method.
- [ ] H06.02 Separate planned, implemented, verified, deferred, blocked and not-applicable work.
- [ ] H06.03 Record reproducible evidence: relevant commands, scenarios, artifacts and results.
- [ ] H06.04 Distinguish static review, automated execution, manual interaction and user evidence.
- [ ] H06.05 Check visible affordances against actual behavior and remove misleading incomplete promises.
- [ ] H06.06 Review feature connections, not just the files changed in isolation.
- [ ] H06.07 Define release blockers by consequence and likelihood; keep cosmetic improvements proportionate.
- [ ] H06.08 Report unresolved assumptions, unsupported environments and required external dependencies.
- [ ] H06.09 Verify a bug's trigger and expected effect before presenting it as confirmed.
- [ ] H06.10 Do not claim device, accessibility, security or performance validation that did not happen.
- [ ] H06.11 Keep small changes on a focused review path; broaden checks when their impact crosses boundaries.
- [ ] H06.12 Preserve a concise project handoff so later agents can continue without rediscovering settled facts.

## I. Requirements for the future skill itself

### I01. Token-efficient structure and routing — Core skill design

- [ ] I01.01 Keep the entry file limited to activation, triage, routing, core invariants and required output.
- [ ] I01.02 Maintain a compact index of modules with precise triggers and scope boundaries.
- [ ] I01.03 Load only applicable platform, feature and risk modules for the current task.
- [ ] I01.04 Store shared requirements once and reference stable IDs rather than duplicating prose.
- [ ] I01.05 Separate enduring principles from version-specific API instructions and policy checks.
- [ ] I01.06 Use concise rule cards with applicability, requirement, acceptance criterion and verification.
- [ ] I01.07 Keep long examples, research notes, tool instructions and troubleshooting outside the normal reading path.
- [ ] I01.08 Provide task modes for discovery, implementation, review, regression diagnosis and release readiness.
- [ ] I01.09 Support focused changes without rereading or rechecking the entire catalogue.
- [ ] I01.10 Discover actual repository capabilities and available tools before selecting commands or frameworks.
- [ ] I01.11 Avoid universal stack prescriptions, arbitrary numeric targets and speculative abstractions.
- [ ] I01.12 Keep a compact project-specific applicability/evidence record so future sessions reload relevant context only.
- [ ] I01.13 Use scripts for repeatable mechanical checks when they reduce mistakes; keep their output selective.
- [ ] I01.14 Measure routing accuracy and token cost, not just entry-file length.

### I02. Development over time and quality of the skill — Core skill design

- [ ] I02.01 Develop and review one bounded scope at a time with an explicit status and owner.
- [ ] I02.02 Separate candidate ideas from accepted guidance and deprecated guidance.
- [ ] I02.03 Require concrete failure examples or a clear rationale for adding new rules.
- [ ] I02.04 Track source authority, relevant version, review date and conditions requiring revalidation.
- [ ] I02.05 Maintain changelog, stable identifiers and migration notes for reorganized modules.
- [ ] I02.06 Deduplicate overlapping rules and define precedence when platform and general guidance differ.
- [ ] I02.07 Test the skill on representative web, mobile and desktop tasks, including small changes.
- [ ] I02.08 Evaluate whether agents detect real omissions without inventing requirements or expanding scope unnecessarily.
- [ ] I02.09 Evaluate correct implementation, evidence quality, false positives, missed issues and token/tool cost.
- [ ] I02.10 Include counterexamples where a rule is not applicable or a simpler solution is preferable.
- [ ] I02.11 Reassess modules after actual failures, platform changes or repeated confusion.
- [ ] I02.12 Keep user/project instructions authoritative and avoid embedding unrequested publication or approval behavior.
- [ ] I02.13 Define how agents handle unavailable tools: complete independent work and report exact verification limits.
- [ ] I02.14 Keep security/compliance specialist referrals specific to actual domain requirements.
- [ ] I02.15 Compare representative and held-out tasks with and without the skill, measuring omissions, false positives, unnecessary work and token cost.

## J. Cross-cutting omission tests

These original example scenarios illustrate the detail level the eventual rules should reach. They are not extra features to add indiscriminately.

| Situation | What the skill should make an agent verify |
| --- | --- |
| A user presses Save twice on a slow connection | One intended operation; clear pending state; safe duplicate handling; a recoverable final outcome |
| The server commits a change but the reply is lost | UI does not assert failure prematurely; authoritative reconciliation prevents duplication |
| Account A has queued work, then account B signs in | A's queue and results never execute or appear under B |
| A search request for an old query finishes last | New query results remain visible |
| A selected row is deleted while a menu is open | The menu closes or becomes validly unavailable; focus lands somewhere useful |
| A dialog closes after its launching control disappeared | Focus returns to a suitable surviving destination |
| The keyboard opens over a form's submit action | The field, its error and the completion action remain reachable |
| The app changes from two panes to one during editing | Selection, draft and navigation context remain coherent |
| Large text makes a translated label wrap | Content remains legible and the control still works |
| Reduced motion is enabled during a transition | Meaning and completion remain clear without problematic motion |
| Permission is revoked while a resource is active | Work stops or degrades safely, resources are released and recovery is explained |
| A file is moved or storage fills during export | No false completion; partial output is handled and retry preserves the original work |
| A device sleeps during upload | Resumption or retry follows a defined, observable policy |
| An app process is killed after a local draft save | The permitted draft is recoverable without leaking it to another identity |
| An old notification refers to a deleted item | A valid explanation and useful destination replace a dead end |
| Another window changes settings or logs out | Effective state is reconciled without stale privileges or UI contradictions |
| A user upgrades after skipping several releases | Migration preserves their actual data and pending work |
| A service-worker update arrives while a form is dirty | Update behavior avoids losing input or mixing incompatible assets/storage |
| An external monitor is removed before reopening | The window remains visible and operable |
| An animation is reversed halfway through | It continues from its actual state without a jump or duplicated operation |
| A batch operation succeeds for only some items | The UI identifies completed and failed items and retries safely |
| Connectivity returns but authentication has expired | Pending work waits for correct authentication instead of failing repeatedly |
| A token-refresh request finishes after logout | The logged-out state is not silently replaced by the old session |
| An action is accessible only through hover or swipe | Another supported input can discover and perform it |
| A test suite passes while a visible button does nothing | Journey verification identifies the missing implementation |

## K. Suggested order for developing the skill

This is a proposed order for discussion, not a commitment to implement all scopes now. Accessibility, security and data integrity apply from the first relevant module; they are not postponed until a late polishing phase.

| Increment | Main content | Why start here / evidence of useful progress |
| --- | --- | --- |
| 1 | Applicability model, rule-card structure, evidence/status model and compact routing | Establish a way to grow without creating a prompt that must always be loaded in full |
| 2 | Journey/surface inventory, component contracts, state presentation, navigation and forms | Directly addresses missing elements and behaviors in ordinary app work |
| 3 | Adaptive layout, input/focus, accessibility, appearance, content and motion | Makes the same journey complete across realistic device and interaction conditions |
| 4 | Persistence, lifecycle, asynchronous work, networking, recovery and offline behavior | Prevents lost work, incorrect status, stale results and duplicate operations |
| 5 | Architecture, code health, security/privacy depth, dependencies and performance | Gives agents implementation and review guidance that remains maintainable |
| 6 | Web, Android, Apple, desktop and shared-code adapters, developed individually | Adds native conventions and current API specifics without bloating the common core |
| 7 | Test matrices, release/update/migration, operations and maintenance depth | Establishes reliable completion and continued quality after release |
| 8 | Selected specialist feature packs and regression-driven refinements | Expands only when an actual product or recurring omission justifies it |

At every increment, include its own verification examples and evaluate token cost. Tests and review are part of each increment; increment 7 adds broader delivery and operational coverage.

## L. Proposed acceptance criteria for this scope project

- The inventory includes product purpose, UI details, functional contracts, code quality, data/reliability, platform behavior, verification and maintenance.
- Every future module has a clear applicability trigger and avoids requiring unnecessary product features.
- Every adopted rule can lead to an observable decision, implementation requirement or verification result.
- Platform-specific claims and changing API requirements have primary-source references and review dates.
- The common entry remains small; extensive detail lives in selectively loaded modules.
- The skill can improve incrementally without repeatedly rewriting its foundation.
- Quality claims remain tied to actual evidence, and unverified behavior remains visible.

## Sources and research boundaries

Primary sources consulted for the initial taxonomy, accessed 31 October 2026. Links are reference material for later module development, not a requirement to load every source during every task. Standards, platform recommendations and our proposed practices must remain distinguishable.

| ID | Source | Used to inform |
| --- | --- | --- |
| S01 | [ISO/IEC 25010:2023 public abstract](https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/07/81/78176.html) | Lifecycle quality model and specification/evaluation framing; full standard not reviewed |
| S02 | [Android core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) | Broad platform quality and runtime conditions |
| S03 | [Android adaptive display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes) | Responsive/adaptive window behavior |
| S04 | [Apple Human Interface Guidelines: Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Layout, adaptation and platform context |
| S05 | [Windows keyboard interactions](https://learn.microsoft.com/en-us/windows/apps/develop/input/keyboard-interactions) | Keyboard and focus conventions |
| S06 | [GNOME Human Interface Guidelines](https://developer.gnome.org/hig/) and [accessibility](https://developer.gnome.org/hig/guidelines/accessibility.html) | Linux-native components, conventions and accessibility review |
| S07 | [KDE Human Interface Guidelines](https://develop.kde.org/hig/) | Desktop workflows, platform integration and evolving guidance |
| S08 | [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Testable web accessibility requirements; not a blanket claim of native conformance |
| S09 | [WAI ARIA Authoring Practices: Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) | Custom-widget keyboard, focus and selection behavior |
| S10 | [WAI WCAG Evaluation Methodology overview](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) | Scope, representative evaluation and evidence |
| S11 | [Android offline-first architecture](https://developer.android.com/topic/architecture/data-layer/offline-first) | Offline data, queued writes and conflict-policy decisions |
| S12 | [Android Room database migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions) | Preserving and testing data across schema upgrades |
| S13 | [OWASP ASVS](https://asvs.owasp.org/) | Web/service security verification scope |
| S14 | [OWASP MASVS](https://mas.owasp.org/MASVS/) | Mobile security areas and verification references |
| S15 | [NIST Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf) | Risk-based secure-development lifecycle |
| S16 | [Google Engineering Practices: What to look for in a code review](https://github.com/google/eng-practices/blob/master/review/reviewer/looking-for.md) | Design, function, complexity and meaningful review |
| S17 | [Web Vitals](https://web.dev/articles/vitals) | Web experience measurement and field/lab distinction |
| S18 | [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) | Operational evidence and diagnostic signals |
| S19 | [SLSA specification 1.2](https://slsa.dev/spec/v1.2/) | Supply-chain provenance and assurance reference |
| S20 | [Service worker lifecycle](https://web.dev/articles/service-worker-lifecycle) | PWA update and multi-version lifecycle concerns |
| S21 | [GNOME design principles](https://developer.gnome.org/hig/principles) | Product scope, simplicity and user effort |
| S22 | [Apple Reduced Motion evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria) | Preserving meaning while accommodating motion sensitivity |
| S23 | [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | Method semantics, idempotency and retry reference |
| S24 | [SQLite corruption guidance](https://www.sqlite.org/howtocorrupt.html) | Concrete persistence and backup failure cases |
| S25 | [freedesktop.org Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry/latest-single/) | Linux launcher identity, activation and file associations |
| S26 | [Playwright best practices](https://playwright.dev/docs/best-practices) | User-visible assertions and isolated automated tests |

The existing Professional App Quality skill was also reviewed as contextual input. Its state, recovery, accessibility and conditional-reference structure overlaps with parts of this proposal. No skill was created, changed or installed as part of this research.

Specialist feature packs are topic inventories, not completed domain research. Their detailed rules, exact thresholds and release requirements should be researched when their scope is selected. This document deliberately avoids freezing changing platform policies or arbitrary universal performance targets into the shared core.
