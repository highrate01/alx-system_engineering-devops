# set new server with nginx

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

file_line { 'redirect_me':
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after  => 'server_name _;',
  notify => Service['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
