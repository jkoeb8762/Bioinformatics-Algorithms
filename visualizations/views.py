from django.shortcuts import render

def home_view(request):
    return render(request, 'visualizations/home.html')

def pattern_count_view(request):
    return render(request, 'visualizations/patternCount.html')

def frequent_words_with_mismatches_view(request):
    return render(request, 'visualizations/frequentWordsWithMismatches.html')

def gibbs_sampler_view(request):
    return render(request, 'visualizations/gibbsSampler.html')

def de_bruijn_graph_view(request):
    return render(request, 'visualizations/deBruijnGraph.html')