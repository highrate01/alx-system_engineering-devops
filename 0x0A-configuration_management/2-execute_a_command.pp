# create a manifest that kills a process named killmenow

exec {'pkill killnow':
path => '/usr/bin:/usr/sbin:/bin',
}

