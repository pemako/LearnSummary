#!/bin/bash

PNAME=idc_crawler
VERSION=0.0.1

rm -rf target
mkdir target

SCRATCH_DIR=$PNAME-$VERSION

cd target
mkdir $SCRATCH_DIR

# 在这里将需要发布的文件，放到scratch目录下
cp -r ../bin ../lib $SCRATCH_DIR

#对发布的文件做一些处理，版本号替换，修改权限等
sed -i -e "s/__BUILD_VERSION__/$VERSION/" $SCRATCH_DIR/bin/idc_crawler.sh
find $SCRATCH_DIR -name '*.sh' -exec chmod +x {} \;
find $SCRATCH_DIR -name '*.py' -exec chmod +x {} \;
chmod +x $SCRATCH_DIR/bin/*

# 添加log目录
mkdir $SCRATCH_DIR/log
mkdir $SCRATCH_DIR/log/hourly

# tar包用于自己打包测试
tar czf $SCRATCH_DIR.tar.gz $SCRATCH_DIR
# rpm包用于线下/线上的标准化部署
fpm -s dir -t rpm -n $PNAME -v $VERSION --rpm-defattrfile=0755 --prefix=/usr/local/mako/prog.d $SCRATCH_DIR

rm -rf $SCRATCH_DIR
