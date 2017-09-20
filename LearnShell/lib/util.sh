#!/bin/bash
# pemakoa@gmail.com
# 2016-10-21 20:04:50

Echo_Red() {
    echo -e " \e[0;31m$1\e[0m"
}

Echo_Green() {
    echo -e " \e[0;32m$1\e[0m"
}

Echo_Yellow() {
    echo -e " \e[0;33m$1\e[0m"
}


Echo_Blue() {
    echo -e " \e[0;34m$1\e[0m"
}

Echo_Red "this is a demo"
Echo_Green "this is a demo"
Echo_Yellow "this is a demo"
Echo_Blue "this is a demo"
