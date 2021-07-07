#AWS-IoT-Data-Publisher

This is a code script I made for an IoT project that I am the lead for. This script shovels the data collected by your IoT sensors/gateways onto an
AWS IoT core endpoint. This code is meant to be ran on your IoT gateway by ssh into the gateway and activating this code. Requirements for this code
is that you will need to pip install the following:

    pip install AWSIoTPythonSDK 
    pip install paho-mqtt

You will also need to modify the code with your own access keys and AWS CA certificate which you can make at https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html