# -*- mode: ruby -*-
# vi: set ft=ruby :
# vi: set nu :

PROJECT_NAME = "zodb_fight"

Vagrant.configure(2) do |config|
  sourcecode_dir = './sourcecode'
  config.vm.synced_folder sourcecode_dir, "/home/vagrant/sourcecode/"

  # Lecture examples
  config.vm.define PROJECT_NAME, primary: true do |zodb|
    zodb.ssh.port = 22
    zodb.ssh.username = 'vagrant'
    zodb.ssh.password = '123'
    zodb.vm.provider 'docker' do |docker|
      docker.build_dir = './vagrant-data'
      docker.name = PROJECT_NAME
      docker.build_args = ['--tag=uralbash/zodb']
      docker.remains_running = false

      docker.link('%s_db_mongodb:mongodb' % PROJECT_NAME)

      # -t - Allocate a (pseudo) tty
      # -i - Keep stdin open (so we can interact with it)
      docker.create_args = ['-i', '-t']
      docker.has_ssh = true
    end
  end

  # MongoDB
  config.vm.define 'mongodb' do |mongodb|
    mongodb.vm.provider 'docker' do |docker|
      docker.image = "dockerfile/mongodb"
      docker.name = '%s_db_mongodb' % PROJECT_NAME
      docker.ports = ["28017:28017"]
    end
  end
end
