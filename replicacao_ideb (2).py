# -*- coding: utf-8 -*-
"""
Artigo: "Efetividade dos gastos públicos em educação e os resultados no Ideb:
 análise do Ensino Médio público" (Revista do TCU, v. 153, 2024)
com a base de dados atualizada até 2025.

Brenda Matsuda e Julia Farias

"""

from pathlib import Path
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

warnings.filterwarnings("ignore")

# =============================================================================
# CONFIGURAÇÃO
# =============================================================================
ARQUIVO_XLSX = Path("Base de dados.xlsx")
PASTA_SAIDA = Path("resultados_replicacao")
ANO_INICIAL = 2005
ANOS_FINAIS = [2017, 2025]      # 2017 = checagem contra o artigo; 2025 = base atualizada
ALPHA = 0.05                    # nível de significância (confiança de 95%)
MOSTRAR_GRAFICOS = False         # False = só salva os PNG, sem abrir janelas

# Nomes das abas da planilha
ABA_NACIONAL = "Nacional"
ABA_ESTADUAL = "Estadual"
ABA_GASTO = "Gasto Educação"

# Investimento médio por aluno do Ensino Médio público (R$ nominais), Gráfico 2 do artigo.
# A planilha NÃO traz esta série. Para estender além de 2017, adicione na aba "Nacional"
# uma coluna D cujo cabeçalho contenha a palavra "aluno" (ex.: "Investimento por aluno (R$)"),
# com os valores de 2019, 2021, 2023 e 2025. Valores da planilha têm prioridade sobre os abaixo.
INVEST_ALUNO_ARTIGO = {
    2005: 954.08, 2007: 1733.12, 2009: 2335.27, 2011: 4112.75,
    2013: 5546.36, 2015: 6636.56, 2017: 7496.13,
}

# Estatísticas reportadas no artigo (só para a checagem da rodada de 2017)
REF_ARTIGO = {
    "nacional": dict(R=0.875, R2=0.766, intercepto=3.143, coef=0.052, F=16.351, p=0.0099),
    "estadual": dict(R=0.472, R2=0.223, intercepto=3.086, coef=0.048, F=7.158, p=0.0130),
}

COR_REAL, COR_META, COR_LINHA = "#001f5b", "#990000", "#2ecc71"


# =============================================================================
# 1. LEITURA E PREPARO DOS DADOS
# =============================================================================
def carregar_nacional():
    df = pd.read_excel(ARQUIVO_XLSX, sheet_name=ABA_NACIONAL)
    cols = list(df.columns)
    base = df.iloc[:, :3].copy()
    base.columns = ["Ano", "Ideb", "Meta"]

    # procura coluna opcional de investimento por aluno
    col_inv = next((c for c in cols[3:] if "aluno" in str(c).lower()), None)
    base["Invest_aluno"] = pd.to_numeric(df[col_inv], errors="coerce") if col_inv else np.nan

    base["Ano"] = pd.to_numeric(base["Ano"], errors="coerce")
    base = base.dropna(subset=["Ano"]).copy()          # descarta linhas de legenda
    base["Ano"] = base["Ano"].astype(int)
    for c in ["Ideb", "Meta"]:
        base[c] = pd.to_numeric(base[c], errors="coerce")

    # completa com os valores do artigo onde a planilha não tem
    base["Invest_aluno"] = base["Invest_aluno"].fillna(base["Ano"].map(INVEST_ALUNO_ARTIGO))
    return base.sort_values("Ano").reset_index(drop=True)


