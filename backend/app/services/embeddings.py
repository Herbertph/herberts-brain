import requests
from app.core.config import settings


def embed_text(text: str) -> list[float]:
    response = requests.post(
        f"{settings.ollama_url}/api/embeddings",
        json={
            "model": settings.ollama_embed_model,
            "prompt": text,
        },
        timeout=30,
    )

    response.raise_for_status()
    return response.json()["embedding"]
