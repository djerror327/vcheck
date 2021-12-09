# Create your models here.


class Version:
    def __init__(self, instance_id, release_version, installed_version):
        self.installed_version = installed_version
        self.release_version = release_version
        self.instance_id = instance_id
