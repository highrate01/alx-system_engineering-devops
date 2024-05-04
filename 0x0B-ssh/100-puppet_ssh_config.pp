#!/usr/bin/env bash
# using puppet to connect password

file { '/etc/ssh/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

file_line { 'Declare Identity file':
 ensure => present,
 path   => '/etc/ssh/ssh_config',
 line   => 'IdentityFile ~/.ssh/school',
 match  => '^IdentityFile',
}
