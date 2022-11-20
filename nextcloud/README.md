安装完毕后，打开/www/wwwroot/file.bugxia.com/config/config.php，在其尾部添加以下代码

```php
  'memcache.local' => '\\OC\\Memcache\\APCu',
  'memcache.distributed' => '\OC\Memcache\Redis',
  'redis' => [
    'host' => 'redis',
    'port' => 6379,
  ],
  'memcache.locking' => '\OC\Memcache\Redis',
  'filelocking.enabled' => 'true',
```


https://github.com/pulsejet/memories/wiki/File-Type-Support
https://github.com/pulsejet/memories/wiki/Configuration#imagevideo-support