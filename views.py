from django.shortcuts import render, redirect

def submit(request):
    """
    Handles processing the submitted mock exam data.
    """
    if request.method == 'POST':
        # Insert your score calculation logic here
        # Example: request.session['score'] = calculation_result
        return redirect('show_exam_result')
    
    return render(request, 'exam_form.html')

def show_exam_result(request):
    """
    Displays the results page featuring a congratulations message and score.
    """
    # Fetching values (placeholder example logic)
    score = request.session.get('score', 100) 
    
    context = {
        'score': score,
        'message': "Congratulations! You successfully completed the mock exam."
    }
    return render(request, 'exam_result.html', context)
