sudo yum install epel-release -y
sudo yum update -y

sudo yum -y install gcc openssl-devel bzip2-devel libffi libffi-devel
sudo rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
sudo yum -y install ffmpeg

sudo yum install -y wget
sudo yum install -y unzip

sudo yum -y install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-linux64.tar.gz
tar xvzf geckodriver-v0.22.0-linux64.tar.gz
chmod +x geckodriver
mv geckodriver /usr/bin/
rm -f geckodriver-v0.22.0-linux64.tar.gz

cd /usr/src
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar xzf Python-3.7.0.tgz
cd Python-3.7.0
./configure --enable-optimizations
make altinstall
rm =f /usr/src/Python-3.7.0.tgz

pip3.7 install --upgrade pip
pip3.7 install youtube-dl
pip3.7 install requests
pip3.7 install numpy
pip3.7 install selenium
pip3.7 install Pillow

firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload

cd ~
wget https://github.com/HalfMAI/AutoYtB/archive/master.zip
unzip master.zip

shutdown -r now
