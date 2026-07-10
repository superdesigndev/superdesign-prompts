# Page Types — the *structure* axis

The counterpart to [`../systems/`](../systems/). Where a system carries **style**,
a page type carries **structure** — the sections and components a given kind of
page needs, independent of how it looks.

Each `SKILL.md` here is aggregated across every prompt of that category in the
repo, so it captures the *common* anatomy (e.g. what a pricing page usually
contains) rather than one designer's take.

| Page type | Built from |
|---|---|
| [Landing Pages](landing-pages/) · [Pricing Pages](pricing-pages/) · [Auth & Login](auth-login/) · [Dashboards](dashboards/) · [AI Chat](ai-chat/) · [Onboarding](onboarding/) · [Waitlist & Coming Soon](waitlist-coming-soon/) · [Forms & Contact](forms-contact/) · [Blog & Editorial](blog-editorial/) · [E-commerce](e-commerce/) · [Portfolios](portfolios/) · [Mobile Apps](mobile-apps/) · [Components](components/) · [Calendar](calendar/) · [Email & Newsletter](email-newsletter/) | the prompts in each matching category |

## Use a page type

Pair it with a [system](../systems/):

```text
Build a <page type> using the "<system-id>" design system.
Include the common sections/components listed in page-types/<page-type>/SKILL.md.
```

Regenerate:

```bash
python3 scripts/factor_prompts.py
```
