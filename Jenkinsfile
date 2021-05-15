#!/usr/bin/env groovy

def remote = [:]
remote.name = "vServer"
remote.host = "144.91.86.28"
remote.allowAnyHosts = true

node {
    stage("Update source files") {
        echo 'Updating source files...'
        sshCommand remote: remote, command: 'sudo /bin/systemctl stop gainersite'
        sshCommand remote: remote, command: 'cd /home/deploy/gainerSite'
        sshCommand remote: remote, command: '/usr/bin/git pull'
        sshCommand remote: remote, command: 'sudo /bin/systemctl start gainersite'
    }
}