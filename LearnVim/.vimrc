" 目前自己机器上使用的配置，后面有需要在逐个增加设置
" 2017/09/20 21:42:57

" 通过bundle 管理vim插件
set nocompatible
filetype off
" set the runtime path to include Vundle and inititalize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdTree'
call vundle#end()
" 配置结束

filetype on "开启文件类型检查
set number
syntax on

set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

colorscheme desert
