from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Settings(models.Model):
    """
    Modelo para armazenar as configurações do site. 
    Este é um modelo Singleton, o que significa que só pode haver uma instância dele.
    """
    # Personal Information
    name = models.CharField(_("Nome"), max_length=50)
    email = models.EmailField(_("Email"), max_length=50)
    birthday = models.DateField(_("Data de Nascimento"))
    website = models.CharField(_("Website"), max_length=50)
    phone = models.CharField(_("Telefone"), max_length=50)
    city = models.CharField(_("Cidade"), max_length=50)
    education = models.CharField(_("Educação"), max_length=50)
    freelance = models.BooleanField(_("Freelance"))
    # Page Texts
    about = models.TextField(_("Sobre"))
    facts = models.TextField(_("Fatos"))
    skills = models.TextField(_("Habilidades"))
    resume = models.TextField(_("Resumo"))
    portfolio = models.TextField(_("Portfólio"))
    services = models.TextField(_("Serviços"))
    testimonials = models.TextField(_("Testemunhos"))
    contact = models.TextField(_("Contato"))

    def save(self, *args, **kwargs):
        if Settings.objects.exists() and not self.pk:
            raise ValidationError(_('Já existe uma instância de configurações. Edite a instância existente.'))
        return super(Settings, self).save(*args, **kwargs)

    def __str__(self):
        return _('Configurações do Site')
    
    class Meta:
        verbose_name = _('Configuração do Site')
        verbose_name_plural = _('Configurações do Site')


class SocialMedia(models.Model):
    """
    Modelo para armazenar as redes sociais do proprietário do site.
    """
    platform = models.CharField(_("Plataforma"), max_length=50)
    link = models.CharField(_("Link"), max_length=50)

    def getIcon(self):
        platforms = [
            'alexa', 'behance', 'discord', 'dribbble', 'facebook', 'github', 'gitlab', 'google', 'instagram', 'line', 'linkedin', 'mastodon', 'medium', 'messenger', 'microsoft-teams', 'opencollective', 'paypal', 'pinterest', 'quora', 'reddit', 'signal', 'sina-weibo', 'skype', 'slack', 'snapchat', 'sourceforge', 'spotify', 'stack-overflow', 'strava', 'substack', 'telegram', 'tencent-qq', 'threads', 'threads-fill', 'tiktok', 'twitch', 'twitter', 'twitter-x', 'vimeo', 'wechat', 'whatsapp', 'wordpress', 'yelp', 'youtube'
        ]

        if self.platform.lower() in platforms:
            return self.platform.lower()
        else:
            return 'link'
    
    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name = _('Rede Social')
        verbose_name_plural = _('Redes Sociais')


class Education(models.Model):
    """
    Modelo para armazenar a formação educacional do proprietário do site.
    """
    name = models.CharField(_("Nome"), max_length=50)
    start_year = models.IntegerField(_("Ano de Início"))
    end_year = models.IntegerField(_("Ano de Conclusão"), blank=True, null=True)
    present = models.BooleanField(_("Atualmente"), default=False)
    institute = models.CharField(_("Instituição"), max_length=50)
    description = models.TextField(_("Descrição"))

    def save(self, *args, **kwargs):
        if (self.end_year is None and self.present is False) or (self.end_year and self.present is True):
            raise ValidationError(_('Ou o ano de conclusão é preenchido ou o campo "Atualmente" deve ser marcado.'))
        elif self.start_year > self.end_year:
            raise ValidationError(_('O ano de início não pode ser maior que o ano de conclusão.'))
        return super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Formação')
        verbose_name_plural = _('Formações')

    
class Experience(models.Model):
    """
    Modelo para armazenar a experiência profissional do proprietário do site.
    """
    name = models.CharField(_("Nome"), max_length=50)
    start_year = models.IntegerField(_("Ano de Início"))
    end_year = models.IntegerField(_("Ano de Conclusão"), blank=True, null=True)
    present = models.BooleanField(_("Atualmente"), default=False)
    company = models.CharField(_("Empresa"), max_length=50)
    description = models.TextField(_("Descrição"))

    def save(self, *args, **kwargs):
        if (self.end_year is None and self.present is False) or (self.end_year and self.present is True):
            raise ValidationError(_('Ou o ano de conclusão é preenchido ou o campo "Atualmente" deve ser marcado.'))
        elif self.start_year > self.end_year:
            raise ValidationError(_('O ano de início não pode ser maior que o ano de conclusão.'))
        return super(Experience, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Experiência')
        verbose_name_plural = _('Experiências')


class Skill(models.Model):
    """
    Modelo para armazenar as habilidades do proprietário do site.
    """
    name = models.CharField(_("Nome"), max_length=50)
    percentage = models.PositiveSmallIntegerField(
        _("Porcentagem"), 
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Habilidade')
        verbose_name_plural = _('Habilidades')


class Portfolio(models.Model):
    """
    Modelo para armazenar os projetos do portfólio do proprietário do site.
    """
    name = models.CharField(_("Nome"), max_length=50)
    image = models.ImageField(_("Imagem"), upload_to='portfolio')
    description = models.TextField(_("Descrição"))
    category = models.CharField(_("Categoria"), max_length=50)
    link = models.CharField(_("Link"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Portfólio')
        verbose_name_plural = _('Portfólio')


class Testimonial(models.Model):
    """
    Modelo para armazenar os depoimentos sobre o proprietário do site.
    """
    image = models.ImageField(_("Imagem"), upload_to='images/testimonials')
    name = models.CharField(_("Nome"), max_length=50)
    description = models.TextField(_("Descrição"))
    testimonial = models.TextField(_("Testemunho"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Testemunho')
        verbose_name_plural = _('Testemunhos')


class Message(models.Model):
    """
    Modelo para armazenar as mensagens enviadas através do formulário de contato do site.
    """
    name = models.CharField(_("Nome"), max_length=50)
    email = models.EmailField(_("Email"), max_length=50)
    subject = models.CharField(_("Assunto"), max_length=50)
    message = models.TextField(_("Mensagem"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Mensagem')
        verbose_name_plural = _('Mensagens')