# 1. Exibir uma mensagem na tela
print("Olá, Mundo!")

# 2. Realizar um cálculo básico (soma de dois números)
a <- 10
b <- 5
soma <- a + b
print(paste("A soma de", a, "e", b, "é:", soma))

# 3. Criar uma função que calcula a área de um retângulo
calcular_area <- function(largura, altura) {
  area <- largura * altura
  return(area)
}

# Usando a função com valores de exemplo
largura <- 4
altura <- 6
area_total <- calcular_area(largura, altura)
print(paste("A área do retângulo é:", area_total))
