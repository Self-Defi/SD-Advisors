# SDA Website Release Checklist

This branch is the proposed consulting-site redesign. The live site remains on main until merge.

## Automated static checks
Run `python3 scripts/check_site.py` from the repository root. The script uses only the Python standard library and checks all seven pages for required structure, internal links, assets, and known placeholder patterns.

## Manual release checks
- [ ] Review all seven pages at desktop, tablet and phone widths
- [ ] Verify keyboard navigation, focus visibility and horizontal navigation scrolling
- [ ] Open each navigation item and CTA in a real browser
- [ ] Confirm the Self Defi logo displays on every page
- [ ] Check portfolio and WMS demonstration destinations
- [ ] Confirm the Cal.com 15-minute discovery booking works
- [ ] Confirm whether the existing $100 / 60-minute strategy session is still offered and establish a matching booking destination
- [ ] Verify the public email address and published service descriptions
- [ ] Verify any client work has permission to be presented
- [ ] Merge pull request into main and verify GitHub Pages deployment

## Organizational structure
Self Defi is the parent organization. SD Advisory Group is the client-facing consulting practice. B.O.B. (Building on a Budget) is the Research & Development division.

No credentials, private keys, testimonials, or unverified outcome metrics should be committed.
