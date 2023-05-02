# Installs Nginx server and add custom header

exec {'update':
	provider => shell,
	command  => 'sudo apt-get -y update',
	before   => Exec['install nginx'],

}

exec {'install nginx':
	provider => shell,
	command  => 'sudo apt-get -y install nginx',
	before   => Exec['add_header'],

}

exec {'add_header':
	provider     => shell,
	environment  => ["HOST=${HOSTNAME}"],
	command      => 'echo "add_header X-Served-By $hostname;" | sudo tee -a /etc/nginx/nginx.conf > /dev/null',

}

exec {'restart nginx':
	provider  => shell,
	command   => 'sudo service nginx restart',

}
