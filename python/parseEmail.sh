#!/bin/bash

# identify sender
echo "year, month, day, dayOfWeek, rating, comments" > ~/harryMoodRatings.csv
echo "year, month, day, dayOfWeek, rating, comments"  > ~/geenaMoodRatings.csv


for email in `ls ~/mail/new`; do
	#echo $email
	sender=`cat ~/mail/new/$email | grep "From:"`
	sender=`echo $sender | awk '{split($0,a,": "); print a[2]}'`
	sender=`echo $sender | awk '{split($0,a," "); print a[1]}'`
	#echo $sender
	if [ $sender = Harrison ]; then
		saveFile='harryMoodRatings.csv'
	elif [ $sender = Geena ]; then
		saveFile='geenaMoodRatings.csv'
	fi
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
		
		echo -e "${year}\t${month}\t${dayOfMonth}\t$dayOfWeek\t$rating\t$contentWithoutRating" >> "/home/harry/$saveFile"

		
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
		echo -e "${year}\t${month}\t${dayOfMonth}\t$dayOfWeek\t$rating\t$contentWithoutRating" >> "/home/harry/$saveFile"

	fi
	


done

for x in 1 2; do

	if [ $x = 1 ]; then
		saveFile="/home/harry/harryMoodRatings.csv"
	elif [ $x = 2 ]; then
		saveFile="/home/harry/geenaMoodRatings.csv"
	fi

	
	awk '!a[$0]++' $saveFile > cleanedMoodRatings.csv
	
	tail -n +2 cleanedMoodRatings.csv > cleanedMoodRatingsWithoutHeader.csv
	
	echo "month, day, dayOfWeek, rating, comments"  > $saveFile
	sort -k 1M -k 2 cleanedMoodRatingsWithoutHeader.csv >> $saveFile
	
	rm cleanedMoodRatings.csv
	
	rm cleanedMoodRatingsWithoutHeader.csv

done