def carregar_estadual():
    df = pd.read_excel(ARQUIVO_XLSX, sheet_name=ABA_ESTADUAL).iloc[:, :4]
    df.columns = ["UF", "Ano", "Nota", "Meta"]
    df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce")
    df = df.dropna(subset=["UF", "Ano"]).copy()
    df["Ano"] = df["Ano"].astype(int)
    df["UF"] = df["UF"].astype(str).str.strip()
    for c in ["Nota", "Meta"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def carregar_gasto():
    df = pd.read_excel(ARQUIVO_XLSX, sheet_name=ABA_GASTO)
    df = df.rename(columns={c: int(c) for c in df.columns if str(c).strip().isdigit()})
    df["Sigla"] = df["Sigla"].astype(str).str.strip()
    anos = [c for c in df.columns if isinstance(c, int)]
    return df.set_index("Sigla")[anos].apply(pd.to_numeric, errors="coerce")


# =============================================================================
# 2. FUNÇÕES ESTATÍSTICAS
# =============================================================================
def regredir(y, x, nome_x):
    """OLS simples; devolve as mesmas tabelas do Excel usadas no artigo (Tabelas 1 e 4)."""
    X = sm.add_constant(x.astype(float))
    res = sm.OLS(y.astype(float), X).fit()
    ic = res.conf_int(ALPHA)
    n = int(res.nobs)

    resumo = pd.DataFrame({
        "Estatística": ["R múltiplo", "R quadrado", "R quadrado ajustado", "Erro padrão", "Observações"],
        "Valor": [np.sqrt(res.rsquared), res.rsquared, res.rsquared_adj, np.sqrt(res.mse_resid), n],
    })
    anova = pd.DataFrame({
        "gl": [1, n - 2, n - 1],
        "SQ": [res.ess, res.ssr, res.ess + res.ssr],
        "MQ": [res.mse_model, res.mse_resid, np.nan],
        "F": [res.fvalue, np.nan, np.nan],
        "F de sig.": [res.f_pvalue, np.nan, np.nan],
    }, index=["Regressão", "Residual", "Total"])
    coef = pd.DataFrame({
        "Coeficientes": res.params.values,
        "Erro padrão": res.bse.values,
        "Stat t": res.tvalues.values,
        "Valor p": res.pvalues.values,
        "95% inf.": ic[0].values,
        "95% sup.": ic[1].values,
    }, index=["Intercepto", nome_x])
    return res, resumo, anova, coef


def imprimir_regressao(titulo, res, resumo, anova, coef, nome_x, ref=None):
    print(f"\n--- {titulo} ---")
    print(resumo.to_string(index=False, float_format=lambda v: f"{v:,.4f}"))
    print("\nANOVA")
    print(anova.to_string(float_format=lambda v: f"{v:,.4f}"))
    print("\nCoeficientes")
    print(coef.to_string(float_format=lambda v: f"{v:,.4f}"))

    b0, b1 = res.params.values
    sig = "estatisticamente significativo" if res.f_pvalue < ALPHA else "NÃO significativo"
    print(f"\nModelo: Ideb = {b0:.3f} + {b1:.3f} x ({nome_x}); R = {np.sqrt(res.rsquared):.3f}; "
          f"R² = {res.rsquared:.3f}; p = {res.f_pvalue:.4f} -> {sig} a {int((1-ALPHA)*100)}%.")
    if ref:
        comp = pd.DataFrame({
            "Artigo": [ref["R"], ref["R2"], ref["intercepto"], ref["coef"], ref["F"], ref["p"]],
            "Replicado": [np.sqrt(res.rsquared), res.rsquared, b0, b1, res.fvalue, res.f_pvalue],
        }, index=["R", "R²", "Intercepto", "Coeficiente", "F", "p-valor"])
        print("\nComparação com o artigo (rodada de validação):")
        print(comp.to_string(float_format=lambda v: f"{v:,.4f}"))


def atingiu_meta(df, col_res, col_meta):
    """Meta atingida = resultado >= meta (mesma regra da marcação verde da Tabela 2)."""
    ok = df[col_res].round(2) >= df[col_meta].round(2)
    return ok.where(df[col_meta].notna() & df[col_res].notna())


# =============================================================================
# 3. GRÁFICOS
# =============================================================================
def _finalizar(fig, nome):
    fig.tight_layout()
    fig.savefig(PASTA_SAIDA / nome, dpi=150)
    if MOSTRAR_GRAFICOS:
        plt.show()
    plt.close(fig)


def grafico_ideb_nacional(nac, ano_final, nome):
    d = nac[nac["Ano"] <= ano_final].copy()
    d["var"] = d["Ideb"].pct_change().fillna(0) * 100
    x = np.arange(len(d)); w = 0.38
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(x - w/2, d["Ideb"], w, color=COR_REAL, label="Resultado")
    ax.bar(x + w/2, d["Meta"], w, color=COR_META, label="Meta")
    for xi, v in zip(x - w/2, d["Ideb"]):
        ax.text(xi, v + 0.05, f"{v:.1f}", ha="center", fontsize=8, color=COR_REAL)
    for xi, v in zip(x + w/2, d["Meta"]):
        if pd.notna(v):
            ax.text(xi, v + 0.05, f"{v:.1f}", ha="center", fontsize=8, color=COR_META)
    ax.set_xticks(x); ax.set_xticklabels(d["Ano"]); ax.set_ylim(0, 5.5)
    ax.set_ylabel("Ideb"); ax.legend(loc="upper left")
    ax2 = ax.twinx()
    ax2.plot(x, d["var"], color=COR_LINHA, marker="o", label="Variação % do resultado")
    ax2.set_ylabel("Variação % do resultado"); ax2.set_ylim(bottom=0)
    ax.set_title(f"Gráfico 1 – Metas e resultados nacionais do Ideb – Ensino Médio público (2005-{ano_final})")
    _finalizar(fig, nome)


def grafico_invest_aluno(nac, ano_final, nome):
    d = nac[(nac["Ano"] <= ano_final) & nac["Invest_aluno"].notna()].copy()
    d["var"] = d["Invest_aluno"].pct_change().fillna(0) * 100
    x = np.arange(len(d))
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.bar(x, d["Invest_aluno"], 0.6, color=COR_REAL)
    for xi, v in zip(x, d["Invest_aluno"]):
        ax.text(xi, v + 80, f"R$ {v:,.0f}", ha="center", fontsize=8, color=COR_REAL)
    ax.set_xticks(x); ax.set_xticklabels(d["Ano"]); ax.set_ylabel("Investimento por aluno (R$ nominais)")
    ax2 = ax.twinx()
    ax2.plot(x, d["var"], color=COR_LINHA, marker="o")
    ax2.set_ylabel("Variação % entre períodos")
    ax.set_title("Gráfico 2 – Investimento por estudante e sua variação entre períodos")
    _finalizar(fig, nome)


def grafico_dispersao(x, y, rotulos, titulo, xlabel, ylabel, nome, anotar=True, cor="#c0392b"):
    b1, b0 = np.polyfit(x, y, 1)
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(x, y, color=cor, zorder=3)
    xs = np.linspace(min(x), max(x), 100)
    ax.plot(xs, b0 + b1 * xs, linestyle=":", color=cor, linewidth=2,
            label=f"Ideb = {b0:.3f} + {b1:.3f}·x")
    if anotar:
        for xi, yi, r in zip(x, y, rotulos):
            ax.annotate(str(r), (xi, yi), textcoords="offset points", xytext=(4, 4), fontsize=8)
    ax.set_title(titulo); ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3); ax.legend()
    _finalizar(fig, nome)


