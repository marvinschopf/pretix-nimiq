"""

pretix-nimiq
Copyright 2021 Marvin Schopf

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

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

    def execute_payment(request, payment):
        paymentId = payment.id
        return None
