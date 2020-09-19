#!/bin/bash

# 该脚本主要在是为了进行在安装k8s的时候对系统进行一列的初始化操作，第一步设置虚拟机的网络为

_hostname=$1

_init() {
	yum -y update  
	yum install -y vim wget yum-utils device-mapper-persistent-data lvm2 bash-completion
	source /etc/profile.d/bash_completion.sh

	hostnamectl set-hostname ${_hostname}
	_get_sethostname_res=$(hostnamectl status | grep 'Static' | awk -F': ' '{print $2}')
	if [ "${_get_sethostname_res}" == "${_hostname}" ]; then
		printf "\n设置主机名称 %s 完成!\n" "${_hostname}"
		echo "192.168.156.131 ${_hostname}" >> /etc/hosts
	fi

	printf "\n检查防火墙状态"
	_firewall_status=$(firewall-cmd --state)
	if [ "${_firewall_status}" == "not running" ]; then
		printf "\n防火墙未启动\n"        
	elif [ "${_firewall_status}" == "running" ]; then
		systemctl stop firewalld && systemctl disable firewalld
		printf "\n防火墙关闭成功，并禁止开机自启动"
	fi

	printf "\n禁用selinux"
	setenforce 0
	sed -i "s/SELINUX=enforcing/SELINUX=disabled/g" /etc/selinux/config

	printf "\n关闭swap"
	swapoff -a
	yes | cp /etc/fstab /etc/fstab_bak
	cat /etc/fstab_bak |grep -v swap > /etc/fstab
}


_docker() {
	printf "\n设置docker yum 源"
	yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

	printf "\n安装docker-ce"
	yum list docker-ce --showduplicates | sort -r
	yum install -y docker-ce-18.09.6 docker-ce-cli-18.09.6 containerd.io

	printf "\n启动docker 并设置开机自启动"
	systemctl start docker
	systemctl enable docker

	printf "\n设置docker加速器"
	cat <<EOF > /etc/docker/daemon.json
{
	"registry-mirrors": ["https://cxjmzodm.mirror.aliyuncs.com"],
	"exec-opts": ["native.cgroupdriver=systemd]"
}
EOF
	printf "\n重新加载docker"
	systemctl daemon-reload && systemctl restart docker

	
}

_k8s() {
	printf "\n k8s的一些基本设置"
	printf "\n 修改系统内核参数"
	cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
	
	sysctl -p /etc/sysctl.d/k8s.conf

	printf "\n 设置 kubernetes源"
	cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

	yum clean all && yum -y makecache

	printf "\n 安装k8s kubelet,kubectl, kubeadm"
	yum list kubelet --showduplicates | sort -r
	yum install -y kubelet-1.14.2
	yum install -y kubectl-1.14.2
	yum install -y kubeadm-1.14.2

	printf "\n 启动kubelet并设置开机自动动"
	systemctl enable kubelet && systemctl start kubelet

	printf "\n kubelet命令补全"
	echo "source <(kubectl completion bash)" >> ~/.bash_profile
	source ~/.bash_profile

	printf "\n 下载所需镜像文件"
	
	url=registry.cn-hangzhou.aliyuncs.com/google_containers
	version=v1.14.2
	images=(`kubeadm config images list --kubernetes-version=$version|awk -F '/' '{print $2}'`)
	for imagename in ${images[@]} ; do
  		docker pull $url/$imagename
  		docker tag $url/$imagename k8s.gcr.io/$imagename
  		docker rmi -f $url/$imagename
	done
}


main() {
	_init
	_docker
	_k8s
}

main
