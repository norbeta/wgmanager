from django.contrib import admin
from wgconfig import wgexec as wg 

# Register your models here.
from .models import Group, Peer, Key
from .forms import CustomKeyForm, CreateKeyForm

admin.site.register(Group)
admin.site.register(Peer)
@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ("group", "peer", "master", "publickey", "ip4", "ip6", "modified")
    list_filter = ("group", )
    #search_fields = ("group", "peer", "ip4", "ip6",)
    form = CustomKeyForm
    add_form = CreateKeyForm

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
            defaults.update(kwargs)
            return super().get_form(request, obj, **defaults)
        else:
            defaults['form'] = self.form
            defaults.update(kwargs)
            formset = super().get_form(request, obj, **defaults)
            if obj.master is True:
                group = Group.objects.get(name=obj.group)
                config = '# Config for ' + str(obj.group) + ':' + str(obj.peer) + '\n[Interface]\n'
                config += 'PrivateKey = '
                config += str(obj.privatekey)
                config += '\nAddress = ' + str(obj.ip4) + '/' + str(group.mask4) + ', ' + str(obj.ip6) + '/' + str(group.mask6) + '\n'
                config += 'ListenPort = 51820\n\n'
                peers = Key.objects.filter(group=obj.group).exclude(peer=obj.peer)
                for l in peers:
                    config += '# Peer: ' + str(l.peer) + '\n[Peer]\nPublicKey = ' + str(l.publickey) + '\nAllowedIPs = ' + str(l.ip4) + '/32, ' + str(l.ip6) + '/128\n\n'
            else:
                config = '# Config for ' + str(obj.group) + ':' + str(obj.peer) + '\n[Interface]\n'
                config += 'PrivateKey = '
                config += str(obj.privatekey)
                config += '\nAddress = ' + str(obj.ip4) + '/32, ' + str(obj.ip6) + '/128 \n\n'
                try:
                    peer = Key.objects.get(group=obj.group,master=True)
                    group = Group.objects.get(name=peer.group)
                    config += '# ' + str(obj.group) + ':Master\n[Peer]\nPublicKey = ' + str(peer.publickey) + '\nEndpoint = ' + str(group.endpoint) + '\nAllowedIPs = ' + str(group.net4) + '/' + str(group.mask4) + ', ' + str(group.net6) + '/' + str(group.mask6) + '\n'
                except Key.DoesNotExist:
                    config += '# No endpoint configured. Check group settings for endpoint details\n'
                    
            formset.base_fields['configField'].initial = config
            formset.base_fields['configField'].required = False
            return formset

    def get_changeform_initial_data(self, request):
        keys = wg.generate_keypair()
        return {'privatekey': keys[0], 'publickey': keys[1]}
