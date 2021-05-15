#!/usr/bin/env groovy

def remote = [:]
remote.name = "vServer"
remote.host = "144.91.86.28"
remote.allowAnyHosts = true

node {
    withCredentials([sshUserPrivateKey(credentialsId: 'liveServer', keyFileVariable: 'keyFile', passphraseVariable: 'passPhrase', usernameVariable: 'userName')]) {
        remote.user = userName
        remote.passphrase = passPhrase
        remote.identityFile = keyFile

        stage("Update source files") {
            echo 'Updating source files...'
            sshCommand remote: remote, command: 'sudo /bin/systemctl stop gainersite'
            sshCommand remote: remote, command: '/usr/bin/git -C /home/deploy/gainerSite pull'
            sshCommand remote: remote, command: 'sudo /bin/systemctl start gainersite'
        }
    }
}