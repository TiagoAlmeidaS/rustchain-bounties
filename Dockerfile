FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && curl -sSL https://raw.githubusercontent.com/scottcjn/rustchain/main/rustchain_universal_miner.py -o rustchain_universal_miner.py \
    && apt-get purge -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV WALLET=""
ENV NODE_URL="https://node.rustchain.io"

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD ps aux | grep -q "[r]ustchain_universal_miner.py" || exit 1

CMD ["python", "rustchain_universal_miner.py"]
