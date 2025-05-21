from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
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
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()