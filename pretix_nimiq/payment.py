from django import forms
from django.utils.translation import gettext_lazy as _
from pretix.base.models import OrderPayment, OrderRefund
from pretix.base.payment import BasePaymentProvider, PaymentException
from collections import OrderedDict


class Nimiq(BasePaymentProvider):
    identifier = "nimiq"
    verbose_name = _("Nimiq")
    public_name = _("Nimiq")

    @property
    def settings_form_fields(self):
        return OrderedDict(
            list(super().settings_form_fields.items())
            + [
                (
                    "nimiq_address",
                    forms.CharField(
                        widget=forms.Textarea,
                        label=_("Nimiq wallet address"),
                        required=True,
                    ),
                )
            ]
        )
