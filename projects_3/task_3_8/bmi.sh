#!/bin/bash

read -r -p "Введите вес тела(г): " weight
read -r -p "Введите ваш рост(см): " height

BMI=$(((weight * 10)/(height ** 2)))

echo "Индекс массы тела: $BMI"