def grafico_pct_metas(pct_ano, titulo, nome):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(pct_ano.index.astype(str), pct_ano.values, color=COR_REAL)
    for i, v in enumerate(pct_ano.values):
        ax.text(i, v + 1, f"{v:.1f}%", ha="center", fontsize=9)
    ax.axhline(pct_ano.mean(), color=COR_META, linestyle="--", label=f"Média: {pct_ano.mean():.2f}%")
    ax.set_ylim(0, 105); ax.set_ylabel("% de UFs que atingiram a meta"); ax.set_title(titulo); ax.legend()
    _finalizar(fig, nome)


# =============================================================================
# 4. ANÁLISES
# =============================================================================
def analise_nacional(nac, ano_final, saida):
    print("\n" + "=" * 78)
    print(f"ANÁLISE NACIONAL (2005-{ano_final})")
    print("=" * 78)
    d = nac[nac["Ano"] <= ano_final].copy()

    # (a) metas atingidas
    d["Atingiu"] = atingiu_meta(d, "Ideb", "Meta")
    com_meta = d.dropna(subset=["Atingiu"])
    pct = com_meta["Atingiu"].astype(float).mean() * 100
    print(f"\nMetas nacionais atingidas: {int(com_meta['Atingiu'].sum())} de {len(com_meta)} "
          f"({pct:.2f}%). Artigo (2007-2017): 50,00%.")
    print(d[["Ano", "Ideb", "Meta", "Atingiu"]].to_string(index=False))

    # (b) regressão Ideb ~ investimento por aluno (R$ mil)
    r = d.dropna(subset=["Ideb", "Invest_aluno"]).copy()
    r["x"] = r["Invest_aluno"] / 1000.0
    if r["Ano"].max() < ano_final:
        print(f"\n[AVISO] Não há investimento por aluno para {sorted(set(d['Ano']) - set(r['Ano']))}. "
              f"A regressão usa só {sorted(r['Ano'])}. Para atualizar, preencha a coluna "
              f"'Investimento por aluno' na aba '{ABA_NACIONAL}'.")
    nome_x = "Investimento por aluno (R$ mil)"
    res, resumo, anova, coef = regredir(r["Ideb"], r["x"], nome_x)
    imprimir_regressao(f"Regressão nacional – {len(r)} observações", res, resumo, anova, coef, nome_x,
                       ref=REF_ARTIGO["nacional"] if ano_final == 2017 else None)

    # gráficos
    grafico_ideb_nacional(nac, ano_final, f"grafico1_ideb_nacional_{ano_final}.png")
    grafico_invest_aluno(nac, ano_final, f"grafico2_invest_aluno_{ano_final}.png")
    grafico_dispersao(r["x"].values, r["Ideb"].values, r["Ano"].values,
                      f"Gráfico 3 – Ideb nacional x investimento por aluno ({r['Ano'].min()}-{r['Ano'].max()})",
                      "Investimento por aluno (em R$ 1.000)", "Ideb do Ensino Médio público",
                      f"grafico3_regressao_nacional_{ano_final}.png")

    # exporta
    saida[f"Nac_{ano_final}_dados"] = d
    saida[f"Nac_{ano_final}_regressao"] = (resumo, anova.reset_index(), coef.reset_index())


