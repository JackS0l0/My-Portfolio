from articles.models import Articles,Categories
def common_data():
    return {
        'categories':Categories.objects.all().order_by('name'),
        'advertLeftBox':Articles.objects.all().order_by('-date')[0:1],
        'advertRightTopBox':Articles.objects.all().order_by('-date')[1:2],
        'advertRightBottomLeftBox':Articles.objects.all().order_by('-date')[2:3],
        'advertRightBottomRightBox':Articles.objects.all().order_by('-date')[3:4],
        'advertTrends':Articles.objects.all().order_by('-date')[0:5],
    }