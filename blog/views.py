from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm

from blog.models import Article
from blog.models import Comment

def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]
    
    return render(request, 'blog/accueil.html', locals())


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            
            # ajouter la relation avec l'article
            comment = Comment()
            comment.pseudo = form.cleaned_data['pseudo']
            comment.email = form.cleaned_data['email']
            comment.contenu = form.cleaned_data['contenu']
            comment.article = article
            
            comment.save()
            
            renvoi = True 
    else:
            form = CommentForm()

    return render(request, 'blog/lire_article.html', locals())
