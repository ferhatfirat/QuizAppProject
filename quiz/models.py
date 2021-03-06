from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def quiz_count(self):
        return self.quiz_set.count()

class Quiz(models.Model):
    title = models.CharField(max_length=50, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Quizzes"
        
    def question_count(self):
        return self.question_set.count()
        
class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
        

class Question(Update):
    SCALE = (
        (1, "Beginner"),
        (2, "Intermediate"),
        (3, "Advanced")
    )
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="Question")
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    answer_text = models.CharField(max_length=300)
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer_text
    
    
    
    