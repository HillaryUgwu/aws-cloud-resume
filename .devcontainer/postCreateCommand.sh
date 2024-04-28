#!/usr/bin/bash
cd $CODESPACE_VSCODE_FOLDER/..
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
cd $CODESPACE_VSCODE_FOLDER

npm install --global --no-fund http-server
