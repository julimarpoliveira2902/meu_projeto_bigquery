# 📊 Visão Geral e Diagnóstico de Perdas - E-commerce TheLook

## 🎯 Por Que Este Projeto Foi Desenvolvido? 
No ecossistema do varejo digital e e-commerce, o indicador de **Faturamento Bruto (Venda Global)** costuma receber a maior parte da atenção. No entanto, focar apenas na receita total pode mascarar gargalos invisíveis que corroem silenciosamente a margem de lucro de uma empresa. 

Este projeto foi desenvolvido para resolver uma dor real de mercado: a **falta de visibilidade sobre o atrito financeiro** (capital perdido com cancelamentos e devoluções) e a **retenção de caixa na esteira logística** (pedidos que passam semanas travados em processamento ou transporte). Sem uma auditoria de dados rigorosa, as empresas tomam decisões com base em dinheiro que nunca chegará, de fato, ao fluxo de caixa.

---

## 💡 Que Tipo de Solução e Insights Este Projeto Oferece?

A solução entrega um ecossistema completo de Engenharia de Dados e Business Intelligence (BI) ponta a ponta. Ela integra uma pipeline de tratamento automatizada em **Python**, armazenamento e modelagem de alta performance em **Google BigQuery** e um dashboard estratégico interativo no **Looker Studio**.

### Principais Insights de Valor Gerados para o Negócio:
1. **Auditoria de Caixa Sem Furos (Data Quality):** Garante um fechamento matemático perfeito (100% de acurácia no centavo), segmentando o capital em Concluído, Em Trânsito e Perdido. Isso evita previsões orçamentárias falsas.
2. **Identificação de "Vazamentos" de Margem:** O painel expõe de forma cirúrgica o *Top 10 de Categorias e Marcas com Maior Atrito Financeiro*. 
3. **Insumo Direto para Ação Estratégica:** Permite que o setor de compras ou de relacionamento com fornecedores identifique instantaneamente quais parceiros comerciais estão gerando custos excessivos com devoluções por problemas de qualidade, fornecendo dados para renegociação de contratos ou descontinuação de produtos.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3 (com bibliotecas de integração de nuvem)
* **Data Warehouse:** Google BigQuery (Google Cloud Platform - GCP)
* **Visualização de Dados:** Looker Studio
* **Ambiente de Desenvolvimento:** VS Code / Google Colab

---

## 📐 Arquitetura do Ecossistema de Dados

1. **Extração & Carga:** Extração de tabelas de pedidos (`order_items`) e cadastro de produtos (`products`) da base pública global *TheLook eCommerce*.
2. **Transformação & Regras de Negócio (Python):** Script automatizado em Python que valida e reconstrói as views no BigQuery, aplicando as regras financeiras e calculando as flags de atrito por item.
3. **Modelagem de Dados:** Cruzamento analítico (`LEFT JOIN`) para mapear comportamento de compra por categorias e fornecedores específicos.
4. **Camada de Consumo:** Conexão direta via conector nativo do BigQuery para alimentação em tempo real do Looker Studio.

---

## 💼 Regras de Negócio e Métricas Implementadas

Para garantir a auditoria de fluxo de caixa da empresa, as vendas globais foram segmentadas em quatro estágios operacionais distintos:

* **Venda Global:** Todo o volume financeiro transacionado no site.
* **Faturamento Concluído:** Receita real e garantida (pedidos com status `Complete`).
* **Faturamento em Trânsito / Processamento:** Capital em carteira dependente de fluxo logístico (status `Shipped` e `Processing`).
* **Vendas Canceladas e Devolvidas (Atrito):** O prejuízo real (pedidos com status `Cancelled` e `Returned`).

---

## 📈 Resultados e Validação Financeira (Auditoria dos Dados)

A validação matemática dos dados no encerramento deste projeto apresentou os seguintes resultados macro:

| Indicador | Status do Pedido | Valor ($ USD) | Impacto (%) |
| :--- | :--- | :--- | :--- |
| **Venda Global** | *Todos* | **$ 10.815.067,83** | 100,0% |
| **Faturamento Concluído** | `Complete` | **$ 2.673.751,47** | 24,7% |
| **Em Trânsito / Proc.** | `Shipped`, `Processing` | **$ 5.445.721,81** | 50,4% |
| **Prejuízo (Atrito Total)** | `Cancelled`, `Returned` | **$ 2.695.594,55** | 24,9% |

> **Equação de Fechamento Auditada:**
> Faturamento Concluído ($2.673.751,47) + Em Trânsito ($5.445.721,81) + Atrito Total ($2.695.594,55) = **Venda Global ($10.815.067,83)**. 
> *A acurácia dos dados fecha em 100% no centavo.*

---

## 🧠 Painel Visual (Looker Studio)

O dashboard foi estruturado em duas páginas principais utilizando um framework de análise macro-para-micro:

### Página 1: Números da Operação e Evolução de Cancelamentos e Devoluções
* Linha de KPIs executivos com os 4 cartões de fluxo financeiro auditados.
* Análise temporal de picos históricos de faturamento e taxas de conversão de pedidos saudáveis.

<p align="center">
  <img src="grafico1.png" alt="Números da Operação e Evolução de Cancelamentos e Devoluções" width="100%">
</p>

### Página 2: Visão Geral e Diagnóstico de Perdas
* **Top 10 Categorias com Maior Atrito Financeiro:** Gráfico de colunas ordenado de forma decrescente pelo prejuízo absoluto, revelando as categorias onde a operação mais queima margem de lucro.
* **Ranking de Atrito por Fornecedor (Marca):** Tabela analítica com paginação detalhando o volume físico (`Itens Cancelados` e `Itens Devolvidos`) cruzado com o `Prejuízo Total ($)` por marca, servindo como ferramenta direta para renegociação de contratos pelo setor de compras.

<p align="center">
  <img src="grafico2.png" alt="Visão Geral e Diagnóstico de Perdas" width="100%">
</p>

---

## 🚀 Como Executar o Script de Atualização

Caso queira replicar ou forçar a atualização da estrutura no BigQuery, execute o script de automação:

```bash
# Certifique-se de ter as credenciais do GCP configuradas no terminal
python atualiza_view_p2.py
