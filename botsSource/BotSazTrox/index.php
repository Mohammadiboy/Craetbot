<?php
//ارتقا دهنده دیباگ کننده سورس @DevOscar
//اولین چنل اوپن کننده @Virtualservices_3
//بی ناموسی منبع پاک کنی با افتخار به سعید افکونی
ob_start();
$telegram_ip_ranges = [
    ['lower' => '149.154.160.0', 'upper' => '149.154.175.255'], 
    ['lower' => '91.108.4.0',    'upper' => '91.108.7.255'],    
    ];
    $ip_dec = (float) sprintf("%u", ip2long($_SERVER['REMOTE_ADDR']));
    $ok=false;
    foreach ($telegram_ip_ranges as $telegram_ip_range)
    {
        if(!$ok)
        {
            $lower_dec = (float) sprintf("%u", ip2long($telegram_ip_range['lower']));
            $upper_dec = (float) sprintf("%u", ip2long($telegram_ip_range['upper']));
            if($ip_dec >= $lower_dec and $ip_dec <= $upper_dec)
            {
                $ok=true;
                }
            }
        }
    if(!$ok){
        exit(header("location:https://instagram.com/Hosein1383_sh"));
    }
    //ارتقا دهنده دیباگ کننده سورس @DevOscar
//اولین چنل اوپن کننده @Virtualservices_3
//بی ناموسی منبع پاک کنی با افتخار به سعید افکونی
    ?>
