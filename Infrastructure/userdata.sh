#!/bin/bash
apt update
apt install -y apache2

# Install the AWS CLI
#apt install -y awscli

cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
  <title>Hello World</title>
  <style>
    body {
    background-color: #0b192e; 
    text-align: center
    }
    h1 {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        display: inline-flex;
    }
  </style>
</head>
<body>
  <h1>Hello World!(i1)</h1>
</body>
</html>
EOF

# Start Apache and enable it on boot
systemctl start apache2
systemctl enable apache2