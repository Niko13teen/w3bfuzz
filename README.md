<div align="center"> <h1> w3bfuzz </h1></div>
<h2> Asynchronous web application fuzzer to detect open/hidden directories. Logging, autotesting is connected, a wordlist from ChatGPT is used (default). In order to use another wordlist, specify the option for raw </h2>
<h3> Other wordlists: </h3>
<pre><code> https://raw.githubusercontent.com/six2dez/OneListForAll/main/onelistforallmicro.txt (25611 lines) </code>
<code> https://raw.githubusercontent.com/maverickNerd/wordlists/master/cvePaths.txt (7549 lines) </code> 
<code> https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/api/api-endpoints.txt (268 lines) </code></pre>
<div align="center"> <img src="https://media2.giphy.com/media/H6E7CjSrSVWhgEV7E8/giphy.gif?cid=ecf05e478pm9qylq0bjnj9002lkilqx1yb032v8x58tik2nx&rid=giphy.gif&ct=s"></div>
<div>
<div>
  <h3>
<pre><code> pip3 install -r requirements.txt </code>
<code> python3 w3bfuzz.py --target https://example.site --wordlist https://raw.githubusercontent.com/maverickNerd/wordlists/master/cvePaths.txt </code></pre>
  </h3>
</div>
