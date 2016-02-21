PWD=$(pwd)
rm -f /etc/init.d/ubuntu_volume
echo "#!/bin/sh" >> /etc/init.d/ubuntu_volume
echo "$PWD/start.sh" >> /etc/init.d/ubuntu_volume
chmod +x /etc/init.d/ubuntu_volume
