# Skill: resumir_reunion

## Propósito

Convertir la transcripción de una reunión en una minuta breve y accionable.

## Cuándo usarla

- Cuando exista una transcripción o notas extensas
- Cuando se necesite un resumen ejecutivo rápido
- Cuando el usuario pida acuerdos, responsables o próximos pasos

## Entrada esperada

- Transcripción completa, parcial o apuntes de reunión
- Contexto opcional sobre proyecto, cliente o área

## Instrucciones

1. Identifica el tema central de la reunión.
2. Resume solo lo que aparece en la entrada.
3. No inventes acuerdos, fechas ni responsables.
4. Si falta información crítica, indícalo explícitamente.
5. Usa un tono ejecutivo, claro y breve.

## Salida

Entregar en este formato:

```text
Resumen:
<2 a 4 líneas>

Acuerdos:
- ...

Pendientes:
- ...

Responsables mencionados:
- ...

Riesgos o temas abiertos:
- ...
```

## Criterios de calidad

- Fidelidad a la fuente
- Brevedad
- Claridad
- Estructura consistente

## Ejemplo de activación

"Resume esta reunión y entrégame acuerdos, pendientes y riesgos."
