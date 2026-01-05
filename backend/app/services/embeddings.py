import requests
from typing import List
from app.core.config import settings


class EmbeddingError(Exception):
    """Controled error."""
    pass


def embed_text(text: str) -> List[float]:
    """
    Generate vectorial embedding for the given text using Ollama API.

    Retorna:
        List[float] (768 dimensions for nomic-embed-text)

    Levanta:
        EmbeddingError if something fails during the embedding process.
    """
    url = f"{settings.ollama_url}/api/embeddings"

    payload = {
        "model": settings.ollama_embed_model,
        "prompt": text,
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=15,
        )
    except requests.RequestException as e:
        raise EmbeddingError(f"Ollama connection error: {e}") from e

    if response.status_code != 200:
        raise EmbeddingError(
            f"Ollama error {response.status_code}: {response.text}"
        )

    data = response.json()

    embedding = data.get("embedding")

    if not embedding:
        raise EmbeddingError("No embedding returned by Ollama")

    return embedding
