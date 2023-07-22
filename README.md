# CloudO

# Vscode setting.json
```
{
    "workbench.colorTheme": "Predawn",
    "workbench.iconTheme": "ayu",
    "python.defaultInterpreterPath": "/usr/bin/python3",
    "python.formatting.provider": "black",
    "workbench.editor.highlightModifiedTabs": true,
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "code-runner.executorMap": {
        "python": "$pythonPath -u $fullFileName"
    },
    "code-runner.clearPreviousOutput": true,
    "code-runner.showExecutionMessage": false,
    "code-runner.ignoreSelection": true,
    "code-runner.saveFileBeforeRun": true,
    "editor.quickSuggestionsDelay": 100,
    "zenMode.centerLayout": false,
    "zenMode.fullScreen": false,
    "zenMode.hideLineNumbers": false,
    "zenMode.hideTabs": false,
    "editor.minimap.enabled": false,
    "workbench.settings.openDefaultSettings": true,
    "workbench.settings.editor": "json",
    "workbench.settings.useSplitJSON": true,
    "workbench.statusBar.feedback.visible": false,
    "workbench.startupEditor": "newUntitledFile",
    "[python]": {
        "editor.formatOnType": true
    }
}
```

# Installing the AWS SAM CLI on Linux
1. Download the [AWS SAM CLI .zip](https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip) file to a directory of your choice.
2. Unzip the installation files into a directory of your choice. The following is an example, using the sam-installation subdirectory.
```
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
```
3. Install the AWS SAM CLI by running the install executable. This executable is located in the directory used in the previous step. The following is an example, using the sam-installation subdirectory:
```
$ sudo ./sam-installation/install
```

4. Verify the installation.
```
$ sam --version
```
On successful installation, you should see output like the following:
```
 SAM CLI, version 1.58.0
```