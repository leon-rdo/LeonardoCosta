from home.models import Settings, SocialMedia

def context_processors(request):
    settings = Settings.objects.first()
    social_media = SocialMedia.objects.all()
    return {'settings': settings, 'social_media': social_media}
