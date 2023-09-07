#!/usr/bin/bash
cd ..
brew install aws/tap/aws-sam-cli
sam --version
cd $CODESPACE_VSCODE_FOLDER