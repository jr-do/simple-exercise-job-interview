# simple-exercise-job-interview
Simple exercise given for a job interview
1) Create random test log data.

   log data should be delimited with "|"(pipe) and 10,000 lines with 500 bytes
   
   each line and contain following format with random data.
   
      date|time|pid|status|data|comment
	  
      range of each column:
	  
      date    : 20130101
	  
      time    : 09:00:00-11:59:59
	  
      pid     : 3000-5000
	  
      status  : OK || TEMP || PERM
	  
      data    : refer words/sentences used in whichever of the following
                pages and set them randomly.
                https://en.wikipedia.org/wiki/Amazon_S3
				
      comment : fill in with "X" to fit one line as 500 bytes.
	  
   (Example) random test log data would be like below:
   
20120101|09:00:00|4887|TEMP|Amazon S3 (Simple Storage Service) is an online file storage web service offered by Amazon Web Services. Amazon S3 provides storage through web services interfaces (REST, SOAP, and BitTorrent).[1] Amazon launched S3, its first publicly available web service, in the United States in March 2006[2] and in Europe in November 2007.[3]|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
20120101|09:00:00|4418|TEMP|At its inception, Amazon charged end users US$0.15 per gigabyte-month, with additional charges for bandwidth used in sending and receiving data, and a per-request (get or put) charge.[4] On November 1, 2008, pricing moved to tiers where end users storing more than 50 terabytes receive discounted pricing.[5] Amazon says that S3 uses the same scalable storage infrastructure that Amazon.com uses to run its own global e-commerce network.|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
20120101|09:00:01|4124|PERM|Amazon S3 is reported to store more than 2 trillion objects as of April 2013.[7] This is up from 102 billion objects as of March 2010,[8] 64 billion objects in August 2009,[9] 52 billion in March 2009,[10] 29 billion in October 2008,[5] 14 billion in January 2008, and 10 billion in October 2007.[11]|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
20120101|09:00:02|3977|OK|S3 uses include web hosting, image hosting, and storage for backup systems. S3 guarantees 99.9% monthly uptime service-level agreement (SLA),[12] that is, not more than 43 minutes of downtime per month.[13]|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
20120101|09:00:02|4020|OK|Details of S3's design are not made public by Amazon, though it clearly manages data with an object storage architecture. According to Amazon, S3's design aims to provide scalability, high availability, and low latency at commodity costs.|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   -> Please send compressed log and the script you used to created it.
   
2) Create a graph to show number of status per minute so that you can easier to
   understand how many "OK" were in this minute, how many "TEMP" were in this
   minute and so on.
   -> Please send graph file and also intermediate file (eg. csv format file)
      used to create the graph and also the script if used to create intermediate
      file. Excel graph is acceptable.
	  
3) (If you have time for extra points) Create the top 10 used words list in
   data column.
   -> Please send the result with script you used to created it.
