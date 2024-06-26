#!/usr/bin/env bash
# using puppet to connect password

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off password auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
}

file_line { 'Declare Identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}
