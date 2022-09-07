def makeWebpages(email, years, savePath):
    # Make the user specific index, AKA the page we land on after logging in
    f = open("{}/index_{}.php".format(savePath, email), 'w')

    location = 'post-signin'
    f = makeHeader(f, email, location)

    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("        <title>The Mood Project</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")

    f.write("<div class='w3-row-padding w3-padding-64 w3-container'>\n")
    f.write("<div class='w3-content'>\n")
    f.write("<center>\n")
    f.write("<h1>Visualize</h1>\n")
    f.write("<h5 class='w3-padding-1'>\n")
    for year in years:
        f.write("		<p><a href='{}_{}.php'>{}</a></p>\n".format(email, year, year))
    f.write("<h1>Analyze</h1>\n")

    f.write("<p><a href='custom.php'>Compare Keywords</a></p>\n")
    f.write("</center>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()


def makeHeader(f, email, location):
    f.write("<?php\n")
    f.write("session_start();\n")
    f.write("include('connection.php');\n")
    f.write("include('functions.php');\n")
    f.write("$user_data = check_login($con);\n")

    f.write("$value =  $_POST['subject']\n")

    f.write("?>\n")

    f.write("<!DOCTYPE html>\n")
    f.write("<html lang='en''>\n")
    f.write("<title>THE MOOD PROJECT</title>\n")
    f.write("<meta charset='UTF-8'>\n")
    f.write("<meta name='viewport' content='width=device-width, initial-scale=1''>\n")
    f.write("<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>\n")
    f.write("<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Lato'>\n")
    f.write("<link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Montserrat'>\n")
    f.write(
        "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>\n")
    f.write("<style>\n")
    f.write("body,h1,h2,h3,h4,h5,h6 {font-family: 'Lato'', sans-serif}\n")
    f.write(".w3-bar,h1,button {font-family: 'Montserrat', sans-serif}\n")
    f.write(".fa-anchor,.fa-coffee {font-size:200px}\n")
    f.write("</style>\n")
    f.write("<body>\n")

    f.write("<!-- !PAGE CONTENT! -->\n")
    f.write("<div class='w3-top'>\n")
    f.write("  <div class='w3-bar w3-black w3-card w3-left-align w3-large''>\n")
    f.write(
        "    <a class='w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-black' href='javascript:void(0);' onclick='myFunction()' title='Toggle Navigation Menu'><i class='fa fa-bars'></i></a>\n")
    f.write("    <a href='../index.html'' class='w3-bar-item w3-button w3-padding-large w3-black'>\n")
    f.write("       <img src='../logo2.png' height=20px>\n")
    f.write("       THE MOOD PROJECT\n")
    f.write("</a>\n")

    f.write(
        "<a href='login.php' class='w3-bar-item w3-button w3-hide-small w3-padding-large w3-right w3-hover-white w3-black'>Log Out</a>\n")

    f.write("</div>\n")

    f.write("  <!-- Navbar on small screens -->\n")
    f.write("  <div id='navDemo' class='w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large''>\n")
    f.write("    <a href='login/login.php' class='w3-bar-item w3-button w3-padding-large'>Log Out</a>\n")
    f.write("  </div>\n")
    f.write("</div>\n")

    return f


