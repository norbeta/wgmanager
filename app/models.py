from django.db import models
from wgconfig import wgexec as wg

# Create your models here.

NETMASK4 = [
        (24, '/24'), 
        (25, '/25'), 
        (26, '/26'), 
        (27, '/27'), 
        (28, '/28'), 
        (29, '/29'), 
        (30, '/30'), 
]

NETMASK6 = [
        (64, '/64'),
]

class Group(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    net4 = models.GenericIPAddressField(protocol='ipv4', blank=True, null=True)
    mask4 = models.IntegerField(choices=NETMASK4,default=24)
    net6 = models.GenericIPAddressField(protocol='ipv6', blank=True, null=True)
    mask6 = models.IntegerField(choices=NETMASK6,default=64)
    endpoint = models.CharField(max_length=128,default='host:port')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = str(self.name)
        return name

class Peer(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = str(self.name)
        return name

class Key(models.Model):
    peer = models.ForeignKey(Peer, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    privatekey = models.CharField(max_length=44)
    publickey = models.CharField(max_length=44)
    master = models.BooleanField(default=False)
    ip4 = models.GenericIPAddressField(protocol='ipv4', blank=True, null=True)
    ip6 = models.GenericIPAddressField(protocol='ipv6', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = str(self.group) + ':' + str(self.peer)
        return name

    class Meta:
        constraints = [
                models.UniqueConstraint(
                    fields = ['peer', 'group'], 
                    name = 'unique_peer_per_group'
                ),
                models.UniqueConstraint(
                    fields = ['group', 'ip4'], 
                    name = 'unique_ip4_per_group'
                ), 
                models.UniqueConstraint(
                    fields = ['group', 'ip6'], 
                    name = 'unique_ip6_per_group'
                )
            ]


