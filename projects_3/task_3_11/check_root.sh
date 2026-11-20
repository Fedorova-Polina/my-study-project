#!/bin/bash

check_root() {
    if [ "$EUID" -eq 0 ]; then
    return 0
    else
    echo "Внимание! Произошла ошибка.Данный скрипт записан не от имени суперпользователя."
    exit 1

fi
}

check_root

