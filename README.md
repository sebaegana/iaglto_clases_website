# iaglto_clases_website

Repositorio del sitio Quarto del curso y su material de clases.

## Estructura

- La raiz del repo es el unico proyecto Quarto que define el sitio.
- `clases/` contiene el contenido fuente de las clases, imagenes, extensiones y materiales de apoyo.
- `docs/` es la salida publicada del sitio.
- `renv/` y `renv.lock` fijan el entorno de R del proyecto.
- `notes/` guarda apuntes operativos que no forman parte del sitio.

## Flujo de trabajo

Render del sitio completo:

```bash
quarto render
```

El sitio publicado se genera en `docs/`.

## Notas tecnicas

Si al generar PDFs aparece un problema de idioma en TinyTeX, instalar:

```r
tinytex::tlmgr_install("babel-spanish")
```
