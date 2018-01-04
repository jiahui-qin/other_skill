<html>
<head></head>
<body>
<?php
$con = mysql_connect("localhost", "root","123456")
if (!$con)
    (
        die('数据库链接失败：' .mysql_error());
    )
    else(
        mysql_select_db('world', $con);
        $result = mysql_query("SELECT id, Name FROM city")
        echo
        "<table border = '1'>
        <tr>
        <th>id</th>
        <th>name</th>
        </tr>";
        
        while($row = mysql_fetch_array($result))
        {
            
        }