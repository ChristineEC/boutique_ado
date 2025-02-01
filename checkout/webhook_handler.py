from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webbook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event['type']}',
            status=200)

    def handle_payment_event_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webbook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200)
        
    def handle_payment_event_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webbook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200)