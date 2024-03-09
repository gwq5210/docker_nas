# wifi连接

[TrueNAS Scale with WiFi](https://clint.id.au/?p=2958)

```shell
# 列出pci设备，查看是否有wifi设备
lspci

# 可选，启用apt
sudo chmod +x /bin/apt*
sudo apt update

# 安装firmware-iwlwifi wpasupplicant
sudo apt install firmware-iwlwifi wpasupplicant

# 重启
reboot

# 查找wifi设备接口名
ip a

# 类似
wlp6s0: mtu 1500 qdisc noqueue state DOWN group default qlen 1000

# 生成wifi密码配置
wpa_passphrase WIFI_NAME

network={
    ssid="WIFI_NAME"
    #psk="wifi密码"
    psk=加密后的wifi密码
}

# 将wifi密码配置保存
vim /etc/wpa_supplicant/WIFI_NAME.conf

# truenas界面系统初始化前期添加wifi.sh脚本
bash /usr/local/bin/wifi.sh
```

