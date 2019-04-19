from googlevoice import Voice
voice = Voice()
voice.login(YOUR_USERNAME,YOUR_PASSWORD)# you must enter your username and password #
truckers = [[]] 

msgArray = ["Hello ", ", we are contacting you about the resume you posted online indicating you are looking for job as a professional driver.  We are hiring for dedicated routes from Chicago to Los Angeles - 100% guarantee no-touch freight.  We have multiple spots we need to fill.  If you are still looking for a job, contact us!  Call us at this number or apply online at www.mycdlapp.com/sltg/002 , or email me - jeff@sltruckinggroup.com.  We look forward to hearing from you!"]
numbers_dialed = 0
for i in truckers[0:10]:
	name = str(i[0].split(" ")[1]).title()
	msg = msgArray[0]+name+msgArray[1]
	if r"(\d*)" in i[1]:
		voice.send_sms(i[1], msg)
		numbers_dialed = numbers_dialed +1

print "numbers dialed "+ str(numbers_dialed)

# California_job_board_msg = " I saw your resume on the the California job board and wanted to reach out to you about a job opening.  We are looking for class A drivers with good attitudes.  Our drivers average $5,000 a month with 2 days at home each week.  Call me back if you are interested!"
# # for i in names:
# # 	print i.split()[0]

