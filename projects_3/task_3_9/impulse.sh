#!/bin/bash

gene_name="$1"
expression_level="$2"

if [[ -n "$gene_name" && -n "$expression_level" ]]; then
  echo "Экспрессия гена $gene_name составляет $expression_level единиц"
else 
  echo "Недостаточно входящих данных"

fi

