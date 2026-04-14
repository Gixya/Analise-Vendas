import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados/vendas.csv')

# Criar faturamento
df['Faturamento'] = df['Valor'] * df['Quantidade']

# 💰 Total
total = df['Faturamento'].sum()
print("Total de faturamento:", total)

# 🏆 Produto mais vendido
produto = df.groupby('Produto')['Quantidade'].sum().idxmax()
print("Produto mais vendido:", produto)

# 📊 Categoria
faturamento_categoria = df.groupby('Categoria')['Faturamento'].sum()
print("\nFaturamento por categoria:")
print(faturamento_categoria)

# 📊 GRÁFICO
faturamento_categoria.plot(kind='bar')

plt.title('Faturamento por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Faturamento')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
