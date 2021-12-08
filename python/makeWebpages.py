def makeWebpages(email, years, savePath):

	# Make the user specific index, AKA the page we land on after logging in
	f = open("{}/index_{}.php".format(savePath, email), 'w')
	
	
	f.write("<?php\n") 
	f.write("session_start();\n")

	f.write("    include('connection.php');\n")
	f.write("    include('functions.php');\n")

	f.write("    $user_data = check_login($con);\n")

	f.write("?>\n")

	f.write("<!DOCTYPE html>\n")
	f.write("<html>\n")
	f.write("<head>\n")
	f.write("        <title>The Mood Project</title>\n")
	f.write("</head>\n")
	f.write("<body>\n")

	f.write("        <a href='logout.php'>Logout</a>\n")
	f.write("        <h1>The Mood Project</h1>\n")

	f.write("        <br>\n")
	f.write("		Visualize:\n")
	for year in years:
		f.write("		<p><a href='{}_{}.php'>{}</a></p>\n".format(email, year, year))
	f.write("</body>\n")
	f.write("</html>\n")
	f.close()
	

