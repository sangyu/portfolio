# Adding a learning resource

1. Put the PDF in `../files/learning/` with a descriptive filename.
2. Put a preview image in `../images/learning/`.
3. Copy `chinese-multiplication-table.qmd` to a new `.qmd` file in this directory.
4. Update its title, description, image, image-alt, categories, PDF links, and page text. Describe what the resource actually contains in English and Chinese where useful.
5. Run `quarto render` from `nbs`.

The Bilingual Learning grid automatically includes every `.qmd` resource in this directory. Each resource gets its own HTML page, searchable text, social metadata, and sitemap entry through the existing Quarto website configuration.
