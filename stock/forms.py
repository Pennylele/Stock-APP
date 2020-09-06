from django import forms


class TickerForm(forms.Form):
	ticker = forms.CharField(label="Ticker Symbol", max_length=10)