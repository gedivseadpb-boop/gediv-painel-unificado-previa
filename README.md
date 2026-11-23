# Prévia Pública Estática — Painel Unificado do Observatório GEDIV

Repositório dedicado exclusivamente à **demonstração pública gratuita no GitHub Pages** do Painel Unificado do Observatório GEDIV (**Delicadeza Visual**), alimentada por **dados 100% sintéticos e descartáveis**.

- **Endereço da prévia:** https://gedivseadpb-boop.github.io/gediv-painel-unificado-previa/
- **Repositório principal (código completo com backend Python/SQLite):** https://github.com/gedivseadpb-boop/Observat-rio-GEDIV-CLAUDE

## Garantias de Privacidade e Escopo

- **Dados exclusivamente sintéticos:** processos fictícios `SAD-PSE-2099/*`, matrículas fictícias `950.xxx-x` e nomes `SERVIDOR FICTICIO ...`. Nenhum dado real de servidor, CPF, senha, token ou banco SQLite está presente neste repositório.
- **Somente leitura (sem backend):** todas as 7 abas, cartões, gráficos, calendário, filtros, tabela ampliada e exportações client-side funcionam sem rotas `/api/*`.
- **Funções gerenciais desabilitadas honestamente:** login gerencial real, conferência documental, conflitos (D2), auditoria (D3) e alterações de registros exigem servidor backend e permanecem desabilitadas (sem senha simulada em JavaScript).
- **Validação automática antes do deploy:** o workflow `.github/workflows/publicar-pages.yml` executa `scripts/validar_artefato_publico.py` em modo fail-closed antes de enviar qualquer artefato ao GitHub Pages.
