#debugging web server by correcting syntax of php file
exec { 'change phpp with php':
  path    => '/bin/',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
