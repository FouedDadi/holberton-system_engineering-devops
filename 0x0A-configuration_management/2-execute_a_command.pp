# kill a process using pkill
exec { 'pkill killmenow':
  provider => 'shell',
}
