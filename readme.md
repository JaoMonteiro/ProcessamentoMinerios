# PoC de sistema de processamento de minérios 

### Treino Análise de dados 
### Orientador: Marcelo Pio 


**1. DEFINIÇÃO DO SISTEMA** 

O sistema desenvolvido simula um pequeno sistema de gestão de processamento de minérios, onde é possível realizar operações básicas como cadastro de minérios, receber cargas de minérios, processá-los, transformá-los em produtos e também realizar vendas. 

O sistema foi criado em Python com FastAPI, a base de dados em PostgreSql.

**2. REQUISITOS**

**RF01 – Cadastro / edição de minério** 
É possível adicionar um novo minério ou alterar as informações de um já existente 

**RF02 – Visualizar informações dos minérios e sub-produtos** 
É possível escolher um minério ou sub-produto para visualizar suas informações 

**RF03 – Visualizar contagem e valor dos minérios** 
É possível verificar informações gerais do estoque, como total de minérios, valor total do estoque 

**RF04 – Processar minérios** 
É possível processar TODOS os minérios que entram, gerando sub-produtos ou alterando pureza do próprio minério 

**RF05 - Geração de produtos** 
É possível transformar minérios em produtos a serem vendidos 

**RF06 – Realizar vendas** 
É possível remover o estoque de minérios, registrando o que foi vendido e quando 

**RF07 – Visualizar venda** 
É possível visualizar as informações de uma venda separadamente 


**3. ARQUITETURA**

A arquitetura utilizada é de duas camadas, uma vez que não há necessidade de interface gráfica. 

**Módulos do Sistema:** 

Entrada de materiais 
- Cadastro de minério 
- Entrada de minério 
- Edição de informações 
Estoque 
- Visualizar estoque individualmente 
- Visualizar valores totais  
- Descarte de material 
Processar minérios e subprodutos 
- Métodos individuais para processar X minério e gerar Y produtos 
- Gerar novo método 
Vender minérios / produtos 
- Realizar venda 
- Visualizar vendas 
- Visualizar resumo de vendas 


**4. EXECUÇÃO**
Para rodar o sistema, baixar os arquivos, instalar as dependências (FastApi,uvicorn), e na pasta raiz executar o seguinte comando:

__python -m uvicorn main:app --reload__