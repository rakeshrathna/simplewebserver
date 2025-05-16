# EX01 Developing a Simple Webserver
## Date:13/05/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIMPLE WEBSERVER</title>
    <style>
        *{
            margin: 0px;
            padding: 0px
        }
        .Navbar h1{
            background-color: #003366;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .c1{
            background-color: #f0f4f8;
            margin: 20px auto;
            padding: 20px;
            border-radius: 10px;
            width: 80%;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            font-family: 'Segoe UI', sans-serif;
        }
        .un{
            list-style-type: square;
            margin-left: 20px;
            padding-top: 10px;
            color: #333;
        }
        .c1:hover{
            transform: translateY(-10px);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        }

    </style>

    
</head>
<body>
    <div class="Navbar">
        <h1>TCP/IP PROTOCOL</h1>

    </div>
    <div class="c1">
        <h2>APPLICATION LAYER</h2>
        <ul class="un">
            <li>HTTP</li>
            <li>FTP</li>
            <li>SMTP</li>
            <li>DNS</li>
            <li>TELNET</li>
            <li>SSH</li>

        </ul>
    </div>
    <div class="c1">
        <h2>TRANSPORT LAYER</h2>
        <ul class="un">
            <li>TCP (Transmission Control Protocol)</li>
            <li>UDP (User Datagram Protocol)</li>
        </ul>
    </div>
    <div class="c1">
        <h2>INTERNT LAYER</h2>
        <Ul class="un">
            <li>IP (Internet Protocol)</li>
            <li>ICMP (Internet Control Message Protocol)</li>
            <li>ARP (Address Resolution Protocol)</li>
            <li>IGMP (Internet Group Management Protocol)</li>

        </Ul>
    </div>
    <div class="c1">
        <h2>NETWORK ACCESS LAYER</h2>
        <ul class="un">
            <li>Ethernet</li>
            <li>Wi-Fi</li>
            <li>PPP (Point-to-Point Protocol)</li>
        </ul>
    </div>


    
</body>
</html>
~~~





## OUTPUT:

![Screenshot 2025-05-10 223353](https://github.com/user-attachments/assets/b05dc462-0d05-44f6-b978-e1e66c1d2320)


## RESULT:
The program for implementing simple webserver is executed successfully.
