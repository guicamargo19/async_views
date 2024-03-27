# Async e Sync Views

## Blocking and Non-Blocking HTTP Request

- Função e View Assíncronas
- Função e View Síncronas

Djando Async Views do curso de Full Stack Python da EBAC - Escola Britânica de Artes Criativas e Tecnologia

## Para executar

Foi utilizado uvicorn neste projeto:

```uvicorn --reload asyncviews.asgi:application```

[http://127.0.0.1:8000/async](http://127.0.0.1:8000/async) - Para View assíncrona

Página é renderizada mesmo com a função de contagem de seis segundos em segundo plano.

[http://127.0.0.1:8000/sync](http://127.0.0.1:8000/sync) - Para View síncrona

Página aguarda a contagem de 6 segundos para ser renderizada.

## 🛠️ Ferramentas utilizadas para construção do projeto

* **Python** - Linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
* **Django** - Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.
* **Uvicorn** - Servidor ASGI peso leve, construído com uvloop e httptools.

## ✒️ Autor

Guilherme Ferreira Camargo