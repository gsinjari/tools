# author      : @g0vandS, Govand Sinjari
# license           : MIT

<?php
// Anti-Crawler v1.0
// By Govand Sinjari
// 2013-09-13
// apt-get install php5-sqlite
// service apache2 restart
$db = new SQLite3('dictionary.db');
//$randx2 = rand(1,80368);
$randx2 = rand(1,10000);
$result2 = "SELECT word FROM dict WHERE id=".$randx2."";
$rr2 = $db->querySingle($result2)." ";
?>

<a style="color: rgb(51, 102, 255);" href="../index.php">Home</a><br>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<meta name="Author" content="Govand Sinjari">
<meta name="Description" content="This is an experimental page to test behavior of different search engine crawler">
<title>govand.info -&gt; Anti crawler <?php echo $_GET['idx']."-".$rr2; ?></title>

<style type="text/css">

body {
background-color: #000000;
font-weight: normal;
font-style: normal;
text-align: left;
font-size: medium;
line-height: normal;
color: #000000; <!-- #33cc00 -->
font-family: Courier New;
}
a:link {
color: #000000; <!-- #009933 -->
text-decoration: underline;
}
a:visited {
color: #000000;
text-decoration: underline;
}
a:hover {
color: #000000;
font-weight: bold;
text-decoration: underline blink;
}
a:active {
color: #000000;
}
.xxc {
color: #009933; 
}
.xxc a:link {
color: #009933; 
}
.xxc a:visited {
color: #009933; 
}
.xxc a:active {
color: #009933; 
}

</style>

</head><body>

<font class = "xxc">

<h1>This is an experimental page to test behavior of different search engine crawlers</h1>


<?php 
$b = 100000;
$a = (int) $_GET['idx'];
echo "Max I can go now is = ". $b."<br>";

if ($a == 0) $a = 70;

echo $a."  :  ";
if ($a < $b ) {
 $a++;
 }
 
//
?>

<a color="#009933" href="index.php?idx=<?php echo $a."&".$rr2."=".$a;?>">  This is a new link nr. <?php echo $a."=".$rr2;?></a><br>


<?php 
echo "<br>";
echo "Now: ".date('Y-m-d')." ".time()."<br>";


// creating random dictionary text

echo "<br><b>Creating random text from dictionary</b><br><br></font>";

//unlink('dictionary.db'); // to delete existing db

//$db = new SQLite3('dictionary.db');

/* This is used only first time, to create the table and enter words from txt file

$db->exec('CREATE TABLE dict (id INTEGER, word STRING)');

$myFile = "dictionary_full.txt"; 
$f=fopen($myFile,'rb'); 
$x = 1;
while(!feof($f)) {
    $dic=fgets($f);
    $run = "INSERT INTO dict (id, word) VALUES (".$x.",'".$dic."')";
    $db->exec($run);
    $x++;
    }
fclose($f);
*/

$maxtextwords = 500;
$dicmax = 10000; //total number of words in dictionary

for ($z=1;$z<$maxtextwords; $z++) {

$randx = rand(1,$dicmax);
$randhex = dechex($randx);
$result = "SELECT word FROM dict WHERE id=".$randx."";
$rr = $db->querySingle($result)." ";

echo "<font color=#".$randhex.">";

echo $rr."</font>";

}

// show iframe

$urlb = "https://en.wikipedia.org/wiki/".$rr2;
?>

<br><br><br>
<font class="xxc">
<a href="<?php echo $urlb;?>"><?php echo $urlb;?></a>
</font>
<br><br><br>

<div style="background-color:black;color:black;">

<?php
$homepage = file_get_contents($urlb);
echo $homepage;
?>

</div>
</body></html>