def analise_estadual(est, gasto, ano_final, saida):
    print("\n" + "=" * 78)
    print(f"ANÁLISE ESTADUAL (2005-{ano_final})")
    print("=" * 78)
    e = est[(est["Ano"] >= ANO_INICIAL) & (est["Ano"] <= ano_final)].copy()

    # (a) metas atingidas por UF e ano (Tabela 2)
    e["Atingiu"] = atingiu_meta(e, "Nota", "Meta")
    pivot = e.pivot(index="UF", columns="Ano", values="Atingiu")
    pct_ano = (e.dropna(subset=["Atingiu"]).groupby("Ano")["Atingiu"].mean() * 100)
    print("\n% de UFs que atingiram a meta, por ano:")
    print(pct_ano.round(2).to_string())
    print(f"Média de alcance: {pct_ano.mean():.2f}%  (artigo, 2007-2017: 47,53%)")
    ult = e[(e["Ano"] == ano_final) & (e["Atingiu"] == True)]["UF"].tolist()
    print(f"UFs que atingiram a meta em {ano_final}: {ult if ult else 'nenhuma'}")

    # (b) variável explicativa: variação média anual do gasto total (Tabela 3), em R$ 100 milhões
    # Reproduz a coluna "Variação" da Tabela 3: (gasto_final - gasto_inicial) / nº de anos / 1e8
    n_anos = ano_final - ANO_INICIAL
    variacao = (gasto[ano_final] - gasto[ANO_INICIAL]) / n_anos / 1e8
    ideb_medio = e.groupby("UF")["Nota"].mean()          # "Média Res." da Tabela 2

    dados = pd.DataFrame({"Ideb_medio": ideb_medio, "Variacao_gasto": variacao})
    faltando = dados[dados.isna().any(axis=1)]
    if len(faltando):
        print(f"\n[AVISO] UFs excluídas por falta de dados: {faltando.index.tolist()}")
    dados = dados.dropna()

    nome_x = "Variação média do gasto (R$ 100 mi)"
    res, resumo, anova, coef = regredir(dados["Ideb_medio"], dados["Variacao_gasto"], nome_x)
    imprimir_regressao(f"Regressão estadual – {len(dados)} UFs", res, resumo, anova, coef, nome_x,
                       ref=REF_ARTIGO["estadual"] if ano_final == 2017 else None)
    print(f"\nIdeb médio (média das UFs): {dados['Ideb_medio'].mean():.3f} (artigo: 3,191)")

    # gráficos
    grafico_dispersao(dados["Variacao_gasto"].values, dados["Ideb_medio"].values, dados.index,
                      f"Gráfico 4 – Ideb x variação média do gasto em educação (2005-{ano_final})",
                      "Variação média do gasto (em R$ 100.000.000)", "Ideb do Ensino Médio público",
                      f"grafico4_regressao_estadual_{ano_final}.png", cor="#e67e22")
    grafico_pct_metas(pct_ano, f"% de UFs que atingiram a meta do Ideb (até {ano_final})",
                      f"pct_metas_estaduais_{ano_final}.png")

    saida[f"Est_{ano_final}_metas"] = pivot.reset_index()
    saida[f"Est_{ano_final}_pct_metas"] = pct_ano.rename("% atingiu").reset_index()
    saida[f"Est_{ano_final}_dados_reg"] = dados.reset_index()
    saida[f"Est_{ano_final}_regressao"] = (resumo, anova.reset_index(), coef.reset_index())


