#!/usr/bin/env python3
"""Agente Asclepio ⚡ — CLI de Desenvolvimento Autônomo e Solução de Problemas."""

import os
import sys
from pathlib import Path

# Configurações de diretório do produto
ROOT_DIR = Path(__file__).resolve().parent
HERMES_DIR = ROOT_DIR / "hermes-agent"

sys.path.insert(0, str(HERMES_DIR))

# Garante o carregamento dos módulos do engine
os.environ["HERMES_QUIET"] = "1"
os.environ["HERMES_HOME"] = str(Path(os.environ.get("LOCALAPPDATA", "")) / "hermes")

# Executa o CLI do Agente Asclepio
if __name__ == "__main__":
    from cli import main
    import fire
    fire.Fire(main)
