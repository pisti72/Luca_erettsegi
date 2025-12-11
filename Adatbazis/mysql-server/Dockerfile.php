FROM php:8.2-fpm-alpine

# MariaDB/MySQL PDO driver telepítése
RUN docker-php-ext-install pdo pdo_mysql mysqli

# Munkakönyvtár
WORKDIR /var/www/html

# PHP fájlok másolása
COPY ./php/index.php /var/www/html/

# Port
EXPOSE 9000

CMD ["php-fpm"]
