from django.test import TestCase

import datetime
from django.utils import timezone
from ..models import Question
from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        # method should return false for future dated questions.
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_question(self):
        # method should return false for past dated questions.
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        past_question = Question(pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_with_current_question(self):
        # should return True for current question
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        current_question = Question(pub_date=time)
        self.assertIs(current_question.was_published_recently(), True)
