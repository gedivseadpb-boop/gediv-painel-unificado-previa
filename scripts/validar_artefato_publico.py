"""Validador fail-closed do artefato público antes do deploy no GitHub Pages."""
from __future__ import annotations

import json
import re
from pathlib import Path

PASTA = Path(__file__).resolve().parent.parent / "public"
PERMITIDOS = {".nojekyll", "dados-sinteticos-publicos.json", "index.html"}


def main() -> None:
    arquivos = sorted(p.relative_to(PASTA).as_posix() for p in PASTA.rglob("*") if p.is_file())
    assert set(arquivos) == PERMITIDOS, f"Arquivos não autorizados em public/: {arquivos}"

    html = (PASTA / "index.html").read_text(encoding="utf-8")
    dados_txt = (PASTA / "dados-sinteticos-publicos.json").read_text(encoding="utf-8")
    dados = json.loads(dados_txt)

    for nome, txt in (("index.html", html), ("dados-sinteticos-publicos.json", dados_txt)):
        assert not re.search(r"SAD-PSE-202\d/\d+", txt), f"Processo não sintético (202x) em {nome}"
        assert not re.search(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b", txt), f"CPF encontrado em {nome}"
        assert not re.search(r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|PreviaGediv2026!|previa\.gediv)", txt), f"Credencial encontrada em {nome}"
        assert not re.search(r"C:[\\/]+Users[\\/]+", txt, re.I), f"Caminho local encontrado em {nome}"

    assert not re.search(r"/api/pdf/", dados_txt), "Referência /api/pdf/ encontrada no JSON público"
    assert dados["backend"]["autenticado"] is False
    assert dados["backend"]["ehAdmin"] is False
    assert dados["backend"]["modoDemonstracaoEstatica"] is True
    assert len(dados["rows"]) > 0
    for r in dados["rows"]:
        assert str(r.get("process") or "").startswith("SAD-PSE-2099/"), f"Processo fora da faixa 2099: {r.get('process')}"
        assert str(r.get("registration") or "").startswith("950."), f"Matrícula fora da faixa 950: {r.get('registration')}"
        assert "FICTICIO" in str(r.get("server") or "").upper(), f"Servidor não fictício: {r.get('server')}"

    assert html.count("\r\n") == 0, "CRLF detectado em public/index.html"
    assert "./dados-sinteticos-publicos.json" in html
    assert "openStaticBackendNotice" in html
    print(f"OK: artefato público validado ({len(arquivos)} arquivos autorizados, {len(dados['rows'])} registros 100% sintéticos).")


if __name__ == "__main__":
    main()
