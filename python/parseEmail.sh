#!/bin/bash

emailAddress=$1

# Specify paths
pathToEmail='/home/harry'
savePath='/home/harry/moodProject'

# identify sender
echo "year, month, day, dayOfWeek, rating, comments" > "${savePath}/${emailAddress}_MoodRatings.csv"


for email in `ls ${pathToEmail}/mail/new`; do
#for email in 1640270542.M293276P1560Q0Ra532027150de6cd4.raspberrypi; do
	echo $email
	
	sender1=`cat ${pathToEmail}/mail/new/$email | grep "From:"`
	sender2=`echo $sender1 | awk '{split($0,a,"<"); print a[2]}'`
	sender3=`echo $sender2 | awk '{split($0,a,">"); print a[1]}'`
	echo "sender is " $sender3
	
	saveFile='${emailAddress}_MoodRatings.csv'

	#echo $saveFile
	
	containsStandardSubjectTemplate=`cat ~/mail/new/$email | grep -c "Subject: Re: Please rate your mood from today on a scale of 0-10."`
	
	subject=`cat ~/mail/new/$email | grep "Subject:"`
	echo $subject

	containsJanuaryException=`echo $subject | grep -ci "January"`

	
		echo $email
	
	# if containsStandardSubjectTemplate is 1, then we have the standard response. unpack it
	if [ $containsStandardSubjectTemplate -eq 1 ] ; then
		
		# figure out the date
		dateLine=`cat ~/mail/new/$email | grep -n "<hgmoodproject2020@gmail.com> wrote:"`
		date=`echo $dateLine | awk '{split($0, a, " "); print a[2]; print a[3]; print a[4]; print a[5]}'`
		dayOfWeek=`echo $dateLine | awk '{split($0, a, " "); print a[2]}'`
		dayOfWeek=`echo "${dayOfWeek//,}"`
		month=`echo $dateLine | awk '{split($0, a, " "); print a[3]}'`
		month=`echo "${month//,}"`
		dayOfMonth=`echo $dateLine | awk '{split($0, a, " "); print a[4]}'`
		dayOfMonth=`echo "${dayOfMonth//,}"`
		year=`echo $dateLine | awk '{split($0, a, " "); print a[5]}'`
		year=`echo "${year//,}"`

		#echo "date is: $dayOfWeek $month $dayOfMonth $year"
		
		# figure out the message content
		beginContentLine=`cat ~/mail/new/$email | grep -n "Content-Type: text/plain;" | awk '{split($0, a, ":"); print a[1]}'`
		beginContentLine=$((beginContentLine + 2))
		endContentLine=`cat ~/mail/new/$email | grep -n "<hgmoodproject2020@gmail.com> wrote:" | awk '{split($0, a, ":"); print a[1]}'`
		endContentLine=$((endContentLine - 1))
		content=`sed -n "${beginContentLine},${endContentLine}p" ~/mail/new/$email` 
		
		## grab rating
		# grab all numbers in content
		rating=`echo "$content" | tr '\n' ' ' | sed -e 's/[^0-9.]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' '`
		# grab the first one in case there is more than one number
		rating=`echo "${rating%% *}"`
		lastCharacterOfRating=`echo "${rating: -1}"`
		if [ $lastCharacterOfRating = . ]; then
			rating=`echo $rating | rev | cut -c 2- | rev`
		fi
		
		#echo "Rating is: $rating"
		
		# grab any other text
		contentWithoutRating=`printf '%s\n' "${content#*$rating}"`
		if [ -z "$contentWithoutRating" ]; then
			contentWithoutRatings='']
		else
		# if the first character is a period, remove it
			firstCharacterAfterRating="${contentWithoutRating:0:1}"
			if [ $firstCharacterAfterRating = . ]; then
				contentWithoutRating="${contentWithoutRating:1}"
			fi
		fi
		
		# remove any leading white space
		contentWithoutRating=`echo $contentWithoutRating | sed -e 's/^[ \t]*//'`
		#echo "Content is: $contentWithoutRating"
		
		if [ $sender3 = $emailAddress ]; then
			echo -e "${year}\t${month}\t${dayOfMonth}\t$dayOfWeek\t$rating\t$contentWithoutRating" >> "${savePath}/${emailAddress}_MoodRatings.csv"
			echo "i made it here"
		fi
		
	elif [ $containsJanuaryException -eq 1 ] ; then
		month='Jan'
		dayOfMonth=`echo "$subject" | tr '\n' ' ' | sed -e 's/[^0-9.]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' '`
		date="01-0${dayOfMonth}-2020"
		dayOfWeek=`date -j -f '%m-%d-%Y' $date +'%A'`
		dayOfWeek=${dayOfWeek:0:2}
		
		
			# figure out the message content
		beginContentLine=`cat ~/mail/new/$email | grep -n "Content-Type: text/plain;" | awk '{split($0, a, ":"); print a[1]}'`
		beginContentLine=$((beginContentLine + 2))
		endContentLine=`cat ~/mail/new/$email | grep -n "Content-Type: text/plain;" | awk '{split($0, a, ":"); print a[2]}'`
		endContentLine=$((endContentLine - 0))
		content=`sed -n "${beginContentLine},${endContentLine}p" ~/mail/new/$email` 
			
		
		## grab rating
		# grab all numbers in content
		rating=`echo "$content" | tr '\n' ' ' | sed -e 's/[^0-9.]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' '`
		# grab the first one in case there is more than one number
		rating=`echo "${rating%% *}"`
		lastCharacterOfRating=`echo "${rating: -1}"`
		if [ $lastCharacterOfRating = . ]; then
			rating=`echo $rating | rev | cut -c 2- | rev`
		fi
		
	
		# grab any other text
		contentWithoutRating=`printf '%s\n' "${content#*$rating}"`
		if [ -z "$contentWithoutRating" ]; then
			contentWithoutRatings='']
		else
		# if the first character is a period, remove it
			firstCharacterAfterRating="${contentWithoutRating:0:1}"
			if [ $firstCharacterAfterRating = . ]; then
				contentWithoutRating="${contentWithoutRating:1}"
			fi
		fi
		
		# remove any leading white space
		contentWithoutRating=`echo $contentWithoutRating | sed -e 's/^[ \t]*//'`
		echo "Content is: $contentWithoutRating"
		if [ $sender3 = $emailAddress ]; then

			echo -e "${year}\t${month}\t${dayOfMonth}\t$dayOfWeek\t$rating\t$contentWithoutRating" >> "${savePath}/${emailAddress}_MoodRatings.csv"
		fi
	else
		# see if the subject is a date
		subject=`echo $subject | awk '{split($0,a,"Subject:"); print a[2]}'`
		echo "we think the date is $subject"
		if date -d "$subject"; then
			echo "whoa boy, doing something cray"
			dayOfWeek=$(date -d "$subject" '+%a')

			month=$(date -d "$subject" '+%b')

			dayOfMonth=$(date -d "$subject" '+%d')
			dayOfMonth=$(echo $dayOfMonth | sed 's/^0*//')

			year=$(date -d "$subject" '+%Y')

