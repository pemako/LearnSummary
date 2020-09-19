#!/bin/bash

NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)
SYSOS=$(uname -s)
 
function red() {
    echo -e "$RED$*$NORMAL"
}
 
function green() {
    echo -e "$GREEN$*$NORMAL"
}
 
function yellow() {
    echo -e "$YELLOW$*$NORMAL"
}

function generate {
    FULL=$1
    NAME=$2
    # info_server => InfoServer
    if [ $SYSOS == "Darwin" ]; then
        CAPITAL_FULL=`echo "$FULL" | gsed 's/\b[a-z]/\U&/g'`
    else
        CAPITAL_FULL=`echo "$FULL" | sed 's/\b[a-z]/\U&/g'`
    fi

    arr=(${NAME//_/ })
    for i in ${arr[@]}
    do
        if [ "$SYSOS" == "Darwin" ]; then
            CAPITAL_PART=`echo "$i" | gsed 's/\b[a-z]/\U&/g'`
        else
            CAPITAL_PART=`echo "$i" | sed 's/\b[a-z]/\U&/g'`
        fi
        CAPITAL_NAME=$CAPITAL_NAME$CAPITAL_PART
    done

    git clone https://github.com/pemako/pygenerator.git tmp
    # coding
    # git clone https://git.coding.net/pemako/pygenerator.git tmp
    USER_PROJ_DRI=$NAME

    cp -r tmp/templates/$FULL/ $USER_PROJ_DRI

    cd $USER_PROJ_DRI

    if [ $SYSOS == "Darwin" ]; then
        echo 'starting....'
        find . -type f | xargs gsed -i "s/$FULL/$NAME/g"
        find . -type f | xargs gsed -i "s/$CAPITAL_FULL/$CAPITAL_NAME/g"
        find . -name "$FULL*" -type f | xargs rename "s/$FULL/$NAME/"
    else
        find . -type f | xargs sed -i "s/$FULL/$NAME/g"
        find . -type f | xargs sed -i "s/$CAPITAL_FULL/$CAPITAL_NAME/g"
        find . -name "$FULL*" -type f | xargs rename "$FULL" "$NAME"
    fi
    
    cd ..
    rm -rf tmp
}

red 'Pemako Python Project Generator\n'

echo 'supported project template:'
green "Simple" 
echo "Simple is quite simple python project with main framework and some logging, config loading."

green "Multithread"
echo "Multithread is also a simple service model using threading, with those logging and config thing."

green "Multithread with task queue"
echo "Multithread with task queue is a little bit complicated service model. Module 'Queue' is used as a task queue. Main thread plays the role of PRODUCER while worker threads being CONSUMER."

green "Multiprocess"
echo "Multiprocess is a service model using multiprocessing, helping you deal with logging, data share, and other problem that you will encounter without dmpy."

green "Multiprocess with Thrift"
echo "Multiprocess with Thrift is a multiprocessing service model using TProcessPoolServer."

yellow "\nWhich Python serivce model do you want, s(simple) or mt(multithread) or mtq(multithread queue) or mp(multiprocess) or mpt(multiprocess thrift):"
read TYPE
case "$TYPE" in
    s)
        FULL=simple
        ;;
    mt)
        FULL=multi_t
        ;;
    mtq)
        FULL=multi_t_q
        ;;
    mp)
        FULL=multi_p
        ;;
    mpt)
        FULL=multi_p_t
        ;;
    *)
        echo "Sorry, only 's' and 'm' are supported now."
        exit 1
esac

yellow "What name do you like for your new project:"
read NAME

generate $FULL $NAME

exit 0