# =============================================================================
# 5. EXPORTAÇÃO E EXECUÇÃO
# =============================================================================
def exportar_excel(saida):
    caminho = PASTA_SAIDA / "resultados_replicacao.xlsx"
    with pd.ExcelWriter(caminho, engine="openpyxl") as xw:
        for aba, conteudo in saida.items():
            nome = aba[:31]
            if isinstance(conteudo, tuple):          # regressão: empilha as 3 tabelas
                linha = 0
                for tab in conteudo:
                    tab.to_excel(xw, sheet_name=nome, startrow=linha, index=False)
                    linha += len(tab) + 3
            else:
                conteudo.to_excel(xw, sheet_name=nome, index=False)
    print(f"\nTabelas salvas em: {caminho.resolve()}")


def main():
    PASTA_SAIDA.mkdir(exist_ok=True)
    nac, est, gasto = carregar_nacional(), carregar_estadual(), carregar_gasto()

    # checagens básicas
    sem_gasto = set(est["UF"]) - set(gasto.index)
    if sem_gasto:
        print(f"[AVISO] UFs sem gasto na aba '{ABA_GASTO}': {sorted(sem_gasto)}")
    print(f"Base lida: {est['UF'].nunique()} UFs, anos Ideb {sorted(est['Ano'].unique())[0]}-"
          f"{sorted(est['Ano'].unique())[-1]}; gasto {min(gasto.columns)}-{max(gasto.columns)}.")

    saida = {}
    for ano_final in ANOS_FINAIS:
        analise_nacional(nac, ano_final, saida)
        analise_estadual(est, gasto, ano_final, saida)
    exportar_excel(saida)
    print(f"Gráficos (PNG) salvos em: {PASTA_SAIDA.resolve()}")


if __name__ == "__main__":
    main()
