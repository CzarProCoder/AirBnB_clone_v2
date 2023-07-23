<h1>0x04. AirBnB clone - Web framework</h1>
<div>
    <div>PythonBack-endWebserverFlask</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume, CTO at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;2</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jul 20, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 24, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jul 21, 2023 6:00 AM</span></li>
        <li>&nbsp;<strong>Manual QA review must be done</strong> (request it when you are done with the project)</li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at this concept:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/74">AirBnB clone</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/64SQpOGx46Ljp0zFJchESg" title="What is a Web Framework?" target="_blank">What is a Web Framework?</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/LM0zyaIOfusNXz12bZXKVQ" title="A Minimal Application" target="_blank">A Minimal Application</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/PBYpb5Giu7U5uOb-A9PMxw" title="Routing" target="_blank">Routing</a> (<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/g-W9H6gxHkNqaTw6giSG8Q" title="Rendering Templates" target="_blank">Rendering Templates</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ" title="Synopsis" target="_blank">Synopsis</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/ITzobwYP1Lc4KqEUUcYCGw" title="Variables" target="_blank">Variables</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/ykUFuQSE9KD1M7WGY-4v4w" title="Comments" target="_blank">Comments</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/NMLZom50ZVOxQlgYW3rnuQ" title="Whitespace Control" target="_blank">Whitespace Control</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/5AGhzIt0zSpPJh9SFysdMQ" title="List of Control Structures" target="_blank">List of Control Structures</a> (<em>read up to &ldquo;Call&rdquo;</em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/VJs151_hsE9g7Cw-Pz5bVg" title="Flask" target="_blank">Flask</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ" title="Jinja" target="_blank">Jinja</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/fja4_zmJuVaRtHFviyVv9Q" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>What is a Web Framework</li>
            <li>How to build a web framework with Flask</li>
            <li>How to define routes in Flask</li>
            <li>What is a route</li>
            <li>How to handle variables in a route</li>
            <li>What is a template</li>
            <li>How to create a HTML response in Flask by using a template</li>
            <li>How to create a dynamic template (loops, conditions&hellip;)</li>
            <li>How to display in HTML data from a MySQL database</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
        </ul>
        <h2>Requirements</h2>
        <h3>Python Scripts</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using&nbsp;<code>python3</code> (version 3.4.3)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the&nbsp;<code>PEP 8</code> style (version 1.7)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
            <li>All your modules should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
        </ul>
        <h3>HTML/CSS Files</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files should end with a new line</li>
            <li>A&nbsp;<code>README.md</code> file at the root of the folder of the project is mandatory</li>
            <li>Your code should be W3C compliant and validate with&nbsp;<a href="https://intranet.alxswe.com/rltoken/_bfSTiq2t4otmyPespKhEg" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
            <li>All your CSS files should be in the&nbsp;<code>styles</code> folder</li>
            <li>All your images should be in the&nbsp;<code>images</code> folder</li>
            <li>You are not allowed to use&nbsp;<code>!important</code> or&nbsp;<code>id</code> (<code>#...</code> in the CSS file)</li>
            <li>All tags must be in uppercase</li>
            <li>Current screenshots have been done on&nbsp;<code>Chrome 56.0.2924.87</code>.</li>
            <li>No cross browsers</li>
        </ul>
        <h2>More Info</h2>
        <h3>Install Flask</h3>
        <pre><code>$ pip3 install Flask
</code></pre>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png" alt=""></p>
        <h3>Manual QA Review</h3>
        <p><strong>It is your responsibility to request a review for this project from a peer before the project&rsquo;s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>
    </div>
</div>
<div>
    <div>
        <div>
            <div>
                <h3>Video library<small>(1&nbsp;total)</small></h3>
            </div>
            <div>
                <div>
                    <div><input placeholder="Search by title" type="search" value=""></div>
                </div>
            </div>
            <div>
                <div><span title="">
                        <div>
                            <div>
                                <div><br></div>
                            </div>
                            <div>Python: Flask the web framework</div>
                        </div>
                    </span></div>
            </div>
        </div>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Hello Flask!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo &quot;&quot; | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>0-hello_route.py, __init__.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. HBNB</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo &quot;&quot; | cat -e
HBNB$
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>1-hbnb_route.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. C is fun!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                        <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)</li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo &quot;&quot; | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo &quot;&quot; | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>2-c_route.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Python is cool!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                        <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)</li>
                        <li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)<ul>
                                <li>The default value of&nbsp;<code>text</code> is &ldquo;is cool&rdquo;</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo &quot;&quot; | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo &quot;&quot; | cat -e
