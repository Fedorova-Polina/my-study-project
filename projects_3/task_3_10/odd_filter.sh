#!/bin/bash

for i in {1..20}; do
  if [ "$i" -ge 15 ]; then
     break
  elif [ "$(($i % 2))" -eq 0 ]; then
    continue  
  fi

  echo "Подходящие нечетные числа: $i"
done
