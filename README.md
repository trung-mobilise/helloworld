# Setting up Hello World on AWS Elastic Beanstalk
	Pip install awsebcli –upgrade --user
	eb init -p python-3.8 hello-world –-region eu-west-2
	eb create hello-world-dev
	eb deploy
	eb open hello-world-dev