Python is cool$
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>3-python_route.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. Is it a number?</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                        <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)</li>
                        <li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)<ul>
                                <li>The default value of&nbsp;<code>text</code> is &ldquo;is cool&rdquo;</li>
                            </ul>
                        </li>
                        <li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo;&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer</li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo &quot;&quot; | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>4-number_route.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. Number template</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                        <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)</li>
                        <li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)<ul>
                                <li>The default value of&nbsp;<code>text</code> is &ldquo;is cool&rdquo;</li>
                            </ul>
                        </li>
                        <li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo;&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer</li>
                        <li><code>/number_template/&lt;n&gt;</code>: display a HTML page&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer:<ul>
                                <li><code>H1</code> tag: &ldquo;Number:&nbsp;<code>n</code>&rdquo; inside the tag&nbsp;<code>BODY</code></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>5-number_template.py, templates/5-number.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. Odd or even?</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>Routes:<ul>
                        <li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
                        <li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
                        <li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)</li>
                        <li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the&nbsp;<code>text</code> variable (replace underscore&nbsp;<code>_</code> symbols with a space&nbsp;)<ul>
                                <li>The default value of&nbsp;<code>text</code> is &ldquo;is cool&rdquo;</li>
                            </ul>
                        </li>
                        <li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo;&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer</li>
                        <li><code>/number_template/&lt;n&gt;</code>: display a HTML page&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer:<ul>
                                <li><code>H1</code> tag: &ldquo;Number:&nbsp;<code>n</code>&rdquo; inside the tag&nbsp;<code>BODY</code></li>
                            </ul>
                        </li>
                        <li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page&nbsp;<strong>only</strong> if&nbsp;<code>n</code> is an integer:<ul>
                                <li><code>H1</code> tag: &ldquo;Number:&nbsp;<code>n</code> is&nbsp;<code>even|odd</code>&rdquo; inside the tag&nbsp;<code>BODY</code></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89 is odd&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 32 is even&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>Directory:&nbsp;<code>web_flask</code></li>
                    <li>File:&nbsp;<code>6-number_odd_or_even.py, templates/6-number_odd_or_even.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. Improve engines</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>
            <p>Update&nbsp;<code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>
            <ul>
                <li>Add a public method&nbsp;<code>def close(self):</code>: call&nbsp;<code>reload()</code> method for deserializing the JSON file to objects</li>
            </ul>
            <p>Update&nbsp;<code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>
            <ul>
                <li>Add a public method&nbsp;<code>def close(self):</code>: call&nbsp;<code>remove()</code> method on the private session attribute (<code>self.__session</code>)&nbsp;<a href="https://intranet.alxswe.com/rltoken/_lTxhB5UgQ4nFRoS9ooI5g" title="tips" target="_blank">tips</a> or&nbsp;<code>close()</code> on the class&nbsp;<code>Session</code> <a href="https://intranet.alxswe.com/rltoken/xlPf9pDUFMb599rkoDElvg" title="tips" target="_blank">tips</a></li>
            </ul>
            <p>Update&nbsp;<code>State</code>: (<code>models/state.py</code>) - If it&rsquo;s not already present</p>
            <ul>
                <li>If your storage engine is not&nbsp;<code>DBStorage</code>, add a public getter method&nbsp;<code>cities</code> to return the list of&nbsp;<code>City</code> objects from&nbsp;<code>storage</code> linked to the current&nbsp;<code>State</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
