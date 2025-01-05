# یادگیری امنیت بوسیله سایت [tryhackme](https://tryhackme.com/)

## [Become a Hacker](https://tryhackme.com/room/becomeahackeroa)

<br>
1. task 2

 Discovered the Hidden Pages Automated with <span style="color:red;">gobuster</span>

 ```bash
 user@thm ~> gobuster dir --url http://www.onlineshop.thm/ -w /usr/share/wordlists/dirbuster/directory-list.txt
 ```
 . <span style="color:yellow;">gobuster</span> is the terminal command to start Gobuster

 . <span style="color:yellow;">dir</span> uses directory and file enumeration mod

 . <span style="color:yellow;">----url http://www.onlineshop.thm/</span> sets the target website

 . <span style="color:yellow;">-w /usr/share/wordlists/dirbuster/directory-list.txt</span>  specifies the word list to

<br>
2. task 3

 Find [admin] Pass Automated (brutforce) with <span style="color:red;">hydra</span>

 ```bash
 user@thm ~> hydra -l admin -P passlist.txt www.onlineshop.thm http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" -V
 ```


 <li><code>hydra</code><span> is the terminal command to start <a class="pL0tzEBB glossary-term" onclick="initPopOver('Hydra', 'pL0tzEBB')">Hydra</a></span></li>
 <li><code>-l admin</code> attempts to log in using the username <code>admin</code></li>
 <li><code>-P passlist.txt</code> specifies the password list to try</li>
 <li><code>www.onlineshop.thm</code> sets the target website</li>
 <li><code>http-post-form</code><span> indicates that this is an <a class="ScR1CbEO glossary-term" onclick="initPopOver('HTTP', 'ScR1CbEO')">HTTP</a> POST request form</span></li>
 <li><code>"/login:username=^USER^&amp;password=^PASS^:F=incorrect"</code><span> specifies the shape of the <a class="kiGWhWg6 glossary-term" onclick="initPopOver('HTTP', 'kiGWhWg6')">HTTP</a> POST request and how to check if the login credentials are incorrect</span></li>
 <li><code>-V</code> is used for verbose output</li>

 