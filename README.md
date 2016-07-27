# Summer 2016 video streaming project
CS4390 – Socket Programming: Video Streaming with RTSP and RTP

Configuration:

1. Put all video streaming code files in same folder path
2. Install Python (2.7.12) and pip (package manager)
3. Navigate to folder path 
4. Start server:

	python Server.py serverPort
	
	For example: python Server.py 2000

5. Run ClientLauncher.py: 

	python ClientLauncher.py a b c d
		a. hostServer - name or IP address
		b. serverPort
		c. rtpPort - default is 554 but set >1024
		d. videoClip (.Mjpeg)

	For example: python ClientLauncher.py 127.0.0.1 2000 6000 movie.Mjpeg

