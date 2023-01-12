#!/bin/bash

# Script para buscar vulnerabilidades no site www.exemplo.com.br

echo "Iniciando a busca por vulnerabilidades no site www.exemplo.com.br..."

# Utilizando o comando nmap para verificar as portas abertas do site: 
nmap -sV www.exemplo.com.br

# Verificando se existem algumas vulnerabilidades conhecidas no site: 
nikto -h www.exemplo.com.br

# Utilizando o comando dirb para buscar arquivos e diretórios escondidos: 
dirb http://www.exemplo.com.br/

 # Utilizando o comando sqlmap para verificar se existem falhas de segurança relacionadas ao banco de dados: 
sqlmap -u http://www.exemplo.com.br/ --dbs

 # Verificando se existem algumas vulnerabilidades desconhecidas no site: 
wpscan --url http://www.exemplo.com.br/ --enumerate vp

 # Verificando se existem falhas de segurança relacionadas ao servidor web do site: 
uniscan -u http://www.exemplo.com.br/ -qweds

 # Verificação de qualquer outras possíveis vulnerabilidades no site:  
nsec3map -d www exemplo com br

 # Caso não encontre nada, exibir uma mensagem informativa na tela:  
if [ $? == 0 ]; then echo "Nenhuma vulnerabilidade foi encontrada."; else echo "Vulnerabilidades foram detectadas."; fi
