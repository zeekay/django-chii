from django.conf import settings

def core(request):
    return {
        'site_name': settings.SITE_NAME,
        'static_url': settings.STATIC_URL,
        'irc_channel': settings.IRC_CHANNEL,
        'irc_channel_link': settings.IRC_CHANNEL_LINK,
    }
