# ⚡ Agente Asclepio — Modo Autônomo Extremo

O **Agente Asclepio** é um assistente autônomo avançado de engenharia de software, ciência de dados e inteligência artificial, projetado para operar com autonomia máxima (zero interrupções, auto-correção em tempo real e entrega 100% verificada).

O sistema integra o motor do **Hermes Agent** (Nous Research) customizado e otimizado para a **Assinatura Gemini Pro** (Google AI Studio / Google One AI Premium).

---

## 🚀 Filosofia de Operação

1. **Zero Interrupções:** Não para em decisões intermediárias banais; toma decisões técnicas sólidas e avança.
2. **Auto-Correção em Loop:** Detecta erros em tempo de execução, formula hipóteses, edita o código e retesta até a solução definitiva.
3. **Alto Sinal, Zero Filler:** Comunicação direta e objetiva, sem respostas genéricas ou corporatiquês.
4. **Verificação de Ponta a Ponta:** Todo trabalho concluído é entregue com verificação prática e rastreabilidade.

---

## 📂 Estrutura do Projeto

```plaintext
Agente Asclepio/
├── asclepio.py              # Ponto de entrada CLI do Agente Asclepio
├── config.yaml              # Configurações do perfil e modelos (Gemini Pro)
├── iniciar_asclepio.bat     # Launcher Windows rápido
├── SOUL.md                  # Diretrizes fundamentais de identidade do Asclepio
├── .env.example             # Modelo seguro de variáveis de ambiente
├── .gitignore               # Proteção estrita contra vazamento de chaves e caches
└── hermes-agent/            # Engine autônomo customizado (Hermes + Asclepio Branding)
```

---

## ⚙️ Instalação e Configuração

### 1. Clonar o Repositório
```bash
git clone https://github.com/marlonferreira1800-hue/agente-asclepio.git
cd agente-asclepio
```

### 2. Configurar o Ambiente Virtual
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
cd hermes-agent
pip install -e .
cd ..
```

### 4. Configurar as Chaves de API
Copie o arquivo `.env.example` para `.env`:
```bash
copy .env.example .env
```
Edite o arquivo `.env` inserindo sua chave da Google Gemini API (`GOOGLE_API_KEY`) e quaisquer outros provedores desejados.

---

## 💻 Como Executar

### Via Launcher Rápido (.bat)
Dê duplo clique no arquivo `iniciar_asclepio.bat` ou execute no terminal:
```cmd
.\iniciar_asclepio.bat
```

### Via Python CLI Direto
```bash
python asclepio.py
```

Ou execute comandos diretos em modo single-query:
```bash
python asclepio.py chat "Analise este repositório e otimize a estrutura de classes"
```

---

## 👤 Autor & Titularidade
- **Criador:** Marlon Ferreira
- **Repositório:** [marlonferreira1800-hue/agente-asclepio](https://github.com/marlonferreira1800-hue/agente-asclepio)
