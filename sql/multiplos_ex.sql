SELECT categoria, sum(valor) as total_vendas FROM vendas 
GROUP BY categoria ORDER BY total_vendas DESC;

SELECT .c nome, c.cidade, count(p.id) AS total_pedidos
FROM clientes c  
JOIN pedidos p ONc.id = p.cliente_id
GROUP BY c.id, c.nome, c.cidade
HAVING COUNT(P.id) > 2;

SELECT nome, departamento, salario FROM funcionarios
WHERE salario > (SELECT AVG(salario) FROM funcionarios);

select NOME, DEPARTAMENTE, SALARIO from funcionarios
RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) as rank;

WITH CalculoAnterior AS (
    SELECT 
        mes,
        receita,
        LAG(receita) OVER (ORDER BY mes) AS receita_mes_anterior
    FROM vendas_mensais
)
SELECT 
    mes,
    receita,
    receita_mes_anterior,
    ROUND(
        ((receita - receita_mes_anterior) / receita_mes_anterior) * 100, 
        2
    ) AS crescimento_pct
FROM CalculoAnterior;