&gt;&gt;&gt; from models import storage
&gt;&gt;&gt; from models.state import State
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # Time to insert new data!
</code></pre>
            <p>At this moment, in another tab:</p>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ echo &apos;INSERT INTO `states` VALUES (&quot;421a55f1-7d82-45d9-b54c-a76916479545&quot;,&quot;2017-03-25 19:42:40&quot;,&quot;2017-03-25 19:42:40&quot;,&quot;Alabama&quot;);&apos; | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>
            <p>And let&rsquo;s go back the Python console:</p>
            <pre><code>&gt;&gt;&gt; # Time to insert new data!
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # normal: the SQLAlchemy didn&apos;t reload his `Session`
&gt;&gt;&gt; # to force it, you must remove the current session to create a new one:
&gt;&gt;&gt; storage.close()
&gt;&gt;&gt; len(storage.all(State))
6
&gt;&gt;&gt; # perfect!
</code></pre>
            <p>And for the getter&nbsp;<code>cities</code> in the&nbsp;<code>State</code> model:</p>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
&quot;&quot;&quot;
 Test cities access from a state
&quot;&quot;&quot;
from models import storage
from models.state import State
from models.city import City

&quot;&quot;&quot;
 Objects creations
&quot;&quot;&quot;
state_1 = State(name=&quot;California&quot;)
print(&quot;New state: {}&quot;.format(state_1))
state_1.save()
state_2 = State(name=&quot;Arizona&quot;)
print(&quot;New state: {}&quot;.format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name=&quot;Napa&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name=&quot;Sonoma&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name=&quot;Page&quot;)
print(&quot;New city: {} in the state: {}&quot;.format(city_2_1, state_2))
city_2_1.save()


&quot;&quot;&quot;
 Verification