# figure out the message content
		beginContentLine=`cat ~/mail/new/$email | grep  -n "<div dir" | awk '{split($0, a, ":"); print a[1]}'`
		endContentLine=$beginContentLine
echo "endcontnetline is $beginContentLine"
		#content=`cat ~/mail/new/$email | grep -n "<div dir="auto">" | awk '{split($0, a, "</div>"); print a[0]}'`		
#beginContentLine=$((beginContentLine + 2))
		#endContentLine=`cat ~/mail/new/$email | grep -n "<hgmoodproject2020@gmail.com> wrote:" | awk '{split($0, a, ":"); print a[1]}'`
		#endContentLine=$((endContentLine - 1))
		content=`sed -n "${beginContentLine},${endContentLine}p" ~/mail/new/$email` 
		echo $content		

		## grab rating
		# grab all numbers in content
		rating=`echo "$content" | tr '\n' ' ' | sed -e 's/[^0-9.]/ /g' -e 's/^ *//g' -e 's/ *$//g' | tr -s ' '`
		# grab the first one in case there is more than one number
		rating=`echo "${rating%% *}"`
		lastCharacterOfRating=`echo "${rating: -1}"`
		if [ $lastCharacterOfRating = . ]; then
			rating=`echo $rating | rev | cut -c 2- | rev`
		fi
		
		#echo "Rating is: $rating"
		
		# grab any other text
		contentWithoutRating=`printf '%s\n' "${content#*$rating}"`
		if [ -z "$contentWithoutRating" ]; then
			contentWithoutRatings='']
		else
		# if the first character is a period, remove it
			firstCharacterAfterRating="${contentWithoutRating:0:1}"
			if [ $firstCharacterAfterRating = . ]; then
				contentWithoutRating="${contentWithoutRating:1}"
			fi
		fi
		
		# remove any leading white space
		contentWithoutRating=`echo $contentWithoutRating | sed -e 's/^[ \t]*//'`
		contentWithoutRating=`echo $contentWithoutRating | awk '{split($0, a, "</div>"); print a[1]}'`
		#echo "Content is: $contentWithoutRating"
		
		if [ $sender3 = $emailAddress ]; then
			echo -e "${year}\t${month}\t${dayOfMonth}\t$dayOfWeek\t$rating\t$contentWithoutRating" >> "${savePath}/${emailAddress}_MoodRatings.csv"
			echo "i made it here"
		fi


		fi

	fi
	


done

#for x in 1 2; do

#	if [ $x = 1 ]; then
#		saveFile="/home/harry/harryMoodRatings.csv"
#	elif [ $x = 2 ]; then
#		saveFile="/home/harry/geenaMoodRatings.csv"
#	fi

	
	awk '!a[$0]++' ${savePath}/${emailAddress}_MoodRatings.csv > cleanedMoodRatings.csv
	
	tail -n +2 cleanedMoodRatings.csv > cleanedMoodRatingsWithoutHeader.csv
	
	echo "month, day, dayOfWeek, rating, comments"  > ${savePath}/${emailAddress}_MoodRatings.csv
	sort -k 1M -k 2 cleanedMoodRatingsWithoutHeader.csv >> ${savePath}/${emailAddress}_MoodRatings.csv
	
	rm cleanedMoodRatings.csv
	
	rm cleanedMoodRatingsWithoutHeader.csv

#done

