from django.contrib import admin

from .models import Article, Categorie, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date', 'is_visible', )
    list_filter = ('categorie', )
    search_fields = ('titre', 'auteur', )

    prepopulated_fields = {'slug': ('titre', )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'article', 'date', 'description', 'is_visible')
    list_filter = ('article', 'pseudo', )
    search_fields = ('pseudo', 'article__titre',)
    
    def description(self, comment):
        """Retourne les 40 premiers caractères du commentaires"""
        text = comment.contenu[0:40]
        if len(comment.contenu) > 40:
            return '%s...' % text
        else:
            return text
    
    # Ajout du champ description à la place de contenu
    description.short_description = 'description'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Categorie)