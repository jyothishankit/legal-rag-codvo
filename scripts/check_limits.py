"""Print the OpenAI rate limits this account currently gets.

The values feed the embed_rpm / embed_tpm / llm_rpm / llm_tpm settings. Tier
upgrades change them, and running with stale numbers either wastes throughput or
triggers 429s.
"""

from __future__ import annotations

import sys

from legalrag.config import get_settings


def main() -> None:
    from openai import OpenAI

    settings = get_settings()
    client = OpenAI(api_key=settings.openai_api_key.get_secret_value())

    embedding = client.embeddings.with_raw_response.create(
        model=settings.embedding_model, input=["rate limit probe"], dimensions=256
    )
    chat = client.chat.completions.with_raw_response.create(
        model=settings.llm_model,
        messages=[{"role": "user", "content": "ping"}],
        max_completion_tokens=1,
    )

    for label, response in (("embeddings", embedding), ("chat", chat)):
        print(f"\n{label}:")
        for key, value in response.headers.items():
            if key.lower().startswith("x-ratelimit"):
                print(f"  {key[12:]:<22} {value}")

    print(
        "\nA reset-requests value far above 60s means a per-day request cap, "
        "not a per-minute one."
    )


if __name__ == "__main__":
    sys.exit(main())
