# kill a process using pkill
exec { 'pkill killmenow':
  path => '/usr/bin',
}
