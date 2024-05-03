from django import forms
from portfolio_app.models import PortfolioItem

class portfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ["title","category"]
        widget = {
            'image' : forms.FileInput(),
            'category' : forms.ChoiceField()
        }