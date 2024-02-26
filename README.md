# Blocking and Non-Blocking HTTP Request

- Função e View Assíncrona
- Função e View Síncrona

Exercício do módulo de Djando Async Views do curso de Full Stack Python da EBAC - Escola Britânica de Artes Criativas e Tecnologia

## Para executar

Foi utilizado uvicorn neste projeto:

```uvicorn --reload asyncviews.asgi:application```

http://127.0.0.1:8000/async - Para View assíncrona

Página é renderiza mesmo com a função de contagem de seis segundos em segundo plano.

http://127.0.0.1:8000/sync - Para View síncrona

Página aguarda a contagem de 6 segundos para ser renderizada.

