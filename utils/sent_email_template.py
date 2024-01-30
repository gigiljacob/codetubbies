from django.core.mail import EmailMultiAlternatives

from core import settings


def send_email(subject, to, html_template, from_mail=None, text_content=None):
    from_email = from_mail if from_mail else settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_template, "text/html")
    msg.send()
