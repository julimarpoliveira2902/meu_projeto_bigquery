from google.cloud import bigquery

client = bigquery.Client()
view_id = "curso-ebac-497612.meu_portfolio_thelook.view_diagnostico_perdas"

view_sql = """
SELECT
    oi.status AS status_pedido,
    oi.sale_price AS valor_venda,
    p.category AS categoria_produto,
    p.brand AS marca_produto,
    CASE WHEN oi.status = 'Cancelled' THEN 1 ELSE 0 END AS flag_cancelado,
    CASE WHEN oi.status = 'Returned' THEN 1 ELSE 0 END AS flag_devolvido,
    CASE WHEN oi.status = 'Cancelled' THEN oi.sale_price ELSE 0 END AS valor_cancelado,
    CASE WHEN oi.status = 'Returned' THEN oi.sale_price ELSE 0 END AS valor_devolvido
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS oi
LEFT JOIN `bigquery-public-data.thelook_ecommerce.products` AS p
    ON oi.product_id = p.id
"""

client.delete_table(view_id, not_found_ok=True)
view = bigquery.Table(view_id)
view.view_query = view_sql
view = client.create_table(view)

print("Sucesso: View 'view_diagnostico_perdas' atualizada com cruzamento de produtos!")