&quot;&quot;&quot;
print(&quot;&quot;)
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print(&quot;Find the city {} in the state {}&quot;.format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&apos;name&apos;: &apos;California&apos;, &apos;id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&apos;name&apos;: &apos;Arizona&apos;, &apos;id&apos;: &apos;a5e5311a-3c19-4995-9485-32c74411b416&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {&apos;name&apos;: &apos;Napa&apos;, &apos;id&apos;: &apos;e3e36ded-fe56-44f5-bf08-8a27e2b30672&apos;, &apos;state_id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&apos;name&apos;: &apos;California&apos;, &apos;id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {&apos;name&apos;: &apos;Sonoma&apos;, &apos;id&apos;: &apos;12a58d70-e255-4c1e-8a68-7d5fb924d2d2&apos;, &apos;state_id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&apos;name&apos;: &apos;California&apos;, &apos;id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {&apos;name&apos;: &apos;Page&apos;, &apos;id&apos;: &apos;a693bdb9-e0ca-4521-adfd-e1a93c093b4b&apos;, &apos;state_id&apos;: &apos;a5e5311a-3c19-4995-9485-32c74411b416&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&apos;name&apos;: &apos;Arizona&apos;, &apos;id&apos;: &apos;a5e5311a-3c19-4995-9485-32c74411b416&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {&apos;name&apos;: &apos;Napa&apos;, &apos;id&apos;: &apos;e3e36ded-fe56-44f5-bf08-8a27e2b30672&apos;, &apos;state_id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&apos;name&apos;: &apos;California&apos;, &apos;id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {&apos;name&apos;: &apos;Sonoma&apos;, &apos;id&apos;: &apos;12a58d70-e255-4c1e-8a68-7d5fb924d2d2&apos;, &apos;state_id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {&apos;name&apos;: &apos;California&apos;, &apos;id&apos;: &apos;5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {&apos;name&apos;: &apos;Page&apos;, &apos;id&apos;: &apos;a693bdb9-e0ca-4521-adfd-e1a93c093b4b&apos;, &apos;state_id&apos;: &apos;a5e5311a-3c19-4995-9485-32c74411b416&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {&apos;name&apos;: &apos;Arizona&apos;, &apos;id&apos;: &apos;a5e5311a-3c19-4995-9485-32c74411b416&apos;, &apos;updated_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), &apos;created_at&apos;: datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>models/engine/file_storage.py, models/engine/db_storage.py, models/state.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. List of states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>You must use&nbsp;<code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or&nbsp;<code>DBStorage</code>) =&gt;&nbsp;<code>from models import storage</code> and&nbsp;<code>storage.all(...)</code></li>
                <li>After each request you must remove the current SQLAlchemy Session:<ul>
                        <li>Declare a method to handle&nbsp;<code>@app.teardown_appcontext</code></li>
                        <li>Call in this method&nbsp;<code>storage.close()</code></li>
                    </ul>
                </li>
                <li>Routes:<ul>
                        <li><code>/states_list</code>: display a HTML page: (inside the tag&nbsp;<code>BODY</code>)<ul>
                                <li><code>H1</code> tag: &ldquo;States&rdquo;</li>
                                <li><code>UL</code> tag: with the list of all&nbsp;<code>State</code> objects present in&nbsp;<code>DBStorage</code> <strong>sorted by&nbsp;<code>name</code></strong> (A-&gt;Z)&nbsp;<a href="https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>
                                    <ul>
                                        <li><code>LI</code> tag: description of one&nbsp;<code>State</code>:&nbsp;<code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>Import this&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <p><strong>IMPORTANT</strong></p>
            <ul>
                <li>Make sure you have a running and valid&nbsp;<code>setup_mysql_dev.sql</code> in your&nbsp;<code>AirBnB_clone_v2</code> repository (<a href="https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
                <li>Make sure all tables are created when you run&nbsp;<code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>web_flask/7-states_list.py, web_flask/templates/7-states_list.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. Cities by states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>You must use&nbsp;<code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or&nbsp;<code>DBStorage</code>) =&gt;&nbsp;<code>from models import storage</code> and&nbsp;<code>storage.all(...)</code></li>
                <li>To load all cities of a&nbsp;<code>State</code>:<ul>
                        <li>If your storage engine is&nbsp;<code>DBStorage</code>, you must use&nbsp;<code>cities</code> relationship</li>
                        <li>Otherwise, use the public getter method&nbsp;<code>cities</code></li>
                    </ul>
                </li>
                <li>After each request you must remove the current SQLAlchemy Session:<ul>
                        <li>Declare a method to handle&nbsp;<code>@app.teardown_appcontext</code></li>
                        <li>Call in this method&nbsp;<code>storage.close()</code></li>
                    </ul>
                </li>
                <li>Routes:<ul>
                        <li><code>/cities_by_states</code>: display a HTML page: (inside the tag&nbsp;<code>BODY</code>)<ul>
                                <li><code>H1</code> tag: &ldquo;States&rdquo;</li>
                                <li><code>UL</code> tag: with the list of all&nbsp;<code>State</code> objects present in&nbsp;<code>DBStorage</code> <strong>sorted by&nbsp;<code>name</code></strong> (A-&gt;Z)&nbsp;<a href="https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>
                                    <ul>
                                        <li><code>LI</code> tag: description of one&nbsp;<code>State</code>:&nbsp;<code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code> +&nbsp;<code>UL</code> tag: with the list of&nbsp;<code>City</code> objects linked to the&nbsp;<code>State</code> <strong>sorted by&nbsp;<code>name</code></strong> (A-&gt;Z)<ul>
                                                <li><code>LI</code> tag: description of one&nbsp;<code>City</code>:&nbsp;<code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>Import this&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
            </ul>
            <p><strong>IMPORTANT</strong></p>
            <ul>
                <li>Make sure you have a running and valid&nbsp;<code>setup_mysql_dev.sql</code> in your&nbsp;<code>AirBnB_clone_v2</code> repository (<a href="https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
                <li>Make sure all tables are created when you run&nbsp;<code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Akron&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Babbie&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Calera&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Fairfield&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Douglas&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Kearny&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Tempe&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Fremont&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Napa&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Francisco&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Jose&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Sonoma&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Denver&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Miami&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Orlando&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Honolulu&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Kailua&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Pearl city&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Baton rouge&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Lafayette&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;New Orleans&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Saint Paul&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Jackson&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Meridian&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Tupelo&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Eugene&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Portland&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=895bb9d962f91c96c989b697b06f7475a465295e9ab82b7fa08c08ecbaafc870" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. States and State</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>You must use&nbsp;<code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or&nbsp;<code>DBStorage</code>) =&gt;&nbsp;<code>from models import storage</code> and&nbsp;<code>storage.all(...)</code></li>
                <li>To load all cities of a&nbsp;<code>State</code>:<ul>
                        <li>If your storage engine is&nbsp;<code>DBStorage</code>, you must use&nbsp;<code>cities</code> relationship</li>
                        <li>Otherwise, use the public getter method&nbsp;<code>cities</code></li>
                    </ul>
                </li>
                <li>After each request you must remove the current SQLAlchemy Session:<ul>
                        <li>Declare a method to handle&nbsp;<code>@app.teardown_appcontext</code></li>
                        <li>Call in this method&nbsp;<code>storage.close()</code></li>
                    </ul>
                </li>
                <li>Routes:<ul>
                        <li><code>/states</code>: display a HTML page: (inside the tag&nbsp;<code>BODY</code>)<ul>
                                <li><code>H1</code> tag: &ldquo;States&rdquo;</li>
                                <li><code>UL</code> tag: with the list of all&nbsp;<code>State</code> objects present in&nbsp;<code>DBStorage</code> <strong>sorted by&nbsp;<code>name</code></strong> (A-&gt;Z)&nbsp;<a href="https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ" title="tip" target="_blank">tip</a>
                                    <ul>
                                        <li><code>LI</code> tag: description of one&nbsp;<code>State</code>:&nbsp;<code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag&nbsp;<code>BODY</code>)<ul>
                                <li>If a&nbsp;<code>State</code> object is found with this&nbsp;<code>id</code>:<ul>
                                        <li><code>H1</code> tag: &ldquo;State:&nbsp;&rdquo;</li>
                                        <li><code>H3</code> tag: &ldquo;Cities:&rdquo;</li>
                                        <li><code>UL</code> tag: with the list of&nbsp;<code>City</code> objects linked to the&nbsp;<code>State</code> <strong>sorted by&nbsp;<code>name</code></strong> (A-&gt;Z)<ul>
                                                <li><code>LI</code> tag: description of one&nbsp;<code>City</code>:&nbsp;<code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                                <li>Otherwise:<ul>
                                        <li><code>H1</code> tag: &ldquo;Not found!&rdquo;</li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
                <li>Import this&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
            </ul>
            <p><strong>IMPORTANT</strong></p>
            <ul>
                <li>Make sure you have a running and valid&nbsp;<code>setup_mysql_dev.sql</code> in your&nbsp;<code>AirBnB_clone_v2</code> repository (<a href="https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
                <li>Make sure all tables are created when you run&nbsp;<code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In another tab:</p>
            <pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;State: Illinois&lt;/H1&gt;
        &lt;H3&gt;Cities:&lt;/H3&gt;
        &lt;UL&gt;
                &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;
        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo &quot;&quot;
&lt;!DOCTYPE html&gt;
&lt;HTML lang=&quot;en&quot;&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;Not found!&lt;/H1&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>web_flask/9-states.py, web_flask/templates/9-states.html</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>11. HBNB filters</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>You must use&nbsp;<code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or&nbsp;<code>DBStorage</code>) =&gt;&nbsp;<code>from models import storage</code> and&nbsp;<code>storage.all(...)</code></li>
                <li>To load all cities of a&nbsp;<code>State</code>:<ul>
                        <li>If your storage engine is&nbsp;<code>DBStorage</code>, you must use&nbsp;<code>cities</code> relationship</li>
                        <li>Otherwise, use the public getter method&nbsp;<code>cities</code></li>
                    </ul>
                </li>
                <li>After each request you must remove the current SQLAlchemy Session:<ul>
                        <li>Declare a method to handle&nbsp;<code>@app.teardown_appcontext</code></li>
                        <li>Call in this method&nbsp;<code>storage.close()</code></li>
                    </ul>
                </li>
                <li>Routes:<ul>
                        <li><code>/hbnb_filters</code>: display a HTML page like&nbsp;<code>6-index.html</code>, which was done during the project&nbsp;<a href="https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a>
                            <ul>
                                <li>Copy files&nbsp;<code>3-footer.css</code>,&nbsp;<code>3-header.css</code>,&nbsp;<code>4-common.css</code> and&nbsp;<code>6-filters.css</code> from&nbsp;<code>web_static/styles/</code> to the folder&nbsp;<code>web_flask/static/styles</code></li>
                                <li>Copy files&nbsp;<code>icon.png</code> and&nbsp;<code>logo.png</code> from&nbsp;<code>web_static/images/</code> to the folder&nbsp;<code>web_flask/static/images</code></li>
                                <li>Update&nbsp;<code>.popover</code> class in&nbsp;<code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
                                <li>Use&nbsp;<code>6-index.html</code> content as source code for the template&nbsp;<code>10-hbnb_filters.html</code>:<ul>
                                        <li>Replace the content of the&nbsp;<code>H4</code> tag under each filter title (<code>H3</code> States and&nbsp;<code>H3</code> Amenities) by&nbsp;<code>&amp;nbsp;</code></li>
                                    </ul>
                                </li>
                                <li><code>State</code>,&nbsp;<code>City</code> and&nbsp;<code>Amenity</code> objects must be loaded from&nbsp;<code>DBStorage</code> and&nbsp;<strong>sorted by name</strong> (A-&gt;Z)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
                <li>Import this&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql" title="10-dump" target="_blank">10-dump</a> to have some data</li>
            </ul>
            <p><strong>IMPORTANT</strong></p>
            <ul>
                <li>Make sure you have a running and valid&nbsp;<code>setup_mysql_dev.sql</code> in your&nbsp;<code>AirBnB_clone_v2</code> repository (<a href="https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
                <li>Make sure all tables are created when you run&nbsp;<code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 10-dump.sql &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 10-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In the browser:</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4f993ec8ca2a2f639a80887667106ac63a0a3701.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=de2282160d16c6c61561dcabdc40a42234f8dea34eed0fb995d4f1f8f7f89e58" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1549b553d726cc37f64440be910cb6b858aa32ae.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a1efdfde8751391d6ed330233d8872599de7e4ce0809266cc231a90776e85093" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/94b3a416ba1551c59701eb6672ac0a36fbebba14.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5ae1d9959c2af4afbed0cccb3e7106605cb6c76bd6aec8af51b70301d249e838" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/1e559707dd34a37564dc10e54b707815a516d363.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d6e3599669929698b4466349b1a4acf46ef8cbb63afc0a61059c33c1d5f5b737" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>12. HBNB is alive!</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write a script that starts a Flask web application:</p>
            <ul>
                <li>Your web application must be listening on&nbsp;<code>0.0.0.0</code>, port&nbsp;<code>5000</code></li>
                <li>You must use&nbsp;<code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or&nbsp;<code>DBStorage</code>) =&gt;&nbsp;<code>from models import storage</code> and&nbsp;<code>storage.all(...)</code></li>
                <li>To load all cities of a&nbsp;<code>State</code>:<ul>
                        <li>If your storage engine is&nbsp;<code>DBStorage</code>, you must use&nbsp;<code>cities</code> relationship</li>
                        <li>Otherwise, use the public getter method&nbsp;<code>cities</code></li>
                    </ul>
                </li>
                <li>After each request you must remove the current SQLAlchemy Session:<ul>
                        <li>Declare a method to handle&nbsp;<code>@app.teardown_appcontext</code></li>
                        <li>Call in this method&nbsp;<code>storage.close()</code></li>
                    </ul>
                </li>
                <li>Routes:<ul>
                        <li><code>/hbnb</code>: display a HTML page like&nbsp;<code>8-index.html</code>, done during the&nbsp;<a href="https://intranet.alxswe.com/rltoken/EG-iGbr_iPTlHrQQSNho1g" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a> project<ul>
                                <li>Copy files&nbsp;<code>3-footer.css</code>,&nbsp;<code>3-header.css</code>,&nbsp;<code>4-common.css</code>,&nbsp;<code>6-filters.css</code> and&nbsp;<code>8-places.css</code> from&nbsp;<code>web_static/styles/</code> to the folder&nbsp;<code>web_flask/static/styles</code></li>
                                <li>Copy all files from&nbsp;<code>web_static/images/</code> to the folder&nbsp;<code>web_flask/static/images</code></li>
                                <li>Update&nbsp;<code>.popover</code> class in&nbsp;<code>6-filters.css</code> to enable scrolling in the popover and set max height to 300 pixels.</li>
                                <li>Update&nbsp;<code>8-places.css</code> to always have the price by night on the top right of each place element, and the name correctly aligned and visible (i.e. screenshots below)</li>
                                <li>Use&nbsp;<code>8-index.html</code> content as source code for the template&nbsp;<code>100-hbnb.html</code>:<ul>
                                        <li>Replace the content of the&nbsp;<code>H4</code> tag under each filter title (<code>H3</code> States and&nbsp;<code>H3</code> Amenities) by&nbsp;<code>&amp;nbsp;</code></li>
                                        <li>Make sure all HTML tags from objects are correctly used (example:&nbsp;<code>&lt;BR /&gt;</code> must generate a new line)</li>
                                    </ul>
                                </li>
                                <li><code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Amenity</code> and&nbsp;<code>Place</code> objects must be loaded from&nbsp;<code>DBStorage</code> and&nbsp;<strong>sorted by name</strong> (A-&gt;Z)</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li>You must use the option&nbsp;<code>strict_slashes=False</code> in your route definition</li>
                <li>Import this&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql" title="100-dump" target="_blank">100-dump</a> to have some data</li>
            </ul>
            <p><strong>IMPORTANT</strong></p>
            <ul>
                <li>Make sure you have a running and valid&nbsp;<code>setup_mysql_dev.sql</code> in your&nbsp;<code>AirBnB_clone_v2</code> repository (<a href="https://intranet.alxswe.com/rltoken/v5CSUMU7FY9wj_cnBY7P1A" title="Task" target="_blank">Task</a>)</li>
                <li>Make sure all tables are created when you run&nbsp;<code>echo &quot;quit&quot; | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 100-dump.sql &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql&quot;
guillaume@ubuntu:~/AirBnB_v2$ cat 100-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.100-hbnb
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>
            <p>In the browser:</p>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/396ae10c9f85a6128ae40e1b63f4bce95adf411c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8d6c6ff90eb6596966389449ed98db23ce18c7120dd74f226bfa1895735986b1" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/9eb21499b5f3b59751fdbf561174e2f259d97482.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ff90cad6be6d0d51a520f9e2d051d2430f8433fed6b90fea0f62ad182e70c1fb" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/bf248a63c15a746ad694acffdd56d80281782c71.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d9d0061d2825fc09e523db02796c6a74e45a5c127b1a0a109ecc869c31389eb0" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/494317aad058a649a51f416eceee1a609f07c6c0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aa5adee13b1adc3722c6bee116f2f5ff811f434ffaab9f047fd3145e47143758" alt="">&nbsp;<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/016911388aa92532e06c4d5361188a2622425517.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230723%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230723T113721Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c6a80a319a2d9450c61671749c4dcf25404dd6a46f2b789a976c162b8e91b56" alt=""></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>AirBnB_clone_v2</code></li>
                    <li>File:&nbsp;<code>web_flask/100-hbnb.py, web_flask/templates/100-hbnb.html, web_flask/static/</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>
