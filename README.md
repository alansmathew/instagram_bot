# Instagram_bot:
  Python project based on Selenium automation, which helps to see all following people who havent followed yet and much more.
 
# Step to Run:
  <B>1) Install selenium</b>
      <br><br>&nbsp;&nbsp;&nbsp;window users: <pre>pip install selenium</pre>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;osX users:  <pre>brew install selenium or pip install selenium </pre>
  <b>2) Download browser software</b>
      <br>Note: i used chrome and its already included in this repo ( depends on version of ur browser )
      <pre>https://chromedriver.chromium.org </pre>
  <b>3) Run using python </b>
      <br><pre>python instafollowing.py </pre>
# Note :
  All the class names usered in the project can get changed !. So if any error occures try identifying those class using inspect element and change it accordingly. 
# Findings:
<ul style="circle">
  <li> I tried firefox but it showed up some error. </li>
  <pre> RuntimeError: maximum recursion depth exceeded | <b> because of low internet speed or failed to load </b></pre>          
  <pre>NoSuchElementException: Message: no such element: Unable to locate element | <b> change time.sleep( to a higher value )</b></pre>
  <pre>selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable may have wrong permissions.<br>if using Mac go to <b>System preference -> Security & Privacy -> Allow application </b></pre>
  </ul>
  
