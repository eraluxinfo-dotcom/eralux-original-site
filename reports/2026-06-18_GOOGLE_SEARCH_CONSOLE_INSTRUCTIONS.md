# Google Search Console instructions

Run these steps only after an approved production deployment:

1. Open Google Search Console.
2. Add a Domain property or URL-prefix property for the approved domain.
3. Verify ownership through DNS or an HTML verification file.
4. Open **Sitemaps**.
5. Submit `https://DOMAIN/sitemap.xml`.
6. Open **URL Inspection** and inspect the main Ukrainian URL.
7. Select **Request indexing**.
8. Repeat inspection for `/ru/` and `/en/` if required.

Prepared locally:

- `robots.txt`
- `sitemap.xml`
- canonical URLs
- RU / UK / EN hreflang and x-default
- OpenGraph metadata
- schema.org `LocalBusiness`
