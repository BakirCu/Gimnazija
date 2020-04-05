from urllib.parse import urlsplit, parse_qsl
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def embed_video(link):

    video_id = dict(parse_qsl(urlsplit(link).query))

    if video_id:
        return 'https://www.youtube.com/embed/' + video_id['v']
    elif urlsplit(link).netloc == 'youtu.be':
        return 'https://www.youtube.com/embed' + urlsplit(link).path
    else:
        raise ValidationError(
            _("Niste dobro iskopirali lik"))
