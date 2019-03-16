#### 常用命令

#### find  `find [PATH] [option] [action]`

-  `find /tmp -name core -type f -print | xargs rm -f` 

	`查找并删除指定的文件，注意：如果文件名中包含换行符、单引号、双引号和空格将不会工作`

-  `find /tmp -name core -type f -print0 | xargs -0 rm -f`
	
	`当文件名或目录中包含换行符、单引号、双引号或者空格的时候可以使用该命令`
 
- 	`find . -type f -exec file '{}' \;`

	`查找当前文件夹下的所有文件并执行 file 命令`

-	`find /  \( -perm -4000 -fprintf /root/suid.txt '%#m %u %p\n' \) ,   \( -size +100M -fprintf /root/big.txt '%-10s %p\n' \)`
	
	`查找用户权限及文件大小分别写入到 /root/suid.txt 和 /root/big.txt 文件中`

-	`find $HOME -mtime 0`
	
	`查找在过去24小时被修改的文件`

-	`find /sbin /usr/sbin -executable \! -readable -print`

	`查找可以执行的但是不可以读文件`

-	`find . -perm 664`

	`搜索文件的读和写权限的所有者和组,但其他用户可以读但不能写。文件符合这些标准,但其他权限位(例如如果有人可以执行文件)将不会匹配`

-	`find . -perm -664`

	`搜索文件的读和写权限的所有者和组,其他用户可以阅读,不考虑任何额外的权限位(例如可执行位)。这将匹配文件模式0777,例如。`

-	`cd /source-dir; find . -name .snapshot -prune -o \( \! -name *~ -print0 \) | cpio -pmd0 /dest-dir`

	`该命令是拷贝 /source-dir 的内容到 /dest-dir中。忽略 文件名或目录为 .snapshot 及 名字 *~ 的文件和目录`
