<?php
$kg=60;
$m=1.74;
$get=$kg/($m*$m);
if($get<25 and $get >20){
	echo "good";
}else if($get < 20){
	echo "shou";
}else{
	echo "pang";
}
?>